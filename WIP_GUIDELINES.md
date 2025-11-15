# Work-In-Progress Guidelines

Magnetar projects optimize flow by limiting concurrent work. These guidelines are mandatory for both humans and AI contributors.

## Core Rules
1. **Maximum of two `in_progress` tasks per contributor.**
2. **Document every WIP change in `BITACORA.md`.** Include task IDs, rationale, and expected completion date.
3. **Promote focus before starting new work.** Move at least one task to `done` or `in_review` before opening another.
4. **Respect task readiness.** Only pull from the `ready` state defined in `PLAN.md`.

## Exceptions
- Request exceptions via a `WIP exception` entry in `BITACORA.md` with approver name and expiry date.
- Update `STATUS.md` to reflect temporary WIP adjustments.
- Revert to standard limits within two working days or document an extension.

## Monitoring
- Weekly audits compare `PLAN.md` task states with branch activity.
- Automated checks flag contributors exceeding limits based on commit metadata and YAML ownership fields.
- Project leads must review WIP status during standups and ensure blockers are addressed before granting new work.

Maintaining disciplined WIP levels ensures predictable delivery and highlights issues before they escalate.
