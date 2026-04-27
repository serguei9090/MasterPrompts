---
name: SequentialThinkingBackup
description: Simulation of the Sequential Thinking MCP for cases where the tool is unavailable.
---

# /SequentialThinkingBackup Workflow

If the `sequentialthinking` MCP tool is missing from your context, use this structured thought process to solve complex problems.

## 🧠 The Thinking Loop

For any complex problem, execute the following steps in your internal reasoning block:

### 1. Initial Hypothesis
- Define the problem clearly.
- Estimate the number of "thoughts" needed (e.g., 5-10).
- State your initial goal.

### 2. Step-by-Step Analysis
- **Thought [N]**: Break down one specific aspect of the problem.
- **Refinement**: Question your previous thought. Is there a simpler way? Did you miss a dependency?
- **Branching**: If there are multiple paths, explore Path A, then Path B.
- **Revision**: Explicitly state if a previous assumption was wrong.

### 3. Verification
- Test your solution hypothesis against the requirements.
- Identify edge cases.

### 4. Final Solution
- Synthesize the thoughts into a single, actionable answer.

## 📝 Example Reasoning Block
> [!NOTE]
> **Thought 1**: I need to implement X. I'll need about 5 steps.
> **Thought 2**: X depends on Y. I should check if Y is initialized.
> **Thought 3 (Revision)**: Actually, checking Y is not enough, I need to check the config for Y.
> **Thought 4**: Verified config. Proceeding with X implementation logic...
