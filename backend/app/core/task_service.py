from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from ..models.task import Task, TaskStatus
from ..models.user import User


class TaskService:
    """
    Service class to handle task operations via direct API calls.
    This complements the TodoAgentService which handles AI-driven operations.
    """

    @staticmethod
    def create_task(db_session: Session, user_id: int, task_data: dict) -> Task:
        """
        Create a new task
        """
        # Parse due_date if provided
        due_date = None
        if task_data.get('due_date'):
            try:
                due_date = datetime.fromisoformat(task_data['due_date'].replace('Z', '+00:00'))
            except ValueError:
                # If parsing fails, ignore the due_date
                pass
        
        task = Task(
            title=task_data['title'],
            description=task_data.get('description'),
            status=task_data.get('status', 'pending'),
            due_date=due_date,
            user_id=user_id
        )
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)
        return task

    @staticmethod
    def get_tasks(db_session: Session, user_id: int, offset: int = 0, limit: int = 50, status: str = None) -> List[Task]:
        """
        Retrieve tasks for a specific user with optional filtering
        """
        statement = select(Task).where(Task.user_id == user_id)
        
        if status:
            statement = statement.where(Task.status == status)
        
        statement = statement.offset(offset).limit(limit)
        tasks = db_session.exec(statement).all()
        return tasks

    @staticmethod
    def update_task(db_session: Session, task_id: int, user_id: int, update_data: dict) -> Optional[Task]:
        """
        Update an existing task
        """
        # First, get the task to ensure it belongs to the user
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = db_session.exec(statement).first()
        
        if not task:
            return None

        # Update fields if provided in update_data
        if 'title' in update_data:
            task.title = update_data['title']
        if 'description' in update_data:
            task.description = update_data['description']
        if 'status' in update_data:
            task.status = update_data['status']
        if 'due_date' in update_data:
            try:
                due_date = datetime.fromisoformat(update_data['due_date'].replace('Z', '+00:00'))
                task.due_date = due_date
            except ValueError:
                # If parsing fails, ignore the due_date
                pass
        
        task.updated_at = datetime.utcnow()
        
        db_session.add(task)
        db_session.commit()
        db_session.refresh(task)
        return task

    @staticmethod
    def delete_task(db_session: Session, task_id: int, user_id: int) -> bool:
        """
        Delete a task by ID for a specific user
        """
        # First, get the task to ensure it belongs to the user
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = db_session.exec(statement).first()
        
        if not task:
            return False

        db_session.delete(task)
        db_session.commit()
        return True