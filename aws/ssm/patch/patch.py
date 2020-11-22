import logging
import boto3
import datetime
import sys
import json
import csv
import argparse
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import csv
from botocore.exceptions import ClientError
from io import StringIO


CHARSET = "UTF-8"

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 
           'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 
           'ap-southeast-2', 'ap-south-1', 'sa-east-1']

log_file = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M") + "-patch.log"



def lambda_handler(event, context):
   
    print(f'event in lambda: {event}')
    print(f'instance id is: {event["i"]}')
   
    instanceId = event["i"]
    region = event["r"]
    command = event["c"]

    ses_client = boto3.client('ses', region_name=region )
    ssm = boto3.client('ssm', region_name=region)
    ec2 = boto3.resource('ec2', region_name=region)

    if instanceId == "all":
        #geet all instance id and call send_ssm
        print('all')
        ec2 = boto3.resource('ec2', region_name=region)
        for instance in ec2.instances.all():
            print(instance.id , instance.state)
            send_ssm(region , instance.id, ssm ,command)


    elif instanceId.startswith("i-"):
        send_ssm(region , instanceId, ssm ,command)
    

    else:
        raise Exception("Instance name is not in correct format.")
        

def send_email_withAttachement(region, body , instance_id , command):
    ses_client = boto3.client("ses", region_name=region)

    # Try to send the email.
    try:
        #fetching the report
        msg = MIMEMultipart('mixed')
        # Add subject, from and to lines.
        msg['Subject'] = "Status for your EC2 SSM command run: "+instance_id
    
        #Add text in message body.
        msg_body = MIMEMultipart('alternative')
        BODY_TEXT = "SSM has ran command on your ec2 server."
        textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
        # Add the text and HTML parts to the child container.
        msg_body.attach(textpart)
        msg.attach(msg_body)

        filename = 'report.csv'
        
        csv_buffer = StringIO() 
        writer = csv.writer(csv_buffer, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(['Instance_Id' , 'Command' , 'SSM Run Status'])
        writer.writerow([ instance_id , command , 'Command has been sent to EC2.' ])
          
        
        # new lines
        csv_file = MIMEText(csv_buffer.getvalue())
        attachment = csv_file.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(csv_file)


        #att.add_header('Content-Disposition','attachment',filename=filename)
        #msg.attach(att)

        # Provide the contents of the email.
        response = ses_client.send_raw_email(
            Source='chakraborty.rock@gmail.com',
		    Destinations=['sudipta1436@gmail.com'],
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

def send_ssm(region, instance_id, ssm , command ):
    #ssm = boto3.client('ssm', region_name=region)
    # query SSM for information about this instance
    filterList = [{'key': 'InstanceIds', 'valueSet': [instance_id]}]
    response = ssm.describe_instance_information(InstanceInformationFilterList=filterList, MaxResults=50)
    #logger.debug('SSM DescribeInstanceInformation response:')
    #logger.debug(response)
    print(f'response ssm: {response}')
    instanceInfo = response['InstanceInformationList'][0]
    #logger.debug('Instance information:')
    #logger.debug(instanceInfo)
    pingStatus = instanceInfo['PingStatus']
    #logger.info('SSM status of instance: ' + pingStatus)
    lastPingTime = instanceInfo['LastPingDateTime']
    #logger.debug('SSM last contact:')
    #logger.debug(lastPingTime)
    agentVersion = instanceInfo['AgentVersion']
    #logger.debug('SSM agent version: ' + agentVersion)
    platformType = instanceInfo['PlatformType']
    #logger.info('OS type: ' + platformType)
    osName = instanceInfo['PlatformName']
    #logger.info('OS name: ' + osName)
    osVersion = instanceInfo['PlatformVersion']
    #logger.info('OS version: ' + osVersion)

    # Terminate if SSM agent is offline
    if pingStatus != 'Online':
        #logger.info('SSM agent for this instance is not online: ' + pingStatus)
        return 1

    # This script only supports remediation on Linux
    if platformType != "Linux":
        #logger.info('Skipping non-Linux platform: ' + platformType)
        return 1

    # Look up the correct command to update this Linux distro
    # to-do: patch only CVEs, or patch only the specific CVE
    if osName == 'Ubuntu':
        #commandLine = "sudo apt-get update -qq -y; sudo apt-get upgrade -y"
        commandLine = command
    elif osName == 'Amazon Linux':
        commandLine = command
        #commandLine = "sudo yum update -q -y; sudo yum upgrade -y"
    else:
        #logger.info('Unsupported Linux distribution: ' + osName)
        return 1
    #logger.info('Command line to execute: ' + commandLine)

    # now we SSM run-command
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Comment='Lambda function performing updates',
        Parameters={'commands': [commandLine]}
    )

    #logger.info('SSM send-command response:')
    #logger.info(response)
    print(f'response from ssm {response}')
    #sendLogFileEmail(log_data, log_data_csv)

    send_email_withAttachement(region ,response , instance_id, command )
    return {"success": True, "message": "OK"}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Alerts and invoke SSM.')
    parser.add_argument("-i")
    parser.add_argument("-r")
    parser.add_argument("-c")
    args = parser.parse_args()
    event = {"i": args.i, "r": args.r, "c": args.c } 
    lambda_handler(event, {})

