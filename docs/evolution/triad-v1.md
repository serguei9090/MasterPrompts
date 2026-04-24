# Triad Orchestration Workflow v1.0

This workflow describes the default interaction pattern for the Antigravity-Gemini-Jules triad.

## Steps

1. **Intake & Planning**
    - Antigravity reads the user request.
    - Antigravity checks `.agents/rules` for constraints.
    - Antigravity updates `docs/track/TODO.md`.

2. **Work Assignment**
    - IF task is < 3 files and < 200 lines: Handled locally by **Antigravity** or **Gemini CLI**.
    - IF task involves system-wide refactoring or complex testing: Call **Jules CLI** directly (`jules remote new ... --record`).

3. **Execution & Validation**
    - Code is committed and pushed upstream before Jules invocation.
    - Jules processes the task remotely while Antigravity monitors or proceeds.
    - Results are pulled and verified.

4. **Completion**
    - Antigravity updates `docs/track/TODO.md`.
    - Final summary is shared with the user.
