from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from app.models.question import QuestionRequest, QuestionResponse, QuestionScoreRequest, QuestionScoreResponse
from app.services.question import get_questionnaireByTitle, get_questionnaire_answerByQId, get_score
from app.services.user import get_userByUsername

question_router = APIRouter()


# 获取体检表的请求
@question_router.post("/questionnaire")
async def get_questionnaire(request: QuestionRequest):
    username = request.phone_number
    title = request.system

    # 查询用户
    try:
        user = get_userByUsername(username)
    except Exception as e:
        return JSONResponse({"state": "E", "error": str(e)}, status_code=400)
    # 用户不存在
    if user is None:
        return JSONResponse({"state": "E", "error": "User not found"}, status_code=400)

    # 查询问卷
    try:
        questionnaire = get_questionnaireByTitle(title)
    except Exception as e:
        return JSONResponse({"state": "E", "error": str(e)}, status_code=400)
    # 问卷不存在
    if questionnaire is None:
        return JSONResponse({"state": "E", "error": "Questionnaire not found"}, status_code=400)

    return QuestionResponse(
        id=questionnaire.id,
        content=questionnaire.content,
        state="Y"
    )


# 获取体检表得分的请求
@question_router.post("/submit")
async def get_questionnaire_score(request: QuestionScoreRequest):
    user_answer = request.answers
    try:
        answer = get_questionnaire_answerByQId(request.id)
    except Exception as e:
        return JSONResponse({"state": "E", "error": str(e)}, status_code=400)
    # 答案不存在
    if answer is None:
        return JSONResponse({"state": "E", "error": "Answer not found"}, status_code=400)

    score = get_score(user_answer, answer)

    return QuestionScoreResponse(
        id=request.id,
        score=score,
        state="Y"
    )
