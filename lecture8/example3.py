import functools
from functools import wraps


@functools.lru_cache
def some_function(*args):
    return sum(args)


a = some_function(1, 2, 3)
a1 = some_function(1, 2, 3, 4)
a2 = some_function(1, 2, 3)


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def say_hello():
    """
    Function for saying hello
    :return:
    """
    print('say_hello')


say_hello()
print(say_hello.__doc__)
