from datetime import datetime
import subprocess 
import csv
import argparse
import json
import re
import os

#start_function
def del_secret():
     js_file = os.environ['json_file']
     data = json.load(open(js_file,"r"))
     for secret in data["secrets"]:
         json_body='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}'
     #print the secret with year , put a tab b/w keyword db-pass and year 2022
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
         #print the secret with out year
         for _secret in secrets:
              print(_secret)

         #make it logic with user interactive pattern "do you want to delete"?
         #if yes then it will do the delete secret step else it will exit the program
         
         #answer = input("do you want to delete: ") #this is python3 only
         #answer = raw_input("do you want to delete: ") #this is python2 only
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
     #delete the secret
     #cmd1 = "kubectl get secrets -o jsonpath=json_body | tr "}" "\n" | sed 's/2022-.*/ 2022/g' | grep -E 'db-pass' | awk '{print $1;}' | xargs -I {} kubectl delete secret {}"
     #c1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE)
    # c1.wait()
     #out = c1.communicate()
     #data = json.loads(out[0].decode("utf-8"))
    # print(%s"secret got deleted")


os.environ['json_file'] = 'sec.json'

del_secret()
