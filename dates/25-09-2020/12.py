#print i as long as 6 bit break when it become 3

"""

i=1
while i < 6:
  print(i)
  if i==3:
    break
  i+=1

"""
"""
#print hello world for 3 times by while loop

i=0
while i < 3:
    print("hello")
    i+=1

"""
import sys
#print all letters except u and x
#you want output to be lin .?>Yes
i=0
a='linux'

#the problem with print is that it always adds \n , for this you need sys
#1st method
while i < len(a):
    if a[i] == 'u' or a[i] == 'x':
        i+=1
        continue
    sys.stdout.write(a[i])
    sys.stdout.flush()
    i+=1

print("\n")#this is just to seperate mthods
#2nd method

for i in a:
	if i == "u" or i == "x":
		continue
	else:
		sys.stdout.write(i)
		sys.stdout.flush()

print("\n")#this is just to seperate mthods
#3rd method

a = str(a.replace("u","")).replace("x","")
print(a)













