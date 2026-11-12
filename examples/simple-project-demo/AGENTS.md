# Magnetar Agent Routing & Operational Protocol

> This document is the primary entry point and routing protocol for AI coding agents (Claude, Gemini, Codex, Copilot, Cursor, etc.) collaborating on a Magnetar project. It defines which markdown documents to consult and update for each development activity, preventing context dilution and hallucination.

---

## 1. Core Philosophy: The Markdown Nervous System

In the Magnetar model:
- **Agents are transient execution workers**: AI agents have stateless sessions, finite context windows, and tend to drift over long conversations.
- **Markdown documents are the persistent state machine**: Files like `PLAN.md`, `BITACORA.md`, `REQUIREMENTS.md`, and `STATUS.md` form the durable external memory and audit trail of the project.
- **Spec-Driven Governance**: Agents do not invent scope, alter architectures, or bypass WIP rules without documenting rationale in the canonical markdown files.

---

## 2. Agent Context Router: What to Read & What to Update

Instead of ingesting the entire documentation set into your context window on every turn, consult the targeted files below based on your immediate task:

| Lifecycle Phase / Action | Primary Files to READ | Files to UPDATE | Invariant Rule |
| :--- | :--- | :--- | :--- |
| **Project Orientation** | `projects/*.project.yml`, `README.md`, `RULES.md` | *None* | Identify project tier (`micro`, `standard`, `extended`) before executing any work. |
| **Selecting Next Task** | `PLAN.md` (look for `ready` state), `WIP_GUIDELINES.md` | `PLAN.md` (`ready → in_progress`), `BITACORA.md` | Never exceed maximum **2** concurrent `in_progress` tasks per contributor/agent. |
| **Scoping & Feature Design** | `REQUIREMENTS.md`, `ARCHITECTURE.md` | `REQUIREMENTS.md`, `PLAN.md` | Do not write code until acceptance criteria and effort points are documented. |
| **Architectural Decision** | `ARCHITECTURE.md`, `DECISIONS.md` | `DECISIONS.md` (record ADR), `ARCHITECTURE.md` | Any structural change or technology choice requires a recorded decision in `DECISIONS.md`. |
| **Coding & Implementation** | Task details in `PLAN.md`, coding standards in `RULES.md` | Source code files, `BITACORA.md` | Maintain atomic commits referencing the task ID (e.g. `feat(task-102): ...`). |
| **Encountering a Blocker** | `RULES.md` (Blocker Lifecycle) | `BLOCKERS.md`, `STATUS.md`, `BITACORA.md`, `PLAN.md` (`→ blocked`) | A blocked task stops counting toward active WIP, but must have a documented escalation path. |
| **Testing & Quality Assurance** | `TESTING.md`, Acceptance Criteria in `REQUIREMENTS.md` | `TESTING.md`, `STATUS.md` (tested %) | No task transitions to `done` without passing verification defined in `TESTING.md`. |
| **Submitting for Review** | PR checklist in `CONTRIBUTING.md`, `BRANCHING_MODEL.md` | `PLAN.md` (`in_progress → in_review`), `BITACORA.md` | Open PRs only from properly named feature branches (e.g. `feature/<task-id>-<desc>`). |
| **Task Completion & Sign-off** | `PLAN.md` acceptance criteria | `PLAN.md` (`in_review → done`), `STATUS.md`, `BITACORA.md` | Recalculate effort points and progress percentage in `STATUS.md`. |

---

## 3. Project Sizing Tiers (Context Sensitivity)

Magnetar recognizes three project scales. Adjust your documentation overhead accordingly:

```
+-----------------------------------------------------------------+
| TIER 1: MICRO (Spike, Script, Prototype, < 1 week)              |
| Docs: README.md, AGENTS.md, PLAN.md, STATUS.md, RULES.md        |
+-----------------------------------------------------------------+
                                |
                                v
+-----------------------------------------------------------------+
| TIER 2: STANDARD (Application, Service, Library, 1-3 months)   |
| Docs: Tier 1 + REQUIREMENTS, ARCHITECTURE, BITACORA, TESTING,   |
|       BLOCKERS, BRANCHING_MODEL, WIP_GUIDELINES, project.yml    |
+-----------------------------------------------------------------+
                                |
                                v
+-----------------------------------------------------------------+
| TIER 3: EXTENDED (Multi-service, Monorepo, Enterprise, Regulated)|
| Docs: Tier 2 + DECISIONS.md (ADRs), GLOSSARY.md, SECURITY.md,   |
|       MODEL_POLICY.md, automated CI linting                     |
+-----------------------------------------------------------------+
```

If you are working in a **Tier 1 (Micro)** project, do not enforce or create unnecessary heavy governance files unless formally requested. Always respect the declared `tier:` field in `projects/*.project.yml`.

---

## 4. Invariant Rules for AI Agents

1. **Never "Vibe Code"**: Always verify you have a designated task ID from `PLAN.md` before altering codebase files.
2. **Respect the WIP Limit**: Check active tasks in `PLAN.md`. If you or your collaborator already have 2 tasks in `in_progress`, finish or transition one before opening another.
3. **Log Every Transition in `BITACORA.md`**:
   Format:
   ```markdown
   | YYYY-MM-DD | HH:MM | Agent/<ModelName> | [task-id] Moved from ready to in_progress. Starting implementation of ... |
   ```
4. **Valid Task States Only**:
   Allowed states are strictly: `planned`, `ready`, `in_progress`, `in_review`, `blocked`, `done`.
5. **No Blind Assumptions**: If specifications in `REQUIREMENTS.md` or `ARCHITECTURE.md` are ambiguous, log an inquiry entry in `BITACORA.md` or raise a blocker in `BLOCKERS.md` before making breaking structural assumptions.
6. **Model Selection**: Consult [MODEL_POLICY.md](MODEL_POLICY.md) to ensure appropriate AI model tiers are matched to project complexity and task risk.

---

## 5. Parallel Execution & Multi-Model Collision Prevention (Locking Protocol)

When multiple AI models or agents (e.g. Codex, Claude, Gemini, Cursor) collaborate simultaneously on the same repository, they must not step on each other or create merge collisions.

Magnetar enforces a file-based **Work Reservation & Lock Protocol** via the `locks/` directory:

```
              Agent A (e.g. Codex)                      Agent B (e.g. Claude)
                       │                                         │
        1. Check locks/ directory                 1. Check locks/ directory
                       │                                         │
        2. Create locks/task-101.lock.yml         2. Sees task-101 is locked!
           (Locks auth subsystem)                    (Picks task-102 instead)
                       │                                         │
        3. Work on feature branch                 3. Creates locks/task-102.lock.yml
                       │                             (Locks ui subsystem)
        4. Move to in_review &                    4. Work on feature branch
           rm locks/task-101.lock.yml                            │
                       │                          5. Move to in_review &
        (Auth unlocked for others)                   rm locks/task-102.lock.yml
```

### The 4 Mandatory Steps for Parallel Agent Work:

1. **Pre-Flight Lock Inspection**:
   - Before moving any task from `ready → in_progress`, inspect all active `.lock.yml` files in `locks/`.
   - If another model has already reserved the `task_id` or has locked overlapping file paths (`files_locked`), **DO NOT TOUCH THOSE FILES OR RE-CLAIM THAT TASK**. Pick an independent `ready` task.

2. **Acquiring a Work Reservation**:
   - Create `locks/<task-id>.lock.yml` using `locks/_template.lock.yml` as reference:
     ```yaml
     task_id: task-101
     agent_id: codex-backend-01
     model: gpt-4o
     status: in_progress
     branch: feature/task-101-auth
     files_locked:
       - src/auth/*
     started_at: "2026-11-12T10:45:00Z"
     summary: "Implementing OAuth2 authentication endpoints"
     ```
   - Transition the task in `PLAN.md` from `ready → in_progress`.
   - Log the start and reservation in `BITACORA.md`.

3. **Isolated Execution**:
   - Work exclusively in your designated feature branch (`feature/<task-id>-<desc>`).
   - Confine modifications strictly to the `files_locked` scope. If unexpected cross-system changes are required, check `locks/` before touching other subsystems.

4. **Releasing the Lock**:
   - Once implementation and tests are complete, move the task in `PLAN.md` to `in_review` (or `blocked` if an impediment arises).
   - Delete your reservation file: `rm locks/<task-id>.lock.yml`.
   - Record the transition in `BITACORA.md` so other agents and humans know the subsystem is free for integration.

### Stale Lock Handling:
- If a reservation in `locks/` has seen no commits, PR/MR activity, or heartbeats for > 24 hours, an agent or human coordinator may release the stale lock, noting the intervention in `BITACORA.md`.
