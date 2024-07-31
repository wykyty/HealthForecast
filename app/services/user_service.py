from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.models.schemas import UserCreate
from app.models.user import UserInDB
from app.db.session import dbSession


# 新建用户, 成功返回User对象
def create_user(user: UserCreate, db = dbSession()):
    try:
        new_user = UserInDB(**user.dict())
        db.addRecord(new_user)
        return new_user
    except OperationalError as e:
        print(f"数据库操作出错: {e}")
        return None


# 根据id获取用户
def get_userById(user_id: int, db = dbSession()):
    try:
        user = db.queryById(UserInDB, user_id)
        return user
    except OperationalError as e:
        print(f"数据库操作出错: {e}")
        return None


# 根据用户名获取用户
def get_userByUsername(username: str, db = dbSession()):
    try:
        user = db.queryByUsername(UserInDB, username)
        return user
    except OperationalError as e:
        print(f"数据库操作出错: {e}")
        return None





