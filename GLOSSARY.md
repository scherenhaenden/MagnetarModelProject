# Magnetar Project Glossary

> This document establishes a shared lexicon of terms, concepts, and identifiers used across all Magnetar projects, ensuring unequivocal alignment between human engineers and AI collaborators.

---

## Core Magnetar Concepts

| Term | Definition |
| :--- | :--- |
| **Magnetar Canon** | The official, version-controlled set of standards, documentation schemas, branching policies, and governance rules defined in `MagnetarModelProject`. |
| **Bitácora** | (From the nautical *bítacora* / logbook) The permanent, append-only chronological journal (`BITACORA.md`) recording all state transitions, key technical decisions, blocker resolutions, and exceptions. |
| **Blocker** | Any impediment that completely halts progress on an `in_progress` task. Must be logged in `BLOCKERS.md` and triggers an immediate status transition to `blocked`. |
| **WIP Limit** | Work-In-Progress constraint limiting each contributor (human or AI agent) to a maximum of **two** active concurrent tasks in the `in_progress` state. |
| **Task State** | One of the 6 canonical phases of work: `planned`, `ready`, `in_progress`, `in_review`, `blocked`, or `done`. |
| **Milestone** | A major checkpoint grouping related tasks with defined acceptance criteria and target delivery dates. |
| **ADR (Architectural Decision Record)** | A structured document (`DECISIONS.md`) capturing the context, options, decision, and consequences of a significant architectural choice. |
| **Agent Router** | The navigational contract defined in `AGENTS.md` guiding AI agents on which files to read and write for any given development action. |
| **Task Lock / Reservation** | An ephemeral YAML file in `locks/<task-id>.lock.yml` declaring that an AI model or contributor is actively working on a task and specific file scopes, preventing parallel collisions. |

---

## Project Sizing Tiers

| Tier Identifier | Label | Scope | Required Documentation Footprint |
| :--- | :--- | :--- | :--- |
| `micro` | **Tier 1 (Micro)** | Spikes, prototypes, single-purpose scripts, utilities (< 1-2 weeks). | `README.md`, `AGENTS.md`, `PLAN.md`, `STATUS.md`, `RULES.md` |
| `standard` | **Tier 2 (Standard)** | Standalone applications, backend services, client apps, libraries. | Full standard set: Tier 1 + `REQUIREMENTS.md`, `ARCHITECTURE.md`, `BITACORA.md`, `TESTING.md`, `BLOCKERS.md`, `BRANCHING_MODEL.md`, `WIP_GUIDELINES.md`, `project.yml` |
| `extended` | **Tier 3 (Extended)** | Multi-service distributed systems, monorepos, enterprise, high-compliance. | Tier 2 + `DECISIONS.md`, `GLOSSARY.md`, `SECURITY.md`, `CHANGELOG.md`, `MODEL_POLICY.md`, automated CI verification. |

---

## Technical & Identifier Conventions

| Identifier Pattern | Format | Example | Context |
| :--- | :--- | :--- | :--- |
| **Repository Name** | `magnetar-<domain>-<descriptor>` | `magnetar-core-auth` | Git repositories (GitLab, GitHub, Bitbucket, Gitea, etc.) |
| **Branch Name** | `<type>/<kebab-description>` | `feature/user-session-cache` | Git branches (`feature`, `fix`, `chore`, `experiment`, `hotfix`) |
| **Task ID** | `task-<number>` or `task-<slug>` | `task-102` | `PLAN.md`, PR/MR descriptions, commit messages |
| **Blocker ID** | `blocker-<number>` or `blocker-<slug>` | `blocker-001` | `BLOCKERS.md`, `STATUS.md` |
| **Milestone ID** | `ms-<number>` | `ms-01` | `PLAN.md`, `project.yml` |
| **ADR ID** | `ADR-<number>` | `ADR-001` | `DECISIONS.md` |
| **YAML Keys** | `lower_snake_case` | `overall_progress`, `standup_channel` | `projects/*.project.yml` |
