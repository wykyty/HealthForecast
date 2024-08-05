from sqlalchemy.exc import OperationalError
from app.models.question import Questionnaire, Questionnaire_answer
from app.db.session import dbSession


# 根据问卷标题（某个系统）获取问卷
def get_questionnaireByTitle(title: str):
    with dbSession() as db:
        try:
            ques = db.query(Questionnaire, title=title)
            return ques
        except OperationalError as e:
            print(e)
            return None


# 根据问卷id获取问卷答案
def get_questionnaire_answerByQId(q_id: int):
    with dbSession() as db:
        try:
            answer = db.query(Questionnaire_answer, questionnaire_id=q_id)
            return answer
        except OperationalError as e:
            print(e)
            return None


# 根据问卷答案、用户作答情况获取得分
def get_score(user_answer: list, answer: list, power: list):
    power = [1 for i in user_answer] if power is None else power
    scores = []
    for ind in range(len(user_answer)):
        score = 0
        for i in user_answer[ind]:
            if i in answer[ind]:
                score += 1
            else:
                score -= 1
        score /= len(answer[ind])  # 这里未事先设置权重所以默认使用答案个数作为总分
        scores.append(0 if score<0 else score)
    power_normal = [10*i/sum(power) for i in power]
    re = sum([score*power for score, power in zip(scores,power_normal)])
    return re
