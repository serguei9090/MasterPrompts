Assume Role: Orchestra Hub (@scribe)

# 📂 scripts Context

## 🎯 Purpose
Localized utility engine for framework maintenance, automated builds, and intelligence indexing. This folder contains the operational scripts that bridge the gap between the agentic framework and the physical environment.

## 🏗️ Architectural Role
Infrastructure (Operational Scripts). These are standalone Python and PowerShell utilities used by both humans and agents to manage the project lifecycle.

## 🔑 Key Files & Exports
- **`build_morphic.py`**: The primary distribution engine. Handles versioning, exclusion logic, and packaging of the framework into a tarball.
- **`install_morphic.py`**: Intelligent installer for deploying the framework into new projects with conflict detection.
- **`cognee_indexer.py`**: Bridge for indexing the physical codebase into the Cognee semantic memory graph.
- **`cognee_memory.py`**: CLI utility for recalling rationale and technical context from the memory graph.
- **`hal-sync.ps1`**: Environment synchronization script for resolving path variables (ROOT, AGENTS, DOCS, TRACK).

## 🛠️ Operational Logic
- **Data Flow**: Scripts generally consume environment variables (via HAL) and project files to produce artifacts (dist/) or memory indices.
- **State Management**: Stateless. Rely on the filesystem and external databases (Cognee/Dolt) for persistence.
- **Concurrency**: Mostly synchronous execution for reliability.

## 📜 Local Rules & Standards
- Python scripts MUST use `uv` for dependency management.
- All scripts MUST support non-interactive execution for agent compatibility.

## 🔗 Dependencies
- **Internal**: `.agents/rules/`, `agents.yaml`.
- **External**: `uv`, `python`, `powershell`, `cognee`, `codanna`.
