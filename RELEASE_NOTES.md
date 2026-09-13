# Release Notes

## Full Course Structure

The repository is now organized as a practical engineering-school AI teaching system:

- `notebooks/01_python_data_science/`
- `notebooks/02_big_data_engineering/`
- `notebooks/03_data_product_bi_decision/`
- `notebooks/04_final_product/`
- `notebooks/90_kaggle_public/`
- `notebooks/99_templates/`

The naming convention now follows the syllabus: `B1_Sxx`, `B2_Sxx`, `B3_Sxx`, and `FP_01`.

## Three Teaching Blocks

Bloc 1 builds the data science foundation: cleaning, EDA, ML baselines, unsupervised patterns, and reproducible pipelines.

Bloc 2 turns analysis into a lightweight data engineering pipeline: formats, architecture, partitioning, NoSQL views, orchestration, and monitoring.

Bloc 3 turns evidence into decisions: business framing, KPIs, storytelling, BI outputs, A/B testing, prioritization, ROI, and recommendation.

## Kaggle Public Assets

The Kaggle layer includes:

- a Google Trends dataset package;
- a decision-oriented Google Trends notebook;
- a pandas cleaning case study;
- an ML pipeline and deployment-thinking notebook.

These assets support public portfolio building and Kaggle Code + Dataset progression.

## Final Decision Product Pipeline

Running the notebooks in order produces a full data product flow:

raw signals -> clean data -> analysis -> model checks -> pipeline artifacts -> BI outputs -> final recommendation.

The final notebook assembles executive summary, key evidence, model metrics, pipeline status, KPIs, limitations, and next steps.

## How Students Should Start

1. Run `./setup.sh`, then `./check.sh`, then `./run.sh`.
2. Follow `RUN_ALL_COURSE.md`.
3. Start with Bloc 1 session notebooks.
4. Treat every notebook as one step toward the final decision product.
5. Use outputs as evidence, not just completed exercises.
