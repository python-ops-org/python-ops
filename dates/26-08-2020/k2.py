"""
n=121
i=n
c=0
while(n>0):
    k=n%10
    c=c*10+k
    n=n//10
if(i==c):
    print("pale")
else:
    print("na")
"""

s = "mam"
if (s==s[::-1]):
    print("pale")
else:
    print("na")
