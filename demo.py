"""
Demo script for the Todo Application
This demonstrates all the functionality of the Phase I Todo Application
"""
from src.todo_app.cli.main import TodoApp
from unittest.mock import patch


def demo_application():
    """Demonstrate the application functionality."""
    print("=== Todo Application Demo ===\n")
    
    # Create an instance of the application
    app = TodoApp()
    
    print("1. Adding tasks:")
    task_id_1 = app.task_service.add_task("Buy groceries")
    print(f"   Added task with ID: {task_id_1}")
    
    task_id_2 = app.task_service.add_task("Walk the dog")
    print(f"   Added task with ID: {task_id_2}")
    
    task_id_3 = app.task_service.add_task("Finish report")
    print(f"   Added task with ID: {task_id_3}")
    
    print("\n2. Viewing all tasks:")
    app.view_task_list()
    
    print("\n3. Updating a task:")
    print(f"   Updating task {task_id_2} description...")
    app.task_service.update_task_description(task_id_2, "Walk the dog in the morning")
    print(f"   Task {task_id_2} updated successfully")
    
    print("\n4. Viewing tasks after update:")
    app.view_task_list()
    
    print("\n5. Marking a task as complete:")
    print(f"   Marking task {task_id_1} as Complete...")
    app.task_service.update_task_status(task_id_1, "Complete")
    print(f"   Task {task_id_1} marked as Complete")
    
    print("\n6. Viewing tasks after status change:")
    app.view_task_list()
    
    print("\n7. Deleting a task:")
    print(f"   Deleting task {task_id_3}...")
    app.task_service.delete_task(task_id_3)
    print(f"   Task {task_id_3} deleted successfully")
    
    print("\n8. Final task list:")
    app.view_task_list()
    
    print("\n=== Demo completed successfully ===")


if __name__ == "__main__":
    demo_application()