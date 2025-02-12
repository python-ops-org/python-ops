
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
































