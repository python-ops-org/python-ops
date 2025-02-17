
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

Raising Built-in Exceptions
----------------------------

Raising an exception refers to explicitly trigger an error condition in your program
This can be useful for handling situations where the normal flow of your program 
cannot continue due to an error or an unexpected condition


```
def divide(a, b):
   if b == 0:
      raise ValueError("Cannot divide by zero")
   return a / b

try:
   result = divide(10, 0)
except ValueError as e:
   print(e)

```


Raising Custom Exceptions
---------------------------


```
class MyCustomError(Exception):
   pass

def risky_function():
   raise MyCustomError("Something went wrong in risky_function")

try:
   risky_function()
except MyCustomError as e:
   print(e)

```

Creating Custom Exceptions
-----------------------------



Custom exceptions is useful for handling specific error conditions that are unique to your application, providing more precise error reporting and control.



```

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(150)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")

```

Exception Chaining
--------------------


Exception chaining is a technique of handling exceptions by re-throwing a caught exception after wrapping it inside a new exception

Example
In the following code snippet, trying to open a non-existent file raises FileNotFoundError. It is detected by the except block. While handling another exception is raised.


```

try:
   open("nofile.txt")
except OSError:
   raise RuntimeError("unable to handle error")


```


The raise . . from Statement
------------------------------

If you use an optional from clause in the raise statement, it indicates that an exception is a direct consequence of another

```
try:
   open("nofile.txt")
except OSError as exc:
   raise RuntimeError from exc

```

The raise . . from None Statement
----------------------------------


```
try:
   open("nofile.txt")
except OSError as exc:
   raise RuntimeError from None

```


Nested try Block in Python
-----------------------------
In a Python program, if there is another try-except construct either inside either a try block or inside its except block, it is known as a nested-try block.


```
a=10
b=0
try:
   print (a/b)
except Exception:
   print ("General Exception")
finally:
   print ("inside outer finally block")
```

```
a=10
b=0
try:
   print (a/b)
   try:
      print ("This is inner try block")
   except Exception:
      print ("General exception")
   finally:
      print ("inside inner finally block")
      
except ZeroDivisionError:
   print ("Division by 0")
finally:
   print ("inside outer finally block")

```

Example 3
-----------


```
a=10
b=0
try:
   print ("This is outer try block")
   try:
      print (a/b)
   except ZeroDivisionError:
      print ("Division by 0")
   finally:
      print ("inside inner finally block")
      
except Exception:
   print ("General Exception")
finally:
   print ("inside outer finally block")

```

Example 4
----------

```
a=10
b=0
try:
   print ("This is outer try block")
   try:
      print (a/b)
   except KeyError:
      print ("Key Error")
   finally:
      print ("inside inner finally block")
      
except ZeroDivisionError:
   print ("Division by 0")
finally:
   print ("inside outer finally block")

```

User-Defined Exceptions in Python
------------------------------------
User-defined exceptions in Python are custom error classes that you create to handle specific error conditions in your code


```
class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

```

```
class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return f"{self.message}. Provided age: {self.age}"

```

```

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
     return f"{self.message}. Provided age: {self.age}"

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(150)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")


```

Logging in Python
--------------------
Logging is the process of recording messages during the execution of a 
program to provide runtime information that can be useful for monitoring, debugging, and auditing.


```
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def calculate_sum(a, b):
   logging.debug(f"Calculating sum of {a} and {b}")
   result = a + b
   logging.info(f"Sum calculated successfully: {result}")
   return result

# Main program
if __name__ == "__main__":
   logging.info("Starting the program")
   result = calculate_sum(10, 20)
   logging.info("Program completed")

```

Configuring Logging
--------------------

Configuring logging in Python refers to setting up various components such as loggers, 
handlers, and formatters to control how and where log messages are stored and displayed.


```
import logging

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

```

| **Handler**            | **Description** |
|------------------------|----------------|
| **StreamHandler**      | Sends log messages to streams such as `sys.stdout` or `sys.stderr`. Useful for displaying log messages in the console or command line interface. |
| **FileHandler**        | Writes log messages to a specified file on the file system. Useful for persistent logging and archiving of log data. |
| **RotatingFileHandler** | Similar to `FileHandler` but automatically rotates log files based on size or time intervals. Helps manage log file sizes and prevent them from growing too large. |
| **SMTPHandler**        | Sends log messages as emails to designated recipients via SMTP. Useful for alerting administrators or developers about critical issues. |
| **SysLogHandler**      | Sends log messages to the system log on Unix-like systems (e.g., syslog). Allows integration with system-wide logging facilities. |
| **MemoryHandler**      | Buffers log messages in memory and sends them to a target handler after reaching a certain buffer size or timeout. Useful for batching and managing bursts of log messages. |
| **HTTPHandler**        | Sends log messages to a web server via HTTP or HTTPS. Enables logging messages to a remote server or logging service. |




Assertions in Python
----------------------
Assertions in Python are statements that assert or assume a condition to be true. 
If the condition turns out to be false, Python raises an AssertionError exception.



```

print('Enter marks out of 100:')
num = 75
assert num >= 0 and num <= 100
print('Marks obtained:', num)

num = 125
assert num >= 0 and num <= 100
print('Marks obtained:', num)

```

Custom Error Messages
----------------------


```
try:
   num = int(input('Enter a number: '))
   assert num >= 0, "Only non-negative numbers are accepted"
   print(num)
except AssertionError as msg:
   print(msg)

```







































































































































