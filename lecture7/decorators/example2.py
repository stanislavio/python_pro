
def greeting_decorator(greeting_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(greeting_message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Використання декоратора з параметрами
@greeting_decorator("Привіт, дорогий!")
def say_hello(name):
    print(f"Привіт, {name}!")


say_hello("Іван")
# Виведе:
# Привіт, дорогий!
# Привіт, Іван!
