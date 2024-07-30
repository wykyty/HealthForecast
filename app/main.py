from fastapi import FastAPI
from app.models.schemas import UserCreate
from app.api.users import users_router
from services.user_service import create_user, get_userById

app = FastAPI()
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Health Forecast"}


@app.get("/health/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/health/users/{id}")
async def get_userInfo(id: int):
    user_info = get_userById(id)
    return user_info


@app.post("/health/users/item")
async def create_user(item: UserCreate):
    create_user(item)
    return item

