

```

import boto3
import argparse

def ec2_handle(action, region):
    # Validate region
    if region not in ['us-east-1', 'ap-south-1']:
        print(f"Invalid region: {region}")
        return

    # Create EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Describe EC2 instances
    response = ec2.describe_instances()

    # Loop through instance states and perform actions
    instance_states = response['Reservations']

    for i in instance_states:
        for j in i['Instances']:
            instance_id = j['InstanceId']
            current_state = j['State']['Name']
            
            if action == 'start' and current_state == 'stopped':
                print(f"Starting instance {instance_id} in region {region}")
                ec2.start_instances(InstanceIds=[instance_id])

if __name__ == "__main__":
    # Parse arguments for action and region
    parser = argparse.ArgumentParser(description="EC2 instance handler")
    parser.add_argument('action', choices=['start', 'stop'], help="Action to perform on the instance")
    parser.add_argument('region', help="AWS region to target")

    args = parser.parse_args()
    
    # Call the ec2_handle function
    ec2_handle(args.action, args.region)


```
