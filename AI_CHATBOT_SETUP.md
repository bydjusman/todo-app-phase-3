# AI Chatbot Setup Guide

## Overview
Your todo app already has a fully implemented AI chatbot using Google's Generative AI. Follow these steps to ensure it works properly.

## Prerequisites
- Python 3.8+
- Node.js 18+
- Google AI API key with sufficient quota

## Step 1: Configure Google AI API Key

1. Get your Google AI API key from the [Google AI Studio](https://aistudio.google.com/)
2. Add it to your `.env` file in the backend directory:

```env
# Google AI Configuration
GOOGLE_API_KEY=your_actual_google_api_key_here
```

## Step 2: Install Dependencies

Make sure you have all required dependencies installed:

Backend:
```bash
cd backend
pip install -r requirements.txt
```

Frontend:
```bash
cd frontend
npm install
```

## Step 3: Start the Services

1. Start the backend server:
```bash
cd backend
python -m uvicorn app.main:app --reload
```

2. Start the frontend:
```bash
cd frontend
npm run dev
```

## Step 4: Test the Chatbot

1. Visit the frontend at http://localhost:3000
2. Register a new account or log in
3. Navigate to the chat page at http://localhost:3000/chat
4. Start chatting with the AI assistant

## Supported Commands

The AI chatbot understands natural language commands such as:

- "Add a task to buy groceries"
- "Show me my tasks"
- "What's pending?"
- "Mark task 3 as complete"
- "Delete the meeting task"
- "Change task 1 to 'Call mom tonight'"
- "I need to remember to pay bills"
- "What have I completed?"

## Troubleshooting

1. **Rate Limit Errors**: If you see quota exceeded errors, check your Google AI plan and billing details.

2. **Authentication Issues**: Ensure your JWT token is valid and properly sent with requests.

3. **Database Connection**: Verify your DATABASE_URL is correctly configured.

4. **CORS Issues**: Check that your frontend origin is allowed in the backend CORS configuration.

## Architecture

The AI chatbot uses the following architecture:

```
┌─────────────────┐     ┌──────────────────────────────────────────────┐     ┌─────────────────┐
│                 │     │              FastAPI Server                   │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │     │    Database     │
│  Chat Interface │────▶│  │         Chat Endpoint                  │  │     │  (PostgreSQL)   │
│  (Frontend)     │     │  │  POST /api/chat                        │  │     │                 │
│                 │     │  └───────────────┬────────────────────────┘  │────▶│  - tasks        │
│                 │     │                  │                           │     │  - conversations│
│                 │     │                  ▼                           │     │  - messages     │
│                 │     │  ┌────────────────────────────────────────┐  │     │                 │
│                 │◀────│  │      Google AI Agent                  │  │     │                 │
│                 │     │  │      (Google Generative AI)           │  │     │                 │
│                 │     │  └───────────────┬────────────────────────┘  │     │                 │
│                 │     │                  │                           │     │                 │
│                 │     │                  ▼                           │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │────▶│                 │
│                 │     │  │         MCP Tools                 │  │     │                 │
│                 │     │  │  (Task Operations)                    │  │◀────│                 │
│                 │     │  └────────────────────────────────────────┘  │     │                 │
└─────────────────┘     └──────────────────────────────────────────────┘     └─────────────────┘
```

## Customization

You can customize the chatbot's behavior by modifying:
- `backend/app/core/google_ai_agent.py` - AI processing logic
- `backend/app/tools/` - Task operation tools
- `backend/app/core/agent_service.py` - Agent service logic