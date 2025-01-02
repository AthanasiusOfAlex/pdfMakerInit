#!/bin/bash
set -e

# Create a virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Use `.venv\Scripts\activate` on Windows

# Install development dependencies
pip install -e ".[dev]"
pip install PyInstaller

# Build the executable
python build_exe.py

echo "Build complete! Executable can be found in dist/ directory"