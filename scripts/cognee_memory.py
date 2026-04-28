import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_dataset_name():
    """Determine the dataset name from .env or current project directory."""
    env_dataset = os.getenv("COGNEE_DATASET")
    if env_dataset:
        return env_dataset
    # Default to current working directory name
    return Path.cwd().name

def run_cognee_command(command_type, args):
    """Execute a cognee-cli command and filter out log garbage."""
    dataset_name = get_dataset_name()
    
    # Construct the base command
    cmd = ["uv", "run", "cognee-cli", command_type] + args
    
    # Ensure dataset flag is present
    if "-d" not in args and "--dataset-name" not in args:
        cmd.extend(["-d", dataset_name])

    # Run the command and capture output
    try:
        # Set environment variable to suppress logging if possible, 
        # though cognee-cli might not respect it directly from here
        env = os.environ.copy()
        env["LOG_LEVEL"] = "ERROR"
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env
        )
        
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"Error executing Cognee: {stderr}", file=sys.stderr)
            return

        # Filter logic: Cognee logs usually start with [ or a timestamp
        # and contain things like [info] or [warning]
        clean_output = []
        for line in stdout.splitlines():
            # Basic heuristic: ignore lines that look like structlog output
            if any(marker in line for marker in ["[info", "[warning", "[error", "[debug"]):
                continue
            if line.strip().startswith("202") and "[" in line: # Timestamp check
                continue
            if ">>> LOADING PROFILE <<<" in line:
                continue
            if "Building masterprompts" in line or "Built masterprompts" in line:
                continue
            
            clean_output.append(line)

        # Print cleaned output
        print("\n".join(clean_output).strip())

    except Exception as e:
        print(f"Failed to run Cognee proxy: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cognee_memory.py [recall|remember] [args...]")
        sys.exit(1)

    cmd_type = sys.argv[1]
    cmd_args = sys.argv[2:]
    
    if cmd_type not in ["recall", "remember", "forget", "improve", "add", "cognify", "search"]:
        print(f"Unsupported command: {cmd_type}")
        sys.exit(1)

    run_cognee_command(cmd_type, cmd_args)
