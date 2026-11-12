# Architecture Blueprint

> This document describes the architecture of the Magnetar Canonical Project Model, covering governance, planning, agent orchestration, and execution workflows. It defines the standard components, repository layouts across project tiers, and how the architecture adapts to small and large initiatives.

The Magnetar Canonical Project Model defines architecture as the structure of governance, planning artifacts, agent interaction protocols, and execution workflows that any project must adopt. Its guidance scales from lightweight single-purpose scripts to complex multi-team enterprise platforms.

---

## 1. Conceptual Architecture Diagram

```
+-----------------------------------------------------------------------------+
| AGENT & COLLABORATOR ENTRY LAYER                                            |
| (AGENTS.md, MODEL_POLICY.md, CLAUDE.md, GEMINI.md)                         |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| GOVERNANCE & BOUNDARIES                                                     |
| (RULES.md, WIP_GUIDELINES.md, BRANCHING_MODEL.md, GLOSSARY.md)              |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| STRATEGY & REQUIREMENTS LAYER                                               |
| (README.md, REQUIREMENTS.md, ARCHITECTURE.md, DECISIONS.md)                 |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| PLANNING & STATE MACHINE                                                    |
| (PLAN.md, projects/*.project.yml)                                           |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| EXECUTION & LIVING AUDIT TRAIL                                              |
| (BITACORA.md, STATUS.md, BLOCKERS.md, TESTING.md)                           |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| AUTOMATED VERIFICATION                                                      |
| (scripts/magnetar_check.py, .github/workflows/magnetar-lint.yml)            |
+-----------------------------------------------------------------------------+
```

---

## 2. Standard Architectural Layers

1. **Agent & Collaborator Entry Layer**: Provides an immediate context-efficient router (`AGENTS.md`) and model allocation policy (`MODEL_POLICY.md`) preventing AI context bloat and hallucination.
2. **Governance Layer**: Enforces branch lifecycle rules, non-negotiable WIP limits (maximum 2 active tasks), and consistent naming conventions.
3. **Strategy & Design Layer**: Clarifies the "what" and "why" (`REQUIREMENTS.md`), the structural system topology (`ARCHITECTURE.md`), and the historical decision journal (`DECISIONS.md`).
4. **Planning Layer**: Maintains the structured backlog, effort weighting, milestones, and machine-readable project schema.
5. **Execution & Audit Layer**: Captures real-time project pulse (`STATUS.md`), the immutable chronological journal (`BITACORA.md`), active impediments (`BLOCKERS.md`), and test validation metrics (`TESTING.md`).
6. **Automated Verification**: Zero-dependency tooling (`scripts/magnetar_check.py`) that audits canon compliance locally and in CI.

---

## 3. Tiered Repository Layouts

### Tier 1: Micro Project (Spike, CLI Script, Prototype)
```
my-micro-tool/
├── README.md
├── AGENTS.md
├── PLAN.md
├── STATUS.md
├── RULES.md
└── src/
```

### Tier 2: Standard Project (Application, Service, Library)
```
my-standard-service/
├── README.md
├── AGENTS.md
├── REQUIREMENTS.md
├── ARCHITECTURE.md
├── PLAN.md
├── STATUS.md
├── BITACORA.md
├── BLOCKERS.md
├── TESTING.md
├── RULES.md
├── BRANCHING_MODEL.md
├── WIP_GUIDELINES.md
├── CONTRIBUTING.md
├── projects/
│   └── my-service.project.yml
└── src/
```

### Tier 3: Extended / Enterprise (Monorepo, Multi-Service, Regulated)
```
my-enterprise-platform/
├── README.md
├── AGENTS.md
├── MODEL_POLICY.md
├── REQUIREMENTS.md
├── ARCHITECTURE.md
├── DECISIONS.md              <-- Architecture Decision Records (ADRs)
├── GLOSSARY.md               <-- Domain vocabulary & identifier registry
├── PLAN.md
├── STATUS.md
├── BITACORA.md
├── BLOCKERS.md
├── TESTING.md
├── RULES.md
├── BRANCHING_MODEL.md
├── WIP_GUIDELINES.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── projects/
│   └── platform.project.yml  <-- tier: extended
├── scripts/
│   └── magnetar_check.py     <-- CI validation script
└── docs/
    └── specs/                <-- Deep domain feature specifications
```

---

## 4. Integration with AI Agent Workflows

The architecture treats AI agents as modular execution workers and Markdown as the durable state machine:
- **No Agent Vendor Lock-in**: Whether interacting via Claude Code, Antigravity, Cursor, or Codex, agents read standard Markdown and execute within standard Git workflows.
- **Traceability**: Code cannot be committed without a task in `PLAN.md` and an entry in `BITACORA.md`.
- **Context Preservation**: Agents only open the files relevant to their immediate task (as routed by `AGENTS.md`), avoiding context saturation.
