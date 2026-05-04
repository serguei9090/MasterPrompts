import asyncio
import cognee

async def session_demo():
    # 1. Choose a Session ID (Like a Bead ID)
    session_id = "DEMO-SESSION-123"
    
    print(f"\n[1] Saving context to Session: {session_id}")
    await cognee.remember(
        "The project uses Biome for linting and Ruff for Python quality.",
        dataset_name = "test_memory",
        session_id = session_id
    )
    print(">>> Context saved.")

    print(f"\n[2] Recalling context for Session: {session_id}")
    # We ask a question specifically about the decisions in this session
    results = await cognee.recall(
        "What tools are we using for linting and quality?",
        session_id = session_id
    )

    print("\n>>> RECALL RESULTS:")
    if results:
        for res in results:
            print(f"- {res}")
    else:
        print("No results found.")

if __name__ == "__main__":
    asyncio.run(session_demo())
