"""Legacy batch migration helper for the interactive learning shell.

Use ``generate_clean_notebooks.py`` for all current notebook authoring. This
module remains as a reference for how the older notebooks were wrapped.

This script does not try to solve every legacy exercise. Instead, it wraps the
existing lesson content with the shared retrieval-first runtime:

* Colab setup and progress store
* NOTEBOOK metadata
* prerequisite retrieval/review queue
* end-of-notebook reflection and mastery dashboard

The migration is idempotent. It removes cells tagged ``interactive-v1`` before
inserting a fresh wrapper.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

from interactive_generator import COLAB_SETUP


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "mathematics" / "notebooks"
SOLUTION_DIR = ROOT / "mathematics" / "solutions"
INDEX_PATH = ROOT / "curriculum" / "notebook_index.json"
TAG = "interactive-v1"


def source(cell: dict) -> str:
    raw = cell.get("source", [])
    if isinstance(raw, list):
        return "\n".join(raw)
    return str(raw)


def make_cell(cell_type: str, text: str) -> dict:
    cell = {
        "cell_type": cell_type,
        "id": f"iv1{abs(hash((cell_type, text))) % 10_000_000:07d}",
        "metadata": {"tags": [TAG]},
        "source": text.rstrip("\n").split("\n"),
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def first_markdown_title(nb: dict, filename: str) -> str:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "markdown":
            text = source(cell).strip()
            if "INSTRUCTOR SOLUTION KEY" in text:
                continue
            match = re.search(r"#\s+(.+?)(?:\*\*Learning Objectives|\n|$)", text)
            if match:
                return re.sub(r"\s+", " ", match.group(1)).strip()
    return filename.replace(".ipynb", "").replace("_", " ").title()


def learning_objectives(nb: dict) -> list[str]:
    text = "\n".join(source(cell) for cell in nb.get("cells", []) if cell.get("cell_type") == "markdown")
    objectives: list[str] = []
    match = re.search(r"\*\*Learning Objectives(?:\*\*|[^:]*:)\s*(.*?)(?=\*\*Prerequisites:|\*\*Estimated time:|---|##|$)", text, re.S)
    if match:
        block = re.sub(r"\s+", " ", match.group(1)).strip()
        block = block.replace("— By the end of this notebook you will be able to:", "").strip()
        parts = re.split(r"(?=\d+\.\s*)", block)
        for item in parts:
            cleaned = re.sub(r"^\d+\.\s*", "", item).strip()
            if cleaned and not cleaned.startswith("**"):
                objectives.append(cleaned)
    return objectives[:6]


def prerequisites(nb: dict) -> list[str]:
    text = "\n".join(source(cell) for cell in nb.get("cells", []) if cell.get("cell_type") == "markdown")
    match = re.search(r"\*\*Prerequisites:\*\*\s*(.*?)(?:\*\*Estimated time|\*\*Textbook|$)", text, re.S)
    if not match:
        return []
    raw = re.sub(r"\s+", " ", match.group(1)).strip(" -")
    raw = raw.replace("  ", " ")
    parts = [part.strip() for part in re.split(r",| and ", raw) if part.strip()]
    return parts[:6]


def infer_level(filename: str) -> int:
    if filename.startswith("math_0"):
        return 1
    if filename.startswith(("01_", "02_", "03_", "04_", "05_", "06_", "07_", "08_")):
        return 1
    if filename.startswith(("09_", "10_", "11_", "18_", "19_", "20_")):
        return 2
    if filename.startswith(("14_", "15_", "22_", "23-25_")):
        return 3
    if filename.startswith(("12_", "13_", "17_", "21_", "31_", "32-33_")):
        return 4
    if filename.startswith(("16_", "26_", "27-28_", "29_", "30_", "34_")):
        return 5
    if filename.startswith(("35-36_", "43_")):
        return 6
    if filename.startswith(("37-39_", "40-42_")):
        return 7
    return 1


def skill_id_for(filename: str) -> str:
    stem = filename.replace(".ipynb", "")
    stem = stem.replace("-", "_")
    if stem.startswith("math_"):
        return "lesson." + stem
    return "lesson.algorithms_" + stem


def next_notebook(filename: str, ordered: list[str]) -> str | None:
    try:
        index = ordered.index(filename)
    except ValueError:
        return None
    if index + 1 < len(ordered):
        return ordered[index + 1]
    return None


def clean_legacy_markdown(nb: dict) -> None:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        text = source(cell)
        text = text.replace("<summary>💡 Answers</summary>", "<summary>💡 Explanation after a retrieval attempt</summary>")
        text = text.replace("<summary>💡 Answer</summary>", "<summary>💡 Explanation after a retrieval attempt</summary>")
        text = text.replace("<summary>💡 Sketch</summary>", "<summary>💡 Sketch after a retrieval attempt</summary>")
        cell["source"] = text.split("\n")


def remove_old_interactive_cells(nb: dict) -> None:
    kept = []
    for cell in nb.get("cells", []):
        tags = cell.get("metadata", {}).get("tags", [])
        if TAG not in tags:
            kept.append(cell)
    nb["cells"] = kept


def insertion_index(nb: dict) -> int:
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") == "markdown" and source(cell).lstrip().startswith("# "):
            return i + 1
    return 0


def setup_cell() -> dict:
    return make_cell("code", COLAB_SETUP)


def metadata_cell(meta: dict) -> dict:
    skill_rows = []
    for skill_id in meta["skills_taught"] + meta["skills_practiced"]:
        skill_rows.append({
            "id": skill_id,
            "title": skill_id.replace(".", " ").replace("_", " ").title(),
            "notebook": meta["filename"],
            "level": meta["level"],
        })
    return make_cell(
        "code",
        "NOTEBOOK = " + json.dumps({
            "id": meta["id"],
            "level": meta["level"],
            "title": meta["title"],
            "prerequisites": meta["prerequisites"],
            "skills_taught": meta["skills_taught"],
            "skills_practiced": meta["skills_practiced"],
            "next_notebook": meta["next_notebook"],
        }, indent=4)
        + "\n\nSKILLS = "
        + json.dumps(skill_rows, indent=4),
    )


def retrieval_gate_cells(meta: dict) -> list[dict]:
    prereq_text = ", ".join(meta["prerequisites"]) if meta["prerequisites"] else "the previous foundations"
    skill_id = meta["skills_taught"][0]
    prompt = f"Before reading, name one key idea or procedure you remember from: {prereq_text}."
    return [
        make_cell(
            "markdown",
            "## Before You Learn: Retrieval Gate\n"
            "Close notes for a moment. Try to pull prerequisite ideas from memory before continuing. "
            "Getting stuck is useful data for the spaced-review system.",
        ),
        make_cell(
            "code",
            "due = store.review_queue(skills=SKILLS, limit=5)\n"
            "if due:\n"
            "    print('Due review items:')\n"
            "    for item in due:\n"
            "        print(f\"- {item['title']} (mastery {item['mastery']})\")\n"
            "else:\n"
            "    print('No due reviews yet. Use the recall prompt below to warm up.')",
        ),
        make_cell("markdown", f"**Recall prompt.** {prompt}"),
        make_cell(
            "code",
            "recall_answer = ''  # write a one-sentence memory before continuing\n"
            f"retrieved = len(recall_answer.strip()) >= 12\n"
            f"record = store.record_attempt({skill_id!r}, retrieved, confidence=3, item_type='prerequisite_recall')\n"
            "print('Recorded retrieval attempt.' if retrieved else 'Write a real memory first, then rerun this cell.')\n"
            "record",
        ),
        make_cell(
            "markdown",
            "## Learning Loop\n"
            "Use the existing lesson cells below as the micro-lesson and practice surface. For each exercise: "
            "predict first, attempt from memory, run checks, then open explanations only after the attempt.",
        ),
    ]


def footer_cells(meta: dict) -> list[dict]:
    skill_id = meta["skills_taught"][0]
    return [
        make_cell(
            "markdown",
            "## End-of-Notebook Review\n"
            "Retrieve the core idea one more time before leaving. This final recall makes the next review easier.",
        ),
        make_cell(
            "code",
            "final_recall = ''  # summarize the most important idea in your own words\n"
            "confidence = 3  # set 1-5 after answering\n"
            f"ok = len(final_recall.strip()) >= 20\n"
            f"store.record_attempt({skill_id!r}, ok, confidence=confidence, item_type='end_review')\n"
            f"mastery_dashboard(store=store, skills=SKILLS, next_notebook={meta['next_notebook']!r})",
        ),
    ]


def migrate_file(path: Path, ordered: list[str]) -> dict:
    nb = json.loads(path.read_text(encoding="utf-8"))
    clean_legacy_markdown(nb)
    remove_old_interactive_cells(nb)
    filename = path.name
    primary_skill = skill_id_for(filename)
    meta = {
        "id": filename.replace(".ipynb", ""),
        "filename": filename,
        "title": first_markdown_title(nb, filename),
        "level": infer_level(filename),
        "objectives": learning_objectives(nb),
        "prerequisites": prerequisites(nb),
        "skills_taught": [primary_skill],
        "skills_practiced": ["py.arithmetic.expressions"] if not filename.startswith("math_00") else [],
        "next_notebook": next_notebook(filename, ordered),
    }
    insert_at = insertion_index(nb)
    injected = [setup_cell(), metadata_cell(meta), *retrieval_gate_cells(meta)]
    nb["cells"][insert_at:insert_at] = injected
    nb["cells"].extend(footer_cells(meta))
    nb.setdefault("metadata", {}).setdefault("colab", {"name": filename, "provenance": []})
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    return meta


def legacy_order() -> list[str]:
    files = [p.name for p in NOTEBOOK_DIR.glob("*.ipynb") if not p.name.startswith("math_00")]
    math = sorted([name for name in files if name.startswith("math_")])
    algorithms = sorted([name for name in files if not name.startswith("math_")])
    return math + algorithms


def write_index(metas: list[dict]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps({
        "schema_version": 1,
        "description": "Legacy notebooks migrated into the interactive-v1 shell.",
        "notebooks": metas,
    }, indent=2), encoding="utf-8")


def main() -> int:
    ordered = legacy_order()
    metas: list[dict] = []
    for folder in [NOTEBOOK_DIR, SOLUTION_DIR]:
        for filename in ordered:
            path = folder / filename
            if path.exists():
                meta = migrate_file(path, ordered)
                if folder == NOTEBOOK_DIR:
                    metas.append(meta)
                print(f"migrated {path.relative_to(ROOT)}")
    write_index(metas)
    print(f"wrote {INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
