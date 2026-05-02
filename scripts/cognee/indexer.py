"""
Cognee Indexer — Clean, silent, progress-tracked ingestion.

Environment Variables:
  LOG_LEVEL            Engine log level routed to the log file (default: ERROR)
  COGNEE_VERBOSE       "true" to also print engine logs to the console (default: false)
  COGNEE_BATCH_SIZE    Files per ingestion call (default: 1)
  COGNEE_DATASET       Dataset name override (default: project root folder name)
  COGNEE_INDEX_LOG_LEVEL  Script verbosity: INFO=bar only, DEBUG=bar+batch details
"""

import asyncio
import argparse
import logging
import os
import sys
import warnings
from pathlib import Path

# --- BOOTSTRAP: NOISY IMPORTS ARE FORBIDDEN HERE ---

# Silence specific runtime warnings from third-party libraries (cognee/litellm)
warnings.filterwarnings("ignore", category=RuntimeWarning, message="coroutine '.*' was never awaited")

def _find_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT   = _find_project_root()
COGNEE_VERBOSE = os.getenv("COGNEE_VERBOSE", "false").lower() == "true"
ENV_LOG_LEVEL  = os.getenv("LOG_LEVEL", "ERROR").upper()

# --- PRESERVE REAL TERMINAL ---
# We keep the original streams to bypass global redirection later.
TERM_OUT = sys.stdout
TERM_ERR = sys.stderr

def _bootstrap_logging():
    """
    Absolute Silence Protocol:
    1. Sets up file-based logging for the engine.
    2. Redirects sys.stdout and sys.stderr to the log file (Nuclear Silence).
    3. Silences structlog and noisy third-party loggers.
    """
    logs_dir = PROJECT_ROOT / "scripts" / "cognee" / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    engine_log = logs_dir / "cognee.log"

    level_int = getattr(logging, ENV_LOG_LEVEL, logging.ERROR)

    # 1. Setup File Handler
    file_handler = logging.FileHandler(engine_log, mode="w", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)s: %(message)s")
    )
    file_handler.setLevel(level_int)

    # 2. Configure Root Logger (File Only)
    root = logging.getLogger()
    root.setLevel(level_int)
    root.handlers = [file_handler]

    # 3. Silence Noisy Sub-Loggers
    NOISY = [
        "cognee", "litellm", "transformers", "openai", "instructor",
        "httpcore", "httpx", "urllib3", "sqlalchemy",
        "aiosqlite", "databases", "asyncio",
    ]
    for name in NOISY:
        lg = logging.getLogger(name)
        lg.setLevel(level_int)
        lg.propagate = False
        lg.handlers = [file_handler]

    # 4. Silence Structlog
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

    # 5. --- NUCLEAR SILENCE HIJACK ---
    # We open the log file and replace sys.stdout/stderr.
    # Any library using print() or sys.stderr.write() will now go to the log file.
    if not COGNEE_VERBOSE:
        # We use buffering=1 for line buffering so logs are semi-realtime
        f = open(engine_log, "a", encoding="utf-8", buffering=1)
        sys.stdout = f
        sys.stderr = f

    return engine_log

# Perform bootstrap BEFORE any third-party imports
ENGINE_LOG = _bootstrap_logging()

# --- SAFE IMPORTS ---
import pathspec
from tqdm import tqdm

def _print(msg: str = ""):
    """Write to the REAL terminal (bypasses redirection)."""
    TERM_OUT.write(msg + "\n")
    TERM_OUT.flush()

def _tprint(msg: str):
    """Write through tqdm so the progress bar is not clobbered."""
    tqdm.write(msg, file=TERM_OUT)

def _ignore_spec(root: Path) -> pathspec.PathSpec:
    patterns = [".git/", "**/node_modules/", "__pycache__/", ".venv/"]
    for name in (".cogneeignore", ".gitignore"):
        fp = root / name
        if fp.exists():
            with open(fp, encoding="utf-8", errors="ignore") as f:
                patterns += [l.strip() for l in f if l.strip() and not l.startswith("#")]
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

def _collect_files(root: Path) -> list[str]:
    spec = _ignore_spec(PROJECT_ROOT)
    root_str = str(root.resolve())
    results = []
    for walk_root, dirs, files in os.walk(root_str):
        # Calculate path relative to project root for accurate ignore matching
        rel_walk_root = os.path.relpath(walk_root, str(PROJECT_ROOT))
        if rel_walk_root == ".":
            rel_walk_root = ""
        
        # Filter directories in-place
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_walk_root, d) + "/")]
        
        for fname in files:
            rel_path = os.path.normpath(os.path.join(rel_walk_root, fname))
            # Some pathspecs require a leading slash or specific formatting for root files
            if not spec.match_file(rel_path) and not spec.match_file("/" + rel_path):
                results.append(os.path.join(walk_root, fname))
    return sorted(results)

async def run_index(target_dir: Path, dataset_name: str, batch_size: int, script_log_level: str):
    import cognee # MUST be after bootstrap

    files = _collect_files(target_dir)
    total = len(files)

    if not files:
        _print("  [!] No files found to index.")
        return {"items_processed": 0, "errors": 0}

    _print(f"  {total} files queued  *  batch {batch_size}  *  log -> {ENGINE_LOG.name}")
    _print()

    errors = []
    processed = 0
    error_log = PROJECT_ROOT / "scripts" / "cognee" / "logs" / "errors.log"

    with tqdm(
        total=total,
        desc="Indexing",
        unit="file",
        file=TERM_OUT, # Use real terminal
        leave=True,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        dynamic_ncols=True,
    ) as pbar:
        for i in range(0, total, batch_size):
            batch = files[i : i + batch_size]
            
            # Show current file in description
            current_file_name = Path(batch[0]).name
            pbar.set_description(f"Indexing: {current_file_name}")

            if script_log_level == "DEBUG":
                _tprint(f"  -> processing: {[Path(p).name for p in batch]}")

            try:
                await cognee.remember(data=batch, dataset_name=dataset_name)
                processed += len(batch)
            except (asyncio.CancelledError, KeyboardInterrupt):
                raise
            except Exception as exc:
                errors.append((str(batch), str(exc)))
                _tprint(f"  ✗ error: {exc}")

            pbar.update(len(batch))

    if errors:
        with open(error_log, "w", encoding="utf-8") as f:
            f.write(f"COGNEE INDEXING ERRORS ({len(errors)})\n{'-' * 40}\n")
            for item, err in errors:
                f.write(f"Batch : {item}\nError : {err}\n{'-' * 40}\n")

    return {"items_processed": processed, "errors": len(errors)}

async def main():
    parser = argparse.ArgumentParser(prog="cognee-indexer", description="Cognee workspace indexer")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--dir", metavar="PATH", default=None)
    args = parser.parse_args()

    dataset = os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    batch = int(os.getenv("COGNEE_BATCH_SIZE", "1"))
    script_ll = os.getenv("COGNEE_INDEX_LOG_LEVEL", "INFO").upper()

    if args.dir:
        target = Path(args.dir).resolve()
        mode_label = f"DIR  · {target.relative_to(PROJECT_ROOT)}"
    else:
        target = PROJECT_ROOT
        mode_label = "FULL WORKSPACE"

    _print()
    _print("-------------------------------------------")
    _print(f"|  COGNEE INDEXER  *  {mode_label:<21}|")
    _print(f"|  Dataset: {dataset:<31}|")
    _print(f"|  Verbose: {'ON ' if COGNEE_VERBOSE else 'OFF':<31}|")
    _print("-------------------------------------------")

    try:
        result = await run_index(target, dataset, batch, script_ll)
    except (asyncio.CancelledError, KeyboardInterrupt):
        _print()
        _print("\n  [!]  ABORTED BY USER. Stopping gracefully...")
        return

    _print()
    ok, err = result["items_processed"], result["errors"]
    if err:
        _print(f"  [!] Done  .  {ok} indexed  .  {err} errors  ->  check logs/errors.log")
    else:
        _print(f"\n  [OK]  INDEXING COMPLETE: {ok} files indexed successfully.")
    _print()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        _print("\n  ⊘  Interrupted.")
        sys.exit(0)
    except Exception as e:
        import sys
        print(f"\n  [!] CRITICAL ERROR: {type(e).__name__} - {e}", file=sys.stderr)
        sys.exit(1)
