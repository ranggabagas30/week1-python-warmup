"""Load local configuration from environment variables.

This file demonstrates a common pattern for AI apps: keep secrets like API keys
outside the source code, usually in a local `.env` file.
"""

import os

from dotenv import load_dotenv


# Read key-value pairs from `.env` and add them to the process environment.
# Example `.env` content:
# OPENAI_API_KEY=your_api_key_here
load_dotenv()

# Fetch the API key from the environment.
# `os.environ[...]` raises KeyError if OPENAI_API_KEY is missing, which makes
# configuration problems fail fast instead of silently using an empty value.
API_KEY = os.environ["OPENAI_API_KEY"]
