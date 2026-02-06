# MCP Tool Contract: list_tasks

## Overview
The `list_tasks` tool retrieves tasks for the authenticated user based on specified filters.

## Tool Specification

```json
{
  "type": "function",
  "function": {
    "name": "list_tasks",
    "description": "Retrieve tasks for the user with optional filtering",
    "parameters": {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "integer",
          "description": "The ID of the user whose tasks to retrieve"
        },
        "status": {
          "type": "string",
          "enum": ["pending", "completed", "all"],
          "description": "Filter tasks by status. Default is 'all'"
        },
        "limit": {
          "type": "integer",
          "description": "Maximum number of tasks to return. Default is 50"
        },
        "offset": {
          "type": "integer",
          "description": "Number of tasks to skip. Default is 0"
        }
      },
      "required": ["user_id"]
    }
  },
  "id": "listtask2"
}
```

## Expected Behavior
- Retrieves tasks associated with the specified user
- Filters tasks by status if provided (pending, completed, or all)
- Limits results by the specified limit and offset for pagination
- Returns tasks ordered by creation date (newest first)

## Success Response
```json
{
  "success": true,
  "tasks": [
    {
      "id": 123,
      "user_id": 456,
      "title": "Buy groceries",
      "description": "Get milk, bread, and eggs",
      "status": "pending",
      "due_date": "2026-02-15T10:00:00Z",
      "created_at": "2026-01-29T15:30:00Z",
      "updated_at": "2026-01-29T15:30:00Z"
    },
    {
      "id": 124,
      "user_id": 456,
      "title": "Call mom",
      "status": "completed",
      "completed_at": "2026-01-28T14:00:00Z",
      "created_at": "2026-01-27T10:00:00Z",
      "updated_at": "2026-01-28T14:00:00Z"
    }
  ],
  "total_count": 2
}
```

## Error Responses
- `user_not_found`: When the user_id does not correspond to an existing user
- `invalid_parameters`: When provided parameters are invalid
- `authorization_error`: When the user is not authorized to view tasks

## Validation Rules
- User must exist in the database
- Status must be one of the allowed values: "pending", "completed", "all"
- Limit must be a positive integer if provided
- Offset must be a non-negative integer if provided