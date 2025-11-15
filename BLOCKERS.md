# Blocker Register

> Este archivo es el Registro de Bloqueos del proyecto. Se utiliza para documentar todos los impedimentos que obstaculizan el progreso del proyecto. Cada entrada debe incluir una descripción clara del bloqueo, su impacto, el propietario, los pasos de mitigación y la ruta de escalada.

Document blockers immediately to maintain transparency and drive resolution. Each entry should map back to tasks in `PLAN.md` and be referenced in `BITACORA.md` updates.

## Template
```
id: blocker_001
title: "Dependency unavailable"
impact: high
status: open
owner: <name>
discovered: <YYYY-MM-DD>
description: |
  <Explain the issue, affected tasks, and immediate impact.>
mitigation_steps:
  - <Step 1>
  - <Step 2>
escalation_path: <Channel or person>
next_review: <YYYY-MM-DD>
notes: |
  <Additional context or updates>
```

## Active Blockers
- id: blocker_002
  title: "Escalation path pending approval"
  impact: medium
  status: open
  owner: Arun
  discovered: 2024-01-10
  description: |
    Awaiting confirmation from governance board on official blocker escalation contacts.
    Tasks task-201 and task-203 cannot proceed without this alignment.
  mitigation_steps:
    - Draft interim escalation flow and share for feedback.
    - Schedule governance sync on 2024-01-11.
  escalation_path: pending final decision
  next_review: 2024-01-12
  notes: |
    Temporary workaround allows logging blockers but not formal escalation.

## Resolved Blockers
- id: blocker_001
  title: "Schema comment coverage incomplete"
  impact: low
  status: resolved
  owner: Kai
  discovered: 2024-01-09
  resolved: 2024-01-10
  description: |
    Initial YAML template lacked explanatory comments for automation fields.
  mitigation_steps:
    - Added inline comments to template.
    - Updated REQUIREMENTS.md acceptance criteria.
  notes: |
    Closure recorded in BITACORA on 2024-01-10 16:40.
