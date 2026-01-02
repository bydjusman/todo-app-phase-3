"""
Unit tests for the TaskService
"""
import pytest
from src.todo_app.services.task_service import TaskService


def test_add_task():
    """Test adding a task."""
    service = TaskService()
    task_id = service.add_task("Test task")
    
    assert task_id == 1
    assert len(service.get_all_tasks()) == 1
    
    task = service.get_task_by_id(1)
    assert task.id == 1
    assert task.description == "Test task"
    assert task.status == "Incomplete"


def test_add_task_empty_description():
    """Test adding a task with empty description."""
    service = TaskService()
    
    with pytest.raises(ValueError):
        service.add_task("")
    
    with pytest.raises(ValueError):
        service.add_task("   ")


def test_get_all_tasks():
    """Test getting all tasks."""
    service = TaskService()
    
    # Initially empty
    assert len(service.get_all_tasks()) == 0
    assert service.is_empty() is True
    
    # Add tasks
    service.add_task("First task")
    service.add_task("Second task")
    
    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[0].description == "First task"
    assert tasks[1].id == 2
    assert tasks[1].description == "Second task"


def test_get_task_by_id():
    """Test getting a task by ID."""
    service = TaskService()
    service.add_task("Test task")
    
    task = service.get_task_by_id(1)
    assert task.id == 1
    assert task.description == "Test task"
    
    # Test non-existent task
    with pytest.raises(KeyError):
        service.get_task_by_id(999)


def test_update_task_description():
    """Test updating a task's description."""
    service = TaskService()
    service.add_task("Original task")
    
    service.update_task_description(1, "Updated task")
    
    task = service.get_task_by_id(1)
    assert task.description == "Updated task"
    
    # Test updating with empty description
    with pytest.raises(ValueError):
        service.update_task_description(1, "")
    
    with pytest.raises(ValueError):
        service.update_task_description(1, "   ")


def test_delete_task():
    """Test deleting a task."""
    service = TaskService()
    service.add_task("Test task")
    
    assert len(service.get_all_tasks()) == 1
    
    service.delete_task(1)
    
    assert len(service.get_all_tasks()) == 0
    assert service.is_empty() is True
    
    # Test deleting non-existent task
    with pytest.raises(KeyError):
        service.delete_task(999)


def test_update_task_status():
    """Test updating a task's status."""
    service = TaskService()
    service.add_task("Test task")
    
    # Test updating to Complete
    service.update_task_status(1, "Complete")
    task = service.get_task_by_id(1)
    assert task.status == "Complete"
    
    # Test updating to Incomplete
    service.update_task_status(1, "Incomplete")
    task = service.get_task_by_id(1)
    assert task.status == "Incomplete"
    
    # Test invalid status
    with pytest.raises(ValueError):
        service.update_task_status(1, "Invalid")
    
    # Test non-existent task
    with pytest.raises(KeyError):
        service.update_task_status(999, "Complete")


def test_is_empty():
    """Test checking if the task list is empty."""
    service = TaskService()
    assert service.is_empty() is True
    
    service.add_task("Test task")
    assert service.is_empty() is False
    
    service.delete_task(1)
    assert service.is_empty() is True