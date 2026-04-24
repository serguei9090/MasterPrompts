Assume Role: Orchestra Hub (@scribe)

# 📂 .agents/rules Context

## 🎯 Purpose
This folder serves as the **Governance Layer** and "Knowledge Base" for the project. it contains the foundational "Laws of Physics" that govern both the AI's autonomous behavior and the structural integrity of the codebase. These rules ensure consistency across architecture, quality, security, and specialized protocols.

## 🏗️ Architectural Role
**Policy & Governance Layer**. This directory dictates the standards for all other layers (Domain, Infrastructure, UI). It functions as the source of truth for the AI's decision-making process, ensuring every turn aligns with the project's long-term health and architectural vision.

## 🔑 Key Files & Exports
- **`Architecture/`**: Mandates Hexagonal (Ports & Adapters), Interface-First design, and strict Separation of Concerns.
- **`Automation/`**: Defines the **Autonomous Execution Protocol**, including the recursive loop and the 3-Strike Incident Breaker for self-healing.
- **`CodeQuality/`**: Enforces the use of `Biome` for linting/formatting and `Lefthook` for pre-commit orchestration.
- **`System/`**: Foundational standards for software development, project tracking, and architecture documentation.
- **`Specialized/`**: niche protocols such as **AVAS** (Agentic Visual Architecture Standard) for diagrams and integration with tools like the **Jules CLI**.
- **`Testing/`**: standards for the Master Agent Ops Mode and Protocol Retrofitting.

## 🛠️ Operational Logic
- **Ingestion**: Rules are triggered either by `always_on` (foundational mandates) or `model_decision` (context-dependent guidelines).
- **Enforcement**: The AI is expected to validate its actions against these rules during the **Research** and **Validation** phases of every task.
- **Error Recovery**: The `Automation/SelfCorrection.md` and `Automation/AutonomousExecution.md` files define how the AI should react to failures.

## 📜 Local Rules & Standards
- **Assume Role Header**: Every file created or edited MUST start with `Assume Role: <Persona> (@handle)`.
- **Semantic Commenting**: Functions must include purpose and architectural rationale; non-trivial variables must explain **WHY** they exist.
- **TODO(ID) Protocol**: technical debt must follow the strict `// TODO(ID): [WHAT] ... [WHY] ... [EXPECTATION] ... [CONTEXT] See docs/track/specs/ID.md` syntax.
- **Conventional Commits**: All git commits must follow the conventional commit standard.

## 🔗 Dependencies
- **Internal**: Closely linked to `docs/track/` (for TODOs and specs) and `.gemini/agents/` (defining the personas that execute these rules).
- **External**: Refers to third-party standards and tools: `Biome`, `Lefthook`, `Gitleaks`, `Conventional Commits`, and `Semantic Versioning 2.0.0`.
