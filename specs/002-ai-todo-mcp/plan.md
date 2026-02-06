# Implementation Plan: AI-Powered Todo Chatbot with MCP

**Branch**: `002-ai-todo-mcp` | **Date**: 2026-01-29 | **Spec**: [specs/002-ai-todo-mcp/spec.md](specs/002-ai-todo-mcp/spec.md)
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of an AI-powered todo chatbot using MCP (Model Context Protocol) that allows users to manage tasks through natural language commands. The system uses a stateless architecture with an AI agent that interprets user intents and maps them to predefined MCP tools for task operations. The architecture emphasizes strict separation between the AI layer, MCP tools, and database persistence.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Official MCP SDK, SQLModel, Better Auth
**Storage**: PostgreSQL database (via SQLModel ORM)
**Testing**: pytest for unit and integration tests
**Target Platform**: Linux server (cloud deployment)
**Project Type**: Web application (backend service)
**Performance Goals**: Handle 1000 concurrent users, response time <2 seconds for AI processing
**Constraints**: <200ms p95 for database operations, stateless operation between requests, no in-memory state
**Scale/Scope**: Support 10k users, secure user isolation, MCP tool call IDs ≤9 characters

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] AI-Native Design: System designed with agent → tool → database architecture
- [x] Strict Stateless Architecture: Backend holds no in-memory state between requests
- [x] Deterministic Tool Invocation: MCP tool call IDs will be alphanumeric only, ≤9 characters
- [x] Security-First Approach: JWT authentication required, user isolation enforced
- [x] MCP Compatibility: System works across multiple AI providers (OpenAI, Claude, Mistral)
- [x] No Hallucinated Actions: Agent uses MCP tools for all operations, never fabricates data
- [x] Development Workflow: No manual coding (Claude Code only), MCP tools stateless

## Project Structure

### Documentation (this feature)

```text
specs/002-ai-todo-mcp/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py      # Chat endpoint implementation
│   │   └── auth.py      # Authentication middleware
│   ├── core/
│   │   ├── agent_service.py  # AI agent orchestration
│   │   ├── auth.py      # JWT verification
│   │   └── database.py  # Database session management
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py      # User model
│   │   ├── task.py      # Task model
│   │   └── conversation.py # Conversation model
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── base.py      # Base tool definitions
│   │   ├── add_task.py  # Add task MCP tool
│   │   ├── list_tasks.py # List tasks MCP tool
│   │   ├── update_task.py # Update task MCP tool
│   │   ├── complete_task.py # Complete task MCP tool
│   │   └── delete_task.py # Delete task MCP tool
│   └── schemas/
│       ├── __init__.py
│       ├── user.py      # User schema
│       ├── task.py      # Task schema
│       └── conversation.py # Conversation schema
├── mcp_server/
│   ├── main.py          # MCP server entry point
│   ├── tools/           # MCP tool implementations
│   └── config.py        # MCP server configuration
├── tests/
│   ├── unit/
│   │   ├── test_models/ # Unit tests for models
│   │   └── test_tools/  # Unit tests for MCP tools
│   ├── integration/
│   │   └── test_api/    # Integration tests for API
│   └── contract/        # Contract tests for MCP tools
└── requirements.txt     # Python dependencies
```

**Structure Decision**: Selected web application structure with separate backend for the AI-powered todo chatbot service. The backend contains API endpoints, models, tools, and schemas. MCP server runs separately to handle tool invocations.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Separate MCP server | Required for MCP protocol compliance and provider compatibility | Embedding tools in main app would violate MCP standards |
| JWT authentication | Required for user isolation and security | Session cookies insufficient for API-only architecture |
| SQLModel ORM | Required for clean database interactions | Direct SQL queries harder to maintain and test |