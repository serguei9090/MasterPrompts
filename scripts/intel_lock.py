"""
IntelLock (Phase 0 Master Script)
=================================
Why: Consolidates the mandatory L1, L2, and L5 research phases into a single atomic operation.
     Reduces context pollution and ensures absolute adherence to the 'Intelligence Lock' protocol.

Mandatory Layers:
- L1 (Physical): Codanna impact & search.
- L2 (Semantic): Cognee memory recall (short-term) and semantic recall (long-term).
- L5 (Operational): Beads task status.

Usage for AI Agents:
    uv run python scripts/intel_lock.py --json '{"bead_id": "...", "query": "...", "symbols": ["..."]}'

AI Protocol:
    1. READ this output carefully before proceeding to Phase 1 (Planning).
    2. USE the 'Actionable Files' and 'Historical Rationale' to ground your plan.
    3. IF 'impact' returns 0 results, check the 'Search Results' for semantic matches.
"""

import argparse
import json
import subprocess
import sys
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def _run_cmd(cmd: List[str]) -> Dict[str, Any]:
    """Run a shell command and return its structured output/error."""
    try:
        # Use shell=True on Windows if needed, but here we prefer direct list execution
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            encoding="utf-8", 
            errors="replace"
        )
        if result.returncode != 0:
            return {
                "success": False,
                "exit_code": result.returncode,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip()
            }
        return {
            "success": True,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def get_beads_info(bead_id: Optional[str] = None) -> Dict[str, Any]:
    """L5 Operational: Fetch task status."""
    cmd = ["bd", "show", bead_id] if bead_id else ["bd", "ready"]
    return _run_cmd(cmd)

def get_cognee_memory(bead_id: str) -> Dict[str, Any]:
    """L2 Short-term: Recall micro-decisions and thought history."""
    cmd = ["uv", "run", "python", "scripts/cognee/memory.py", "recall", bead_id, "--json"]
    res = _run_cmd(cmd)
    if not res["success"]:
        return res
    try:
        return json.loads(res["stdout"])
    except json.JSONDecodeError:
        return {"raw_output": res["stdout"]}

def get_cognee_recall(query: str) -> Dict[str, Any]:
    """L2 Long-term: Recall architectural rationale and lessons."""
    cmd = ["uv", "run", "python", "scripts/cognee/recall.py", query, "--json"]
    res = _run_cmd(cmd)
    if not res["success"]:
        return res
    try:
        return json.loads(res["stdout"])
    except json.JSONDecodeError:
        return {"raw_output": res["stdout"]}

def get_codanna_impact(symbol: str) -> Dict[str, Any]:
    """L1 Physical: Map dependency graph for a symbol."""
    cmd = ["uv", "run", "python", "scripts/codanna/impact.py", symbol]
    return _run_cmd(cmd)

def get_codanna_calls(symbol: str) -> Dict[str, Any]:
    """L1 Physical: Map call sites for a symbol."""
    cmd = ["uv", "run", "python", "scripts/codanna/calls.py", symbol]
    return _run_cmd(cmd)

def get_codanna_docs_search(query: str) -> Dict[str, Any]:
    """L1 Physical Search: Find local patterns and internal docs."""
    cmd = ["uv", "run", "python", "scripts/codanna/docs_search.py", query]
    return _run_cmd(cmd)

def get_codanna_search(query: str) -> Dict[str, Any]:
    """L1 Physical Search: Semantic code/docs search with context."""
    cmd = ["uv", "run", "python", "scripts/codanna/search.py", query, "--context"]
    return _run_cmd(cmd)

def main():
    parser = argparse.ArgumentParser(
        description="IntelLock: Unified Intelligence Gathering for Phase 0."
    )
    parser.add_argument("--json", help="JSON string with research intent keys: bead_id, query, symbols, force_search")
    parser.add_argument("--bead", help="Specific Bead ID to research")
    parser.add_argument("--query", help="Research query for semantic recall and search")
    parser.add_argument("--symbols", nargs="+", help="List of physical symbols to analyze")
    parser.add_argument("--verify", action="store_true", help="Include L1 Verification (calls/docs)")

    args = parser.parse_args()

    # Parse Intent
    intent: Dict[str, Any] = {}
    if args.json:
        try:
            intent = json.loads(args.json)
        except json.JSONDecodeError:
            print(json.dumps({"error": "Invalid JSON input for --json argument"}, indent=2))
            sys.exit(1)
    else:
        intent = {
            "bead_id": args.bead,
            "query": args.query,
            "symbols": args.symbols or [],
            "verify": args.verify
        }

    bead_id = intent.get("bead_id")
    query = intent.get("query")
    symbols = intent.get("symbols", [])
    force_search = intent.get("force_search", False)

    # 1. Operational Context (L5)
    beads_res = get_beads_info(bead_id)
    
    # 2. Semantic Context (L2)
    short_term = get_cognee_memory(bead_id) if bead_id else None
    long_term = get_cognee_recall(query) if query else None

    # 3. Physical Context (L1)
    physical_hits = []
    deep_mode = intent.get("deep", True)  # Default to deep for maximum lock

    for sym in symbols:
        impact = get_codanna_impact(sym)
        calls = get_codanna_calls(sym) if deep_mode else None
        
        physical_hits.append({
            "symbol": sym,
            "impact": impact.get("stdout") if impact["success"] else impact.get("error") or impact.get("stderr"),
            "call_sites": calls.get("stdout") if calls and calls["success"] else None
        })

    # Search Fallback / Augmentation
    search_results = None
    docs_search_results = None
    
    if (not symbols or force_search) and query:
        search_res = get_codanna_search(query)
        search_results = search_res.get("stdout") if search_res["success"] else search_res.get("error") or search_res.get("stderr")
        
        if deep_mode:
            docs_res = get_codanna_docs_search(query)
            docs_search_results = docs_res.get("stdout") if docs_res["success"] else docs_res.get("error") or docs_res.get("stderr")

    # Construct Report
    report = {
        "metadata": {
            "bead_id": bead_id,
            "query": query,
            "symbols_analyzed": symbols
        },
        "operational_sync_l5": {
            "status": "Success" if beads_res["success"] else "Failure",
            "data": beads_res.get("stdout") if beads_res["success"] else beads_res.get("stderr")
        },
        "semantic_memory_l2": {
            "short_term_thought": short_term,
            "long_term_rationale": long_term
        },
        "physical_truth_l1": {
            "impact_analysis": physical_hits,
            "semantic_search": search_results,
            "internal_docs_search": docs_search_results
        }
    }

    # Guidance for the AI
    print("\n" + "="*80)
    print("PHASE 0: INTELLIGENCE LOCK REPORT")
    print("="*80)
    print(json.dumps(report, indent=2, default=str))
    print("\n" + "="*80)
    print("AI GUIDANCE:")
    if not report["operational_sync_l5"]["data"]:
        print("- [!] No active bead detected. Claim a task via 'bd claim' before proceeding.")
    if not symbols and not query:
        print("- [!] Warning: No query or symbols provided. Report reflects general project state.")
    print("- Use 'impact_analysis' to identify files for surgical implementation.")
    print("- Use 'internal_docs_search' to verify local coding patterns and conventions.")
    print("- Use 'long_term_rationale' to ensure architectural compliance.")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
