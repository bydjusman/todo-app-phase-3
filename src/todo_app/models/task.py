"""
Task model for the Todo Application
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task in the todo list.
    
    Attributes:
        id (int): Unique identifier for the task, assigned sequentially starting from 1
        description (str): The text description of the task
        status (str): The completion status of the task ("Complete" or "Incomplete")
    """
    id: int
    description: str
    status: str = "Incomplete"
    
    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError("Task description must be a non-empty string")
        
        if self.status not in ["Complete", "Incomplete"]:
            raise ValueError("Task status must be either 'Complete' or 'Incomplete'")