import asyncio
import os
import logging
import argparse
from pathlib import Path
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"

def get_project_name():
    """Look upward from this script's location for the project root (.git or .cogneeignore)"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent.name
    return Path.cwd().name

DATASET_NAME = os.getenv("COGNEE_DATASET", get_project_name())

async def manage_session(action: str, session_id: str, content: str = None):
    """
    Manages session-aware memory in Cognee.
    
    Args:
        action (str): 'add' to store context, 'recall' to retrieve session context.
        session_id (str): The unique identifier for the session (e.g. BEAD_ID).
        content (str): The context to store (only for 'add').
    """
    print(f"\n--- COGNEE SESSION: {session_id} ---")
    
    try:
        if action == "add":
            if not content:
                print("Error: content required for 'add' action.")
                return
            
            result = await cognee.remember(
                content,
                dataset_name = DATASET_NAME,
                session_id = session_id
            )
            print(f">>> CONTEXT ADDED TO SESSION")
            return result
            
        elif action == "recall":
            # Recall with session_id will check session memory first
            results = await cognee.recall(
                "Summarize the current session context and decisions.",
                session_id = session_id
            )
            
            print(f">>> SESSION RECALL RESULTS:")
            if results:
                for res in results:
                    print(f"\n- {res}")
            else:
                print("No session context found.")
            return results

    except Exception as e:
        print(f"\n>>> SESSION ERROR: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Cognee session-aware memory.")
    parser.add_argument("action", choices=["add", "recall"], help="Action to perform.")
    parser.add_argument("session_id", help="The session/Bead ID.")
    parser.add_argument("--content", help="Content to store (for 'add').")
    
    args = parser.parse_args()
    
    asyncio.run(manage_session(args.action, args.session_id, args.content))
