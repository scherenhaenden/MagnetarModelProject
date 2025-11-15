# Requirements Specification

> Este documento detalla los requisitos funcionales y no funcionales del Magnetar Canonical Project Model. Describe lo que el proyecto debe hacer, incluyendo el conjunto de documentación canónica, la plantilla de esquema del proyecto y una implementación de ejemplo. También define los criterios de aceptación para el proyecto.

## Functional Requirements
1. **Canonical Documentation Set**
   - The repository must contain the full suite of governance and execution documents listed in the README table.
   - Each document must include predefined sections, definitions, and examples that projects can adapt directly.
2. **Project Schema Template**
   - Provide a machine-readable YAML template with descriptive comments for every field.
   - The schema must cover metadata, milestones, tasks, risks, testing, communication paths, and reporting cadence.
3. **Example Implementation**
   - Deliver a fully populated example project under `examples/simple-project-demo/` demonstrating correct usage of every artifact.
   - The example must include realistic progress metrics, blockers, and test declarations.
4. **Guidance for AI and Human Collaboration**
   - Clearly describe how agents should interpret documents, enforce WIP limits, and update project history.

## Non-Functional Requirements
- **Clarity** – Language must be explicit, avoiding ambiguous verbs or jargon; each rule references the document responsible for compliance.
- **Consistency** – Headings, lists, and terminology remain uniform across files (e.g., task states, blocker statuses).
- **Traceability** – Cross-references point to file names and sections so readers can navigate the canon quickly.
- **AI-Readable** – Structured data uses predictable formatting (tables, YAML, bullet lists) to support automated parsing.
- **Versionable** – Content should minimize duplication and highlight when updates must cascade to other files.

## Acceptance Criteria (Gherkin)
```
Feature: Canonical Magnetar model availability
  Scenario: Repository bootstrapping a new project
    Given a consumer clones the canonical repository
    When they inspect the root directory
    Then they find all required governance and execution documents
    And each document explains how to tailor it to a new initiative

  Scenario: Generating a project YAML file
    Given a template is available at projects/_template.project.yml
    When a maintainer copies the template into a new project
    Then every field contains a comment describing its purpose
    And the resulting YAML validates against Magnetar parsing tools

  Scenario: Consulting the example project
    Given the examples/simple-project-demo directory
    When a contributor reviews its files
    Then they observe coherent progress metrics, tasks, blockers, and testing notes
    And the narrative aligns with the canonical rules and requirements
```

## Completion Criteria
- All files listed in Phase 2 exist with comprehensive, human-readable content.
- The YAML template covers every field referenced in the rules and requirements with inline documentation.
- The example project reflects partial progress, open blockers, and pending tests consistent with the canonical standards.
- Documentation cross-references align (e.g., task states in `PLAN.md`, `STATUS.md`, and `RULES.md`).
- `git status` is clean and all changes reside on the `canonical-model-init` branch ready for review.
