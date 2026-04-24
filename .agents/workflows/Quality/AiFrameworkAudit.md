---
name: ai-framework-audit
description: >
  Comprehensive audit of the Agentic AI Framework, covering persona alignment,
  workflow compliance, rule signal-to-noise ratio, and skill health. Output is
  saved to `docs/track/audits/ai-framework-audit-<DATE>.md`.
---
# `/ai-framework-audit` — AI Agentic Framework Audit
> **Assume Role:** `@arch-audit` (Architecture Audit)

## 🎯 Purpose
To ensure the AI agentic infrastructure (personas, workflows, rules, and skills) remains high-performance, consistent, and free of agentic drift. This audit verifies that the "Morphic" laws defined in `AGENTS.md` are being strictly enforced across all operational files.

## 🛠️ Step 1 — Framework Inventory
1. **Persona Check**: Read `AGENTS.md` and `.gemini/agents/`. Verify that every persona has a clear description and toolset.
2. **Workflow Check**: List `.agents/workflows/`. Verify that every workflow has an `Assume Role` header and follows the standardized audit nomenclature.
3. **Rule Check**: List `.agents/rules/`. Categorize rules by trigger (always_on, glob, manual).
4. **Skill Check**: List `.agents/skills/`. Verify that each skill has a `SKILL.md` and is correctly indexed.

## 📊 Step 2 — Drift & Signal Analysis
1. **Drift Analysis**: Identify any workflows or rules that refer to non-existent personas or deprecated paths.
2. **Signal-to-Noise**: Identify redundant or overly verbose rules that may be causing "Token Bloat" without adding reasoning value.
3. **Instruction Parity**: Ensure that `SoftwareStandards.md` and `CodeQuality.md` are correctly referenced in the implementation workflows.

## 📝 Step 3 — Write the AI Audit Results
Write the full audit to `docs/track/audits/ai-framework-audit-<DATE>.md` using this template:

```md
# 🤖 AI Agentic Framework Audit
**Date:** <DATE>
**Assumed Persona:** `@arch-audit` (Architecture Audit)
**Framework Version:** v1.0.0 (Morphic)

---

## 👥 1. Persona Compliance
| Persona | Defined in AGENTS.md | Config in .gemini/ | Status |
| :--- | :---: | :---: | :--- |
| @brain | [x] | [x] | Healthy |
| @arch-audit | [x] | [x] | Healthy |
| ... | ... | ... | ... |

## 🔄 2. Workflow Integrity
- **Audit Nomenclature**: [ ] Pass / [ ] Fail (List violations)
- **Role Assumption**: [ ] Pass / [ ] Fail (List workflows missing "Assume Role")
- **Manual vs Auto Parity**: Check if Smith manual workflows match Auto phases.

## 📜 3. Rule Signal Analysis
- **High Signal**: Rules that are frequently triggered and provide clear guardrails.
- **Low Signal / Bloat**: Rules that are redundant or too generic.
- **Missing Triggers**: Rules that should be `always_on` but are `manual`.

## 🛠️ 4. Skill Health
- **Orphaned Skills**: Skills without active workflow usage.
- **Documentation Gaps**: Skills missing `SKILL.md` or usage examples.

## 🚀 5. Actionable Fixes
1. [ ] TODO(ai_fix_xxx): ...
2. [ ] TODO(ai_fix_yyy): ...
```

## 🏁 Step 4 — Close the Loop
1. **Update TODO.md**: Add any identified framework fixes with the `TODO(ai_framework_xxx)` prefix.
2. **Summary**: Share a high-level summary of the framework health with the user.
