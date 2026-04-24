Assume Role: Orchestra Hub (@scribe)

# 📂 .agents/workflows Context

## 🎯 Purpose
This folder contains the **Operational Layer** of the framework. It houses the "Standard Operating Procedures" (SOPs) and multi-step blueprints that guide the AI through complex, recursive, or high-stakes tasks. These workflows ensure that operations like feature implementation, hotfixes, and repository management are executed with consistent quality and architectural alignment.

## 🏗️ Architectural Role
**Orchestration Layer**. Workflows act as the "Glue" of the framework. They integrate **Rules** (governance) and **Skills** (capabilities) into cohesive, sequential processes. They provide the high-level logic for project lifecycle events and specialized agent interactions.

## 🔑 Key Folders & Blueprints
- **`Development/`**: Core task-oriented workflows.
    - `Feature.md`: End-to-end lifecycle for new capabilities.
    - `FixCycle.md`: Systematic debugging and verification.
    - `PlanningProtocol.md`: Spec-first design and boundary definition.
    - `GeminiContext.md`: Automatic generation of localized context files.
- **`Lifecycle/`**: Repository and state management.
    - `GitPush.md`: Standardized pipeline for staging, committing (Conventional Commits), and pushing.
    - `ReleasePrepare.md`: Automation for version bumps and changelog updates.
- **`Delegation/`**: Protocols for multi-agent collaboration.
    - Defines how to dispatch and sync with sub-agents like **Jules** or **AutoCode**.
- **`Quality/`**: Verification and auditing.
    - `TestCoverageExpansion.md`: procedural guides for increasing unit and integration coverage.

## 🛠️ Operational Logic
- **Persona Adoption**: Workflows typically begin with an `Assume Role` header (e.g., `@brain`, `@scribe`), focusing the AI's intent and tone.
- **Turbo Execution**: Uses `// turbo` or `// turbo-all` annotations to indicate steps that should be executed rapidly or in parallel.
- **Surgical Procedures**: Workflows often define "strikes" or "attempts" (e.g., the 3-Strike Incident Breaker) to handle failures autonomously before requesting human intervention.

## 📜 Local Rules & Standards
- **Assume Role Header**: Mandatory for all workflow-driven files.
- **Traceability**: Every workflow step must be traceable back to a tracking ID in `TODO.md` or `JULES.md`.
- **Validation-First**: No workflow is complete until validation (linting, testing, or auditing) has been successfully performed.

## 🔗 Dependencies
- **Internal**: Orchestrates the use of `.agents/rules` and `.agents/skills`. Updates state in `docs/track/` and `conductor/`.
- **External**: Relies on system-level tools like `git`, `bun`, `uv`, and `gitleaks`.
