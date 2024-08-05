from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey, DateTime, Enum, JSON
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, validator
from typing import Optional, List, Dict

Base = declarative_base()


# 体检问卷(存放在数据库中)
class Questionnaire(Base):
    __tablename__ = 'questionnaire'

    id = Column(INTEGER, primary_key=True, nullable=False)  # 问卷id
    title = Column(VARCHAR(50), nullable=False, index=True, unique=True)  # 问卷对应的人体系统
    description = Column(VARCHAR(500), nullable=False)  # 问卷描述
    content = Column(JSON, nullable=False)  # 问卷内容
    answer = Column(JSON, nullable=False)  # 问卷答案


# 体检问卷作答
class Questionnaire_answer(Base):
    __tablename__ = 'questionnaire_answer'

    id = Column(INTEGER, primary_key=True, nullable=False)  # 问卷答案id
    time = DateTime(timezone=True)  # 问卷答案提交时间
    questionnaire_id = Column(INTEGER, ForeignKey('questionnaire.id'), nullable=False)  # 问卷id
    content = Column(JSON, nullable=False)  # 问卷答案内容
    user_id = Column(INTEGER, ForeignKey('users.id'), nullable=False)  # 用户id
    score = Column(INTEGER, nullable=False)  # 问卷答案得分
    suggestion = Column(VARCHAR(500), nullable=False)   # 建议


# 体检表请求表单
class QuestionRequest(BaseModel):
    phone_number: str
    system: str

    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.isdigit() or len(v) != 11:
            raise ValueError('Invalid phone number')
        return v


class Question(BaseModel):
    question: str
    options: List[str]
    can_choose_count: int


class Content(BaseModel):
    title: str
    description: str
    questions: Dict[str, Question]


# 体检表请求响应
class QuestionResponse(BaseModel):
    id: Optional[int] = None  # 问卷id = questionnaire.id
    content: Optional[Content] = None  # 问卷内容
    state: str   # "Y" or "E"
    error_message: str = None   # 错误信息


# 体检表得分请求表单
class QuestionScoreRequest(BaseModel):
    id: int  # 问卷id
    phone_number: str
    answers: List[List[int]]

    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.isdigit() or len(v) != 11:
            raise ValueError('Invalid phone number')
        return v


class QuestionScoreResponse(BaseModel):
    id: int = None  # 问卷id
    score: int = None  # 得分
    state: str   # "Y" or "E"
    error_message: str = None   # 错误信息
