from fastapi import FastAPI
from app.db.session import dbSession
from app.models.schemas import UserCreate
from app.api.users import users_router

app = FastAPI()
app.include_router(users_router)
dbsession = dbSession()


@app.get("/")
async def root():
    return {"message": "Health Forecast"}


@app.get("/health/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/health/users/{id}")
async def get_userInfo(id: int):
    user_info = dbsession.get_userById(id)
    return user_info


@app.post("/health/users/item")
async def create_user(item: UserCreate):
    dbsession.create_user(item)
    return item

