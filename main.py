from sqlalchemy.orm import Session
from distutils.command.upload import upload
from operator import itemgetter
import shutil

from fastapi import FastAPI, Body, Depends, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
import schemas
import models
from fastapi import File, UploadFile
from typing import List
from fastapi.staticfiles import StaticFiles
from database import prod_table
from starlette.responses import RedirectResponse

# from PIL import Image
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

#from database import Base, engine, SessionLocal

# Base.metadata.create_all(engine)
templates = Jinja2Templates(directory='template')


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get('/')
async def index(request: Request):
    all_products = prod_table.find()
    return templates.TemplateResponse("home.html", {'request': request, 'items': all_products})


@app.post("/additem")
async def addItem(product_id: int = Form(), title: str = Form(), description: str = Form(),
                  category: str = Form(), quantity: int = Form(), price: float = Form()):
    item = {}
    item['product_id'] = product_id
    item['title'] = title
    item['description'] = description
    item['category'] = category
    item['quantity'] = quantity
    item['price'] = price
    prod_table.insert_one(item)

    return "one item added"


@app.get('/add')
async def add(request: Request):

    return templates.TemplateResponse("additem.html", {'request': request})


@app.get('/{id}')
def find(id, request: Request):
    obj = prod_table.find_one({ 'product_id': int(id) })
    return templates.TemplateResponse("one_item.html", {'request': request, 'items': obj})



@app.put("/updateitem")
async def updateitem(product_id: int = Form(), title: str = Form(), description: str = Form(),
                  category: str = Form(), quantity: int = Form(), price: float = Form()):
    item = {}
    filter = {'product_id':product_id}
    item['product_id'] = product_id
    item['title'] = title
    item['description'] = description
    item['category'] = category
    item['quantity'] = quantity
    item['price'] = price
    newvalues = { "$set": item }
    prod_table.update_one(filter,newvalues)

    return "one item added"