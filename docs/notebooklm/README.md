# NotebookLM Export

NotebookLM can ingest Markdown more cleanly than raw `.ipynb` files. Jupyter notebooks mix markdown, code, metadata, execution state, and outputs, which can make course material noisy.

This folder contains generated Markdown documents designed for NotebookLM.

## Generate Documents

From the repository root:

```bash
python3 scripts/export_notebooks_to_notebooklm.py
```

Generated files are written to:

```text
docs/notebooklm/generated/
```

## Files To Upload

Recommended upload set:

- `docs/notebooklm/generated/BLOCK_1_Python_Data_Science.md`
- `docs/notebooklm/generated/BLOCK_2_Big_Data_Engineering.md`
- `docs/notebooklm/generated/BLOCK_3_Data_Product_BI_Decision.md`
- `docs/notebooklm/generated/MODERN_AI_DEEP_LEARNING_BRIDGE.md`
- `docs/notebooklm/generated/FINAL_PRODUCT.md`
- `TDSP_TEACHING_LAYER.md`
- `RUN_ALL_COURSE.md`

Optional:

- individual session Markdown files from `docs/notebooklm/generated/`
- `docs/notebooklm/generated/INDEX.md`

Do not upload raw `.ipynb` files unless you specifically want NotebookLM to inspect code syntax and notebook metadata.

## Student Prompt Examples

- "Explain how Bloc 1 turns raw signals into trusted evidence."
- "What outputs should I have after running Bloc 2?"
- "Help me prepare a 3-minute explanation of the final decision product."
- "What are the main limitations of using Google Trends for product decisions?"
- "Explain why deep learning is representation learning rather than magic."
- "Create a checklist for validating my project before submission."
- "Quiz me on the difference between analysis, pipeline artifacts, BI outputs, and final recommendation."
