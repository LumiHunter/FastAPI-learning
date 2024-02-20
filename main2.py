import uvicorn

from fastapi import FastAPI, status, Query, Path

from typing import Optional, List
from pydantic import BaseModel, HttpUrl, Field

app = FastAPI()

inventory = (
    {
        "id": 1,
        "user_id": 1,
        "name": "레전드포션",
        "price": 2500.0,
        "amount": 100,
    },
    {
        "id": 2,
        "user_id": 1,
        "name": "포션",
        "price": 300.0,
        "amount": 50,
    },
)

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge = 0)
    amount: int = Field(
        default=1,
        gt=0,
        le=100,
        title="수량",
        description="아이템 갯수. 1~100개까지 소지 가능"
    )    # JSON을 본문으로(request body) 갖는 요청의 경우 데이터 검증에 Field 객체 사용

class User(BaseModel):
    name: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []    # 중첩모델

class CreateUser(User):    # User를 상속받음
    password: str

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)    # 201 상태코드 추가. FastAPI가 제공!
def create_user(user:CreateUser):    # 요청모델과 응답모델을 구분했다.
    return user

@app.get("/users/me")
def get_user():
    fake_user = User(
        name="FastCampus",
        password="1234",
        inventory= [
            Item(name="무기", price=10000),
            Item(name="방어구", price=12000)
        ]
    )
    return fake_user

@app.get("/users/{user_id}/inventory", response_model=List[Item])
def get_item(
    user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),    # ...(엘립시스): 필수값이란 뜻!
    name: str = Query(None, min_length=1, max_length=2, title="아이템 이름")    # None: 없어도 됨
):    # 경로, 쿼리 매개변수에 대해서는 데이터 검증을 Path, Query 함수에 명시함.
    user_items = []
    for item in inventory:
        if item["user_id"] == user_id:
            user_items.append(item)
    
    response = []
    for item in user_items:
        if name is None:
            response = user_items
        if item["name"] == name:
            response.append(item)
    
    return response

if __name__ == "__main2__":
    uvicorn.run("main2:app", reload=True)