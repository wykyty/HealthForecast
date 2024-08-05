from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from app.models.user import UserCreate
from app.models.auth import AuthRequest
from app.services.user import create_user, get_userByUsername

users_router = APIRouter()


# 处理注册/登录请求表单，成功返回Y，失败返回N，异常返回E
@users_router.post("/auth")
async def user_auth(auth: AuthRequest):
    # 验证请求类型
    if auth.type != "register" and auth.type != "login":
        return JSONResponse({"state": "E", "error_message": "Auth type must be register or login"}, status_code=401)
    if auth.phone_number is None or auth.passwd is None:
        return JSONResponse({"state": "E", "error_message": "Auth username and password must be set"}, status_code=401)

    # 查询用户
    try:
        user_db = get_userByUsername(auth.phone_number)
    except Exception as e:
        return JSONResponse({"state": "E", "error_message": str(e)})

    # 注册
    if auth.type == "register":
        # 用户已存在
        if user_db is not None:
            return JSONResponse({"state": "N", "error_message": "该手机号已经注册"})
        # 创建用户
        user = UserCreate(username=auth.phone_number, password=auth.passwd, nickname="health" + auth.phone_number)
        try:
            create_user(user)
        except Exception as e:
            return JSONResponse({"state": "E", "error_message": str(e)})
        # 注册成功
        return JSONResponse({"state": "Y"})

    # 登录
    if auth.type == "login":
        # 用户不存在
        if user_db is None:
            return JSONResponse({"state": "N", "error_message": "该手机号未注册"})
        # 密码错误
        if user_db.password != auth.passwd:
            return JSONResponse({"state": "N", "error_message": "密码错误"})
        # 登录成功
        return JSONResponse({"state": "Y"})


