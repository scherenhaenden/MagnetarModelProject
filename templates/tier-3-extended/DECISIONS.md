# Architectural Decision Records (ADRs)

> This document records significant architectural, technical, and governance decisions made over the lifetime of the project. Each record captures the context, options considered, final decision, and consequences.

---

## 1. ADR Lifecycle & Format

Every significant decision (such as adopting a major framework, altering data models, changing deployment targets, or updating governance rules) must be recorded here.

### Status Values
- **Proposed** – Under review by architects and team members.
- **Accepted** – Approved and active.
- **Deprecated** – No longer applicable.
- **Superseded** – Replaced by a newer decision (link to the new ADR).

---

## 2. ADR Template

```markdown
### ADR-[NUM]: [Concise Title in Imperative Form]

- **Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]
- **Date:** YYYY-MM-DD
- **Deciders:** [Names / Roles]
- **Relevant Tasks:** [task-xxx]

#### Context & Problem Statement
[Describe the problem, motivations, and technical or business constraints.]

#### Considered Options
1. [Option A]: [Brief summary of pros and cons]
2. [Option B]: [Brief summary of pros and cons]

#### Decision Outcome
Chosen option: "[Option]", because [justification, trade-off explanation].

#### Consequences
- **Positive:** [What becomes easier or better]
- **Negative / Risks:** [What trade-offs or technical debt are accepted]
- **Follow-up Tasks:** [List of tasks added to PLAN.md to implement this decision]
```

---

## 3. Decision Log

| ID | Date | Title | Status | Deciders |
| :--- | :--- | :--- | :--- | :--- |
| ADR-001 | 2026-11-12 | Adopt Tiered Documentation and Agent Router Architecture | Accepted | Project Stewards |

---

### ADR-001: Adopt Tiered Documentation and Agent Router Architecture

- **Status:** Accepted
- **Date:** 2026-11-12
- **Deciders:** Magnetar Core Maintainers
- **Relevant Tasks:** task-canon-v2

#### Context & Problem Statement
The original Magnetar model enforced an identical, 12+ document footprint on all projects, resulting in excessive administrative overhead for small spikes and scripts. Furthermore, emerging AI coding agents often consumed excessive context when attempting to parse all documents simultaneously, leading to instruction dilution and drift.

#### Considered Options
1. **Status Quo**: Keep the single monolithic 12-file model for every project.
2. **Agent-Only Architecture**: Remove markdown governance and rely solely on system prompts inside agent configuration files.
3. **Tiered Canonical Model with Agent Context Router**: Retain the markdown-as-nervous-system philosophy, but introduce 3 explicit project sizing tiers (Micro, Standard, Extended) and an agent router (`AGENTS.md`) plus `MODEL_POLICY.md`.

#### Decision Outcome
Chosen option: **Option 3**, because it preserves the essential strength of the Magnetar standard (stateful, version-controlled markdown as the single source of truth) while making the framework lightweight for small projects and token-efficient for AI agents.

#### Consequences
- **Positive:** Small projects can bootstrap in seconds with 5 files; agents have clear read/write contracts; zero-dependency validation script enforces consistency.
- **Negative / Risks:** Project maintainers must select an appropriate tier during initiation (`tier: micro | standard | extended`).
- **Follow-up Tasks:** Implement `AGENTS.md`, `MODEL_POLICY.md`, `scripts/magnetar_check.py`, and updated tier templates.
