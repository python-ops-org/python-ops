#n = 12345
#r = str(n)[::-1]
#print(int(r))

"""
def rev(x):
        r=0
        i=0
        while x/10 > 0:
                r = (r * 10) + (x % 10)
                x= x/10
        r = (r * 10) + (x % 10)
        return r
print rev(21)

"""

"""
def swap(s1, s2):
   return s2, s1

s1 = 'chakraborty'
s2 = 'sudipta'

s1, s2 = swap(s1, s2)

print(s1, s2)

"""


https://codescracker.com/python/program/python-program-swap-two-numbers.htm

for i in range(6,0,-1):
    print(i * '' + (6-i) * '*')












1.


def swap(a, b):
    return b,a

a = 'virat'
b = 'kohli'

a, b = swap(a, b)
print(a, b)


2.

a = "kohlivirat"
b = a[::-1]
print(b)

3.

n = int(input("enter number:"))
r = int(str(n)[::-1])
print(r)

4.

from collections import Counter

def double(s):
    return [char for char, count in Counter(s).items() if count > 1 ]
s="linuxi"
print(double(s))



