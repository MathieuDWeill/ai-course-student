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
