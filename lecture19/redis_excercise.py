import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def cache(func):
    def wrapper(*args, **kwargs):
        kwargs_str = ".".join([f"{key}={value}" for key, value in kwargs.items()])
        unique_key = f'{func.__name__}:{".".join(map(str, args))}'
        if kwargs_str:
            unique_key += f':{kwargs_str}'
        print(f'generated unique key = {unique_key}')

        cached_data = redis_client.get(unique_key)
        if cached_data:
            print('Received data from cache')
            return cached_data.decode('utf-8')

        print('Calculate data by function')
        result = func(*args, **kwargs)
        redis_client.set(unique_key, result, ex=30)
        return result

    return wrapper


@cache
def operation(num: int, k=1):

    return (num ** k) / k ** 3


result = operation(10, 3)
print(result)

