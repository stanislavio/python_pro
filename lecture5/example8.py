
names = ['stas', 'igor', 'andrew', 'nikita', 'sasha', 'misha', 'petro']

names = ['Anton', 'Stas', 'Nadiia', 'Mihaylo', 'Stanislav', 'a', 'b', 'c', 'd', 'e']

mylist = [{'id': i, 'name': names[i]} for i in range(len(names))]
print(mylist)

mylist = [{'id': idx, 'name': name} for idx, name in enumerate(names)]
print(mylist)
with open('mylist.json','w') as file:
    import json
    json.dump(mylist,file)

print(list(enumerate(names)))
