from distutils.command.upload import upload
import shutil



from fastapi import FastAPI, Body, Depends,Request,File,UploadFile
from fastapi.templating import Jinja2Templates
import schemas
import models
from fastapi import File,UploadFile
from typing import List
from fastapi.staticfiles import StaticFiles
from database import prod_table
# from PIL import Image
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

#from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

#Base.metadata.create_all(engine)
templates=Jinja2Templates(directory='template')
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get('/')
async def index(request:Request):
    all_products=prod_table.find()
    return templates.TemplateResponse("home.html",{'request':request,'items':all_products})
    

@app.post("/additem")
async def addItem():
    for i in range(100):
        print('hello')
    item=dict(item)
    print(item)
    prod_table.insert_one(item)
    return templates.TemplateResponse("additem.html")

@app.get('/add')
async def add(request:Request):
    print('hello')
    if request.method=='POST':
        print('hello')

    return templates.TemplateResponse("additem.html",{'request':request})


