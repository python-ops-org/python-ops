


```
capitals = {"Maharashtra":"Mumbai", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty"}
marks = {"Sachin":67, "Virat":88, "Rohit":91}

```

```
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

```


```

# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)


```

Accessing Dictionary Items

```

student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)  

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)


student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)


```

Removing Dictionary Items


```

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")

print(student_info)

```

Iterating Through a Dictionary
--------------------------------


```

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value)


```

Access Dictionary Items Using Square Brackets []
-------------------------------------------------

```
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])


```

Access Dictionary Items Using get() Method
--------------------------------------------

```
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))

```

 Retrieving all the keys from the dictionary
 ---------------------------------------------

```

# Creating a dictionary with keys and values
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing all keys using the keys() method
all_keys = student_info.keys()
print("Keys:", all_keys)

```

Access Dictionary Values
------------------------------


```

# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing dictionary values using square brackets
name = student_info["name"]
age = student_info["age"]
print("Name:", name) 
print("Age:", age)

```

Modifying Dictionary Values
-----------------------------

```
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Modifying the value associated with the key 'age'
person['age'] = 26
print(person)


```

Updating Multiple Dictionary Values
-------------------------------------

```
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)

```

Conditional Dictionary Modification
------------------------------------

```

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Conditionally modifying the value associated with 'age'
if person['age'] == 25:
   person['age'] = 26
print(person)

```

Modify Dictionary by Adding New Key-Value Pairs
--------------------------------------------------

```
# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person['city'] = 'New York'
print(person)


```

Modify Dictionary by Removing Key-Value Pairs
-----------------------------------------------

```
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
del person['age']
print(person)


```

Pop
----

```
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')

print(person)
print("Removed age:", removed_age)

```


Add Dictionary Item Using Square Brackets
------------------------------------------


```
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Initial dictionary: ", marks)
marks['Kavya'] = 58
print ("Dictionary after new addition: ", marks)

```


Add Dictionary Item Using Unpacking
------------------------------------


```
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)

```


Add Dictionary Item Using the Union Operator (|)
-------------------------------------------------


```
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)


```


Remove Dictionary Items Using del Keyword
------------------------------------------

```
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)

```

Remove Dictionary Items Using pop() Method
-------------------------------------------

```
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.pop(20)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

```

Remove Dictionary Items Using popitem() Method
------------------------------------------------

```

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.popitem()
print ("numbers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)


```

Remove Dictionary Items Using Dictionary Comprehension
---------------------------------------------------------

```
# Creating a dictionary
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)

print(student_info)

```

Loop Through Dictionary Using a For Loop
------------------------------------------


```
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key in student:
   print(key, student[key])

```

 Iterating over Key-Value Pairs
 ----------------------------------

 ```
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key, value in student.items():
   print(key, value)

```

Loop Through Dictionary Using dict.items() Method
--------------------------------------------------

```
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through key-value pairs 
for key, value in student.items():
   print(key, value)

```

Loop Through Dictionary Using dict.keys() Method
-------------------------------------------------

```
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through keys 
for key in student.keys():
   print(key)

```

Loop Through Dictionary Using dict.values() Method
----------------------------------------------------


```
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through values 
for value in student.values():
   print(value)

```

Creating a Nested Dictionary in Python
-----------------------------------------


```
# Define the outer dictionary
nested_dict = {
   "outer_key1": {"inner_key1": "value1", "inner_key2": "value2"},
   "outer_key2": {"inner_key3": "value3", "inner_key4": "value4"}
}
print(nested_dict)

```

Adding Items to a Nested Dictionary in Python
-----------------------------------------------



```
# Initial nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"}
}

# Adding a new key-value pair to Alice's nested dictionary
students["Alice"]["GPA"] = 3.8

# Adding a new nested dictionary for a new student
students["Charlie"] = {"age": 22, "major": "Mathematics"}

print(students)

```

Accessing Items of a Nested Dictionary in Python
---------------------------------------------------



```

# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Access Alice's major
alice_major = students["Alice"]["major"]
print("Alice's major:", alice_major) 

# Access Bob's age
bob_age = students["Bob"]["age"]
print("Bob's age:", bob_age)

```

Iterating Through a Nested Dictionary in Python
-------------------------------------------------


```
# Defining a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Iterating through the Nested Dictionary:
for student, details in students.items():
   print(f"Student: {student}")
   for key, value in details.items():
      print(f"  {key}: {value}")

```

Python program to create a new dictionary by extracting the keys from a given dictionary.

```
d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2={}
for k in keys:
   d2[k]=d1[k]
print (d2)

```

Python program to remove keys with same values in a dictionary

```
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())#all values
uvals = [v for v in vals if vals.count(v)==1]#unique values
d2 = {}
for k,v in d1.items():
   if v in uvals:
      d = {k:v}
      d2.update(d)
print ("dict with unique value:",d2)


```

```


















































































































































































