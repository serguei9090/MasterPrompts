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

def get_project_name():
    """Look upward from this script's location for the project root (.git or .cogneeignore)"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent.name
    return Path.cwd().name

DATASET_NAME = os.getenv("COGNEE_DATASET", get_project_name())

async def record_trace(lesson: str, session_id: str = None, category: str = "general"):
    """
    Commits a technical lesson or 'AgentTrace' to Cognee memory.
    This acts as a mirror to the LessonsLearned.md file but in the graph.
    
    Args:
        lesson (str): The lesson or insight to record.
        session_id (str): Optional session ID (e.g. BEAD_ID) for context.
        category (str): The category of the lesson (e.g. 'architecture', 'bug', 'setup').
    """
    print(f"\n--- COGNEE TRACE: {DATASET_NAME} ---")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lesson = f"[{timestamp}] [{category.upper()}] {lesson}"
    
    try:
        # Use remember for high-level ingestion
        # If session_id is provided, it goes to session memory first
        result = await cognee.remember(
            formatted_lesson,
            dataset_name = DATASET_NAME,
            session_id = session_id
        )
        
        print(f">>> LESSON RECORDED: {category}")
        if session_id:
            print(f"Session: {session_id}")
            
        return result

    except Exception as e:
        print(f"\n>>> TRACE ERROR: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Record an AgentTrace (Lesson Learned) in Cognee memory.")
    parser.add_argument("lesson", help="The lesson or insight to record.")
    parser.add_argument("--session", help="Optional session/Bead ID.")
    parser.add_argument("--category", default="general", help="Category of the lesson.")
    
    args = parser.parse_args()
    
    asyncio.run(record_trace(args.lesson, args.session, args.category))
