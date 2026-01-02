"""
Unit tests for the Task model
"""
import pytest
from src.todo_app.models.task import Task


def test_task_creation():
    """Test creating a valid task."""
    task = Task(id=1, description="Test task", status="Incomplete")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.status == "Incomplete"


def test_task_creation_defaults():
    """Test creating a task with default status."""
    task = Task(id=1, description="Test task")
    assert task.id == 1
    assert task.description == "Test task"
    assert task.status == "Incomplete"


def test_task_creation_invalid_id():
    """Test creating a task with invalid ID."""
    with pytest.raises(ValueError):
        Task(id=0, description="Test task")
    
    with pytest.raises(ValueError):
        Task(id=-1, description="Test task")
    
    with pytest.raises(ValueError):
        Task(id="invalid", description="Test task")


def test_task_creation_invalid_description():
    """Test creating a task with invalid description."""
    with pytest.raises(ValueError):
        Task(id=1, description="")
    
    with pytest.raises(ValueError):
        Task(id=1, description="   ")
    
    with pytest.raises(ValueError):
        Task(id=1, description=None)


def test_task_creation_invalid_status():
    """Test creating a task with invalid status."""
    with pytest.raises(ValueError):
        Task(id=1, description="Test task", status="Invalid")
    
    with pytest.raises(ValueError):
        Task(id=1, description="Test task", status="Done")