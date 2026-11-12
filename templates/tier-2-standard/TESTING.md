# Testing Standards

> This document defines the Testing Standards for Magnetar projects. It outlines the types of tests (unit, integration, documentation, acceptance), coverage expectations, reporting protocols, and how to declare untested areas.

Magnetar projects must define and execute rigorous testing strategies appropriate to their technology stack and project tier. Tailor the following expectations to your project while preserving their intent.

---

## Test Types
- **Unit Tests** – Validate the smallest meaningful components (functions, classes, scripts). Mandatory for any executable logic.
- **Integration Tests** – Verify interactions between modules, services, databases, or third-party APIs.
- **Documentation & Canon Tests** – Ensure required files exist, conform to the project's tier, and follow schema rules via `python scripts/magnetar_check.py`.
- **Acceptance Tests** – End-to-end user flow validations confirming acceptance criteria in `REQUIREMENTS.md`.

---

## Coverage Expectations
- **Tier 1 (Micro)**: Basic smoke tests and documentation linting.
- **Tier 2 (Standard)**: Minimum 80% coverage on core business logic; 100% compliance with canon linting.
- **Tier 3 (Extended)**: Strict coverage thresholds (>= 85%), automated regression test suites, security scans, and mandatory CI gates.

---

## Reporting Protocol
- Summarize the latest test run in this document, recording date, execution command, outcome, and coverage percentage.
- Update `STATUS.md` with the `tested` percentage and note any untested areas.
- Link failing tests immediately to an active task in `PLAN.md` or a blocker in `BLOCKERS.md`.

---

## Declaring Untested Areas
- Format: `untested: <scope> — <reason> — <owner> — <planned date>`.
- Untested scopes must not linger longer than one milestone without formal stakeholder approval.

---

## Test Run Log Template

```yaml
last_run:
  date: YYYY-MM-DD
  command: pytest / npm test / scripts/magnetar_check.py
  outcome: passed # passed | failed
  coverage: 0%
untested: []
```
