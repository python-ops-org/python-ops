
Accessing Values in Lists
---------------------------

```
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
```

Updating Lists
----------------
```
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])
```

Delete List Elements
------------------------

```
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)

```


Change Consecutive List Items
---------------------------------

```
list1 = ["a", "b", "c", "d"]

print ("Original list: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2

print ("List after changing with sublist: ", list1)

```

Adding List Items Using append() Method
-----------------------------------------

```
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)
```

Adding List Items Using insert() Method
----------------------------------------

```
list1 = ["Rohan", "Physics", 21, 69.75]

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)

```

Adding List Items Using extend() Method
------------------------------------------

```
# Original list
list1 = [1, 2, 3]
# Another list to extend with
another_list = [4, 5, 6]

list1.extend(another_list)
print("Extended list:", list1)

```

Remove List Item Using remove() Method
----------------------------------------

```
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

```

Remove List Item Using pop() Method
--------------------------------------

```
list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

```


Remove List Item Using del Keyword
------------------------------------

```
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)


```

Loop Through List Items with For Loop
---------------------------------------



```

lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')

```


Loop Through List Items with While Loop
----------------------------------------

```
my_list = [1, 2, 3, 4, 5]
index = 0

while index < len(my_list):
   print(my_list[index])
   index += 1

```

Loop Through List Items with Index
--------------------------------------


```
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])

```

Iterate using the enumerate() Function
----------------------------------------

```
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)

```

Sorting List in Lexicographical Order
---------------------------------------

```
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

```

Example of Sorting List in Numerical Order
------------------------------------------

```
list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)


```

Sorting Lists Using sorted() Method
-------------------------------------


```
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc) 

```

Sorting List Items with Callback Function
--------------------------------------------

```
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)

```

Join Lists Using Concatenation Operator
----------------------------------------

```
# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
# Joining the lists
joined_list = L1 + L2

# Printing the joined list
print("Joined List:", joined_list)

```

Join Lists Using append() Function
------------------------------------

```

# List to which elements will be appended
list1 = ['Fruit', 'Number', 'Animal']
# List from which elements will be appended
list2 = ['Apple', 5, 'Dog']
# Joining the lists using the append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List:", list1)

```

Python program to find unique numbers in a given list.
-------------------------------------------------------

```

L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for x in L1:
   if x not in L2:
      L2.append(x)
print (L2)

```

Python program to find sum of all numbers in a list.
------------------------------------------------------

```
L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)

```

Python program to create a list of 5 random integers.
------------------------------------------------------

```
import random
L1 = []
for i in range(5):
   x = random.randint(0, 100)
   L1.append(x)
print (L1)


```




































































































































































