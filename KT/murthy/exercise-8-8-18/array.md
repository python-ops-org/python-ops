
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

loop

for
```
import array as arr
newArray = arr.array('i', [56, 42, 23, 85, 45])
for iterate in newArray:
   print (iterate)

```

while

```

import array as arr

# creating array
a = arr.array('i', [96, 26, 56, 76, 46])

# checking the length
l = len(a)

# loop variable
idx = 0

# while loop
while idx < l:
   print (a[idx])
   # incrementing the while loop
   idx+=1

```


Python for Loop with Array Index



```
import array as arr
a = arr.array('d', [56, 42, 23, 85, 45])
l = len(a)
for x in range(l):
   print (a[x])

```


reverse

Using slicing operation

```

import array as arr

# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])

print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)


```


Reverse an Array Using reverse() Method

```

import array as arr

# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

# converting the array into list
newArray = numericArray.tolist()

# reversing the list
newArray.reverse()

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

```


Using for Loop

```
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print(a)
print(b)


```



Sort Arrays Using a Sorting Algorithm


```
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)

```

Sort Arrays Using sort() Method of List

```

import array as arr

# creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
# converting to list 
sortedList = orgnlArray.tolist()
# sorting the list
sortedList.sort()

# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)

```
Sort Arrays Using sorted() Method

```
import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print(a)

```


 Join Two Arrays by Appending Elements

```
import array as arr

# creating two arrays
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])

# merging both arrays
for i in range(len(b)):
   a.append(b[i])
print (a)

```

Using + operator

```

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x = a.tolist()
y = b.tolist()
z = x+y
a = arr.array('i', z)
print (a)

```


Using extend() Method

```

import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])
a.extend(b)
print (a)

```


Python program to find the largest number in an array


```

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)

```


Python program to find the average of all numbers in a Python array

```

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
s = 0
for i in range(len(a)):
   s+=a[i]
avg = s/len(a)
print ("Average:", avg)

# Using sum() function
avg = sum(a)/len(a)
print ("Average:", avg)

```

```

import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b = a
print("Copied array:",b)
print (id(a), id(b))

```


Python program find difference between each number in the array and the average of all numbers

Python program to convert a string in an array

Python program to split an array in two and store even numbers in one array and odd numbers in the other.

Python program to perform insertion sort on an array.

Python program to store the Unicode value of each character in the given array.



 


























```

myarray=( apple banana mango kiwi litchi watermelon )

# printing all array elements

echo ${myarray[@]}
echo ${myarray[@]:0}

echo ${myarray[@]:1:3}
echo ${myarray[@]:1:5}

```







