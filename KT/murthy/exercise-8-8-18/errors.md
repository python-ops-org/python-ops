
What is Exception?

An exception is an event, which occurs during the execution of a 
program that disrupts the normal flow of the program's instructions.


```

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.


```


```

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()


```


The try-finally Clause
------------------------

You can use a finally: block along with a try: block. The finally block is a 
place to put any code that must execute, whether the try-block 
raised an exception or not. The syntax of the try-finally statement is this −

```
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")

```


```

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")


```

Python Try-Except Block
-------------------------

```
try:
   # Code that might cause an exception
   risky_code()
except SomeException as e:
   # Code that runs if an exception occurs
   handle_exception(e)


```

Handling Multiple Exceptions
--------------------------------

```
try:
   # Code that might raise exceptions
   risky_code()
except FirstExceptionType:
   # Handle the first type of exception
   handle_first_exception()
except SecondExceptionType:
   # Handle the second type of exception
   handle_second_exception()
# Add more except blocks as needed for other exception types

```

```
try:
   dividend = int(input("Enter the dividend: "))
   divisor = int(input("Enter the divisor: "))
   result = dividend / divisor
   print(f"Result of division: {result}")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")

```


Using Else Clause with Try-Except Block
----------------------------------------

```
try:
   # Code that might raise exceptions
   risky_code()
except SomeExceptionType:
   # Handle the exception
   handle_exception()
else:
   # Code that runs if no exceptions occurred
   no_exceptions_code()

```

```
try:
   numerator = int(input("Enter the numerator: "))
   denominator = int(input("Enter the denominator: "))
   result = numerator / denominator
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"Result of division: {result}")

```

The Finally Clause
--------------------

```
try:
   file = open("example.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("Error: The file was not found.")
else:
   print("File read operation successful.")
finally:
   if 'file' in locals():
      file.close()
   print("File operation is complete.")


```


























































