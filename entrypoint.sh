#!/bin/bash
set -e

# Compile all .cpp files in the /workspace directory (mounted at runtime)
for file in /workspace/*.cpp; do
    [ -e "$file" ] || continue
    exe="/workspace/$(basename "$file" .cpp)"
    g++ "$file" -o "$exe"
done

# If a test script is provided, run it with Python
if [ -n "$TEST_SCRIPT" ]; then
    python "/workspace/$TEST_SCRIPT"
# Otherwise, run Flask app if present
elif [ -f /workspace/app.py ]; then
    python /workspace/app.py
else
    echo "No test script or app.py found."
    ls -l /workspace
fi
