"""Small asyncio example for running slow tasks concurrently.

This script simulates calling an LLM three times. Each call waits for one
second, but because the calls run concurrently, the total runtime is about one
second instead of three seconds.
"""

import asyncio
import time


async def call_llm(prompt: str) -> str:
    """Simulate an async LLM/API call.

    `asyncio.sleep(1)` represents waiting for an external service. While this
    coroutine is waiting, Python can continue running other coroutines.
    """

    await asyncio.sleep(1)
    return f"answer to: {prompt}"


async def main():
    """Run several simulated LLM calls at the same time."""

    start = time.perf_counter()

    # Create one coroutine per prompt and run all of them concurrently.
    # `gather` waits until every coroutine finishes and returns their results.
    results = await asyncio.gather(*[call_llm(p) for p in ["a", "b", "c"]])

    # Print the number of results and the elapsed time in seconds.
    print(len(results), round(time.perf_counter() - start, 2))


# Start the async program. Expected output is around: 3 1.0, not 3 seconds.
asyncio.run(main())
