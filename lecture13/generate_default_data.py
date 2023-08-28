from random import random, randint

from faker import Faker
from sqlalchemy.orm import Session

from lecture13.db import Customer, Product, engine
fake = Faker()


def generate_customers(count: int = 100):

    customers = [
        Customer(
            first_name=(lambda: fake.name().split()[0])(),
            surname=(lambda: fake.name().split()[1])(),
            email=fake.ascii_free_email(),
            phone=fake.msisdn()
        ) for _ in range(count)
    ]

    with Session(engine) as session:
        session.add_all(customers)
        session.commit()


def generate_products(count: int = 100):

    products = [
        Product(
            name=fake.name(),
            price=randint(50, 1000),
            description=fake.text(),
            store_id=1,
        ) for _ in range(count)
    ]

    with Session(engine) as session:
        session.add_all(products)
        session.commit()

