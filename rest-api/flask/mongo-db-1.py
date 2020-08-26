from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://dbx:dbc123@127.0.0.1/db1")
mydb = client['db1']

book = [
        { "author": "doyel",
          "title" : "diamond",
          "tags" : ["thriller", "price", "london"],
          "date" : datetime.datetime.utcnow() },
        { "author": "cristi",
          "title" : "nemesis",
          "tags" : ["suspense", "price", "newyork"],
          "date" : datetime.datetime.utcnow() }
        ]





record_id = mydb.library.insert(book)

print(record_id)
print(mydb.collection_names())
