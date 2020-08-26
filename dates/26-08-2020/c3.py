class usalibrary:
    def __init__(self, author,title):
        self.author = author
        self.title  = title

    def booksdetails(self):
        print("Author_Name:", self.author, ", Title_Name:", self.title)

"""
class indialibrary(usalibrary):
    pass
"""
class indialibrary(usalibrary):
    def  __init__(self, author,title):
        usalibrary.__init__(self, author,title)

book1=indialibrary("doyel", "diamond")
book1.booksdetails()
