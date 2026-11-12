# Canonical Planning Model

> This document is the Project Plan and Backlog. It outlines milestones, the prioritized task backlog, effort estimates, ownership, and current task states. It is the single source of truth for planning and must be kept continuously in sync with actual work.

---

## Milestones Overview

| Milestone ID | Name | Target Date | Description | Completion Criteria |
| :--- | :--- | :--- | :--- | :--- |
| `ms-01` | Project Initiation | YYYY-MM-DD | Establish repository foundation and project plan | Documentation initialized, stakeholders aligned |
| `ms-02` | Core Implementation | YYYY-MM-DD | Execute primary functional requirements | Core features built, unit tests passing |
| `ms-03` | Release & Validation | YYYY-MM-DD | End-to-end verification and release delivery | Acceptance criteria met, verification signed off |

---

## Task Backlog

| Task ID | Milestone | Title | Owner | Effort (pts) | Weight (%) | State | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `task-001` | `ms-01` | Initialize repository structure and project tier | Project Lead | 2 | 20 | ready | Configure `projects/*.project.yml` |
| `task-002` | `ms-01` | Define requirements and system architecture | Architect | 3 | 30 | planned | Populate `REQUIREMENTS.md` & `ARCHITECTURE.md` |
| `task-003` | `ms-02` | Implement core feature set | Dev Team / AI | 5 | 50 | planned | Bound to acceptance criteria |

---

## Effort Summary
- **Total effort:** 10 points
- **Completed:** 0 points (0%)
- **In progress:** 0 points (0%)
- **Remaining:** 10 points (100%)

---

## Canonical Task State Definitions

Every task must occupy exactly one of these six states:
- **`planned`**: Scoped in the backlog; prerequisites or prioritization pending.
- **`ready`**: Clarified, estimated, unblocked, and ready for execution.
- **`in_progress`**: Actively being worked on; counts against the contributor's maximum WIP limit of 2.
- **`blocked`**: Progress halted by an external impediment; documented in `BLOCKERS.md`.
- **`in_review`**: Implementation complete; under peer review, testing, or CI verification.
- **`done`**: Fully verified against acceptance criteria and documented in `BITACORA.md`.

---

## Change Management Discipline
- Update this plan whenever tasks change state, effort points, or scope.
- Every state transition from `ready → in_progress`, `in_progress → in_review`, or `in_review → done` must be logged in `BITACORA.md`.
- Keep effort summaries and progress percentages synchronized with `STATUS.md`.
