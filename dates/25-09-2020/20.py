import csv
f=open("test.csv")
#k=f.readlines()
k=csv.reader(f)
#print(k)
c=0
for line in k:
#    if c > 0:
    print(line[4]) 
    c+=1

