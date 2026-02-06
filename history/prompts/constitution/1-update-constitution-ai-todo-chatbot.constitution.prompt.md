---
id: 1
title: "update-constitution-ai-todo-chatbot"
stage: "constitution"
dateIso: "2026-01-29"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "phase-3-ai-todo-chatbot"
branch: "main"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "ai", "mcp", "todo-chatbot"]
spec: null
ticket: null
adr: null
pr: null
files:
  - ".specify/memory/constitution.md"
tests: []
---

# Prompt History Record

## Command
`/sp.constitution`

## User Input
```
Phase III – AI-Powered Todo Chatbot (MCP-Safe)

Project:
Hackathon 2 – Phase III: AI-powered conversational Todo application using MCP and Agentic AI.

Core principles:
- AI-native design (agent → tool → database)
- Strict stateless architecture (no server memory)
- Deterministic tool invocation (no hallucinated actions)
- Security-first (authenticated, user-isolated operations)
- MCP compatibility across providers (Claude, OpenAI, Mistral)

Critical MCP & Tooling Standards:
- All MCP tool call IDs MUST:
  - Be alphanumeric only (a–z, A–Z, 0–9)
  - Be ≤ 9 characters in length
  - Contain NO hyphens, underscores, or UUIDs
- Tool IDs must be deterministic and human-readable
- Example valid IDs:
  - addtask01
  - listtask2
  - updatetsk
  - complet01
  - deletetsk
- UUID-based or auto-generated tool call IDs are STRICTLY FORBIDDEN

Agent Behavior Rules:
- The AI agent MUST use MCP tools for every task operation
- The agent MUST NOT fabricate task IDs, user IDs, or database state
- The agent MUST confirm successful actions in natural language
- The agent MUST gracefully handle:
  - Task not found
  - Ambiguous user intent
  - Invalid task references
- The agent MUST request clarification if intent cannot be resolved

Stateless Conversation Rules:
- Backend holds NO in-memory state
- Each request cycle must:
  1. Fetch conversation history from database
  2. Append new user message
  3. Run agent with MCP tools
  4. Persist assistant response
- MCP tools themselves MUST be stateless
- All persistence occurs via SQLModel + Neon PostgreSQL

Authentication & Security:
- All requests require JWT issued by Better Auth
- User identity must be extracted from JWT
- All task operations must be filtered by authenticated user
- Cross-user data access is strictly prohibited

Constraints:
- No manual coding (Claude Code only)
- No prompt-only task manipulation
- No hidden agent memory
- No direct DB access from frontend
- No UUIDs in tool calls

Success criteria:
- All natural language commands correctly map to MCP tools
- Tool calls execute without provider validation errors
- Works across OpenAI, Claude, and Mistral providers
- Phase III passes /sp.analyze with zero CRITICAL issues
```

## Response Summary
Updated the project constitution at `.specify/memory/constitution.md` to reflect the specific requirements for the Phase III AI-Powered Todo Chatbot project. The new constitution incorporates all the MCP and tooling standards, agent behavior rules, and security requirements specified in the user input. The version has been updated from 1.0.0 to 1.1.0 to reflect the addition of new principles and sections.

## Outcome
The constitution now properly defines the core principles for the AI-Powered Todo Chatbot project, including AI-Native Design, Strict Stateless Architecture, Deterministic Tool Invocation, Security-First Approach, MCP Compatibility Across Providers, and No Hallucinated Actions. Additional sections for MCP Tooling Standards, Agent Behavior Rules, Authentication & Security, and Development Workflow were added to ensure compliance with the project requirements.

## Evaluation
The updated constitution meets all requirements specified in the user input, with no placeholder tokens remaining and proper versioning applied.