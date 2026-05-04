# Morphic Web Calculator

A premium, tactical web calculator built with the Morphic "Engine Precision" philosophy. It leverages a Python Sidecar for mathematical operations, following the Sidecar Standard.

## Features
- **Tactical UI**: Obsidian-based glassmorphic design with tactical green accents.
- **Sidecar Logic**: Mathematical operations are processed via a FastAPI backend, ensuring precision and separation of concerns.
- **Animated Interactions**: Smooth transitions using Framer Motion.
- **Standard Compliant**: Adheres to the Sidecar Standard and Morphic Architecture protocols.

## Tech Stack
- **Frontend**: React 19, Vite 8, Framer Motion, Lucide React.
- **Backend**: Python 3.13, FastAPI, Uvicorn (Sidecar).
- **Communication**: JSON-RPC over HTTP (Bridge).

## Getting Started

### Prerequisites
- [Bun](https://bun.sh)
- [UV](https://github.com/astral-sh/uv)

### Installation

1. **Frontend Setup**:
   ```bash
   bun install
   ```

2. **Sidecar Setup**:
   ```bash
   cd sidecar
   uv sync
   ```

### Running the Application

1. **Start the Sidecar**:
   ```bash
   cd sidecar
   uv run python src/api.py
   ```

2. **Start the Frontend**:
   ```bash
   bun run dev
   ```

## Architecture
This project follows the **Sidecar Standard**:
- The frontend is a thin client that delegates logic to the Python backend.
- The backend implements the core calculator logic ported from the CLI version.
- Communication is handled via the `useSidecarBridge` hook.
