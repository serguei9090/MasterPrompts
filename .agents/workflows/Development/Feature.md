---
description: Formal workflow for documentation, description, and implementation of new feature requests.
---
# /feature [request]
> **Assume Role:** `@brain` (Lead Architect)

This workflow standardizes how new capabilities are added to LogLensAi.

## Phase 1: The Spec (Vibe → Research)
1. **Understand**: Antigravity (Chat) analyzes the raw request against `AGENTS.md` and `PRD.md`.
2. **Draft**: Create a specific feature spec in `docs/features/<feature_id>.md`.
3. **Standards**: Ensure the spec includes:
    - **UI Designer (@ui-designer)**: Component logic, interactions, and accessibility (Frontend).
    - **Theme Expert (@theme-expert)**: Design tokens, layout primitives, and visual identity.
    - **API Specialist (@api-specialist)**: Data contracts, RPC boundary definition, and backend logic.
    - **Acceptance Criteria**: Gherkin or TDD requirements.

## Phase 2: Approval & API Handshake
1. **Present**: Share the spec link with the user.
2. **API Handshake (@api-specialist)**: 
   - Mandatory: Define strict Pydantic models (Backend) and TS Interfaces (Frontend).
   - Verify serialization/deserialization logic for the JSON-RPC bridge.
3. **Critique**: User provides feedback or "Approve."
4. **Finalize**: Update `AGENTS.md` if the core contract changes.

## Phase 3: The Plan (Ticketing)
1. **Index**: Add sub-tasks to `docs/track/TODO.md` with unique IDs (e.g., `FEAT-001`).
2. **Memory**: Create `docs/track/specs/<task_id>.md` for implementation details.

## Phase 4: Execution Choice
Select the appropriate execution engine:

### Engine A: Antigravity (Interactive Chat)
// turbo
1. **Implement**: Perform the file changes directly in this chat session.
2. **Verify**: Run tests and linting in the background.

### Engine B: Jules (Direct CLI Cycle)
// turbo
1. **Instruct**: Antigravity constructs `docs/Documentation/meta/jules_instruct.md`.
2. **Launch**: Run the direct CLI command:
   ```powershell
   $prompt = Get-Content docs/Documentation/meta/jules_instruct.md -Raw ; $prompt | jules new
   ```
3. **Sync**: Once Jules finishes, Antigravity documents the session ID and pulls results via `jules pull`.

### Engine C: AutoCode (Autonomous Implementation Engine)
// turbo
1. **Mission**: Run `gemini -y -p "Execute /autocode for <feature_id>"`
2. **Loop**: The engine performs the 3-iteration surgical edit loop autonomously.
3. **Merge**: Review and merge results into the main branch.

## Phase 5: Architecture & Quality Audit (@arch-audit)
1. **Structural Audit**: Run `/project-audit` to generate a fresh `docs/track/audits/project-audit-<DATE>.md`.
2. **Logic Check**: Verify implementation against `.agents/rules/System/Architecture.md`.
3. **AVAS Sync**: Update architecture diagrams using `diagram-creator`.

## Phase 6: Verification & Lessons Learned
1. **E2E Check**: Verify the feature works in the Tauri desktop environment.
2. **Retrospective**: Update `docs/track/Session_Retrospective.md` and `docs/track/LessonsLearned.md`.
