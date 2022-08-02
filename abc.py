
from pymongo import MongoClient 

#engine=create_engine('mongodb+srv://avadheshy2022:1997Avdy@cluster0.a2ic8ii.mongodb.net/?retryWrites=true&w=majority')

client = MongoClient("mongodb+srv://catalogue:catalogue12@cataloguedb.baqy2.mongodb.net/test")
db = client.catalog
collection = db.products
collection.insert_one({'product_id':11,'name':"ftr"})