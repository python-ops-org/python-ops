import csv,datetime
import json,socket
import requests
import itertools
import re
import datetime
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random
import pandas as pd




def job_list():
        #sg="2020-04-01"
        #sl="2020-04-23"
        addr="http://192.168.56.159"
        tok = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
        ct = datetime.now()
        cts = ct.strftime("%d-%b-%Y-%H-%M")
        fo = open("/home/nik/Desktop/report/job_list_" + cts  + ".csv" , "w")
        #nex = "/api/v2/jobs/?started_gt=%sT11:13:31.189777Z&started_lt=%sT11:13:31.189777Z&page=1&page_size=100"%(sg,sl)
        nex = "/api/v2/jobs/?page=1&page_size=100"
        writer=csv.writer(fo)
        writer.writerow(["JOBID","ORGNIZATIONS","GB","GF"])
        #all_data=[]
        while True:    
            headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
            r0 = requests.get("%s%s"%(addr,nex),headers=headers)
            data = json.loads(r0.text)
            #print(data)
            #quit()
            all_data=[]
            for i in range(0,len(data["results"])):
                job_id = data["results"][i]["id"]
                #print(job_id)
                
                org_name = data["results"][i]["summary_fields"]["organization"]["name"]
                #print(org_name)
                
                
                gf = org_name.split("_")[-1]
                gb = org_name.replace(gf,"")
                print("%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf))
                all_data.append([job_id,org_name,gb,gf])


            all_data.sort()
            all_data=list(all_data for all_data,_ in itertools.groupby(all_data))
            for row in all_data:
                writer.writerow(row)    

            if str(data["next"]) == "None":
                break
            else:
                #nex = "%s&started_gt=%sT11:13:31.189777Z&started_lt=%sT11:13:31.189777Z"%(str(data["next"]),sg,sl)
                nex = str(data["next"])



job_list()       
