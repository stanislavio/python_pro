
# Простий декоратор, який виводить повідомлення перед та після виконання функції
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Початок виконання функції")
        result = func(*args, **kwargs)
        print(result)
        print("Кінець виконання функції")
        return result
    return wrapper


def say_hello():
    print("Привіт!")


# огортаємо функцію в декоратор
say_hello = my_decorator(say_hello)


# альтернатива такому використанню використовувати синтаксис вигляду @
@my_decorator
def say_bye():
    print('Бувай!')

# Виклик функції, що використовує декоратор
say_hello()
say_bye()


import time


def timer(func):
    def wrapper():
        now = time.time()
        func()
        print(f'My function was done with time {time.time() - now}')
    return wrapper


@timer
@my_decorator
def calculate():
    # code of function
    return 10


calculate()


numbers = [1, 2, 3, 4, 4]

my_len = my_decorator(len)

print(my_len(numbers))
