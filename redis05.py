# python redis05.py

import redis

import time
import logging 

r = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None)

#Create and configure logger 
logging.basicConfig(filename="redisfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 

# save to file
#logging.basicConfig( level=logging.DEBUG, filename='example.log')

                    
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 


# Strings
  
# Create string value
r.set('index', '1')
logger.info(f"index: {r.get('index')}")

# Increment string by 1
r.incr('index')
logger.info(f"index: {r.get('index')}")

# Decrement string by 1
r.decr('index')
logger.info(f"index: {r.get('index')}")

# Increment string by 3
r.incrby('index', 3)


# Lists

r.lpush('my_list', 'A')
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")

# Push second string to list from the right.
r.rpush('my_list', 'B')
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")

# Push third string to list from the right.
r.rpush('my_list', 'C')
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")

# Remove 1 instance from the list where the value equals 'C'.
r.lrem('my_list', 1, 'C')
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")

# Push a string to our list from the left.
r.lpush('my_list', 'C')
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")

# Pop first element of our list and move it to the back.
r.rpush('my_list', r.lpop('my_list'))
logger.info(f"my_list: {r.lrange('my_list', 0, -1)}")


# Sets

# Add item to set 1
r.sadd('my_set_1', 'Y')
logger.info(f"my_set_1: {r.smembers('my_set_1')}'")

# Add item to set 1
r.sadd('my_set_1', 'X')
logger.info(f"my_set_1: {r.smembers('my_set_1')}'")

# Add item to set 2
r.sadd('my_set_2', 'X')
logger.info(f"my_set_2: {r.smembers('my_set_2')}'")

# Add item to set 2
r.sadd('my_set_2', 'Z')
logger.info(f"my_set2: {r.smembers('my_set_2')}'")

# Union set 1 and set 2
logger.info(f"Union: {r.sunion('my_set_1', 'my_set_2')}")

# Interset set 1 and set 2
logger.info(f"Intersect: {r.sinter('my_set_1', 'my_set_2')}")


## Sorted Sets

# Initialize sorted set with 3 values
r.zadd('top_songs_set', {'Never Change - Jay Z': 1,
                         'Rich Girl - Hall & Oats': 2,
                         'The Prayer - Griz': 3})
logger.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")

# Add item to set with conflicting value
r.zadd('top_songs_set', {'Can\'t Figure it Out - Bishop Lamont': 3})
logger.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")

# Shift index of a value
r.zincrby('top_songs_set', 3, 'Never Change - Jay Z')
logger.info(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}'")


# Hashes

record = {
    "name": "Hackers and Slackers",
    "description": "Mediocre tutorials",
    "website": "https://hackersandslackers.com/",
    "github": "https://github.com/hackersandslackers"
}

# redis_server.hset(key, value, number)
#r.hset('business', record, 1)
#logger.info(f"business: {r.hgetall('business')}")


