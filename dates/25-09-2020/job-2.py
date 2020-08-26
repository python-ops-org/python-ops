#python inv.py -a host_list -u http://192.168.56.117 -t jge72IFPtqPvYsflypTkFQk79jgAyo
import csv,datetime
import json,socket
import requests
import re,time
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random


def job_list():
        addr="http://192.168.56.159"
        nex = "/api/v2/jobs/"
        tok = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
        ct = datetime.now()
        cts = ct.strftime("%d-%b-%Y-%H-%M")
        fo = open("/home/nik/Desktop/report/job_list_" + cts  + ".csv" , "w")
        all_data=[]
        while True:    
            f1=open("job.json",'r')
            data=json.load(f1)
            #print(data)
            
            for i in range(0,len(data["results"])):
                job_id = data["results"][i]["id"]
                print(job_id)
                

                proj_name = data["results"][i]["summary_fields"]["project"]["name"]

                temp_name = data["results"][i]["summary_fields"]["job_template"]["name"]
                #print("%s\t%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf,temp_name))
                
                
                st = data["results"][i]["started"]
                ft = data["results"][i]["finished"]
                
                
                jn = data["results"][i]["name"]
                sta = data["results"][i]["status"]
                print("%s\t%s\t%s\t%s\t%s\t%s\t%s"%(job_id,proj_name,temp_name,st,ft,jn,sta))

                #cb = data["results"][i]["summary_fields"]["created_by"]["username"]
                #sc = data["results"][i]["summary_fields"]["schedule"]["name"]
                #print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(job_id,proj_name,temp_name,sc,st,ft,jn,sta))
                all_data.append([job_id,proj_name,temp_name,st,ft,jn,sta])
                #all_data.append([job_id,proj_name,temp_name,st,ft,jn,sta])

            writer=csv.writer(fo)
            #writer.writerow(["JOBID","PROJECT","TEMPLATENAME","CREATEDBY","SCHEDULED BY","STARTED","FINISHED","JOBNAME","STATUS"])
            writer.writerow(["JOBID","PROJECT","TEMPLATENAME","STARTED","FINISHED","JOBNAME","STATUS"])
            for row in all_data:
                writer.writerow(row)

            if str(data["next"]) == "None":
                break
            else:
                nex = str(data["next"])

job_list()

