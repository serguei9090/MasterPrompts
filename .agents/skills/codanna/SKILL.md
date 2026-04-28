# Codanna Skill: High-Performance Indexing & Search

This skill provides a reliable, serverless interface to Codanna for deep codebase analysis and document search. It bypasses the need for a persistent MCP server by executing tools directly via the CLI.

## 🛠️ Core Capabilities
- **Serverless MCP**: Execute standard MCP tools (find_symbol, analyze_impact, search_documents) directly via `codanna mcp`.
- **Hybrid Search**: Perform both symbol-based code search and semantic document search.
- **Impact Analysis**: Generate full dependency graphs and impact reports for architectural changes.
- **JSON-Ready**: All outputs are formatted as JSON for precise agent parsing.

## 📋 Tool Reference (CLI Mapping)

Use the following command pattern:
`codanna mcp <tool_name> --args '<json_args>' --json`

| MCP Tool | Description | Common Arguments |
| :--- | :--- | :--- |
| `analyze_impact` | Full dependency graph and usage analysis. | `{"name": "SymbolName"}` |
| `find_symbol` | Find exact symbol definition and metadata. | `{"name": "SymbolName"}` |
| `search_symbols` | Fuzzy full-text search across codebase. | `{"query": "term", "limit": 10}` |
| `search_documents` | Semantic search across indexed docs. | `{"query": "natural language", "limit": 5}` |
| `get_calls` | List functions called by a symbol. | `{"symbol_id": 123}` |
| `find_callers` | List functions that call a symbol. | `{"name": "FunctionName"}` |
| `get_index_info` | Stats on current index state. | `{}` |

## 🚀 Workflows

### 1. Initialization & Indexing
Before any analysis, ensure the index is warm:
```powershell
# Initialize if needed
codanna init

# Add document collections
codanna documents add-collection docs docs/

# Build code and document indices
codanna index .
codanna documents index
```

### 2. Surgical Impact Analysis
When planning a refactor:
1. Run `codanna mcp analyze_impact --args '{"name": "TargetSymbol"}' --json`.
2. Parse the `data.relationships` to identify all affected files.
3. Verify with `find_callers` if specific invocation logic is needed.

### 3. Documentation Search (RAG)
When researching framework patterns:
1. Run `codanna mcp search_documents --args '{"query": "How to implement a new skill", "limit": 3}' --json`.
2. Extract the `content_preview` from the JSON response to understand established patterns.

## ⚠️ Guardrails
- **Sync Required**: If you modify code, run `codanna index .` to refresh the symbol graph.
- **JSON Parsing**: Always use the `--json` flag to ensure output is machine-readable.
- **Relative Paths**: Prefer relative paths for document collections to maintain project portability.
