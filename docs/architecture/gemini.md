Assume Role: Orchestra Hub (@scribe)

# 📂 docs/architecture Context

## 🎯 Purpose
This folder serves as the **Blueprinting & Theoretical Layer** of the Morphic framework. It houses the high-level technical specifications, architectural diagrams, and foundational concepts that define the framework's "Soul." It is the source of truth for the system's design patterns, including the **Triad** (Antigravity, Gemini, Jules), Hexagonal boundaries, and the **HAL** (Hardware Abstraction Layer).

## 🏗️ Architectural Role
**Conceptual & Design Layer**. This directory documents the "why" and "how" of the entire framework's structure. It defines the relationships between the local orchestrator, the sub-agents, and the remote execution engines.

## 🔑 Key Files & Exports
- **`Technical_Specification.md`**: The master design document defining functional/non-functional requirements and the core tech stack.
- **`triad.md`**: Visual and conceptual breakdown of the framework's primary personas and their interaction loops.
- **`communication.md`**: Protocols for inter-agent and inter-layer communication (e.g., JSON-RPC, message schemas).
- **`diagrams.md`**: Index of architectural diagrams following the AVAS standard.
- **`layers/`**: detailed documentation of the individual architectural layers (Domain, Infrastructure, UI).
- **`gemini.md`**: specific architectural notes for the Gemini CLI integration.

## 🛠️ Operational Logic
- **Visual Law**: All diagrams within this folder must adhere to the **AVAS** (Agentic Visual Architecture Standard) and should be generated/updated via the `diagram-creator` skill.
- **Spec-First Alignment**: Before implementation, the AI must ensure that new features align with the principles documented here.
- **HAL Integration**: This directory defines the hardware-agnostic nature of the framework, ensuring portability via `agents.yaml` and `hal-check.ps1`.

## 📜 Local Rules & Standards
- **Architectural Fidelity**: No implementation may deviate from the core principles (Hexagonal, SoC, Interface-First) without an update to these specifications.
- **Visual Signal**: Diagrams must prioritize data flow and state persistence over trivial implementation details.

## 🔗 Dependencies
- **Internal**: Governs the structure of `.agents/rules` and `.agents/skills`. Referenced by `AGENTS.md` and `GEMINI.md` in the root.
- **External**: Provides the theoretical basis for interaction with `google-adk`, `Jules`, and ecosystem tools.
