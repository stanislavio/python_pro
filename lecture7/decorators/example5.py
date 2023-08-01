

def handle_exception(default_value):
    print('Handle exception')

    def decorator(func):
        print('decorator')

        def wrapper(*args, **kwargs):
            print('wrapper')
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as err:
                print(f'Виникла помилка {err}')
                return default_value

        return wrapper

    return decorator


@handle_exception(default_value=0)  # decorator(divide)
def divide(a, b):
    return a / b


print(divide(10, 0))
