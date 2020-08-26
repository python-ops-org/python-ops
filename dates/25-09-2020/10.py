#Create a class named Person, with firstname and lastname properties, and a printname method:
#Use the Person class to create an object, and then execute the printname method:

class Mobile:
  def __init__(self, name, price):
    self.name=name
    self.price=price
  def printme(self):
    print(self.name, self.price)

class Tv(Mobile):
 pass   

class Router(Mobile):
 pass   


x1=Tv("Mi", 1000)
x2=Router("Tenda", 5000)
x1.printme()
x2.printme()
