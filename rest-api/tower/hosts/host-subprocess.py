##get ips from output then write in to csv and then print on terminal

from datetime import datetime
import subprocess 
import csv
import argparse
import json

#curl -k -s --user admin:password -X GET  http://192.168.56.159/api/v2/hosts/?enabled=true&inventory=2


##global vars
#url = 'http://192.168.56.159/api/v2/hosts/?enabled=true&inventory=2'

#start_function
def get_hosts(url):
    cred = "admin:password"
    p = subprocess.Popen("curl -k -s --user %s %s"%(cred,url),shell=True, stdout=subprocess.PIPE)
    p.wait()
    out = p.communicate()
    data = json.loads(out[0].decode("utf-8"))
    name = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    with open("%s.csv"%name,"w+") as op:
        op.write("ip adresses\n")
        for ad in data["results"]:
            print(ad["name"])
            op.write("%s\n"%ad["name"])

parser = argparse.ArgumentParser()
parser.add_argument("-u",required=True)
args = parser.parse_args()
get_hosts(args.u)
