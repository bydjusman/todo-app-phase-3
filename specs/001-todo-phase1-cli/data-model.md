# Data Model: Phase I Todo Console Application

## Task Entity

### Attributes
- **id** (int): Unique identifier for the task, assigned sequentially starting from 1
  - Constraints: Positive integer, unique within the application session
  - Generated: Automatically by the system when a new task is created

- **description** (str): The text description of the task
  - Constraints: Required field, minimum 1 character, maximum 500 characters
  - Validation: Cannot be empty or contain only whitespace

- **status** (str): The completion status of the task
  - Values: "Incomplete" (default) or "Complete"
  - Validation: Only these two values are allowed

### State Transitions
- Default state: "Incomplete" when task is created
- Transitions: Can change from "Incomplete" to "Complete" or "Complete" to "Incomplete"
- Constraints: No other state transitions are allowed

## Task Collection

### In-Memory Storage
- **Type**: Python list of Task objects
- **Access**: Thread-safe operations (though single-user application so not strictly necessary)
- **Lifetime**: Exists only during application runtime, cleared when application exits

### Operations Supported
- Add new task to collection
- Retrieve task by ID
- Update task description by ID
- Delete task by ID
- Update task status by ID
- List all tasks
- Check if collection is empty

## Validation Rules
1. Task descriptions must not be empty or contain only whitespace
2. Task IDs must be positive integers
3. Task status must be either "Complete" or "Incomplete"
4. Operations on non-existent task IDs must raise appropriate exceptions
5. Task IDs must be unique within the collection