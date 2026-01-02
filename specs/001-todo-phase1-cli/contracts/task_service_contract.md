# Internal API Contracts: Phase I Todo Console Application

## Task Service Interface

### add_task(description: str) -> int
- **Purpose**: Add a new task to the collection
- **Input**: Task description (string, 1-500 characters)
- **Output**: The ID of the newly created task (positive integer)
- **Exceptions**: ValueError if description is empty or only whitespace
- **Side effects**: Task added to in-memory collection with "Incomplete" status

### get_all_tasks() -> List[Task]
- **Purpose**: Retrieve all tasks in the collection
- **Input**: None
- **Output**: List of all Task objects, sorted by ID
- **Exceptions**: None
- **Side effects**: None

### get_task_by_id(task_id: int) -> Task
- **Purpose**: Retrieve a specific task by its ID
- **Input**: Task ID (positive integer)
- **Output**: Task object with the specified ID
- **Exceptions**: KeyError if task ID doesn't exist
- **Side effects**: None

### update_task_description(task_id: int, new_description: str) -> None
- **Purpose**: Update the description of an existing task
- **Input**: Task ID (positive integer), new description (string, 1-500 characters)
- **Output**: None
- **Exceptions**: KeyError if task ID doesn't exist, ValueError if new description is invalid
- **Side effects**: Task description updated in collection

### delete_task(task_id: int) -> None
- **Purpose**: Remove a task from the collection
- **Input**: Task ID (positive integer)
- **Output**: None
- **Exceptions**: KeyError if task ID doesn't exist
- **Side effects**: Task removed from collection, other task IDs remain unchanged

### update_task_status(task_id: int, new_status: str) -> None
- **Purpose**: Update the completion status of a task
- **Input**: Task ID (positive integer), new status ("Complete" or "Incomplete")
- **Output**: None
- **Exceptions**: KeyError if task ID doesn't exist, ValueError if status is invalid
- **Side effects**: Task status updated in collection