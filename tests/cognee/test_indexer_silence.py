import os
import subprocess
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INDEXER_SCRIPT = PROJECT_ROOT / "scripts" / "cognee" / "indexer.py"

def test_indexer_silence():
    """
    Verifies that the indexer script does not output Cognee initialization 
    logs to the console when COGNEE_VERBOSE is set to false.
    """
    print(f"Testing silence of: {INDEXER_SCRIPT}")
    env = os.environ.copy()
    env["COGNEE_VERBOSE"] = "false"
    env["LOG_LEVEL"] = "DEBUG"
    env["COGNEE_BATCH_SIZE"] = "1"
    env["COGNEE_DATASET"] = "test_silence_dataset"
    
    try:
        process = subprocess.Popen(
            ["uv", "run", "python", str(INDEXER_SCRIPT)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
            cwd=str(PROJECT_ROOT)
        )
        
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()

        combined_output = stdout + stderr
        
        # Forbidden strings
        forbidden = [
            "[info]", 
            "[warning]", 
            "Logging initialized", 
            "connect_tcp.started",
            "Deleted old log file"
        ]
        
        for word in forbidden:
            if word.lower() in combined_output.lower():
                print(f"FAILED: Found forbidden log message: {word}")
                sys.exit(1)
        
        print("SUCCESS: No forbidden logs found in console output.")
        
    except Exception as e:
        print(f"FAILED: Indexer script failed to run: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_indexer_silence()
