# Morphic AI Engineering Framework: Core Governance Hub

![Morphic Header](file:///C:/Users/ASCC/.gemini/antigravity/brain/9dce4e39-b2fb-4296-8aab-1d06d22b3a13/morphic_header_logo_1777250484085.png)

> **The Source of Truth for Agentic Intelligence.**
> This repository contains the foundational rules, personas, and workflows that govern the Morphic AI Engineering ecosystem.

---

## 🏗️ Project Role: The Governance Layer

Unlike application repositories, **MasterPrompts** is a meta-repository. It functions as the "brain" and "instruction manual" for AI agents operating within the framework.

- **Foundational Rules:** The `.agents/rules/` directory defines the "Laws of Physics" for code quality, architecture, and security.
- **Specialized Personas:** The `.gemini/agents/` directory houses 19+ unique AI expert profiles (Architects, QA, DevSecOps).
- **Automated Workflows:** The `.agents/workflows/` directory contains executable markdown sequences for complex tasks like `/auto-cycle` and `/readme-gen`.

## 🤖 AI Ecosystem Overview

This hub is designed to be ingested by **Antigravity** and other Gemini-compatible agents to ensure consistent behavior across different codebases.

### Key Components
- **AGENTS.md:** The high-level manifest of framework mandates and core personas.
- **GEMINI.md:** Operational overview and developer onboarding for the framework itself.
- **agents.yaml:** The Hardware Abstraction Layer (HAL) defining tool aliases and project paths.

## 🛠️ Actual Tech Stack

This project is a **Logic & Metadata Engine** and does not contain application source code.

| Category | Component | Description |
| :--- | :--- | :--- |
| **Governance** | Markdown (.md) | Structured rules and agent personas. |
| **Config** | YAML / TOML | HAL definitions and custom CLI commands. |
| **Orchestration** | Gemini CLI | The execution engine for the workflows. |
| **Automation** | PowerShell (.ps1) | Environment synchronization and path resolution. |
| **Tooling (Aliases)** | Bun / UV | Standardized runtime managers for the ecosystem. |

## 🧠 Multi-Layer Memory Architecture

This framework employs a state-of-the-art 4-layer memory stack to provide agents with unprecedented context density and reasoning reliability.

### 1. Codanna (Physical Layer)
*   **Role**: Codebase Intelligence & RAG.
*   **Function**: Performs deep symbol analysis, impact mapping, and provides semantic search over internal documentation and code comments.
*   **Tool**: `codanna mcp` CLI.

### 2. Cognee (Semantic Layer)
*   **Role**: Conceptual Memory.
*   **Function**: Stores architectural rationale, technical decisions (ADRs), and distills "Lessons Learned" into a persistent knowledge graph.
*   **Tool**: `cognee_memory.py`.

### 3. context7 (External Layer)
*   **Role**: Living Documentation.
*   **Function**: Retrieves up-to-date API syntax and patterns for third-party libraries directly from the web.
*   **Tool**: `context7` MCP.

### 4. Beads (Operational Layer)
*   **Role**: Task & Roadmap State.
*   **Function**: Authoritative source for issue tracking, session handoffs, and operational history using a graph-based versioned database (Dolt).
*   **Tool**: `bd` (Beads).

## 🚀 Usage for Developers

### 1. Synchronize Environment
Before contributing to the rules or workflows, run the synchronization script:

```powershell
./scripts/hal-sync.ps1
```

### 2. Testing Workflows
You can test the workflows contained here by invoking them via the Gemini CLI:

```powershell
gemini -y -p "@/readme-gen"
```

## 📜 Repository Standards

To maintain the integrity of the framework, all edits to this repo must follow these rules:

1. **Rule Parity:** Any change to a rule in `.agents/rules/` must be reflected in the relevant `AGENTS.md` or `GEMINI.md` summary.
2. **Persona Consistency:** Personas must follow the YAML frontmatter standard defined in the global protocols.
3. **Workflow Documentation:** Every new workflow must include a `description` in its frontmatter and a clear "Success Criteria" list.

---

*Built with passion by the Deepmind Team. Morphic is the future of Agentic Coding.*
