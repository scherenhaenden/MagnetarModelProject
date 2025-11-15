# Branching Model

The Magnetar canonical branching strategy balances stability with rapid iteration. All repositories must adhere to these rules unless an exception is documented in `BITACORA.md` and approved by maintainers.

## Core Branches
- **master** – Stable, production-ready state of the project model. Only reviewed and tested work is merged here. Each merge requires updates to `STATUS.md` and confirmation that `BLOCKERS.md` is current.
- **develop** *(optional)* – Integration branch used when multiple features need coordination before reaching `master`. If used, it must be updated daily and never diverge more than one release cycle from `master`.

## Working Branches
- **feature/** – Adds new capabilities or documentation sections. Originates from `master` or `develop`. Must reference at least one task in `PLAN.md`.
- **fix/** – Addresses defects or clarifies ambiguities. Includes regression testing notes in `TESTING.md`.
- **chore/** – Tooling, automation, or dependency updates. Requires a brief rationale in `BITACORA.md`.
- **hotfix/** – Emergency corrections applied directly to `master`. Post-merge, `develop` must be fast-forwarded.
- **experiment/** – Time-boxed explorations. Cannot merge without conversion to a feature/fix branch and compliance with documentation standards.

## Pull Request Expectations
1. Rebase onto target branch before requesting review to maintain a linear history.
2. Update `BITACORA.md` with a summary of changes and impacted tasks.
3. Refresh `STATUS.md` metrics if progress, testing, or risk posture changes.
4. Confirm related blockers are updated or resolved in `BLOCKERS.md`.
5. Reference the relevant task IDs from `PLAN.md` in the PR description.

## Branch Lifecycle
- Create a branch when moving a task to `in_progress`.
- Keep branches short-lived; close or merge within five working days.
- Delete remote branches after merge to reduce clutter.

Adhering to this branching model ensures traceability between work items, documentation, and code, providing a repeatable governance pattern across all Magnetar projects.
