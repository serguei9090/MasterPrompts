# Morphic AI Engineering Framework (v0.10.7)

Welcome to the **Morphic AI Engineering Framework**. This workspace is a high-performance software engineering environment governed by strict architectural laws and supported by a specialized ecosystem of AI sub-agents.

## 🗺️ Project Overview
This project is an **AI-Native Engineering Framework** designed for autonomous and semi-autonomous software development. It leverages a "Sidecar" architecture, Hexagonal (Ports & Adapters) principles, and a robust suite of rules to ensure structural integrity and operational excellence.

- **Type:** Meta-Framework / Agent Orchestration System
- **Core Philosophy:** Spec-Driven Development, DESIGN.md-First Governance, and Visual Law (AVAS).
- **Architecture:** Hexagonal (Ports & Adapters) strictly separating domain logic from infrastructure.

## 🚀 Getting Started

### Initializing the Agent
Before starting any work, you MUST synchronize your internal state with the workspace:
1.  **Read `AGENTS.md`**: This is your primary Source of Truth for framework mandates.
2.  **Sync Roadmap**: Run `bd ready` to align your task queue with the current project status (Beads protocol).
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

### 2. DESIGN.md-First Governance
All UI changes must be documented in `DESIGN.md` before code implementation. Hardcoded values are forbidden; use design tokens only.

### 3. Visual Architecture (AVAS)
All diagrams must adhere to the **Agentic Visual Architecture Standard**:
-   Use Mermaid.js with clear subgraphs and labeled connections.
-   Activate the `diagram-creator` skill for compliant generation.

### 4. Docs-First Standard (Local Review)
Never implement code for external libraries based on assumptions:
1.  **Search**: Use `search_packages` to find the correct library documentation.
2.  **Sync**: Ensure the package is available via `download_package`.
3.  **Verify**: Extract specific patterns using `get_docs`.
4.  **Codanna Research**: Use `codanna mcp search_documents` to find project-specific patterns and architectural mandates.
5.  **Web Fallback (context7)**: If local docs are missing or insufficient, use `context7` (Resolve -> Query) to perform a live web search/research for the latest API documentation.
6.  **Reference**: Document the verified API in the implementation spec.

## 🤖 AI Assistant Ecosystem
You are one part of a specialized multi-agent system. Delegate tasks to maintain focus:
-   **`@brain`**: Lead Architect & PM (System design & roadmap).
-   **`@qa`**: Quality Assurance (Testing & bug verification).
-   **`@ui-auditor`**: Enforces visual parity between DESIGN.md and implementation.
-   **`@api-specialist`**: Backend logic & JSON-RPC contracts.
-   **`@ui-designer`**: Frontend UX/UI & Atomic Design.
-   **`@arch-audit`**: Structural verification & AVAS compliance.

## 📦 Distribution & Shipping (v0.10.7)

To prepare this framework for a new project or to ship it as a standalone engine, follow the **v0.10.7 Automated Build Protocol**:

### 1. Automated Build
The framework is packaged into a single distribution archive using the builder script. This ensures all personas, rules, and scripts are synchronized.
```powershell
python scripts/build_morphic.py
```
*   **Artifact**: `dist/morphic_v0.10.7.tar.gz`

### 2. Intelligent Installation
Deployment into a new project is handled by the intelligent installer. It prevents accidental overwrites and manages environment collisions.
```powershell
python scripts/install_morphic.py
```
*   **Protection**: If core files (like `AGENTS.md` or `.env.example`) already exist, the installer skips them and generates a `MERGE_REQUIRED.md` report.
*   **AI-Assisted Merging**: The report includes pre-configured AI prompts to help you surgically merge framework mandates with your existing project identity.

### 3. Distribution Policy
*   **Version Control**: Recommended for continuous updates. Ensure you run the installer after pulling major framework updates.
*   **Safe Handoff**: NEVER force overwrite governance files manually. Always use the installer to identify conflicts.

## 📂 Directory Structure
-   `.agents/rules/`: Foundational "Laws of Physics" for the AI.
-   `.gemini/agents/`: Sub-agent configurations and personas.
-   `docs/track/`: Roadmap, specs, and telemetry for the current sprint.
-   `scripts/`: Utility scripts for builds, indexing, and HAL sync.

---
*This file is generated and maintained as a living instructional context for the Morphic AI Engineering Framework.*

---
*This file is generated and maintained as a living instructional context for the Morphic AI Engineering Framework.*
