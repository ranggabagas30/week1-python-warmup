# Week 1 Python Warmup

Small Python warmup repository for Week 1 of the AI Engineering Pivot Program.

This folder contains standalone examples for foundational Python patterns used in AI engineering:

- Data validation with Pydantic
- Nested data models with Pydantic
- Concurrent async execution with `asyncio`
- Limiting async concurrency with `asyncio.Semaphore`
- Loading environment variables from `.env`

## Files

| File | Description |
| --- | --- |
| `pydantic_kata.py` | Basic Pydantic example that defines an `Invoice` model and validates JSON input. |
| `pydantic_kata2.py` | Beginner-friendly Pydantic example with detailed comments for imports, models, fields, validation rules, invalid data handling, and nested `Patient` / `Nurse` models. |
| `async_kata.py` | Basic async example that demonstrates concurrent execution with `asyncio.gather`. |
| `async_kata2.py` | Beginner-friendly async example with detailed comments for `async`, `await`, coroutines, `asyncio.gather`, timing, and optional concurrency limiting with `asyncio.Semaphore`. |
| `config.py` | Loads `OPENAI_API_KEY` from the environment using `python-dotenv`. |
| `.env` | Local environment file for secrets. This file should not be committed. |

## Requirements

Recommended:

- Python 3.10+
- `pydantic`
- `python-dotenv`

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install pydantic python-dotenv
```

## Run the examples

### Basic Pydantic example

Run:

```bash
python3 pydantic_kata.py
```

Expected output:

```text
128.5
```

This example shows how Pydantic can validate JSON data and turn it into a Python object.

### Commented Pydantic example

Run:

```bash
python3 pydantic_kata2.py
```

Expected output includes:

- A valid `TraineeProfile` object
- A `ValidationError` for invalid `years_experience`
- A valid `Patient` object
- A valid nested `Nurse` object containing a list of patients

This example explains important Pydantic concepts such as:

- `BaseModel`: the parent class for validated data models
- `Field`: a helper for adding validation rules and metadata
- `ValidationError`: the exception raised when validation fails
- `Field(...)`: marks a field as required while adding extra rules
- `ge=0`: means "greater than or equal to zero"
- `min_length` and `max_length`: string length validation rules
- `model_validate_json(...)`: validates data from a JSON string
- `model_validate(...)`: validates data from a Python dictionary

### Basic async example

Run:

```bash
python3 async_kata.py
```

Expected output is similar to:

```text
3 1.0
```

The elapsed time may vary slightly. The important point is that the three async calls complete in about one second because they run concurrently.

### Commented async example

Run:

```bash
python3 async_kata2.py
```

Expected output is similar to:

```text
5 results in 1.0 s
```

This example explains important async concepts such as:

- `async def`: defines a coroutine function
- Coroutine: async work that must be awaited before getting the final result
- `await`: pauses one coroutine while allowing other async tasks to keep running
- `asyncio.sleep(...)`: simulates slow I/O without blocking the whole program
- `asyncio.gather(...)`: runs multiple coroutines concurrently and waits for all results
- `*tasks`: unpacks a list so each coroutine is passed separately to `gather`
- `time.perf_counter()`: measures elapsed runtime accurately
- `asyncio.run(...)`: starts the event loop and runs the top-level coroutine

`async_kata2.py` also includes an optional `fetch_limited(...)` example using `asyncio.Semaphore(3)`. A semaphore limits how many tasks can run at the same time. For example, 10 one-second tasks with a limit of 3 run in waves and finish in about 4 seconds instead of starting all 10 at once.

## Environment variables

`config.py` expects an environment variable named `OPENAI_API_KEY`.

Create a `.env` file in this folder:

```bash
OPENAI_API_KEY=your_api_key_here
```

Then `config.py` can load it with:

```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ["OPENAI_API_KEY"]
```

## Running from Claude Code

If you want to run commands directly from the Claude Code prompt, use the `!` prefix:

```bash
! python3 pydantic_kata.py
! python3 pydantic_kata2.py
! python3 async_kata.py
! python3 async_kata2.py
```
