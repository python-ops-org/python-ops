

## While Loop
--------------

```
+-------------------+
| Initialize values |
+-------------------+
         |
         v
+-----------------------------+
| Evaluate while condition   |
| (Condition is True or False)|
+-----------------------------+
         |
   +-----+-----+
   |           |
   v           v
+--------+   +-------------------+
| Execute |   | Exit the loop    |
|  Block  |   | (Condition False)|
+--------+   +-------------------+
     |
     v
+-----------------+
| Update/Iterate  |
| (Optional)      |
+-----------------+
     |
     v
  Back to condition

```

![while-loop](images/while.jpg)



```
# Example while loop

count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")



```

```

var = '0'
while var.isnumeric() == True:
   var = "test"
   if var.isnumeric() == True:
      print ("Your input", var)
print ("End of while loop")

```



```
var = 1
while var == 1 : # This constructs an infinite loop
   num = int(input("Enter a number :"))
   print ("You entered: ", num)
print ("Good bye!")


```




## While-Else Loop
--------------


![whileless-loop](images/whileelse.jpg)


```
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")


```

```

flag = 0
while (flag): print ("Given flag is really true!")
print ("Good bye!")

```


Syntax of break Statement
--------------------------

![break](images/break.jpg)





```
looping statement:
   condition check:
      break


```

break Statement with for loop
------------------------------

```

for letter in 'Python':    
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")


```


## break Statement with while loop
-----------------------------------
```
var = 10                   
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")

```

break Statement with Nested Loops
--------------------------------------

```
no = 33
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num == no:
      print ('number found in list')
      break
else:
   print ('number not found in list')

```


















