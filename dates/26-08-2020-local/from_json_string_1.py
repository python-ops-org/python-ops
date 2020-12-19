import json
from datetime import datetime
import csv



dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
rh = ['Name', 'City', 'Salary']
log = open("%s.csv"%dt, "w+")
wr = csv.writer(log)
wr.writerow(rh)




x = {"name": "nik", "city": "tokyo", "salary": 1000}
y = json.dumps(x["name"])
k = y.replace('"', '')
print("%s"%(k))

wr.writerow([k])
