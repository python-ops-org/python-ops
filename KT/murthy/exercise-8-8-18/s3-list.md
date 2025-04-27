
```
import boto3
from botocore.exceptions import ClientError

# Initialize S3 client
s3 = boto3.client('s3')

def check_bucket_security(bucket_name):
    # Check Public Access Block
    try:
        public_access_block = s3.get_public_access_block(Bucket=bucket_name)
        config = public_access_block['PublicAccessBlockConfiguration']
        public_blocked = all([
            config.get('BlockPublicAcls', False),
            config.get('IgnorePublicAcls', False),
            config.get('BlockPublicPolicy', False),
            config.get('RestrictPublicBuckets', False)
        ])
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
            public_blocked = False
        else:
            print(f"Error checking public access for {bucket_name}: {e}")
            return

    # Check Encryption
    try:
        encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        rules = encryption['ServerSideEncryptionConfiguration']['Rules']
        kms_encrypted = any(
            rule['ApplyServerSideEncryptionByDefault']['SSEAlgorithm'] == 'aws:kms'
            for rule in rules
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
            kms_encrypted = False
        else:
            print(f"Error checking encryption for {bucket_name}: {e}")
            return

    # Print result
    print(f"Bucket: {bucket_name}")
    print(f"  Public Access Blocked: {'Yes' if public_blocked else 'No'}")
    print(f"  KMS Encryption Enabled: {'Yes' if kms_encrypted else 'No'}")
    print()

def main():
    response = s3.list_buckets()
    buckets = response.get('Buckets', [])
    for bucket in buckets:
        check_bucket_security(bucket['Name'])

if __name__ == "__main__":
    main()



```
