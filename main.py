from fastapi import FastAPI # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from schemas import Todo

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(
        status_code=200,
        content={"message": "Welcome to the TODO API"}
    )

todos = []

@app.post("/todos")
def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo

@app.get("/todos")
def get_all_todos():
    return todos