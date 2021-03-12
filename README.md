# Python_-_Redis
Python_-_redis

# 1. Install redis 

[LINUX]
sudo apt install python3-pip
sudo systemctl start redis

[MAC]
brew services start redis

[WINDOWS]

last file .msi of Redis
https://github.com/MicrosoftArchive/redis/releases
https://github.com/microsoftarchive/redis/releases/tag/win-3.2.100
MEMORY ASSIGMENT : 100 MB (can be chaged later)
.
[CMD]
redis-cli
loclhost:6379
.
ping
rpta : PONG
.
exit

[WINDOWS]
https://pypi.org/project/redis/
pip install redis

# 2 Test Redis
127.0.0.1:6379> SET Bahamas Nassau
OK
127.0.0.1:6379> SET Croatia Zagreb
OK
127.0.0.1:6379> GET Croatia
"Zagreb"
127.0.0.1:6379> GET Japan
(nil)
.
>>> capitals = {}
>>> capitals["Bahamas"] = "Nassau"
>>> capitals["Croatia"] = "Zagreb"
>>> capitals.get("Croatia")
'Zagreb'
>>> capitals.get("Japan")  # None
.
Type	Commands
Sets	SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE
Hashes	HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, HSETNX, HSTRLEN, HVALS
Lists	BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, RPOPLPUSH, RPUSH, RPUSHX
Strings	APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN

# 3 Run Programs
python redis01.py
...
python redis06.py



