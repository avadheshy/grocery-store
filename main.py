from distutils.command.upload import upload
import shutil
from fastapi import FastAPI, Body, Depends,Request,File,UploadFile
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





