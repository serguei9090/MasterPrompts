import asyncio
from cognee.api.v1.data import get_data

async def check():
    data = await get_data()
    print(f"Total files in Cognee: {len(data)}")
    for d in data:
        if 'esprima' in d.name.lower():
            print(f"✅ Indexed: {d.name} (Dataset: {d.dataset_id})")
        if 'identifier.js' in d.name.lower():
            print(f"✅ Indexed: {d.name} (Dataset: {d.dataset_id})")

if __name__ == "__main__":
    asyncio.run(check())
