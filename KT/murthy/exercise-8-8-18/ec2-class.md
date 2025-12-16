


import boto3
import argparse


class EC2Handler:
    ALLOWED_REGIONS = ['us-east-1', 'ap-south-1']

    def __init__(self, region: str):
        if region not in self.ALLOWED_REGIONS:
            raise ValueError(f"Invalid region: {region}")

        self.region = region
        self.ec2 = boto3.client('ec2', region_name=region)

    def _get_instances(self):
        response = self.ec2.describe_instances()
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                yield instance

    def start_instances(self):
        for instance in self._get_instances():
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            if state == 'stopped':
                print(f"Starting instance {instance_id} in region {self.region}")
                self.ec2.start_instances(InstanceIds=[instance_id])

    def stop_instances(self):
        for instance in self._get_instances():
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            if state == 'running':
                print(f"Stopping instance {instance_id} in region {self.region}")
                self.ec2.stop_instances(InstanceIds=[instance_id])


def main():
    parser = argparse.ArgumentParser(description="EC2 instance handler")
    parser.add_argument(
        'action',
        choices=['start', 'stop'],
        help="Action to perform on EC2 instances"
    )
    parser.add_argument(
        'region',
        help="AWS region to target"
    )

    args = parser.parse_args()

    handler = EC2Handler(args.region)

    if args.action == 'start':
        handler.start_instances()
    elif args.action == 'stop':
        handler.stop_instances()


if __name__ == "__main__":
    main()


