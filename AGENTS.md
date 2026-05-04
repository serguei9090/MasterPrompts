# Master AI Context: Morphic AI Engineering Framework (v0.11.0)

Welcome to the Morphic AI Engineering Framework. This workspace is governed by high-performance software engineering laws.

## 🗺️ Rule-Map (The Laws of Physics)
- **Architecture**: `.agents/rules/System/Architecture.md` (Hexagonal + Ports/Adapters)
- **Tracking**: `.agents/rules/System/ProjectTracking.md` (Beads-First Protocol)
- **Software Standards**: `.agents/rules/System/SoftwareStandards.md` (DRY, KISS, SOLID, Language Specs)
- **Quality/Beads**: `.agents/rules/System/CodeQuality.md` (Beads Protocol + Skill Trigger Matrix)
- **Intelligence Stack**: `.agents/rules/System/IntelligenceStack.md` (**CRITICAL**: L0-L5 usage protocol — Sequential Thinking, Codanna, Cognee, Context, Context7, Beads)
- **No-Guesswork Law**: `.agents/rules/System/NoGuesswork.md` (**CRITICAL**: When the AI must use tools vs. when inference is allowed)
- **Skill Matrix**: `.agents/rules/System/SkillMatrix.md` (**CRITICAL**: Canonical skill-to-persona bindings for every SDLC phase)
- **Automation**: `.agents/rules/Automation/AutonomousExecution.md` (Sprint Mode + Loop Protocol)
- **Expert Practices**: `.agents/rules/Specialized/AIExpertPractices.md` (Mnemonic Anchors + Verification)
- **Visual Law**: `.agents/rules/Specialized/VisualArchitecture.md` (AVAS Visualization)

## Core Mandates

1. **Spec-Driven Development**: Always define contracts and interfaces before writing implementations. Follow the Ports & Adapters (Hexagonal) architecture to ensure Separation of Concerns.
2. **Multi-Layer Memory Architecture**: This project uses a 5-layered intelligence stack for maximum context density:
   - **Reasoning Engine: Sequential Thinking**: Core logical tool for planning, reflection, and multi-step verification. Must be used before any complex implementation.
   - **Layer 1: Codanna (Physical)**: Authoritative source for deep code analysis (symbols, call graphs, impact) and internal documentation RAG.
   - **Layer 2: Cognee (Semantic)**: Graph-based memory for conceptual rationale, architectural decisions, and cross-project technical lessons.
   - **Layer 3: context (Local)**: High-speed source for version-specific documentation of installed libraries (via `download_package`).
   - **Layer 4: context7 (External)**: Real-time source of truth for 3rd-party library documentation and live API research.
   - **Layer 5: Beads (Operational)**: Authoritative state for active tasks, roadmap, and session-to-session handoffs.

3. **Auto-Indexing Mandate**: To ensure zero-stale context, the `codanna-index` and `cognee-index` tasks are triggered automatically via Git hooks (`lefthook`). Always verify the index status if a large refactor has occurred.
4. **Codanna CLI-First Protocol**: To ensure reliability and avoid connection friction, always prefer the `codanna mcp` CLI interface over the persistent server. 
   - **Command Pattern**: `codanna mcp <tool> --args '<json>' --json`.
   - **Mandatory Refresh**: Run `codanna index .` and `codanna documents index` after any significant structural changes.
5. **Beads Protocol**: Every technical debt or feature request MUST be registered as a `bead`. Use `bd create` to initialize new tasks and reference the `bead ID` in code comments. Use `bd search` to retrieve context.

6. **UI Atomic Design**: Structure frontend components strictly by Atoms, Molecules, Organisms, Templates, and Pages.
7. **Visual Architecture Law**: All architectural representations MUST follow the **AVAS** (Agentic Visual Architecture Standard).
   - **Passive Law**: Diagrams must always use subgraphs and labeled connections.
   - **Active Capability**: For diagram generation, use the `diagram-creator` skill.

## AI Assistant Ecosystem
You are supported by a suite of specialized master sub-agents:
- **`@lead` (Lead Architect)**: Designs system architecture, defines contracts, and manages the high-level roadmap.
- **`@builder` (Master Implementation)**: Full-stack execution engine. Responsible for logic, UI components, and infra.
- **`@auditor` (Quality Gatekeeper)**: Enforces visual parity, engineering standards, and testing compliance.
- **`@memory-manager`**: Specialized in distilling context and maintaining the Beads memory.
- **`@ui-designer`**: Focuses on high-fidelity UX/UI and Atomic Design tokens.
- **`@commander`**: High-level orchestrator for autonomous coding cycles.
- **`@scribe`**: Specialized in technical history and knowledge distillation.
- **`@diagram-agent`**: Expert for generating AVAS-compliant visual maps.

## Persona Constraints
- **Mandatory Skills**: Every persona MUST be initialized with relevant skills (e.g., `@builder` -> `frontend-design`, `@lead` -> `codetographer`).
- **No Reasoning Skips**: Agents must never assume infrastructure exists; they must verify via `builder` or `lead`.
- **Handoff Integrity**: Every delegation must include the current `Bead ID` and a link to the relevant spec file.

## Core Meta-Skills
You are equipped to evolve your own capabilities:
- **`rule-creator`**: Create and maintain high-signal architectural and operational rules.
- **`skill-creator`**: Build modular capabilities, workflows, and automated scripts.
- **`diagram-creator`**: Generate multi-level (C4-style) architectural maps.
- **`code-gap-reviewer`**: Perform specialized audits and architectural drift analysis.
- **`session-handover`**: Perform a "Session Wrap-up" to ensure context continuity.

## Initialization & Operational Logic
- **HAL Synchronization**: At the start of every session, the agent MUST run `scripts/hal-sync.ps1` to resolve path variables (ROOT, AGENTS, DOCS, TRACK) and populate the environment context.
- **Intelligence Sync**: Verify that **Codanna** and **Cognee** are indexed. Run `codanna index .` and `uv run scripts/cognee/indexer.py` if code has changed significantly outside of the AI session.
- **Specialized Workflows**: Utilize the domain-specific workflows in `.agents/workflows/` for **cognee**, **beads**, and **codanna** to ensure task-specific consistency.
- **Context Injection**: Before starting a task, run `bd ready` or `bd list --status open` to ensure your internal state matches the workspace.
- **Rules Persistence**: Every request you handle must be evaluated against the files in `.agents/rules/`.
- **Codetographer Mode**: When asked to "map" or "visualize," activate `diagram-creator` or delegate to `@diagram-agent`.

## Golden Standards
- **Contract -> Interface -> Mock -> Impl**: Never write logic without defining the boundary first.
- **Abstractions over Concretes**: Never hardcode infrastructure inside domain files.
- **100% Transparency**: Never leave silent placeholders. If it's missing, it gets a bead (`bd create`).

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
