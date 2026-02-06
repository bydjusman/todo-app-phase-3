# MCP Tool Contract: add_task

## Overview
The `add_task` tool creates a new task for the authenticated user.

## Tool Specification

```json
{
  "type": "function",
  "function": {
    "name": "add_task",
    "description": "Create a new task for the user",
    "parameters": {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "integer",
          "description": "The ID of the user creating the task"
        },
        "title": {
          "type": "string",
          "description": "The title of the task"
        },
        "description": {
          "type": "string",
          "description": "Optional description of the task"
        },
        "due_date": {
          "type": "string",
          "format": "date-time",
          "description": "Optional due date for the task in ISO 8601 format"
        }
      },
      "required": ["user_id", "title"]
    }
  },
  "id": "addtask01"
}
```

## Expected Behavior
- Creates a new task with status "pending"
- Associates the task with the specified user
- Returns the created task with all details including the new task ID
- Validates that the user exists and owns the task

## Success Response
```json
{
  "success": true,
  "task": {
    "id": 123,
    "user_id": 456,
    "title": "Buy groceries",
    "description": "Get milk, bread, and eggs",
    "status": "pending",
    "due_date": "2026-02-15T10:00:00Z",
    "created_at": "2026-01-29T15:30:00Z",
    "updated_at": "2026-01-29T15:30:00Z"
  }
}
```

## Error Responses
- `user_not_found`: When the user_id does not correspond to an existing user
- `invalid_input`: When required parameters are missing or invalid
- `authorization_error`: When the user is not authorized to create tasks

## Validation Rules
- User must exist in the database
- Title must not be empty
- Due date must be in valid ISO 8601 format if provided