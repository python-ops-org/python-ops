import json
import csv
import re
import numpy as np
import pandas as pd 


#ips=[]
f1=open("ip-ranges.json",'r')
f2=open("/home/nik/Desktop/report/ip-list-1.csv", mode='a')





w=csv.writer(f2)
w.writerow(["IP"])
d=json.load(f1)
for i in d['prefixes']:
    c=(i["ip_prefix"])
    print(c)
    w.writerow([c])
quit()

fo1=np.subtract(32, 15)
print(fo1)

fo2=np.multiply(2, 17)
print(fo2)

fo3=np.subtract(32, 16)
print(fo3)

fo4=np.multiply(2, 16)
print(fo4)

#fo5=np.sum(fo2, fo4)
#print(fo5)



