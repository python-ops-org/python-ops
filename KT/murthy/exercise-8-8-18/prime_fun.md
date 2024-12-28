
```
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

```

```
for num in range(2,101):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)

```
```
#!/bin/bash

# Loop through numbers from 2 to 100
for num in {2..100}; do
    is_prime=1  # Assume the number is prime

    # Check divisors from 2 to num-1
    for ((i=2; i<num; i++)); do
        if ((num % i == 0)); then
            is_prime=0  # Not a prime number
            break
        fi
    done

    # If is_prime is still 1, the number is prime
    if ((is_prime == 1)); then
        echo "$num"
    fi
done
```


```
#!/bin/bash

# Number to check
n=10
i=2
c=0

# Loop to check divisors
while ((i <= n / 2)); do
    if ((n % i == 0)); then
        c=1
        break
    fi
    ((i++))
done

# Check the result
if ((c == 0)); then
    echo "prime"
else
    echo "not prime"
fi
```




