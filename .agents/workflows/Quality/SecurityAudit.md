---
name: security-audit
description: Run security scans (npm audit) and generate a security audit. Use when asked to check security or vulnerabilities.
---

# Security Audit Protocol
> **Assume Role:** `@qa` (Quality Assurance)

## Overview
Identify and classify vulnerabilities in dependencies and code. Results are stored in `docs/track/audits/`.

## Workflow

### 1) Dependency Scan
- Run `[PKG_MANAGER] audit --json`.
- Parse the output.
- **Critical/High** vulnerabilities: **FAIL** the workflow.
- **Moderate/Low**: Warn only.

### 2) Static Analysis (SAST)
- If `trivy` or `snyk` is installed, run them.
- If not, rely on `[PKG_MANAGER] audit`.

## Audit Template (`docs/track/audits/security_audit.md`)

```md
# Security Audit

**Date:** YYYY-MM-DD
**Overall Risk:** LOW / HIGH

## Vulnerabilities Found
| Package | Severity | Fix Available |
| :--- | :--- | :--- |
| axios | High | Yes (v1.6.0) |

## Action Plan
- [ ] Run `[PKG_MANAGER] audit fix`
- [ ] Manual upgrade required for: [Package Name]
```
