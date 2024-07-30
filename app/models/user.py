from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserInDB(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, index=True)  # 用户ID 索引
    username = Column(VARCHAR(20), nullable=False, unique=True, index=True)  # 用户账号：手机号
    password = Column(VARCHAR(20), nullable=False)  # 用户密码
    nickname = Column(VARCHAR(20), nullable=False)  # 用户昵称
    checkup_currency = Column(INTEGER, default=0)  # 用户体检币数量


# 体检记录表
class Checkup(Base):
    __tablename__ = "checkups"
    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, index=True)  # 体检记录ID
    user_id = Column(INTEGER, ForeignKey("users.id"), nullable=False, index=True)  # 体检用户ID
    checkup = Column(VARCHAR(20), nullable=False)   # 体检类型
