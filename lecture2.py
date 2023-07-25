

def get_value_from_keyboard(input_msg):
    attempt = 1
    while attempt < 4:
        try:
            value = int(input(f'Input real digit for {input_msg}: '))
            return value
        except ValueError as error:
            print('It is not a digit, please try one more time: ')
            attempt += 1
            continue


if __name__ == '__main__':
    a = get_value_from_keyboard('a')
    b = get_value_from_keyboard('b')
    c = get_value_from_keyboard('c')
    v = get_value_from_keyboard('v')

    result = None

    try:
        if a and b:
            result = a / b / c / v
    except ZeroDivisionError as error:
        print("Sorry we can't divide by zero")
    else:
        print(f'Result {a} / {b} = {result}')
    finally:
        print('Good bye!')
