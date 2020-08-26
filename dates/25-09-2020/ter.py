#python term.py
import boto3

def ec2_term():
    client = boto3.client("ec2")
    response = client.describe_regions(AllRegions=True)
    for regionDict in response["Regions"]:
        region = regionDict["RegionName"]
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
                        'Value': False
                    }
                )
                print(f"Region: {region} - Instance ID: {instance.id}")
                instance.terminate()
        except Exception as exception:
            print(f"Exception in region {region}: {exception}")
            continue

if __name__ == "__main__":
    ec2_term()
