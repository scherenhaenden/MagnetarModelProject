# Architecture Blueprint

The Magnetar Canonical Project Model defines architecture as the structure of governance, planning artifacts, and execution workflows that any project must adopt. Although the repository contains no runnable code, its architectural guidance scales from lightweight initiatives to complex multi-team programs.

## Conceptual Diagram
```
             +------------------------------+
             | Vision & Strategy            |
             | (README, REQUIREMENTS)       |
             +---------------+--------------+
                             |
                             v
+----------------------------+----------------------------+
| Planning Backbone                                          |
| (PLAN, projects/*.project.yml, ARCHITECTURE)               |
+----------------------------+----------------------------+
                             |
                             v
+----------------------------+----------------------------+
| Execution & Governance                                     |
| (BITACORA, STATUS, BLOCKERS, TESTING, RULES, WIP)          |
+----------------------------+----------------------------+
                             |
                             v
             +------------------------------+
             | Feedback & Continuous Learn  |
             | (BRANCHING_MODEL, examples/) |
             +------------------------------+
```

## Standard Components
- **Vision Layer** – Captures purpose, constraints, and success measures.
- **Planning Backbone** – Provides structured backlog, milestones, dependencies, and architecture expectations.
- **Execution Layer** – Tracks progress, blockers, test outcomes, and compliance with operating rules.
- **Feedback Loop** – Feeds lessons learned and example updates back into strategy and planning.

## Recommended Repository Layout for New Projects
```
project-root/
  README.md
  REQUIREMENTS.md
  ARCHITECTURE.md
  PLAN.md
  BITACORA.md
  STATUS.md
  TESTING.md
  BLOCKERS.md
  RULES.md
  BRANCHING_MODEL.md
  WIP_GUIDELINES.md
  CONTRIBUTING.md
  projects/
    <project-name>.project.yml
  docs/                # optional deeper design notes
  src/                 # application code (if applicable)
  tests/               # automated tests
```

## Architecture for Small vs. Large Projects
- **Small Projects**
  - May collapse `docs/` and `ARCHITECTURE.md` into a single design narrative.
  - Typically have one active project YAML and a concise set of milestones.
  - Use lightweight CI but still follow blocker and testing documentation.
- **Large Projects**
  - Maintain multiple project YAML files (per stream) under `projects/`.
  - Extend `ARCHITECTURE.md` with component diagrams, integration contracts, and dependency maps.
  - Require explicit interface definitions and may include subsystem-specific WIP rules.

## Example Dependencies
- **Process Dependencies** – Pull requests depend on updated `BITACORA.md` entries and passing tests declared in `TESTING.md`.
- **Information Dependencies** – Task states in `PLAN.md` must match `projects/*.project.yml` entries.
- **Organizational Dependencies** – Blocker resolution requires escalation paths defined in the project YAML `communication` section.

## Example Workflow Flow
1. Requirements changes land in `REQUIREMENTS.md` and trigger task updates in `PLAN.md`.
2. Contributors branch according to `BRANCHING_MODEL.md`, update files, and open PRs.
3. Upon PR completion, `BITACORA.md`, `STATUS.md`, and the YAML file are updated to reflect new progress percentages and risk posture.
4. Testing outcomes are recorded in `TESTING.md` and cross-referenced in relevant tasks.
5. Lessons learned feed into architecture adjustments and the example project for future guidance.

This blueprint ensures every Magnetar project has a shared skeleton, regardless of technical stack or team size.
