# python redis02.py

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# r = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None)

r.set('foo', 'bar')

d = r.get('foo')
print(d)

