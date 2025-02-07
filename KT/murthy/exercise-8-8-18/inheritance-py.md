
Inheritance
------------

It is used to inherit the properties and behaviours of one class to another.

 The class that inherits another class is called a child class and the class that gets inherited 
 is called a base class or parent class

 Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance




Single Inheritance
--------------------


```
# parent class
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

# child class
class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()  
# calling method of child class
c.childMethod() 
# calling method of parent class
c.parentMethod() 

```


Python - Multiple Inheritance
--------------------------------

```
class parent1:
   #statements
   
class parent2:
   #statements
   
class child(parent1, parent2):
   #statements

```

```
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)

x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())


```

Python - Multilevel Inheritance
---------------------------------

a class is derived from another derived class

```

# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()  
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 


```

Python - Hierarchical Inheritance
---------------------------------------














