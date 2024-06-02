from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int):    # 타입 힌트
    return {"item_id": item_id}

@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# 타입 힌트: 고급형(리스트, 딕셔너리)

@app.get("/list_items")
async def read_items(q: List[int] = Query([])):
    return {"q": q}

@app.post("/create_item")
async def create_item(item: Dict[str, int]):
    return item