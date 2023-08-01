
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def math_operation(operation, a, b):
    return operation(a, b)


def get_operation(operation):
    if operation == 'add':
        return add

    if operation == 'subtract':
        return subtract

    raise Exception("Operation doesn't found")

result = math_operation(add, 3, 4)

operation = get_operation('add')

print(operation(10, 12))
