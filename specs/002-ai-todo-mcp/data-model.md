# Data Model: AI-Powered Todo Chatbot with MCP

## Overview

This document defines the data models for the AI-Powered Todo Chatbot with MCP system.

## Entity: User

**Description**: Represents an authenticated user in the system

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `email`: String(255), Unique, Not Null
- `name`: String(255), Optional
- `created_at`: DateTime, Not Null, Default: current timestamp
- `updated_at`: DateTime, Not Null, Default: current timestamp

**Validation**:
- Email must be a valid email format
- Email must be unique across all users

**Relationships**:
- One-to-Many: User has many Tasks
- One-to-Many: User has many Conversations

## Entity: Task

**Description**: Represents a user's todo item

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `user_id`: Integer, Foreign Key to User.id, Not Null
- `title`: String(500), Not Null
- `description`: Text, Optional
- `status`: String(20), Not Null, Default: "pending", Values: ["pending", "completed"]
- `due_date`: DateTime, Optional
- `created_at`: DateTime, Not Null, Default: current timestamp
- `updated_at`: DateTime, Not Null, Default: current timestamp
- `completed_at`: DateTime, Optional

**Validation**:
- Status must be one of allowed values: "pending", "completed"
- User_id must reference an existing user

**State Transitions**:
- From "pending" to "completed": When task is marked as complete
- From "completed" to "pending": When task is marked as incomplete (optional feature)

**Relationships**:
- Many-to-One: Task belongs to one User
- One-to-Many: Task has many ConversationEntries (via conversation history)

## Entity: Conversation

**Description**: Represents a conversation thread between user and AI agent

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `user_id`: Integer, Foreign Key to User.id, Not Null
- `title`: String(255), Optional, Auto-generated based on first message
- `created_at`: DateTime, Not Null, Default: current timestamp
- `updated_at`: DateTime, Not Null, Default: current timestamp

**Validation**:
- User_id must reference an existing user

**Relationships**:
- Many-to-One: Conversation belongs to one User
- One-to-Many: Conversation has many ConversationEntries

## Entity: ConversationEntry

**Description**: Represents a single message in a conversation (either from user or AI agent)

**Fields**:
- `id`: Integer, Primary Key, Auto-increment
- `conversation_id`: Integer, Foreign Key to Conversation.id, Not Null
- `role`: String(10), Not Null, Values: ["user", "assistant"]
- `content`: Text, Not Null
- `timestamp`: DateTime, Not Null, Default: current timestamp
- `tool_calls`: JSON, Optional, Records MCP tool calls made during this interaction
- `tool_responses`: JSON, Optional, Records MCP tool responses

**Validation**:
- Role must be one of allowed values: "user", "assistant"
- Conversation_id must reference an existing conversation

**Relationships**:
- Many-to-One: ConversationEntry belongs to one Conversation

## Indexes

**User**:
- Index on `email` for fast authentication lookups

**Task**:
- Index on `user_id` for user-specific queries
- Index on `status` for filtering by task status
- Index on `user_id` and `status` for combined queries

**Conversation**:
- Index on `user_id` for user-specific queries
- Index on `created_at` for chronological ordering

**ConversationEntry**:
- Index on `conversation_id` for conversation-specific queries
- Index on `timestamp` for chronological ordering
- Index on `conversation_id` and `timestamp` for ordered retrieval

## Constraints

1. **Referential Integrity**: All foreign key relationships enforce referential integrity
2. **User Isolation**: All queries must filter by user_id to ensure data isolation
3. **Data Consistency**: Updates to task status must update completed_at accordingly
4. **Audit Trail**: All entities have created_at and updated_at timestamps for tracking changes