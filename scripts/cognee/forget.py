import asyncio
import os
import logging
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"

async def forget_dataset(dataset_name: str):
    """
    Surgically removes a specific dataset from the user-scoped memory.
    
    Args:
        dataset_name (str): Name of the dataset to delete.
    """
    print(f"\n>>> FORGETTING DATASET: {dataset_name}...")
    try:
        await cognee.forget(dataset_name = dataset_name)
        print(">>> DATASET DELETED.")
    except Exception as e:
        print(f">>> ERROR DELETING DATASET: {e}")

async def main():
    print("\n" + "=" * 70)
    print("--- COGNEE v1.0 MEMORY MANAGEMENT CONSOLE ---")
    print("=" * 70)
    
    try:
        datasets = await cognee.datasets.list_datasets()
        
        if not datasets:
            print("\n[ NO DATASETS FOUND ]")
        else:
            print("\n[ DATASETS ]")
            for i, ds in enumerate(datasets, 1):
                name = getattr(ds, "name", "Unknown")
                print(f"   {i}. Forget: {name}")

        print("\n[ GLOBAL ACTIONS ]")
        print("   A. Forget EVERYTHING (User-scoped wipe)")
        print("   P. PRUNE SYSTEM      (Destructive DB reset)")
        print("   Q. Quit")

        choice = (await asyncio.to_thread(input, "\nSelect an option: ")).strip().upper()

        if choice == "Q":
            return
        elif choice == "A":
            confirm = await asyncio.to_thread(input, "Confirm wipe of ALL user datasets? (y/n): ")
            if confirm.lower() == 'y':
                await cognee.forget()
                print("Global wipe complete.")
        elif choice == "P":
            confirm = await asyncio.to_thread(input, "!!! WARNING: Destructive system prune. Continue? (y/n): ")
            if confirm.lower() == 'y':
                await cognee.prune()
                print("System pruned.")
        else:
            try:
                idx = int(choice) - 1
                target_ds = datasets[idx].name
                await forget_dataset(target_ds)
            except (ValueError, IndexError):
                print("Invalid selection.")

    except Exception as e:
        print(f"Error in management console: {e}")

if __name__ == "__main__":
    asyncio.run(main())
