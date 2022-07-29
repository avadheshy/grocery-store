
from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
"""
class User(Base):
    __tablename__='users'
    username=Column(String(256),primary_key=True,unique=True)
    first_name=Column(String(256))
    last_name=Column(String(256))
    email = Column(String(50), unique=True)
    phone = Column(Integer,unique=True)
    age=Column(Integer,unique=True)
    address=Column(String(256))

class Product(Base):
    ____tablename__='products'
    name=Column(String(256))
    id=Column(Integer)
    category=Column(String(256))
    image=Column(Integer)
    price=Column(Integer)
    description=Column(Integer)

class Order(Base):
    ____tablename__='orders'
    id=Column(Integer)
    user=Column(String(256))
    product_name=Column(String(256))

class Payment(Base):
    ____tablename__='payments'
    id=Column(Integer)
    user_id=Column(Integer)
    product_id=Column(Integer)
    product_name=Column(String(256))


"""