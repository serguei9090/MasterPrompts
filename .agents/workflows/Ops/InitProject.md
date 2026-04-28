---
name: init
description: Comprehensive project initialization. Installs Beads (bd), scans the codebase to adapt personas/skills to the tech stack, populates the Beads memory, and generates project documentation.
---

# Init Project Workflow (// turbo-all)

> **Assume Role:** `@brain` (Lead Architect)

This workflow is the absolute starting point for any project. It replaces all legacy onboarding and adaptation scripts. It initializes the **Beads (bd)** system as the sole Source of Truth and adapts the AI ecosystem to the detected codebase.

## 🏁 Phase 1: Environment & Beads Setup
1.  **Install Database**: Run `winget install DoltHub.Dolt --accept-package-agreements --accept-source-agreements`
2.  **Install Beads Tracker**: Run `npm install -g @beads/bd`
3.  **Initialize Tracker**: Run `bd init`
4.  **Install Dependencies**: Run `[PKG_MANAGER] install` based on the detected lockfile (e.g., `npm`, `bun`, `uv`).
5.  **Install Cognee Intelligence**: 
    - Run `uv venv` to create a local environment.
    - Run `uv pip install cognee` or `uv add cognee` to install the intelligence layer.
    - Refer to `docs/cognee_install.md` for detailed environment setup.

## 🔍 Phase 2: Codebase Adaptation & Scanning
1.  **Scan Codebase**: Scrutinize the file system (e.g., `package.json`, `pyproject.toml`, `pubspec.yaml`) to identify the project's "Technical DNA".
2.  **Skill & Agent Adaptation**: Automatically adjust `.gemini/agents/` and `.agents/skills/` to match the local stack (e.g., swapping "React" profiles for "Flutter", or `npm` for `bun`).
3.  **Initial Cognification (Memory Build)**: # Cognee Intelligence Setup: Codebase Cognification
    # 1. Setup ignore and pre-commit logic
    Execute `/cognee-init` workflow or run manually:
    - Create `.cogneeignore` and copy `scripts/cognee_indexer.py`
    - Setup `lefthook` (run `lefthook install`)
    
    # 2. Index Documentation and Codebase (Build the Knowledge Graph)
    uv run python scripts/cognee_indexer.py --full

    # 3. Initial Intelligence Recall (Verification)
    uv run cognee-cli recall "What is the primary architecture of this project?" -d <project_name>

## 🧠 Phase 3: Population of Beads Memory
1.  **Populate Stack**: Feed the analyzed stack into the Beads memory system.
    ```bash
    bd remember "STACK: [Primary Language/Framework]"
    bd remember "RUNTIME: [Package Manager / Runner]"
    bd remember "DATABASE: [Database Tech]"
    bd remember "STANDARDS: [Project specific linting/architecture rules]"
    ```
2.  **Environment Sync**: If `.env.example` exists, copy it to `.env` and prompt the user for secrets if necessary. Ensure `SYSTEM_ROOT_DIRECTORY` and `DATA_ROOT_DIRECTORY` point to `./.cognee`.

## 📄 Phase 4: Documentation & Hybrid Memory Scaffolding
1.  **Generate `docs/STACK.md`**: Create a high-level markdown summary of the codebase, frameworks, and tools used.
2.  **Generate `docs/PROJECT_MAP.md`**: Map out the core directory structure and application architecture.
3.  **Scaffold Hybrid Memory**: Create the `docs/memory/` hierarchy (`specs`, `architecture`, `lessons`) to act as the long-form hard drive for Beads indexing.

## 🚀 Execution
Run this workflow whenever a repository is cloned or a completely new project is started.
