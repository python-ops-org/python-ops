import boto3


ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for instance in instances:
        print(instance.id)
        instance.stop()

    return True
