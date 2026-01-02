"""
Task service for the Todo Application
"""
from typing import List, Optional
from ..models.task import Task


class TaskService:
    """
    Service class to handle all task-related operations.
    """
    
    def __init__(self):
        """Initialize the task service with an empty task list."""
        self._tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, description: str) -> int:
        """
        Add a new task to the collection.
        
        Args:
            description (str): The task description
            
        Returns:
            int: The ID of the newly created task
            
        Raises:
            ValueError: If description is empty or only whitespace
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty or contain only whitespace")
        
        task = Task(
            id=self._next_id,
            description=description.strip(),
            status="Incomplete"
        )
        
        self._tasks.append(task)
        task_id = self._next_id
        self._next_id += 1
        
        return task_id
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the collection.
        
        Returns:
            List[Task]: List of all tasks, sorted by ID
        """
        return sorted(self._tasks, key=lambda t: t.id)
    
    def get_task_by_id(self, task_id: int) -> Task:
        """
        Retrieve a specific task by its ID.
        
        Args:
            task_id (int): The task ID
            
        Returns:
            Task: The task object with the specified ID
            
        Raises:
            KeyError: If task ID doesn't exist
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"Task with ID {task_id} does not exist")
    
    def update_task_description(self, task_id: int, new_description: str) -> None:
        """
        Update the description of an existing task.
        
        Args:
            task_id (int): The task ID
            new_description (str): The new description
            
        Raises:
            KeyError: If task ID doesn't exist
            ValueError: If new description is invalid
        """
        if not new_description or not new_description.strip():
            raise ValueError("Task description cannot be empty or contain only whitespace")
        
        task = self.get_task_by_id(task_id)
        task.description = new_description.strip()
    
    def delete_task(self, task_id: int) -> None:
        """
        Remove a task from the collection.
        
        Args:
            task_id (int): The task ID
            
        Raises:
            KeyError: If task ID doesn't exist
        """
        task = self.get_task_by_id(task_id)
        self._tasks.remove(task)
    
    def update_task_status(self, task_id: int, new_status: str) -> None:
        """
        Update the completion status of a task.
        
        Args:
            task_id (int): The task ID
            new_status (str): The new status ("Complete" or "Incomplete")
            
        Raises:
            KeyError: If task ID doesn't exist
            ValueError: If status is invalid
        """
        if new_status not in ["Complete", "Incomplete"]:
            raise ValueError("Task status must be either 'Complete' or 'Incomplete'")
        
        task = self.get_task_by_id(task_id)
        task.status = new_status
    
    def is_empty(self) -> bool:
        """
        Check if the task collection is empty.
        
        Returns:
            bool: True if the collection is empty, False otherwise
        """
        return len(self._tasks) == 0