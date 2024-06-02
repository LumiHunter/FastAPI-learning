import uvicorn

from fastapi import FastAPI, Header

from typing import Optional
from enum import Enum

app = FastAPI()

class UserLevel(str, Enum):
    master = "마스터"
    member = "멤버"

@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}    # X-는 사용자 정의 헤더라는 뜻.

@app.get("/users/{user_id}")
def get_user(user_id: int):    # URL은 전부 문자열이기 때문에 타입 힌트 int 작성
    return {"user_id": user_id}

@app.get("/users/me")
def get_current_user():
    return {"user_id": 123}   # FastAPI는 위에서 아래로 경로를 검사하기 때문에, /users/me 라는 경로는 위 /users/{user_id}에 붙어서 오류가 발생한다.

@app.get("/users")    # 경로에 limit가 없으므로, fastAPI는 limit가 경로 매개변수가 아닌 쿼리 매개변수임을 알아본다.
def get_users(limit: Optional[int] = None):    # limit=None 이면 값이 없어도 된다는 뜻이 됨
    return {"limit": limit}

@app.get("/admin_users")
def get_users(is_admin: bool, limit = 100):
    return {"is_admin": is_admin, "limit": limit}

@app.get("/master_users")
def get_users(grade: UserLevel = UserLevel.member):    # 기본값을 member로 지정
    return {"grade": grade}    # /master_users?grade={"마스터"가 인코딩된 것}으로 보내야 함.

if __name__ == "__main1__":
    uvicorn.run("main1:app", reload=True)