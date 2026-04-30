import asyncio
import os
import logging
from pathlib import Path
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"
os.environ["LITELLM_LOG"] = "ERROR"

def _find_project_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".cogneeignore").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()

PROJECT_ROOT = _find_project_root()

async def improve_memory(dataset_name: str):
    """
    Runs the Cognee Improve pipeline on an existing dataset.
    This enriches the knowledge graph and bridges session memory into the permanent graph.
    
    Args:
        dataset_name (str): The name of the dataset to enrich.
    """
    print(f"\n>>> IMPROVING DATASET: {dataset_name}")
    try:
        await cognee.improve(dataset_name = dataset_name)
        print(">>> ENRICHMENT COMPLETE")
    except Exception as e:
        print(f">>> IMPROVE ERROR: {e}")

async def main():
    print("\n" + "=" * 60)
    print("--- COGNEE v1.0 MEMORY IMPROVEMENT CONSOLE ---")
    print("=" * 60)
    
    datasets = await cognee.datasets.list_datasets()
    default_name = os.getenv("COGNEE_DATASET", PROJECT_ROOT.name)
    
    if not datasets:
        print("No datasets found to improve.")
        return

    print("\nAvailable datasets:")
    for i, ds in enumerate(datasets, 1):
        name = getattr(ds, "name", "Unknown")
        print(f"  {i}. {name}")

    print(f"\nSelect a number, or press Enter for default ({default_name}):")
    choice = input("> ").strip()
    
    if choice == "":
        target_name = default_name
    else:
        try:
            idx = int(choice) - 1
            target_name = datasets[idx].name
        except (ValueError, IndexError):
            print("Invalid selection.")
            return

    await improve_memory(target_name)

if __name__ == "__main__":
    asyncio.run(main())
