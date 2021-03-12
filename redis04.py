# python redis04.py

import redis

import time

#r = redis.Redis(host='localhost', port=6379, db=0)
r = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None)

r.set('ip_address', '0.0.0.0')
r.set('timestamp', int(time.time()))
r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)')
r.set('last_page_visited', 'account')

d = r.get('ip_address')
print(d)

d = r.get('timestamp')
print(d)

d = r.get('user_agent')
print(d)

d = r.get('last_page_visited')
print(d)
