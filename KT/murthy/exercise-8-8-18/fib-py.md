
```

fibo=[0,1]
for i in range (50):
    fibo.append(fibo[-1]+fibo[-2])

print fibo
```

```

#!/bin/bash

# Initialize the Fibonacci sequence
fibo=(0 1)

# Generate the next 50 numbers in the sequence
for ((i=2; i<52; i++)); do
    fibo[i]=$((fibo[i-1] + fibo[i-2]))
done

# Print the Fibonacci sequence
echo "${fibo[@]}"

```
