#python log.py -a log_level -u http://192.168.56.159 -t b6aCCurUXr6nAAb2JtPaxV3KvK1Lct

import csv,datetime
import json,socket
import requests
import re,time
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random
import subprocess


def log_level(addr,tok):
        nex = "/api/v2/job_templates"
        #%s%s?page=%s&page_size=100"
        all_data=[]
        print("template-name\tbefore\tafter")
        while True:
            headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
            r0 = requests.get("%s%s"%(addr,nex),headers=headers)
            d0 = json.loads(r0.text)
            for i in range(0,len(d0["results"])):
                try:
                    temp_id = d0["results"][i]["id"]
                    temp_name = d0["results"][i]["name"]
                    verbose = d0["results"][i]["verbosity"]
                    #print("%s\t%s\t%s"%(temp_id,temp_name,verbose))
                    #quit()
                    u2 = "%s/api/v2/job_templates/%s/"%(addr,temp_id)
                    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
                    data = {"name": temp_name,"description": "","job_type": "run", "verbosity": "0"}
                    #r2 = requests.patch(u2,headers=headers,body=data,verify=False)
                    r2 = requests.patch(u2,headers=headers,json=data,verify=False)
                    d1 = json.loads(r2.text)
                    after = d1["verbosity"]
                    print("%s\t%s\t%s"%(temp_name,verbose,after))
                    #print("verbose mode got changed")
                except:
                    continue





            if str(d0["next"]) == "None":
                break
            else:
                nex = str(d0["next"])
        


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u")
    parser.add_argument("-a")
    parser.add_argument("-t")
    args = parser.parse_args()
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("script started at: %s"%now)
    if (args.a is not None) and (args.a in ["log_level"]):    
        if args.a == "log_level":
            log_level(args.u,args.t)
            now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("script ended at: %s"%now)
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

