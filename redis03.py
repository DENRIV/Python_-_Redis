# python redis03.py

import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def helloRedis():
    try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")

        # Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)        
   
    except Exception as e:
        print(e)

if __name__ == '__main__':
    helloRedis()