import boto3
from boto3.dynamodb.conditions import Attr


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('library')

def lambda_handler(event, context):
    #With filter
    response = table.scan(FilterExpression=Attr('author').eq('doyel'))
    data = response['Items']
    
    #Without filter
    response = table.scan()
    data.update(response['Items'])
    
    return "\n".join([str(value) for value in data])

#def lambda_handler(event, context):
#    response = table.scan()
#    data = response['Items']
#    return "\n".join([str(value) for value in data])
