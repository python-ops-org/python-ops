
from datetime import datetime
import subprocess 
import csv
import argparse
import json


#start_function
def get_hosts():
    url = "http://192.168.56.159"
    headers = "Content-Type: application/json"
    cred = "admin:password"
    command = "curl -ks -u %s -H %s %s/api/v2/inventories/4/hosts/"%(cred,headers,url)
    get_call = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
    get_call.wait()
    out = get_call.communicate()
    data = json.loads(out[0].decode("utf-8"))
    for host in data["results"]:
        host_name = host["name"]
        post_url = "%s/api/v2/inventories/6/hosts/"%url
        post_body = {"id": "", "name": "%s"%host_name,"description":"tower"}
        #post_body = post_body.replace("'",'"')
        #post_body = json.dumps(post_body_tmp)
#        print('curl -ks -u %s -X POST -H "Content-Type: application/json" -d "%s" %s'%(cred,str(post_body).replace("'",'"'),post_url))
        post_call = subprocess.Popen("curl -ks -u %s -X POST -H '%s' -d '%s' %s"%(cred,headers,str(post_body).replace("'",'"'),post_url),shell=True, stdout=subprocess.PIPE)
        post_call.wait()
        resp = post_call.communicate()
        resp_data = json.loads(resp[0].decode("utf-8"))
        print(resp_data)
get_hosts()
