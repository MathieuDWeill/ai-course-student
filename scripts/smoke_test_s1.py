"""Smoke test hors-ligne du matériel S1. Lancez depuis la racine du repo."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets" / "retail_case"
files = {name: DATA / f"{name}.csv" for name in ("customers", "orders", "order_lines", "products")}
for path in files.values():
    assert path.exists(), f"Missing {path}"

customers = pd.read_csv(files["customers"])
orders = pd.read_csv(files["orders"])
lines = pd.read_csv(files["order_lines"])
products = pd.read_csv(files["products"])

fact = (lines
        .merge(orders, on="order_id", validate="many_to_one")
        .merge(customers, on="customer_id", validate="many_to_one")
        .merge(products[["product_id", "product_name", "category"]], on="product_id", validate="many_to_one"))
fact["revenue"] = fact["quantity"] * fact["unit_price"]
reference = fact["revenue"].sum()

tags = pd.DataFrame({
    "customer_id": ["C001", "C001", "C002", "C002", "C003", "C003", "C004", "C004", "C005", "C005"],
    "tag": ["newsletter", "vip", "newsletter", "promo", "organic", "loyalty", "partner", "vip", "organic", "promo"],
})
bad = fact.merge(tags, on="customer_id", how="left")
assert len(fact) == len(lines)
assert bad["revenue"].sum() == 2 * reference
try:
    fact.merge(tags, on="customer_id", how="left", validate="many_to_one")
except pd.errors.MergeError:
    pass
else:
    raise AssertionError("Expected MergeError was not raised")

print("S1 smoke test PASS")
print("fact rows:", len(fact))
print("reference revenue:", reference)
print("bad-join revenue:", bad["revenue"].sum())
