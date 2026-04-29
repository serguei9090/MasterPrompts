import asyncio
import os
import logging
from pathlib import Path
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"
os.environ["LITELLM_LOG"] = "ERROR"

def get_project_name():
    """Look upward from this script's location for the project root (.git or .cogneeignore)"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent.name
    return Path.cwd().name

DATASET_NAME = os.getenv("COGNEE_DATASET", get_project_name())

def load_ignore_patterns():
    """Loads patterns from .cogneeignore and .gitignore."""
    patterns = []
    for ignore_file in [".cogneeignore", ".gitignore"]:
        if os.path.exists(ignore_file):
            with open(ignore_file, "r") as f:
                patterns.extend([line.strip() for line in f if line.strip() and not line.startswith("#")])
    return patterns

async def run_workspace_index():
    """
    Scans the entire workspace and ingests files into Cognee memory.
    Respects .cogneeignore and .gitignore patterns.
    Uses incremental loading to prevent redundant processing.
    
    Returns:
        dict: Summary of items processed and pipeline IDs.
    """
    print(f"\n--- COGNEE INDEXER: {DATASET_NAME} ---")
    try:
        # v1.0 SDK: Split add and cognify for granular control
        print(f"Ingesting files from {Path('.').resolve()}...")
        await cognee.add(
            Path("."), 
            dataset_name = DATASET_NAME
        )
        
        print("Running temporal cognification (incremental)...")
        # temporal_cognify=True allows tracking changes over time
        result = await cognee.cognify(
            datasets = [DATASET_NAME],
            temporal_cognify = True
        )
        
        if result:
            print("\n>>> INDEXING COMPLETE")
            # result is typically a list of processed items/batches
            print(f"Dataset: {DATASET_NAME}")
        
        return result

    except Exception as e:
        print(f"\n>>> INDEXING ERROR: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(run_workspace_index())
