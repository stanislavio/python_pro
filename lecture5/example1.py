

numbers = [1, 2, 3, 4, 5]

# new_numbers = numbers + [6, 7, 8]

numbers.extend([6, 7, 8])

numbers.append(9)

numbers.reverse()

numbers.sort()

print(numbers)

numbers = []
for item in range(10):
    if item > 5:
        numbers.append(item)

# list comprehensions

numbers = [number for number in range(10)]

print(numbers)

items = [(1, 1), (2, 4), (3, 9)]

print(items)

items = [(item, item**2) for item in range(1, 5)]
print(items)


print(numbers[3:9:2])

string = 'Hello, world!'

print(string[2:5])

numbers[0] = 3
print(numbers)
