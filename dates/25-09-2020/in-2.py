#python in-2.py -a lambda_start -r us-east-1 -s started

import boto3
import argparse

def ec2_control():
    parser = argparse.ArgumentParser()
    #parser.add_argument("file", type=str, help="File name of JSON file")
    parser.add_argument("-a", dest="command",  required=False, type=str, help="Command")
    parser.add_argument("-r", dest="region",  required=False, type=str, help="Region")
    parser.add_argument("-s", dest="start",   required=False, type=str, help="Receive this parameter to start")
    parser.add_argument("-k", dest="stop",   required=False, type=str, help="Receive this parameter to stop")
    args = parser.parse_args()

    if args.start and args.start != "started":
        print("Kindly parse correct key")
        return
    elif args.stop and args.stop != "stopped":
        print("Kindly parse correct key")
        return
    elif (args.command and args.command not in ["lambda_start", "lambda_stop"]) or (args.command == "lambda_start" and not args.start) or (args.command == "lambda_stop" and not args.stop):
        print("Kindly parse correct key")
        return

    ec2 = boto3.resource('ec2', args.region)


    if args.command == "lambda_stop" or args.stop is not None:
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for instance in instances:
            print(instance.id)
            instance.stop()
    elif args.command == "lambda_start" or args.start is not None:
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
        for instance in instances:
            print(instance.id)
            instance.start()

if __name__ == "__main__":
    ec2_control()
