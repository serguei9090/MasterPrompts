import asyncio
import os
import logging
import signal
import sys
from pathlib import Path

# --- BOOTSTRAP LOGGING (MUST BE FIRST) ---
def get_project_root():
    """Look upward from this script's location for the project root (.git or .cogneeignore)"""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT = get_project_root()
COGNEE_VERBOSE = os.getenv("COGNEE_VERBOSE", "false").lower() == "true"
ENV_LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR").upper()

# Preserve original streams for tqdm
ORIGINAL_STDOUT = sys.stdout
ORIGINAL_STDERR = sys.stderr

class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        try:
            from tqdm import tqdm
            msg = self.format(record)
            tqdm.write(msg, file=ORIGINAL_STDERR)
            self.flush()
        except Exception:
            self.handleError(record)

def bootstrap():
    """Configures logging and redirects streams to catch early imports."""
    effective_level = ENV_LOG_LEVEL
    logs_dir = PROJECT_ROOT / "scripts" / "cognee" / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    engine_log_file = logs_dir / "cognee.log"
    
    # Silence extremely noisy sub-loggers
    noisy_loggers = [
        "cognee", "litellm", "transformers", "openai", 
        "httpcore", "httpx", "urllib3", "sqlalchemy", 
        "aiosqlite", "databases", "asyncio"
    ]
    
    file_handler = logging.FileHandler(engine_log_file, mode = "w")
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)s: %(message)s"))
    file_handler.setLevel(getattr(logging, effective_level))

    tqdm_handler = TqdmLoggingHandler()
    tqdm_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)-8s] %(message)s"))

    # Configure ROOT first
    root_l = logging.getLogger()
    root_l.setLevel(getattr(logging, effective_level))
    root_l.handlers = [file_handler] # Start with ONLY file handler
    
    if COGNEE_VERBOSE:
        root_l.addHandler(tqdm_handler)

    # Pre-emptively silence loggers
    for logger_name in noisy_loggers:
        l = logging.getLogger(logger_name)
        l.setLevel(getattr(logging, effective_level))
        l.propagate = False
        l.handlers = [file_handler]
        if COGNEE_VERBOSE:
            l.addHandler(tqdm_handler)

    # --- STRUCTLOG SILENCE ---
    try:
        import structlog
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(
                logging.DEBUG if COGNEE_VERBOSE else logging.CRITICAL
            ),
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )
    except ImportError:
        pass

    # --- NUCLEAR STREAM REDIRECTION ---
    # If not verbose, we pipe ALL stdout/stderr to the log file to prevent leaks
    if not COGNEE_VERBOSE:
        f = open(engine_log_file, "a", buffering=1)
        sys.stdout = f
        sys.stderr = f

# Execute bootstrap
bootstrap()

# Now safe to import others
import pathspec
from tqdm import tqdm
# cognee is imported inside the function to ensure no side-effects during setup

def get_ignore_spec():
    """Creates a pathspec.GitIgnoreSpec from .cogneeignore and .gitignore."""
    patterns = []
    patterns.extend([".git/", "**/node_modules/", "__pycache__/", ".venv/"])
    for ignore_file in [".cogneeignore", ".gitignore"]:
        file_path = PROJECT_ROOT / ignore_file
        if file_path.exists():
            with open(file_path, "r") as f:
                patterns.extend([line.strip() for line in f if line.strip() and not line.startswith("#")])
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

def get_filtered_files():
    """Manually walks the project root and filters files based on ignore patterns."""
    spec = get_ignore_spec()
    files_to_index = []
    root_str = str(PROJECT_ROOT.resolve())
    for root, dirs, files in os.walk(root_str):
        rel_root = os.path.relpath(root, root_str)
        if rel_root == ".": rel_root = ""
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_root, d) + "/")]
        for file in files:
            rel_file_path = os.path.join(rel_root, file)
            if not spec.match_file(rel_file_path):
                files_to_index.append(os.path.join(root, file))
    return files_to_index

async def run_workspace_index():
    """
    Scans the workspace, filters files, and ingests them into Cognee.
    Uses batching to improve speed while providing progress updates.
    """
    import cognee
    DATASET_NAME = os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    SCRIPT_LOG_LEVEL = os.getenv("COGNEE_INDEX_LOG_LEVEL", "INFO").upper()
    BATCH_SIZE = int(os.getenv("COGNEE_BATCH_SIZE", "1"))

    print(f"\n--- COGNEE INDEXER: {DATASET_NAME} ---")
    print(f"Script Mode: {SCRIPT_LOG_LEVEL} | Batch Size: {BATCH_SIZE} | Cognee Verbose: {COGNEE_VERBOSE}")
    
    try:
        clean_file_list = get_filtered_files()
        total_files = len(clean_file_list)
        
        if not clean_file_list:
            print("No files found to index. Check your ignore patterns.")
            return None

        print(f"Targeting {total_files} files for indexing...")

        errors = []
        processed_count = 0
        logs_dir = PROJECT_ROOT / "scripts" / "cognee" / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        error_log_path = logs_dir / "errors.log"

        if SCRIPT_LOG_LEVEL in ["INFO", "DEBUG"]:
            # Progress Bar Mode with Batching
            with tqdm(total = total_files, desc = "Indexing Progress", unit = "file", leave = True, file=ORIGINAL_STDERR) as pbar:
                for i in range(0, total_files, BATCH_SIZE):
                    batch = clean_file_list[i : i + BATCH_SIZE]
                    pbar.set_description("Indexing")
                    
                    if SCRIPT_LOG_LEVEL == "DEBUG":
                        tqdm.write(f"-> Batch {i//BATCH_SIZE + 1}: Processing {len(batch)} files...")
                    
                    try:
                        import cognee
                        await cognee.remember(
                            data = batch,
                            dataset_name = DATASET_NAME
                        )
                        processed_count += len(batch)
                    except (asyncio.CancelledError, KeyboardInterrupt):
                        raise
                    except Exception as e:
                        errors.append((str(batch), str(e)))
                        tqdm.write(f" [!] BATCH ERROR: {e}")
                    
                    pbar.update(len(batch))
            
            result = {"items_processed": processed_count, "errors": len(errors)}
        else:
            # Full Batch Mode (Maximum speed, no progress updates)
            print("Indexing in full batch mode...")
            import cognee
            result = await cognee.remember(
                data = clean_file_list,
                dataset_name = DATASET_NAME
            )

        # Log results
        if errors:
            with open(error_log_path, "w") as f:
                f.write(f"--- COGNEE INDEXING ERRORS ({len(errors)}) ---\n")
                for item, err in errors:
                    f.write(f"Batch/File: {item}\nError: {err}\n{'-'*20}\n")
            print(f"\n>>> INDEXING COMPLETED WITH {len(errors)} ERRORS. Details: {error_log_path}")
        else:
            if error_log_path.exists(): error_log_path.unlink()

        print("\n>>> INDEXING SESSION FINISHED")
        return result

    except (asyncio.CancelledError, KeyboardInterrupt):
        print("\n\n[!] ABORTED BY USER. Stopping gracefully...")
        return None
    except Exception as e:
        print(f"\n>>> CRITICAL INDEXER ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    try:
        asyncio.run(run_workspace_index())
    except KeyboardInterrupt:
        # Final clean exit for Windows
        sys.exit(0)
