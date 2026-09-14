from pathlib import Path
import os

import jupyterlab
import matplotlib
import numpy as np
import pandas as pd
import sklearn


required = [
    Path("datasets/retail_case/customers.csv"),
    Path("datasets/retail_case/orders.csv"),
    Path("datasets/retail_case/order_lines.csv"),
    Path("datasets/retail_case/products.csv"),
    Path("notebooks/01_python_data_science/B1_S01_logic_over_code.ipynb"),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit("Fichiers manquants: " + ", ".join(missing))

customers = pd.read_csv(required[0])
orders = pd.read_csv(required[1])
lines = pd.read_csv(required[2])
products = pd.read_csv(required[3])

assert customers["customer_id"].is_unique
assert orders["order_id"].is_unique
assert products["product_id"].is_unique
assert not lines.duplicated(["order_id", "line_id"]).any()

print("OK Python / NumPy / Pandas / Matplotlib / scikit-learn / JupyterLab")
print("OK Dataset retail_case")
print("OK Notebook S1")
print("OK Test hors-ligne reussi")

if os.environ.get("CHECK_ONLINE") == "1":
    from pytrends.request import TrendReq

    p = TrendReq(hl="fr-FR", tz=360)
    p.build_payload(["chatgpt"], timeframe="today 12-m", geo="FR")
    df = p.interest_over_time()
    print("OK Test optionnel pytrends, rows:", len(df))
