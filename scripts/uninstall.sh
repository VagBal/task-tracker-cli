#!/bin/bash

# Navigate to the root directory where setup.py is located
cd "$(dirname "$0")/.."

# Uninstall the package
pip uninstall -y task_tracker_cli

echo "Package uninstalled successfully."
