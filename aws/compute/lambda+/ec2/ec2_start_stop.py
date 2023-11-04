import boto3
import json

def lambda_handler(event, context):
    # Parse the JSON body from the Lambda event
    try:
        body = json.loads(event['body'])
        action = body.get('command')
        instances = body.get('instances', {})
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON body'})
        }

    # Initialize a list to store formatted output
    formatted_output = []

    # Iterate over the specified regions and instance IDs
    for region, instance_ids in instances.items():
        # Create an EC2 client for the region
        ec2_client = boto3.client('ec2', region_name=region)

        # Perform the action on the specified instances
        if action == 'start':
            response = ec2_client.start_instances(InstanceIds=instance_ids)
            action_description = 'starting'
        elif action == 'stop':
            response = ec2_client.stop_instances(InstanceIds=instance_ids)
            action_description = 'stopping'
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid action. Use "start" or "stop".'})
            }

        # Append formatted output
        for instance_id in instance_ids:
            formatted_output.append(f'{region} {instance_id} {action_description}')

    # Create a single string with formatted output
    response_body = '\n'.join(formatted_output)

    # Return a JSON response with the formatted output
    return {
        'statusCode': 200,
        'body': response_body
    }
