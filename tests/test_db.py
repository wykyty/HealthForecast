from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.models.user import UserInDB
from app.db.session import dbSession


def query_dbByUsername(username: str, db = dbSession()) -> UserInDB:
    try:
        return db.query(UserInDB, username)
        # return list(filter(lambda x: x.id == id, db.query(UserInDB)))[0]
    except OperationalError:
        return None


if __name__ == '__main__':
    user = query_dbByUsername('19099933340')
    print(user.nickname)