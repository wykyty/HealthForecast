from pydantic import BaseModel, validator


# 用户基类, POST请求参数校验
class UserBase(BaseModel):
    username: str  # 手机号
    password: str
    nickname: str = None  # 昵称


# 用户创建类, POST请求参数校验
class UserCreate(UserBase):
    @validator('username')  # 每一位都是数字，长度为11的手机号
    def username_validate(cls, v):
        # 手机号长度为11
        if len(v) != 11:
            return ValueError('手机号长度不正确')
        # 手机号每一位都是数字
        if not v.isdigit():
            return ValueError('手机号必须是数字')
        return v

    @validator('password')  # 密码长度为6-20位
    def password_validate(cls, v):
        if len(v) < 6 or len(v) > 20:
            return ValueError('密码长度必须在6-20位之间')
        return v

    @validator('nickname')  # 昵称长度为2-20位
    def nickname_validate(cls, v):
        if len(v) < 2 or len(v) > 20:
            return ValueError('昵称长度必须在2-20位之间')
        return v


# 用户更新类, PUT请求参数校验
class UserUpdate(UserBase):
    pass


# 用户详情类, GET请求参数校验
class UserDetail(UserBase):
    id: int = None   # 新增id字段, 用于GET请求参数校验
