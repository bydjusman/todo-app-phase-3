<!-- SYNC IMPACT REPORT
Version change: N/A (initial creation) → v1.0.0
Modified principles: N/A (new principles created)
Added sections: Core Principles (6), Technology Constraints, Development Workflow, Governance
Removed sections: N/A
Templates requiring updates: 
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated  
- .specify/templates/tasks-template.md ✅ updated
- .specify/commands/*.toml ✅ reviewed
- README.md ⚠ pending
Follow-up TODOs: None
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow the strict sequence: Constitution → Specifications → Plan → Tasks → Implementation. No agent may write code without approved specifications and tasks. Every feature, change, and enhancement must originate from an approved specification document.

### II. Agent Behavior Rules
Agents must operate within defined constraints: No manual coding by humans, no feature invention beyond approved specifications, no deviation from approved specifications, and all refinements must occur at the specification level, not during code implementation.

### III. Phase Governance
Each project phase is strictly scoped by its specification. Features from future phases must never leak into earlier phases. Architecture may evolve only through updated specifications and plans, maintaining clear boundaries between phases.

### IV. Technology Stack Compliance
All development must adhere to the approved technology stack: Python for backend services, Next.js for frontend in later phases, FastAPI for API frameworks, SQLModel for database interactions, Neon DB for data storage, OpenAI Agents SDK and MCP for agent communication, and Docker, Kubernetes, Kafka, and Dapr for infrastructure in later phases.

### V. Quality and Architecture Standards
All code must follow clean architecture principles with stateless services where required, clear separation of concerns, and cloud-native readiness. Code must be maintainable, testable, and scalable according to established architectural patterns.

### VI. Specification Integrity
Specifications are the authoritative source of truth for all development activities. Any changes to requirements must be reflected in updated specifications before implementation begins. Code implementation must strictly adhere to the approved specifications without deviation.

## Technology Constraints

The following technologies are approved for use in the Evolution of Todo project:

- Backend: Python with FastAPI framework
- Database: SQLModel with Neon DB
- Frontend: Next.js (introduced in later phases)
- Infrastructure: Docker, Kubernetes, Kafka, Dapr (introduced in later phases)
- Agent Framework: OpenAI Agents SDK with MCP
- Testing: pytest for backend, appropriate frontend testing frameworks
- Deployment: Containerized deployment with orchestration tools

All technology choices must align with these approved technologies unless explicitly updated through the specification process.

## Development Workflow

The development workflow must strictly follow these steps:

1. Specification creation and approval
2. Technical planning and architecture design
3. Task breakdown with acceptance criteria
4. Implementation following approved specifications
5. Testing and quality assurance
6. Review and approval process
7. Integration and deployment

No step may be skipped or performed out of sequence. Each phase must be completed and approved before proceeding to the next.

## Governance

This constitution serves as the supreme governing document for all agents and processes in the Evolution of Todo project. All activities must comply with these principles and requirements.

Amendments to this constitution require formal approval through the specification process. Any changes to the constitution must be documented, reviewed, and approved before implementation.

All agents working on this project must verify compliance with these principles during all development activities. Non-compliance must be reported and addressed immediately.

**Version**: v1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-01-01