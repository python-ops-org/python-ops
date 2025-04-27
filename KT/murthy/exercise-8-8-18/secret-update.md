
```
import boto3
import json
import random
import string

# Initialize Secrets Manager client
client = boto3.client('secretsmanager')

# Define the secret name and existing username
secret_name = 'ag-key'
existing_username = 'user123'  # Keep your existing username here

def generate_random_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def rotate_secret(secret_name):
    try:
        # Retrieve the current secret value
        response = client.get_secret_value(SecretId=secret_name)
        
        # Parse the current secret value
        if 'SecretString' in response:
            secret_string = response['SecretString']
            secret = json.loads(secret_string)
        else:
            secret = json.loads(response['SecretBinary'])

        # Generate a new random password
        new_password = generate_random_password()

        # Update the secret with the existing username and new password
        secret['username'] = existing_username
        secret['password'] = new_password

        # Update the secret in Secrets Manager
        client.update_secret(
            SecretId=secret_name,
            SecretString=json.dumps(secret)
        )

        print(f"Successfully updated secret '{secret_name}' with new password.")
        print(f"New Password: {new_password}")
    
    except Exception as e:
        print(f"Error updating secret: {e}")

def lambda_handler(event, context):
    """
    AWS Lambda function handler to rotate the secret in Secrets Manager.
    """
    rotate_secret(secret_name)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Secret '{secret_name}' updated successfully.")
    }


```
