


 classmethod() which transforms an instance method to a class method which can be called with 
 the reference to the class only and not the object.
 
 Employee class, define a showcount() instance method with the "self" argument.
 

```
class Cricketer:
   batCount = 0
   def __init__(self, name, score):
      self.__name = name
      self.__score = score
      Cricketer.batCount += 1
   def showcount(self):
      print (self.batCount)
      
   counter = classmethod(showcount)

e1 = Cricketer("Sachin", 24)
e2 = Cricketer("Rahul", 26)
e3 = Cricketer("Virat", 27)

e1.showcount()
Cricketer.counter()

```

@classmethod() decorator is the prescribed way to define a class method as it is more convenient than
first declaring an instance method and then transforming it into a class method

```
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)


Employee.showcount()

```


Access Class Attributes in Class Method
----------------------------------------


```
class Cloth:
   # Class attribute
   price = 4000

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
print(Cloth.showPrice()) 

```

Dynamically Add Class Method to a Class
-----------------------------------------

The Python setattr() function is used to set an attribute dynamically.

```

class Cloth:
   pass

# class method
@classmethod
def brandName(cls):
   print("Name of the brand is Raymond")

# adding dynamically
setattr(Cloth, "brand_name", brandName)
newObj = Cloth()
newObj.brand_name()

```


Dynamically Delete Class Methods
----------------------------------


```
class Cloth:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth.brandName
print("Method deleted")



```

Static Method
---------------

 a static method is a type of method that does not require any instance to be called. 
 It is very similar to the class method but the difference is that the static method doesn't have a mandatory 
 argument like reference to the object − self or reference to the class − cls

```

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   
   # creating staticmethod
   def showcount():
      print (Employee.empCount)
      return
   counter = staticmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.counter()
Employee.counter()

```

we are creating a static method using the @staticmethod decorator.

```

class Student:
   stdCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Student.stdCount += 1
   
   # creating staticmethod
   @staticmethod
   def showcount():
      print (Student.stdCount)

e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()

```



















