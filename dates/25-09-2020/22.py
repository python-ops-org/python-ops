import json
import csv
import re

#ips=[]
f1=open("ip-ranges.json",'r')
f2=open("/home/nik/Desktop/report/ip-list-1.csv", mode='a')
#d=json.load(f1)
#print(d)

"""
for i in d['prefixes']:
    c=(i["ip_prefix"])
    print(c)
"""    


w=csv.writer(f2)
w.writerow(["IP"])
d=json.load(f1)
for i in d['prefixes']:
    c=(i["ip_prefix"])
    print(c)
    w.writerow([c])

