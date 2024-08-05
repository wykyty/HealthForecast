from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, IntegrityError, ProgrammingError
from app.models.user import UserInDB, UserCreate
from app.db.session import dbSession


# 新建用户, 成功返回User对象
def create_user(user: UserCreate):
    with dbSession() as db:
        try:
            new_user = db.add(UserInDB, **user.dict())
            return new_user
        except (OperationalError, IntegrityError, ProgrammingError) as e:
            print(f"数据库操作出错: {e}")
        except Exception as e:
            print(f"其他错误: {e}")
    return None


# 根据id获取用户
def get_userById(user_id: int):
    with dbSession() as db:
        try:
            user = db.query(UserInDB, id=user_id)
            return user
        except (OperationalError, IntegrityError, ProgrammingError) as e:
            print(f"数据库操作出错: {e}")
        except Exception as e:
            print(f"其他错误: {e}")
    return None


# 根据用户名获取用户
def get_userByUsername(user_name: str):
    with dbSession() as db:
        try:
            user = db.query(UserInDB, username=user_name)
            return user
        except (OperationalError, IntegrityError, ProgrammingError) as e:
            print(f"数据库操作出错: {e}")
        except Exception as e:
            print(f"其他错误: {e}")
    return None






