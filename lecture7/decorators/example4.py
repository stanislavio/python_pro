

def format_output_decorator(format_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if format_type == "uppercase":
                return result.upper()
            elif format_type == "lowercase":
                return result.lower()
            else:
                return result
        return wrapper
    return decorator


# Використання декоратора з параметрами
@format_output_decorator(format_type="uppercase")
def get_message():
    return "Hello, World!"


print(get_message())  # Виведе: HELLO, WORLD!
