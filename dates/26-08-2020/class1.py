#create a sample class books to print author name and title name
class books:
    def __init__(self, author, title):
        self.author = author
        self.title = title
p = books("doyel", "diamond")


print(p.author)
print(p.title)
