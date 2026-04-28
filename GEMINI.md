# Morphic AI Engineering Framework

Welcome to the **Morphic AI Engineering Framework**. This workspace is a high-performance software engineering environment governed by strict architectural laws and supported by a specialized ecosystem of AI sub-agents.

## 🗺️ Project Overview
This project is an **AI-Native Engineering Framework** designed for autonomous and semi-autonomous software development. It leverages a "Sidecar" architecture, Hexagonal (Ports & Adapters) principles, and a robust suite of rules to ensure structural integrity and operational excellence.

- **Type:** Meta-Framework / Agent Orchestration System
- **Core Philosophy:** Spec-Driven Development, Dual-Roadmap Parity, and Visual Law (AVAS).
- **Architecture:** Hexagonal (Ports & Adapters) strictly separating domain logic from infrastructure.

## 🚀 Getting Started

### Initializing the Agent
Before starting any work, you MUST synchronize your internal state with the workspace:
1.  **Read `AGENTS.md`**: This is your primary Source of Truth for framework mandates.
2.  **Sync Roadmap**: Read `docs/track/TODO.md` to align your task queue with the current project status.
3.  **Check Rules**: Familiarize yourself with the "Laws of Physics" in `.agents/rules/`.

### Core Operational Commands
- **Mapping**: Use `/map` or delegate to `@diagram-agent` to visualize architecture using the AVAS standard.
- **Auditing**: Run `/project-audit` to verify structural integrity and identify technical debt.
- **Sprint Mode**: Command `/startcycle` to initiate the **Autonomous Execution Protocol** for recursive task completion.

## 🛠️ Development Conventions

### 1. Spec-Driven Development (The Definition Path)
Never write implementation logic before defining boundaries:
1.  **Define Contract**: Specify the communication data types (e.g., Pydantic schemas).
2.  **Define Interface**: Write the abstract interface (Port) in the domain layer.
3.  **Mock Test**: Write tests against a mock implementation.
4.  **Implementation**: Build the concrete logic (Adapter).

### 2. TODO(ID) Protocol
Every piece of technical debt or pending feature must be tracked:
-   **Format**: `// TODO(ID): Description`
-   **Documentation**: Each ID must have a detail file in `docs/track/specs/<ID>.md`.

### 3. Visual Architecture (AVAS)
All diagrams must adhere to the **Agentic Visual Architecture Standard**:
-   Use Mermaid.js with clear subgraphs and labeled connections.
-   Activate the `diagram-creator` skill for compliant generation.

### 4. Docs-First Standard (Local Review)
Never implement code for external libraries based on assumptions:
1.  **Search**: Use `search_packages` to find the correct library documentation.
2.  **Sync**: Ensure the package is available via `download_package`.
3.  **Verify**: Extract specific patterns using `get_docs`.
4.  **Web Fallback (context7)**: If local docs are missing or insufficient, use `context7` (Resolve -> Query) to perform a live web search/research for the latest API documentation.
5.  **Reference**: Document the verified API in the implementation spec.

## 🤖 AI Assistant Ecosystem
You are one part of a specialized multi-agent system. Delegate tasks to maintain focus:
-   **`@brain`**: Lead Architect & PM (System design & roadmap).
-   **`@qa`**: Quality Assurance (Testing & bug verification).
-   **`@api-specialist`**: Backend logic & JSON-RPC contracts.
-   **`@ui-designer`**: Frontend UX/UI & Atomic Design.
-   **`@arch-audit`**: Structural verification & AVAS compliance.

## 📂 Directory Structure
-   `.agents/rules/`: Foundational "Laws of Physics" for the AI.
-   `.gemini/agents/`: Sub-agent configurations and personas.
-   `docs/track/`: Roadmap, specs, and telemetry for the current sprint.
-   `conductor/`: Operational plans and active execution tracking.

---
*This file is generated and maintained as a living instructional context for the Morphic AI Engineering Framework.*
