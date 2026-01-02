"""
Main CLI application for the Todo Application
"""
from typing import Optional
from ..services.task_service import TaskService


class TodoApp:
    """
    Main CLI application class for the Todo Application.
    """
    
    def __init__(self):
        """Initialize the Todo application."""
        self.task_service = TaskService()
    
    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")
        
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            
            try:
                if choice == '1':
                    self.add_task()
                elif choice == '2':
                    self.view_task_list()
                elif choice == '3':
                    self.update_task()
                elif choice == '4':
                    self.delete_task()
                elif choice == '5':
                    self.mark_task_complete_incomplete()
                elif choice == '6':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose a number from 1 to 6.")
            except ValueError as e:
                print(f"Error: {e}")
            except KeyError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    
    def display_menu(self):
        """Display the main menu."""
        print("\nTodo Application")
        print("1. Add Task")
        print("2. View Task List")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
    
    def add_task(self):
        """Add a new task."""
        description = input("Enter task description: ").strip()
        
        if not description:
            print("Task description cannot be empty.")
            return
        
        task_id = self.task_service.add_task(description)
        print(f"Task added successfully with ID: {task_id}")
    
    def view_task_list(self):
        """View all tasks."""
        if self.task_service.is_empty():
            print("Your task list is empty.")
            return
        
        tasks = self.task_service.get_all_tasks()
        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            status_indicator = "X" if task.status == "Complete" else "O"
            print(f"[{status_indicator}] [{task.id}] {task.description} - {task.status}")
        print("-" * 50)
    
    def update_task(self):
        """Update a task's description."""
        if self.task_service.is_empty():
            print("Your task list is empty. Nothing to update.")
            return
        
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        try:
            # Get current task to show user
            current_task = self.task_service.get_task_by_id(task_id)
            print(f"Current task: {current_task.description}")
            
            new_description = input("Enter new description: ").strip()
            
            if not new_description:
                print("Task description cannot be empty.")
                return
            
            self.task_service.update_task_description(task_id, new_description)
            print("Task updated successfully.")
        except KeyError:
            print(f"Task with ID {task_id} does not exist.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_task(self):
        """Delete a task."""
        if self.task_service.is_empty():
            print("Your task list is empty. Nothing to delete.")
            return
        
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        try:
            # Show task before deletion for confirmation
            task = self.task_service.get_task_by_id(task_id)
            print(f"You are about to delete: {task.description}")
            
            confirm = input("Are you sure? (y/N): ").strip().lower()
            if confirm in ['y', 'yes']:
                self.task_service.delete_task(task_id)
                print("Task deleted successfully.")
            else:
                print("Deletion cancelled.")
        except KeyError:
            print(f"Task with ID {task_id} does not exist.")
    
    def mark_task_complete_incomplete(self):
        """Mark a task as complete or incomplete."""
        if self.task_service.is_empty():
            print("Your task list is empty. Nothing to mark.")
            return
        
        try:
            task_id = int(input("Enter task ID to mark: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        try:
            # Get current task to show user
            current_task = self.task_service.get_task_by_id(task_id)
            print(f"Current status for task '{current_task.description}': {current_task.status}")
            
            # Ask for new status
            new_status = input("Enter new status (Complete/Incomplete): ").strip().capitalize()
            
            if new_status not in ["Complete", "Incomplete"]:
                print("Invalid status. Please enter 'Complete' or 'Incomplete'.")
                return
            
            self.task_service.update_task_status(task_id, new_status)
            print(f"Task marked as {new_status} successfully.")
        except KeyError:
            print(f"Task with ID {task_id} does not exist.")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """Main entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()