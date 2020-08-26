import re


"""
string1='::1 - - [31/Mar/2020:12:55:54 +0530] "GET /icons/ubuntu-logo.png HTTP/1.1" 404 209 "http://localhost:75/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"' 
p=string1.split(" ")
pattern1='("%s %s %s"%(p[3]+p[4],p[9],p[10])'
print(pattern1.replace('"',""))

#print("%s %s %s"%(p[3]+p[4],p[9],p[10].replace('"',"")))

"""
#example-02
#extract 2380 from stdout 

l2='tcp        0      0 192.168.56.145:2380     0.0.0.0:*               LISTEN      4285/etcd'
"""
#sol-1
p=l2.split(" ")
print(p[15].partition(':')[2])
"""

"""
#sol-2
#\s=Returns a match where the string contains a white space character
#\d=Returns a match where the string contains digits (numbers from 0-9)
#\w=Returns a match where the string contains any word characters 
#(characters from a to Z, digits from 0-9, and the underscore _ character)
#.=Any character (except newline character)
#+=One or more occurrences
#*=Zero or more occurrences
#$=Ends with
#^=Starts with
#()=Capture and group
#[]=A set of characters
q=re.findall(r'^[\w\d\s\.:]+:(2380)\s+.*$',  l2)
print(q[0])
"""



#sol-3
#[]=A set of characters
#()=Capture and group
#^=Starts with
#+=One or more occurrences
pattern=':([^ ]+)'
new=re.findall(pattern, l2)[0]
print(new)






#example-03
#s5="Once you have accomplished small things, you may attempt great ones safely."
#p=re.findall(r'\ba\w+', s5)
#print(p[0])

#print(re.split("\W+", s5))
#print(re.sub("[ ,.]", ":", s5))






#l2='10.0.2.15 - - [08/Feb/2020:12:01:59 +0000] "GET" / HTTP/1.0" 200 116 "-" "ApacheBench/2.3"'

