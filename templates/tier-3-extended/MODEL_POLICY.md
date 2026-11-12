# Magnetar AI Model Policy & Sizing Framework

> This document defines the model selection framework for AI collaborators on Magnetar projects. It matches AI model tiers (speed/compact, balanced, and deep-reasoning) to project sizes and task risk categories, optimizing cost, speed, and cognitive accuracy.

---

## 1. Why Model Sizing Matters

Not every task requires a high-latency, maximum-parameter model, and small models often struggle with complex multi-system architectural refactoring. Magnetar uses a tiered model allocation matrix so teams and agents allocate the right intelligence tier to the right problem:

```
+-----------------------------------------------------------------------------+
| TIER 1 (FAST / COMPACT)                                                     |
| Models: Gemini Flash, Claude Haiku, GPT-4o-mini                             |
| Focus: High-velocity execution, single-file scripts, doc linting, status    |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| TIER 2 (BALANCED / PRODUCTION)                                              |
| Models: Claude Sonnet, Gemini Pro / Argon, GPT-4o                           |
| Focus: Core engineering, multi-file refactoring, feature implementation     |
+-----------------------------------------------------------------------------+
                                      |
                                      v
+-----------------------------------------------------------------------------+
| TIER 3 (DEEP REASONING / ARCHITECTURAL)                                     |
| Models: o1 / o3-mini, Claude Opus / Sonnet Thinking, Gemini Thinking        |
| Focus: Cross-service topology, ADR evaluation, security audits, math logic  |
+-----------------------------------------------------------------------------+
```

---

## 2. Project Tier to Model Tier Mapping

| Project Scale | Recommended Default Model Tier | Fallback / Escalation Tier | Rationale |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Micro)**<br>*Scripts, Spikes, Prototypes* | **Fast / Compact** | Balanced | Low architectural complexity; prioritizes speed, immediate iteration, and lightweight updates to `PLAN.md` and `STATUS.md`. |
| **Tier 2 (Standard)**<br>*Applications, Services, Libraries* | **Balanced / Production** | Deep Reasoning | Standard commercial development; requires nuanced code synthesis, rigorous testing design, and consistent state tracking. |
| **Tier 3 (Extended)**<br>*Monorepos, Multi-Service, Regulated* | **Balanced** for tasks<br>**Deep Reasoning** for architecture/ADRs | Deep Reasoning | High penalty for architectural errors. Complex cross-repo dependency graphs and strict compliance demands deep cognitive modeling. |

---

## 3. Task Risk & Cognitive Profile Matrix

Regardless of the project size, individual tasks may require escalating or downgrading model capabilities:

| Task Category | Recommended Model Type | Key Model Characteristics Needed | Example Activities |
| :--- | :--- | :--- | :--- |
| **Operational & Tracking** | Fast / Compact | Fast latency, tight JSON/table parsing | Updating `BITACORA.md`, refreshing `STATUS.md` metrics, running `scripts/magnetar_check.py`. |
| **Unit & Integration Coding** | Balanced | Strong language understanding, tool use | Implementing API endpoints, building UI components, writing unit tests. |
| **Architectural Design (ADRs)** | Deep Reasoning | Extensive chain-of-thought, trade-off analysis | Drafting `DECISIONS.md`, designing schema migrations, boundary definitions in `ARCHITECTURE.md`. |
| **Root Cause Debugging** | Deep Reasoning | Multi-hypothesis elimination, log analysis | Resolving critical blockers in `BLOCKERS.md`, race conditions, concurrency bottlenecks. |
| **Code Review & Audit** | Balanced or Deep Reasoning | High precision, attention to security rules | Verifying acceptance criteria before moving `in_review → done`, checking against `RULES.md`. |

---

## 4. Multi-Agent Team Composition (When using swarms or subagents)

When orchestrating multiple agents within a Magnetar project:
1. **Coordinator / Lead Agent**: Run on **Balanced** or **Deep Reasoning** to maintain macro-level planning, milestone tracking, and task state management in `PLAN.md`.
2. **Worker Agents (Specialists)**: Run on **Balanced** (or **Fast** for small edits) pinned to specific task IDs.
3. **Reviewer / Verifier Agent**: Run on an independent context on a **Balanced** model to execute `TESTING.md` protocols and approve transitions to `done`.

---

## 5. Model Change Discipline

If an agent or human developer changes models during a project lifecycle:
- Document the switch in `BITACORA.md` if it changes architectural ownership or task validation approach.
- In automated environments, declare the active model tier in the `projects/*.project.yml` metadata block:
  ```yaml
  metadata:
    model_tier_default: balanced # fast | balanced | reasoning
  ```
