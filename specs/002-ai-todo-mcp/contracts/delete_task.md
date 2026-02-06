# MCP Tool Contract: delete_task

## Overview
The `delete_task` tool removes a task from the user's task list.

## Tool Specification

```json
{
  "type": "function",
  "function": {
    "name": "delete_task",
    "description": "Delete a task from the user's list",
    "parameters": {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "integer",
          "description": "The ID of the user who owns the task"
        },
        "task_id": {
          "type": "integer",
          "description": "The ID of the task to delete"
        }
      },
      "required": ["user_id", "task_id"]
    }
  },
  "id": "deletetsk"
}
```

## Expected Behavior
- Permanently removes the task from the database
- Validates that the user owns the task being deleted
- Returns confirmation of deletion

## Success Response
```json
{
  "success": true,
  "message": "Task deleted successfully",
  "deleted_task_id": 123
}
```

## Error Responses
- `user_not_found`: When the user_id does not correspond to an existing user
- `task_not_found`: When the task_id does not correspond to an existing task
- `unauthorized_access`: When the user does not own the task
- `authorization_error`: When the user is not authorized to delete tasks

## Validation Rules
- User must exist in the database
- Task must exist in the database
- User must own the task being deleted