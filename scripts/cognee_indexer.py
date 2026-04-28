import os
import sys
import fnmatch
import subprocess
from pathlib import Path

def load_ignore_patterns(ignore_file):
    patterns = []
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # normalize for fnmatch
                    if line.endswith('/'):
                        line = line[:-1]
                    patterns.append(line)
    return patterns

def is_ignored(path_str, patterns, base_dir):
    try:
        # Convert absolute to relative path based on root
        rel_path = Path(path_str).relative_to(base_dir).as_posix()
    except ValueError:
        return False # Not in base dir
    
    parts = rel_path.split('/')
    
    for pattern in patterns:
        # Match directory name exactly (like .venv or node_modules)
        for part in parts:
            if fnmatch.fnmatch(part, pattern):
                return True
        # Or match the whole relative path
        if fnmatch.fnmatch(rel_path, pattern):
            return True
            
    return False

def index_file(filepath, dataset_name):
    print(f"Indexing [{dataset_name}]: {filepath}")
    try:
        # Use subprocess to run the uv cognee-cli remember command with dataset isolation
        subprocess.run(["uv", "run", "cognee-cli", "remember", filepath, "-d", dataset_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to index {filepath}: {e}", file=sys.stderr)
    except FileNotFoundError:
        print("Error: 'uv' command not found. Ensure uv is installed and in your PATH.", file=sys.stderr)
        sys.exit(1)
        
def main():
    base_dir = Path.cwd()
    # Use the project root directory name as the default dataset name
    default_dataset = base_dir.name
    
    ignore_file = base_dir / '.cogneeignore'
    
    # Load primary cogneeignore
    patterns = load_ignore_patterns(ignore_file)
    
    # Always merge with .gitignore for safety
    gitignore = base_dir / '.gitignore'
    if gitignore.exists():
         patterns.extend(load_ignore_patterns(gitignore))
         
    # Deduplicate patterns
    patterns = list(set(patterns))
         
    args = sys.argv[1:]
    
    if not args:
        print("Usage: uv run python scripts/cognee_indexer.py [--full] [file1 file2 ...]")
        print("  --full : Recursively index all non-ignored files in the workspace")
        sys.exit(1)
        
    dataset_name = os.getenv("COGNEE_DATASET", default_dataset)

    if args[0] == '--full':
        print(f"Starting full workspace index for dataset '{dataset_name}'...")
        for root, dirs, files in os.walk(base_dir):
            # Filter dirs in place to not walk ignored directories
            dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), patterns, base_dir)]
            
            for file in files:
                filepath = os.path.join(root, file)
                if not is_ignored(filepath, patterns, base_dir):
                    index_file(filepath, dataset_name)
    else:
        # Index specific files (Incremental - ideal for lefthook pre-commit)
        for filepath in args:
            abs_filepath = Path(filepath).resolve()
            if abs_filepath.exists() and not is_ignored(str(abs_filepath), patterns, base_dir):
                index_file(str(abs_filepath), dataset_name)
            else:
                print(f"Skipping (ignored or deleted): {filepath}")

if __name__ == "__main__":
    main()
