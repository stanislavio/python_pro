import json

with open('example.json', 'r') as file:

    person = json.load(file)
    print(person)

print(json.dumps(person))
