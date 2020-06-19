from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import  pymongo
from pymongo import MongoClient
import  json
from  bson.json_util  import  dumps
import redis


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db1'
app.config["MONGO_URI"] = "mongodb://dbx:dbc123@172.17.0.2/db1"

mongo = PyMongo(app)
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/books', methods=['GET'])
def get_all_stars():
  lib = mongo.db.library
  output = []

  redis_keys = redis.keys()
  #for title in redis.keys():
  #  output.append({ "key/title": title, "value/author": redis.get(title)})
  for s in lib.find():
    try:
      r = json.loads(redis.get(s['title']))
      print(f"{s['title']} is present in redis")
      output.append({'author' : r["author"], 'title' : s['title']})
    except:
      print(f"{s['title']} was absent so key got created")
      output.append({'author' : s['author'], 'title' : s['title']})
      redis.set(s["title"], json.dumps({"author": s['author']}))
      
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)  
