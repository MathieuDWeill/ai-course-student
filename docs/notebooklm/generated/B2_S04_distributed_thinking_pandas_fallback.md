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
