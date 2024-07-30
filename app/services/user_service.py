from sqlalchemy.orm import Session
from app.models.schemas import UserCreate
from app.models.user import UserInDB
from app.db.session import dbSession


# 新建用户
def create_user(user: UserCreate, db: Session = dbSession()):
    db_user = UserInDB(username=user.username, nickname=user.nickname, password=user.password)
    db.add(db_user)
    return db_user


# 根据用户名获取用户
def get_userById(user_id: int, db: Session = dbSession()):
    return db.query(UserInDB).filter(UserInDB.id == user_id).all()
