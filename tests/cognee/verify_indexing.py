import asyncio
import os
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import cognee
from cognee.api.v1.search import search

async def check_file_in_cognee(file_path: str):
    """
    Checks if a specific file exists in the Cognee memory graph
    by searching for its filename or path.
    """
    print(f"Checking for file: {file_path}")
    
    # We search the graph for the filename or absolute path
    # 'search' in cognee v1.0 searches the graph nodes.
    try:
        results = await cognee.search(query=f"file:{file_path}", dataset_name="MasterPrompts")
        
        if not results:
            # Try searching just the filename if the full path fails
            filename = os.path.basename(file_path)
            results = await cognee.search(query=filename, dataset_name="MasterPrompts")

        if results:
            print(f"✅ Found {len(results)} potential match(es) in Cognee!")
            for i, res in enumerate(results):
                print(f"--- Match {i+1} ---")
                print(res)
        else:
            print("❌ File not found in Cognee graph.")
            
    except Exception as e:
        print(f"Error querying Cognee: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_indexing.py <file_path_or_name>")
        sys.exit(1)
        
    target = sys.argv[1]
    asyncio.run(check_file_in_cognee(target))
