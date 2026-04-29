---
name: Cognee Recall
description: Queries the Cognee Knowledge Graph with auto-routing and session-awareness.
---

# Cognee Recall Workflow

Use this workflow to retrieve architectural rationale, technical patterns, or session-specific context.

## Parameters
- `query`: The question or topic to search for.
- `session`: (Optional) The Bead ID or session identifier.

## Execution Steps

1. **Perform Search**:
   If a specific session is active, pass the `--session` flag.
   ```powershell
   uv run python scripts/cognee/recall.py "How is X implemented?" --session "{{BEAD_ID}}"
   ```

2. **Analyze Results**:
   Review the graph-backed or session-cached results. Cognee will automatically pick the best search strategy (Summary, Graph, or Code).

## Best Practices
- Always provide a session ID if working on a specific task to ensure continuity.
- Be specific in the query text for better graph retrieval.
