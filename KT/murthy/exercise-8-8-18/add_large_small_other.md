

```
n1 = 10
n2 = 12
s = n1 + n2
print(s)
```
```
# Function to find the smallest number in a list
def find_smallest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None
    smallest = numbers[0]  # Assume the first number is the smallest
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
numbers = [45, 67, 23, 89, 12, 55]
smallest_number = find_smallest_number(numbers)
print(f"The smallest number is: {smallest_number}")

```

import numpy as np
n1 = np.array([10])
n2 = np.array([12])
r = n1 + n2
print(r)










