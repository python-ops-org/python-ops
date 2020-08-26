from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import  pymongo
from pymongo import MongoClient
import  json
from  bson.json_util  import  dumps




app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db1'
app.config["MONGO_URI"] = "mongodb://dbx:dbc123@172.17.0.2/db1"

mongo = PyMongo(app)




@app.route('/books', methods=['GET'])
def get_all_stars():
  lib = mongo.db.library
  output = []
  for s in lib.find():
    output.append({'author' : s['author'], 'title' : s['title']})
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)  
