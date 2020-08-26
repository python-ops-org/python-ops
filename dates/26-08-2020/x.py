#do we need to parse it or just get size on disk ?just get size 
import csv
from datetime import datetime

dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)
writer.writerow(["Size On Disk"])

fo = open("art.xml","r")
a = fo.readlines()
fo.close()
for line in a:
	if "<sizeOnDisk>" in line:
		line = str(line.replace("<sizeOnDisk>","")).replace("</sizeOnDisk>","").replace("\n","")
		writer.writerow([line.replace(" ","")])
