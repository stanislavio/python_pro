import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper


# Використання декоратора
@timer
def slow_function():
    time.sleep(3)
    print("Функція виконана")


slow_function()
