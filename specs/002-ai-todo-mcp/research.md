# Research: AI-Powered Todo Chatbot with MCP

## Overview

This document captures research findings and decisions made during the planning phase for the AI-Powered Todo Chatbot with MCP implementation.

## MCP Tool Implementation Patterns

**Decision**: Use official MCP SDK to implement a separate MCP server that exposes task operations as standardized tools.

**Rationale**: MCP (Model Context Protocol) provides a standardized way to expose tools to AI agents across multiple providers (OpenAI, Claude, Mistral). This ensures compatibility and follows best practices for AI agent integration.

**Alternatives considered**:
- Direct function calls from agent: Would violate MCP standards and reduce provider compatibility
- Custom API endpoints: Would not leverage MCP benefits and create vendor lock-in

## Agent-Tool Communication Architecture

**Decision**: Implement a stateless communication pattern where the AI agent calls MCP tools that operate on the database directly.

**Rationale**: Maintains the required stateless architecture while enabling the agent to perform all necessary operations. The agent never holds state or directly accesses the database.

**Alternatives considered**:
- Agent holding temporary state: Would violate the stateless architecture requirement
- Direct agent-database access: Would violate security requirements and bypass MCP tools

## MCP Tool Call ID Standards

**Decision**: Use alphanumeric-only, ≤9 character, deterministic tool call IDs as required by the constitution.

**Rationale**: Ensures compatibility across all AI providers and maintains auditability of tool calls. Examples: addtask01, listtask2, updatetsk, complet01, deletetsk.

**Alternatives considered**:
- UUID-based IDs: Prohibited by constitution for provider compatibility
- Longer descriptive names: Would exceed character limits

## Authentication and User Isolation

**Decision**: Implement JWT-based authentication with user ID extraction and enforcement at both API and MCP tool levels.

**Rationale**: Provides secure user isolation and meets security-first requirements. JWT tokens are verified at the API gateway and user context is passed to MCP tools.

**Alternatives considered**:
- Session-based authentication: Insufficient for stateless architecture
- API keys: Less secure than JWT tokens

## Database Persistence Strategy

**Decision**: Use SQLModel ORM for database operations to ensure clean, testable, and maintainable code.

**Rationale**: SQLModel provides type safety, validation, and clean integration with FastAPI. It supports the required database operations while maintaining code quality.

**Alternatives considered**:
- Raw SQL queries: Harder to maintain and test
- Other ORMs: SQLModel integrates well with FastAPI ecosystem

## Conversation State Management

**Decision**: Store conversation history in the database and fetch it for each request to maintain stateless operation.

**Rationale**: Enables conversation continuity while maintaining the required stateless architecture. Each request cycle fetches the conversation history before agent processing.

**Alternatives considered**:
- In-memory storage: Would violate stateless requirements
- Client-side storage: Would compromise security and reliability

## Error Handling Strategy

**Decision**: Implement graceful error handling with clear messages for all scenarios (task not found, invalid input, auth failures).

**Rationale**: Provides good user experience while maintaining system stability. MCP tools return structured error responses that the agent can interpret.

**Alternatives considered**:
- Generic error messages: Would provide poor user experience
- System crash on errors: Would violate stability requirements