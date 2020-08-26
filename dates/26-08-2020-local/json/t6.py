import json
from datetime import datetime
import csv



"""
###json_dump
all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
row_header=['Name', 'City', 'Salary']
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(row_header)
x = {"name": "nik", "city": "tokyo", "salary": 10000}
y = json.dumps(x["name"])
z = json.dumps(x["city"])

print("%s\t%s"%(y,z))
all_data.append([y,z])
writer.writerow(all_data)
quit()


"""

"""
##json_loads

all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
row_header=['Name', 'City', 'Salary']
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(row_header)
x = '{"name": "nik", "city": "tokyo", "salary": 10000}'
y = json.loads(x)
o = (y["name"])
p = (y["city"])
print("%s\t%s"%(o,p))
all_data.append([o,p])
writer.writerow(all_data)

"""

###json_files

all_data=[]
dt = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
row_header=['Name', 'City', 'Salary']
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(row_header)
fo = open("r.json","r")
bar = json.load(fo,strict=False)
#print(bar)
#all_data.append([o,p])
#writer.writerow(all_data)

