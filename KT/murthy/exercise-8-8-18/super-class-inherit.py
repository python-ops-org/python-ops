class Cricket:
    def __init__(self):
        self.value = "London"

   
class Mumbai(Cricket):
    def __init__(self):
        super().__init__()
        self.value = "Mumbai"

object = Mumbai()
print(obj.value)
