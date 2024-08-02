import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from app.models.schemas import UserCreate
from app.api.users import users_router
from app.services.user_service import create_user, get_userById

from app.db.session import dbSession
from app.models.user import Base

Base.metadata.create_all(bind=dbSession().engine)

app = FastAPI()
app.include_router(users_router, prefix='/health/user')


@app.get("/")
async def root():
    return {"message": "Health Forecast"}


@app.get("/health/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/health/users/{id}")
async def get_userInfo(id: int):
    user = get_userById(id)
    return user


@app.post("/health/users/item")
async def createUser(item: UserCreate):
    try:
        db_user = create_user(item)
        return db_user
    except Exception as e:
        return {"message": str(e)}


