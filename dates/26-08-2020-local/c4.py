class usalibrary:
    def books(self):
        print("calling parent")

class indialibrary(usalibrary):
    def books(self):
        print("calling child")

b = indialibrary()
b.books()                
