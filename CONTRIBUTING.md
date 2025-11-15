# Contributing Guide

> Esta es una guía para contribuir al Magnetar Canonical Project Model. Detalla el flujo de trabajo que los contribuidores deben seguir, incluyendo la necesidad de revisar los documentos de gobernanza, asegurar que las tareas existan en el plan del proyecto y seguir el proceso de Pull Request.

Thank you for helping maintain the Magnetar Canonical Project Model. Consistency is critical—follow these steps for any contribution.

## Before You Start
- Review `RULES.md`, `BRANCHING_MODEL.md`, and `WIP_GUIDELINES.md` to ensure proposed work complies with governance standards.
- Confirm the task you plan to tackle exists in `PLAN.md` and is in the `ready` state.
- Create or update the corresponding entry in `projects/_template.project.yml` or project-specific YAML files.

## Workflow
1. Create a branch using the appropriate prefix (`feature/`, `fix/`, etc.).
2. Update relevant documentation, including `BITACORA.md`, `STATUS.md`, `PLAN.md`, and `BLOCKERS.md` if applicable.
3. Run validation scripts or checks defined by the repository (e.g., linting, schema validation).
4. Ensure testing expectations from `TESTING.md` are met or note exceptions.
5. Submit a pull request referencing task IDs and summarizing changes.

## Documentation Updates
- Every PR must include a `BITACORA.md` entry with timestamp, author, and impact.
- If progress metrics change, update `STATUS.md` and adjust effort totals in `PLAN.md`.
- For new rules or deviations, amend `RULES.md` and describe rationale in `BITACORA.md`.

## Review Process
- At least one maintainer reviews each PR for adherence to canonical standards.
- Reviewers verify that cross-file consistency is maintained.
- Changes may be rejected if supporting documentation or YAML updates are missing.

## Communication
- Use the communication channels defined in the relevant project YAML for escalations.
- Major changes should be previewed in a synchronous review (meeting or huddle) before merging.

Following this guide ensures the canonical model remains trustworthy and actionable for all Magnetar teams.
