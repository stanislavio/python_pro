def log_function_call(func):
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()])
        print(f"Виклик функції {func.__name__} з аргументами: {arg_str}")
        result = func(*args, **kwargs)
        return result
    return wrapper


# Використання декоратора
@log_function_call
def add(a, b):
    return a + b


print(add(3, 5))  # Виведе: Виклик функції add з аргументами: 3, 5, Результат: 8

