---
trigger: model_decision
description: Systematic quality check and audit workflow.
---

# 🛡️ Quality Audit Workflow
> **Assume Role:** `@qa` (Quality Assurance)

Triggered by `/quality-audit`. Executes comprehensive linting and formatting checks and generates both summary and detailed audits in `docs/track/audits/`.

## 📋 Execution Steps

### 1. 🔍 Validation Readiness
- Check if `biome` and `ruff` are installed via `scripts/hal-check.ps1`.
- Verify if any files are currently staged for commit.

### 2. 🧹 Linting & Formatting
- **Frontend (JS/TS)**:
  - Run `bun x biome check --write .`
  - Capture any remaining errors or warnings.
- **Backend (Python)**:
  - Run `uv run ruff check --fix .`
  - Run `uv run ruff format .`
  - Capture any remaining errors.

### 3. 📝 Audit Generation
- **Summary Audit (`docs/track/audits/quality_summary.md`)**:
  - Timestamp of the run.
  - Overall Pass/Fail status.
  - Count of fixed vs. remaining issues.
- **Detailed Audit (`docs/track/audits/quality_detailed.md`)**:
  - Full list of remaining lint/format violations.
  - Exact file paths and line numbers.
  - Suggested fix for each item.

### 4. 🏁 Conclusion
- If 0 errors remain: Finalize with "Codebase is IMPECCABLE."
- If errors remain: Assign a `TODO(quality_fix_xxx)` to address the failures.

---

// turbo
**Command to execute**: `bun x biome check . ; uv run ruff check .`
