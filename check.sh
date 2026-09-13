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

"$VENV_PYTHON" - <<'PY'
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
import sklearn
import jupyterlab

required = [
    Path("datasets/retail_case/customers.csv"),
    Path("datasets/retail_case/orders.csv"),
    Path("datasets/retail_case/order_lines.csv"),
    Path("datasets/retail_case/products.csv"),
    Path("notebooks/01_python_data_science/B1_S01_logic_over_code.ipynb"),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit("❌ Fichiers manquants: " + ", ".join(missing))

customers = pd.read_csv(required[0])
orders = pd.read_csv(required[1])
lines = pd.read_csv(required[2])
products = pd.read_csv(required[3])
assert customers["customer_id"].is_unique
assert orders["order_id"].is_unique
assert products["product_id"].is_unique
assert not lines.duplicated(["order_id", "line_id"]).any()
print("✅ Python / NumPy / Pandas / Matplotlib / scikit-learn / JupyterLab")
print("✅ Dataset retail_case")
print("✅ Notebook S1")
print("✅ Test hors-ligne réussi")
PY

if [ "${CHECK_ONLINE:-0}" = "1" ]; then
  "$VENV_PYTHON" - <<'PY'
from pytrends.request import TrendReq
p = TrendReq(hl="fr-FR", tz=360)
p.build_payload(["chatgpt"], timeframe="today 12-m", geo="FR")
df = p.interest_over_time()
print("✅ Test optionnel pytrends, rows:", len(df))
PY
fi
