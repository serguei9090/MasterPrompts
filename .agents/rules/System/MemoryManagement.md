# AI Memory Management Rule

To ensure long-term architectural integrity and context continuity, all agents must adhere to the Memory Management Protocol.

## 1. The Distillation Mandate
At the completion of any task labeled `feat`, `refactor`, or `fix` (v0.5+), the agent MUST:
- Identify if any new **Architectural Decisions**, **Implementation Patterns**, or **Lessons Learned** were generated.
- If so, invoke the `@memory-manager` or follow the `/CreateMemory` workflow to record the insight in `docs/memory/`.

## 2. Memory Indexing
The `docs/memory/index.md` file is the Source of Truth for available project memory.
- Every new memory file MUST be registered in the index with a one-sentence summary.
- The index must be categorized by the folder structure: `decisions`, `entities`, `patterns`, `lessons`, `sessions`.

## 3. Atomic Memory Format
Memory files should be "AI-Optimized":
- **Header**: Purpose and Date.
- **Context**: Why this memory exists.
- **The Core Insight**: Concise, factual bullet points.
- **References**: Links to relevant files, TODOs, or conversation IDs.

## 4. Conflict Resolution
If a new task contradicts an existing memory:
- Use `sequentialthinking` to analyze the conflict.
- **Fallback**: If `sequentialthinking` is unavailable, follow the `/SequentialThinkingBackup` workflow.
- Propose a "Memory Pivot" to the user.
- Upon approval, update the existing memory and mark the old one as superseded (or move to `archive/`).

## 5. Graceful Degradation (MCP Fallback)
All agents must monitor for tool execution failures related to MCP servers.
- If an MCP tool (e.g., `sequentialthinking`) is missing or fails, agents MUST automatically pivot to the corresponding `/Backup` workflow in `.agents/workflows/Autonomous/`.
- Report the tool failure to the user in the final summary.

## 6. Smith Integration
During the `Smith` (Autonomous) cycle:
- A "Memory Sync" step must occur at the beginning to ingest relevant project memories.
- A "Memory Distillation" step must occur at the end to persist new knowledge.
