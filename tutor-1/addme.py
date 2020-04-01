'''
sum = 0

while a:
    sum+=a[0]
    a=a[1:]

print sum
'''

'''
sum = 0

for i in a:
    sum+=i

print sum
'''
'''
for i in range(1,7):
    print i
'''

'''
for i in range(5):
    for j in range(5-i):
        print ' ',
    for j in range(i):
        print '*',
    for j in range(1, i):
        print '*',
    print
'''
'''
a, b = 0, 1

print a, b,

while b<20:
    a, b = b, a+b
    print b,
'''
'''
def summe(a, b):
    c = a+b
    return c

print summe(45, 45)
'''
'''
def summe(a, b=45):
    c = a+b
    return c

print summe(45, 50)
'''
'''
def summe(*arg):
    print type(arg)
    for i in arg:
        print i

summe(3, 4, 5, 6, 7, 8)
'''
'''
def summe(**arg):
    print type(arg)
    print arg['a'],
    print arg['c']    

summe(a='Hello', b=3, c='world')
'''
a = [4, 5, 4, 3, 10]
'''
#recursive
def recur(a):
    print a
    if a==1:
        return 1
    else:
        return recur(a-1)

recur(5)
'''
sum = 0

def summe(a):
    size = len(a)
    if size==0:
        return 0
    else:
        return a[0]+summe(a[1:])

print summe(a)

  
