from sqlalchemy.orm import Session

from lecture13.db import engine, Customer, Store, Product
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def get_customers():
    with Session(engine) as session:

        return (
            session.query(Customer)
            .filter(
                Customer.first_name.like('%ah%'),
                Customer.surname.like('%ia%')
            )
            .limit(10)
            .all()
        )


def get_product():

    with Session(engine) as session:
        store = session.query(Store).first()
        for product in store.products:
            print(product.name)


print(get_customers()[0].__dict__)