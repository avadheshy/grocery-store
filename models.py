
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base 
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

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
    product_id=Column(Integer)
    category=Column(String(256))
    image=column(URLType)
    price=Column(Integer)
    description=Column(String(256))

class Order(Base):
    ____tablename__='orders'
    order_id=Column(Integer)
    user_id=Column(String(256) )
    product_id=Column(String(256)
    
class Payment(Base):
    ____tablename__='payments'
    id=Column(Integer)
    user=Column(Integer) # foreign key for user
    product=Column(Integer) # foreign key for product
    price=Column(Integer) 
    status=Column(Boolean) 
"""