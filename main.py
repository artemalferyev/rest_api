from http.client import HTTPException
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Task(BaseModel):
    title: str
    status: str = "pending"

class UpdateTask(BaseModel):
        title: str
        status: str

tasks = [
    {"id": 1, "title": "Learn FastAPI", "status": "pending"},
    {"id": 2, "title": "Build REST API", "status": "in progress"},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API."}
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
          raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}

@app.post("/tasks")
def create_task(task: Task):
    new_task = {"id": len(tasks) + 1, "title": task.title, "status": task.status}
    tasks.append(new_task)
    return {"message": "Task added", "task": new_task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: UpdateTask):
    task_data = next((task for task in tasks if task["id"] == task_id), None)
    if task_data is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data["title"] = task.title
    task_data["status"] = task.status
    return {"message": "Task updated", "task": task_data}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted"}