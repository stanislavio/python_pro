def odd_number_generator():
    number = 1

    def generate_next():
        nonlocal number
        result = number
        number += 2
        return result

    return generate_next


# Використання замикання
odd_gen = odd_number_generator()
for i in range(5):
    print(odd_gen())  # Виведе: 1, 3, 5, 7, 9
