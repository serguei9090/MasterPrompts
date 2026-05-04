# Task Spec: Refactor Calculator UI and Add "Multiply by 100" Button

## Objective
Refactor the `web_calculator` UI to improve button ergonomics (smaller size) and add a quick conversion button to multiply the current number by 100.

## Requirements
1.  **UI Refinement**:
    *   Reduce the size of calculator buttons in `App.css`.
    *   Target `.btn` padding or dimensions.
2.  **Multiply by 100 Button**:
    *   Add a new button labeled "×100" (or similar).
    *   This button should immediately multiply the current display value by 100.
    *   Integrate this operation into the sidecar `api.py` for consistency with the "Engine Precision" standard.

## Technical Details

### Backend (Sidecar)
- **File**: `sidecar/src/api.py`
- **Changes**:
    - Add `"mul100"` to `CalculatorRequest.operation` Literal.
    - Add logic in `calculate` endpoint to handle `mul100`.

### Frontend
- **File**: `src/App.tsx`
- **Changes**:
    - Add `"mul100"` to `Operation` type (verify in `hooks/useSidecarBridge.ts`).
    - Update `getOpIcon` to return an icon or text for `mul100`.
    - Add a button in the keypad for `mul100`.
- **File**: `src/App.css`
- **Changes**:
    - Reduce `.btn` padding (e.g., from `1rem` to `0.75rem`).
    - Adjust grid/layout if necessary to accommodate the new button.

## Verification Plan
1.  Verify button size visually.
2.  Test numerical input.
3.  Test "×100" button: enter `5`, press `×100`, expect `500`.
4.  Verify history reflects the multiplication.
