#https://github.com/python-ops-org/python-ops/blob/master/tutor-2/demo.py



import re


"""
name = "Murthy Raju"
city = "chennai"
#print(name[0:6])
#output: Murthy
#p=name.replace("Murthy", "murthy")
#output: murthy
#print(p)
#print(name.lower())
#output: murthy raju
#print(name.upper())
#output: MURTHY RAJU
#s1="{} live in {}".format(name,city)
#output: Murthy Raju live in chennai
#print(s1)
"""

#example-02
string1="Murthy Raju lives in Chennai and his email Ids are murthyraju@gmail.com and murthyraju123@gmail.com"
"""
#task: grep raju from text
pattern='raju'
new=re.search(pattern, string1)
print(new.group())
"""

"""
#task: grep email id  from text
#output: murthyraju@gmail
p=re.search(r'\w+@\w+', s2)
print(p)

"""

"""
#task: grep email ids  from text
#output: murthyraju@gmail.com murthyraju123@gmail.com
#\S=Returns a match where the string DOES NOT contain a white space character
#\s=Returns a match where the string contains a white space character
p=re.findall(r'\S+@\S+\.\S+', s2)
print(p)
"""

#example-04
#.=Anycharacter(except newline character)
#*=Zero or more occurrences
#()=Capture and group
s3="Sudipto Chakraborty"
#p=re.search(r'.*', s3)
#print(p.group())
#p=re.search(r'Sud....\s', s3)
#output: sudipto
#p=re.search(r'(Sud....\s)(.*)', s3)
#print(p.group())
#p=re.search(r'(Sud.+)', s3)
#print(p.group(0))


n='Jacob Ordonez'
pattern='Jac..\s'
new=re.search(pattern, n)
print(new.group())













