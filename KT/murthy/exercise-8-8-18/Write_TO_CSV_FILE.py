from datetime  import datetime
import csv 

ct = datetime.now()
cts = ct.strftime("%d-%b-%Y-%H-%M")
file = open("list_" + cts + ".csv", "w",newline="")
writer = csv.writer(file)
writer.writerow(["NAME","SCORE"])
data = ["virat", "101"]
writer.writerow(data)
