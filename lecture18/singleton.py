class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.value = None
        return cls._instance

    def __init__(self, value):
        if self.value is None:
            self.value = value


singleton1 = Singleton("Hello")
print(singleton1.value)  # Виведе: Hello

singleton2 = Singleton("World")
print(singleton2.value)  # Виведе: Hello (так як це той самий екземпляр)

print(singleton1 is singleton2)

