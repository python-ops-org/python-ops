import boto3
import argparse
import logging
import json
from botocore.exceptions import ClientError
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


logger = logging.getLogger()
logger.setLevel(logging.INFO)

inspector = boto3.client('inspector')

my_session = boto3.session.Session()


# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "chakraborty.rock@gmail.com"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "sudipta1436@gmail.com"

# The character encoding for the email.
CHARSET = "UTF-8"


def lambda_handler(event, context):
    region = my_session.region_name
    print(region)
    print("event event")
    print(event)

    message = event['Records'][0]['Sns']['Message']
    print('Event from SNS: ' + message)

    notificationType = json.loads(message)['event']
    logger.info('Inspector SNS message type: ' + notificationType)


    if notificationType != "FINDING_REPORTED":
        print('Skipping notification that is not a new finding: ' + notificationType)
        return 1

    runArn = json.loads(message)['run']
    logger.info('Run ARN: ' + runArn)

    # extract finding ARN
    findingArn = json.loads(message)['finding']
    logger.info('Finding ARN: ' + findingArn)


    # get finding and extract detail
    response = inspector.describe_findings(findingArns = [ findingArn ], locale='EN_US')
    logger.debug('Inspector DescribeFindings response:')
    logger.debug(response)
    finding = response['findings'][0]
    logger.debug('Raw finding:')
    logger.debug(finding)


    # skip uninteresting findings
    title = finding['title']
    logger.debug('Finding title: ' + title)

    if title == "Unsupported Operating System or Version":
        logger.info('Skipping finding: ' + title)
        handle_no_alert(region)
        return 1
        

    if title == "No potential security issues found":
        logger.info('Skipping finding: ' + title)
        #handle_no_alert(region)
        return 1

    service = finding['service']
    logger.debug('Service: ' + service)
    if service != "Inspector":
        logger.info('Skipping finding from service: ' + service)
        #handle_no_alert(region)
        return 1

    cveId = ""
    for attribute in finding['attributes']:
        if attribute['key'] == "CVE_ID":
            cveId = attribute['value']
            break
    logger.info('CVE ID: ' + cveId)

    if cveId == "":
        logger.info('Skipping non-CVE finding (could not find CVE ID)')
        #handle_no_alert(region)
        return 1

    assetType = finding['assetType']
    logger.debug('Asset type: ' + assetType)
    if assetType != "ec2-instance":
        logger.info('Skipping non-EC2-instance asset type: ' + assetType)
        handle_no_alert(region)
        return 1

    instanceId = finding['assetAttributes']['agentId']
    logger.info('Instance ID: ' + instanceId)
    if not instanceId.startswith("i-"):
        logger.info('Invalid instance ID: ' + instanceId)
        return 1

    handle_alert(instanceId, region , title , response , runArn)


def handle_alert(instance_id, region , mail_subject, mail_body , runArn ):
    # send mail with attachment using SES
    send_email_withAttachement(region, mail_subject, mail_body , runArn )
    # send update command
    send_ssm(instance_id, region)
    return 1


def handle_no_alert(region):
    # send mail using SES
    subject = "There is NO vulnerability issue in your ec2"
    body = "No Vulnerability issues were discoverd in your EC2"
    send_email(region, subject, body)
    return 0


def send_email_withAttachement(region, subject, body , runArn):
    ses_client = boto3.client("ses", region_name=region)

    # Try to send the email.
    try:
        #fetching the report
        reportStatus = "WORK_IN_PROGRESS"
        while(reportStatus != "COMPLETED"):
            response = inspector.get_assessment_report(
            assessmentRunArn= runArn,
            reportFileFormat='PDF',reportType='FINDING')

            reportStatus = response['status']

        reportPDFUrl = response['url']
        print(reportPDFUrl)

        msg = MIMEMultipart('mixed')
        # Add subject, from and to lines.
        msg['Subject'] = subject
        #msg['From'] = SENDER
        #msg['To'] = RECIPIENT

        #Add text in message body.
        msg_body = MIMEMultipart('alternative')
        BODY_TEXT = "There is vulnerability issue in your ec2. Please find the attched report"
        textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
        # Add the text and HTML parts to the child container.
        msg_body.attach(textpart)
        msg.attach(msg_body)

        fp = urllib.request.urlopen(reportPDFUrl)
        filename = 'myreport.pdf'
        att = MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)

        # Provide the contents of the email.
        response = ses_client.send_raw_email(
            Source=SENDER,
            Destinations=[RECIPIENT],
            RawMessage={
               'Data':msg.as_string(),
            },
          #    ConfigurationSetName=CONFIGURATION_SET
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def send_email(region, subject, body):
    ses_client = boto3.client("ses", region_name=region)
    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def send_ssm(instance_id, region):
    ssm = boto3.client('ssm', region_name=region)
    # query SSM for information about this instance
    filterList = [{'key': 'InstanceIds', 'valueSet': [instance_id]}]
    response = ssm.describe_instance_information(InstanceInformationFilterList=filterList, MaxResults=50)
    logger.debug('SSM DescribeInstanceInformation response:')
    logger.debug(response)
    instanceInfo = response['InstanceInformationList'][0]
    logger.debug('Instance information:')
    logger.debug(instanceInfo)
    pingStatus = instanceInfo['PingStatus']
    logger.info('SSM status of instance: ' + pingStatus)
    lastPingTime = instanceInfo['LastPingDateTime']
    logger.debug('SSM last contact:')
    logger.debug(lastPingTime)
    agentVersion = instanceInfo['AgentVersion']
    logger.debug('SSM agent version: ' + agentVersion)
    platformType = instanceInfo['PlatformType']
    logger.info('OS type: ' + platformType)
    osName = instanceInfo['PlatformName']
    logger.info('OS name: ' + osName)
    osVersion = instanceInfo['PlatformVersion']
    logger.info('OS version: ' + osVersion)

    # Terminate if SSM agent is offline
    if pingStatus != 'Online':
        logger.info('SSM agent for this instance is not online: ' + pingStatus)
        return 1

    # This script only supports remediation on Linux
    if platformType != "Linux":
        logger.info('Skipping non-Linux platform: ' + platformType)
        return 1

    # Look up the correct command to update this Linux distro
    # to-do: patch only CVEs, or patch only the specific CVE
    if osName == 'Ubuntu':
        commandLine = "apt-get update -qq -y; apt-get upgrade -y"
    elif osName == 'Amazon Linux':
        commandLine = "yum update -q -y; yum upgrade -y"
    else:
        logger.info('Unsupported Linux distribution: ' + osName)
        return 1
    logger.info('Command line to execute: ' + commandLine)

    # now we SSM run-command
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Comment='Lambda function performing updates',
        Parameters={'commands': [commandLine]}
    )

    logger.info('SSM send-command response:')
    logger.info(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Alerts and invoke SSM.')
    parser.add_argument("-a")
    parser.add_argument("-i")
    parser.add_argument("-r")
    args = parser.parse_args()
    event = {"a": args.a, "i": args.i, "r": args.r}
    lambda_handler(event, {})

