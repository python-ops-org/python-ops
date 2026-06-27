

import boto3

VALID_REGIONS = ["us-east-1", "ap-south-1"]


def ec2_handle(action, region):
    if region not in VALID_REGIONS:
        raise ValueError(f"Invalid region: {region}")

    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]

            if action == "start" and state == "stopped":
                print(f"Starting {instance_id}")
                ec2.start_instances(InstanceIds=[instance_id])

            elif action == "stop" and state == "running":
                print(f"Stopping {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])


def lambda_handler(event, context):
    action = event.get("action")
    region = event.get("region", "ap-south-1")

    if action not in ["start", "stop"]:
        return {
            "statusCode": 400,
            "body": "Action must be 'start' or 'stop'."
        }

    ec2_handle(action, region)

    return {
        "statusCode": 200,
        "body": f"EC2 {action} completed successfully."
    }
