#python sa-23.py -e stage -l http://192.168.10.117 -t 1K7eLFJL1XNU0nglxaqd7gk3DNTCGf -k connector-2-250114-d261c3498843.json -p connector-2-250114 -a nik-12345656 -d "dp-9" -c gcp-test-1 -i 5 



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



def create_service_account(projectid,accountid,displayname,keyfile,new_name,envi,idd,link,token,user):
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
	ansible_cred(projectid,new_name,envi,idd,link,token,user)
    except HttpError as err:
        # If the error is a rate limit or connection error,
        # wait and try again.
        if err.resp.get('content-type', '').startswith('application/json'):
            reason = json.loads(err.content).get('error').get('message')
            print (reason)


def ansible_cred(proj,name,envi,idd,url,toke,user):
    creds = open("credentials.json","r")
    tmp = json.load(creds)
    key = tmp["private_key"]
    print key
    data = {
            "name": name,
            "description": "",
            "organization": 1,
            "credential_type": 10,
            "inputs":  {
                "username": user,
                "project":  proj,
                "ssh_key_data": key,
                }
            }
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%toke}
    u1 = '%s/api/v2/credentials/%s/'%(url,idd)
    r1 = requests.put(u1,headers=headers,json=data, verify=False)
    data=json.loads(r1.text)
    dat = (str(url),str(toke),str(data))
    print(dat)


parser = argparse.ArgumentParser()
parser.add_argument("-k","--keyname", help="keyfile for authentication", required=True)
parser.add_argument("-p","--project", help="project id in GCP", required=True)
parser.add_argument("-a","--account", help="account id", required=True)
parser.add_argument("-d","--display_name", help="display name for account", required=True)
parser.add_argument("-c","--name", required=True)
parser.add_argument("-e","--env", required=True)
parser.add_argument("-i","--id", required=True)
parser.add_argument("-l","--link", required=True)
parser.add_argument("-t","--token", required=True)
parser.add_argument("-u","--user", required=True)
args = parser.parse_args()
print (args.project,args.account,args.display_name)
create_service_account(args.project,args.account,args.display_name,args.keyname,args.name,args.env,args.id,args.link,args.token,args.user)
#ansible_cred(args.project,args.name,args.env)

