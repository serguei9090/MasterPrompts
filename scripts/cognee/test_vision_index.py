import asyncio
import os
import sys
from pathlib import Path

# Fix python path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.cognee.indexer import run_index, _bootstrap_logging

async def test_vision_ingestion():
    # Setup paths
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    assets_dir = PROJECT_ROOT / "tests" / "cognee" / "assets"
    
    # Force verbose for this test so we can see the engine logs
    os.environ["COGNEE_VERBOSE"] = "true"
    
    print(f"\n--- TESTING VISION INGESTION ---")
    print(f"Targeting: {assets_dir}")
    
    # Run indexer on the assets folder
    result = await run_index(
        target_dir=assets_dir,
        dataset_name="test_vision_dataset",
        batch_size=1,
        script_log_level="DEBUG"
    )
    
    print(f"\n--- TEST RESULTS ---")
    print(f"Processed: {result['items_processed']} files")
    print(f"Errors   : {result['errors']}")
    print(f"Check logs at scripts/cognee/logs/cognee.log for engine output.")

if __name__ == "__main__":
    asyncio.run(test_vision_ingestion())
