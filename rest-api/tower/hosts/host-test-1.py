#python inv.py -a host_list -u http://192.168.56.117 -t jge72IFPtqPvYsflypTkFQk79jgAyo

import csv,datetime
import json,socket
import requests
import re,time
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random
import subprocess



def users_list(addr,tok):
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
        r0 = requests.get("%s/api/v2/hosts/"%(addr),headers=headers)
        data0 = json.loads(r0.text)
        cc = int(data0["count"])
        all_users=[]
        try:    
           user_id = data["results"][0]["id"]
           all_ids.append(host_id)
        except:
             all_ids.append("not found")






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u")
    parser.add_argument("-a")
    parser.add_argument("-t")
    args = parser.parse_args()
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("script started at: %s"%now)
    if (args.a is not None) and (args.a in ["host_list"]):    
        if args.a == "add":
            user_list(args.u,args.t)
        else:
            print("Error")
            return None
            now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("script ended at: %s"%now)
    else:
        print("kindly parse correct key")
        return None

if __name__ == "__main__":
    main()         

   


