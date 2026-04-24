---
name: test-coverage-audit
description: Run unit tests and coverage for this repository ([PKG_MANAGER] test, [PKG_MANAGER] run test:coverage) and write a summary audit to docs/track/audits/code_test_audit.md. Use when the user asks to execute tests/coverage and produce or refresh the test audit.
---

# Test Coverage Audit
> **Assume Role:** `@qa` (Quality Assurance)

## Overview

Run the repo unit tests and coverage, then capture the results in `docs/track/audits/code_test_audit.md`.

## Workflow

### 1) Confirm execution intent
- If the user explicitly says not to run tests now, do not execute commands; explain the intended steps only.
- Otherwise, proceed with execution.

### 2) Run unit tests
- From repo root, run `[PKG_MANAGER] test`.
- Capture pass/fail summary and any notable warnings.

### 3) Run coverage
- From repo root, run `[PKG_MANAGER] run test:coverage`.
- **Optimization:** Ensure the `text-summary` reporter is used (if supported) to get a concise console output, or parse the `reports/coverage/index.html` if available.
- Capture coverage summaries for each workspace/package and any failures.
- Code Coverage acceptance criteria is > 80%

### 4) Write audit results
- Write an audit results file to `docs/track/audits/code_test_audit.md` in the repo root.
- Keep the report concise, ASCII-only, and include:
  - Commands run
  - Unit test results by package/workspace
  - Coverage summary by package/workspace
  - Notable warnings or failures

Use this template:

```md
# Code Test Audit

Commands run:
- `[PKG_MANAGER] test`
- `[PKG_MANAGER] run test:coverage`

Unit test results:
- <package/workspace>: <summary>

Coverage results:
- <package/workspace>: <statements/branches/functions/lines>

Notes:
- <warnings/failures or "None">
```
