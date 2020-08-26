###create class mobile ...use init functiom to assign values to name and price

class Mobile:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def update_price(self):
      print("Updated Mobile Price" + str(self.price))  
p=Mobile("Mi", 20000)
#print(p.name)
#print(p.price)
p.update_price()        
