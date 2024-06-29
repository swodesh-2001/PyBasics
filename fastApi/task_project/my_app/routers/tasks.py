from fastapi import APIRouter, HTTPException, status
from typing import List
from ..utils.data import load_data, save_data
from ..models.model import Task

router = APIRouter()

@router.get("/", response_model=List[Task])
def read_tasks():
    tasks_data = load_data()
    return tasks_data

@router.post("/", response_model=Task)
def create_task(task: Task):
    tasks_data = load_data()
    task_ids = [t["id"] for t in tasks_data]
    if task.id in task_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task ID already exists")
    tasks_data.append(task.model_dump())
    save_data(tasks_data)
    return task

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int):
    tasks_data = load_data()
    for task in tasks_data:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    tasks_data = load_data()
    for index, task in enumerate(tasks_data):
        if task["id"] == task_id:
            tasks_data[index] = updated_task.model_dump()
            save_data(tasks_data)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    tasks_data = load_data()
    for index, task in enumerate(tasks_data):
        if task["id"] == task_id:
            del tasks_data[index]
            save_data(tasks_data)
            return {"detail": "Task deleted successfully"}
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Task not found")
