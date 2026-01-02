---

description: "Task list for Phase I Todo Console Application"
---

# Tasks: Phase I Todo Console Application

**Input**: Design documents from `/specs/001-todo-phase1-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: These tasks must comply with the Evolution of Todo Constitution which mandates:
- Spec-Driven Development: All work follows Constitution → Specifications → Plan → Tasks → Implementation
- Agent Behavior Rules: No manual coding by humans, no feature invention beyond specs
- Phase Governance: Strict adherence to phase specifications without cross-phase feature leakage
- Technology Stack Compliance: Python, FastAPI, SQLModel, Neon DB, Next.js, OpenAI Agents SDK, MCP
- Quality and Architecture Standards: Clean architecture, stateless services, separation of concerns

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 [P] Create src/todo_app/__init__.py
- [X] T003 [P] Create src/todo_app/models/__init__.py
- [X] T004 [P] Create src/todo_app/services/__init__.py
- [X] T005 [P] Create src/todo_app/cli/__init__.py
- [X] T006 [P] Create tests/unit/__init__.py
- [X] T007 [P] Create tests/integration/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T008 Create Task data model in src/todo_app/models/task.py
- [X] T009 Create TaskService in src/todo_app/services/task_service.py
- [X] T010 Create CLI menu structure in src/todo_app/cli/main.py
- [X] T011 [P] Create unit tests for Task model in tests/unit/test_task.py
- [X] T012 [P] Create unit tests for TaskService in tests/unit/test_task_service.py
- [X] T013 [P] Create integration tests for CLI in tests/integration/test_cli.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with unique IDs and "Incomplete" status

**Independent Test**: The application allows a user to add a new task via the CLI interface and displays confirmation that the task was added successfully.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T014 [P] [US1] Contract test for add_task functionality in tests/unit/test_task_service.py
- [X] T015 [P] [US1] Integration test for add task flow in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T016 [P] [US1] Implement Task model with id, description, status fields in src/todo_app/models/task.py
- [X] T017 [US1] Implement add_task method in TaskService in src/todo_app/services/task_service.py
- [X] T018 [US1] Implement add task CLI interface in src/todo_app/cli/main.py
- [X] T019 [US1] Add validation for empty task descriptions in src/todo_app/services/task_service.py
- [X] T020 [US1] Add sequential ID generation in src/todo_app/services/task_service.py
- [X] T021 [US1] Add default "Incomplete" status assignment in src/todo_app/services/task_service.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Enable users to view their complete task list with ID, description, and completion status

**Independent Test**: The application displays all tasks in the list with their ID, description, and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T022 [P] [US2] Contract test for view_task_list functionality in tests/unit/test_task_service.py
- [X] T023 [P] [US2] Integration test for view task list flow in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T024 [P] [US2] Implement get_all_tasks method in TaskService in src/todo_app/services/task_service.py
- [X] T025 [US2] Implement view task list CLI interface in src/todo_app/cli/main.py
- [X] T026 [US2] Add formatted display of tasks with ID, description, and status in src/todo_app/cli/main.py
- [X] T027 [US2] Handle empty task list case with appropriate message in src/todo_app/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Description (Priority: P2)

**Goal**: Enable users to update the description of existing tasks by providing task ID and new description

**Independent Test**: The application allows a user to update the description of an existing task by providing the task ID and new description.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T028 [P] [US3] Contract test for update_task functionality in tests/unit/test_task_service.py
- [X] T029 [P] [US3] Integration test for update task flow in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T030 [P] [US3] Implement update_task_description method in TaskService in src/todo_app/services/task_service.py
- [X] T031 [US3] Implement update task CLI interface in src/todo_app/cli/main.py
- [X] T032 [US3] Add validation for invalid task IDs in src/todo_app/services/task_service.py
- [X] T033 [US3] Add validation for empty new descriptions in src/todo_app/services/task_service.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Enable users to delete tasks by providing their ID with appropriate confirmation

**Independent Test**: The application allows a user to delete a task by providing its ID and confirms the deletion.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T034 [P] [US4] Contract test for delete_task functionality in tests/unit/test_task_service.py
- [X] T035 [P] [US4] Integration test for delete task flow in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T036 [P] [US4] Implement delete_task method in TaskService in src/todo_app/services/task_service.py
- [X] T037 [US4] Implement delete task CLI interface with confirmation in src/todo_app/cli/main.py
- [X] T038 [US4] Add validation for invalid task IDs in src/todo_app/services/task_service.py
- [X] T039 [US4] Add confirmation prompt for deletion in src/todo_app/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Enable users to change the completion status of tasks by providing their ID

**Independent Test**: The application allows a user to change the completion status of a task by providing its ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T040 [P] [US5] Contract test for update_task_status functionality in tests/unit/test_task_service.py
- [X] T041 [P] [US5] Integration test for mark task complete/incomplete flow in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T042 [P] [US5] Implement update_task_status method in TaskService in src/todo_app/services/task_service.py
- [X] T043 [US5] Implement mark task complete/incomplete CLI interface in src/todo_app/cli/main.py
- [X] T044 [US5] Add validation for invalid task IDs in src/todo_app/services/task_service.py
- [X] T045 [US5] Add validation for invalid status values in src/todo_app/services/task_service.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T046 [P] Handle invalid menu options with error messages in src/todo_app/cli/main.py
- [X] T047 [P] Add input validation for very long task descriptions in src/todo_app/services/task_service.py
- [X] T048 [P] Handle special characters in task descriptions in src/todo_app/services/task_service.py
- [X] T049 [P] Add error handling for missing task IDs in src/todo_app/services/task_service.py
- [X] T050 [P] Add graceful handling of empty task lists in all operations in src/todo_app/services/task_service.py
- [X] T051 [P] Documentation updates in src/todo_app/
- [X] T052 [P] Code cleanup and refactoring
- [X] T053 [P] Performance optimization to ensure <100ms response time
- [X] T054 [P] Additional unit tests (if requested) in tests/unit/
- [X] T055 [P] Security hardening
- [X] T056 [P] Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add_task functionality in tests/unit/test_task_service.py"
Task: "Integration test for add task flow in tests/integration/test_cli.py"

# Launch all models for User Story 1 together:
Task: "Implement Task model with id, description, status fields in src/todo_app/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 5 (also P1)
   - Developer D: User Story 3
   - Developer E: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence