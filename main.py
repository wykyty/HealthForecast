from fastapi import FastAPI

from app.api.users import users_router
from app.api.question import question_router

from app.models.user import UserCreate
from app.services.user import create_user, get_userById

from app.db.session import dbSession
from app.models.user import Base

Base.metadata.create_all(bind=dbSession().engine)

app = FastAPI()
app.include_router(users_router, prefix='/health/user')
app.include_router(question_router, prefix='/health/question')


@app.get("/")
async def root():
    return {"message": "Health Forecast"}


@app.get("/health/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/health/user/{id}")
async def get_userInfo(id: int):
    user = get_userById(id)
    return user


@app.post("/health/user/item")
async def createUser(user: UserCreate):
    try:
        db_user = create_user(user)
        return db_user
    except Exception as e:
        return {"message": str(e)}


