import imp
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient 
#engine=create_engine('mysql+pymysql://root:#1997Avdy@localhost:3306/grocery')
#engine=create_engine('mongodb+srv://avadheshy2022:1997Avdy@cluster0.a2ic8ii.mongodb.net/?retryWrites=true&w=majority')
# meta=MetaData()
# con=engine.connect()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
client = MongoClient("mongodb+srv://catalogue:catalogue12@cataloguedb.baqy2.mongodb.net/test")
# db = client.catalog
# collection = db.products