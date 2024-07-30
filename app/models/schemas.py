from pydantic import BaseModel


# 用户基类, POST请求参数校验
class UserBase(BaseModel):
    username: str
    password: str
    nickname: str


# 用户创建类, POST请求参数校验
class UserCreate(UserBase):
    pass


# 用户更新类, PUT请求参数校验
class UserUpdate(UserBase):
    pass


# 用户详情类, GET请求参数校验
class UserDetail(UserBase):
    id: int = None   # 新增id字段, 用于GET请求参数校验