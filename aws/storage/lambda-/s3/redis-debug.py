import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
mydict = { "mcity" : "mumbai", 'salary' : 1000 }
rval = json.dumps(mydict)
r.set("k1", rval)
data = r.get("k1")
result = json.loads(data)
arr = result["salary"]
