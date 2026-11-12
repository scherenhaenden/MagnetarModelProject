# Cache Pruner Plan & Backlog

## Milestones
| Milestone ID | Name | Target Date | Description | Completion Criteria |
| :--- | :--- | :--- | :--- | :--- |
| `ms-01` | MVP Release | 2026-11-20 | Working CLI tool with dry-run support | Tests pass, dry-run works |

## Tasks
| Task ID | Milestone | Title | Owner | Effort (pts) | Weight (%) | State | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `cp-101` | `ms-01` | Implement directory scanner | Alex | 2 | 40 | done | Scans .cache and build dirs |
| `cp-102` | `ms-01` | Add dry-run deletion flag | Alex | 1 | 30 | in_progress | Handling safety prompt |
| `cp-103` | `ms-01` | Write CLI unit tests | Maya | 1 | 30 | ready | Pytest suite |

## Effort Summary
- **Total:** 4 pts | **Completed:** 2 (50%) | **In Progress:** 1 (25%) | **Remaining:** 1 (25%)
