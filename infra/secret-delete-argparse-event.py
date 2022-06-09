from datetime import datetime
import subprocess 
import csv
import argparse
import json
import re
import os

#start_function
def del_secret(js_file):
     #js_file = os.environ['json_file']
     data = json.load(open(js_file,"r"))
     for secret in data["secrets"]:
         json_body='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}'
         cmd1 = "kubectl get secrets -o jsonpath='%s'"%json_body
         c1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE)
         c1.wait()
         out = c1.communicate()
         data = out[0].decode("utf-8")
         secrets = []
         for i in data.split("}")[:-1]:
             _secret = i.split(secret["year"])[0]
             if secret["secret_name"] in _secret:
                 secrets.append(_secret)
                 print(_secret+" "+secret["year"])
         #print(data_json)
         for _secret in secrets:
              print(_secret)

         if secret["proceed"] == "true":
             for _secret in secrets:
                 cmd2 = "kubectl delete secret %s"%_secret
                 c2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE)
                 c2.wait()
                 out = c2.communicate()
                 data = out[0].decode("utf-8")
                 print(data)
         else:
                 print("delete aborted.")
                 continue


#os.environ['json_file'] = 'sec.json'
parser = argparse.ArgumentParser()
parser.add_argument("-f",required=True)
args = parser.parse_args()
del_secret(args.f)
