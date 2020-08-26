class plus:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'plus (%d, %d)' %(self.a, self.b)
    def __add__(self,other):
        return plus(self.a + other.a, self.b + other.b)
b = plus(10,2)
c = plus(20,-3)
print(b + c)
