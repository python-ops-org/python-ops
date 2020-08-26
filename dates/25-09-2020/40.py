import re

n1="The rain in Spain falls mainly in the plain!"
n2="my no is 8433674164"
n3="regex is awesome!"
n4="dance more"

#x=re.search("^The.*Spain$", s)
#find pa
#x=re.findall("pa", s)
#find first whitespace
#x=re.search("\s", s)
#string contains "a" followed by exactly two "l"
#x=re.findall("al{2}", s)
#print(x.start())
#x=re.match("\D", n)
#x=re.match("\w", n)
#x=re.findall(r'[0-9]+', n)
#print(str(x)[1:-1])
#print(", ".join(x))
#print(*x, sep=', ')
#print(x[0])
#p=re.compile(r"\w+")
#r=p.match(n1)
#print(r.group)
#r=re.match("[^\d+]", n4)
#r=re.search(r"\w+", n2, re.MULTILINE)  
#print(r.group())

cmd ='tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      3400/sendmail: MTA:'
#r7=re.findall(r'^[\w\d\s\.:]+:(25)\s+.*$',  cmd, re.MULTILINE)
#print(r7[0])

sal="5 6 7 10 12 13 14 100 200 300 1000 2000 4000"
n5=re.findall(r"\w+", sal)
print(n5[4])


