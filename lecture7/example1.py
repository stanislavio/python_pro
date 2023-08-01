def factorial(n):
    # Базовий випадок: факторіал 0 і 1 дорівнює 1
    if n == 0 or n == 1:
        return 1
    # Рекурсивний виклик для обчислення факторіала
    return n * factorial(n - 1)


# Виклик рекурсивної функції
print(factorial(5))  # Виведе: 120 (5! = 5 * 4 * 3 * 2 * 1)


def sum_recursive1(n):
    if n <= 1:
        return 1
    return n + sum(n - 1)


def fibonacci_recursive(n, m=0):
    if m > n:
        return 0
    return m + fibonacci_recursive(n, m + 1)

print(fibonacci_recursive(5))


# def fibonacci(n):
#     # print(f'Iterate {n}')
#     if n <= 1:
#         return n
#     return fibonacci(n + 1) + fibonacci(n + 2)
#
# print(fibonacci(5))


def fibonacci_by_for(n):
    a, b = 0, 1

    for index in range(n):
        a, b = b, a + b

    return a


print(fibonacci_by_for(14))


def fibonacci_generator():
    a, b = 0, 1

    def inner():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result
    return inner

gen = fibonacci_generator()
print(gen())
print(gen())
print(gen())
print(gen())
print(gen())
