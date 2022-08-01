import shutil
from fastapi import FastAPI, Body, Depends,Request
from fastapi.templating import Jinja2Templates
import schemas
import models
from fastapi import File,UploadFile
import secrets
from typing import List
from fastapi.staticfiles import StaticFiles
# from PIL import Image
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)
templates=Jinja2Templates(directory='template')
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



# @app.post('/img')
# async def root(file:UploadFile=File(...)):
#     with open()

@app.get("/")
def getItems(request:Request,session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    
    return templates.TemplateResponse("home.html",{'request':request,'items':items})

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item


@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item



@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject


@app.delete("/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted...'
