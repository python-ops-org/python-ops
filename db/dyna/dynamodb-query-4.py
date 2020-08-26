import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('library')

def lambda_handler(event, context):
    response = table.scan()
    data = response['Items']
    return "\n".join(data)
