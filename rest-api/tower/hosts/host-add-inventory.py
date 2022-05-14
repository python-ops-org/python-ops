import csv,datetime
import json
import requests
import re,time
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re



def inv_add():
       cred = ("admin","password")
       url= "http://192.168.56.159"
       headers = {'Content-Type': 'application/json'}
       get_url = "%s/api/v2/inventories/4/hosts"%url
       get_call = requests.get(get_url, verify=False,headers=headers,auth=cred)
       data = json.loads(get_call.text)
       for host in data["results"]:
            host_name = host["name"]
            post_body = {"id":"","name":host_name,"description":"tower"}
            post_call = requests.post("%s/api/v2/inventories/6/hosts/"%url,json=post_body,headers=headers,auth=cred)
            print(post_call.text)
inv_add()

