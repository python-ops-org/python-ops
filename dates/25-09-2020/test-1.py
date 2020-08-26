from apiclient.discovery import build
from google.oauth2 import service_account
SCOPES = ['https://www.googleapis.com/auth/youtube']
SERVICE_ACCOUNT_FILE = 'connector-3.json'
cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
print(cred)
