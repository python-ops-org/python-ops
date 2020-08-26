import boto3
from boto3.dynamodb.conditions import Key, Attr




dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('library')

response = table.scan(
    FilterExpression=Attr('author').eq('doyel')
)

items = response['Items']
print(items)








