Assume Role: Orchestra Hub (@scribe)

# 📂 scripts Context

## 🎯 Purpose
The `scripts/` directory contains standalone utility scripts and automation tools used for environment synchronization, maintenance, and framework orchestration.

## 🏗️ Architectural Role
**Infrastructure Layer (Utilities)**. These scripts provide the glue between the framework's high-level definitions (like `agents.yaml`) and the local execution environment. They are designed to be run in PowerShell.

## 🔑 Key Files & Exports
- **`hal-sync.ps1`**: PowerShell script that parses `agents.yaml` and sets environment variables for the current process. It resolves relative paths to absolute paths based on the project root.

## 🛠️ Operational Logic
- **Data Flow**: Reads configuration from `agents.yaml` in the project root.
- **State Management**: Modifies the `Process` level environment variables.
- **Concurrency**: Synchronous execution.

## 📜 Local Rules & Standards
- Scripts must be PowerShell compatible.
- Every script must start with an `Assume Role` header and a clear `Purpose` statement.
- Use `agents.yaml` as the source of truth for paths and binaries.

## 🔗 Dependencies
- **Internal**: `agents.yaml` (Project Root).
- **External**: PowerShell 5.1+ or PowerShell Core.
