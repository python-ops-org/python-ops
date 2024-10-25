
"""
Class: A template or blueprint for creating objects (e.g., Dog).
Constructor (__init__): A special method to initialize object attributes.
self: Refers to the specific instance of the class, allowing access to instance attributes and methods.
"""

class Cricket:
    def __init__(self, name, score):
        self.name = name
        self.score = score

c1 = Cricket("Sachin", 100)
c2 = Cricket("Rahul", 95)




print(c1.name)
print(c1.score)
print(c2.name)
print(c2.score)
