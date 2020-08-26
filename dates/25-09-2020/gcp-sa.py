#python sa-23.py -a sa -k connector-2-250114-d261c3498843.json -p connector-2-250114 -n nik-12345656 -d "dp-9" -



from pprint import pprint
import base64
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os
import json,requests
import argparse
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()



def create_service_account(projectid,accountid,displayname,keyfile):
    #credentials = GoogleCredentials.get_application_default()
    # credentials = json.load(open("gcptraining-262610-659778c4732a.json"))
    credentials = service_account.Credentials.from_service_account_file(keyfile)


    # service = service_account._JWTAccessCredentials.from_json_keyfile_dict(credentials)
    service = discovery.build('iam', 'v1', credentials=credentials)

    # Required. The resource name of the project associated with the service
    # accounts, such as `projects/my-project-123`.
    name = 'projects/{}'.format(projectid)  # TODO: Update placeholder value.

    create_service_account_request_body = {
        "accountId": "",
        "serviceAccount": {
            "displayName": ""
        }
    }
    create_service_account_request_body['accountId'] = accountid
    create_service_account_request_body['serviceAccount']['displayName'] = displayname
    request = service.projects().serviceAccounts().create(name=name, body=create_service_account_request_body)
    try:
        response = request.execute()

        # TODO: Change code below to process the `response` dict:
        #pprint(response)

        name = response['name']
        create_service_account_key_request_body = {
            # TODO: Add desired entries to the request body.
            "keyAlgorithm": "KEY_ALG_RSA_2048",
            "privateKeyType": "TYPE_GOOGLE_CREDENTIALS_FILE"
        }

        request = service.projects().serviceAccounts().keys().create(name=name,
                                                                     body=create_service_account_key_request_body)
        response = request.execute()

        # TODO: Change code below to process the `response` dict:
        #pprint(response)
        my_json = base64.b64decode(response['privateKeyData']).decode('utf8')
        key = json.loads(my_json)
        #with open("{}-{}.json".format(projectid,key['private_key_id'][:12]), 'w') as f:
        with open("credentials.json", 'w') as f:
            json.dump(key, f, indent=2)
        print ("Service Account {} has been created successfully.".format(accountid))
	#ansible_cred(projectid,new_name,envi,idd,link,token,user)
    except HttpError as err:
        # If the error is a rate limit or connection error,
        # wait and try again.
        if err.resp.get('content-type', '').startswith('application/json'):
            reason = json.loads(err.content).get('error').get('message')
            print (reason)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a")
    parser.add_argument("-k")
    parser.add_argument("-p")
    parser.add_argument("-n")
    parser.add_argument("-d")
    args = parser.parse_args()
    if (args.a is not None) and (args.a in["sa"]):
        if args.a == "sa":
            create_service_account(args.project,args.account,args.display_name,args.keyname)

        else:
            print("kindly parse correct key")
            return None

    if __name__ == "__main__":
        main()

