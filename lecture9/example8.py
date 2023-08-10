from dataclasses import dataclass


def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class MyClass:
    @log_method
    def my_method(self, x):
        return x * 2


obj = MyClass()
result = obj.my_method(5)


def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
            print(f"Creating an instance of {cls.__name__}")

        def __getattr__(self, name):
            attr = getattr(self.wrapped, name)
            if callable(attr):
                return log_method(attr)
            return attr

    return Wrapper


@log_class
class MyClass:
    def my_method(self, x):
        return x * 2

    def _hello(self):
        print('Hello')


obj = MyClass()
result = obj.my_method(5)


obj._hello()

