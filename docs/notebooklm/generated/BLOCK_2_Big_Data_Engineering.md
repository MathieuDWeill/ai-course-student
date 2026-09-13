# Bloc 2 - Big Data Engineering

# B2_S01 — Why Pandas Breaks

Source notebook: `notebooks/02_big_data_engineering/B2_S01_Why_Pandas_Breaks.ipynb`

## Decision Problem

Not explicitly stated.

## Key Concepts

- data quality
- model validation
- reproducibility
- data engineering
- business decision

## Course Notes

# B2_S01 — Why Pandas Breaks

## Opening hook

The CEO wants the dashboard at **9:00 AM**.

It is **8:47 AM**.

Your notebook has been running for twelve minutes. The fan is screaming. The progress bar is not moving. You try to rerun the groupby. The kernel dies.

Nothing is wrong with your business question. Nothing is wrong with pandas either.

The problem is architectural: you are asking a single-machine, in-memory tool to behave like a production data platform.

**Final lesson:** Big Data starts when pandas stops being enough.

## Decision problem

How do we know when a pandas notebook has become a data engineering problem?

This session starts with failure, not Hadoop theory. Students should feel the pain first: CSV loading, slow groupbys, expensive joins, RAM pressure, and temporary copies.

# Stage 1 — It breaks

A realistic dashboard starts simply: load transactions from CSV, join customer/product tables, compute revenue by month/country/channel/category, and export dashboard tables.

At small scale, pandas feels magical. At larger scale, the same logic becomes fragile.

## 1. Large CSV loading

CSV is convenient, but painful at scale: text parsing, type inference, no column pruning, and weak schema guarantees.

## 2. Slow groupby pressure

The dashboard asks for revenue by month and channel. That requires date parsing, derived columns, and aggregation.

## 3. Expensive joins and temporary copies

Joins are where notebook code starts to feel production-shaped. A merge can duplicate columns, allocate temporary arrays, and multiply memory pressure before the final table exists.

## 4. The hurt, summarized

Pandas is built for single-machine, in-memory analytics. It often creates temporary copies, and those copies can multiply memory usage significantly.

When the dataset grows from thousands to millions to billions of rows, the notebook does not slowly become elegant. It becomes brittle.

# Stage 2 — Why it breaks

The problem is not that pandas is bad. The problem is that the architecture is wrong for the workload.

- **RAM limits:** pandas wants data in memory; joins, strings, derived columns, and filters can create copies.
- **CPU limits:** one machine has limited cores.
- **Vertical scaling limits:** buying a bigger machine works until it becomes too expensive or fragile.
- **I/O bottlenecks:** CSV forces repeated text parsing.
- **Operational limits:** a notebook on one machine is not a reliable 9AM dashboard pipeline.

# Stage 3 — What changes everything

Big Data tools are not magic. They change the execution model.

- **Parquet:** typed, columnar storage; less repeated parsing.
- **Partitioning:** skip irrelevant slices such as dates or countries.
- **Distributed compute:** split work across partitions and machines.
- **Spark mindset:** define transformations, let the engine plan execution.
- **Bronze → Silver → Gold:** raw data, clean validated data, business-ready outputs.

This is why Hadoop/Spark exist. Not because theory says so, but because the 9AM dashboard cannot depend on one dying notebook.

# Stage 4 — Minimal real Spark credibility

You do not need a Hadoop installation to understand the shift.

The key idea: Spark expresses the same business logic as transformations over distributed DataFrames.

# Pipeline recommendation

The 9AM dashboard should not depend on a fragile notebook rerun.

Recommended pipeline:

1. **Bronze:** land raw CSV exports unchanged.
2. **Silver:** validate schema, parse dates, type numeric columns, write Parquet.
3. **Gold:** build dashboard aggregates by month, country, segment, category, and channel.
4. **Monitoring:** check row counts, freshness, failed joins, and output size.
5. **Serving:** BI reads Gold tables, not raw CSV files.

## Practical exercise

Take the dashboard problem and answer:

1. Which step is Bronze?
2. Which table is Silver?
3. Which output is Gold?
4. What would you monitor before the CEO opens the dashboard?
5. At what point would pandas stop being enough?

## Conclusion

Pandas is excellent until the workload becomes too large, too repeated, or too important to depend on a single machine.

Students should leave remembering one sentence:

**Big Data starts when pandas stops being enough.**

## Practical Activities

### Code activity 1

create charts

### Code activity 2

save reusable artifacts

### Code activity 3

load course data

### Code activity 4

aggregate and summarize evidence

### Code activity 5

aggregate and summarize evidence

### Code activity 6

save reusable artifacts; aggregate and summarize evidence

### Code activity 7

create charts

### Code activity 8

run a practical notebook step

### Code activity 9

create charts

### Code activity 10

save reusable artifacts; aggregate and summarize evidence; validate pipeline quality

### Code activity 11

aggregate and summarize evidence

### Code activity 12

save reusable artifacts; aggregate and summarize evidence

### Code activity 13

save reusable artifacts; validate pipeline quality

## Expected Outputs

- No saved output artifact detected.

## Reflection Questions

- How do we know when a pandas notebook has become a data engineering problem?
- 1. Which step is Bronze?
- 2. Which table is Silver?
- 3. Which output is Gold?
- 4. What would you monitor before the CEO opens the dashboard?


---

# Bloc 2.1 — Big Data fundamentals

Source notebook: `notebooks/02_big_data_engineering/B2_S01_big_data_fundamentals.ipynb`

## Decision Problem

when does a data product need engineering discipline instead of another spreadsheet?

## Key Concepts

- data quality
- data engineering
- business decision

## Course Notes

# Bloc 2.1 — Big Data fundamentals

**Decision problem:** when does a data product need engineering discipline instead of another spreadsheet?

Output: dataset inventory for downstream architecture choices.

## Exercise

Add one operational risk that appears when this dataset grows 100x.

## Conclusion

Big Data starts when volume, velocity, variety, or reliability changes the decision process.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc2/data_inventory.csv`

## Reflection Questions

- **Decision problem:** when does a data product need engineering discipline instead of another spreadsheet?


---

# Bloc 2.2 — Data lakes vs warehouses

Source notebook: `notebooks/02_big_data_engineering/B2_S02_data_lake_vs_warehouse.ipynb`

## Decision Problem

where should evidence live so analysts and product teams can trust it?

## Key Concepts

- data quality
- reproducibility
- data engineering
- business decision

## Course Notes

# Bloc 2.2 — Data lakes vs warehouses

**Decision problem:** where should evidence live so analysts and product teams can trust it?

Output: architecture decision note.

## Exercise

Classify one artifact as raw, curated, or data mart.

## Conclusion

Architecture is a decision about trust, reuse, and ownership.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

save reusable artifacts

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc2/architecture_decision.md`
- `outputs/bloc2/lake_warehouse_decision.csv`

## Reflection Questions

- **Decision problem:** where should evidence live so analysts and product teams can trust it?


---

# Bloc 2.3 — File formats: CSV, JSON, Parquet

Source notebook: `notebooks/02_big_data_engineering/B2_S03_file_formats_csv_json_parquet.ipynb`

## Decision Problem

which file format preserves usability without overengineering?

## Key Concepts

- data quality
- data engineering
- business decision

## Course Notes

# Bloc 2.3 — File formats: CSV, JSON, Parquet

**Decision problem:** which file format preserves usability without overengineering?

Output: small format comparison and exported files.

## Exercise

Choose the best format for a BI dashboard and justify the trade-off.

## Conclusion

Formats are product decisions: readability, performance, schema, and interoperability.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; save reusable artifacts

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`

## Reflection Questions

- **Decision problem:** which file format preserves usability without overengineering?


---

# Bloc 2.4 — Spark-style distributed thinking with pandas fallback

Source notebook: `notebooks/02_big_data_engineering/B2_S04_distributed_thinking_pandas_fallback.ipynb`

## Decision Problem

how would this pipeline change if one machine were not enough?

## Key Concepts

- data quality
- reproducibility
- data engineering
- business decision

## Course Notes

# Bloc 2.4 — Spark-style distributed thinking with pandas fallback

**Decision problem:** how would this pipeline change if one machine were not enough?

Output: partition summary using pandas as the local execution engine.

## Exercise

Identify which operation is map-like and which is reduce-like.

## Conclusion

Distributed thinking is about partitioning, aggregating, and minimizing data movement; pandas is enough to teach the pattern.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; save reusable artifacts; aggregate and summarize evidence

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc2/partition_summary.csv`

## Reflection Questions

- **Decision problem:** how would this pipeline change if one machine were not enough?


---

# Bloc 2.5 — NoSQL concepts

Source notebook: `notebooks/02_big_data_engineering/B2_S05_nosql_concepts.ipynb`

## Decision Problem

when is a document view more useful than a relational table?

## Key Concepts

- data quality
- model validation
- business decision

## Course Notes

# Bloc 2.5 — NoSQL concepts

**Decision problem:** when is a document view more useful than a relational table?

Output: document-style signal profiles.

## Exercise

Name one query that is easier with documents and one easier with tables.

## Conclusion

NoSQL is a modeling choice for access patterns, not a badge of modernity.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; save reusable artifacts; aggregate and summarize evidence

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc2/nosql_signal_profiles.json`

## Reflection Questions

- **Decision problem:** when is a document view more useful than a relational table?


---

# Bloc 2.6 — Orchestration and pipeline monitoring

Source notebook: `notebooks/02_big_data_engineering/B2_S06_orchestration_monitoring.ipynb`

## Decision Problem

how do we know the pipeline is fresh, complete, and safe to use?

## Key Concepts

- data quality
- model validation
- reproducibility
- data engineering
- business decision

## Course Notes

# Bloc 2.6 — Orchestration and pipeline monitoring

**Decision problem:** how do we know the pipeline is fresh, complete, and safe to use?

Output: monitoring report.

## Exercise

Add one freshness check and one schema check.

## Conclusion

Monitoring converts pipelines from scripts into reliable decision infrastructure.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc1/model_metrics.csv`
- `outputs/bloc2/format_comparison.csv`
- `outputs/bloc2/partition_summary.csv`
- `outputs/bloc2/pipeline_monitoring_report.csv`

## Reflection Questions

- **Decision problem:** how do we know the pipeline is fresh, complete, and safe to use?


---

# Bloc 2.7 — Mini pipeline project

Source notebook: `notebooks/02_big_data_engineering/B2_S07_mini_pipeline_project.ipynb`

## Decision Problem

can the data product be rebuilt from raw signal to monitored artifact?

## Key Concepts

- data quality
- reproducibility
- data engineering
- business decision

## Course Notes

# Bloc 2.7 — Mini pipeline project

**Decision problem:** can the data product be rebuilt from raw signal to monitored artifact?

Output: Bloc 2 pipeline manifest.

## Exercise

Explain which artifact you would hand to an analyst, an engineer, and a stakeholder.

## Conclusion

Bloc 2 turns analysis into a small but inspectable data product pipeline.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc2/mini_pipeline_manifest.json`

## Reflection Questions

- **Decision problem:** can the data product be rebuilt from raw signal to monitored artifact?


---
