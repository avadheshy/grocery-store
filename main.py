from fastapi import FastAPI,Depends
from sqlalchemy import Column,String,Integer,Boolean
from database import SessionLocal, engine,Base
# import model
from pydantic import  BaseModel
# model.Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import Session
app = FastAPI()

# models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True)
    #is_active=Column(Boolean,default=True)

# schema
class UserSchema(BaseModel):
    id:int
    email:str
    is_active=bool

    class config:
        orm_mode=True

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users",response_model=UserSchema)
def index(user:UserSchema,db:Session=Depends(get_db)):
    # db work will be here
    new_user=User(email=user.email,id=user.id,is_active=user.is_active)
    db.add(new_user)
    db.commit()
    return new_user


@app.get("/users",response_model=list[UserSchema])
def index(user:UserSchema,db:Session=Depends(get_db)):
    return db.quary(User).all()
