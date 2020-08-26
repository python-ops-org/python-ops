#python term.py
import boto3

ACCESS_KEY = ""
SECRET_KEY = ""


session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

def ec2_term():
    client = session.client("ec2")
    response = session.describe_regions(AllRegions=True)
    for regionDict in response["Regions"]:
        region = regionDict["RegionName"]
        ec2 = session.resource("ec2", region)
        instances = ec2.instances.filter(
            Filters=[
                {"Name": "instance-state-name", "Values": ["running"]},
                {"Name": "instance-type", "Values": ["t2.micro"]}
            ]
        )
        for instance in instances:
            instance.modify_attribute(
                DisableApiTermination={
                    'Value': True
                }
            )
            print(f"Region: {region} - Instance ID: {instance.id}")
            instance.terminate()


if __name__ == "__main__":
    ec2_term()
