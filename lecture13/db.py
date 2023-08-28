from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())


class Customer(BaseModel):
    __tablename__ = 'customer'

    first_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    updated_at = Column(DateTime, default=datetime.now())
    basket = relationship("Basket", back_populates="customer")

    def __repr__(self):
        return f"{self.first_name} {self.surname}"


class Store(BaseModel):
    __tablename__ = 'store'
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    products = relationship("Product", back_populates="store")


class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, default=0)

    store_id = mapped_column(ForeignKey("store.id"))
    store = relationship("Store", back_populates='products')
    basket = relationship("Basket", back_populates="product")


class Basket(BaseModel):
    __tablename__ = 'basket'

    customer_id = mapped_column(ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates='basket')

    product_id = mapped_column(ForeignKey("product.id"))
    product = relationship("Product", back_populates='basket')


engine = create_engine("postgresql+psycopg2://stas-home:1qaz1qaz@localhost/pro_shop")

Base.metadata.create_all(engine)

