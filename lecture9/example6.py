from datetime import datetime


class TimestampMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.created_at = datetime.now()
        cls.updated_at = datetime.now()


class BaseModel(metaclass=TimestampMeta):
    pass


class User(BaseModel):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Product(BaseModel):
    def __init__(self, name, price):
        self.name = name
        self.price = price


user = User("Stas", "stas@gmail.com")
product = Product("Phone", 799)

print(user.created_at)
print(user.updated_at)
print(product.created_at)
print(product.updated_at)
