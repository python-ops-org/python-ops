from pymongo import MongoClient
import redis


mongo   = MongoClient("mongodb://dbx:dbc123@127.0.0.1/db1")
lib = mongo.db.library
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

def lambda_handler(event, context):
    output = []
    for s in lib.find():
        try:
            r = json.loads(redis.get(s['title']))
            print(f"{s['title']} is present in redis")
            output.append({'author' : r["author"], 'title' : s['title']})
        except:
            print(f"{s['title']} was absent so key got created")
            output.append({'author' : s['author'], 'title' : s['title']})
            redis.set(s["title"], json.dumps({"author": s['author']}))
    return output
