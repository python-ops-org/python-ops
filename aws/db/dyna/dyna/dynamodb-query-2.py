import boto3
import json

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('library')

response = table.scan()
data = response['Items']
#print(data)

for i in data:
    print(i)

