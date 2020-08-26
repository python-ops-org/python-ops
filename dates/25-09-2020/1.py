import re
"""
l2=[1,2,3,4,5,6,7]
l2.pop(8)
print(l2)

"""

s2="My Mobile Nos Are 6867676898 and 7666675757"
phone = "2004-959-559 # This is Phone Number"
l1='tcp        0      0 192.168.56.145:2380     0.0.0.0:*               LISTEN      4285/etcd'         
l2='10.0.2.15 - - [08/Feb/2020:12:01:59 +0000] "GET" / HTTP/1.0" 200 116 "-" "ApacheBench/2.3"'
l3='::1 - - [31/Mar/2020:12:55:54 +0530] "GET /icons/ubuntu-logo.png HTTP/1.1" 404 209 "http://localhost:75/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"'
r1=re.match( r'(.*) Mobile (.*?) .*', s2, re.M|re.I)
r2=re.search(r'\d+', s2)
r3=re.findall(r'\d+', l1)
r4=re.sub(r'\D', "", phone)
#r5=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', l1).group(1)
#r6=re.findall(r'^[\w\d\s\.:]+:(2380)\s+.*$',  l1)
#print(str(r6).replace("'","")[1:-1])
#r7=(str(r6).replace("'","").replace('[','').replace(']',''))  
#r7=(str(r6))
#print(r7[1:-1].strip('\''))   
#print(r7.strip('[]').strip('\''))
#r8=l1.split(" ")
#print(r8[15].partition(':')[0])
#print(r8[15].strip(':')[15:19])
#print(r8[15].partition(':')[2])



 

l3='::1 - - [31/Mar/2020:12:55:54 +0530] "GET /icons/ubuntu-logo.png HTTP/1.1" 404 209 "http://localhost:75/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"' 
#l4=l3.split(" ")
#print("%s %s %s"%(l4[3]+l4[4],l4[9],l4[10].replace('"',"")))

#output will be like this
#31/Mar/2020:12:55:54   209 http://localhost:75/



#print (r1.group(3))
#print(r2.group())
#r4 = list(map(int, r3)) 
#print(str(r4[3]))
#print(r4)


#r10='00202_19042013_99_16_508546.TD2'
#0020219042013_99_16_508546.TD2
#print(s)

#r11=r10.replace("_", "", 1)
#print(r11)

#r11=r10[:5] + r10[7:]
#print(r11)
"""
f='ABC_15092014.txt DEF_14092014.txt ABC_14092014.txt'
f.sort()
print(f)
"""

"""
with open('old.csv', 'r') as t1, open('new.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
            
            """
            
            
            
t="The Rain In Spain at 05:04:2020"
x=re.search("^The.*Spain$", t)   
#print(x)
r20=re.findall("ai", t)   
#print(r20)      
r21=re.findall("\AXhe", t)
#print(r21)
r22=re.findall(r"\bRain", t)
#print(r22)
r23=re.findall("\d", t)
#print(r23)
r24=re.findall("\w", t)
#print(r24)
r25=re.findall("Spain\Z", t)
#print(r25)
r26=re.findall("[The]", t)
#print(r26)
r27=re.sub("\s", "_", t)
print(r27)



















