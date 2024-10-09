from fastapi import FastAPI
from todo import todo_router

app = FastAPI()    # 인스턴스 생성

@app.get('/')    # '/' 라우트
async def welcome():
    return {
        'message': 'Hello World'
    }
    
app.include_router(todo_router)