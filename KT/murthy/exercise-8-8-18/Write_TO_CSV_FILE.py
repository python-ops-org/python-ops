from datetime  import datetime
import csv 

ct = datetime.now()
cts = ct.strftime("%d-%b-%Y-%H-%M")
file = open("list_" + cts + ".csv", "w",newline="")
writer = csv.writer(file)
writer.writerow(["NAME","SCORE"])
data = ["virat", "101"]
writer.writerow(data)





import csv

file = 'test.csv'
data = [
    ["name", "score"],
    ["virat", "100"],
    ["rohit", "120"]
]

f = open(file, newline='', mode='w')  # Using your original open syntax
w = csv.writer(f)

for row in data:
    w.writerow(row)

f.close()  # Don't forget to close the file

print(f"Data written to {file}")
