---
description: Automated Codanna Indexing Pipeline
---

# Codanna AutoIndex Workflow

This workflow ensures the Codanna index is initialized and synchronized with the latest code and documentation.

## Steps

### 1. Environment Verification
Check if Codanna is available and initialized.
```powershell
// turbo
codanna --version
if (!(Test-Path .codanna)) { codanna init }
```

### 2. Collection Management
Ensure the `docs` and `root` collections are registered.
```powershell
// turbo
codanna documents add-collection docs docs/
codanna documents add-collection root .
```

### 3. Synchronization
Execute a full re-index of both code symbols and document embeddings.
```powershell
// turbo
codanna index .
codanna documents index
```

### 4. Verification
Verify the index status.
```powershell
// turbo
codanna mcp get_index_info --json
```

## Summary
The project is now fully indexed and ready for deep architectural analysis and semantic search.
