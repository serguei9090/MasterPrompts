"""
Cognee Indexer — Clean, silent, progress-tracked ingestion.

Environment Variables:
  LOG_LEVEL            Engine log level routed to the log file (default: ERROR)
  COGNEE_VERBOSE       "true" to also print engine logs to the console (default: false)
  COGNEE_BATCH_SIZE    Files per ingestion call (default: 1)
  COGNEE_DATASET       Dataset name override (default: project root folder name)
  COGNEE_INDEX_LOG_LEVEL  Script verbosity: INFO=bar only, DEBUG=bar+batch details

Process Safety:
  Uses a PID file (logs/indexer.pid) to prevent concurrent runs and detect
  zombie processes. On Ctrl+C or crash, atexit + signal handlers guarantee cleanup.
"""

import asyncio
import argparse
import atexit
import logging
import os
import signal
import sys
import warnings
from pathlib import Path

try:
    import psutil
    _PSUTIL_AVAILABLE = True
except ImportError:
    _PSUTIL_AVAILABLE = False

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

# --- PID FILE: Zombie Prevention ---
PID_FILE = PROJECT_ROOT / "scripts" / "cognee" / "logs" / "indexer.pid"

def _is_pid_alive(pid: int) -> bool:
    """Check if a process with the given PID is still running (cross-platform)."""
    try:
        os.kill(pid, 0)  # Signal 0 = probe only, doesn't actually send a signal
        return True
    except (OSError, ProcessLookupError):
        return False

def _write_pid() -> None:
    """Write current PID to the lockfile. Called at startup."""
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()), encoding="utf-8")

def _cleanup_pid() -> None:
    """Remove PID lockfile. Registered with atexit — runs on any exit."""
    try:
        if PID_FILE.exists():
            PID_FILE.unlink()
    except OSError:
        pass

def _check_existing_process() -> bool:
    """
    Detect a concurrently running indexer.
    Returns True if safe to proceed, False if another live instance is found.
    Automatically cleans up stale PID files from crashed runs.
    """
    if not PID_FILE.exists():
        return True
    try:
        existing_pid = int(PID_FILE.read_text(encoding="utf-8").strip())
        if existing_pid == os.getpid():
            return True  # Same process (e.g. re-entrant call)
        if _is_pid_alive(existing_pid):
            return False  # Live zombie — abort
        # Stale PID from a previous crash — safe to overwrite
        PID_FILE.unlink(missing_ok=True)
        return True
    except (ValueError, OSError):
        PID_FILE.unlink(missing_ok=True)
        return True

STOP_REQUESTED = False

def _setup_signal_handlers() -> None:
    """Intercept Ctrl+C and SIGTERM for graceful shutdown."""
    def _handle(signum, frame):
        global STOP_REQUESTED
        if not STOP_REQUESTED:
            STOP_REQUESTED = True
            # We use _print to ensure it goes to the real terminal even if redirected
            _print("\n  [!] STOP REQUESTED: Finishing current batch...")
        else:
            _print("\n  [!] FORCE STOPPING...")
            # We don't use sys.exit here directly to avoid asyncio hang; 
            # instead, we kill the process group to be sure.
            os._exit(1)

    try:
        signal.signal(signal.SIGINT, _handle)
        signal.signal(signal.SIGTERM, _handle)
    except (OSError, ValueError):
        pass  # Can't set signals in non-main threads — silently skip

def _find_rogue_indexers() -> list:
    """
    Scan all Python processes for any that are running indexer.py.
    This catches zombies that existed BEFORE the PID file feature, or
    processes that crashed before writing their PID file.
    Returns list of (pid, memory_mb) tuples excluding the current process.
    """
    if not _PSUTIL_AVAILABLE:
        return []
    rogues = []
    my_pid = os.getpid()
    my_ppid = os.getppid()
    try:
        for proc in psutil.process_iter(["pid", "name", "cmdline", "memory_info"]):
            pid = proc.info.get("pid")
            if pid in (my_pid, my_ppid):
                continue
            
            # Must strictly be a python process (ignores uv.exe, bash, powershell, etc.)
            proc_name = (proc.info.get("name") or "").lower()
            if "python" not in proc_name:
                continue
                
            cmdline = proc.info.get("cmdline") or []
            if any("indexer.py" in arg for arg in cmdline):
                mem_mb = round(proc.info["memory_info"].rss / 1024 / 1024, 1)
                rogues.append((proc.info["pid"], mem_mb))
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    return rogues

def _kill_rogue_indexers() -> int:
    """Kill all rogue indexer.py processes. Returns count killed."""
    rogues = _find_rogue_indexers()
    killed = 0
    for pid, mem_mb in rogues:
        try:
            proc = psutil.Process(pid)
            proc.kill()
            print(f"  [✓] Killed PID {pid} ({mem_mb}MB)", flush=True)
            killed += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"  [!] Could not kill PID {pid}: {e}", flush=True)
    # Also clean up any stale PID file
    PID_FILE.unlink(missing_ok=True)
    return killed

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
                for line in f:
                    line = line.split("#")[0].strip()
                    if line:
                        patterns.append(line)
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
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.join(rel_walk_root, d).replace("\\", "/") + "/")]
        
        for fname in files:
            rel_path = os.path.normpath(os.path.join(rel_walk_root, fname)).replace("\\", "/")
            # Some pathspecs require a leading slash or specific formatting for root files
            if not spec.match_file(rel_path) and not spec.match_file("/" + rel_path):
                results.append(os.path.join(walk_root, fname))
    return sorted(results)

async def run_index(target_dir: Path, dataset_name: str, batch_size: int, script_log_level: str, explicit_files: list[str] = None):
    import cognee # MUST be after bootstrap

    spec = _ignore_spec(PROJECT_ROOT)
    if explicit_files:
        files = []
        for f in explicit_files:
            abs_f = os.path.abspath(f)
            if not os.path.exists(abs_f):
                continue
            rel_path = os.path.relpath(abs_f, str(PROJECT_ROOT)).replace("\\", "/")
            if not spec.match_file(rel_path) and not spec.match_file("/" + rel_path):
                files.append(abs_f)
    else:
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
                if STOP_REQUESTED:
                    _tprint("  [!] Breaking loop for graceful exit...")
                    break
                
                await cognee.remember(data=batch, dataset_name=dataset_name)
                processed += len(batch)
            except (asyncio.CancelledError, KeyboardInterrupt):
                _tprint("  [!] Interrupted during I/O operation.")
                break
            except Exception as exc:
                msg = str(exc)
                if "Could not set lock on file" in msg:
                    _tprint(f"  [!] DATABASE LOCKED: Another process is using the database.")
                    _tprint(f"      Close other AI tools or check for zombie processes.")
                    errors.append((str(batch), "DATABASE_LOCKED"))
                    # If the database is locked, we can't proceed with other batches either
                    return {"items_processed": processed, "errors": len(errors), "locked": True}
                
                errors.append((str(batch), msg))
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
    parser.add_argument("--dataset", help="Optional: Specific dataset name to target")
    parser.add_argument("--kill", action="store_true", help="Kill any running indexer processes and exit")
    parser.add_argument("--reset", action="store_true", help="Clear the current dataset and exit")
    parser.add_argument("files", nargs="*", help="Specific files to index")
    args = parser.parse_args()

    # --- --kill mode: nuke all rogue indexers ---
    if args.kill:
        if not _PSUTIL_AVAILABLE:
            _print("  [!] psutil not installed. Run: uv add psutil")
            sys.exit(1)
        rogues = _find_rogue_indexers()
        if not rogues:
            _print("  [✓] No rogue indexer processes found.")
        else:
            _print(f"  Found {len(rogues)} rogue indexer(s):")
            count = _kill_rogue_indexers()
            _print(f"  [✓] Killed {count} process(es). Database lock released.")
        sys.exit(0)

    # --- --reset mode: clear the dataset ---
    dataset = args.dataset or os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    if getattr(args, "reset", False):
        import cognee
        _print(f"  [!] Resetting dataset: {dataset}...")
        try:
            await cognee.forget(dataset=dataset)
            _print(f"  [✓] Dataset '{dataset}' cleared successfully.")
        except Exception as e:
            _print(f"  [✗] Failed to reset dataset: {e}")
        sys.exit(0)

    # --- PROCESS SAFETY: Zombie Detection + PID Lock ---
    _setup_signal_handlers()

    # Pre-flight: detect zombies that predate PID file system (e.g. old full-index runs)
    if _PSUTIL_AVAILABLE:
        rogues = _find_rogue_indexers()
        if rogues:
            pids = ", ".join(f"{pid} ({mb}MB)" for pid, mb in rogues)
            _print(f"  [!] Rogue indexer(s) detected: {pids}")
            _print(f"      Run with --kill to terminate them, then retry.")
            sys.exit(1)

    if not _check_existing_process():
        existing_pid = PID_FILE.read_text(encoding="utf-8").strip()
        _print(f"  [!] Another indexer is already running (PID {existing_pid}).")
        _print(f"      Wait for it to finish, or run with --kill to force stop.")
        sys.exit(1)
    _write_pid()
    atexit.register(_cleanup_pid)  # Guaranteed cleanup: crash, Ctrl+C, or normal exit
    # --- END PROCESS SAFETY ---

    dataset = args.dataset or os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    batch = int(os.getenv("COGNEE_BATCH_SIZE", "10"))
    script_ll = os.getenv("COGNEE_INDEX_LOG_LEVEL", "INFO").upper()

    if args.files:
        mode_label = f"FILES · {len(args.files)} specified"
        target = PROJECT_ROOT
    elif args.dir:
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
        result = await run_index(target, dataset, batch, script_ll, explicit_files=args.files)
    except (asyncio.CancelledError, KeyboardInterrupt):
        _print()
        _print("\n  [!] ABORTED: Stopped by user.")
        return

    _print()
    ok, err = result["items_processed"], result["errors"]
    
    if result.get("locked"):
        _print(f"  [!] ABORTED: Database is locked by another process.")
        _print(f"      Check if your IDE or another agent is running Cognee.")
        sys.exit(1)
    
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
