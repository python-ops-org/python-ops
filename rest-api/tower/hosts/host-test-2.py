import csv,datetime
import json,socket
import requests
import re,time
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random



def host_list():
        addr="http://192.168.56.159"
        nex = "/api/v2/hosts/"
        tok = "UZj22SwyfG3LdUYELJlzd65f4gzFBZ"
        all_data=[]
        while True:    
            headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
            r0 = requests.get("%s%s"%(addr,nex),headers=headers)
            data = json.loads(r0.text)
            for i in range(0,len(data["results"])):
                host_name = data["results"][i]["name"]
                print(host_name)
            if str(data["next"]) == "None":
                break
            else:
                nex = str(data["next"])

host_list()         



#this is my debug script
#can you print only hostnames with pagination??








