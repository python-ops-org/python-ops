import requests
from requests.auth import HTTPBasicAuth
import json
requests.packages.urllib3.disable_warnings()



def post():
    headers = {'Content-Type': 'application/json'}
    json_body = { "r": "us-east-1", "i": "i-03ebaa1f1804edeac", "c": "free -m" }
    js = json.dumps(json_body)
    r = requests.post('url/dev', headers=headers, data=js)
    print(r.text)

post()
