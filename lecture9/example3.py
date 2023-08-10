

class Example:

    def method(self):
        print('method')

    def __setattr__(self, key, value):
        print(f'Setattr {key} = {value}')
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        print(f'Getattribute {item}')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print(f"Accessing the attribute {item}, but it's not found.")
        return None

    def __len__(self):
        return 24


example = Example()
example.attr = 'Hello'
setattr(example, 'new_attr', 'new_value')
print(example.attr)
print(getattr(example, 'unknown_attr'))

example.method()

numbers = [1, 2, 3, 4]

print(len(numbers))

print(len(example))

