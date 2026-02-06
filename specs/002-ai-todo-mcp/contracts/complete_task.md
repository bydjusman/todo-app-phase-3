# MCP Tool Contract: complete_task

## Overview
The `complete_task` tool marks an existing task as completed for the authenticated user.

## Tool Specification

```json
{
  "type": "function",
  "function": {
    "name": "complete_task",
    "description": "Mark a task as completed",
    "parameters": {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "integer",
          "description": "The ID of the user who owns the task"
        },
        "task_id": {
          "type": "integer",
          "description": "The ID of the task to mark as completed"
        }
      },
      "required": ["user_id", "task_id"]
    }
  },
  "id": "complet01"
}
```

## Expected Behavior
- Changes the task status from "pending" to "completed"
- Sets the completed_at timestamp to the current time
- Validates that the user owns the task being completed
- Returns the updated task with all details

## Success Response
```json
{
  "success": true,
  "task": {
    "id": 123,
    "user_id": 456,
    "title": "Buy groceries",
    "description": "Get milk, bread, and eggs",
    "status": "completed",
    "due_date": "2026-02-15T10:00:00Z",
    "created_at": "2026-01-29T15:30:00Z",
    "updated_at": "2026-01-29T16:50:00Z",
    "completed_at": "2026-01-29T16:50:00Z"
  }
}
```

## Error Responses
- `user_not_found`: When the user_id does not correspond to an existing user
- `task_not_found`: When the task_id does not correspond to an existing task
- `unauthorized_access`: When the user does not own the task
- `already_completed`: When the task is already marked as completed
- `authorization_error`: When the user is not authorized to complete tasks

## Validation Rules
- User must exist in the database
- Task must exist in the database
- Task must be in "pending" status (not already completed)
- User must own the task being completed