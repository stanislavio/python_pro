
def func(*args, **kwargs):
    print(f'Args = {args}')
    print(f'Args = {kwargs}')


# func(
#     1, 'dsfds', (1, 2, 3), [123, 3], {'key': 'value'},
#     key1='sdlsd', key2={'fdna': 'dsfds'},
#     ndfs=123
# )

# def generate():
#     for item in range(10):
#         yield item


try:
    1 / 1
    import dlsnfd
except ZeroDivisionError as error:
    print(error)
except ImportError as error:
    print(error)
except Exception as error:
    print('exception')
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


class Horse:
    def __init__(self):
        ...


class Employee(Person, Horse):
    def __init__(self, *args, salary, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary


print(Employee.__mro__)
