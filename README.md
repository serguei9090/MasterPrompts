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

This framework employs a state-of-the-art 5-layer memory stack to provide agents with unprecedented context density and reasoning reliability.

### 0. Reasoning Engine (Sequential Thinking)
*   **Role**: Internal Planning & Verification.
*   **Function**: A dynamic thought process that allows the agent to branch, backtrack, and verify hypotheses before executing terminal commands.

### 1. Codanna (Physical Layer)
*   **Role**: Codebase Intelligence & RAG.
*   **Function**: Performs deep symbol analysis, impact mapping, and provides semantic search over internal documentation and code comments.
*   **Tool**: `codanna mcp` CLI.

### 2. Cognee (Semantic Layer)
*   **Role**: Conceptual Memory.
*   **Function**: Stores architectural rationale, technical decisions (ADRs), and distills "Lessons Learned" into a persistent knowledge graph.
*   **Tool**: `cognee_memory.py`.

### 3. context (Local Layer)
*   **Role**: Installed Library Documentation.
*   **Function**: Provides instant, offline access to version-specific documentation for packages installed via `download_package`.
*   **Tool**: `context` MCP.

### 4. context7 (External Layer)
*   **Role**: Living Documentation.
*   **Function**: Retrieves up-to-date API syntax and patterns for third-party libraries directly from the web.
*   **Tool**: `context7` MCP.

### 5. Beads (Operational Layer)
*   **Role**: Task & Roadmap State.
*   **Function**: Authoritative source for issue tracking, session handoffs, and operational history using a graph-based versioned database (Dolt).
*   **Tool**: `bd` (Beads).

## ⚠️ Concurrency & Multi-Process Limits

In local environments using the default file-based storage, the **Morphic Intelligence Stack** (specifically Cognee/KůzuDB) uses strict file-based locking. 

### Local Concurrency Law
*   **Sequential Access Only**: You MUST run Cognee operations (`recall`, `index`, `trace`) sequentially. Running multiple memory-related scripts in different terminal windows simultaneously will cause `IO exception: Could not set lock on file` errors.
*   **The Rule**: This is enforced via the **Local Concurrency Law** in `.agents/rules/System/IntelligenceStack.md`.

### Scaling for Multi-User/Multi-Agent Support
If your use case requires multiple processes or agents to read/write memory simultaneously:
1.  **Switch to Server-Based DBs**: Refer to the [Cognee Documentation](https://docs.cognee.ai) to configure **PostgreSQL** (Relational) and **Neo4j** or **Qdrant** (Graph/Vector) as your providers.
2.  **Update Governance**: You must modify the **Local Concurrency Law** in `.agents/rules/System/IntelligenceStack.md` once your environment is upgraded to a server-based architecture.
3.  **Alternative (Sidecar)**: Use a single "Sidecar" API process to act as the sole database owner, allowing other clients to connect via HTTP without hitting file-system locks.

## 📦 Installing the Framework into a Project

When you download the Morphic Framework bundle (`morphic_v0.10.7.tar.gz`), extract it into your target project directory and run the single Python installer. 

*(Note: This README is bundled as `MorphicReadme.md` to avoid overwriting your project's existing README).*

```bash
# 1. Run the unified installer
python install.py

# The installer handles both:
# - Phase 1: Deploying framework files to your project
# - Phase 2: Bootstrapping tools (Dolt, Node, Bun, Python uv, Beads, Codanna, Cognee)

# 2. Fill in your API keys in the generated .env file
# 3. Open your AI assistant and run the /init workflow to finish setup
```

## 🚀 Usage for Developers (Framework Maintainers)

### 1. Build the Framework Bundle
To package the framework for distribution:
```powershell
uv run .\BuildScripts\build_morphic.py
```

### 2. Synchronize Environment (HAL)
Before contributing to rules or workflows, run the sync script:
```powershell
# Windows
.\scripts\hal-sync.ps1
# Linux/macOS
bash ./scripts/hal-sync.sh
```

## 📜 Repository Standards

To maintain the integrity of the framework, all edits to this repo must follow these rules:

1. **Rule Parity:** Any change to a rule in `.agents/rules/` must be reflected in the relevant `AGENTS.md` or `GEMINI.md` summary.
2. **Persona Consistency:** Personas must follow the YAML frontmatter standard defined in the global protocols.
3. **Workflow Documentation:** Every new workflow must include a `description` in its frontmatter and a clear "Success Criteria" list.

---

*Built with passion by the Deepmind Team. Morphic is the future of Agentic Coding.*
