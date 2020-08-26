class Mobile:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Sum %d %d' % (self.a , self.b)
    def __add__(self,kali):
        return Mobile(self.a + kali.a, self.b + kali.b)

v1 = Mobile(10, 20)
v2 = Mobile(20,-2)
print(v1 + v2)
