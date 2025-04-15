from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from typing import List, Optional
import random

# Create FastAPI app
app = FastAPI(title="Demo API")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
class Task(BaseModel):
    id: int
    title: str
    completed: bool

tasks = [
    Task(id=1, title="Learn Python", completed=True),
    Task(id=2, title="Build FastAPI server", completed=False),
    Task(id=3, title="Connect with React", completed=False),
]

# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the Python + React Demo API"}

@app.get("/api/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/api/tasks/{task_id}", response_model=Optional[Task])
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return None

@app.post("/api/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/api/random")
def get_random_number():
    return {"number": random.randint(1, 1000)}

# Run the server
if __name__ == "__main__":
    print("Starting FastAPI server...")
    print("Install dependencies with: uv pip install fastapi uvicorn")
    print("Run with: uvicorn server:app --reload")
    uvicorn.run(app, host="0.0.0.0", port=8000)
