# Week 1 Python Warmup

Small Python warmup repository for Week 1 of the AI Engineering Pivot Program.

This folder contains standalone examples for foundational Python patterns used in AI engineering:

- Data validation with Pydantic
- Concurrent async execution with `asyncio`
- Loading environment variables from `.env`

## Files

| File | Description |
| --- | --- |
| `pydantic_kata.py` | Defines an `Invoice` model with Pydantic and validates JSON input. |
| `async_kata.py` | Demonstrates concurrent async execution with `asyncio.gather`. |
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

Run the Pydantic example:

```bash
python3 pydantic_kata.py
```

Expected output:

```text
128.5
```

Run the async example:

```bash
python3 async_kata.py
```

Expected output is similar to:

```text
3 1.0
```

The elapsed time may vary slightly. The important point is that the three async calls complete in about one second because they run concurrently.

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
! python3 async_kata.py
```
