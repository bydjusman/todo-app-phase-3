# Quickstart Guide: AI-Powered Todo Chatbot with MCP

## Overview

This guide provides a quick introduction to setting up and running the AI-Powered Todo Chatbot with MCP system.

## Prerequisites

- Python 3.11+
- PostgreSQL database
- OpenAI API key (or alternative provider keys)
- Better Auth credentials

## Environment Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd todo-chatbot-mcp
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit the .env file with your configuration
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://username:password@localhost/dbname
   JWT_SECRET=your_jwt_secret
   BETTER_AUTH_SECRET=your_auth_secret
   ```

## Database Setup

1. **Initialize the database**:
   ```bash
   python -m backend.app.core.database init
   ```

2. **Run migrations**:
   ```bash
   python -m backend.app.core.database migrate
   ```

## Running the Services

1. **Start the MCP server**:
   ```bash
   python -m backend.mcp_server.main
   ```
   The MCP server will run on `http://localhost:8001` by default.

2. **Start the main API server**:
   ```bash
   uvicorn backend.app.main:app --reload --port 8000
   ```
   The API server will run on `http://localhost:8000`.

## Testing the System

1. **Verify the services are running**:
   - API server health check: `GET http://localhost:8000/health`
   - MCP server health check: `GET http://localhost:8001/health`

2. **Test the chat endpoint** (with a valid JWT token):
   ```bash
   curl -X POST http://localhost:8000/api/chat \
     -H "Authorization: Bearer <valid-jwt-token>" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Add a task to buy groceries"
     }'
   ```

## Using the Chat Interface

1. **Authenticate**: Obtain a JWT token from Better Auth
2. **Send messages**: Use the `/api/chat` endpoint with your JWT token
3. **Receive responses**: The AI agent will process your natural language and respond

## Example Commands

Try these example commands with the chatbot:
- "Add a task to buy groceries"
- "What tasks are pending?"
- "Mark task 2 as complete"
- "Show me my completed tasks"
- "Update task 1 to call mom tonight"

## Architecture Components

- **Frontend**: OpenAI ChatKit (handles user interface)
- **Backend API**: FastAPI server (handles authentication, conversation flow)
- **AI Agent**: OpenAI Agents SDK (interprets natural language)
- **MCP Server**: MCP SDK server (exposes task operations as tools)
- **Database**: PostgreSQL (stores users, tasks, conversations)

## Troubleshooting

- **MCP tools not being called**: Verify the MCP server is running and accessible
- **Authentication errors**: Check that your JWT token is valid and properly formatted
- **Database connection issues**: Verify your DATABASE_URL is correct
- **AI agent not responding**: Check that your API key is valid and has sufficient quota