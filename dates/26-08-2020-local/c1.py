class library:
    books = 0
    def __init__(self, author, title):
        self.author = author
        self.title  = title
        #library.books +=1

    """
    def bookscount(self):
        print("TotalBooks %d", library.books)
    """

    def booksdetails(self):
        print("Author_Name: ", self.author, ", Title_Name: ", self.title)

#"This would create first object of library class"
book1 = library("Crsiti", "Nemesis")
#This would create second object of library class
book2 = library("Doyel", "Diamond")
#we can access the object's attributes using the dot operator with object
#

book1.booksdetails()
book2.booksdetails()
#print(getattr(book1, 'author'))
#Class variable would be accessed using class name as follows

#print("TotalBooks %d", library.books)
