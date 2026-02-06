---
id: 2
title: "plan-ai-todo-chatbot"
stage: "plan"
dateIso: "2026-01-29"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "ai-todo-mcp"
branch: "002-ai-todo-mcp"
user: "user"
command: "/sp.plan"
labels: ["plan", "ai", "mcp", "todo", "architecture"]
spec: "specs/002-ai-todo-mcp/spec.md"
ticket: null
adr: null
pr: null
files:
  - "specs/002-ai-todo-mcp/plan.md"
  - "specs/002-ai-todo-mcp/research.md"
  - "specs/002-ai-todo-mcp/data-model.md"
  - "specs/002-ai-todo-mcp/quickstart.md"
  - "specs/002-ai-todo-mcp/contracts/add_task.md"
  - "specs/002-ai-todo-mcp/contracts/list_tasks.md"
  - "specs/002-ai-todo-mcp/contracts/update_task.md"
  - "specs/002-ai-todo-mcp/contracts/complete_task.md"
  - "specs/002-ai-todo-mcp/contracts/delete_task.md"
tests: []
---

# Prompt History Record

## Command
`/sp.plan Phase III – AI-Powered Todo Chatbot with MCP`

## User Input
```
/sp.plan Phase III – AI-Powered Todo Chatbot with MCP

Create:
- System architecture sketch (logical + request flow)
- Component-level design for Agent, MCP Server, Backend, Database
- Conversation lifecycle and stateless request cycle
- MCP tool design and invocation flow
- Authentication and user isolation strategy
- Quality validation and acceptance checks

Architecture overview:
- Frontend (OpenAI ChatKit):
  - Sends user messages with JWT token
  - Receives assistant responses only
  - Holds no business logic or state

- Backend (FastAPI):
  - Stateless chat endpoint (/api/chat)
  - Fetches conversation history from database
  - Passes messages to OpenAI Agents SDK
  - Persists user + assistant messages
  - Verifies JWT via Better Auth

- AI Layer (OpenAI Agents SDK):
  - Interprets natural language intent
  - Decides which MCP tool(s) to call
  - Never accesses database directly
  - Never stores memory internally

- MCP Server (Official MCP SDK):
  - Exposes task operations as tools
  - Tools are stateless
  - All state changes persisted via SQLModel
  - Uses safe, deterministic tool call IDs

- Database (Neon PostgreSQL):
  - Stores users, tasks, and conversation history
  - Acts as the single source of truth

Conversation request flow (stateless):
1. Receive user message + JWT
2. Authenticate user via JWT
3. Fetch conversation history from database
4. Append new user message
5. Run agent with MCP tools
6. Agent invokes one or more MCP tools
7. MCP tools persist changes to database
8. Store assistant response in database
9. Return assistant response to client
10. Server forgets everything (stateless)

MCP tool design:
- Tools to define:
  - add_task
  - list_tasks
  - update_task
  - complete_task
  - delete_task
- Each tool:
  - Accepts user_id and task-specific parameters
  - Performs ownership validation
  - Reads/writes via SQLModel
  - Returns structured response
- Tool call IDs must be:
  - Alphanumeric only
  - ≤ 9 characters
  - Deterministic (no UUIDs)

Agent decision rules:
- Always map user intent to MCP tools
- Never perform task logic without tool invocation
- If task reference is ambiguous:
  - Call list_tasks first
  - Ask for clarification if needed
- Always confirm completed actions in natural language
- Gracefully handle errors (task not found, invalid input)

Authentication & security plan:
- JWT issued by Better Auth on frontend
- Backend verifies JWT on every request
- User ID extracted from token
- All MCP tools enforce user-level data isolation
- No cross-user data access under any condition

Decisions needing documentation (ADRs):
- Why MCP over direct function calls
- Why stateless backend with DB-backed memory
- Why Agents SDK instead of prompt-only logic
- Why deterministic tool call IDs for provider compatibility

Testing & validation strategy:
- Manual acceptance testing using example prompts:
  - "Add a task to buy groceries"
  - "What tasks are pending?"
  - "Mark task 2 as complete"
- Verify:
  - Correct MCP tool invoked
  - Database state updated correctly
  - Conversation continuity across requests
  - Unauthorized requests return 401
- Validation via /sp.analyze against:
  - Success criteria
  - Functional scope
  - Stateless guarantees

Planning structure:
- Phase A: Architecture & ADRs
- Phase B: MCP tool contracts
- Phase C: Agent behavior logic
- Phase D: Conversation persistence
- Phase E: Validation & polish

Output expectations:
- Clear architectural blueprint
- Ready input for /sp.tasks
- No implementation code
- Fully aligned with Phase III /sp.specify
```

## Response Summary
Created a comprehensive implementation plan for the AI-Powered Todo Chatbot with MCP project. The plan includes: technical context, constitution compliance check, project structure, research findings, data models, MCP tool contracts (add_task, list_tasks, update_task, complete_task, delete_task), and a quickstart guide. All components align with the stateless architecture, MCP compatibility requirements, and security-first approach specified in the constitution.

## Outcome
Successfully created the implementation plan with all required components:
- plan.md: Overall implementation strategy and architecture
- research.md: Technical research and decision justification
- data-model.md: Detailed entity relationships and validation rules
- quickstart.md: Setup and usage instructions
- contracts/: MCP tool specifications for all five required tools
- All artifacts comply with constitution requirements (stateless, deterministic tool IDs, security-first)

## Evaluation
The implementation plan fully satisfies the requirements with proper separation of concerns, MCP compliance, and adherence to the stateless architecture principles. The plan is ready for the next phase (/sp.tasks) to generate implementation tasks.