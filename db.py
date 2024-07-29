from contextlib import contextmanager
from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://health:Health2024***@116.204.83.200:3306/healthdb"
Base = declarative_base()


# 定义POST请求参数模型
class Item(BaseModel):
    username: str
    password: str
    nickname: str


# 用户表
class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, index=True)  # 用户ID 索引
    username = Column(VARCHAR(20),nullable=False, unique=True, index=True)  # 用户账号：手机号
    password = Column(VARCHAR(20), nullable=False)  # 用户密码
    nickname = Column(VARCHAR(20), nullable=False)  # 用户昵称
    checkup_currency = Column(INTEGER, default=0)  # 用户体检币数量


# 体检记录表
class Checkup(Base):
    __tablename__ = "checkups"
    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, index=True)  # 体检记录ID
    user_id = Column(INTEGER, ForeignKey("users.id"), nullable=False, index=True)  # 体检用户ID
    checkup = Column(VARCHAR(20), nullable=False)   # 体检类型


# 创建数据库连接类
class dbSession:
    def __init__(self, db_url=SQLALCHEMY_DATABASE_URL):
        self.engine = create_engine(db_url, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=False)
        self.SessionThreadLocal = scoped_session(self.SessionLocal)

    # 获取数据库连接
    @contextmanager
    def get_db(self):  # 定义上下文管理器
        if self.SessionThreadLocal is None:  # 判断数据库是否连接
            raise Exception("Database not connected")  # 数据库未连接时抛出异常
        session = self.SessionThreadLocal()  # 获取数据库连接
        try:  # 开始事务
            yield session
        finally:
            session.close()

    # 插入数据
    def add(self, record):
        with self.get_db() as session:  # 获取数据库连接
            session.add(record)  # 插入数据
            session.commit()  # 提交事务
            session.refresh(record)  # 刷新数据
            return record.id  # 返回插入数据的id

    # 删除数据
    def delete(self, record):
        record_id = record.id  # 获取删除数据的id
        with self.get_db() as session:  # 获取数据库连接
            session.delete(record)  # 删除数据
            session.commit()  # 提交事务
            return record_id  # 返回删除数据的id

    # 更新数据
    def update(self, record):
        record_id = record.id  # 获取更新数据的id
        with self.get_db() as session:  # 获取数据库连接
            session.update(record)  # 更新数据
            session.commit()  # 提交事务
            return record_id  # 返回更新数据的id

    # 查询数据
    def query(self, model, **kwargs):
        with self.get_db() as session:  # 获取数据库连接
            return session.query(model).filter_by(**kwargs).all()  # 查询数据

    # 获取用户信息
    def get_userById(self, user_id: int):
        with self.get_db() as session:
            return session.query(User).filter_by(id=user_id).all()  # 获取用户信息

    def create_user(self, item: Item):
        user = User(username=item.username, password=item.password, nickname=item.nickname)
        self.add(user)
        return user


if __name__ == "__main__":
    dbsession = dbSession()

    # 插入数据
    user = User(username="12345678901", password="123456", nickname="yty")
    dbsession.add(user)
