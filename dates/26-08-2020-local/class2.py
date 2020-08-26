class library:
    def __init__(self, author, title):
        self.author_name = author
        self.title_name  = title
    def printme(self):
        print(self.author_name, self.title_name)
class books(library):
    def __init__(self, author, title):
        super().__init__(author, title)
x = books("Doyel", "Diamond")
x.printme()

variable "s3_bucket_name" {
  description = "The name of the s3 bucket to store the registry data in"
  default = "tera-2"
}
