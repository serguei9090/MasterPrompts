# Morphic AVAS Architecture: Intelligence Sync
Assume Role: @diagram-agent

This diagram maps the relationship between the human-facing **Beads (bd)** state and the AI-facing **Intelligence Stack**, ensuring the "Parity Law" is strictly enforced via the AVAS standard.

```mermaid
graph TD
    subgraph OperationalLayer [Human / Operational Space]
        BD_TODO["Beads (bd)<br/>(Master Task State)"]
        BD_REM["bd remember<br/>(Atomic Rationale)"]
        H_DESIGN["DESIGN.md<br/>(UI/UX Source of Truth)"]
    end

    subgraph IntelligenceLayer [AI Intelligence Stack]
        L1_COD["Codanna (Physical)<br/>(Impact & Symbol Mapping)"]
        L2_COG["Cognee (Semantic)<br/>(Graph-based Memory)"]
        L0_ST["Sequential Thinking<br/>(Logic & Planning)"]
    end

    subgraph ExecutionFactory [Smith Auto Cycle]
        F1[Research: Recall & Analyze]
        F2[Plan: Spec Update]
        F3[Act: Surgical Coding]
        F4[Audit: Quality & Visual]
    end

    %% Sync Relationships
    BD_TODO -- "1. Context Injection" --> F1
    L1_COD -- "2. Impact Mapping" --> F1
    L2_COG -- "3. Rationale Retrieval" --> F1
    L0_ST -- "4. Orchestration" --> F2
    F2 -- "5. DESIGN.md Update" --> H_DESIGN
    F3 -- "6. Atomic Implementation" --> F4
    F4 -- "7. Close Loop [x]" --> BD_TODO
    F4 -- "8. Lessons Learned" --> L2_COG

    %% Visual Standards (AVAS)
    style OperationalLayer fill:#f9f,stroke:#333,stroke-width:2px
    style IntelligenceLayer fill:#bbf,stroke:#333,stroke-width:2px
    style ExecutionFactory fill:#dfd,stroke:#333,stroke-width:2px
```

## AVAS (Agentic Visual Architecture Standard) Protocol
To ensure architectural clarity, all system diagrams MUST follow these rules:
1. **Mandatory Subgraphs**: Group logical layers (Operational, Domain, Infrastructure, AI).
2. **Labeled Connections**: Every arrow MUST describe the action or data flow (e.g., "Recall", "Inject", "Audit").
3. **Double-Line Sync**: Use distinct arrow styles for synchronous vs asynchronous data flows.
4. **Color Coding**: 
   - **Pink/Purple**: Human/Operational state.
   - **Blue/Indigo**: AI Intelligence & Memory.
   - **Green**: Execution & Implementation.
