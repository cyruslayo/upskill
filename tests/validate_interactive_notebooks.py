"""Validate the clean generated notebook set.

Run from the repo root:
    python tests/validate_interactive_notebooks.py
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "mathematics" / "notebooks"
SOLUTIONS = ROOT / "mathematics" / "solutions"
INDEX = ROOT / "curriculum" / "notebook_index.json"
SKILLS = ROOT / "curriculum" / "skills.json"

REQUIRED_PHRASES = [
    "Google Colab Setup",
    "NOTEBOOK =",
    "Before You Learn",
    "Micro-Lesson",
    "Worked Example",
    "Faded Example",
    "Independent Practice",
    "Transfer Challenge",
    "End-of-Notebook Review",
    "mastery_dashboard",
]

FORBIDDEN_SOLUTION_PATTERNS = [
    "YOUR CODE HERE",
    "TODO",
    "pass",
    "return None",
    "student scaffold",
]


def cell_source(cell: dict) -> str:
    source = cell.get("source", [])
    return "".join(source) if isinstance(source, list) else str(source)


def source_text(nb: dict) -> str:
    return "\n".join(cell_source(cell) for cell in nb.get("cells", []))


def python_source_for_compile(text: str) -> str:
    """Approximate IPython execution while preserving real Python indentation.

    Generated setup cells contain Colab/IPython shell escapes such as ``!pip``.
    Those lines are valid in notebooks but not in ``compile``. Everything else
    should be ordinary Python and must parse exactly as stored.
    """
    kept = []
    for line in text.splitlines():
        if line.lstrip().startswith(("!", "%")):
            kept.append("")
        else:
            kept.append(line)
    return "\n".join(kept)


def tags(cell: dict) -> set[str]:
    return set(cell.get("metadata", {}).get("tags", []))


def load_nb(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def metadata_payload(nb: dict) -> dict:
    for cell in nb.get("cells", []):
        text = cell_source(cell)
        if text.strip().startswith("NOTEBOOK ="):
            match = re.search(r"NOTEBOOK\s*=\s*(\{.*?\})\s*SKILLS\s*=", text, flags=re.S)
            if match:
                return json.loads(match.group(1))
    raise AssertionError("missing NOTEBOOK metadata cell")


def validate_common(path: Path, nb: dict) -> list[str]:
    errors: list[str] = []
    if nb.get("nbformat") != 4:
        errors.append(f"{path}: nbformat is not 4")
    for index, cell in enumerate(nb.get("cells", []), 1):
        if cell.get("cell_type") == "code":
            if cell.get("execution_count") is not None:
                errors.append(f"{path}: code cell {index} has execution_count")
            if cell.get("outputs"):
                errors.append(f"{path}: code cell {index} has outputs")
            try:
                compile(python_source_for_compile(cell_source(cell)), f"{path}:cell-{index}", "exec")
            except SyntaxError as exc:
                errors.append(f"{path}: code cell {index} does not parse: {exc.msg}")
    text = source_text(nb)
    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            errors.append(f"{path}: missing {phrase!r}")
    try:
        metadata_payload(nb)
    except AssertionError as exc:
        errors.append(f"{path}: {exc}")
    return errors


def validate_student(path: Path, nb: dict) -> list[str]:
    errors = validate_common(path, nb)
    all_tags = [tag for cell in nb.get("cells", []) for tag in tags(cell)]
    if "solution" in all_tags:
        errors.append(f"{path}: student notebook contains solution-tagged cell")
    if "student-answer" not in all_tags:
        errors.append(f"{path}: student notebook has no student-answer scaffold")
    text = source_text(nb)
    if "Instructor Solution" in text:
        errors.append(f"{path}: student notebook exposes instructor label")
    return errors


def validate_solution(path: Path, nb: dict) -> list[str]:
    errors = validate_common(path, nb)
    all_tags = [tag for cell in nb.get("cells", []) for tag in tags(cell)]
    if "solution" not in all_tags:
        errors.append(f"{path}: solution notebook has no solution-tagged cells")
    text = source_text(nb)
    for pattern in FORBIDDEN_SOLUTION_PATTERNS:
        if pattern in text:
            errors.append(f"{path}: solution contains forbidden placeholder {pattern!r}")
    if 'answer = ""' in text or "answer = ''" in text:
        errors.append(f"{path}: solution retrieval answer is blank")
    return errors


def main() -> int:
    errors: list[str] = []
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    skills = json.loads(SKILLS.read_text(encoding="utf-8"))
    expected = [item["filename"] for item in index.get("notebooks", [])]
    if not expected:
        errors.append("curriculum/notebook_index.json has no notebooks")

    skill_ids = {item["id"] for item in skills.get("skills", [])}
    if not skill_ids:
        errors.append("curriculum/skills.json has no skills")

    notebook_files = {path.name for path in NOTEBOOKS.glob("*.ipynb")}
    solution_files = {path.name for path in SOLUTIONS.glob("*.ipynb")}
    if notebook_files != set(expected):
        errors.append("student notebook files do not match curriculum/notebook_index.json")
    if solution_files != set(expected):
        errors.append("solution notebook files do not match curriculum/notebook_index.json")

    for item in index.get("notebooks", []):
        for skill_id in item.get("skills_taught", []) + item.get("skills_practiced", []):
            if skill_id not in skill_ids:
                errors.append(f"{item['filename']}: skill {skill_id!r} is missing from skills.json")
        student = NOTEBOOKS / item["filename"]
        solution = SOLUTIONS / item["filename"]
        if student.exists():
            errors.extend(validate_student(student, load_nb(student)))
        if solution.exists():
            errors.extend(validate_solution(solution, load_nb(solution)))

    if errors:
        print("\n".join(errors))
        return 1
    print("clean notebook validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
