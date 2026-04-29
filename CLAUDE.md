# Morphic Framework: AI Engineering Mandate (v0.10.7)

This file provides instructions and context for AI coding agents working on this project.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->

## 🛠️ Build & Test commands

| Stack | Build / Install | Test / Lint |
| :--- | :--- | :--- |
| **Python** | `uv sync` | `uv run pytest` / `uv run ruff check` |
| **JS / TS** | `bun install` | `bun test` / `bunx biome check` |
| **Framework** | `python scripts/build_morphic.py` | `scripts/hal-check.ps1` |

## 🏗️ Architecture Overview
- **Hexagonal (Ports & Adapters)**: Domain logic is isolated from infrastructure.
- **Sidecar Standard**: Pure Python JSON-RPC 2.0 backend (`sidecar/src/api.py`).
- **Atomic UI**: Component hierarchy (Atoms -> Molecules -> Organisms).
- **Bridge**: React-to-Sidecar communication via `callSidecar`.

## 📜 Conventions & Patterns
1. **Spec-First**: Define contracts (Pydantic/TS) before implementation.
2. **Design-First**: Update `DESIGN.md` before UI changes. Use Tokens only.
3. **5-Layer Memory**: ST -> Codanna -> Cognee -> context -> Beads.
4. **Assume Role**: Every file must start with `Assume Role: <Persona> (@handle)`.
5. **AVAS Law**: Diagrams must use Mermaid.js with labeled connections and subgraphs.
