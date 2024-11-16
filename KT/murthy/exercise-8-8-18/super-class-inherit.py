class Cricket:
    def __init__(self):
        self.value = "London"

   
class Mumbai(Cricket):
    def __init__(self):
        super().__init__()
        self.value = "Mumbai"

object = Mumbai()
print(obj.value)



---------

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls the Parent's greet method
        print("Hello from Child!")

obj = Child()
obj.greet()


----------


class A:
    def show(self):
        print("From A")

class B(A):
    def show(self):
        print("From B")
        super().show()

class C(B):
    def show(self):
        print("From C")
        super().show()

obj = C()
obj.show()
