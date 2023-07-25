

person = {'name': 'Stas', 'surname': 'Dumi', 'age': 25, 'name': 'Petro2'}

print(person['name'])

person['name'] = 'Petro'

print(person.get('identifier', 'default'))

person['identifier'] = '123'
print(person)

keys = ['name', 'surname']
person1 = dict.fromkeys(keys, 'default')

print(person1)

print(person.keys())
print(person.values())
print(person.items())

for key, value in person.items():
    print(key, value)


person.update({'key': 'unique'})
print(person)

numbers = {number: number**2 for number in range(10)}
print(numbers)
