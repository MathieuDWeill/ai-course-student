#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# shellcheck disable=SC1091
source .venv/bin/activate
VENV_PYTHON=".venv/bin/python"

echo "==> Starting Jupyter Lab..."
"$VENV_PYTHON" -m jupyterlab
