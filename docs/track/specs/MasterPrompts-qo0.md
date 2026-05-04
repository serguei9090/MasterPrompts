# MasterPrompts-qo0: Add unit converters and collapsible history sidebar

## 1. Context & Rationale
The user requested adding mass and distance conversion capabilities to the calculator, transforming it based on modes. Additionally, the history panel must be refactored into a collapsible sidebar accessible via a floating button.

## 2. API / Backend Updates (sidecar/src/api.py)
- Extend `CalculatorRequest.operation` Literal with: `"mass_kg_lb", "mass_lb_kg", "dist_mm_cm", "dist_cm_mm"`.
- Implement corresponding math functions.
- Add routing logic in `calculate` endpoint to map new operations to functions.

## 3. Frontend State Updates (src/hooks/useSidecarBridge.ts & src/App.tsx)
- Add new operations to `Operation` type in `useSidecarBridge.ts`.
- Add `calcMode` state: `"math" | "mass" | "distance"`.
- Add `isHistoryOpen` state: `boolean`.
- Create UI for mode switching (e.g., small buttons in the header or below the display).
- Based on `calcMode`, conditionally render the grid of operations.

## 4. UI/UX Updates (src/App.tsx & src/App.css)
- Refactor `.main-layout` to avoid requiring the history panel inline.
- Style `.history-panel` as a fixed sidebar attached to the right edge.
- Create `.history-toggle-btn`, a floating button on the right edge (middle vertically).
- Use `framer-motion` to animate the sidebar in and out.
- Ensure Atomic Design and existing design tokens (glassmorphism, vibrant colors) are maintained.
