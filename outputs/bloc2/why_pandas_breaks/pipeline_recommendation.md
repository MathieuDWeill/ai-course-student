# Pipeline Recommendation

Do not run the CEO dashboard directly from raw CSV in a notebook.

Use a Bronze -> Silver -> Gold pipeline:
1. Bronze: raw CSV exports preserved.
2. Silver: cleaned typed Parquet tables.
3. Gold: dashboard aggregates.
4. Monitoring: freshness, row counts, schema checks, failed joins.

Spark or another distributed engine becomes justified when single-machine pandas is too slow, too memory-heavy, or too unreliable for the decision deadline.
