import os
import sys
import argparse
from pathlib import Path

# Try to import pathspec
try:
    import pathspec
except ImportError:
    print("Error: 'pathspec' package not found. Please install it with 'uv pip install pathspec'.")
    sys.exit(1)

def _find_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT = _find_project_root()

def _load_ignore_spec(root: Path) -> pathspec.PathSpec:
    # Default built-in ignores
    patterns = [".git/", "**/node_modules/", "__pycache__/", ".venv/", ".cognee/"]
    sources = [".cogneeignore", ".gitignore"]
    
    print(f"--- Loading Ignore Patterns ---")
    for name in sources:
        fp = root / name
        if fp.exists():
            print(f" [+] Found {name}")
            with open(fp, encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.split("#")[0].strip()
                    if line:
                        patterns.append(line)
        else:
            print(f" [-] {name} not found")
    
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

def run_ignore_test(verbose=False):
    print(f"\n--- COGNEE IGNORE TEST (DRY RUN) ---")
    print(f"Project Root: {PROJECT_ROOT}")
    
    spec = _load_ignore_spec(PROJECT_ROOT)
    
    total_found = 0
    ignored_count = 0
    to_index = []
    folder_counts = {}

    print(f"\n--- Scanning Filesystem ---")
    
    for walk_root, dirs, files in os.walk(str(PROJECT_ROOT)):
        rel_walk_root = os.path.relpath(walk_root, str(PROJECT_ROOT))
        if rel_walk_root == ".":
            rel_walk_root = ""
        
        # Filter directories in-place to prevent deep walking of ignored folders
        original_dirs = list(dirs)
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_walk_root, d).replace("\\", "/") + "/")]
        
        # Track which directories were pruned
        pruned = set(original_dirs) - set(dirs)
        if pruned and verbose:
            for p in pruned:
                print(f" [SKIP DIR] {os.path.join(rel_walk_root, p)}")

        for fname in files:
            total_found += 1
            rel_path = os.path.normpath(os.path.join(rel_walk_root, fname)).replace("\\", "/")
            
            # Match against spec
            if spec.match_file(rel_path) or spec.match_file("/" + rel_path):
                ignored_count += 1
                if verbose:
                    print(f" [IGNORE]   {rel_path}")
            else:
                to_index.append(rel_path)
                
                # Track folder distribution
                folder = os.path.dirname(rel_path) or "(root)"
                folder_counts[folder] = folder_counts.get(folder, 0) + 1
                
                if verbose:
                    print(f" [INDEX]    {rel_path}")

    print(f"\n--- Results ---")
    print(f" Total files encountered: {total_found}")
    print(f" Files ignored:           {ignored_count}")
    print(f" Files to be indexed:     {len(to_index)}")
    print(f"-------------------------------")

    if to_index:
        print("\n--- Folder Distribution (Indexed) ---")
        # Sort folders alphabetically for clarity
        for folder in sorted(folder_counts.keys()):
            count = folder_counts[folder]
            print(f" {folder:<40} | {count:>3} files")
        print(f"-------------------------------")
    
    if not verbose:
        print("\n[TIP] Run with --verbose to see exactly which files are being ignored/indexed.")
    
    if to_index and not verbose:
        print("\nExample files TO INDEX (first 10):")
        for f in to_index[:10]:
            print(f"  - {f}")
            
    return len(to_index)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify .cogneeignore functionality")
    parser.add_argument("-v", "--verbose", action="store_true", help="List every file processed")
    args = parser.parse_args()
    
    run_ignore_test(verbose=args.verbose)
