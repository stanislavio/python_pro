def make_sum_closure():
    total = 0

    def add_to_total(number):
        nonlocal total
        total += number
        return total

    return add_to_total


# Використання замикання
sum_closure = make_sum_closure()
print(sum_closure(5))  # Виведе: 5
print(sum_closure(3))  # Виведе: 8
print(sum_closure(10))  # Виведе: 18
