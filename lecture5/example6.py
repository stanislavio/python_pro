from collections import defaultdict


fruits_counter = defaultdict(int)

print(fruits_counter)

fruits = ['apple', 'orange', 'apple']

for fruit in fruits:
    fruits_counter[fruit] += 1

print(fruits_counter)
print(fruits_counter['mango'])


def default_value():
    return 'Not found'


person = defaultdict(default_value)

person['name'] = 'Stas'

print(person)
print(f'Surname: -{person["surname"]}-')
