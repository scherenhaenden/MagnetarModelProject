# Magnetar Canonical Project Model

> This is the main README file for the Magnetar Canonical Project Model. It provides an overview of the repository's purpose, contents, and usage. It serves as the starting point for anyone interacting with the project, explaining how to clone the model, replicate the documentation set, and follow the governance rules.

The Magnetar Canonical Project Model is the definitive reference implementation for every Magnetar initiative. It exists to remove ambiguity, align humans and AI collaborators, and guarantee that each future repository starts from the same shared understanding of scope, process, and documentation. This project is not an application—its value lies in the structure and guidance it provides.

## Purpose
- Establish a universal template covering documentation, planning, execution, and governance.
- Describe the lifecycle expectations for Magnetar tasks, milestones, blockers, and deliverables.
- Provide a complete YAML schema that downstream projects can adopt without interpretation gaps.
- Offer an end-to-end, fully populated example that demonstrates the standard in action.

## How to Use This Repository
1. **Clone the canonical model** when creating a new Magnetar project.
2. **Copy the `projects/_template.project.yml` file** into your repository and fill it out with project-specific values.
3. **Replicate the documentation set** listed below, retaining file names and required sections.
4. **Follow the WIP, branching, blocker, and testing rules** verbatim unless an exception is formally approved.
5. **Keep the example project** nearby to resolve questions about expected tone, depth, or formatting.

## Project Contents
This repository is intentionally documentation-first. Each file has a specific role within the model.

| File              | Purpose                                         |
|-------------------|-------------------------------------------------|
| PLAN.md           | Project tasks & milestones                      |
| BITACORA.md       | Chronological logbook                           |
| REQUIREMENTS.md   | Functional & non-functional specs               |
| ARCHITECTURE.md   | System/module structure                         |
| RULES.md          | Naming & workflow standards                     |
| STATUS.md         | Health summary & progress stats                 |
| TESTING.md        | Test coverage & reporting rules                 |
| BLOCKERS.md       | Documented blockers & escalation paths          |

Additional governance references include `BRANCHING_MODEL.md` for Git flow rules and `WIP_GUIDELINES.md` for work-in-progress policies.

## Progress Model Overview
Magnetar projects track progress through milestones, tasks, and state transitions. Tasks advance through `planned → in_progress → in_review → done`, with blockers and risks captured transparently in `BLOCKERS.md` and `STATUS.md`. Every change in task state must be recorded in `BITACORA.md`, ensuring that the written history aligns with repository state and PR activity.

## YAML Project Schema
The `projects/_template.project.yml` file specifies the canonical machine-readable schema. It includes metadata, stakeholders, milestones, task definitions, risk registers, test commitments, and reporting hooks. Inline comments explain each field, enabling AIs to parse the file reliably and humans to adapt it without breaking compatibility.

## Guidance for AI Collaborators
AI agents must:
- Parse the YAML template to understand priorities, timelines, and ownership.
- Use `PLAN.md` and `STATUS.md` to determine current focus and constraints.
- Respect `RULES.md`, `WIP_GUIDELINES.md`, and `BRANCHING_MODEL.md` before proposing or executing work.
- Update `BITACORA.md` whenever they complete, reprioritize, or discover work.

## Architecture Diagram Overview
```
+---------------------------+
| Governance & Standards    |
| (RULES, WIP, BRANCHING)   |
+------------+--------------+
             |
             v
+---------------------------+
| Planning Layer            |
| (PLAN, REQUIREMENTS)      |
+------------+--------------+
             |
             v
+---------------------------+
| Execution & Tracking      |
| (BITACORA, STATUS,        |
|  BLOCKERS, TESTING)       |
+------------+--------------+
             |
             v
+---------------------------+
| Reference Implementations |
| (projects/, examples/)    |
+---------------------------+
```
The diagram expresses how standards inform planning, which then feeds execution artifacts and concrete examples. Every new project should reflect this flow.

## Applying This Template to a New Project
1. Copy the repository structure into the new project root.
2. Replace placeholder content with project-specific details while preserving headings and semantics.
3. Instantiate a project YAML file from `projects/_template.project.yml` and validate it against automated checks.
4. Establish your initial milestones and log the starting state in `PLAN.md`, `STATUS.md`, and `BITACORA.md`.
5. Enforce WIP limits, testing expectations, and branching conventions from day one.

## Validating Canon Compliance
To verify that a project follows the Magnetar canon:
- Confirm that all required files exist with the mandated sections and headings.
- Ensure the project YAML matches the schema fields and naming conventions.
- Review `BITACORA.md` for continuous, chronological updates aligned with Git history.
- Check that active branches obey the rules described in `BRANCHING_MODEL.md` and WIP counts respect `WIP_GUIDELINES.md`.
- Verify that testing commitments and blocker processes match the expectations in `TESTING.md` and `BLOCKERS.md`.

By adhering to this canonical model, every Magnetar project speaks a shared language, enabling seamless collaboration across teams and intelligent agents.
