
 classmethod() which transforms an instance method to a class method 
 which can be called with the reference to the class only and not the object.
 
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


Public Methods
-----------------

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

Add another instance variable salary. Make age private and salary as protected by prefixing double and single underscores respectively

```
class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)

```


Getters and Setter Methods

```
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age

e1=Employee("Bhavana", 24)
print ("Name:", e1.get_name(), "age:", e1.get_age())
e1.set_name("Archana")
e1.set_age(21)
print ("Name:", e1.get_name(), "age:", e1.get_age())

```


complete program with property objects

```
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age
      return
   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)

```


method overriding refers to defining a method in a subclass with the same name as a method in its superclass.

```
# define parent class
class Parent: 
   def myMethod(self):
      print ('Calling parent method')

# define child class
class Child(Parent): 
   def myMethod(self):
      print ('Calling child method')

# instance of child
c = Child() 
# child calls overridden method
c.myMethod()

```


```
class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)
      self.incnt=inc
   def getSalary(self):
      return self.salary+self.incnt

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))


```


Method overloading is a feature of object-oriented programming where a 
class can have multiple methods with the same name but different parameters



```

class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20)

```


```

class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))

```
































