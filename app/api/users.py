from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import UserCreate
from app.models.auth import AuthResponse, AuthRequest
from app.services.user_service import create_user, get_userByUsername

users_router = APIRouter()


@users_router.post("/register/", response_model=UserCreate)
def register_user(user: UserCreate):
    db_user = create_user(user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user


# 是否登录成功，返回Y/N/E
@users_router.post("/login/", response_model=AuthResponse)
def login_user(auth: AuthRequest):
    user_db = get_userByUsername(auth.username)
    if user_db is None:
        return AuthResponse(status="E")
    # 密码错误
    if user_db.password!= auth.password:
        return AuthResponse(status="N")
    return AuthResponse(status="Y")
