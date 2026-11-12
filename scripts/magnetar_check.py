#!/usr/bin/env python3
"""
Magnetar Canon Compliance Validator
Zero-dependency CLI script to verify that a repository adheres to the
Magnetar Canonical Project Model according to its declared project tier.
"""

import sys
import os
import re
import argparse
from pathlib import Path

VALID_TASK_STATES = {"planned", "ready", "in_progress", "in_review", "blocked", "done"}

TIER_REQUIRED_FILES = {
    "micro": [
        "README.md",
        "AGENTS.md",
        "PLAN.md",
        "STATUS.md",
        "RULES.md",
    ],
    "standard": [
        "README.md",
        "AGENTS.md",
        "PLAN.md",
        "STATUS.md",
        "RULES.md",
        "REQUIREMENTS.md",
        "ARCHITECTURE.md",
        "BITACORA.md",
        "TESTING.md",
        "BLOCKERS.md",
        "BRANCHING_MODEL.md",
        "WIP_GUIDELINES.md",
    ],
    "extended": [
        "README.md",
        "AGENTS.md",
        "PLAN.md",
        "STATUS.md",
        "RULES.md",
        "REQUIREMENTS.md",
        "ARCHITECTURE.md",
        "BITACORA.md",
        "TESTING.md",
        "BLOCKERS.md",
        "BRANCHING_MODEL.md",
        "WIP_GUIDELINES.md",
        "DECISIONS.md",
        "GLOSSARY.md",
        "MODEL_POLICY.md",
    ],
}

class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @classmethod
    def disable(cls):
        cls.GREEN = cls.YELLOW = cls.RED = cls.BLUE = cls.BOLD = cls.RESET = ""

if not sys.stdout.isatty():
    Colors.disable()


def detect_project_tier(root: Path) -> str:
    """Detect project tier from YAML files in projects/ or fallback to standard."""
    projects_dir = root / "projects"
    if projects_dir.exists() and projects_dir.is_dir():
        for yml_file in projects_dir.glob("*.project.yml"):
            try:
                content = yml_file.read_text(encoding="utf-8")
                match = re.search(r"tier:\s*([a-zA-Z0-9_\-]+)", content)
                if match:
                    tier = match.group(1).lower().strip()
                    if tier in TIER_REQUIRED_FILES:
                        return tier
            except Exception:
                continue
    return "standard"


def check_required_files(root: Path, tier: str, errors: list, warnings: list):
    """Verify presence of mandatory files for the tier."""
    required = TIER_REQUIRED_FILES.get(tier, TIER_REQUIRED_FILES["standard"])
    for rel_path in required:
        file_path = root / rel_path
        if not file_path.exists():
            errors.append(f"Missing required file for tier '{tier}': {rel_path}")
        elif file_path.stat().st_size == 0:
            warnings.append(f"File is empty: {rel_path}")

    # Check for projects/*.project.yml in standard and extended
    if tier in {"standard", "extended"}:
        projects_dir = root / "projects"
        if not projects_dir.exists() or not list(projects_dir.glob("*.project.yml")):
            errors.append("Standard/Extended tier requires at least one project YAML file in 'projects/*.project.yml'")


def check_plan_file(root: Path, errors: list, warnings: list):
    """Verify PLAN.md task backlog table, task states, and WIP limits."""
    plan_file = root / "PLAN.md"
    if not plan_file.exists():
        return

    content = plan_file.read_text(encoding="utf-8")
    lines = content.splitlines()

    in_backlog = False
    header_indices = {}
    tasks = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## ") and any(term in stripped.lower() for term in ["task backlog", "tasks"]):
            in_backlog = True
            continue
        elif in_backlog and stripped.startswith("## "):
            in_backlog = False
            continue

        if in_backlog:
            if stripped.startswith("|") and ("Task ID" in stripped or "State" in stripped):
                headers = [h.strip().lower() for h in stripped.split("|")[1:-1]]
                header_indices = {h: i for i, h in enumerate(headers)}
                continue
            elif stripped.startswith("|") and header_indices:
                cols = [c.strip() for c in stripped.split("|")[1:-1]]
                if all(set(c).issubset({"-", ":", " "}) for c in cols if c):
                    continue
                if len(cols) >= len(header_indices):
                    task_id_col = header_indices.get("task id")
                    state_col = header_indices.get("state")
                    owner_col = header_indices.get("owner")

                    task_id = cols[task_id_col] if task_id_col is not None else "unknown"
                    state = cols[state_col].strip("`").lower() if state_col is not None else ""
                    owner = cols[owner_col] if owner_col is not None else "unassigned"

                    if task_id and state:
                        tasks.append({"id": task_id, "state": state, "owner": owner})

    if not tasks:
        warnings.append("PLAN.md: No tasks detected in Task Backlog table.")
        return

    # Validate task states
    invalid_states = [t for t in tasks if t["state"] not in VALID_TASK_STATES]
    for inv in invalid_states:
        errors.append(f"PLAN.md: Task '{inv['id']}' has invalid state '{inv['state']}'. Must be one of: {', '.join(sorted(VALID_TASK_STATES))}")

    # WIP limit check: max 2 in_progress per owner
    in_prog_by_owner = {}
    for t in tasks:
        if t["state"] == "in_progress":
            owner = t["owner"].lower()
            in_prog_by_owner[owner] = in_prog_by_owner.get(owner, 0) + 1

    for owner, count in in_prog_by_owner.items():
        if count > 2:
            warnings.append(f"PLAN.md: WIP limit exceeded for owner '{owner}' ({count} tasks in_progress, maximum allowed is 2).")


def check_locks(root: Path, errors: list, warnings: list):
    """Validate active task locks in locks/ to prevent parallel collisions."""
    locks_dir = root / "locks"
    if not locks_dir.exists() or not locks_dir.is_dir():
        return

    seen_tasks = {}
    for lock_file in locks_dir.glob("*.lock.yml"):
        if lock_file.name.startswith("_template"):
            continue
        try:
            content = lock_file.read_text(encoding="utf-8")
            task_match = re.search(r"task_id:\s*([a-zA-Z0-9_\-]+)", content)
            agent_match = re.search(r"agent_id:\s*([a-zA-Z0-9_\-]+)", content)

            if not task_match:
                errors.append(f"Lock file '{lock_file.name}' is missing required 'task_id:' declaration.")
                continue

            task_id = task_match.group(1)
            agent_id = agent_match.group(1) if agent_match else "unknown"

            if task_id in seen_tasks:
                errors.append(f"Collision detected: Task '{task_id}' is locked by multiple agents ('{seen_tasks[task_id]}' and '{agent_id}').")
            else:
                seen_tasks[task_id] = agent_id
        except Exception as ex:
            warnings.append(f"Could not read lock file '{lock_file.name}': {ex}")


def check_bitacora(root: Path, tier: str, warnings: list):
    """Check BITACORA.md has the proper structure and at least one entry."""
    if tier == "micro":
        return
    bitacora_file = root / "BITACORA.md"
    if not bitacora_file.exists():
        return

    content = bitacora_file.read_text(encoding="utf-8")
    if "## Chronological Log" not in content and "| Date" not in content:
        warnings.append("BITACORA.md: Expected '## Chronological Log' table with '| Date | Time | Author | Entry |'.")


def main():
    parser = argparse.ArgumentParser(description="Magnetar Canon Compliance Validator")
    parser.add_argument("--path", default=".", help="Root directory of the project to check")
    parser.add_argument("--tier", choices=["micro", "standard", "extended"], default=None, help="Force specific tier check (defaults to autodetect)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    tier = args.tier or detect_project_tier(root)

    print(f"\n{Colors.BOLD}{Colors.BLUE}=== Magnetar Canon Compliance Check ==={Colors.RESET}")
    print(f"Project Path: {root}")
    print(f"Assessed Tier: {Colors.BOLD}{tier.upper()}{Colors.RESET}\n")

    errors = []
    warnings = []

    check_required_files(root, tier, errors, warnings)
    check_plan_file(root, errors, warnings)
    check_locks(root, errors, warnings)
    check_bitacora(root, tier, warnings)

    # Print results
    if warnings:
        print(f"{Colors.YELLOW}{Colors.BOLD}Warnings ({len(warnings)}):{Colors.RESET}")
        for w in warnings:
            print(f"  {Colors.YELLOW}⚠{Colors.RESET} {w}")
        print()

    if errors:
        print(f"{Colors.RED}{Colors.BOLD}Errors ({len(errors)}):{Colors.RESET}")
        for e in errors:
            print(f"  {Colors.RED}✖{Colors.RESET} {e}")
        print()
        print(f"{Colors.RED}{Colors.BOLD}RESULT: FAILED{Colors.RESET} ({len(errors)} errors found)\n")
        sys.exit(1)

    if args.strict and warnings:
        print(f"{Colors.RED}{Colors.BOLD}RESULT: FAILED (--strict mode: {len(warnings)} warnings treated as errors){Colors.RESET}\n")
        sys.exit(1)

    print(f"{Colors.GREEN}{Colors.BOLD}RESULT: PASSED{Colors.RESET}")
    print(f"All canonical constraints satisfied for Tier '{tier}'.\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
