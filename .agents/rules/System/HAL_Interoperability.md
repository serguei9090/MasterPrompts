---
trigger: always_on
---
# HAL: Hardware Abstraction Layer Protocol

To ensure universal interoperability and project portability, all agents must adhere to the **HAL standard** defined in `agents.yaml`.

## 1. Zero-Guesswork Initialization
At the start of every session, agents must:
- Read `agents.yaml` to resolve environment-specific paths and tool aliases.
- Replace any hardcoded paths in their mental context with the variables defined in the HAL (e.g., `project.root`).

## 2. Command Execution Law
When executing `run_command` or similar, agents must use the tool aliases defined in `binaries` (e.g., `uv`, `bun`, `jules`). NEVER call system-global binaries if a project-specific binary is defined.

## 3. Path Variable Resolution
All documentation, internal manifests, and handoff files MUST use standardized path variables.
- **Syntax**: `{{VAR_NAME}}`
- **Standard Variables**:
    - `{{ROOT}}`: The absolute project root directory.
    - `{{AGENTS}}`: Path to the `.agents/` folder.
    - `{{DOCS}}`: Path to the `docs/` folder.
    - `{{TRACK}}`: Path to the `docs/track/` folder.
- **Resolution**: Agents MUST resolve these variables using the values defined in `agents.yaml` before executing file reads or shell commands.

## 4. Handoff Continuity
Before calling another agent (e.g., Gemini CLI or Jules), the current agent MUST update the `handoff.json` manifest located at `handoff.manifest_path` with the current task state and environment context.
