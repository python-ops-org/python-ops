import boto3
import argparse

def ec2_handler(action, region):

    if region not in ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 
                      'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 
                      'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 
                      'ap-southeast-2', 'ap-south-1', 'sa-east-1']:
        print(f"Invalid region: {region}")
        return

    try:
        # Create EC2 client for the specified region
        ec2 = boto3.client('ec2', region_name=region)

        # Get the list of instances in the region
        response = ec2.describe_instances()
        instance_states = response['Reservations']

        # Iterate over instances in the region
        for reservation in instance_states:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                current_state = instance['State']['Name']

                # Perform the desired action based on the command
                if action == 'start' and current_state == 'stopped':
                    print(f"Starting instance {instance_id} in region {region}")
                    ec2.start_instances(InstanceIds=[instance_id])
                elif action == 'stop' and current_state == 'running':
                    print(f"Stopping instance {instance_id} in region {region}")
                    ec2.stop_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage EC2 instances.')
    parser.add_argument('-a', '--action', choices=['start', 'stop'], required=True, help='Action to perform on instances (start/stop)')
    parser.add_argument('-r', '--region', required=True, help='Region of the EC2 instances')

    args = parser.parse_args()

    ec2_handler(args.action, args.region)
