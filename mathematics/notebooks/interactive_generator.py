"""Legacy Level 0 generator for retrieval-first Colab notebooks.

Use ``generate_clean_notebooks.py`` for all current notebook authoring. This
module is kept only as a historical reference for the first interactive pass.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import textwrap
import uuid


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "mathematics" / "notebooks"
SOLUTION_DIR = ROOT / "mathematics" / "solutions"
CURRICULUM_DIR = ROOT / "curriculum"


def _split(source: str) -> list[str]:
    return source.rstrip("\n").split("\n")


def cell(cell_type: str, source: str, metadata: dict | None = None) -> dict:
    item = {
        "cell_type": cell_type,
        "id": uuid.uuid4().hex[:8],
        "metadata": metadata or {},
        "source": _split(source),
    }
    if cell_type == "code":
        item["execution_count"] = None
        item["outputs"] = []
    return item


def md(source: str) -> dict:
    return cell("markdown", textwrap.dedent(source).strip())


def code(source: str, metadata: dict | None = None) -> dict:
    return cell("code", textwrap.dedent(source).strip(), metadata=metadata)


def save_notebook(cells: list[dict], path: Path) -> None:
    nb = {
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
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


@dataclass
class RetrievalItem:
    id: str
    skill_id: str
    prompt: str
    accepted: list[str]


@dataclass
class Exercise:
    id: str
    skill_id: str
    title: str
    prompt: str
    scaffold: str
    solution: str
    tests: str
    hints: list[str]


@dataclass
class Lesson:
    notebook_id: str
    filename: str
    title: str
    level: int
    objectives: list[str]
    prerequisites: list[str]
    skills_taught: list[str]
    skills_practiced: list[str]
    micro_lesson: str
    worked_example: str
    faded_example: str
    retrieval: list[RetrievalItem] = field(default_factory=list)
    exercises: list[Exercise] = field(default_factory=list)
    transfer: str = ""
    visualization_code: str = ""
    next_notebook: str = ""


LEARNING_TOOLS_SOURCE = (ROOT / "learning_tools.py").read_text(encoding="utf-8")


COLAB_SETUP = f"""
# Google Colab Setup
!pip install -q ipywidgets jupyterquiz ipytest plotly sympy networkx pandas numpy matplotlib tqdm

import json, os, sys
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
    Path('learning_tools.py').write_text({LEARNING_TOOLS_SOURCE!r}, encoding='utf-8')
    from learning_tools import (
        ProgressStore, Skill, setup_colab, check, code_check,
        short_answer_check, hint_box, mastery_dashboard
    )

progress_path = setup_colab()
store = ProgressStore(progress_path)
print('Ready for retrieval practice.')
"""


def metadata_cell(lesson: Lesson) -> dict:
    return code(
        f"""
        NOTEBOOK = {json.dumps({
            "id": lesson.notebook_id,
            "level": lesson.level,
            "title": lesson.title,
            "prerequisites": lesson.prerequisites,
            "skills_taught": lesson.skills_taught,
            "skills_practiced": lesson.skills_practiced,
            "next_notebook": lesson.next_notebook,
        }, indent=4)}

        SKILLS = [
        {",".join(json.dumps({"id": skill, "title": skill, "notebook": lesson.filename, "level": lesson.level}) for skill in lesson.skills_taught + lesson.skills_practiced)}
        ]
        """
    )


def retrieval_cells(items: list[RetrievalItem]) -> list[dict]:
    cells: list[dict] = [md("## Before You Learn: Pull From Memory\nAnswer these before reading the lesson. The point is retrieval, not perfection.")]
    for item in items:
        cells.append(md(f"**Recall {item.id}.** {item.prompt}"))
        cells.append(code(
            f"""
            answer = ""  # type your answer inside the quotes
            short_answer_check(
                {item.id!r},
                answer,
                {item.accepted!r},
                skill_id={item.skill_id!r},
                confidence=3,
                store=store,
            )
            """
        ))
    return cells


def exercise_cells(exercise: Exercise, solution: bool) -> list[dict]:
    cells = [
        md(f"### {exercise.title}\n\n{exercise.prompt}"),
        code(exercise.solution if solution else exercise.scaffold, metadata={"tags": ["solution" if solution else "student-answer"]}),
        code(exercise.tests),
        code(
            f"""
            hint_box(
                {('Hints for ' + exercise.title)!r},
                {exercise.hints!r},
                unlock=False,
            )
            """
        ),
    ]
    if solution:
        cells.append(md("**Instructor note:** The full solution is included above. The student version receives scaffolded code, active checks, and staged hints."))
    return cells


def lesson_cells(lesson: Lesson, solution: bool = False) -> list[dict]:
    cells: list[dict] = []
    title_prefix = "Instructor Solution: " if solution else ""
    cells.append(md(
        f"""
        # {title_prefix}{lesson.title}

        **Level:** {lesson.level}

        **Learning Objectives**
        {chr(10).join(f"{i + 1}. {objective}" for i, objective in enumerate(lesson.objectives))}
        """
    ))
    cells.append(code(COLAB_SETUP))
    cells.append(metadata_cell(lesson))
    cells.extend(retrieval_cells(lesson.retrieval))
    cells.append(md(f"## Micro-Lesson\n{lesson.micro_lesson}"))
    cells.append(md(f"## Worked Example\n{lesson.worked_example}"))
    cells.append(md(f"## Faded Example\n{lesson.faded_example}"))
    if lesson.visualization_code:
        cells.append(md("## Interactive Visualization"))
        cells.append(code(lesson.visualization_code))
    cells.append(md("## Independent Practice"))
    for exercise in lesson.exercises:
        cells.extend(exercise_cells(exercise, solution=solution))
    if lesson.transfer:
        cells.append(md(f"## Transfer Challenge\n{lesson.transfer}"))
    cells.append(md("## End-of-Notebook Review\nBefore leaving, retrieve the most important ideas once more."))
    cells.append(code(
        f"""
        mastery_dashboard(store=store, skills=SKILLS, next_notebook={lesson.next_notebook!r})
        """
    ))
    return cells


def lessons() -> list[Lesson]:
    return [
        Lesson(
            notebook_id="math_00_python_arithmetic",
            filename="math_00_python_arithmetic.ipynb",
            title="Math 00A: Python Arithmetic and Variables",
            level=0,
            objectives=[
                "Evaluate arithmetic expressions using Python.",
                "Store intermediate results in variables.",
                "Write tiny functions that return computed values.",
                "Use checks to verify answers instead of guessing.",
            ],
            prerequisites=[],
            skills_taught=["py.arithmetic.expressions", "py.variables.functions"],
            skills_practiced=[],
            retrieval=[
                RetrievalItem("mental_addition", "py.arithmetic.expressions", "What is 7 + 8?", ["15"]),
                RetrievalItem("multiplication_fact", "py.arithmetic.expressions", "What is 6 * 9?", ["54"]),
            ],
            micro_lesson="""
            Python can act like a precise mathematical notebook. Arithmetic expressions such as `2 + 3 * 4`
            follow order of operations: multiplication happens before addition. Variables let you name a result
            so working memory does not have to hold every number at once.
            """,
            worked_example="""
            Suppose a notebook costs 750 and a pen costs 125. Three notebooks and two pens cost:

            ```python
            total = 3 * 750 + 2 * 125
            ```

            The variable `total` stores the result so we can use it later.
            """,
            faded_example="""
            A bus ticket costs 350. Four tickets cost `4 * ___`. Fill the blank before running code.
            """,
            visualization_code="""
            import ipywidgets as widgets
            from IPython.display import display

            price = widgets.IntSlider(value=350, min=50, max=1000, step=50, description='price')
            quantity = widgets.IntSlider(value=4, min=1, max=12, step=1, description='quantity')
            output = widgets.Output()

            def show_total(change=None):
                with output:
                    output.clear_output()
                    print(f'total = {quantity.value} * {price.value} = {quantity.value * price.value}')

            price.observe(show_total, names='value')
            quantity.observe(show_total, names='value')
            display(price, quantity, output)
            show_total()
            """,
            exercises=[
                Exercise(
                    id="ticket_total",
                    skill_id="py.arithmetic.expressions",
                    title="Compute a Total",
                    prompt="Write `ticket_total(price, quantity)` so it returns the total cost.",
                    scaffold="""
                    def ticket_total(price, quantity):
                        # Replace None with the expression that computes total cost.
                        return None
                    """,
                    solution="""
                    def ticket_total(price, quantity):
                        return price * quantity
                    """,
                    tests="""
                    code_check(
                        'ticket_total',
                        ticket_total,
                        [((350, 4), 1400), ((125, 2), 250), ((0, 8), 0)],
                        skill_id='py.arithmetic.expressions',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "Total cost combines the same price repeated quantity times.",
                        "Use multiplication, not addition with one fixed number.",
                        "The return line should look like `return price * quantity`.",
                    ],
                ),
                Exercise(
                    id="average_two",
                    skill_id="py.variables.functions",
                    title="Average Two Numbers",
                    prompt="Write `average_two(a, b)` using a variable named `total` before returning the average.",
                    scaffold="""
                    def average_two(a, b):
                        total = None
                        return None
                    """,
                    solution="""
                    def average_two(a, b):
                        total = a + b
                        return total / 2
                    """,
                    tests="""
                    code_check(
                        'average_two',
                        average_two,
                        [((10, 20), 15), ((3, 5), 4), ((-2, 2), 0)],
                        skill_id='py.variables.functions',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "First add the two numbers.",
                        "A mean is total divided by the number of values.",
                        "`total = a + b`, then `return total / 2`.",
                    ],
                ),
            ],
            transfer="Write a function for the total price after a percentage discount. Try it first without hints.",
            next_notebook="math_00_pre_algebra.ipynb",
        ),
        Lesson(
            notebook_id="math_00_pre_algebra",
            filename="math_00_pre_algebra.ipynb",
            title="Math 00B: Pre-Algebra Foundations",
            level=0,
            objectives=[
                "Apply order of operations.",
                "Compute with negative numbers.",
                "Use fractions as division.",
                "Solve proportional reasoning problems.",
            ],
            prerequisites=["py.arithmetic.expressions"],
            skills_taught=["math.pre_algebra.order_operations", "math.pre_algebra.fractions"],
            skills_practiced=["py.arithmetic.expressions"],
            retrieval=[
                RetrievalItem("order_memory", "math.pre_algebra.order_operations", "In 2 + 3 * 4, which operation happens first?", ["multiplication", "*", "multiply"]),
                RetrievalItem("fraction_memory", "math.pre_algebra.fractions", "What does 3/4 mean as division?", ["3 divided by 4", "3/4", "3 over 4"]),
            ],
            micro_lesson="""
            Algebra becomes easier when arithmetic chunks are automatic. Order of operations protects meaning:
            parentheses first, then multiplication/division, then addition/subtraction. Fractions are division
            written compactly, so `3/4` means three divided by four.
            """,
            worked_example="""
            Evaluate `2 + 3 * (10 - 6)`.

            1. Parentheses: `10 - 6 = 4`
            2. Multiplication: `3 * 4 = 12`
            3. Addition: `2 + 12 = 14`
            """,
            faded_example="""
            Evaluate `5 + 2 * (9 - 4)`: first compute `9 - 4 = ___`, then multiply by `2`, then add `5`.
            """,
            visualization_code="""
            from fractions import Fraction
            import ipywidgets as widgets
            from IPython.display import display

            numerator = widgets.IntSlider(value=3, min=1, max=12, description='top')
            denominator = widgets.IntSlider(value=4, min=1, max=12, description='bottom')
            out = widgets.Output()

            def show_fraction(change=None):
                with out:
                    out.clear_output()
                    f = Fraction(numerator.value, denominator.value)
                    print(f'{numerator.value}/{denominator.value} = {float(f):.3f} = {f}')

            numerator.observe(show_fraction, names='value')
            denominator.observe(show_fraction, names='value')
            display(numerator, denominator, out)
            show_fraction()
            """,
            exercises=[
                Exercise(
                    id="evaluate_expression",
                    skill_id="math.pre_algebra.order_operations",
                    title="Order of Operations",
                    prompt="Write `evaluate_expression()` to return the value of `5 + 2 * (9 - 4)`.",
                    scaffold="""
                    def evaluate_expression():
                        return None
                    """,
                    solution="""
                    def evaluate_expression():
                        return 5 + 2 * (9 - 4)
                    """,
                    tests="""
                    check(
                        'evaluate_expression',
                        evaluate_expression(),
                        15,
                        skill_id='math.pre_algebra.order_operations',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "Start inside the parentheses.",
                        "Multiplication happens before addition.",
                        "`9 - 4` is `5`, `2 * 5` is `10`, and `5 + 10` is `15`.",
                    ],
                ),
                Exercise(
                    id="fraction_of",
                    skill_id="math.pre_algebra.fractions",
                    title="Fraction of a Quantity",
                    prompt="Write `fraction_of(numerator, denominator, amount)`.",
                    scaffold="""
                    def fraction_of(numerator, denominator, amount):
                        # Example: fraction_of(3, 4, 20) should return 15.
                        return None
                    """,
                    solution="""
                    def fraction_of(numerator, denominator, amount):
                        return numerator / denominator * amount
                    """,
                    tests="""
                    code_check(
                        'fraction_of',
                        fraction_of,
                        [((3, 4, 20), 15), ((1, 2, 50), 25), ((2, 5, 100), 40)],
                        skill_id='math.pre_algebra.fractions',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "A fraction of an amount means multiply by the fraction.",
                        "The fraction is numerator divided by denominator.",
                        "`return numerator / denominator * amount`.",
                    ],
                ),
            ],
            transfer="A recipe uses 3/4 cup of flour for one batch. Write a function that computes flour for any number of batches.",
            next_notebook="math_00_functions_and_graphs.ipynb",
        ),
        Lesson(
            notebook_id="math_00_functions_and_graphs",
            filename="math_00_functions_and_graphs.ipynb",
            title="Math 00C: Functions, Tables, and Graphs",
            level=0,
            objectives=[
                "Understand a function as an input-output rule.",
                "Build tables of values.",
                "Connect formulas to plotted graphs.",
                "Recognize slope as repeated change.",
            ],
            prerequisites=["py.variables.functions", "math.pre_algebra.order_operations"],
            skills_taught=["math.functions.input_output", "math.functions.graph_tables"],
            skills_practiced=["py.variables.functions", "math.pre_algebra.order_operations"],
            retrieval=[
                RetrievalItem("function_memory", "math.functions.input_output", "If f(x)=2x+1, what is f(3)?", ["7"]),
                RetrievalItem("slope_memory", "math.functions.graph_tables", "In y=3x+2, what number tells you the repeated change in y?", ["3", "slope"]),
            ],
            micro_lesson="""
            A function is a rule that turns an input into an output. A table shows several inputs and outputs.
            A graph draws those pairs as points. When a function is linear, equal steps in `x` create equal
            changes in `y`.
            """,
            worked_example="""
            For `f(x) = 2x + 1`, the input `x = 3` gives `2 * 3 + 1 = 7`.
            The point `(3, 7)` belongs on the graph.
            """,
            faded_example="""
            For `g(x) = 4x - 2`, the input `x = 5` gives `4 * ___ - 2 = ___`.
            """,
            visualization_code="""
            import numpy as np
            import matplotlib.pyplot as plt
            import ipywidgets as widgets
            from IPython.display import display

            slope = widgets.IntSlider(value=2, min=-5, max=5, description='slope')
            intercept = widgets.IntSlider(value=1, min=-10, max=10, description='intercept')
            out = widgets.Output()

            def plot_line(change=None):
                with out:
                    out.clear_output()
                    xs = np.arange(-5, 6)
                    ys = slope.value * xs + intercept.value
                    plt.figure(figsize=(5, 3))
                    plt.axhline(0, color='black', linewidth=0.5)
                    plt.axvline(0, color='black', linewidth=0.5)
                    plt.plot(xs, ys, marker='o')
                    plt.title(f'y = {slope.value}x + {intercept.value}')
                    plt.grid(True)
                    plt.show()

            slope.observe(plot_line, names='value')
            intercept.observe(plot_line, names='value')
            display(slope, intercept, out)
            plot_line()
            """,
            exercises=[
                Exercise(
                    id="linear_function",
                    skill_id="math.functions.input_output",
                    title="Write a Linear Function",
                    prompt="Write `f(x)` for the rule `2x + 1`.",
                    scaffold="""
                    def f(x):
                        return None
                    """,
                    solution="""
                    def f(x):
                        return 2 * x + 1
                    """,
                    tests="""
                    code_check(
                        'f',
                        f,
                        [((0,), 1), ((3,), 7), ((-2,), -3)],
                        skill_id='math.functions.input_output',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "Use the input variable `x`.",
                        "Double the input, then add one.",
                        "`return 2 * x + 1`.",
                    ],
                ),
                Exercise(
                    id="build_table",
                    skill_id="math.functions.graph_tables",
                    title="Build a Table",
                    prompt="Write `build_table(fn, xs)` to return pairs `(x, fn(x))`.",
                    scaffold="""
                    def build_table(fn, xs):
                        table = []
                        # append (x, fn(x)) for every x
                        return table
                    """,
                    solution="""
                    def build_table(fn, xs):
                        table = []
                        for x in xs:
                            table.append((x, fn(x)))
                        return table
                    """,
                    tests="""
                    code_check(
                        'build_table',
                        build_table,
                        [((lambda x: 2*x + 1, [0, 1, 2]), [(0, 1), (1, 3), (2, 5)])],
                        skill_id='math.functions.graph_tables',
                        confidence=3,
                        store=store,
                    )
                    """,
                    hints=[
                        "A table is a list of input-output pairs.",
                        "Loop through `xs` and call the function on each input.",
                        "`table.append((x, fn(x)))` inside the loop.",
                    ],
                ),
            ],
            transfer="Create a table and graph for a taxi fare rule: base fee plus price per kilometer.",
            next_notebook="math_01_algebra_linear_equations.ipynb",
        ),
    ]


def diagnostic_lesson() -> Lesson:
    return Lesson(
        notebook_id="math_00_diagnostic",
        filename="math_00_diagnostic.ipynb",
        title="Math 00: Diagnostic and Placement",
        level=0,
        objectives=[
            "Retrieve prerequisite knowledge before studying.",
            "Identify the right starting point.",
            "Initialize the progress dashboard.",
        ],
        prerequisites=[],
        skills_taught=[],
        skills_practiced=[
            "py.arithmetic.expressions",
            "math.pre_algebra.order_operations",
            "math.functions.input_output",
            "math.linear_equations.solve_ax_b_c",
        ],
        retrieval=[
            RetrievalItem("arithmetic", "py.arithmetic.expressions", "What is 8 * 7?", ["56"]),
            RetrievalItem("order_ops", "math.pre_algebra.order_operations", "What is 2 + 3 * 4?", ["14"]),
            RetrievalItem("function_eval", "math.functions.input_output", "If f(x)=x+5, what is f(9)?", ["14"]),
            RetrievalItem("linear_equation", "math.linear_equations.solve_ax_b_c", "Solve x + 3 = 10.", ["7", "x=7", "x = 7"]),
        ],
        micro_lesson="This diagnostic is not a grade. It routes review. Try from memory before opening notes.",
        worked_example="If you miss an item, that is useful information: it means the review scheduler should bring it back soon.",
        faded_example="After answering, use the dashboard to choose the first notebook with weak or missing prerequisites.",
        exercises=[],
        transfer="If the diagnostic felt hard, begin with `math_00_python_arithmetic.ipynb`. If it felt easy, continue to `math_01_algebra_linear_equations.ipynb`.",
        next_notebook="math_00_python_arithmetic.ipynb",
    )


def generate() -> None:
    all_lessons = [diagnostic_lesson(), *lessons()]
    for lesson in all_lessons:
        save_notebook(lesson_cells(lesson, solution=False), NOTEBOOK_DIR / lesson.filename)
        save_notebook(lesson_cells(lesson, solution=True), SOLUTION_DIR / lesson.filename)


if __name__ == "__main__":
    generate()
