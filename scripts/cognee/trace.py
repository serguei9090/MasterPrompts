import asyncio
import os
import sys
import logging
import argparse
from pathlib import Path
from datetime import datetime
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"

def _find_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT = _find_project_root()

async def record_trace(lesson: str, dataset: str = None, session_id: str = None, category: str = "general"):
    """
    Commits a technical lesson or 'AgentTrace' to Cognee memory.
    
    Args:
        lesson (str): The lesson or insight to record.
        dataset (str): Target dataset name.
        session_id (str): Optional session ID (e.g. BEAD_ID).
        category (str): The category of the lesson.
    """
    target_dataset = dataset or os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    print(f"\n--- COGNEE TRACE: {target_dataset} ---")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lesson = f"[{timestamp}] [{category.upper()}] {lesson}"
    
    try:
        result = await cognee.remember(
            formatted_lesson,
            dataset_name = target_dataset,
            session_id = session_id
        )
        print(f">>> LESSON RECORDED: {category}")
        return result
    except Exception as e:
        print(f"\n>>> TRACE ERROR: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Record an AgentTrace in Cognee memory.")
    parser.add_argument("lesson", help="The lesson or insight to record.")
    parser.add_argument("--dataset", help="Optional: Specific dataset name.")
    parser.add_argument("--session", help="Optional session/Bead ID.")
    parser.add_argument("--category", default="general", help="Category of the lesson.")
    
    args = parser.parse_args()
    
    try:
        asyncio.run(record_trace(args.lesson, args.dataset, args.session, args.category))
    except KeyboardInterrupt:
        print("\n  ⊘  Interrupted.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"\n  [!] CRITICAL ERROR: {type(e).__name__} - {e}", file=sys.stderr)
        sys.exit(1)
