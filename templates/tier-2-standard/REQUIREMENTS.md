# Requirements Specification

> This document details the functional and non-functional requirements for the Magnetar Canonical Project Model. It defines the standards for the tiered documentation set, the YAML schema, agent interaction protocols, validation tooling, and example implementations.

---

## Functional Requirements

### 1. Tiered Canonical Documentation Set
- The repository must define three distinct project sizing tiers (`micro`, `standard`, and `extended`).
- Each tier must have an explicitly specified set of mandatory and optional files.
- Each document must include predefined sections, definitions, and operational guidelines that downstream projects can adopt directly.

### 2. Machine-Readable Project Schema Template
- Provide a machine-readable YAML template (`projects/_template.project.yml`) with descriptive comments for every field.
- The schema must include project metadata, declared tier (`tier: micro | standard | extended`), milestones, task definitions, risk registers, and communication channels.

### 3. Agent Routing & Context Optimization
- Provide a dedicated AI Agent context router (`AGENTS.md`) mapping developer activities (planning, coding, blockers, testing, review) to specific read/write markdown documents.
- Provide a model tiering framework (`MODEL_POLICY.md`) matching AI parameter tiers (Fast, Balanced, Deep Reasoning) to project scale and task complexity.
- Provide optional, platform-agnostic tool bridge files (e.g. `CLAUDE.md`, `GEMINI.md`) pointing to `AGENTS.md`.

### 4. Automated Compliance Tooling
- Provide a zero-dependency CLI script (`scripts/magnetar_check.py`) capable of auditing any repository for canon compliance according to its declared tier.
- Provide sample CI/CD workflows and git hook configurations (`ci/`) to enforce canon compliance across any environment (GitHub Actions, GitLab CI, pre-commit, etc.).

### 5. Reference Implementations & Ready-to-Use Templates
- Deliver ready-to-copy template folders for each project tier under `templates/`.
- Maintain fully populated, realistic reference examples under `examples/` demonstrating correct usage in production.

---

## Non-Functional Requirements
- **Clarity & Directiveness** – Language must be unambiguous and directive; each rule links to its canonical document.
- **Consistency** – Task states (`planned`, `ready`, `in_progress`, `in_review`, `blocked`, `done`), identifier conventions, and section titles must remain strictly identical across all files.
- **Traceability** – Every code commit and PR must map to a `task-<id>` in `PLAN.md` and an entry in `BITACORA.md`.
- **Zero-Dependency Tooling** – The validator script must run on vanilla Python 3 without requiring external package installations (`pip`).
- **Token Efficiency** – AI agent routing must prevent context window saturation by discouraging blind multi-file ingestion.

---

## Acceptance Criteria (Gherkin)

```gherkin
Feature: Magnetar Tiered Canonical Model Compliance

  Scenario: Bootstrapping a new project by tier
    Given a developer or agent initiates a new project
    When they select a project tier (micro, standard, or extended)
    Then they find a corresponding template directory under templates/
    And the template contains exactly the required documentation set for that tier

  Scenario: AI Agent context routing
    Given an AI coding agent begins working in a Magnetar repository
    When the agent consults AGENTS.md
    Then it identifies the exact files to read and update for its specific task
    And it does not need to ingest irrelevant documentation into its context window

  Scenario: Automated validation via magnetar_check.py
    Given a project repository with a declared tier
    When python scripts/magnetar_check.py is executed
    Then it validates file presence, section headers, task states, and WIP limits
    And it returns exit code 0 when compliant or non-zero with actionable errors when failing
```
