import asyncio
import os
import logging
import cognee

# --- SILENCE NOISE ---
logging.getLogger("cognee").setLevel(logging.ERROR)
os.environ["LOG_LEVEL"] = "ERROR"

async def get_memory_status():
    """
    Retrieves a diagnostic overview of all Cognee datasets and their content status.
    Uses official v1.0 datasets API (list_datasets, get_status, list_data).
    
    Returns:
        list: A list of Dataset objects with populated item metadata.
    """
    print("\n" + "=" * 60)
    print("--- COGNEE MEMORY STATUS ---")
    print("=" * 60)
    
    try:
        # 1. List all datasets
        datasets = await cognee.datasets.list_datasets()
        
        if not datasets:
            print("\n[ NO DATASETS FOUND ]")
            print("System is currently empty. Use indexer.py or sync.py to add data.")
            return []

        # 2. Get statuses for all datasets in one batch call
        dataset_ids = [ds.id for ds in datasets]
        try:
            all_statuses = await cognee.datasets.get_status(dataset_ids)
        except Exception:
            all_statuses = {}

        for ds in datasets:
            ds_name = getattr(ds, "name", "Unknown")
            ds_id = ds.id
            
            print(f"\n[ DATASET: {ds_name} ]")
            print(f"  - ID: {ds_id}")
            
            # 3. Get specific status from the batch result
            status = all_statuses.get(str(ds_id), all_statuses.get(ds_id, "Unknown"))
            print(f"  - Pipeline Status: {status}")
            
            try:
                # 4. List data items using the dataset_id (UUID)
                data_items = await cognee.datasets.list_data(dataset_id = ds_id)
                print(f"  - Total Root Items: {len(data_items)}")
                
                if data_items:
                    sample_limit = 3
                    print(f"  - Sample Items (First {sample_limit}):")
                    for item in data_items[:sample_limit]:
                        # Try multiple common attributes to find a useful name
                        label = (
                            getattr(item, "label", None) or 
                            getattr(item, "name", None) or 
                            getattr(item, "identifier", None) or 
                            getattr(item, "text", None) or 
                            str(item)
                        )
                        print(f"    * {label}")
            except Exception as item_error:
                print(f"  - Items: Could not retrieve (Error: {item_error})")
        
        print("\n" + "=" * 60)
        return datasets

    except Exception as e:
        print(f"\n>>> ERROR CHECKING STATUS: {e}")
        return []

if __name__ == "__main__":
    asyncio.run(get_memory_status())
