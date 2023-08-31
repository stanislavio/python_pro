1.
Які
типи
даних
є
в
мові
програмування
Python?
2.
Змінні
і
не
змінні
типи
даних:
dict, list, set - muttable
int, str, float, frozenset, bool, tuple - immutable

a = {'a': 'c'}

b = 1
b = 2

a = 'Hello, world!'
a.replace('world', 'city')
b = a[::-1]

3. Функції


def func():
    pass


lambda a, b:
return a + b

args - arguments
kwargs - key / value
arguments


def func(*args, **kwargs):
    pass


4. Декоратор

from functools import wraps


def banch_mark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(time.now())


a = func(*args, **kwargs)
print('Yhis function return something like this = {a}')


@banch_mark
def hello(name: str):
    return f'Hello, {name}'


a = [1, 2, 3]

iter(a)
a.__iter__()
next(a)


def generate():
    yield 1


with open('filename.txt', 'r') as f:
    ...


class MyClass:
    ...
    # __enter__
    # __exit__

with MyClass() as obj:
    ...


def my_cntx_manager():
    file = open()
    yield file
    file.close()

with my_cntx_manager() as obj
    ...

try:

    1 / 0
except DivisionByZero as error:
    print(error)
else:
    print('My else')
finally:
    print('Finally')


class Person:
    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self._email = email
        self.__password = '123456'


class Workable(ABC):

    def work(self):
        raise NotImplemented()


class Employee(Person, Workable):
    def __init__(self, *args, salary, **kwargs):
        super().__init__(*args, **kwargs)


self.salary = salary


def work():
    print("I'm working")





