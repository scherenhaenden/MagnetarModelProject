# Magnetar Canonical Project Model

> The definitive reference implementation and governance blueprint for all Magnetar initiatives. It establishes a documentation-driven, spec-first standard that aligns human engineers and AI collaborators across projects of any scale.

The Magnetar Canonical Project Model is the reference standard for every Magnetar repository. It eliminates ambiguity, aligns human engineers and AI collaborators, and guarantees that each repository starts from a shared understanding of scope, process, architecture, and governance.

---

## Purpose
- Establish a universal, tier-aware framework covering documentation, planning, execution, and governance.
- Provide a persistent, Markdown-driven "nervous system" that grounds AI coding agents and prevents context drift.
- Offer distinct project tiers (`micro`, `standard`, `extended`) so documentation overhead scales with project scope.
- Provide machine-readable YAML schemas and zero-dependency validation tooling to verify compliance in CI.
- Maintain complete, end-to-end reference implementations for seamless onboarding.

---

## Project Sizing Tiers

Magnetar recognizes that one size does not fit all. Projects declare their tier in `projects/*.project.yml`:

| Tier | Profile Name | Target Scope | Required Core Files |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **Micro** | Single-file scripts, spikes, quick prototypes (< 1-2 weeks) | `README.md`, `AGENTS.md`, `PLAN.md`, `STATUS.md`, `RULES.md` |
| **Tier 2** | **Standard** | Standalone applications, services, libraries, tools (1-3 months) | Full standard set: Tier 1 + `REQUIREMENTS.md`, `ARCHITECTURE.md`, `BITACORA.md`, `TESTING.md`, `BLOCKERS.md`, `BRANCHING_MODEL.md`, `WIP_GUIDELINES.md`, `project.yml` |
| **Tier 3** | **Extended** | Multi-service systems, monorepos, enterprise, high-compliance | Tier 2 + `DECISIONS.md` (ADRs), `GLOSSARY.md`, `SECURITY.md`, `CHANGELOG.md`, `MODEL_POLICY.md`, automated CI verification |

---

## Canonical Document Map

Each file in the Magnetar model serves a distinct, non-overlapping role:

| File | Purpose | Tier |
| :--- | :--- | :--- |
| **`AGENTS.md`** | AI context router & operational navigation protocol | All tiers |
| **`MODEL_POLICY.md`**| AI model tiering (fast vs. balanced vs. deep reasoning) | Tier 3 (rec. for all) |
| **`README.md`** | Project introduction, quickstart, and structural index | All tiers |
| **`RULES.md`** | Non-negotiable naming, task state, and workflow rules | All tiers |
| **`PLAN.md`** | Roadmap, milestones, effort points, and task backlog | All tiers |
| **`STATUS.md`** | Real-time health summary, metrics dashboard, and risks | All tiers |
| **`REQUIREMENTS.md`**| Functional, non-functional, and acceptance specifications | Tier 2 & 3 |
| **`ARCHITECTURE.md`**| Structural system topology, data flow, and module boundaries | Tier 2 & 3 |
| **`BITACORA.md`** | Immutable, chronological logbook of decisions and transitions | Tier 2 & 3 |
| **`BLOCKERS.md`** | Impediment register, owner assignments, and escalation paths | Tier 2 & 3 |
| **`TESTING.md`** | Test coverage commitments, reporting, and untested scope | Tier 2 & 3 |
| **`BRANCHING_MODEL.md`**| Git branch lifecycle conventions and PR requirements | Tier 2 & 3 |
| **`WIP_GUIDELINES.md`**| Work-in-progress limit policies (max 2 active tasks) | Tier 2 & 3 |
| **`DECISIONS.md`** | Architecture Decision Records (ADRs) | Tier 3 |
| **`GLOSSARY.md`** | Domain terms, taxonomy, and identifier conventions | Tier 3 |

Tool bridges (e.g. `CLAUDE.md`, `GEMINI.md`) point directly to `AGENTS.md` to maintain a single source of truth across diverse agent environments.

---

## Progress Model & Task State Machine

Magnetar projects track work through milestones and discrete task state transitions:

```
   [planned] ───> [ready] ───> [in_progress] ───> [in_review] ───> [done]
                                   │     ▲
                                   ▼     │
                                 [blocked]
```

- **`planned`**: Scoped in backlog; prerequisites or prioritization pending.
- **`ready`**: Acceptance criteria clear, effort estimated, dependencies met. Ready to pull.
- **`in_progress`**: Actively being worked on (strictly maximum 2 concurrent tasks per contributor).
- **`blocked`**: Progress halted; blocker details recorded in `BLOCKERS.md`.
- **`in_review`**: Work completed; under peer review, testing, or CI verification.
- **`done`**: Verified against acceptance criteria and recorded in `BITACORA.md`.

---

## Guidance for AI Collaborators

AI coding agents must adhere to the following protocol:
1. **Consult `AGENTS.md` first**: Identify your task and read only the files mapped to your current activity.
2. **Review `MODEL_POLICY.md`**: Ensure your model's reasoning tier matches the cognitive requirements of the task.
3. **Never vibe-code**: Ensure an active task ID exists in `in_progress` before modifying codebase files.
4. **Log every state change in `BITACORA.md`**: Document what was done, why, and what was tested.
5. **Respect WIP constraints**: Never hold more than two concurrent `in_progress` tasks.

---

## Validating Canon Compliance

Magnetar includes an automated, zero-dependency validation script:

```bash
# Validate the current repository against its declared tier
python scripts/magnetar_check.py

# Validate explicitly for a specific tier
python scripts/magnetar_check.py --tier standard
```

The validator verifies:
- All required files for the declared tier exist.
- Required markdown headers and sections are intact.
- Task states in `PLAN.md` obey the canonical 6-state machine.
- WIP limits (max 2 in-progress tasks per owner) are respected.
- Project YAML schema compliance.

---

## Applying This Template to a New Project

1. **Select your tier**: Choose Tier 1 (Micro), Tier 2 (Standard), or Tier 3 (Extended).
2. **Copy the corresponding template folder**:
   - `templates/tier-1-micro/`
   - `templates/tier-2-standard/`
   - `templates/tier-3-extended/`
3. **Fill in project values**: Populate metadata, milestones, and requirements with project-specific details.
4. **Run `python scripts/magnetar_check.py`**: Confirm that all canonical checks pass.
5. **Begin execution**: Move initial tasks to `ready` and log the project kickoff in `BITACORA.md`.
