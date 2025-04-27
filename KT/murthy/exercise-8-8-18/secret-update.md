
```

import boto3
import string
import random
import os

# Initialize Secrets Manager client
secrets_client = boto3.client('secretsmanager')

# Secret Name from Lambda environment variable or hardcode it
SECRET_NAME = os.environ.get('SECRET_NAME', 'your-secret-name')

def generate_random_secret(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_secret = ''.join(random.choice(characters) for i in range(length))
    return random_secret

def lambda_handler(event, context):
    try:
        # Generate new random secret
        new_secret_value = generate_random_secret()

        # Update secret in Secrets Manager
        response = secrets_client.update_secret(
            SecretId=SECRET_NAME,
            SecretString=new_secret_value
        )

        print(f"Successfully updated secret: {SECRET_NAME}")
        return {
            'statusCode': 200,
            'body': f"Secret {SECRET_NAME} updated successfully."
        }

    except Exception as e:
        print(f"Error updating secret: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to update secret: {str(e)}"
        }


```
