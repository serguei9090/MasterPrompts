---
trigger: always_on
description: "CRITICAL: The AI must never guess or assume when real information tools are available. This rule governs when inference is allowed."
---

# Zero-Guesswork Protocol (The Anti-Hallucination Law)

**CRITICAL**: This rule is ALWAYS ON. Violating it is a protocol failure.

## 1. The Core Law: Verify Before You Act

The AI MUST NOT guess, infer, or assume facts about the codebase, libraries, or architecture when real information is available through the Intelligence Stack tools. Guessing when tools are available is a critical failure.

### When You MUST use a real tool instead of guessing:
| Situation | Forbidden Action | Required Action |
| :--- | :--- | :--- |
| Unknown function signature | Guess from memory | `codanna mcp get_calls` / `grep_search` |
| Unfamiliar library API | Assume syntax | `/DocsReview` → `context` → `context7` |
| Unknown dependency of a module | Assume it's safe to change | `codanna mcp analyze_impact` |
| Architectural rationale unknown | Assume the pattern | `uv run scripts/cognee/recall.py` |
| Task status unknown | Guess what's next | `bd ready` / `bd list --status open` |

## 2. The Allowed Inference Zone

The AI MAY reason from memory and inference ONLY in these cases:
- The user **explicitly asks** for a guess, estimate, or opinion: *"What do you think?", "Make your best guess", "Brainstorm"*.
- The tool is **confirmed unavailable** (MCP error returned) — then fall back to `/SequentialThinkingBackup` and STATE CLEARLY that you are inferring.
- The question is about **general software patterns** (not project-specific code).

## 3. The "I Don't Know" Protocol

When information is needed but tools are failing or unavailable:
1. **State it clearly**: "I cannot verify this without the tool. Here is what I infer, which may be incorrect:"
2. **Label the inference**: Prefix any unverified statement with `[INFERRED]`.
3. **Flag for verification**: Create a `bd create "Verify: [topic]"` task immediately.
4. **Never commit inferred code**: Do not `git push` or `bd close` a task where a critical architectural assumption was not verified.

## 4. The No-Silent-Placeholder Law

The AI MUST NEVER:
- Write `# TODO: implement this later` without creating a `bd` task.
- Write `// placeholder` or skip implementation with a comment.
- Return a partial response and say "you can fill in the rest."
- Assume a file exists without first calling `view_file` or `grep_search`.

If something is missing, create a `bd create` task for it and report to the user. Never silently skip.

## 5. Normal Task Consciousness (Non-Workflow Mode)

When operating **without** an explicit workflow (e.g., SmithEngineAuto), the AI MUST still:
1. **Read before writing**: Always `view_file` the target before editing. Never overwrite from memory.
2. **Check before removing**: Use `grep_search` to verify a symbol is unused before deleting it.
3. **Verify dependencies**: Use `codanna mcp analyze_impact` before changing a shared function.
4. **Recall rationale**: Use `uv run scripts/cognee/recall.py` before restructuring existing logic.
5. **Register new work**: Any new feature or bug fix MUST get a `bd create` before implementation starts.
