
"""
def prime(n):
    count = 0
    for i in range(1, (n+1)): 
         if n % i == 0: 
             count += 1
    if count > 2:
        print "Not a prime"
    else:
        print "A prime"
"""

"""
def prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if not x%i:
           return False
    return True
"""

"""
n=7
def check(n):
    x = True
    for i in range(2, n):
        if n%i == 0:
            x = False
            break
    if x:
        print("prime")
    else:
        print("not prime")
check(n)          

"""
"""
n=10
i=2
c=0  
while (i<n/2):
    if n%i == 0:
        c=1 
        break  
    i+=1
if c==0:    
    print("prime")
else:
    print("not prime")    


"""
 """   

n=7
def check(n):
    f=0  
    i=2
    while (i<n/2):
        if n%i == 0:
            f=1 
            break  
        i+=1
    if f==0:    
        print("prime")
    else:
        print("not prime")  
check(n)            
"""













#for i in range(20):
#    print i, prime(i)

#x = int(raw_input("enter a prime number"))
#print prime(x)

for num in range(2,101):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)

