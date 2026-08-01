# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a small Week 1 Python warmup repository for practicing foundational Python patterns used in AI engineering:

- Pydantic model validation
- Async execution with `asyncio`
- Loading local environment variables from `.env`

There is no package structure, build system, lint configuration, or test suite currently configured. The repository consists of standalone Python scripts intended to be run directly.

## Common commands

### Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

The scripts use Pydantic and python-dotenv:

```bash
python3 -m pip install pydantic python-dotenv
```

### Run the examples

```bash
python3 pydantic_kata.py
python3 async_kata.py
```

Expected behavior:

- `pydantic_kata.py` prints `128.5`
- `async_kata.py` prints `3` and an elapsed time around `1.0`, showing concurrent async execution

### Tests, lint, and build

No test runner, lint command, or build command is configured yet. There is also no single-test command because there are no tests in the repository.

If tests are added later, document the exact test commands here instead of assuming a default framework.

## Code structure

- `pydantic_kata.py` defines a small `Invoice` Pydantic v2 model and validates JSON with `Invoice.model_validate_json(...)`.
- `async_kata.py` demonstrates concurrent async execution using `asyncio.gather(...)` over three simulated LLM calls.
- `config.py` loads `.env` with `python-dotenv` and reads `OPENAI_API_KEY` from the process environment.

The files are independent examples rather than a connected application. Prefer keeping examples simple and runnable as standalone scripts unless the repository is intentionally expanded into a package.

## Environment notes

`config.py` expects an environment variable named `OPENAI_API_KEY`. For local development, place it in `.env`:

```bash
OPENAI_API_KEY=your_api_key_here
```

`.env`, `.venv/`, Python bytecode, and Claude local settings are ignored by `.gitignore`.
