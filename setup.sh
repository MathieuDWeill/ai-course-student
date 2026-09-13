#!/usr/bin/env bash
set -euo pipefail

# Toujours se placer à la racine du repo
cd "$(dirname "$0")"

PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "==> Using Python: $PYTHON_BIN"
$PYTHON_BIN --version

if [ ! -d ".venv" ]; then
  echo "==> Creating venv in .venv/"
  $PYTHON_BIN -m venv .venv
else
  echo "==> venv already exists (.venv/)"
fi

echo "==> Activating venv"
# shellcheck disable=SC1091
source .venv/bin/activate
VENV_PYTHON=".venv/bin/python"

echo "==> Upgrading pip"
"$VENV_PYTHON" -m pip install --upgrade pip

echo "==> Installing requirements"
"$VENV_PYTHON" -m pip install -r requirements.txt

echo "✅ Setup complete."
echo "Next: run ./run.sh"
