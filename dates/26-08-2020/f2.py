import boto3

def ec2_control():
    ec2 = boto3.client('ec2')
    instances = ec2.instances.filter {
    Filter = [{'Name': 'instance-state-name', 'Values': ['running']}]
        }
    for i in instances:
        print(i.id)
        i.stop()
ec2_control()
