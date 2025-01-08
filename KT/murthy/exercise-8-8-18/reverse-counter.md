
```
n = 12345
r = str(n)[::-1]
print(int(r))

```

```

n = [1,2,3,4,5]
n.reverse()
print(n)

n = 12345
n = int(str(n)[::-1])
print(n)

list = [1,2,3,45,6,7,8,9]
s_list = list[2:6]
print(s_list)
```


```
def rev(x):
        r=0
        i=0
        while x/10 > 0:
                r = (r * 10) + (x % 10)
                x= x/10
        r = (r * 10) + (x % 10)
        return r
print rev(21)

```
```
n = int(input("please enter no:"))
r1 = 0

while( n > 0):
    r2 = n % 10
    r1 = (r1*10) + r2
    n  =  n //10

print ("\n reverse no is: %d" %r1)
```










```
def swap(s1, s2):
   return s2, s1

s1 = 'chakraborty'
s2 = 'sudipta'

s1, s2 = swap(s1, s2)

print(s1, s2)

```








```

for i in range(6,0,-1):
    print(i * '' + (6-i) * '*')

```







```

def swap(a, b):
    return b,a

a = 'virat'
b = 'kohli'

a, b = swap(a, b)
print(a, b)

```


```

a = "kohlivirat"
b = a[::-1]
print(b)

```


```

n = int(input("enter number:"))
r = int(str(n)[::-1])
print(r)

```


```
from collections import Counter

def double(s):
    return [char for char, count in Counter(s).items() if count > 1 ]
s="linuxi"
print(double(s))

```

```
double() {
    local s="$1"
    echo "$s" | grep -o . | sort | uniq -d
}

# Input string
s="linuxi"
double "$s"


```


- [blog-01](https://codescracker.com/python/program/python-program-swap-two-numbers.htm)
  

