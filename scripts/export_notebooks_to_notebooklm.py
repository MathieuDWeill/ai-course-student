#!/usr/bin/env python3
"""Export course notebooks to NotebookLM-ready Markdown.

The exporter keeps markdown structure, converts code cells into short
"Code activity" summaries, and ignores outputs/execution noise.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_GROUPS = [
    ("BLOCK_1_Python_Data_Science.md", "Bloc 1 - Python Data Science", ROOT / "notebooks" / "01_python_data_science"),
    ("BLOCK_2_Big_Data_Engineering.md", "Bloc 2 - Big Data Engineering", ROOT / "notebooks" / "02_big_data_engineering"),
    ("BLOCK_3_Data_Product_BI_Decision.md", "Bloc 3 - Data Product BI Decision", ROOT / "notebooks" / "03_data_product_bi_decision"),
    ("MODERN_AI_DEEP_LEARNING_BRIDGE.md", "Modern AI - Deep Learning Bridge", ROOT / "notebooks" / "05_modern_ai_deep_learning"),
    ("FINAL_PRODUCT.md", "Final Product", ROOT / "notebooks" / "04_final_product"),
]
OUTPUT_DIR = ROOT / "docs" / "notebooklm" / "generated"


def text_from_source(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source or "")


def clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def first_heading(markdown_chunks: list[str], fallback: str) -> str:
    for chunk in markdown_chunks:
        for line in chunk.splitlines():
            if line.startswith("#"):
                return line.lstrip("#").strip()
    return fallback


def extract_decision_problem(markdown: str) -> str:
    match = re.search(r"\*\*Decision problem:\*\*\s*(.+)", markdown)
    if match:
        return match.group(1).strip()
    return "Not explicitly stated."


def code_activity_summary(code: str) -> str:
    code_lower = code.lower()
    activities: list[str] = []
    if "read_csv" in code_lower or "load_" in code_lower:
        activities.append("load course data")
    if "to_csv" in code_lower or "to_json" in code_lower or "to_parquet" in code_lower or "write_text" in code_lower:
        activities.append("save reusable artifacts")
    if "plot" in code_lower or "savefig" in code_lower:
        activities.append("create charts")
    if "groupby" in code_lower or "agg(" in code_lower:
        activities.append("aggregate and summarize evidence")
    if "sklearn" in code_lower or ".fit(" in code_lower or "logisticregression" in code_lower or "kmeans" in code_lower:
        activities.append("train or evaluate a model")
    if "assert" in code_lower or "validation" in code_lower or "monitor" in code_lower:
        activities.append("validate pipeline quality")
    if not activities:
        activities.append("run a practical notebook step")
    return "; ".join(dict.fromkeys(activities))


def expected_outputs(code_cells: list[str]) -> list[str]:
    outputs: list[str] = []
    pattern = re.compile(r'OUT\s*/\s*["\']([^"\']+)["\']\s*/\s*["\']([^"\']+)["\']')
    for code in code_cells:
        for block, filename in pattern.findall(code):
            outputs.append(f"outputs/{block}/{filename}")
    return sorted(set(outputs))


def reflection_questions(markdown: str) -> list[str]:
    questions: list[str] = []
    for line in markdown.splitlines():
        clean = line.strip("- ").strip()
        if clean.endswith("?"):
            questions.append(clean)
    if not questions:
        questions.append("What decision does this notebook make easier or safer?")
        questions.append("What limitation should be communicated before using the output?")
    return questions[:5]


def key_concepts(markdown: str, code_cells: list[str]) -> list[str]:
    concepts: list[str] = []
    lowered = markdown.lower() + "\n" + "\n".join(code_cells).lower()
    candidates = [
        ("data quality", ["missing", "duplicate", "clean"]),
        ("exploratory analysis", ["eda", "visualization", "storytelling"]),
        ("model validation", ["baseline", "model", "metrics", "error"]),
        ("reproducibility", ["pipeline", "manifest", "artifact"]),
        ("data engineering", ["lake", "warehouse", "format", "partition", "monitor"]),
        ("business decision", ["decision", "recommendation", "kpi", "roi"]),
        ("experimentation", ["a/b", "experiment", "guardrail"]),
        ("representation learning", ["deep learning", "representation", "embedding", "neural", "transformer", "llm"]),
    ]
    for label, needles in candidates:
        if any(needle in lowered for needle in needles):
            concepts.append(label)
    return concepts[:6] or ["decision-oriented data work"]


def export_notebook(path: Path) -> tuple[str, str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    markdown_chunks: list[str] = []
    code_cells: list[str] = []

    for cell in notebook.get("cells", []):
        cell_type = cell.get("cell_type")
        source = text_from_source(cell.get("source"))
        if cell_type == "markdown":
            cleaned = clean_markdown(source)
            if cleaned:
                markdown_chunks.append(cleaned)
        elif cell_type == "code":
            stripped = source.strip()
            if stripped:
                code_cells.append(stripped)

    full_markdown = "\n\n".join(markdown_chunks)
    title = first_heading(markdown_chunks, path.stem)
    decision = extract_decision_problem(full_markdown)
    outputs = expected_outputs(code_cells)
    concepts = key_concepts(full_markdown, code_cells)
    questions = reflection_questions(full_markdown)

    parts = [
        f"# {title}",
        f"Source notebook: `{path.relative_to(ROOT)}`",
        "## Decision Problem",
        decision,
        "## Key Concepts",
        "\n".join(f"- {concept}" for concept in concepts),
        "## Course Notes",
        full_markdown or "No markdown notes were found.",
        "## Practical Activities",
    ]

    if code_cells:
        for idx, code in enumerate(code_cells, start=1):
            parts.append(f"### Code activity {idx}\n\n{code_activity_summary(code)}")
    else:
        parts.append("No code activities were found.")

    parts.extend([
        "## Expected Outputs",
        "\n".join(f"- `{output}`" for output in outputs) if outputs else "- No saved output artifact detected.",
        "## Reflection Questions",
        "\n".join(f"- {question}" for question in questions),
    ])

    document = "\n\n".join(parts).strip() + "\n"
    output_name = path.with_suffix(".md").name
    output_path = OUTPUT_DIR / output_name
    output_path.write_text(document, encoding="utf-8")
    return output_name, document


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_lines = ["# NotebookLM Generated Documents", ""]

    for combined_name, block_title, folder in NOTEBOOK_GROUPS:
        block_docs: list[str] = [f"# {block_title}", ""]
        notebooks = sorted(folder.glob("*.ipynb"))
        index_lines.append(f"## {block_title}")
        for notebook in notebooks:
            output_name, document = export_notebook(notebook)
            index_lines.append(f"- `{output_name}` from `{notebook.relative_to(ROOT)}`")
            block_docs.append(document)
            block_docs.append("\n---\n")
        combined_path = OUTPUT_DIR / combined_name
        combined_path.write_text("\n".join(block_docs).strip() + "\n", encoding="utf-8")
        index_lines.append(f"- Combined file: `{combined_name}`")
        index_lines.append("")

    (OUTPUT_DIR / "INDEX.md").write_text("\n".join(index_lines).strip() + "\n", encoding="utf-8")
    print(f"Generated NotebookLM Markdown in {OUTPUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
