"""MCP Tools for Todo Operations"""
from typing import List, Optional, Dict, Any
from sqlmodel import Session
from pydantic import BaseModel
from ..models.task import Task, TaskBase
from ..database.session import get_session
from ..core.auth import get_current_user_from_token
from fastapi.security import OAuth2PasswordBearer
import uuid
from datetime import datetime


# Define Pydantic models for tool inputs/outputs
class AddTaskInput(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"  # Use "pending" or "completed"
    due_date: Optional[str] = None
    token: str


class AddTaskOutput(BaseModel):
    success: bool
    task_id: Optional[int] = None
    message: str


class ListTasksInput(BaseModel):
    token: str
    offset: Optional[int] = 0
    limit: Optional[int] = 50
    status: Optional[str] = None  # "pending", "completed", or None for all


class ListTasksOutput(BaseModel):
    success: bool
    tasks: List[Dict[str, Any]]
    total_count: int


class UpdateTaskInput(BaseModel):
    task_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # "pending" or "completed"
    due_date: Optional[str] = None
    token: str


class UpdateTaskOutput(BaseModel):
    success: bool
    message: str


class DeleteTaskInput(BaseModel):
    task_id: int
    token: str


class DeleteTaskOutput(BaseModel):
    success: bool
    message: str


class CompleteTaskInput(BaseModel):
    task_id: int
    token: str


class CompleteTaskOutput(BaseModel):
    success: bool
    message: str


class MCPTools:
    """MCP-compatible tools for todo operations"""

    @staticmethod
    def _get_user_from_token(token: str, session: Session):
        """Helper to get user from token"""
        user = get_current_user_from_token(token, session)
        if not user:
            raise ValueError("Invalid or expired token")
        return user

    @staticmethod
    def addtask01(input_data: AddTaskInput) -> AddTaskOutput:
        """
        Add a new task to the user's todo list

        Tool ID: addtask01 (alphanumeric, ≤9 chars, no hyphens/underscores)
        """
        with get_session() as session:
            try:
                user = MCPTools._get_user_from_token(input_data.token, session)

                # Prepare task data
                from ..core.task_service import TaskService
                task_data = {
                    'title': input_data.title,
                    'description': input_data.description,
                    'status': input_data.status,
                    'due_date': input_data.due_date
                }

                # Create task using service
                task = TaskService.create_task(session, user.id, task_data)

                return AddTaskOutput(
                    success=True,
                    task_id=task.id,
                    message=f"Task '{task.title}' added successfully with ID {task.id}"
                )
            except Exception as e:
                return AddTaskOutput(
                    success=False,
                    task_id=None,
                    message=f"Failed to add task: {str(e)}"
                )

    @staticmethod
    def listtask2(input_data: ListTasksInput) -> ListTasksOutput:
        """
        List tasks for the user with optional filtering

        Tool ID: listtask2 (alphanumeric, ≤9 chars, no hyphens/underscores)
        """
        with get_session() as session:
            try:
                user = MCPTools._get_user_from_token(input_data.token, session)

                # Get tasks using service
                from ..core.task_service import TaskService
                tasks_list = TaskService.get_tasks(
                    session,
                    user.id,
                    offset=input_data.offset,
                    limit=input_data.limit,
                    status=input_data.status
                )

                # Convert to dict format for output
                tasks = []
                for task in tasks_list:
                    task_dict = {
                        "id": task.id,
                        "title": task.title,
                        "description": task.description,
                        "status": task.status,
                        "due_date": task.due_date.isoformat() if task.due_date else None,
                        "created_at": task.created_at.isoformat() if task.created_at else None,
                        "updated_at": task.updated_at.isoformat() if task.updated_at else None
                    }
                    tasks.append(task_dict)

                return ListTasksOutput(
                    success=True,
                    tasks=tasks,
                    total_count=len(tasks)
                )
            except Exception as e:
                return ListTasksOutput(
                    success=False,
                    tasks=[],
                    total_count=0,
                    message=f"Failed to list tasks: {str(e)}"
                )

    @staticmethod
    def updatetsk(input_data: UpdateTaskInput) -> UpdateTaskOutput:
        """
        Update a specific task for the user

        Tool ID: updatetsk (alphanumeric, ≤9 chars, no hyphens/underscores)
        """
        with get_session() as session:
            try:
                user = MCPTools._get_user_from_token(input_data.token, session)

                # Prepare update data
                update_data = {}
                if input_data.title is not None:
                    update_data['title'] = input_data.title
                if input_data.description is not None:
                    update_data['description'] = input_data.description
                if input_data.status is not None:
                    update_data['status'] = input_data.status
                if input_data.due_date is not None:
                    update_data['due_date'] = input_data.due_date

                # Update task using service
                from ..core.task_service import TaskService
                task = TaskService.update_task(session, input_data.task_id, user.id, update_data)

                if task:
                    return UpdateTaskOutput(
                        success=True,
                        message=f"Task {input_data.task_id} updated successfully"
                    )
                else:
                    return UpdateTaskOutput(
                        success=False,
                        message=f"Task {input_data.task_id} not found or doesn't belong to user"
                    )
            except Exception as e:
                return UpdateTaskOutput(
                    success=False,
                    message=f"Failed to update task: {str(e)}"
                )

    @staticmethod
    def complet01(input_data: CompleteTaskInput) -> CompleteTaskOutput:
        """
        Mark a task as completed

        Tool ID: complet01 (alphanumeric, ≤9 chars, no hyphens/underscores)
        """
        with get_session() as session:
            try:
                user = MCPTools._get_user_from_token(input_data.token, session)

                # Update task status to completed using service
                from ..core.task_service import TaskService
                task = TaskService.update_task(session, input_data.task_id, user.id, {'status': 'completed'})

                if task:
                    return CompleteTaskOutput(
                        success=True,
                        message=f"Task {input_data.task_id} marked as completed"
                    )
                else:
                    return CompleteTaskOutput(
                        success=False,
                        message=f"Task {input_data.task_id} not found or doesn't belong to user"
                    )
            except Exception as e:
                return CompleteTaskOutput(
                    success=False,
                    message=f"Failed to complete task: {str(e)}"
                )

    @staticmethod
    def deletetsk(input_data: DeleteTaskInput) -> DeleteTaskOutput:
        """
        Delete a specific task for the user

        Tool ID: deletetsk (alphanumeric, ≤9 chars, no hyphens/underscores)
        """
        with get_session() as session:
            try:
                user = MCPTools._get_user_from_token(input_data.token, session)

                # Delete task using service
                from ..core.task_service import TaskService
                success = TaskService.delete_task(session, input_data.task_id, user.id)

                if success:
                    return DeleteTaskOutput(
                        success=True,
                        message=f"Task {input_data.task_id} deleted successfully"
                    )
                else:
                    return DeleteTaskOutput(
                        success=False,
                        message=f"Task {input_data.task_id} not found or doesn't belong to user"
                    )
            except Exception as e:
                return DeleteTaskOutput(
                    success=False,
                    message=f"Failed to delete task: {str(e)}"
                )