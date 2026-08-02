# Import the tools used in this async example.
# - asyncio: Python's built-in library for writing asynchronous/concurrent code.
# - time: Python's built-in library for measuring elapsed time in this script.
import asyncio
import time


# async def creates an asynchronous function, also called a coroutine function.
# Calling fetch_result(...) does not immediately return the final string.
# Instead, it creates a coroutine that must be awaited later.
#
# source: str is a type hint that says source should be a string.
# -> str is a return type hint that says this function eventually returns a string.
async def fetch_result(source: str) -> str:
    # await means "pause this coroutine until the awaited operation finishes."
    # asyncio.sleep(1) simulates a slow I/O task, such as calling an LLM API,
    # reading from a database, or downloading data from the internet.
    # Unlike time.sleep(1), asyncio.sleep(1) does not block the whole program.
    # While this coroutine is sleeping, other async tasks can run.
    await asyncio.sleep(1)

    # After the simulated delay finishes, return a string result for this source.
    return f"data from {source}"


SEM = asyncio.Semaphore(3)  # Limit to 3 concurrent tasks
async def fetch_limited(source: str) -> str: 
    async with SEM: 
        print(f"{time.perf_counter():.1f}s start{source}")
        return await fetch_result(source)
        # in main(): gather fetch_limited for range(10) -> ~4s total, waves of 3

# main is the top-level coroutine that coordinates the async work.
# -> None means this function is not expected to return a useful value.
async def main() -> None:
    # time.perf_counter() gives a high-resolution timer.
    # We store the start time so we can measure how long the async work takes.
    t = time.perf_counter()

    # range(5) creates the numbers 0, 1, 2, 3, and 4.
    # f"s{i}" turns each number into a source name: s0, s1, s2, s3, s4.
    # fetch_result(f"s{i}") creates five coroutine objects.
    tasks = [fetch_result(f"s{i}") for i in range(5)]
    
    # If you want to limit the number of concurrent tasks, you can use fetch_limited instead of fetch_result.
    #tasks = [fetch_limited(f"s{i}") for i in range(10)]

    # asyncio.gather runs the five coroutines concurrently and waits until all
    # of them finish. Because they all sleep at the same time, the total runtime
    # is around 1 second instead of around 5 seconds.
    #
    # The * operator unpacks the list, so gather receives each coroutine as a
    # separate argument: gather(task1, task2, task3, task4, task5).
    out = await asyncio.gather(*tasks)

    # len(out) counts how many results came back.
    # time.perf_counter() - t calculates elapsed time.
    # round(..., 2) keeps only two decimal places for cleaner output.
    print(len(out), "results in", round(time.perf_counter() - t, 2), "s")


# asyncio.run starts the async event loop, runs main(), and closes the loop when done.
# In normal Python scripts, this is the standard way to start async code.
asyncio.run(main())
