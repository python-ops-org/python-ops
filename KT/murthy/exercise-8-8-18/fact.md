
```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

```



```
n = 5
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(n))

```

```
#!/bin/bash

fact() {
  local n=$1
  if [[ $n -eq 0 ]]; then
    echo 1
  else
    local prev=$(fact $((n - 1)))
    echo $((n * prev))
  fi
}

n=5
result=$(fact $n)
echo "Factorial of $n is: $result"


```





