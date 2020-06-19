from pymongo import MongoClient
import redis
import datetime

class DBClient():
  def __init__(self):
    self.mongo   = MongoClient("mongodb://dbx:dbc123@127.0.0.1/db1")
    self.mongodb = self.mongo['db1']
    self.redis   = redis.Redis(host='localhost', port=6379, db=0)

  def insertBooks(self, books):
    self.mongodb.library.insert(books)

    for book in books:
      self.redis.set(book["title"], book["author"])
  
  def getBookAuthor(self, title):
      return self.redis.get(title)

dbClient = DBClient()

def lambda_handler(event, context):
  if event["type"] == "insert":
    dbClient.insertBooks(event["books"])
  elif event["type"] == "get":
    return dbClient.getBookAuthor(event["title"])
  else:
    return f"event['type'] not mapped"

def main():
  books = [
    { 
      "author": "doyel",
      "title" : "diamond",
      "tags" : ["thriller", "price", "london"],
      "date" : datetime.datetime.utcnow() 
    },
    { 
      "author": "cristi",
      "title" : "nemesis",
      "tags" : ["suspense", "price", "newyork"],
      "date" : datetime.datetime.utcnow() 
    }
  ]
  
  dbClient.insertBooks(books)

  print(dbClient.getBookAuthor("diamond"))
  print(dbClient.getBookAuthor("test"))

if __name__ == "__main__":
    main()
