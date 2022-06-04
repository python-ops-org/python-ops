from datetime import datetime
import subprocess 
import csv
import argparse
import json
import re

#start_function
def del_secret(age,name,perm):
     json_body='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}'
     #print the secret with year , put a tab b/w keyword db-pass and year 2022
     cmd1 = "kubectl get secrets -o jsonpath='%s'"%json_body
     c1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE)
     c1.wait()
     out = c1.communicate()
     data = out[0].decode("utf-8")
     secrets = []
     for i in data.split("}")[:-1]:
          secret = i.split(age)[0]
          if name in secret:
              secrets.append(secret)
              print(secret+" "+age)
     #print(data_json)
     #print the secret with out year
     for secret in secrets:
          print(secret)

         
     #answer = input("do you want to delete: ") #this is python3 only
     #answer = raw_input("do you want to delete: ") #this is python2 only
     if perm == 'yes':
        for secret in secrets:
             cmd2 = "kubectl delete secret %s"%secret
             c2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE)
             c2.wait()
             out = c2.communicate()
             data = out[0].decode("utf-8")
             print(data)
     else:
             print("delete aborted.")
             quit()


parser = argparse.ArgumentParser()
parser.add_argument("-age",required = True)
parser.add_argument("-name",required = True)
parser.add_argument("-perm",required = True)
args = parser.parse_args()

del_secret(args.age,args.name,args.perm)
