from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models.user import UserInDB as User

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://health:Health2024***@116.204.83.200:3306/healthdb"


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


