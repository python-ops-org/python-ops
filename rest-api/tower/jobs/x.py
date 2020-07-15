import csv
from datetime import datetime

dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(["Size On Disk"])
print("Size On Disk")
#fo = open("art.xml","r")
#a = fo.readlines()
#fo.close()
a = p.split("\n")
lines = []
for line in a:
	if "<sizeOnDisk>" in line:
		line = str(line.replace("<sizeOnDisk>","")).replace("</sizeOnDisk>","").replace("\n","")
		lines.append(line.replace(" ",""))
print(lines[0])
print(lines[6])
writer.writerow([lines[0]])
writer.writerow([lines[6]])
