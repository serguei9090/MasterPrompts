import asyncio
import os
import sys
import logging
from pathlib import Path

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"

async def hard_reset():
    import cognee
    print("\n" + "=" * 60)
    print("!!! COGNEE SYSTEM PRUNE: CLEARING ALL MEMORY AND QUEUES !!!")
    print("=" * 60)
    
    confirm = await asyncio.to_thread(input, "\nThis will delete ALL graph data, vector stores, and metadata. \nYour project files are safe, but the AI will 'forget' everything. \nContinue? (y/n): ")
    
    if confirm.lower() != 'y':
        print("Reset cancelled.")
        return

    try:
        # 1. Wipes the raw files from your local disk storage backend
        print("\n[1/3] Pruning raw data segments...")
        await cognee.prune.prune_data()
        
        # 2. Wipes the graph, vector store, relational DB, and stuck pipeline state
        print("[2/3] Pruning system databases (Graph/Vector/Relational)...")
        await cognee.prune.prune_system(metadata = True)
        
        # 3. Clean up the logs/PID files if they exist
        print("[3/3] Cleaning internal logs and PID locks...")
        root = Path(__file__).resolve().parents[2]
        pid_file = root / "scripts" / "cognee" / "logs" / "indexer.pid"
        if pid_file.exists():
            pid_file.unlink()
        
        print("\n[✓] Cognee state cleared. The pipeline is empty.")
        print("    You can now run 'uv run python scripts/cognee/indexer.py --full' to start clean.")

    except Exception as e:
        print(f"\n[✗] RESET FAILED: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(hard_reset())
    except KeyboardInterrupt:
        print("\nAborted.")
    except Exception as e:
        print(f"Error: {e}")
