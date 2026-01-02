# Quickstart Guide: Phase I Todo Console Application

## Getting Started

1. Ensure you have Python 3.11 or higher installed on your system
2. Clone or download the repository
3. Navigate to the project directory
4. Run the application:

```bash
cd src/todo_app/cli
python main.py
```

## Using the Application

When you start the application, you'll see a menu with the following options:

```
Todo Application
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
Choose an option:
```

### Adding a Task
1. Select option 1
2. Enter your task description when prompted
3. The task will be added with a unique ID and "Incomplete" status

### Viewing Tasks
1. Select option 2
2. All tasks will be displayed with their ID, description, and status

### Updating a Task
1. Select option 3
2. Enter the task ID you want to update
3. Enter the new description for the task

### Deleting a Task
1. Select option 4
2. Enter the task ID you want to delete
3. Confirm the deletion when prompted

### Marking Task Complete/Incomplete
1. Select option 5
2. Enter the task ID you want to update
3. Choose whether to mark it "Complete" or "Incomplete"

### Exiting the Application
1. Select option 6 to exit the application

## Error Handling

The application handles the following error cases:
- Invalid menu options: Shows an error message and prompts again
- Empty task descriptions: Shows an error message and prompts again
- Invalid task IDs: Shows an error message when the ID doesn't exist
- Empty task list: Shows an appropriate message when viewing an empty list