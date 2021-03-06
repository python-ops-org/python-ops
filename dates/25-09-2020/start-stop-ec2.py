
##python start-stop-ec2.py -p start -u https://u2gxjtmno6.execute-api.us-east-1.amazonaws.com/prod/service 
##python start-stop-ec2.py -p stop -u https://u2gxjtmno6.execute-api.us-east-1.amazonaws.com/prod/service



#python ec2.py -a lambda -s start
#python ec2.py  -a lambda -s stop




import boto3
import requests
import datetime
import sys
import json
import csv
import argparse
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

log_file = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M") + "-start_stop.log"
'''
regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3',
           'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1',
           'ap-southeast-2', 'ap-south-1', 'sa-east-1']
'''

def sendLogFileEmail(log_data, log_data_csv):
	message = MIMEMultipart()
	message['Subject'] = log_file
	message['From'] = 'chakraborty.rock@gmail.com'
	message['To'] = 'sudipta1436@gmail.com'
	message.preamble = 'Multipart message.\n'
	message.attach(MIMEText('status of service'))
	part = MIMEApplication(log_data)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % log_file)
	partcsv = MIMEApplication(log_data_csv)
	log_file_csv = log_file.replace(".log", ".csv")
	partcsv.add_header('Content-Disposition', f'attachment; filename="{log_file_csv}"')
	#message.attach(part)
	message.attach(partcsv)
	client = boto3.client('ses')
	client.send_raw_email (
		Source='chakraborty.rock@gmail.com',
		Destinations=['sudipta1436@gmail.com'],
		RawMessage={'Data': message.as_string()}
	)
	#print "E-mail sent: " + str(response)

def arrayToString(x):
	return ", ".join(x)


def getInstancesRegion(region, state):
	client = boto3.client('ec2', region)
	instances = client.describe_instances(
		Filters=[
			{
				'Name': 'instance-state-name',
				'Values': [state]
			},
		]
	)
	try:
		return [instance["InstanceId"] for reservation in instances["Reservations"] for instance in reservation["Instances"]]
	except:
		return []



def lambda_handler(event, context):
	command = event["command"]
	regions = event["regions"]
	#log_bucket = event["log-bucket"]
	#instances = event["instances"]
	#s3 = boto3.resource('s3')
	
	log_data = ""
	log_data_csv = "regions, instance_id, status\n"
    ###printing start time

	if command.lower() == "started":
		log_data = log_data + "Start command started at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
		print("Start command started at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

		## looping regions from list

		for region in regions:
			instances_region = getInstancesRegion(region, "running")
			if instances_region == []:
				continue
			# start instances
			client = boto3.client('ec2', region)
			client.start_instances(InstanceIds=instances_region)
			for instance in instances_region:
				log_data_csv += f"{region}, {instance}, started\n"
			log_data = log_data + "Started instances in region "  + region + ": " + arrayToString(instances_region) + "\n"
			print("Started instances in region "  + region + ": " + arrayToString(instances_region) + "\n")

		log_data = log_data + "Start command finished at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
		print("Start command finished at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

	elif command.lower() == "stopped":
		log_data = log_data + "Stop command started at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
		print("Stop command started at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
		for region in regions:
			instances_region = getInstancesRegion(region, "stopped")
			if instances_region == []:
				continue
			client = boto3.client('ec2', region)
			client.stop_instances(InstanceIds=instances_region)
			for instance in instances_region:
				log_data_csv += f"{region}, {instance}, stopped\n"
			log_data = log_data + "Stopped instances in region "  + region + ": " + arrayToString(instances_region) + "\n"
			print("Stopped instances in region "  + region + ": " + arrayToString(instances_region) + "\n")

		log_data = log_data + "Stop command finished at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
		print("Stop command finished at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

	else:
		log_data = log_data + "Command " + command + " not mapped."
		print("Command " + command + " not mapped.")

	sendLogFileEmail(log_data, log_data_csv)
	return {"success": True, "message": "OK"}


def main():
	if len(sys.argv) == 2:
		file_name = sys.argv[1]
		json_file = json.loads(open(file_name, "rb").read())
		lambda_handler(json_file, None)
	else:
		parser = argparse.ArgumentParser()
		#parser.add_argument("file", type=str, help="File name of JSON file")
		parser.add_argument("-a", dest="command",  required=False, type=str, help="Command")
		parser.add_argument("-r", dest="region",  required=False, type=str, help="Region")
		parser.add_argument("-s", dest="start",   required=False, type=str, help="Receive this parameter to start")
		parser.add_argument("-k", dest="stop",   required=False, type=str, help="Receive this parameter to stop")
		args = parser.parse_args()

		json_file = {}
		if args.start is not None:
			json_file["command"] = "start"
			json_file["regions"] = [args.region]
		elif args.stop is not None:
			json_file["command"] = "stop"
			json_file["regions"] = [args.region]
			lambda_handler(json_file, None)


if __name__ == '__main__':
	main()

##python ec2.py -p start
##python ec2.py -q stop

