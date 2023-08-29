n1 = 10
n2 = 12
s = n1 + n2
print(s)


def small(arr):
    if not arr:
        return None
    
    smallest = arr[0]
    
    for n in  arr:
        if n < smallest:
            smallest = n
    return smallest

n = [15,7,8,9]
s = small(n)
print(s)



import numpy as np
n1 = np.array([10])
n2 = np.array([12])
r = n1 + n2
print(r)
