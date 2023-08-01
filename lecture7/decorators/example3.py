

def call_limit_decorator(max_calls):
    def decorator(func):
        call_count = 0

        def wrapper(*args, **kwargs):
            nonlocal call_count
            if call_count < max_calls:
                call_count += 1
                return func(*args, **kwargs)
            else:
                print(f"Досягнуто максимальної кількості викликів: {max_calls}")
        return wrapper
    return decorator


# Використання декоратора з параметрами
@call_limit_decorator(3)
def greet():
    print("Привіт!")


greet()  # Викличе функцію 3 рази
greet()  # Викличе функцію 2 рази
greet()  # Викличе функцію 1 раз
greet()  # Виведе: Досягнуто максимальної кількості викликів: 3
