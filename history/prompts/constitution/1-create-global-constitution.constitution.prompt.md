---
id: 1
title: "Create Global Constitution"
stage: constitution
date_iso: "2025-01-01"
surface: "agent"
model: "Qwen"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution Create a single global constitution for the entire Evolution of Todo project"
labels:
  - "governance"
  - "spec-driven-development"
  - "project-structure"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
  - ".specify/templates/plan-template.md"
  - ".specify/templates/spec-template.md"
  - ".specify/templates/tasks-template.md"
tests_yaml: []
---

# Prompt History Record: Create Global Constitution

## Outcome
Successfully created a comprehensive constitution for the "Evolution of Todo" project covering all phases (I-V) and updated dependent templates to ensure consistency.

## Evaluation
The constitution establishes Spec-Driven Development as mandatory, defines agent behavior rules, sets phase governance, specifies technology constraints, and outlines quality principles. All templates were updated to reference and comply with the new constitution.

## Prompt Text
```
/sp.constitution /sp.constitution Create a single global constitution for the entire "Evolution of Todo" project
covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory
   - No agent may write code without approved specs and tasks
   - All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules
   - No manual coding by humans
   - No feature invention
   - No deviation from approved specifications
   - Refinement must occur at spec level, not code level

3. Phase Governance
   - Each phase is strictly scoped by its specification
   - Future-phase features must never leak into earlier phases
   - Architecture may evolve only through updated specs and plans

4. Technology Constraints
   - Python for backend
   - Next.js for frontend (later phases)
   - FastAPI, SQLModel, Neon DB
   - OpenAI Agents SDK, MCP
   - Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles
   - Clean architecture
   - Stateless services where required
   - Clear separation of concerns
   - Cloud-native readiness

This constitution must remain stable across all phases
and act as the supreme governing document for all agents.
```

## Response Text
Created a comprehensive constitution for the "Evolution of Todo" project that covers all phases (I-V) with the following key elements:

1. Spec-Driven Development as mandatory with strict sequence: Constitution → Specifications → Plan → Tasks → Implementation
2. Agent Behavior Rules: No manual coding by humans, no feature invention beyond approved specs, no deviation from approved specifications
3. Phase Governance: Strict adherence to phase specifications without cross-phase feature leakage
4. Technology Constraints: Python, FastAPI, SQLModel, Neon DB, Next.js, OpenAI Agents SDK, MCP, Docker, Kubernetes, Kafka, Dapr
5. Quality Principles: Clean architecture, stateless services, separation of concerns, cloud-native readiness

Updated templates to ensure consistency:
- Updated plan-template.md to include constitution compliance check
- Updated spec-template.md to include constitution compliance section
- Updated tasks-template.md to include constitution compliance section

The constitution is now the supreme governing document for all agents in the project.