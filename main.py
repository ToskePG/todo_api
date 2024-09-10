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

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}, 404

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            todo.completed = updated_todo.completed
            return todo
    return {"error": "Todo not found"}, 404

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}, 404
