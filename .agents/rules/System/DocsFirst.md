# Docs-First: Zero-Guesswork Implementation Law

To prevent architectural drift and model hallucination, all implementations involving external libraries MUST be preceded by a documentation review.

## ⚖️ Mandate
**Never Guess the API.** Before writing any code (Phase 2 of Smith SDLC), the agent MUST verify the syntax, version-specific features, and best practices using the `DocsReview` workflow.

## 🎯 Trigger Conditions
- **New Dependency**: When a new library is added to the project.
- **Complex API**: When using non-trivial features of existing libraries (e.g., React Hooks, DuckDB cursors, ADK Runners).
- **Ambiguity**: Whenever the agent is unsure of the exact parameter signatures or return types.

## 🛠️ Operational Logic
1. **Identify**: In Phase 1 (PM/Brain), identify all libraries requiring verification.
2. **Execute (Local First)**: Trigger the `/DocsReview` workflow using the `context` MCP server.
3. **Fallback (Web Second)**: If local docs are missing or insufficient, use `context7` to perform a live web search/research.
4. **Reference**: Include links to the distilled docs in the implementation spec (`docs/track/specs/`).
5. **Verify**: During Phase 5 (Audit), the `@arch-audit` persona must verify that the code matches the documented patterns.

## 🛑 Enforcement
- Implementations found to be based on hallucinated APIs will be rejected by `@qa` or `@arch-audit` and forced back to Phase 1 for a documentation sync.
