#https://www.youtube.com/watch?v=rvFsGRvj9jo

from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {"todo_id": 1, "todo_name": "groceries", "todo_description": "groceries to get"}
]

@api.get("/")
def index():
    return {"message": "Hello" }

""" @api.get("/caclulation")
def calculation():
    pass 
    return "" """