"""

for i in range(1, 8):
    print(' ' * (7-i), '* ' * i)
"""

"""
fib = [0,1]
for i in range(50):
    fib.append(fib[-1] + fib[-2])
print(fib)

"""

"""
n=6
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))
"""

"""
def swap(s1,s2):
    return s2, s1
s1 = 'a'
s2 = 'b'

s1 , s2 = swap(s1, s2)
print(s1,s2)
"""

import csv
f = open("t1.csv", "w")
users = [("user1","10000"), ("user2", "5000")]
o = csv.writer(f)
for u in users:
    o.writerow(u)
f.close()
