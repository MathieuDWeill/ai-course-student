# Run All Course

Goal: run the course as one coherent data product pipeline.

Pipeline:
raw signals -> clean data -> analysis -> models -> pipeline artifacts -> BI outputs -> decision recommendation

## Output structure

```text
outputs/
  bloc1/          clean data, EDA, features, model metrics
  bloc2/          architecture, formats, partitions, monitoring
  bloc3/          KPIs, dashboard data, experiment plan, ROI
  modern_ai_deep_learning/  representation learning bridge
  final_product/  executive summary and final decision assets
```

## Recommended notebook order

Bloc 1 - Data Science foundation:
1. `notebooks/01_python_data_science/B1_S02_pandas_cleaning_alignment.ipynb`
2. `notebooks/01_python_data_science/B1_S03_eda_visualization_storytelling.ipynb`
3. `notebooks/01_python_data_science/B1_S04_supervised_ml_baseline.ipynb`
4. `notebooks/01_python_data_science/B1_S05_unsupervised_patterns.ipynb`
5. `notebooks/01_python_data_science/B1_S06_reproducible_data_science_pipeline.ipynb`
6. `notebooks/01_python_data_science/B1_S07_S08_guided_project_restitution.ipynb`

Bloc 2 - Data engineering layer:
1. `notebooks/02_big_data_engineering/B2_S01_big_data_fundamentals.ipynb`
2. `notebooks/02_big_data_engineering/B2_S02_data_lake_vs_warehouse.ipynb`
3. `notebooks/02_big_data_engineering/B2_S03_file_formats_csv_json_parquet.ipynb`
4. `notebooks/02_big_data_engineering/B2_S04_distributed_thinking_pandas_fallback.ipynb`
5. `notebooks/02_big_data_engineering/B2_S05_nosql_concepts.ipynb`
6. `notebooks/02_big_data_engineering/B2_S06_orchestration_monitoring.ipynb`
7. `notebooks/02_big_data_engineering/B2_S07_mini_pipeline_project.ipynb`

Bloc 3 - BI and decision layer:
1. `notebooks/03_data_product_bi_decision/B3_S01_business_problem_framing.ipynb`
2. `notebooks/03_data_product_bi_decision/B3_S02_kpi_design.ipynb`
3. `notebooks/03_data_product_bi_decision/B3_S03_data_storytelling.ipynb`
4. `notebooks/03_data_product_bi_decision/B3_S04_dashboarding_bi.ipynb`
5. `notebooks/03_data_product_bi_decision/B3_S05_ab_testing.ipynb`
6. `notebooks/03_data_product_bi_decision/B3_S06_prioritization_roi.ipynb`
7. `notebooks/03_data_product_bi_decision/B3_S07_final_recommendation.ipynb`

Optional but recommended - Modern AI / Deep Learning Bridge:
1. `notebooks/05_modern_ai_deep_learning/DL_S01_Why_Deep_Learning_Changed_Everything.ipynb`

Final assembly:
1. `notebooks/04_final_product/FP_01_final_decision_product.ipynb`

## What each block produces

Bloc 1:
- `clean_trends_wide.csv`
- `clean_trends_long.csv`
- `data_quality_report.csv`
- `eda_signal_summary.csv`
- `eda_weak_signals.png`
- `feature_table.csv`
- `model_metrics.csv`
- `attention_regimes.csv`
- `pipeline_validation_report.csv`
- `project_brief.md`

Bloc 2:
- `data_inventory.csv`
- `lake_warehouse_decision.csv`
- `architecture_decision.md`
- `format_comparison.csv`
- CSV/JSON/Parquet exports when supported
- `partition_summary.csv`
- `nosql_signal_profiles.json`
- `pipeline_monitoring_report.csv`
- `mini_pipeline_manifest.json`

Bloc 3:
- `problem_framing.md`
- `kpi_definitions.csv`
- `kpi_snapshot.csv`
- `storytelling_chart.png`
- `dashboard_dataset.csv`
- `ab_test_plan.csv`
- `prioritization_roi.csv`
- `final_recommendation.md`

Modern AI / Deep Learning Bridge:
- `representation_learning_note.md`
- `model_metrics.csv`
- `modern_ai_bridge_summary.md`

Final product:
- `executive_summary.md`
- `final_signal_summary.csv`
- `final_model_metrics.csv`
- `final_pipeline_status.csv`
- `final_kpi_snapshot.csv`
- `final_manifest.json`

## How outputs connect

Bloc 1 creates trusted analytical evidence.

Bloc 2 turns that evidence into a lightweight data product pipeline.

Bloc 3 turns the pipeline into KPIs, BI artifacts, experiment logic, and prioritization.

The Modern AI bridge explains why learned representations matter for NLP, vision, recommendations, transformers, and LLMs.

The final notebook consumes the previous outputs and writes the executive recommendation.

## Local execution

Run notebooks manually in JupyterLab:

```bash
./run.sh
```

Or execute one notebook from the terminal:

```bash
.venv/bin/jupyter nbconvert --to notebook --execute notebooks/01_python_data_science/B1_S02_pandas_cleaning_alignment.ipynb --output /tmp/S2.ipynb
```

No Spark, Docker, or external infrastructure is required.
