# Spec: MasterPrompts-96x - Web Calculator

## Objective
Create a web-based calculator application in `IndexTest/Folder/web_calculator` that leverages the existing `calculator.py` CLI logic via a Python Sidecar (JSON-RPC 2.0).

## Architecture
- **Backend (Sidecar)**: Python-based JSON-RPC 2.0 server.
  - Port existing logic from `cli_calculator/calculator.py`.
  - Expose `add`, `subtract`, `multiply`, `divide` methods.
  - Implement JSON-RPC 2.0 protocol via ACP (Agent Client Protocol).
- **Frontend**: React + Vite application.
  - Follow Atomic Design (Atoms, Molecules, Organisms).
  - Use `useSidecarBridge` for communication.
  - Apply `DESIGN.md` (Obsidian + Tactical Green) aesthetics.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Create project directory `IndexTest/Folder/web_calculator`.
2. Initialize Vite React project (TS).
3. Initialize Python sidecar (uv).

### Phase 2: Backend Development (Sidecar)
1. Create `sidecar/src/api.py` with JSON-RPC server.
2. Implement calculator logic (reusing `calculator.py`).
3. Add basic tests for sidecar logic.

### Phase 3: Frontend Development
1. Configure Tailwind/CSS variables from `DESIGN.md`.
2. Implement `useSidecarBridge` hook.
3. Build Atomic components (Button, Display, CalculatorBody).
4. Integrate frontend with sidecar.

### Phase 4: Quality & Polish
1. Run linting (Biome for TS, Ruff for Python).
2. Manual verification of calculator operations.
3. Add animations (framer-motion or similar).

## Dependency Map
- `calculator.py` -> `sidecar/src/api.py`
- `sidecar` -> `frontend` (via JSON-RPC over HTTP/WebSocket or Stdout/Stdin as per bridge spec)
  - *Correction*: The Sidecar Standard typically uses JSON-RPC 2.0. I'll use a simple HTTP server for the sidecar for ease of development in a "small webapp".

## Sub-tasks
- [ ] Initialize `web_calculator` project structure.
- [ ] Port logic to `sidecar/api.py`.
- [ ] Create React frontend components.
- [ ] Connect frontend to backend.
- [ ] Apply Morphic design tokens.
