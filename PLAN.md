# Canonical Planning Model

> Este documento es el Plan del Proyecto. Describe los hitos, el backlog de tareas, las estimaciones de esfuerzo y los estados de las tareas. Sirve como una hoja de ruta para el proyecto y debe mantenerse actualizado para reflejar el estado actual del trabajo.

This plan illustrates how Magnetar projects capture milestones, tasks, estimates, and status. Replace placeholder content with project-specific details while keeping structure intact.

## Milestones Overview
| Milestone ID | Name                         | Target Date | Description                                                | Completion Criteria                             |
|--------------|------------------------------|-------------|------------------------------------------------------------|-------------------------------------------------|
| ms-01        | Project Initiation            | 2024-01-12  | Canonical artifacts created, roles assigned               | All core docs drafted, kickoff held             |
| ms-02        | Process Validation            | 2024-01-26  | Validate workflows, WIP rules, and blocker handling       | Dry run conducted, feedback incorporated        |
| ms-03        | Template Launch               | 2024-02-02  | Publish template for adoption across Magnetar projects    | Example project approved, documentation signed  |

## Task Backlog
| Task ID | Milestone | Title                                 | Owner        | Effort (pts) | Weight (%) | State        | Notes |
|---------|-----------|---------------------------------------|--------------|--------------|------------|--------------|-------|
| task-101| ms-01     | Draft canonical documentation set     | Jules        | 5            | 20         | done         | Completed via PR #4 |
| task-102| ms-01     | Define YAML project schema            | Kai          | 3            | 15         | in_review    | Awaiting approval from governance board |
| task-103| ms-01     | Publish architecture blueprint        | Mira         | 2            | 10         | done         | Linked to architecture workshop notes |
| task-201| ms-02     | Simulate blocker lifecycle            | Arun         | 3            | 10         | in_progress  | Blocked by decision on escalation path |
| task-202| ms-02     | Validate WIP limit automation         | Jules        | 2            | 10         | ready        | Script drafted, waiting for review slot |
| task-203| ms-02     | Conduct documentation audit           | Kai          | 4            | 12         | planned      | Pending after blocker simulation |
| task-301| ms-03     | Finalize example project narrative    | Mira         | 3            | 8          | in_progress  | Daily updates captured in BITACORA |
| task-302| ms-03     | Prepare adoption checklist            | Jules        | 2            | 8          | ready        | Checklist outline drafted |
| task-303| ms-03     | Announce canonical model launch       | Comms Team   | 1            | 7          | planned      | Coordinate with marketing |

## Effort Summary
- **Total effort:** 25 points
- **Completed:** 7 points (28%)
- **In progress:** 6 points (24%)
- **Remaining:** 12 points (48%)

## State Definitions
- `planned` – Task scoped but awaiting prerequisites or prioritization.
- `ready` – Task clarified with no blockers; next in line for execution.
- `in_progress` – Actively being worked on; counts toward WIP limit.
- `blocked` – Execution halted; corresponding entry exists in `BLOCKERS.md`.
- `in_review` – Work complete and pending validation or approvals.
- `done` – Accepted and reflected in `STATUS.md` metrics.

## Change Management
- Update this plan whenever tasks change state or scope.
- Reflect the same changes in the project YAML and `BITACORA.md`.
- Maintain effort and weight totals to ensure reporting accuracy.
