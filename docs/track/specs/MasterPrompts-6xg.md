# Implementation Spec: Advanced Calculator Functions (MasterPrompts-6xg)

## Objective
Refactor the `web_calculator` to support `%` (modulo), `cos` (cosine), and `sin` (sine) functions.

## Architectural Changes

### 1. Backend Sidecar (`sidecar/src/api.py`)
- **Model Update**: Extend `CalculatorRequest.operation` to include `mod`, `cos`, and `sin`.
- **Logic Update**: 
    - Implement `modulo(a, b)` using `%`.
    - Implement `cosine(a)` and `sine(a)` using Python's `math` module.
    - Update the `/calculate` endpoint to dispatch these new operations.
    - For `cos` and `sin`, `num1` will be the input value (in radians).

### 2. Sidecar Bridge Hook (`src/hooks/useSidecarBridge.ts`)
- **Type Update**: Add `mod`, `cos`, `sin` to the `Operation` type.

### 3. Frontend UI (`src/App.tsx`)
- **Mapping Update**: 
    - Update `getOpSymbol` to handle `%`, `cos`, `sin`.
    - Update `getOpIcon` to provide appropriate icons (using Lucide symbols if available, otherwise text).
- **Keypad Update**: 
    - Add buttons for `%`, `cos`, and `sin` to the operations grid.
- **Single-Operand Handling**:
    - Modify `handleCalculate` to handle unary operations (cos, sin) by calling the API with `num2=0` (ignored by backend) immediately when the button is pressed, or by adjusting the state flow.
    - *Decision*: To maintain consistency, `cos` and `sin` will be treated as "immediate" operations on the current display value if possible, or follow the existing `num1 -> op -> calculate`.

## Implementation Details

### API Dispatcher
```python
if request.operation == "mod":
    result = request.num1 % request.num2
elif request.operation == "cos":
    result = math.cos(request.num1)
elif request.operation == "sin":
    result = math.sin(request.num1)
```

### UI Buttons
Add to `grid-ops`:
- `%` (mod)
- `cos`
- `sin`

## Verification Plan
1. **Manual Testing**:
   - `10 % 3 = 1`
   - `cos(0) = 1`
   - `sin(0) = 0`
2. **Linting**: Run `ruff` and `biome` checks.
