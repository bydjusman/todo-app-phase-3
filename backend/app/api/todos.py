from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import sys
import os
from enum import Enum

# Add the app directory to the path to import models and crud
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..models.task import Task, TaskStatus
from ..core.task_service import TaskService
from ..database.session import get_db
from ..core.auth import get_current_user
from ..models.user import User

router = APIRouter()

class TaskStatusQuery(str, Enum):
    all = "all"
    pending = "pending"
    completed = "completed"

@router.get("/todos", response_model=List[Task])
async def get_todos(
    status: TaskStatusQuery = "all",
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve all tasks for the current user, optionally filtered by status
    """
    task_service = TaskService(db)

    if status == "all":
        return task_service.get_user_tasks(current_user.id)
    elif status == "pending":
        return task_service.get_user_tasks_by_status(current_user.id, TaskStatus.PENDING)
    elif status == "completed":
        return task_service.get_user_tasks_by_status(current_user.id, TaskStatus.COMPLETED)
    else:
        return task_service.get_user_tasks(current_user.id)


@router.post("/todos", response_model=Task)
async def create_todo(
    todo_data: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new task for the current user
    """
    task_service = TaskService(db)
    return task_service.create_task(
        title=todo_data.get('title', ''),
        description=todo_data.get('description', ''),
        user_id=current_user.id
    )


@router.put("/todos/{todo_id}", response_model=Task)
async def update_todo(
    todo_id: int,
    todo_data: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update a specific task
    """
    task_service = TaskService(db)

    # Verify the task belongs to the current user
    existing_task = task_service.get_task_by_id(todo_id)
    if not existing_task or existing_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")

    # Map completed field to status if provided
    status = None
    if 'completed' in todo_data and todo_data['completed'] is not None:
        if todo_data['completed']:
            status = TaskStatus.COMPLETED
        else:
            status = TaskStatus.PENDING

    return task_service.update_task(
        task_id=todo_id,
        title=todo_data.get('title'),
        description=todo_data.get('description'),
        status=status
    )


@router.delete("/todos/{todo_id}")
async def delete_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a specific task
    """
    task_service = TaskService(db)

    # Verify the task belongs to the current user
    existing_task = task_service.get_task_by_id(todo_id)
    if not existing_task or existing_task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")

    task_service.delete_task(todo_id)
    return {"message": "Task deleted successfully"}