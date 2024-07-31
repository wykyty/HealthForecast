from pydantic import BaseModel


# 认证请求表单
class AuthRequest(BaseModel):
    type: str   # login or register
    login_type: str = None  # password or examiner
    phone_number: str = None  # 手机号
    password: str = None  # 密码


# 认证响应表单
class AuthResponse(BaseModel):
    status: str  # Y or N or E
    error_msg: str = None  # 错误信息


