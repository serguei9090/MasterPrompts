# Master AI Context: Morphic AI Engineering Framework

Welcome to the Morphic AI Engineering Framework. This workspace is governed by high-performance software engineering laws.

## 🗺️ Rule-Map (The Laws of Physics)
- **Architecture**: `.agents/rules/System/Architecture.md` (Hexagonal + Ports/Adapters)
- **Tracking**: `.agents/rules/System/ProjectTracking.md` (Beads-First Protocol)
- **Software Standards**: `.agents/rules/System/SoftwareStandards.md` (DRY, KISS, SOLID)
- **Quality/Beads**: `.agents/rules/System/CodeQuality.md` (Beads Protocol + Atomic Design)
- **Automation**: `.agents/rules/Automation/AutonomousExecution.md` (Sprint Mode + Loop Protocol)
- **Expert Practices**: `.agents/rules/Specialized/AIExpertPractices.md` (Mnemonic Anchors + Verification)
- **Visual Law**: `.agents/rules/Specialized/VisualArchitecture.md` (AVAS Visualization)

## Core Mandates

1. **Spec-Driven Development**: Always define contracts and interfaces before writing implementations. Follow the Ports & Adapters (Hexagonal) architecture to ensure Separation of Concerns.
2. **Hybrid Memory Architecture**: This project uses a multi-layered intelligence stack:
   - **Codanna (Physical)**: Primary engine for deep code analysis (symbols, call graphs, impact).
   - **Cognee (Semantic)**: Graph-based memory for rationale, architectural decisions, and lessons learned.
   - **context7 (External)**: Real-time source of truth for third-party library documentation.
   - **Beads (Operational)**: Authoritative state and task tracker (bd).
   - **Native (Empirical)**: Final verification via `grep_search` and manual file reading.

3. **Software Excellence**: Strictly adhere to **DRY, KISS, YAGNI, and SOLID** principles. Favor composition over inheritance and pure functions where possible.
4. **Beads Protocol**: Every technical debt or feature request MUST be registered as a `bead`. Use `bd create` to initialize new tasks and reference the `bead ID` in code comments. Use `bd search` to retrieve context.

5. **UI Atomic Design**: Structure frontend components strictly by Atoms, Molecules, Organisms, Templates, and Pages.
6. **Visual Architecture Law**: All architectural representations MUST follow the **AVAS** (Agentic Visual Architecture Standard).
   - **Passive Law**: Diagrams must always use subgraphs and labeled connections.
   - **Active Capability**: For diagram generation, use the `diagram-creator` skill.

## AI Assistant Ecosystem
You are supported by a suite of specialized sub-agents:
- **`@brain` (Lead Architect)**: Designs system architecture, defines contracts, and manages the high-level roadmap.
- **`@memory-manager`**: Specialized in distilling context, managing architectural decisions, and maintaining the Beads memory.
- **`@qa` (Quality Assurance)**: Enforces testing standards, executes audits, and verifies bug fixes.
- **`@api-specialist`**: Expert in JSON-RPC contracts, REST/GraphQL design, and backend logic.
- **`@ui-designer`**: Focuses on UX/UI, accessibility, and high-fidelity component design.
- **`@theme-expert`**: Specializes in design tokens, CSS architecture, and visual identity (Tailwind/Vanilla).
- **`@arch-audit` (Architecture Audit)**: Performs deep architectural audits, verifies structural integrity, and ensures AVAS compliance.
- **`@doc-agent`**: Automates documentation updates based on code changes.
- **`@diagram-agent`**: Expert architect sub-agent for generating AVAS-compliant visual maps.
- **`@lint-agent`**: Enforces code style and documentation consistency.
- **`@reviewer-agent`**: Performs deep architectural audits and code reviews.

## Core Meta-Skills
You are equipped to evolve your own capabilities:
- **`rule-creator`**: Create and maintain high-signal architectural and operational rules.
- **`skill-creator`**: Build modular capabilities, workflows, and automated scripts.
- **`diagram-creator`**: Generate multi-level (C4-style) architectural maps.
- **`code-gap-reviewer`**: Perform specialized audits and architectural drift analysis.
- **`session-handover`**: Perform a "Session Wrap-up" to ensure context continuity.

## Initialization & Operational Logic
- **HAL Synchronization**: At the start of every session, the agent MUST run `scripts/hal-sync.ps1` to resolve path variables (ROOT, AGENTS, DOCS, TRACK) and populate the environment context.
- **Intelligence Sync**: Verify that **Codanna** and **Cognee** are indexed. Run `codanna index .` and `scripts/cognee_indexer.py` if code has changed significantly outside of the AI session.
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
