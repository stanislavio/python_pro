"""
Intro to python
"""

name = 'Stas'
surname = 'Dumi'
full_name = surname + ' ' + name

full_name = f'{surname} {name}'

full_name = 'Hello, {} {}'.format(surname, name)

full_name = 'Hello, %(name)s %(surname)s' % {
    'name': name,
    'surname': surname
}

age = 24.73024

new_age = age - 10

is_young = True  # False

# Data structure
#       0           1        2         3
names = ['Stas', 'Artur', 'Andrew', 'Sasha', 'Sasha']
names[0] = 'New Stas Value'
print('Before,', names)

names.append('Anya')

print('After append,', names)

names.extend(['Olga', 'Roksolana'])

print('After extend,', names)

# Dictionary

people = {
    'FU218439': {
        'name': 'Stas',
        'surname': 'Dumi',
        'birthday': '13.01',
        'ethnicity': 'Ukrainian'
    },
    'FU138043': {
        'name': 'Petro',
        'surname': 'Isbf',
        'birthday': '15.06',
        'ethnicity': 'Ukrainian',
        'key': {
            'hello': 'world'
        }
    }
}

print(people['FU138043']['key'])

# Set

names = frozenset({'Stas', 'Artur', 'Andrew', 'Sasha', 'Sasha'})

print('Intersection, ', names.intersection({'Artur', 'Andrew', 'Igor'}))
print('Set, ', names)

# Tuple

names = ('Andrew', 'Sasha', 'Sasha')
print('Tuple, ', names)

print('Name, first item,', name[0:4])


# Mutable & Immutable

# Immutable
# int, str, bool, tuple, frozenset

# Mutable
# List, Set, Dict

name = 'Stas'
print(f'Identifier for {name} = ', id(name))
name = name.replace('s', 'a')
print(f'Identifier for {name} = ', id(name))
surname = 'Dumi'
print(f'Identifier for {surname} = ', id(surname))

age = 2
print(f'Identifier for age = {age} = ', id(age))
age = 4
print(f'Identifier for age = {age} = ', id(age))
new_age = 2
print(f'Identifier for new_age = {new_age} = ', id(new_age))

# Immutable

names = ['Andrew', 'Stas']
print(f'Identifier for names = {names} = ', id(names))
names.append('Igor')
print(f'Identifier for names = {names} = ', id(names))
