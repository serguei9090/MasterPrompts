import asyncio
import cognee
from cognee.infrastructure.databases.relational import get_relational_engine

async def check_database():
    print("\n--- COGNEE DATABASE DIAGNOSTIC ---")
    
    # 1. Check Datasets
    datasets = await cognee.get_datasets()
    print(f"\n[1] Registered Datasets ({len(datasets)}):")
    for ds in datasets:
        print(f" - Name: {ds.name} (ID: {ds.id})")

    # 2. Check File Count in relational DB (metadata)
    # Note: We use the internal relational engine to see what Cognee has tracked
    db_engine = get_relational_engine()
    async with db_engine.get_async_session() as session:
        from cognee.modules.ingestion.models import IngestionModel
        from sqlalchemy import select, func
        
        # Count files per dataset
        result = await session.execute(
            select(IngestionModel.name, func.count(IngestionModel.id))
            .group_by(IngestionModel.name)
        )
        counts = result.all()
        print(f"\n[2] Ingested Metadata (Files per Dataset):")
        for ds_name, count in counts:
            print(f" - {ds_name}: {count} files")

if __name__ == "__main__":
    asyncio.run(check_database())
