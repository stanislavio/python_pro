def make_average_closure():
    total = 0
    count = 0

    def add_to_total_and_count(number):
        nonlocal total, count
        total += number
        count += 1
        return total / count

    return add_to_total_and_count


# Використання замикання
average_closure = make_average_closure()
print(average_closure(5))  # Виведе: 5.0
print(average_closure(10))  # Виведе: 7.5
print(average_closure(15))  # Виведе: 10.0
