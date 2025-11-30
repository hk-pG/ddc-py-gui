#!/bin/bash
set -e

echo "Running Linter (ruff)..."
ruff check .
ruff format --check .

echo "Running Tests (pytest)..."
pytest

echo "All checks passed!"
