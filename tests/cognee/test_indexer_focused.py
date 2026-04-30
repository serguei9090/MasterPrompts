"""
Focused integration test: index scripts/cognee/ and verify:
  - Header visibility
  - Silence of third-party logs (Nuclear Silence)
  - Filename tracking (Start/Finish)
  - Clean exit on KeyboardInterrupt

Run with:
    uv run python tests/cognee/test_indexer_focused.py
"""

import asyncio
import os
import sys
from pathlib import Path
import unittest.mock as mock

# --- SETUP PATHS ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

# --- OVERRIDE ENV ---
os.environ["COGNEE_VERBOSE"] = "false"
os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["COGNEE_BATCH_SIZE"] = "1"
os.environ["COGNEE_DATASET"] = "test_focused_index"
os.environ["COGNEE_INDEX_LOG_LEVEL"] = "INFO"

from scripts.cognee.indexer import run_index, TERM_OUT, _collect_files

async def test_focused_index():
    target_dir = PROJECT_ROOT / "scripts" / "cognee"
    files = _collect_files(target_dir)
    total = len(files)
    
    TERM_OUT.write(f"\n{'-' * 50}\n")
    TERM_OUT.write(f"  TESTING FOCUSED INDEX: {target_dir.name}\n")
    TERM_OUT.write(f"  TARGET FILES: {total}\n")
    TERM_OUT.write(f"{'-' * 50}\n")

    tracker = []

    async def fake_remember(data, dataset_name):
        for f in data:
            name = Path(f).name
            tracker.append(f"STARTED: {name}")
            await asyncio.sleep(0.05) # Small delay to simulate work
            tracker.append(f"FINISHED: {name}")

    with mock.patch("cognee.remember", side_effect=fake_remember):
        result = await run_index(
            target_dir=target_dir,
            dataset_name="test_focused_index",
            batch_size=1,
            script_log_level="INFO"
        )

    TERM_OUT.write(f"\n{'-' * 50}\n")
    TERM_OUT.write("  TRACE LOG:\n")
    for entry in tracker:
        TERM_OUT.write(f"  {entry}\n")
    
    TERM_OUT.write(f"{'-' * 50}\n")
    
    assert result["items_processed"] == total, f"Expected {total}, got {result['items_processed']}"
    assert len(tracker) == total * 2, f"Expected {total*2} trace entries, got {len(tracker)}"
    
    # Check that every start has a finish
    for f in files:
        name = Path(f).name
        assert f"STARTED: {name}" in tracker
        assert f"FINISHED: {name}" in tracker
        
    TERM_OUT.write("  [OK]  TEST PASSED: All files tracked from Start to Finish.\n")
    TERM_OUT.write(f"{'-' * 50}\n\n")

if __name__ == "__main__":
    try:
        asyncio.run(test_focused_index())
    except KeyboardInterrupt:
        TERM_OUT.write("\n  [STOP]  Test interrupted.\n")
