# Retail case — facts, dimensions and grain

Mini dataset used in Bloc 1 Session 2.

The four source tables deliberately represent different grains:
- `customers.csv`: one row per customer;
- `products.csv`: one row per product;
- `orders.csv`: one row per order;
- `order_lines.csv`: one row per order line.

The exercise is to define the analytical grain **before** joining tables, then build a trustworthy sales fact table.
