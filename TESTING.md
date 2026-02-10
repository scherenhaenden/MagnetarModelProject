# Testing Standards

> This document defines the Testing Standards for Magnetar projects. Although the repository is documentation-centric, it outlines the types of tests (unit, integration, documentation, acceptance), coverage expectations, reporting, and how to declare untested areas.

Although this repository is documentation-focused, Magnetar projects must define and execute rigorous testing strategies. Tailor the following expectations to your project while preserving their intent.

## Test Types
- **Unit Tests** – Validate the smallest meaningful components (functions, classes, scripts). Required for any executable logic.
- **Integration Tests** – Verify interactions between modules, services, or workflows. For documentation-heavy projects, treat cross-file validation scripts as integration tests.
- **Documentation Tests** – Ensure required files exist, contain expected sections, and follow schema rules. Implement automated linting or schema validation scripts where possible.
- **Acceptance Tests** – Human or automated end-to-end checks confirming requirements and user flows.

## Coverage Expectations
- Minimum 80% coverage for executable codebases; for documentation projects, target 100% compliance with schema and linting rules.
- Document any coverage gaps in this file with remediation plans and owners.

## Reporting
- Summarize the latest test run results in this document, including date, command, outcome, and coverage percentage.
- Update `STATUS.md` with the `tested` percentage and note untested areas.
- Link failing tests to tasks in `PLAN.md` for remediation.

## Declaring Untested Areas
- Use the format `untested: <scope> — <reason> — <owner> — <planned date>`.
- Untested items must not linger longer than one milestone without approval.

## Example Entry
```
last_run:
  date: 2024-01-12
  command: npm run test && npm run lint
  outcome: failed
  coverage: 76%
untested:
  - workflow automation — awaiting staging environment — Kai — 2024-01-19
```

Adhering to these testing standards ensures the Magnetar canon remains reliable and enforceable across repositories.
