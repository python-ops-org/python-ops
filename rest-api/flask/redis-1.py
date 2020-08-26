import pickle
import redis
#redis = redis.Redis(host='127.0.0.1', port=6379, db=0)

r = redis.StrictRedis('localhost')
mydict = {1:2,2:3,3:4}
p_mydict = pickle.dumps(mydict)
r.set('mydict',p_mydict)

read_dict = r.get('mydict')
yourdict = pickle.loads(read_dict)
