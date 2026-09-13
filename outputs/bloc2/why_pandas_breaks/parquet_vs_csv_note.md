# Parquet vs CSV Note

CSV is easy to exchange but painful at scale: text parsing, weak schema, no efficient column pruning.

Parquet is better for analytical pipelines: typed columns, compression, columnar reads, and stronger compatibility with distributed engines.

Teaching recommendation: use CSV for first contact, then move curated data to Parquet when repeatability and performance matter.
