#kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | sed 's/2022-.*/ 2022/g' | grep -E 'db-pass' | awk '{print $1;}'
#kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | sed 's/2022-.*/ 2022/g' | grep -E 'db-pass' | awk '{print $1;}' | xargs -I {} kubectl delete secret {}


#kubectl get secrets -o jsonpath='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}' | tr "}" "\n" | grep -E 'db-user-pass' | sed 's/....................$//'


#python secret.py -age 2022 -name db-pass -perm yes


from datetime import datetime
import subprocess 
import csv
import argparse
import json
import re

#start_function
def del_secret():
     json_body='{range .items[*]}{.metadata.name}{.metadata.creationTimestamp}}{end}'
     #print the secret with year , put a tab b/w keyword db-pass and year 2022
     #cmd1 = "kubectl get secrets -o jsonpath='%s'"%json_body
     cmd1 = "kubectl get secrets -o jsonpath='%s'"%json_body
     c1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE)
     c1.wait()
     out = c1.communicate()
     data = out[0].decode("utf-8")
     data = data.replace("}","")[:-20]
     matched=re.findall("(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)",data)
     for date in matched:
         data = data.replace(date,"\n")
     secrets = []
     for secret in data.split("\n")[:-1]:
          if "db-user-pass" in secret:
              secrets.append(secret)
     #     print(secret)
     #print(data_json)
     #print the secret with out year
     for secret in secrets:
          print(secret)

     #make it logic with user interactive pattern "do you want to delete"?
     #if yes then it will do the delete secret step else it will exit the program
         
     #answer = input("do you want to delete: ") #this is python3 only
     answer = raw_input("do you want to delete: ") #this is python2 only
     if answer == 'yes':
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
     #delete the secret
     #cmd1 = "kubectl get secrets -o jsonpath=json_body | tr "}" "\n" | sed 's/2022-.*/ 2022/g' | grep -E 'db-pass' | awk '{print $1;}' | xargs -I {} kubectl delete secret {}"
     #c1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE)
    # c1.wait()
     #out = c1.communicate()
     #data = json.loads(out[0].decode("utf-8"))
    # print(%s"secret got deleted")


    

     

del_secret()
