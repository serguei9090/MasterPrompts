---
description: Autonomous Issue & Fix Pipeline (Zero Confirmation)
---

// turbo-all
> **Assume Role:** `@qa` (Quality Assurance)
This workflow is triggered by `/autofix <issue_description>`. Use this to fix bugs and regressions without waiting for manual plan approval.

### Execution Sequence:

1. **Investigative Critique (@critique)**:
   - Identify the reported issue or regression.
   - Perform deep-dive research into the codebase.
   - Propose the most optimal solution and proceed immediately to implementation.

2. **Impact Analysis & Spec (@architect)**:
   - Verify alignment with `Architecture.md`.
   - Assign a Unique ID (e.g., `FIX-UX-001`) and create `docs/track/specs/`.
   - Update `docs/track/TODO.md`.

3. **Surgical Implementation (@backend | @frontend | @ui-designer | @theme-expert | @api-specialist)**:
   - **Backend (@backend)**: Modify `sidecar/src/` with pydantic validation.
   - **API Specialist (@api-specialist)**: Update the RPC boundary if contracts are broken.
   - **Frontend (@frontend)**: Modify `src/` component logic.
   - **UI Designer (@ui-designer) & Theme Expert (@theme-expert)**: Fix CSS variable or design token drift.
   - Link all changes to the `FIX(ID)`.

4. **Quality Guardrail (@qa)**:
   - Execute `audit_code.md` skill on changed files.
   - Verify fix with reproduction steps and ensure no regressions.

5. **Legacy Documentation (@scribe)**:
   - Update `docs/track/LessonsLearned.md`.
   - Close the `TODO(ID)`.
   - **Final Report**: "Issue resolved autonomously! Fix ID: `<ID>` is now part of the codebase."
