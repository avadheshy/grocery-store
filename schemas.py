from pydantic import BaseModel, HttpUrl
from bson import ObjectId


class Product(BaseModel):
    name:str
    category:str
    price:int
    description:str
