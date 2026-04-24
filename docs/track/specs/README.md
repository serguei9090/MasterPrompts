# System Tracking & State Persistence

This directory (`docs/track/specs/`) is the physical brain of the Antigravity framework.
Every active constraint, missing feature, or ongoing refactor MUST be tracked here.

## The TODO(ID) Protocol

When you encounter a gap in logic or need to defer work, do not use simple inline `// TODO`.
Follow the strict protocol:

1. Create a `TODO(ID)` comment in the code (e.g., `TODO(Auth_001)`).
2. Create a detail file here: `docs/track/specs/Auth_001.md`.
3. Add the high-level task to `docs/track/TODO.md`.

## Content of a Detail File
- **Rationale**: Why was this bypassed/deferred?
- **Context**: Any relevant state, libraries, or dependencies needed.
- **Completion Criteria**: Exactly what needs to happen to resolve this ID.
