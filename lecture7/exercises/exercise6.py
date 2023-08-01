def handle_exception(default_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Виникла помилка: {e}")
                return default_value
        return wrapper
    return decorator


# Використання декоратора
@handle_exception(default_value="Неможливо обчислити")
def divide(a, b):
    return a / b


print(divide(10, 2))  # Виведе: 5.0
print(divide(10, 0))  # Виведе: Виникла помилка: division by zero, Неможливо обчислити
