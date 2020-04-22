import json
import csv
import re
import numpy as np
#import panda

#ips=[]
f1=open("ip-ranges.json",'r')
f2=open("/home/nik/Desktop/report/ip-list-1.csv", mode='a')

w=csv.writer(f2)
w.writerow(["IP","SUBNET","CAL1","CAL2","CAL3","HOSTS"])
d=json.load(f1)
print("IP\tSUBNET\tCAL1\tCAL2\tCAL3\tHOSTS")
total_hosts = 0
for i in d['prefixes']:
    d=i["ip_prefix"]
    c=i["ip_prefix"].split("/")
    ip = c[0]
    subnet = c[1]
    cal1 = "32-%s"%str(subnet)
    cal2 = 32-int(subnet)
    cal3 = "2*%s"%str(cal2)
    hosts = 2*cal2
    total_hosts = total_hosts + hosts
    print("%s\t%s\t%s\t%s\t%s\t%s"%(d,subnet,cal1,str(cal2),cal3,str(hosts)))
    w.writerow([d,subnet,cal1,str(cal2),cal3,str(hosts)])
print("\t\t\t\t\t\ttotal=%s"%total_hosts)
w.writerow(["","","","","","TOTAL=%s"%str(total_hosts)])
