"""Generate every clean student and instructor notebook from LessonSpec data."""
from __future__ import annotations

import base64
import json
from pathlib import Path
import sys
import textwrap
import uuid

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from mathematics.notebooks.clean_specs import LEVELS, ExerciseSpec, LessonSpec, build_specs
else:
    from .clean_specs import LEVELS, ExerciseSpec, LessonSpec, build_specs


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "mathematics" / "notebooks"
SOLUTION_DIR = ROOT / "mathematics" / "solutions"
CURRICULUM_DIR = ROOT / "curriculum"
LEARNING_TOOLS_PAYLOAD = base64.b64encode((ROOT / "learning_tools.py").read_bytes()).decode("ascii")


def _lines(source: str) -> list[str]:
    cleaned = textwrap.dedent(source).strip("\n")
    return cleaned.splitlines(keepends=True)


def make_cell(cell_type: str, source: str, tags: list[str] | None = None) -> dict:
    cell = {
        "cell_type": cell_type,
        "id": uuid.uuid4().hex[:8],
        "metadata": {"tags": tags or []},
        "source": _lines(source),
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def md(source: str, tags: list[str] | None = None) -> dict:
    return make_cell("markdown", source, tags)


def code(source: str, tags: list[str] | None = None) -> dict:
    return make_cell("code", source, tags)


COLAB_SETUP = f"""
# Google Colab Setup
!pip install -q ipywidgets jupyterquiz ipytest plotly sympy networkx pandas numpy matplotlib tqdm

import base64, os, sys
from pathlib import Path

if Path('/content').exists():
    repo_root = Path('/content/upskill')
else:
    repo_root = Path.cwd()

if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

try:
    from learning_tools import (
        ProgressStore, Skill, setup_colab, check, code_check,
        short_answer_check, hint_box, mastery_dashboard
    )
except ModuleNotFoundError:
    Path('learning_tools.py').write_bytes(base64.b64decode({LEARNING_TOOLS_PAYLOAD!r}))
    from learning_tools import (
        ProgressStore, Skill, setup_colab, check, code_check,
        short_answer_check, hint_box, mastery_dashboard
    )

progress_path = setup_colab()
store = ProgressStore(progress_path)
print('Ready for retrieval practice.')
"""


def skill_records(spec: LessonSpec) -> list[dict]:
    titles = ["Retrieval for " + spec.title, "Implementation for " + spec.title, "Transfer for " + spec.title]
    return [
        {
            "id": skill_id,
            "title": titles[min(index, len(titles) - 1)],
            "notebook": spec.filename,
            "level": spec.level,
            "prerequisites": spec.prerequisites,
            "tags": [spec.track.lower().replace(" ", "-"), spec.id],
        }
        for index, skill_id in enumerate(spec.skills)
    ]


def metadata_cell(spec: LessonSpec) -> dict:
    payload = {
        "id": spec.id,
        "filename": spec.filename,
        "title": spec.title,
        "level": spec.level,
        "track": spec.track,
        "objectives": spec.objectives,
        "prerequisites": spec.prerequisites,
        "skills_taught": spec.skills,
        "skills_practiced": spec.prerequisites,
        "next_notebook": spec.next_notebook,
    }
    source = f"NOTEBOOK = {json.dumps(payload, indent=4)}\n\nSKILLS = {json.dumps(skill_records(spec), indent=4)}"
    return code(source, ["metadata"])


def retrieval_cells(spec: LessonSpec, solution: bool) -> list[dict]:
    cells = [md("## Before You Learn: Pull From Memory\nAnswer before reading. Retrieval is useful even when it feels effortful.", ["retrieval"])]
    for index, item in enumerate(spec.retrieval, 1):
        answer = item.solution_answer if solution else ""
        cells.append(md(f"**Recall {index}.** {item.prompt}", ["retrieval"]))
        cells.append(
            code(
                f"""
                answer = {answer!r}
                short_answer_check(
                    {('retrieval_' + str(index))!r},
                    answer,
                    {item.accepted_answers!r},
                    skill_id={item.skill_id!r},
                    confidence=3,
                    store=store,
                )
                """,
                ["retrieval", "solution" if solution else "student-answer"],
            )
        )
    return cells


def exercise_cells(exercise: ExerciseSpec, solution: bool) -> list[dict]:
    body = exercise.solution if solution else exercise.scaffold
    cells = [
        md(f"### {exercise.title}\n\n{exercise.prompt}", ["practice"]),
        code(body, ["solution" if solution else "student-answer"]),
        code(exercise.tests, ["check"]),
        code(
            f"""
            hint_box(
                {('Hints: ' + exercise.title)!r},
                {exercise.hints!r},
                unlock=False,
            )
            """,
            ["hint"],
        ),
    ]
    if exercise.visualization:
        cells.append(code(exercise.visualization, ["visualization"]))
    return cells


def lesson_cells(spec: LessonSpec, solution: bool) -> list[dict]:
    title = f"Instructor Solution: {spec.title}" if solution else spec.title
    cells: list[dict] = [
        md(
            f"""
            # {title}

            **Level:** {spec.level}

            **Learning Objectives**
            {chr(10).join(f"{index}. {objective}" for index, objective in enumerate(spec.objectives, 1))}
            """,
            ["title"],
        ),
        code(COLAB_SETUP, ["setup"]),
        metadata_cell(spec),
    ]
    cells.extend(retrieval_cells(spec, solution))
    for section in spec.lesson_sections:
        cells.append(md(f"## {section.heading}\n{section.body}", [section.heading.lower().replace(" ", "-")]))
    cells.append(md("## Independent Practice\nUse the scaffold, run the checks, then revise until the behavior is correct.", ["practice"]))
    for exercise in spec.exercises:
        cells.extend(exercise_cells(exercise, solution))
    cells.append(md(f"## Transfer Challenge\n{spec.transfer_challenge}", ["transfer"]))
    cells.append(md("## End-of-Notebook Review\nRetrieve the key ideas once more and inspect the review dashboard.", ["review"]))
    cells.append(code("mastery_dashboard(store=store, skills=SKILLS, next_notebook=NOTEBOOK.get('next_notebook'))", ["dashboard"]))
    return cells


def save_notebook(cells: list[dict], path: Path) -> None:
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"},
            "colab": {"name": path.name, "provenance": []},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=True), encoding="utf-8")


def write_curriculum(specs: list[LessonSpec]) -> None:
    notebook_index = {
        "schema_version": 2,
        "description": "Clean notebooks generated from mathematics/notebooks/clean_specs.py.",
        "notebooks": [
            {
                "id": spec.id,
                "filename": spec.filename,
                "title": spec.title,
                "level": spec.level,
                "track": spec.track,
                "objectives": spec.objectives,
                "prerequisites": spec.prerequisites,
                "skills_taught": spec.skills,
                "skills_practiced": spec.prerequisites,
                "next_notebook": spec.next_notebook,
            }
            for spec in specs
        ],
    }
    all_skills = [record for spec in specs for record in skill_records(spec)]
    skills = {
        "schema_version": 1,
        "levels": LEVELS,
        "skills": all_skills,
    }
    CURRICULUM_DIR.mkdir(parents=True, exist_ok=True)
    (CURRICULUM_DIR / "notebook_index.json").write_text(json.dumps(notebook_index, indent=2), encoding="utf-8")
    (CURRICULUM_DIR / "skills.json").write_text(json.dumps(skills, indent=2), encoding="utf-8")


def generate() -> None:
    specs = build_specs()
    for spec in specs:
        save_notebook(lesson_cells(spec, solution=False), NOTEBOOK_DIR / spec.filename)
        save_notebook(lesson_cells(spec, solution=True), SOLUTION_DIR / spec.filename)
    write_curriculum(specs)
    print(f"generated {len(specs)} student notebooks and {len(specs)} solution notebooks")


if __name__ == "__main__":
    generate()
