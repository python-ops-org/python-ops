#python inv.py -a host_list -u http://192.168.56.117 -t jge72IFPtqPvYsflypTkFQk79jgAyo
import csv,datetime
import json,socket
import requests
import re
import datetime
import argparse
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re,random


def job_list(addr,tok,sg,sl):
        ct = datetime.now()
        cts = ct.strftime("%d-%b-%Y-%H-%M")
        fo = open("/home/nik/Desktop/report/job_list_" + cts  + ".csv" , "w")
#       addr="http://192.168.56.159"
        #nex = "/api/v2/jobs/"
        #nex="/api/v2/jobs/?started_gt=2020-04-12T11:13:31.189777Z&started_lt=2020-04-23T11:13:31.189777Z&page_size=100"
        nex = "/api/v2/jobs/?started_gt=%sT11:13:31.189777Z&started_lt=%sT11:13:31.189777Z"%(sg,sl)
#        tok = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
        all_data=[]
        while True:    
            headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s'%tok }
            r0 = requests.get("%s%s"%(addr,nex),headers=headers)
            data = json.loads(r0.text)
            #print(data)
            #quit()
            for i in range(0,len(data["results"])):
                job_id = data["results"][i]["id"]
                #print(job_id)
                
                org_name = data["results"][i]["summary_fields"]["organization"]["name"]
                #print(org_name)
                
                
                gf = org_name.split("_")[-1]
                gb = org_name.replace(gf,"")
                #print("%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf))

                proj_name = data["results"][i]["summary_fields"]["project"]["name"]

                temp_name = data["results"][i]["summary_fields"]["job_template"]["name"]
                #print("%s\t%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf,temp_name))
                
                cb = data["results"][i]["summary_fields"]["created_by"]["username"]
                #print("%s\t%s\t%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf,temp_name,cb))
                
                st = data["results"][i]["started"]
                ft = data["results"][i]["finished"]
                #print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf,temp_name,cb,st,ft))
                
                jn = data["results"][i]["name"]
                sta = data["results"][i]["status"]
                print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(job_id,org_name,gb,gf,proj_name,temp_name,cb,st,ft,jn,sta))
                all_data.append([job_id,org_name,gb,gf,proj_name,temp_name,cb,st,ft,jn,sta])

            if str(data["next"]) == "None":
                break
            else:
                nex = "%s&started_gt=%sT11:13:31.189777Z&started_lt=%sT11:13:31.189777Z"%(str(data["next"]),sg,sl)

        writer=csv.writer(fo)
        writer.writerow(["JOBID","ORGANIZATIONS","GB","GF","PROJECT","TEMPLATENAME","LAUNCHEDBY","STARTED","FINISHED","JOBNAME","STATUS"])
        for row in all_data:
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u")
    parser.add_argument("-a")
    parser.add_argument("-t")
    parser.add_argument("-sg")
    parser.add_argument("-sl")
    args = parser.parse_args()
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("script started at: %s"%now)
    if (args.a is not None) and (args.a in ["job_list"]):    
        if args.a == "job_list":
            job_list(args.u,args.t,args.sg,args.sl)
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









#job_list()         

