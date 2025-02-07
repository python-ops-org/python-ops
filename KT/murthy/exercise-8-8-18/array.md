
```

cars = ["Ford", "Volvo", "BMW"]

print(cars)

from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

```

```

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)

```

```

from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

```

Insertion Operation

```
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
 print(x)


```

Search Operation

```
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))

```

Update Operation

```

from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)


```

Accessing array items in Python


Using indexing
Using iteration
Using enumerate() function


```

import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

#indexing
print (numericArray[0])
print (numericArray[1])
print (numericArray[2])


```


Using iteration


```
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# iteration through for loop
for item in numericArray:
   print(item)


```


Accessing a range of array items in Python


```

import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# slicing operation
print (numericArray[2:])
print (numericArray[0:3])

```

```
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")


```

Adding Elements to Python Array

```
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

```

Using insert() method

```
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)


```

Using extend() method

```
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)


```

Remove First Occurrence


```

import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.remove(311)
# after removing array
print ("After removing:", numericArray)


```


Remove Items from Specific Indices

```

import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.pop(3)
# after removing array
print ("After removing:", numericArray)

```










```

myarray=( apple banana mango kiwi litchi watermelon )

# printing all array elements

echo ${myarray[@]}
echo ${myarray[@]:0}

echo ${myarray[@]:1:3}
echo ${myarray[@]:1:5}

```







