import re

"""

f1=open("sal", "r")
#f2=open("sal_out.txt", "w")

c=0
for line in f1:
    #print(line)
    if c > 0:
       r=re.match(r'(\w+)\s+(\d+)\s+(\d+)',line.strip())
       p=r.groups()
       print(p)
       quit()
       name,mobile,salary = p
       cl="%s    %s" % (name, salary)
       print(cl)
    else: 
       cl="%s    %s" % ("name","salary")
       print(cl)
    c+= 1
f1.close()

"""


"""
f=open('f01', 'r')
p=re.findall(r'\d\d\d\d', f.read())
print(p)
f.close()
"""

f1=open('f01', 'r')
for line in f1:
    p=re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
    print(p)
f1.close()
















