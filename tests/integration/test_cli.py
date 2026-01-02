"""
Integration tests for the CLI application
"""
import pytest
from unittest.mock import patch, MagicMock
from src.todo_app.cli.main import TodoApp


def test_add_task_integration():
    """Test adding a task through the CLI."""
    app = TodoApp()
    
    # Mock user input for task description
    with patch('builtins.input', return_value='Test task description'):
        # Capture print output
        with patch('builtins.print') as mock_print:
            app.add_task()
            
            # Verify the task was added
            assert len(app.task_service.get_all_tasks()) == 1
            task = app.task_service.get_all_tasks()[0]
            assert task.description == "Test task description"
            assert task.status == "Incomplete"
            
            # Verify success message was printed
            mock_print.assert_called_with("Task added successfully with ID: 1")


def test_view_task_list_integration():
    """Test viewing task list through the CLI."""
    app = TodoApp()
    
    # Add a task first
    app.task_service.add_task("Test task")
    
    # Capture print output
    with patch('builtins.print') as mock_print:
        app.view_task_list()
        
        # Check that the task list was displayed
        calls = [str(call) for call in mock_print.call_args_list]
        assert any("Test task" in call for call in calls)
        assert any("Incomplete" in call for call in calls)


def test_update_task_integration():
    """Test updating a task through the CLI."""
    app = TodoApp()
    
    # Add a task first
    app.task_service.add_task("Original task")
    
    # Mock user inputs: task ID and new description
    inputs = iter(['1', 'Updated task'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        with patch('builtins.print') as mock_print:
            app.update_task()
            
            # Verify the task was updated
            task = app.task_service.get_task_by_id(1)
            assert task.description == "Updated task"
            
            # Verify success message was printed
            mock_print.assert_called_with("Task updated successfully.")


def test_delete_task_integration():
    """Test deleting a task through the CLI."""
    app = TodoApp()
    
    # Add a task first
    app.task_service.add_task("Test task to delete")
    
    # Mock user inputs: task ID and confirmation
    inputs = iter(['1', 'y'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        with patch('builtins.print') as mock_print:
            app.delete_task()
            
            # Verify the task was deleted
            assert len(app.task_service.get_all_tasks()) == 0
            
            # Verify success message was printed
            mock_print.assert_called_with("Task deleted successfully.")


def test_mark_task_complete_integration():
    """Test marking a task as complete through the CLI."""
    app = TodoApp()
    
    # Add a task first
    app.task_service.add_task("Test task")
    
    # Mock user inputs: task ID and new status
    inputs = iter(['1', 'Complete'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        with patch('builtins.print') as mock_print:
            app.mark_task_complete_incomplete()
            
            # Verify the task status was updated
            task = app.task_service.get_task_by_id(1)
            assert task.status == "Complete"
            
            # Verify success message was printed
            mock_print.assert_called_with("Task marked as Complete successfully.")