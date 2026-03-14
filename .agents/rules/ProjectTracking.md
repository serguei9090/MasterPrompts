---
trigger: manual
description: Standard for project progress tracking and documentation management.
---

# Project Tracking Standards

Maintain a clear, professional, and transparent project roadmap inside `docs/track/`.

## 1. Tracking Files
- **`TODO.md`**: Main active roadmap. Tracks current phases, roadmap items, and completed milestones. 
- **`FeaturesProposal.md`**: Deferred features, ideas, and post-MVP enhancements.
- **`CodeDebt.md`**: Technical debt, refactoring needs, and known bugs.
- **`codegapreview.md`**: Architectural implementation gaps, missing logic, and spec discrepancies. (Audit this using the `code-gap-reviewer` skill).

## 2. Dual-Roadmap Parity Law
- **Sync Requirement**: The AI agent manages an internal state (e.g., `task.md` or system artifact). This internal task list MUST be kept in 100% parity with the human-facing `docs/track/TODO.md`.
- **Status Updates**: After completing any task or feature, the agent MUST update both the internal state and the project's `docs/track/TODO.md` by marking the item as completed (`[x]`).
- **Debt Tracking**: Document any technical debt introduced or discovered during development immediately in `CodeDebt.md`.
- **Scope Management**: New feature requests or ideas mentioned outside the current active sprint should be logged into `FeaturesProposal.md`.
- **Status Reporting**: Always reference the exact status of these files when providing progress summaries.

## 3. Directory Integrity
- All tracking files MUST live in `docs/track/`.
- Redundant tracking files in the root or other generic `docs/` folders must be consolidated here and removed.
