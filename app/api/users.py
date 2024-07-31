from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from app.models.schemas import UserCreate
from app.models.auth import AuthRequest
from app.services.user_service import create_user, get_userByUsername

users_router = APIRouter()


# 处理注册表单，成功返回Y，失败返回E
@users_router.post("/register")
def register_user(auth: AuthRequest):
    if auth.type != "register":
        return JSONResponse({"state": "E", "error_message": "Auth type must be register"}, status_code=401)
    if auth.username is None or auth.password is None:
        return JSONResponse({"state": "E", "error_message": "Auth username and password must be set"}, status_code=401)
    # 查询用户
    try:
        user_db = get_userByUsername(auth.username)
    except Exception as e:
        return JSONResponse({"state": "E", "error_message": str(e)})
    # 用户已存在
    if user_db is not None:
        return JSONResponse({"state": "N", "error_message": "该手机号已经注册"})
    # 创建用户
    user = UserCreate(username=auth.username, password=auth.password, nickname="health"+auth.username)
    try:
        db_user = create_user(user)
        return JSONResponse({"state": "Y"})
    except Exception as e:
        return JSONResponse({"state": "E", "error_message": str(e)})


# 是否登录成功，返回Y/N/E
@users_router.post("/login")
def login_user(auth: AuthRequest):
    if auth.type != "login":
        return JSONResponse({"state": "E", "error_message": "Auth type must be login"}, status_code=401)
    if auth.username is None or auth.password is None:
        return JSONResponse({"state": "E", "error_message": "Auth username and password must be set"}, status_code=401)
    # 查询用户
    try:
        user_db = get_userByUsername(auth.username)
    except Exception as e:
        return JSONResponse({"state": "E", "error_message": str(e)})

    # 用户不存在
    if user_db is None:
        return JSONResponse({"state": "N", "error_message": "该手机号未注册"})
    # 密码错误
    if user_db.password != auth.password:
        return JSONResponse({"state": "N", "error_message": "密码错误"})
    # 登录成功
    return JSONResponse({"state": "Y"})
