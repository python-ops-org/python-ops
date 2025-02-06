

A class is an user-defined prototype for an object that defines a set of attributes 
that characterize any object of the class.


```

# defining class
class Smartphone:
   # constructor    
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand
   
   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description()) 

```



Encapsulation
---------------


```
class Desktop:
   def __init__(self):
      self.__max_price = 25000

   def sell(self):
      return f"Selling Price: {self.__max_price}"

   def set_max_price(self, price):
      if price > self.__max_price:
         self.__max_price = price

# Object
desktopObj = Desktop()
print(desktopObj.sell()) 

# modifying the price directly
desktopObj.__max_price = 35000
print(desktopObj.sell()) 

# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell()) 


```


Inheritance
-------------

A software modelling approach of OOP enables extending capability 
of an existing class to build new class instead of building from scratch


```

#!/usr/bin/python
# define parent class
class Parent:        
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent): 
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()  
# child calls its method        
c.childMethod() 
# calls parent's method     
c.parentMethod()  
# again call parent's method   
c.setAttr(200)  
# again call parent's method     
c.getAttr()

```

Polymorphism
---------------

Polymorphism is a Greek word meaning having multiple forms. 
In OOP, polymorphism occurs when each sub class provides its own implementation of an abstract method in base class.



```
# define parent class
class Parent:        
   def myMethod(self):
      print ("Calling parent method")

# define child class
class Child(Parent): 
   def myMethod(self):
      print ("Calling child method")

# instance of child
c = Child()
# child calls overridden method          
c.myMethod()         

```

| Magic Method      | Description                         | Sample Call                |
|------------------|---------------------------------|----------------------------|
| `__init__(self [,args...])`  | Constructor (with any optional arguments) | `obj = className(args)`  |
| `__del__(self)`  | Destructor, deletes an object | `del obj` |
| `__repr__(self)`  | Evaluable string representation | `repr(obj)` |
| `__str__(self)`  | Printable string representation | `str(obj)` |
| `__cmp__(self, x)`  | Object comparison | `cmp(obj, x)` |


Overloading Operators in Python
---------------------------------

```

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

```

Python constructor is an instance method in a class, that is automatically called whenever 
a new object of the class is created.

Default Constructor in Python
-------------------------------
The Python constructor which does not accept any parameter other than self is called as default constructor.


```

class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

```

Parameterized Constructor
--------------------------


```
class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))



```

```

class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age

e1 = Employee()
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

```


Python Multiple Constructors
------------------------------


```
class Student:
   def __init__(self, *args):
      if len(args) == 1:
         self.name = args[0]
        
      elif len(args) == 2:
         self.name = args[0]
         self.age = args[1]
        
      elif len(args) == 3:
         self.name = args[0]
         self.age = args[1]
         self.gender = args[2]
            
st1 = Student("Shrey")
print("Name:", st1.name)
st2 = Student("Ram", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Shyam", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")

```



Python - Instance Methods
---------------------------


```
class Employee:
   def __init__(self, name="Sachin", score=141):
      self.name = name
      self.score = score
   def displayEmployee(self):
      print ("Name : ", self.name, ", score: ", self.score)

e1 = Employee()
e2 = Employee("Rahul", 101)

e1.displayEmployee()
e2.displayEmployee()




```









