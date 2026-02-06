<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: Added AI-native design, MCP compliance, Stateless architecture principles
- Added sections: MCP Tooling Standards, Agent Behavior Rules, Authentication & Security
- Removed sections: None
- Templates requiring updates: ✅ plan-template.md, ✅ spec-template.md, ✅ tasks-template.md
- Follow-up TODOs: None
-->
# Phase III – AI-Powered Todo Chatbot Constitution

## Core Principles

### AI-Native Design
AI-native design emphasizing agent → tool → database architecture. The system must be designed from the ground up to leverage AI agents that interact with deterministic tools for all operations. No manual coding outside of Claude Code, with strict adherence to agentic AI patterns.

### Strict Stateless Architecture
Backend holds NO in-memory state. Each request cycle must: 1) Fetch conversation history from database, 2) Append new user message, 3) Run agent with MCP tools, 4) Persist assistant response. All MCP tools themselves MUST be stateless with no hidden agent memory.

### Deterministic Tool Invocation
All MCP tool call IDs MUST be alphanumeric only (a-z, A-Z, 0-9), be ≤ 9 characters in length, and contain NO hyphens, underscores, or UUIDs. Tool IDs must be deterministic and human-readable (e.g., addtask01, listtask2, updatetsk, complet01, deletetsk). UUID-based or auto-generated tool call IDs are STRICTLY FORBIDDEN.

### Security-First Approach
All requests require JWT issued by Better Auth. User identity must be extracted from JWT. All task operations must be filtered by authenticated user. Cross-user data access is strictly prohibited. No manual coding, no prompt-only task manipulation, no direct DB access from frontend.

### MCP Compatibility Across Providers
System must work across OpenAI, Claude, and Mistral providers. MCP tools must be compatible with multiple AI providers without vendor lock-in. All natural language commands must correctly map to MCP tools that execute without provider validation errors.

### No Hallucinated Actions
The AI agent MUST use MCP tools for every task operation. The agent MUST NOT fabricate task IDs, user IDs, or database state. The agent MUST confirm successful actions in natural language. The agent MUST gracefully handle: Task not found, Ambiguous user intent, Invalid task references, and request clarification if intent cannot be resolved.

## MCP Tooling Standards

- All MCP tool call IDs MUST be alphanumeric only (a-z, A-Z, 0-9)
- All MCP tool call IDs MUST be ≤ 9 characters in length
- All MCP tool call IDs MUST contain NO hyphens, underscores, or UUIDs
- Tool IDs must be deterministic and human-readable
- Example valid IDs: addtask01, listtask2, updatetsk, complet01, deletetsk
- UUID-based or auto-generated tool call IDs are STRICTLY FORBIDDEN

## Agent Behavior Rules

- The AI agent MUST use MCP tools for every task operation
- The agent MUST NOT fabricate task IDs, user IDs, or database state
- The agent MUST confirm successful actions in natural language
- The agent MUST gracefully handle:
  - Task not found
  - Ambiguous user intent
  - Invalid task references
- The agent MUST request clarification if intent cannot be resolved

## Authentication & Security

- All requests require JWT issued by Better Auth
- User identity must be extracted from JWT
- All task operations must be filtered by authenticated user
- Cross-user data access is strictly prohibited
- No direct DB access from frontend
- No UUIDs in tool calls

## Development Workflow

- No manual coding (Claude Code only)
- No prompt-only task manipulation
- No hidden agent memory
- No direct DB access from frontend
- All persistence occurs via SQLModel + Neon PostgreSQL
- All MCP tools must be stateless
- Each request cycle follows: fetch → append → run → persist pattern

## Governance

All implementations must adhere to MCP compatibility standards. Any deviation from the specified tool ID format (alphanumeric, ≤9 characters, no UUIDs) is prohibited. All changes must maintain cross-provider compatibility across OpenAI, Claude, and Mistral. Compliance with stateless architecture requirements must be verified during code reviews. The constitution supersedes all other development practices.

**Version**: 1.1.0 | **Ratified**: 2026-01-29 | **Last Amended**: 2026-01-29