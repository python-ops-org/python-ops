import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('library')

response = table.query(
    KeyConditionExpression=Key('books').eq('1')
)
items = response['Items']
print(items)
