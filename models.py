
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base 
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(256),primary_key=True,unique=True)
    first_name=Column(String(256))
    last_name=Column(String(256))
    email = Column(String(50), unique=True)
    phone = Column(Integer,unique=True)
    age=Column(Integer)
    address=Column(String(256))
    payments=relationship("Payment",back_populates="person")
    orders = relationship("Order", back_populates="buyer")


class Product(Base):
    __tablename__='products'
    name=Column(String(256))
    id=Column(Integer,primary_key=True,unique=True)
    category=Column(String(256))
    img=Column(URLType)
    price=Column(Integer)
    description=Column(String(256))
    is_active=Column(Boolean)
    orders = relationship("Order", back_populates="product")
    payments=relationship("Payment", back_populates="product")
    
    

class Order(Base):
    __tablename__='orders'
    id=Column(Integer,primary_key=True,unique=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    product_id=Column(Integer,ForeignKey("products.id"))
    buyer = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")


    
class Payment(Base):
    __tablename__='payments'
    payment_id=Column(Integer,primary_key=True,unique=True)
    user_id=Column(Integer,ForeignKey("users.id")) 
    product_id=Column(Integer,ForeignKey("products.id")) 
    price=Column(Integer) 
    status=Column(Boolean) 
    product=relationship("Product", back_populates="payments")
    person=relationship("User",back_populates="payments")

