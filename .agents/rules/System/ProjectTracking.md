---
trigger: model_decision
description: Mandatory standards for session boot sequence, progress tracking, and documentation management.
---

# Project Tracking & Session Boot Standards

Maintain a clear, professional, and transparent project roadmap and session continuity.

## 1. Mandatory Session "Boot Sequence"
At the start of every new session (detected via `model_decision` or the first user prompt), you MUST perform the following actions before writing a single line of code:
1.  **Read the Tracker**: Run `bd ready` or `bd list --status open`.
2.  **Read the Handoff**: Open `docs/track/handoff.md` to understand the last session's exit state and blockers.
3.  **Calibrate Internal Plan**: Update your internal "builtin plan task" to match the active Bead(s) exactly.
4.  **Confirm Readiness**: Briefly acknowledge the current state and the "Next Atomic Step" you are about to execute.

## 2. Tracking Files (Index vs. Detail)
- **Beads (bd) (The Index & Tracker)**: The absolute Source of Truth for task execution. Use `bd list` to view the roadmap and `bd ready` for available work. **Use Beads for status and metadata; avoid long text here.**
- **`docs/track/specs/task-<id>.md` (The Brain)**: Each complex task in Beads must have a dedicated detail file. **This is the primary location for long-form specifications**, technical rationale, and the full dependency map. The Bead description should simply reference this file.
- **`docs/track/TODO.md` (Visual Mirror)**: A non-authoritative, high-level visual summary for humans. This file is secondary to Beads and should not be used by the Agent for state management.
- **`docs/track/audits/` (The Auditor)**: Central folder for all project health reports, architecture audits, security scans, and quality reviews.
- **`FeaturesProposal.md`**: Deferred ideas and post-MVP enhancements.
- **`CodeDebt.md`**: Technical debt, refactoring needs, and known bugs.
- **`codegapreview.md`**: Architectural implementation gaps (Audit this using the `code-gap-reviewer` skill).

## 3. Beads-First Protocol
- **Source of Truth**: The `bd` system (powered by Dolt) is the sole authoritative source for task status, assignments, and dependencies.
- **Planning Parity**: Every major task MUST begin with a `sequentialthinking` pass. The output of this pass (impacted files, ripple effects, architectural risks) MUST be recorded in the task's spec file and broken down into **sub-beads** using `bd create`.
- **Status Updates**: After completing any task, update the `bd` tracker immediately using `bd update <id> --status completed` and run `bd dolt push` to sync.
- **Session Wrap-up**: At the end of a session, you MUST execute the `session-handover` skill to generate the next `handoff.md`.

## 3. Directory Integrity
- All tracking files MUST live in `docs/track/`.
- All audit/report files MUST live in `docs/track/audits/`.
- Redundant tracking or report files in the root or other generic `docs/` folders must be consolidated here and removed.

## 4. Atomic Execution Verifier (STRICT)
To prevent the "Announced but Not Executed" failure mode, the agent MUST adhere to this guardrail:
- **Command Confirmation**: You are FORBIDDEN from reporting a remote process (e.g., Jules, Docker, long-running scripts) as "Started" or "Active" until you have successfully executed the corresponding shell command AND verified its successful output/Session ID.
- **Result Registry**: Every started Jules session MUST have its Session ID and URL immediately registered in the chat and recorded in `docs/track/JULES.md`.
- **Pulse Check**: If a remote task is in progress, the agent MUST run a `jules remote list --session` or equivalent status check at the start of each turn to maintain session awareness.
