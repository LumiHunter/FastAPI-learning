import uvicorn

from fastapi import FastAPI

from typing import Optional, List
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    amount: int = 0

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    inventory: List[Item] = []

@app.post("/users")
def create_user(user:User):
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

if __name__ == "__main2__":
    uvicorn.run("main2:app", reload=True)