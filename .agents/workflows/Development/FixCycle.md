---
description: Issue & Fix Pipeline with Dialogue-First Consensus (LogLensAi Edition)
---

# /fixcycle: Issue & Fix Pipeline
> **Assume Role:** `@reviewer-agent` (Code Reviewer)

This workflow is triggered by `/fixcycle <issue_description>`. It prioritizes architectural consensus and critique before any code is modified.

### Execution Sequence:

### 1. Investigative Critique (@reviewer-agent):
- **Role**: `Reviewer (@reviewer-agent)`
   - Identify the reported issue or regression.
   - Perform deep-dive research into the codebase (sidecar, frontend state, DB queries).
   - Review any user-proposed solution.
   - **Critique Requirement**: Respond with:
     - **Confirmation**: If the solution is perfect.
     - **Fine-tuning**: If the solution needs minor adjustments (e.g., better naming, performance tweaks).
     - **Different Approach**: If the solution is logically flawed or architecturally unsound.
   - **MANDATORY**: Present a clear implementation plan before touching code.
   - **Pause**: "Critique complete. Do you agree with this approach? (Consent required to proceed to Step 2)"

### 2. Impact Analysis & Spec (@brain):
- **Role**: `Lead Architect (@brain)`
   - Verify the solution aligns with `.agents/rules/System/Architecture.md` and `.agents/rules/System/SoftwareStandards.md`.
   - Assign a Unique ID (e.g., `FIX-UX-001`) and create a detail file in `docs/track/specs/`.
   - Update `docs/track/TODO.md` under the "Bug Fixes" section.
   - **Action**: Update `docs/track/Technical_Specification.md` if the fix alters core logic.

### 3. Surgical Implementation (@api-specialist | @ui-designer | @theme-expert):
- **Role**: `Implementation Squad`
- **Tasks**:
  - **API Specialist (@api-specialist)**: Fix data contracts and JSON-RPC boundaries (Backend Logic).
  - **UI Designer (@ui-designer)**: Modify frontend components and interactions.
  - **Theme Expert (@theme-expert)**: Standardize CSS tokens and design consistency.
  - **Rule**: NO silent changes. Every modification must be linked to the `FIX(ID)`.

4. **Architecture & Quality Audit (@arch-audit)**:
   - Run `/project-audit` to verify structural integrity and quality standards.
   - Execute `audit_code.md` skill on the changed files.
   - If UI changed, follow `.agents/rules/Specialized/UIReviewProtocol.md`.
   - Verify fix with reproduction steps and ensure no regressions in `docs/Documentation/architecture/testing.md`.
   - **AVAS Verification**: Ensure all visual/diagrammatic representations are correct and updated via `@diagram-agent`.

### 5. Documentation & Handoff (@doc-agent):
- **Role**: `Documentarian (@doc-agent)`
   - Update `docs/track/LessonsLearned.md` with the root cause and "Preventative Measures" for the future.
   - Close the `TODO(ID)` in `docs/track/TODO.md`.
   - **Final Report**: "Issue resolved! Fix ID: `<ID>` is now part of the codebase. Review `docs/track/LessonsLearned.md` for details."
