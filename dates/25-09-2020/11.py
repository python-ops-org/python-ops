class mobile:
  def __init__(self, name, price):
    self.name=name
    self.price=price

  def printme(self):
    print(self.name, self.price)

class  tv(mobile):
  def __init__(self, name, price):
    super().__init__(name, price)

x=tv("mi", 5000)
x.printme()

