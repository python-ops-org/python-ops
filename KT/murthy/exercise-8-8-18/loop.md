

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







