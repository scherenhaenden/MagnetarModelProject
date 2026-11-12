# Magnetar Canonical Ruleset

> This document is the canonical ruleset for Magnetar projects. It codifies the standards that every project must follow, including naming conventions, required files per project tier, branching conventions, allowed task states, work-in-progress (WIP) constraints, the blocker lifecycle, and documentation discipline.

These rules codify the Magnetar standard. Every project must comply with the requirements of its declared project tier unless a formal variance is documented in `BITACORA.md` (or in `PLAN.md` for Micro projects) and approved by project stewards.

---

## 1. Naming Conventions
- **Repositories**: `magnetar-<domain>-<descriptor>` (e.g., `magnetar-analytics-engine`).
- **Branches**: `<type>/<short-description>` where type is one of `feature`, `fix`, `chore`, `experiment`, or `hotfix`.
- **Tasks and Blockers**: kebab-case identifiers (`task-101`, `blocker-db-outage`).
- **YAML Keys**: `lower_snake_case` for deterministic machine readability.
- **File Names**: Must strictly match the canonical filenames. Additional documents must not conflict with canonical names.

---

## 2. Project Sizing Tiers & Required Files

Magnetar projects declare their tier in `projects/*.project.yml` via the `tier:` property (`micro`, `standard`, or `extended`).

| Tier | Primary Use Case | Required Files | Optional / Recommended |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Micro)** | Spikes, prototypes, single-purpose scripts, utilities (< 1-2 weeks) | `README.md`, `AGENTS.md`, `PLAN.md`, `STATUS.md`, `RULES.md` | `BITACORA.md`, `TESTING.md`, `project.yml` |
| **Tier 2 (Standard)** | Standalone applications, backend services, libraries, tools (1-3 months) | Tier 1 + `REQUIREMENTS.md`, `ARCHITECTURE.md`, `BITACORA.md`, `TESTING.md`, `BLOCKERS.md`, `BRANCHING_MODEL.md`, `WIP_GUIDELINES.md`, `projects/<project>.project.yml` | `CONTRIBUTING.md`, `DECISIONS.md`, `GLOSSARY.md` |
| **Tier 3 (Extended)** | Multi-service distributed systems, monorepos, enterprise, regulated | Tier 2 + `DECISIONS.md` (ADRs), `GLOSSARY.md`, `SECURITY.md`, `CHANGELOG.md`, `MODEL_POLICY.md`, automated CI verification (`magnetar_check.py`) | Domain specs in `docs/specs/` |

> Any omission of a required file for the project's tier requires an explicit exemption noted in `BITACORA.md` and tracked as a task.

---

## 3. Branching Conventions
- `master` (or `main`) is the immutable release line; merges require passing automated tests/linting and up-to-date documentation.
- `develop` (optional) aggregates completed features before stabilization.
- Feature branches originate from `master` or `develop` per project choice and must be rebased before merging.
- Hotfix branches start from `master` and must trigger a `STATUS.md` update upon completion.
- Each Pull Request / Merge Request (PR/MR) must reference the tasks it affects and include `BITACORA.md` entries summarizing the change.

---

## 4. Allowed Task States
A task must always be in exactly one of the following **six** canonical states:
1. `planned` – Scoped and placed in backlog; prerequisites or prioritization pending.
2. `ready` – Clarified, estimated, unblocked, and ready for immediate pull.
3. `in_progress` – Actively being executed; counts directly against the contributor's WIP limit.
4. `in_review` – Execution complete; under testing, CI verification, or peer review.
5. `blocked` – Halting impediment encountered; linked to an entry in `BLOCKERS.md`.
6. `done` – Fully verified against acceptance criteria and documented in `BITACORA.md`.

### Valid State Transitions
```
   [planned] ───> [ready] ───> [in_progress] ───> [in_review] ───> [done]
                                   │     ▲
                                   ▼     │
                                 [blocked]
```
- `planned → ready`: when requirements are clarified, acceptance criteria defined, and dependencies resolved.
- `ready → in_progress`: when work begins; log the transition in `BITACORA.md`.
- `in_progress → blocked`: only when a blocker is documented in `BLOCKERS.md`.
- `blocked → in_progress`: when the blocker is resolved and resolution recorded in `BITACORA.md`.
- `in_progress → in_review`: when implementation is complete and undergoing review or test execution.
- `in_review → done`: when all acceptance criteria and test commitments in `TESTING.md` pass.

---

## 5. Work-In-Progress (WIP) Constraints
- Individual contributors and AI agents may hold at most **two** concurrent `in_progress` tasks.
- Exceeding the limit requires approval documented in `WIP_GUIDELINES.md` and logged in `BITACORA.md`.
- When a task is blocked, it no longer counts toward the active WIP limit, but must be replaced with a `ready` item only after documenting mitigation steps in `BLOCKERS.md`.

---

## 6. Blocker Lifecycle
1. **Discovery** – Log immediately in `BLOCKERS.md` with a unique ID, impact level, owner, and timestamp. Transition task in `PLAN.md` to `blocked`.
2. **Assessment** – Update risks in `STATUS.md` and note mitigation ideas in `BITACORA.md`.
3. **Escalation** – If unresolved within one working day, escalate through the communication contact specified in the project YAML.
4. **Resolution** – Document resolution steps in `BITACORA.md`, update blocker status to `resolved` in `BLOCKERS.md`, and transition task back to `in_progress`.
5. **Retrospective** – Capture lessons learned in `DECISIONS.md` or `ARCHITECTURE.md` if systemic adjustments were required.

---

## 7. Documentation Discipline
- Every state change, key design decision, or exception must be chronologically recorded in `BITACORA.md`.
- `STATUS.md` reflects current sprint/milestone metrics, remaining tasks, and active blockers.
- `PLAN.md` is the single source of truth for milestones, effort points, and task states.
- Testing status updates must appear in both `TESTING.md` and relevant task entries.

---

## 8. AI Agent Governance
- Agents must consult [AGENTS.md](AGENTS.md) as the authoritative context router before inspecting or modifying project files.
- Agents must consult [MODEL_POLICY.md](MODEL_POLICY.md) to ensure their assigned model aligns with task cognitive demands.
- Agents are strictly prohibited from altering code without an assigned `task-<id>` in the `in_progress` state.
- Agents must update `BITACORA.md` upon transitioning any task or completing deliverable milestones.

---

## 9. Enforcing Compliance
- Run the zero-dependency validation script:
  ```bash
  python scripts/magnetar_check.py
  ```
- Automated CI/CD pipelines or local git pre-commit hooks (see samples in `ci/`) validate the presence of required files, valid task states, and WIP constraints on pull and merge requests.
