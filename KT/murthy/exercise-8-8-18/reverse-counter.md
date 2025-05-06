
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
from collections import Counter

def unique_words(s):
    return [word for word, count in Counter(s).items() if count == 1]

s = ["linux", "windows", "unix", "mac", "unix"]
print(unique_words(s))


```



```

import subprocess
import sys

# Get the number of running Apache2 processes
try:
    result = subprocess.run("ps -ef | pgrep apache2 | wc -l", shell=True, capture_output=True, text=True)
    p = int(result.stdout.strip())
except ValueError:
    print("critical")
    sys.exit(2)

# Check conditions
if p == 0:
    print("critical")
    sys.exit(2)
elif p <= 5:
    print("warning")
    sys.exit(1)
else:
    print(f"no of running apache: {p}")
    sys.exit(0)

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

```

p=`ps -ef | pgrep apache2 | wc -l`
if [-z "$p"]
then
echo "critical"
exit 2
else
if ["$p" -le "5"]
then
echo "warning"
exit 1
else
echo "no of running apache:""$p";
exit 0
fi
fi

```






- [blog-01](https://codescracker.com/python/program/python-program-swap-two-numbers.htm)
  

