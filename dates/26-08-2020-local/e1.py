import boto3
import json
import csv
import argparse
import date

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3',
           'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1',
           'ap-southeast-2', 'ap-south-1', 'sa-east-1']

def ax(x):
    if x == 0:
        return x[0]
    else:
        return x[0] + "," + ax(x[1:])

def lambda_handler(event, context):
    command = event["command"]
    instances = event["instances"]
    log_data = ""
    log_data_csv = "region, instance_id, status \n"
    if command.lower == start:
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = "log_data + start started at " + dt + "\n"
        print("log_data + start started at " + dt + "\n")
        for region in regions:
            try:
                instances_region = []
            except:
                instances_region = instances[region]
                continue
            client = boto3.client('ec2', region)
            response = client.start_instances(InstanceIds=instances_region)
            for instance in instances_region:
                cv = f"{region}, {instance}, started\n"
            ld = log_data + "started in " + region + ": " ax(instances_region) + "\n"
            print("started in " + region + ": " ax(instances_region) + "\n")
        log_data = "log_data + start started at " + dt + "\n"
        print("log_data + start started at " + dt + "\n") 
