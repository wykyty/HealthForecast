from sqlalchemy.orm import Session
from app.models.schemas import UserCreate
from app.models.user import UserInDB
from app.db.session import dbSession


def create_user(user: UserCreate, db: Session = dbSession()):
    db_user = UserInDB(username=user.username, nickname=user.nickname, password=user.password)
    db.add(db_user)
    return db_user
