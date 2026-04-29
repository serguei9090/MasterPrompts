import asyncio
import os
import logging
from pathlib import Path
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"
os.environ["LITELLM_LOG"] = "ERROR"

# TARGET CONFIGURATION
TARGET_FOLDER = Path(".agents/rules")

def get_project_name():
    """Look upward from this script's location for the project root (.git or .cogneeignore)"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent.name
    return Path.cwd().name

DATASET_NAME = os.getenv("COGNEE_DATASET", f"{get_project_name()}_Rules_v1")

async def sync_project_rules():
    """
    [TEST ONLY] Ingests project-specific rules or ad-hoc folders for verification.
    This script is reserved for testing and manual validation of the ingestion pipeline.
    """
    print(f"\n--- COGNEE SYNC [TEST MODE]: {DATASET_NAME} ---")
    
    if not TARGET_FOLDER.exists():
        print(f"Error: Target folder {TARGET_FOLDER} not found.")
        return

    try:
        # Ingest the rules folder for testing
        print(f"Testing ingestion for: {TARGET_FOLDER}")
        result = await cognee.remember(
            TARGET_FOLDER,
            dataset_name = DATASET_NAME,
            incremental_loading = True
        )
        
        if result:
            print("\n>>> TEST SYNC COMPLETE")
            print("Category: TEST/RULES")
            print(f"Items processed: {len(result)}")
            
        return result

    except Exception as e:
        print(f"\n>>> TEST SYNC ERROR: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(sync_project_rules())
