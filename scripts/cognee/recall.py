import asyncio
import os
import logging
import argparse
from pathlib import Path
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"
os.environ["LITELLM_LOG"] = "ERROR"

def get_project_name():
    """Resolves the current project name for dataset scoping."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent.name
    return Path.cwd().name

async def recall_memory(query: str, dataset: str = None, session_id: str = None, context_only: bool = False):
    """
    Query Cognee memory using the v1.0 Recall pipeline.
    
    Args:
        query (str): The natural language question to ask memory.
        dataset (str, optional): Target a specific dataset. Defaults to current project name.
        session_id (str, optional): Include session-aware memory for agentic context.
        context_only (bool): If True, returns raw context. If False, returns synthesized AI answer.
        
    Returns:
        The result of the recall operation.
    """
    target_dataset = dataset or get_project_name()
    
    # Auto-routing is enabled by default to pick the best strategy (Summary, Graph, Code, etc.)
    result = await cognee.recall(
        query_text = query,
        datasets = [target_dataset],
        session_id = session_id,
        only_context = context_only
    )
    return result

async def main():
    parser = argparse.ArgumentParser(description="Multi-purpose Cognee Recall Tool")
    parser.add_argument("query", help="The question to ask memory")
    parser.add_argument("--dataset", help="Optional: Specific dataset name")
    parser.add_argument("--session", help="Optional: Session ID for agentic context")
    parser.add_argument("--context", action="store_true", help="Return raw context only")
    
    args = parser.parse_args()
    
    # Header for CLI visibility
    if not args.context:
        print(f"\n--- COGNEE RECALL: {get_project_name()} ---")
    
    try:
        result = await recall_memory(args.query, args.dataset, args.session, args.context)
        
        # If running as a tool, we might just want the raw output
        if args.context:
            print(result)
        else:
            print("\n>>> ANSWER:")
            print(result)
            
    except Exception as e:
        print(f"\n>>> ERROR DURING RECALL: {e}")

if __name__ == "__main__":
    asyncio.run(main())
