import logging
import os
import asyncio
import sys
import argparse
import json
from pathlib import Path

# Set environment variables for major libraries BEFORE any imports
os.environ["LOG_LEVEL"] = "ERROR"
os.environ["LITELLM_LOG"] = "ERROR"
os.environ["HTTPCORE_LOG_LEVEL"] = "ERROR"
os.environ["HTTPX_LOG_LEVEL"] = "ERROR"

def _silence_everything():
    """Nuclear silence for all system loggers."""
    logging.root.setLevel(logging.ERROR)
    # Silence all existing loggers
    for name in logging.root.manager.loggerDict:
        logging.getLogger(name).setLevel(logging.ERROR)
    
    # Specifically target common noisy libraries
    for noisy in [
        "cognee", 
        "httpcore", 
        "httpx", 
        "sqlalchemy", 
        "aiosqlite", 
        "instructor", 
        "openai", 
        "litellm",
        "urllib3",
        "query_router",
        "FSCacheAdapter",
        "LiteLLMEmbeddingEngine",
        "CogneeGraph",
        "recall",
        "cognee.api.v1.recall"
    ]:
        logging.getLogger(noisy).setLevel(logging.ERROR)

def _find_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT = _find_project_root()

async def recall_memory(query: str, dataset: str = None, session_id: str = None, context_only: bool = False):
    import cognee
    target_dataset = dataset or os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    
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
    parser.add_argument("--json", action="store_true", help="Format output as JSON")
    
    args = parser.parse_args()
    
    _silence_everything()
    
    target_dataset = args.dataset or os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    
    if not args.context and not args.json:
        print(f"\n--- COGNEE RECALL: {target_dataset} ---")
    
    try:
        result = await recall_memory(args.query, args.dataset, args.session, args.context)
        
        if args.json:
            print(json.dumps({"result": result}, default=str))
        elif args.context:
            print(result)
        else:
            print("\n>>> ANSWER:")
            print(result)
            
    except Exception as e:
        if args.json:
            print(json.dumps({"error": str(e)}))
        else:
            print(f"\n>>> ERROR DURING RECALL: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        if "--json" not in sys.argv:
            print(f"\n  [!] CRITICAL ERROR: {type(e).__name__} - {e}", file=sys.stderr)
        else:
            print(json.dumps({"error": str(e)}))
        sys.exit(1)
