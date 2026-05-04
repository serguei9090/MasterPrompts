# Task Spec: Refactor web_calculator for Modulo and Trig Functions

**Bead ID:** MasterPrompts-6xg

## Objective
Extend the `web_calculator` functionality to support `%` (modulo), `sin` (sine), and `cos` (cosine) operations.

## Architecture Changes

### Backend (Sidecar)
- **File:** `IndexTest/Folder/web_calculator/sidecar/src/api.py`
- **Changes:**
  - Import `math` module.
  - Update `CalculatorRequest` Pydantic model to include `mod`, `sin`, `cos` in the `operation` Literal.
  - Implement helper functions:
    - `modulo(a, b)`: returns `a % b`.
    - `sine(a)`: returns `math.sin(math.radians(a))`. (Assuming input is in degrees)
    - `cosine(a)`: returns `math.cos(math.radians(a))`. (Assuming input is in degrees)
  - Update `calculate` endpoint to handle these new operations.

### Frontend
- **File:** `IndexTest/Folder/web_calculator/src/hooks/useSidecarBridge.ts`
  - Update `Operation` type: `"add" | "sub" | "mul" | "div" | "mod" | "sin" | "cos"`.
- **File:** `IndexTest/Folder/web_calculator/src/App.tsx`
  - Update `getOpSymbol` to return `%`, `sin`, `cos`.
  - Update `getOpIcon` to return appropriate labels/icons.
  - Add buttons for `%`, `sin`, `cos` in the keypad.
  - Refactor `handleCalculate` to handle unary operations if necessary, or just send them as-is to the sidecar.

## Implementation Details
- For `sin` and `cos`, we will use the value currently in the display as `num1`.
- For `%`, it will work like existing binary operators.

## Verification Plan
- **Backend Tests:** Run sidecar and test via `curl` or automated script.
- **UI Verification:** Manually test buttons and display results.
