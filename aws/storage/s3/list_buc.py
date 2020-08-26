#https://analyticshut.com/list-s3-buckets-using-python-aws-cli/
import boto3
from botocore.exceptions import ClientError

#s3 = boto3.client('s3')
#print(s3)


"""
response = s3.list_buckets()['Buckets']
print(response)
for bucket in response:
    #print('Bucket name: {}'.format(bucket['Name']))
    print(bucket['Name'])
"""
s3 = boto3.resource('s3')
response = s3.buckets.all()
for bucket in response:
    print(bucket)

