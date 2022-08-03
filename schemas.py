from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    username:str
    email:str
    phone_number: str
    address:str
    password:str
class Product(BaseModel):
    #sku:str  = Field(...)
    product_id:int
    title:str = Field(...)
    description:str = Field(...)
    #manufacture_details:dict = Field(...)
    # color:list = Field(...)
    category:list = Field(...)
    price:float = Field(...)
    # offer_price: float = Field(...)
    # your_saving:float = Field(...)
    is_available:Optional[bool]=True
    quantity:int = Field(...)
    # order_quantity:int=Field(..., gt=0, lt=6)
    #shipping_details:dict = Field(...)

class Cart(BaseModel):
    id:int
    status:str
    quantity:int
    total:float
    product_id:list

class Transaction(BaseModel):
    id:int
    created_on:datetime
    shiping:dict
    tracking:dict
    payment:dict
    products:dict