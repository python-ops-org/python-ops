
import argparse
# [START iam_create_key]
import os

from google.oauth2 import service_account
import googleapiclient.discovery

# [END iam_create_key]


# [START iam_create_key]
def create_key(service_account_email):
    """Creates a key for a service account."""

    credentials = service_account.Credentials.from_service_account_file(
        filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    service = googleapiclient.discovery.build(
        'iam', 'v1', credentials=credentials)

    key = service.projects().serviceAccounts().keys().create(
        name='projects/-/serviceAccounts/' + service_account_email, body={}
        ).execute()

    print('Created key: ' + key['name'])
# [END iam_create_key]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(dest='command')

    create_key_parser = subparsers.add_parser(
        'create', help=create_key.__doc__)
    create_key_parser.add_argument('service_account_email')
    args = parser.parse_args()
    if args.command == 'create':
        create_key(args.service_account_email)
