from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


DATABASE_URL = "mysql+pymysql://health:Health2024***@116.204.83.200:3306/healthdb"


# 创建数据库连接类
class dbSession:
    def __init__(self, db_url=DATABASE_URL):
        self.engine = create_engine(db_url, pool_pre_ping=True)
        self.Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine, expire_on_commit=False))
        self.session = self.Session()

    def query(self, model, **kwargs):
        return self.session.query(model).filter_by(**kwargs).first()

    def add(self, model, data: dict):
        obj = model(**data)
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete(self, model, **kwargs):
        obj = self.query(model, **kwargs)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False

    def close(self):
        self.session.close()
        self.Session.remove()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        self.session.close()
