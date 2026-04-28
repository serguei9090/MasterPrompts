# Cognee Installation & Configuration Guide

This guide details the mandatory steps to install and configure Cognee as the intelligence layer for the Morphic framework.

## 📋 Prerequisites
- **Python 3.10+**
- **uv** (Recommended Python package manager)

## 🛠️ Local Installation Protocol

Follow these steps to set up a project-isolated Cognee environment:

### 1. Initialize Virtual Environment
Create a local `.venv` directory to keep dependencies isolated:
```powershell
uv venv
```

### 2. Install Cognee
You can install Cognee using the `uv` project management command (if `pyproject.toml` exists) or directly via `uv pip`:

**Option A: Project Management (Preferred)**
```powershell
uv add cognee
```

**Option B: Manual Pipe Installation**
```powershell
uv pip install cognee
```

### 3. Verify Installation
Ensure the `cognee-cli` is available:
```powershell
uv run cognee-cli --version
```

## ⚙️ Environment Configuration (.env)

Cognee requires specific environment variables to connect to your LLM and Embedding providers. Create or update your `.env` file with the following:

```env
# Cognee Configuration
LLM_PROVIDER="custom"
LLM_MODEL="lm_studio/google/gemma-4-e2b"
LLM_ENDPOINT="http://127.0.0.1:1234/v1"
LLM_API_KEY="not-needed"
LLM_INSTRUCTOR_MODE="json_schema_mode"

# Embedding Configuration
EMBEDDING_PROVIDER="custom"
EMBEDDING_MODEL="lm_studio/text-embedding-nomic-embed-text-v1.5"
EMBEDDING_ENDPOINT="http://127.0.0.1:1234/v1"
EMBEDDING_API_KEY="."
EMBEDDING_DIMENSIONS="768"

# System Settings
COGNEE_SKIP_CONNECTION_TEST="False"
SYSTEM_ROOT_DIRECTORY="./.cognee/system"
DATA_ROOT_DIRECTORY="./.cognee/data"
LITELLM_DROP_PARAMS="True"
```

> [!IMPORTANT]
> Ensure `SYSTEM_ROOT_DIRECTORY` and `DATA_ROOT_DIRECTORY` point to directories inside your project (like `./.cognee`) to maintain project isolation. Or you can poin to a main folder and isolate them using dataset names. I would suggest create a main folder called `Cognee` in `...MasterIndexDB/Cognee` and create a dataset for each project.

## 🚀 Initializing the Knowledge Graph

Once installed and configured, perform the initial full index:

```powershell
uv run python scripts/cognee_indexer.py --full
```

This will:
1.  Read your `.cogneeignore` and `.gitignore`.
2.  Index all valid project files into a dataset named after your project root.
3.  Build the initial knowledge graph for recall operations.
