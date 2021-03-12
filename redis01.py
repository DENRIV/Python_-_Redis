# python redis01.py

import redis
r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

# print(r)
# Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>

d = r.get("Bahamas")
print(d)

d = r.get("Croatia")
print(d)