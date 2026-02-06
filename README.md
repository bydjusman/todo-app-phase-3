# AI-Powered Todo Chatbot - Phase III Implementation

This project implements an AI-powered chatbot for managing todos through natural language using MCP (Model Context Protocol) server architecture and Claude Code with Spec-Kit Plus.

## Architecture Overview

```
┌─────────────────┐     ┌──────────────────────────────────────────────┐     ┌─────────────────┐
│                 │     │              FastAPI Server                   │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │     │    Neon DB      │
│  ChatKit UI     │────▶│  │         Chat Endpoint                  │  │     │  (PostgreSQL)   │
│  (Frontend)     │     │  │  POST /api/chat                        │  │     │                 │
│                 │     │  └───────────────┬────────────────────────┘  │     │  - tasks        │
│                 │     │                  │                           │     │  - conversations│
│                 │     │                  ▼                           │     │  - messages     │
│                 │     │  ┌────────────────────────────────────────┐  │────▶│                 │
│                 │◀────│  │      OpenAI Agents SDK                 │  │     │                 │
│                 │     │  │      (Agent + Runner)                  │  │     │                 │
│                 │     │  └───────────────┬────────────────────────┘  │     │                 │
│                 │     │                  │                           │     │                 │
│                 │     │                  ▼                           │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │────▶│                 │
│                 │     │  │         MCP Server                 │  │     │                 │
│                 │     │  │  (MCP Tools for Task Operations)       │  │◀────│                 │
│                 │     │  └────────────────────────────────────────┘  │     │                 │
└─────────────────┘     └──────────────────────────────────────────────┘     └─────────────────┘
```

## Features Implemented

### Backend (Python FastAPI)
- **MCP Server**: Exposes task operations as tools for AI agents
- **Stateless Chat Endpoint**: Persists conversation state to database
- **Natural Language Processing**: Converts user intents to tool calls
- **Database Models**: Tasks, Conversations, and Messages with proper relationships
- **Authentication**: Better Auth integration for user management

### MCP Tools Available
1. **add_task**: Create a new task
2. **list_tasks**: Retrieve tasks from the list
3. **complete_task**: Mark a task as complete
4. **delete_task**: Remove a task from the list
5. **update_task**: Modify task title or description

### Frontend (Next.js with ChatKit)
- **Conversational Interface**: Natural language interaction with the todo system
- **Real-time Chat**: Interactive chat interface for task management
- **User Authentication**: Secure access to personal task lists

## Database Schema

### Task Model
- `user_id`: Foreign key to user
- `id`: Primary key
- `title`: Task title
- `description`: Task description
- `completed`: Boolean indicating completion status
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

### Conversation Model
- `user_id`: Foreign key to user
- `id`: Primary key
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

### Message Model
- `user_id`: Foreign key to user
- `id`: Primary key
- `conversation_id`: Foreign key to conversation
- `role`: User or assistant role
- `content`: Message content
- `created_at`: Timestamp of creation

## Natural Language Commands Supported

| User Says | Agent Action |
|-----------|--------------|
| "Add a task to buy groceries" | Calls `add_task` with title "buy groceries" |
| "Show me all my tasks" | Calls `list_tasks` with status "all" |
| "What's pending?" | Calls `list_tasks` with status "pending" |
| "Mark task 3 as complete" | Calls `complete_task` with task_id 3 |
| "Delete the meeting task" | Calls `list_tasks` first, then `delete_task` |
| "Change task 1 to 'Call mom tonight'" | Calls `update_task` with new title |
| "I need to remember to pay bills" | Calls `add_task` with title "pay bills" |
| "What have I completed?" | Calls `list_tasks` with status "completed" |

## Installation and Setup

### Prerequisites
- Python 3.8+
- Node.js 18+
- PostgreSQL (or SQLite for development)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### MCP Server Setup
```bash
cd backend/mcp_server
pip install mcp
python main.py
```

## API Endpoints

### Chat API
- `POST /api/chat/{user_id}` - Send message and get AI response

#### Request Body
```json
{
  "message": "User's natural language message",
  "conversation_id": 123,
  "token": "auth_token"
}
```

#### Response
```json
{
  "conversation_id": 123,
  "response": "AI assistant's response",
  "tool_calls": []
}
```

### MCP Tools API
- `POST /api/mcp-tools/add-task` - Add a new task
- `POST /api/mcp-tools/list-tasks` - List tasks
- `POST /api/mcp-tools/complete-task` - Complete a task
- `POST /api/mcp-tools/delete-task` - Delete a task
- `POST /api/mcp-tools/update-task` - Update a task

## Conversation Flow (Stateless Request Cycle)

1. Receive user message
2. Fetch conversation history from database
3. Build message array for agent (history + new message)
4. Store user message in database
5. Run agent with MCP tools
6. Agent invokes appropriate MCP tool(s)
7. Store assistant response in database
8. Return response to client
9. Server holds NO state (ready for next request)

## Key Architecture Benefits

- **MCP Tools**: Standardized interface for AI to interact with the app
- **Single Endpoint**: Simplifies API - AI handles routing to tools
- **Stateless Server**: Scalable, resilient, horizontally scalable
- **Tool Composition**: Agent can chain multiple tools in one turn

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Database Migrations
```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Deployment

### Environment Variables
Create a `.env` file with the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost/dbname
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_secret_key
```

## Troubleshooting

1. **MCP Server Not Responding**: Ensure the MCP server is running and accessible
2. **Authentication Issues**: Verify JWT tokens are correctly formatted
3. **Database Connection**: Check DATABASE_URL configuration
4. **Frontend Not Connecting**: Verify CORS settings and API endpoints

## Future Enhancements

- Voice input/output capabilities
- Advanced NLP for more complex task management
- Integration with calendar applications
- Email notifications for task deadlines
- Multi-user collaboration features
- Advanced analytics and insights 
"# todo-app-phase-3" 
