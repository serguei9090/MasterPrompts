---
description: "DocsReview - Local-First Documentation Review Workflow. Use this to verify API syntax and patterns before coding."
---
# DocsReview: Local-First Documentation Review

This workflow ensures that all implementations are based on official documentation rather than model assumptions.

## 🎯 Objective
Retrieve, install, and distill library-specific documentation using the `context` MCP server.

## 🛠️ Tools
- `mcp_context_search_packages`: Find the correct package.
- `mcp_context_download_package`: Install the package if missing.
- `mcp_context_get_docs`: Extract specific API details.

## 🔄 Execution Steps

### 1. Discovery
**Assume Role:** `@brain`
- Identify all third-party libraries or frameworks involved in the task.
- For each library, run `mcp_context_search_packages(name="<library>")`.

### 2. Synchronization
**Assume Role:** `@memory-manager`
- If the required version is not present, run `mcp_context_download_package(name="<library>", registry="<npm/pip/cargo/go>", version="<version>")`.

### 3. Extraction
**Assume Role:** `@api-specialist`
- For each critical component/method identified in the plan, run `mcp_context_get_docs(library="<name>@<version>", topic="<method/pattern>")`.
- Extract the exact syntax, parameter types, and example usage.

### 4. Distillation
**Assume Role:** `@doc-agent`
- Save the findings to `docs/track/specs/docs_<bead_id>.md`.
- Reference this file in the main implementation spec.

### 5. Web Fallback (context7)
**Assume Role:** `@brain`
- If local documentation (Steps 1-3) is missing, outdated, or insufficient to solve the task:
    - Use `mcp_context7_resolve-library-id(libraryName="<name>", query="<task context>")`.
    - Use `mcp_context7_query-docs(libraryId="<id>", query="<specific technical question>")`.
    - Distill the web findings into the documentation spec.

## 🛑 Exit Criteria
- All non-trivial library APIs have been verified against the `context` documentation.
- The implementation plan references the specific documentation file.
