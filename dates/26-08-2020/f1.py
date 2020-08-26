import re

f = open("data.txt")
#r = f.readlines()
o = [int(i.split()[1]) for i in f.readlines()]
#print(o)
print(sum(o))

#for i in o:
    #print(i)
    #k=i.split()[1]
    #print(k)
    #print(sum(k))






#n = r.split()[1]
#print(n)
