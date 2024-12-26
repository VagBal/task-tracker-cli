#!/bin/bash

# Navigate to the root directory where setup.py is located
cd "$(dirname "$0")/.."

# Install the package in editable mode
pip install -e .

echo "Package installed successfully."
