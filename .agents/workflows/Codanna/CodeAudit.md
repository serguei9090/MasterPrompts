---
description: Deep Symbol Audit and Impact Analysis
---

# Codanna CodeAudit Workflow

This workflow performs a surgical analysis of a specific code symbol to understand its dependencies and the potential impact of changes.

## Parameters
- `SYMBOL`: The name of the function, struct, or variable to audit.

## Steps

### 1. Symbol Identification
Find the exact definition and location of the symbol.
```powershell
// turbo
codanna mcp find_symbol --args '{"name": "{{SYMBOL}}"}' --json
```

### 2. Impact Mapping
Analyze all relationships, including type usage and composition.
```powershell
// turbo
codanna mcp analyze_impact --args '{"name": "{{SYMBOL}}"}' --json
```

### 3. Usage Verification
Identify all direct call sites.
```powershell
// turbo
codanna mcp find_callers --args '{"name": "{{SYMBOL}}"}' --json
```

### 4. Semantic Context
Search for documentation related to the symbol's purpose.
```powershell
// turbo
codanna mcp search_documents --args '{"query": "Purpose and usage of {{SYMBOL}}", "limit": 3}' --json
```

## Summary
The audit provides a complete map of the symbol's footprint in the codebase, enabling safe refactoring and deep understanding.
