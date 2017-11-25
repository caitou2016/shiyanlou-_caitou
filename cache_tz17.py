import redis
from functools import wraps
import json

class RedisCache:
    def __init__(self,redis_client):
        self._redis = redis_client

    def cache(self,timeout=0):
        def decorator(func):
            @wraps(func)
            def wrapper(*arg,**kw):
                if timeout==0:
                    func(*arg,**kw)

                key=func.__name__
                value = self._redis.get(key)
                if not value:
                    content = func(*arg,**kw)
                    self._redis.setex(key,timeout,json.dumps(content))
                    return content
                else:
                    return json.loads(value.decode())
            return wrapper
        return decorator

r=redis.StrictRedis(host='127.0.0.1')
cache= RedisCache(r)

@cache.cache(timeout=10)
def execute():
    return 'hello world'

x=execute()
result = json.loads(r.get(execute.__name__).decode())
t = r.ttl(execute.__name__)
print(result,t,x)
