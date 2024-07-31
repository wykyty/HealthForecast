from sqlalchemy.orm import Session
from app.models.schemas import UserCreate
from app.models.user import UserInDB
from app.db.session import dbSession


# 新建用户
def create_user(user: UserCreate, db: Session = dbSession()):
    db_user = UserInDB(username=user.username, nickname=user.nickname, password=user.password)
    db.add(db_user)
    return db_user


# 根据id获取用户
def get_userById(id: int, db: Session = dbSession()):
    user = db.query(UserInDB).filter(UserInDB.id == id).first()
    return user


# 根据用户名获取用户
def get_userByUsername(username: str, db: Session = dbSession()):
    return db.query(UserInDB).filter(UserInDB.username == username).all()


