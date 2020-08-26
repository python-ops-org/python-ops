#/usr/bin/python2.7 gcp-sa-1.py -a connector-svc-02@connector-2-250114.iam.gserviceaccount.com -k connector-3.json
import argparse
import os
import base64
import json,requests
from google.oauth2 import service_account
import googleapiclient.discovery




def create_key(service_account_email,keyfile):
    """Creates a key for a service account."""
    credentials = service_account.Credentials.from_service_account_file(keyfile)
#    print(credentials)
    
    service = googleapiclient.discovery.build(
        'iam', 'v1', credentials=credentials)
#    print(service)
    
    
    body = {
            # TODO: Add desired entries to the request body.
            "keyAlgorithm": "KEY_ALG_RSA_2048",
            "privateKeyType": "TYPE_GOOGLE_CREDENTIALS_FILE"
    }


    key = service.projects().serviceAccounts().keys().create(
        name='projects/-/serviceAccounts/' + service_account_email, body=body
        ).execute()

    my_json = base64.b64decode(key['privateKeyData']).decode('utf8')
    k = json.loads(my_json)
    print(k)
    with open("cred.json", 'w') as f:
        json.dump(k, f, indent=2)
    print('Created key: ' + key['name'])
    

parser = argparse.ArgumentParser()
parser.add_argument("-a")
parser.add_argument("-k")

args = parser.parse_args()
#print (args.project)
create_key(args.a,args.k)


