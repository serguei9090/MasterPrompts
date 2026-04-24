Assume Role: Orchestra Hub (@scribe)

# 📂 docs/track Context

## 🎯 Purpose
This folder serves as the **Long-Term Memory** and **Operational State** layer of the project. It tracks the evolution of the framework through roadmaps, task statuses, performance telemetry, and technical specifications. It is the central hub for ensuring that the AI remains aligned with the project's goals and architectural standards across multiple sessions and agents.

## 🏗️ Architectural Role
**Persistence & State Layer (Documentation)**. This directory records the "what" and "how" of the project's execution. It provides the AI with the context necessary to resume tasks, verify implementations against specifications, and learn from past failures.

## 🔑 Key Files & Exports
- **`TODO.md`**: The primary source of truth for the project's roadmap and task queue. Uses the `TODO(ID)` protocol.
- **`JULES.md`**: specialized tracker for autonomous, asynchronous remote tasks managed by the Jules agent.
- **`specs/`**: Contains the technical blueprints and detailed requirements for every task identified in `TODO.md`.
- **`audits/`**: Records the results of structural and quality audits (e.g., `/project-audit` outputs).
- **`LessonsLearned.md`**: A recursive feedback loop documenting root causes, resolutions, and preventative measures to improve the framework's rules and workflows.
- **`telemetry.csv`**: Structured data capturing execution metrics and performance trends.

## 🛠️ Operational Logic
- **Task Lifecycle**: Tasks are initiated in `TODO.md`, specified in `specs/`, and validated before being marked as `[x]`.
- **Memory Sync**: The AI reads these files at the start of every session (the "Boot Sequence") to align its internal state with the project's reality.
- **Feedback Loop**: Insights from `LessonsLearned.md` are used to "Self-Evolve" the contents of the `.agents/` directory.

## 📜 Local Rules & Standards
- **ID Protocol**: Every task and spec MUST use a unique ID (e.g., `CORE_001`, `FEAT_002`).
- **Parity**: The state in `TODO.md` must accurately reflect the actual state of the codebase and `JULES.md`.
- **Mandatory Updating**: The AI must update relevant tracking files (TODO, LessonsLearned) upon completion of significant tasks.

## 🔗 Dependencies
- **Internal**: Fed by `.agents/workflows` and verified against `.agents/rules`. Linked to `conductor/` for active execution tracking.
- **External**: serves as the evidentiary record for the user and external collaborators.
