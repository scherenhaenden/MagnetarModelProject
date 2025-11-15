# Magnetar Canonical Ruleset

> Este documento es el conjunto de reglas canónicas para los proyectos de Magnetar. Codifica el estándar que cada proyecto debe seguir, incluyendo convenciones de nomenclatura, archivos requeridos, convenciones de ramificación, estados de tareas permitidos, restricciones de trabajo en progreso (WIP), ciclo de vida de los bloqueos y disciplina de documentación.

These rules codify the Magnetar standard. Every project must comply unless a formal variance is documented in `BITACORA.md` and approved by the canonical maintainers.

## Naming Conventions
- Repositories use `magnetar-<domain>-<descriptor>` (e.g., `magnetar-analytics-engine`).
- Branches follow `<type>/<short-description>` where type is one of `feature`, `fix`, `chore`, `experiment`, or `hotfix`.
- Tasks and blockers use kebab-case identifiers: `task-202`, `blocker-db-outage`.
- YAML keys remain lower_snake_case for machine readability.
- File names mirror those in this repository. Additional documents must not conflict with canonical names.

## Required Files
Every Magnetar project **must** include:
- `README.md`, `PLAN.md`, `BITACORA.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `RULES.md`, `STATUS.md`, `TESTING.md`, `BLOCKERS.md`.
- `BRANCHING_MODEL.md`, `WIP_GUIDELINES.md`, `CONTRIBUTING.md` (contribution flow), and `projects/<project>.project.yml` adhering to the template.
- Any omission requires an explicit exemption noted in `BITACORA.md` and tracked as a task.

## Branching Conventions
- `master` is the immutable release line; merges require CI success and documentation updates.
- `develop` (optional) aggregates completed features before stabilization.
- Feature branches originate from `master` or `develop` per project choice and must be rebased before merging.
- Hotfix branches start from `master` and must trigger a `STATUS.md` update upon completion.
- Each PR references the tasks it affects and includes `BITACORA.md` entries summarizing the change.

## Allowed Task States
1. `planned`
2. `ready`
3. `in_progress`
4. `in_review`
5. `blocked`
6. `done`

Transitions:
- `planned → ready` when requirements are clarified and dependencies resolved.
- `ready → in_progress` when work begins; log the start in `BITACORA.md`.
- `in_progress → blocked` only when a blocker is documented in `BLOCKERS.md`.
- `in_progress → in_review` when work is completed and under review/testing.
- `in_review → done` after acceptance criteria pass; update `STATUS.md` and `BITACORA.md`.

## Work-In-Progress Constraints
- Individuals and AI agents may hold at most **two** concurrent `in_progress` tasks.
- Exceeding the limit requires approval documented in `WIP_GUIDELINES.md` and `BITACORA.md`.
- When a task is blocked, it no longer counts toward the WIP limit but must be replaced with a `ready` item only after documenting mitigation steps.

## Blocker Lifecycle
1. **Discovery** – Log in `BLOCKERS.md` with unique ID, description, severity, owner, and timestamp.
2. **Assessment** – Update `STATUS.md` risks and note mitigation ideas in `BITACORA.md`.
3. **Escalation** – If unresolved within one working day, escalate through the communication path specified in the project YAML.
4. **Resolution** – Document fix steps in `BITACORA.md`, update blocker status to `resolved`, and adjust related tasks.
5. **Retrospective** – Capture lessons learned in the next planning cycle or in `ARCHITECTURE.md` if structural changes were required.

## Documentation Discipline
- Every state change, decision, or exception must be chronologically recorded in `BITACORA.md`.
- `STATUS.md` is updated at least once per working day or after each PR merge.
- `PLAN.md` is the source of truth for current milestones and task assignments.
- Testing status updates must appear in both `TESTING.md` and relevant task entries.

## AI Agent Responsibilities
- Parse `projects/*.project.yml` before acting to understand priorities and constraints.
- Refrain from opening PRs without confirming the task state is `in_review`.
- When uncertain, document assumptions in `BITACORA.md` and tag them for human confirmation.
- Reject requests that violate WIP limits, branching rules, or documentation requirements unless instructed by maintainers with a logged exception.

## Enforcing Compliance
- CI should validate presence and structure of required files.
- Periodic audits compare `PLAN.md` with `STATUS.md` progress percentages.
- Repeated non-compliance must be escalated and tracked as high-impact blockers.

By adhering to these rules, Magnetar teams maintain consistent, auditable workflows that scale across projects and collaborators.
