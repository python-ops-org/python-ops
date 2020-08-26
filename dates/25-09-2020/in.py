import boto3


def ec2_control():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id)
        intance.stop()
        
ec2_control()
