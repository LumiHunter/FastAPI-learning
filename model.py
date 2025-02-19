from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Item(BaseModel):
    item: str
    status: str
    
class Todo(BaseModel):
    id: Optional[int]
    item: str
    
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
    
class TodoItem(BaseModel):
    item: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }
        
class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }