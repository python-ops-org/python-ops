import json
from datetime import datetime
import csv

"""
I have three sample json format from which i want
to grep data and write in to csv file along with timestamp.
internet is doing problem on today. Asking aplogise at the begining.

"""

"""
###json_dump
all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
row_header=['Name', 'City', 'Salary']
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(row_header)
x = {"name": "nik", "city": "tokyo", "salary": 10000}
y = json.dumps(x["name"])
z = json.dumps(x["city"])

print("%s\t%s"%(y,z))
#all_data.append()
writer.writerow([x["name"],x["city"]])
quit()
#looks fine

"""


"""
##json_loads

#all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
row_header=['Name', 'City', 'Salary']
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(row_header)
x = '{"name": "nik", "city": "tokyo", "salary": 10000}'
y = json.loads(x)
o = (y["name"])
p = (y["city"])
k = (y["salary"])
print("%s\t%s"%(o,p))
#all_data.append([o,p])
#writer.writerow(all_data)
writer.writerow([o,p,k])
"""




###json_files

all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
fo = open("r.json","r")
bar = json.load(fo,strict=False)
r = bar["us-east-1"][0]
s = bar["us-east-1"][1]
print(r)
#print(bar)
#all_data.append([o,p])
writer.writerow([r,s])
