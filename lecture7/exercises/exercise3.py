def fibonacci_generator():
    a, b = 0, 1

    def generate_next():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return generate_next


# Використання замикання
fib_gen = fibonacci_generator()
for i in range(10):
    print(fib_gen())  # Виведе: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
