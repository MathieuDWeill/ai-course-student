# Architecture Note

Pain observed: pandas handles the first analysis, but joins, groupbys, and repeated CSV loading create RAM and runtime pressure.

Architecture response:
- Bronze: keep raw CSV exports.
- Silver: create typed cleaned Parquet tables.
- Gold: publish dashboard-ready aggregates.
- Monitoring: track freshness, row counts, schema, and failed joins.

Big Data starts when single-machine notebooks are no longer reliable enough for the decision process.
