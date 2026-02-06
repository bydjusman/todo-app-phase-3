# MCP Tool Contract: update_task

## Overview
The `update_task` tool modifies an existing task for the authenticated user.

## Tool Specification

```json
{
  "type": "function",
  "function": {
    "name": "update_task",
    "description": "Update an existing task for the user",
    "parameters": {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "integer",
          "description": "The ID of the user who owns the task"
        },
        "task_id": {
          "type": "integer",
          "description": "The ID of the task to update"
        },
        "title": {
          "type": "string",
          "description": "New title for the task (optional)"
        },
        "description": {
          "type": "string",
          "description": "New description for the task (optional)"
        },
        "due_date": {
          "type": "string",
          "format": "date-time",
          "description": "New due date for the task in ISO 8601 format (optional)"
        }
      },
      "required": ["user_id", "task_id"]
    }
  },
  "id": "updatetsk"
}
```

## Expected Behavior
- Updates only the fields provided in the request
- Validates that the user owns the task being updated
- Returns the updated task with all details
- Preserves unchanged fields

## Success Response
```json
{
  "success": true,
  "task": {
    "id": 123,
    "user_id": 456,
    "title": "Buy groceries and cook dinner",
    "description": "Get milk, bread, eggs, and vegetables",
    "status": "pending",
    "due_date": "2026-02-15T18:00:00Z",
    "created_at": "2026-01-29T15:30:00Z",
    "updated_at": "2026-01-29T16:45:00Z"
  }
}
```

## Error Responses
- `user_not_found`: When the user_id does not correspond to an existing user
- `task_not_found`: When the task_id does not correspond to an existing task
- `unauthorized_access`: When the user does not own the task
- `invalid_input`: When provided parameters are invalid
- `authorization_error`: When the user is not authorized to update tasks

## Validation Rules
- User must exist in the database
- Task must exist in the database
- User must own the task being updated
- Due date must be in valid ISO 8601 format if provided