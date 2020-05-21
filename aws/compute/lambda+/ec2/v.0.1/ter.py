#python term.py
import boto3

def ec2_term():
    for region in ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "ap-northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-south-1", "sa-east-1"]:
        ec2 = boto3.resource("ec2", region)
        instances = ec2.instances.filter(
            Filters=[
                {"Name": "instance-state-name", "Values": ["running"]},
                {"Name": "instance-type", "Values": ["t2.micro"]}
            ]
        )
        try:
            print(f"Checking region: {region}")
            for instance in list(instances):
                instance.modify_attribute(
                    DisableApiTermination={
                        "Value": False
                    }
                )
                print(f"Region: {region} - Instance ID: {instance.id}")
                instance.terminate()
        except Exception as exception:
            print(f"Exception in region {region}: {exception}")
            continue

if __name__ == "__main__":
    ec2_term()
