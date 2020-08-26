from google.oauth2 import service_account
import googleapiclient.discovery

keyfile='/opt/sa/connector-3.json'

cred = service_account.Credentials.from_service_account_file(keyfile)

print(cred)

service=googleapiclient.discovery.build('iam', 'v1', credentials=cred)

print(service)


