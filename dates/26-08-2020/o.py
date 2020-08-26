
"""
n = 5

if n % 2 == 0:
    print("even")
else:
    print("odd")
"""

"""
n = 5
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))
"""
"""
for i in range(1,6):
    print(' '* (5-i), '* ' * i)
"""

fib = [0,1]
for i in range(50):
    fib.append(fib[-1] + fib[-2])
print(fib)
    
