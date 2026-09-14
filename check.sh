#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -f .venv/bin/activate ]; then
  echo "❌ .venv absent. Lancez d'abord: ./setup.sh"
  exit 1
fi
# shellcheck disable=SC1091
source .venv/bin/activate
VENV_PYTHON=".venv/bin/python"

"$VENV_PYTHON" scripts/check_environment.py
