from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List
from sqlmodel import Session
from enum import Enum

from ..models.task import Task, TaskStatus
from ..core.task_service import TaskService
from ..database.session import get_session
from ..core.auth import get_current_user_from_token
from ..models.user import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class TaskStatusQuery(str, Enum):
    all = "all"
    pending = "pending"
    completed = "completed"

@router.get("/todos", response_model=List[Task])
async def get_todos(
    status: TaskStatusQuery = "all",
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the current user, optionally filtered by status
    """
    # Get current user from token
    current_user = get_current_user_from_token(token, db)
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if status == "all":
        return TaskService.get_tasks(db, current_user.id)
    elif status == "pending":
        return TaskService.get_tasks(db, current_user.id, status="pending")
    elif status == "completed":
        return TaskService.get_tasks(db, current_user.id, status="completed")
    else:
        return TaskService.get_tasks(db, current_user.id)


@router.post("/todos", response_model=Task)
async def create_todo(
    todo_data: dict,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    """
    Create a new task for the current user
    """
    # Get current user from token
    current_user = get_current_user_from_token(token, db)
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    return TaskService.create_task(
        db_session=db,
        user_id=current_user.id,
        task_data=todo_data
    )


@router.put("/todos/{todo_id}", response_model=Task)
async def update_todo(
    todo_id: int,
    todo_data: dict,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    """
    Update a specific task
    """
    # Get current user from token
    current_user = get_current_user_from_token(token, db)
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # Map completed field to status if provided
    update_data = {}
    if 'title' in todo_data:
        update_data['title'] = todo_data.get('title')
    if 'description' in todo_data:
        update_data['description'] = todo_data.get('description')
    if 'completed' in todo_data and todo_data['completed'] is not None:
        if todo_data['completed']:
            update_data['status'] = 'completed'
        else:
            update_data['status'] = 'pending'

    result = TaskService.update_task(
        db_session=db,
        task_id=todo_id,
        user_id=current_user.id,
        update_data=update_data
    )
    
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
        
    return result


@router.delete("/todos/{todo_id}")
async def delete_todo(
    todo_id: int,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    """
    Delete a specific task
    """
    # Get current user from token
    current_user = get_current_user_from_token(token, db)
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    success = TaskService.delete_task(
        db_session=db,
        task_id=todo_id,
        user_id=current_user.id
    )
    
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}