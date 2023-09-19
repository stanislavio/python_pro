import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('YOURKEY', 'your_value')

value = r.get('YOURKEY')
print(value.decode()
      )

r.rpush('YOURLIST', b"{'hello': '1'}")
r.rpush('YOURLIST', 'item2')

elements = r.lrange('YOURLIST', 0, -1)
print(elements)

r.close()
