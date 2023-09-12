class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


# factory method
def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


dog = get_pet("dog")
print(dog.speak())  # Виведе: "Woof!"
print(dog._name)    # Виведе: "Hope"

cat = get_pet("cat")
print(cat.speak())  # Виведе: "Meow!"
print(cat._name)    # Виведе: "Peace"
