"""Validate generated interactive notebooks.

Run from the repo root:
    python tests/validate_interactive_notebooks.py
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "mathematics" / "notebooks"
SOLUTIONS = ROOT / "mathematics" / "solutions"

REQUIRED_PHRASES = [
    "Google Colab Setup",
    "NOTEBOOK =",
    "Before You Learn",
    "Micro-Lesson",
    "Worked Example",
    "Faded Example",
    "Independent Practice",
    "End-of-Notebook Review",
    "mastery_dashboard",
]


def source_text(nb) -> str:
    return "\n".join("".join(cell.get("source", [])) for cell in nb["cells"])


def validate_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    nb = json.loads(path.read_text(encoding="utf-8"))
    if nb.get("nbformat") != 4:
        errors.append(f"{path}: nbformat is not 4")
    text = source_text(nb)
    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            errors.append(f"{path}: missing {phrase!r}")
    return errors


def validate_migrated_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    nb = json.loads(path.read_text(encoding="utf-8"))
    text = source_text(nb)
    tags = [
        cell.get("metadata", {}).get("tags", [])
        for cell in nb.get("cells", [])
    ]
    tag_count = sum(1 for item in tags if "interactive-v1" in item)
    if tag_count < 8:
        errors.append(f"{path}: expected at least 8 interactive-v1 cells, found {tag_count}")
    for phrase in ["Google Colab Setup", "NOTEBOOK =", "Before You Learn", "Retrieval Gate", "End-of-Notebook Review", "mastery_dashboard"]:
        if phrase not in text:
            errors.append(f"{path}: missing migrated phrase {phrase!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    generated = sorted(NOTEBOOKS.glob("math_00*.ipynb"))
    if len(generated) < 4:
        errors.append("expected four math_00 generated notebooks")
    for path in generated:
        errors.extend(validate_notebook(path))

    legacy = sorted(path for path in NOTEBOOKS.glob("*.ipynb") if not path.name.startswith("math_00"))
    if len(legacy) < 40:
        errors.append("expected at least 40 migrated legacy notebooks")
    for path in legacy:
        errors.extend(validate_migrated_notebook(path))

    for path in sorted(SOLUTIONS.glob("math_00*.ipynb")):
        nb = json.loads(path.read_text(encoding="utf-8"))
        text = source_text(nb)
        if "TODO: Reference instructor solution implementation here" in text:
            errors.append(f"{path}: contains placeholder solution TODO")
        if "# Replace None" in text and "Instructor Solution" in text:
            errors.append(f"{path}: appears to contain student scaffold text")

    for path in sorted(SOLUTIONS.glob("*.ipynb")):
        nb = json.loads(path.read_text(encoding="utf-8"))
        text = source_text(nb)
        if "TODO: Reference instructor solution implementation here" in text:
            errors.append(f"{path}: still contains placeholder solution TODO")

    registry = json.loads((ROOT / "curriculum" / "skills.json").read_text(encoding="utf-8"))
    if registry.get("schema_version") != 1:
        errors.append("curriculum/skills.json has wrong schema_version")
    if not registry.get("skills"):
        errors.append("curriculum/skills.json has no skills")

    if errors:
        print("\n".join(errors))
        return 1
    print("interactive notebook validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
