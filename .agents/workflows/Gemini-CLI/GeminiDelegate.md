---
description: The Surgical Route - PM plans, Gemini CLI executes massive local code generation.
---

# 🛸 Gemini Delegate Workflow

Triggered by `/gemini-delegate <idea>`. This workflow uses the external Gemini CLI to handle large-scale code generation tasks, keeping the primary chat clean.

## 📋 Execution Sequence

### 1. 📋 Planning (@pm)
- **Role**: `Product Manager (@pm)`
- **Task**: Use the `shape` skill to define the mission architecture and requirements.
- **Artifacts**: `docs/track/specs/PLAN-[TASK_ID].md` and `docs/track/TODO.md`.
- *(PAUSE for user approval of the plan before continuing.)*

### 2. ⚡ Delegation (@devops)
- **Role**: `DevOps Master (@devops)`
- **Task**: Launch the Gemini CLI to execute the implementation phase.
- **Command**:
  ```powershell
  gemini -y -p "You are the @fullstack-developer. Read the implementation plan in docs/track/specs/PLAN-[TASK_ID].md and execute the implementation using surgical edits. Adhere to System rules in .agents/rules/System/."
  ```

### 3. 🔍 Monitoring & QA (@qa)
- **Role**: `QA Engineer (@qa)`
- **Task**: Inspect the changes made by the CLI.
- **Action**: Run `/quality-report` to verify linting and formatting.

### 4. 🏁 Finalization (@scribe)
- **Role**: `Historian (@scribe)`
- **Task**: Document the session and update `docs/track/LessonsLearned.md`.

---

// turbo
**Command**: `gemini -y -p "Execute /gemini-delegate for <idea>"`
