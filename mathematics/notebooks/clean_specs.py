"""Structured lesson specs for the clean notebook generator.

This module is the authoring surface for the rebuilt notebook set. The
generator consumes these dataclasses to emit both student and instructor
notebooks, plus the curriculum skill and notebook indexes.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RetrievalSpec:
    prompt: str
    accepted_answers: list[str]
    skill_id: str
    solution_answer: str


@dataclass(frozen=True)
class ExerciseSpec:
    prompt: str
    scaffold: str
    solution: str
    tests: str
    hints: list[str]
    skill_id: str
    title: str = "Practice"
    visualization: str = ""


@dataclass(frozen=True)
class LessonSection:
    heading: str
    body: str


@dataclass(frozen=True)
class LessonSpec:
    id: str
    filename: str
    title: str
    level: int
    track: str
    objectives: list[str]
    prerequisites: list[str]
    skills: list[str]
    lesson_sections: list[LessonSection]
    retrieval: list[RetrievalSpec]
    exercises: list[ExerciseSpec]
    transfer_challenge: str
    next_notebook: str | None = None


LEVELS = [
    {"level": 0, "title": "Foundations", "description": "Pre-algebra, Python arithmetic, functions, and placement."},
    {"level": 1, "title": "Algebra and Computational Thinking", "description": "Linear equations, coding primitives, number systems, and recurrence."},
    {"level": 2, "title": "Calculus and Optimization", "description": "Derivatives, roots, gradient descent, differential equations, and dynamical models."},
    {"level": 3, "title": "Linear Algebra and Data Geometry", "description": "Vectors, matrices, elimination, simplex, and pseudoinverse methods."},
    {"level": 4, "title": "Algorithms", "description": "Search, sorting, recursion, graphs, games, hash tables, and complexity."},
    {"level": 5, "title": "Classical Machine Learning", "description": "Clustering, regression, validation, KNN, Naive Bayes, and decision trees."},
    {"level": 6, "title": "Neural Networks", "description": "Forward propagation, training loops, convolution basics, and model behavior."},
    {"level": 7, "title": "Game AI and Capstones", "description": "Minimax, self-play, neuroevolution, and open-ended expert projects."},
]


FOUNDATION_LESSONS = [
    ("math_00_diagnostic.ipynb", "Math 00: Diagnostic and Placement", 0, "Foundations"),
    ("math_00_python_arithmetic.ipynb", "Math 00A: Python Arithmetic and Variables", 0, "Foundations"),
    ("math_00_pre_algebra.ipynb", "Math 00B: Pre-Algebra Foundations", 0, "Foundations"),
    ("math_00_functions_and_graphs.ipynb", "Math 00C: Functions, Tables, and Graphs", 0, "Foundations"),
]


MATH_LESSONS = [
    ("math_01_algebra_linear_equations.ipynb", "Math 01: Algebra - Linear Equations", 1, "Math Foundations"),
    ("math_02_calculus_derivatives.ipynb", "Math 02: Calculus - Derivatives and the Power Rule", 2, "Math Foundations"),
    ("math_03_calculus_chain_rule.ipynb", "Math 03: Calculus - The Chain Rule", 2, "Math Foundations"),
    ("math_04_calculus_local_extrema.ipynb", "Math 04: Calculus - Local Extrema", 2, "Math Foundations"),
    ("math_05_linear_algebra_vectors.ipynb", "Math 05: Linear Algebra - Vectors", 3, "Math Foundations"),
    ("math_06_linear_algebra_matrices.ipynb", "Math 06: Linear Algebra - Matrices", 3, "Math Foundations"),
    ("math_07_calculus_differential_equations.ipynb", "Math 07: Calculus - Differential Equations", 2, "Math Foundations"),
]


ALGORITHM_LESSONS = [
    ("01_introductory_coding.ipynb", "Algorithms 01: Introductory Coding", 1, "Algorithms"),
    ("02_number_systems.ipynb", "Algorithms 02: Number Systems", 1, "Algorithms"),
    ("03_recursive_sequences.ipynb", "Algorithms 03: Recursive Sequences", 1, "Algorithms"),
    ("04_simulating_randomness.ipynb", "Algorithms 04: Simulating Randomness", 1, "Algorithms"),
    ("05_roulette_wheel.ipynb", "Algorithms 05: Roulette Wheel Selection", 1, "Algorithms"),
    ("06_cartesian_product.ipynb", "Algorithms 06: Cartesian Product", 1, "Algorithms"),
    ("07_brute_force_crypto.ipynb", "Algorithms 07: Brute Force Cryptography", 4, "Algorithms"),
    ("08_backtracking_magic_squares.ipynb", "Algorithms 08: Backtracking and Magic Squares", 4, "Algorithms"),
    ("09_estimating_roots.ipynb", "Algorithms 09: Estimating Roots", 2, "Algorithms"),
    ("10_single_variable_gd.ipynb", "Algorithms 10: Single Variable Gradient Descent", 2, "Algorithms"),
    ("11_multivariable_gd.ipynb", "Algorithms 11: Multivariable Gradient Descent", 2, "Algorithms"),
    ("12_basic_sorting.ipynb", "Algorithms 12: Basic Sorting", 4, "Algorithms"),
    ("13_advanced_sorting.ipynb", "Algorithms 13: Advanced Sorting", 4, "Algorithms"),
    ("14_basic_matrix_arithmetic.ipynb", "Algorithms 14: Basic Matrix Arithmetic", 3, "Algorithms"),
    ("15_reduced_row_echelon_form.ipynb", "Algorithms 15: Reduced Row Echelon Form", 3, "Algorithms"),
    ("16_k_means_clustering.ipynb", "Algorithms 16: K-Means Clustering", 5, "Algorithms"),
    ("17_tic_tac_toe_connect_four.ipynb", "Algorithms 17: Tic-Tac-Toe and Connect Four", 4, "Algorithms"),
    ("18_euler_estimation.ipynb", "Algorithms 18: Euler Estimation", 2, "Algorithms"),
    ("19_sir_model.ipynb", "Algorithms 19: SIR Model", 2, "Algorithms"),
    ("20_hodgkin_huxley.ipynb", "Algorithms 20: Hodgkin-Huxley Model", 2, "Algorithms"),
    ("21_hash_tables.ipynb", "Algorithms 21: Hash Tables", 4, "Algorithms"),
    ("22_simplex_method.ipynb", "Algorithms 22: Simplex Method", 3, "Algorithms"),
    ("23-25_regression_pseudoinverse.ipynb", "Algorithms 23-25: Regression via Pseudoinverse", 3, "Algorithms"),
    ("26_overfitting_bias_variance.ipynb", "Algorithms 26: Overfitting, Underfitting, and Bias-Variance", 5, "Algorithms"),
    ("27-28_regression_gradient_descent.ipynb", "Algorithms 27-28: Regression via Gradient Descent", 5, "Algorithms"),
    ("29_k_nearest_neighbors.ipynb", "Algorithms 29: K-Nearest Neighbors", 5, "Algorithms"),
    ("30_naive_bayes.ipynb", "Algorithms 30: Naive Bayes Classification", 5, "Algorithms"),
    ("31_bfs_dfs.ipynb", "Algorithms 31: Breadth-First and Depth-First Search", 4, "Algorithms"),
    ("32-33_shortest_paths_dijkstra.ipynb", "Algorithms 32-33: Shortest Paths and Dijkstra", 4, "Algorithms"),
    ("34_decision_trees.ipynb", "Algorithms 34: Decision Trees", 5, "Algorithms"),
    ("35-36_neural_networks.ipynb", "Algorithms 35-36: Artificial Neural Networks", 6, "Algorithms"),
    ("37-39_minimax_game_trees.ipynb", "Algorithms 37-39: Minimax and Game Trees", 7, "Algorithms"),
    ("40-42_neuroevolution.ipynb", "Algorithms 40-42: Neuroevolution and Blondie24", 7, "Algorithms"),
    ("43_convolutional_blondie24.ipynb", "Algorithms 43: Convolutional Blondie24", 6, "Algorithms"),
]


def notebook_id(filename: str) -> str:
    return filename.removesuffix(".ipynb").replace("-", "_")


def skill_base(filename: str) -> str:
    clean = notebook_id(filename)
    prefix = "lesson"
    if clean.startswith("math_00"):
        prefix = "foundation"
    elif clean.startswith("math_"):
        prefix = "math"
    elif clean[:2].isdigit():
        prefix = "algorithms"
    return f"{prefix}.{clean}"


def topic_from_title(title: str) -> str:
    return title.split(":", 1)[-1].strip()


def _foundation_detail(filename: str) -> tuple[list[str], list[LessonSection], list[RetrievalSpec], list[ExerciseSpec], str]:
    sid = skill_base(filename)
    if filename == "math_00_diagnostic.ipynb":
        retrieval = [
            RetrievalSpec("What is 8 * 7?", ["56"], f"{sid}.retrieval", "56"),
            RetrievalSpec("What is 2 + 3 * 4?", ["14"], f"{sid}.retrieval", "14"),
            RetrievalSpec("If f(x) = x + 5, what is f(9)?", ["14"], f"{sid}.retrieval", "14"),
            RetrievalSpec("Solve x + 3 = 10.", ["7", "x=7", "x = 7"], f"{sid}.retrieval", "7"),
        ]
        return (
            ["Retrieve prerequisite knowledge.", "Locate a comfortable starting point.", "Initialize the progress dashboard."],
            [
                LessonSection("Micro-Lesson", "A diagnostic is a map, not a grade. Answer from memory so the dashboard can expose which ideas need review."),
                LessonSection("Worked Example", "If an item asks for x + 3 = 10, undo the +3 by subtracting 3 from both sides, giving x = 7."),
                LessonSection("Faded Example", "For x + 5 = 12, undo the +5 by subtracting ____ from both sides."),
            ],
            retrieval,
            [],
            "Choose the first later notebook whose retrieval questions felt effortful.",
        )
    if filename == "math_00_python_arithmetic.ipynb":
        return (
            ["Evaluate Python arithmetic.", "Store intermediate values.", "Write small functions with return values."],
            [
                LessonSection("Micro-Lesson", "Python expressions follow mathematical order of operations. Variables name intermediate results so you can inspect and reuse them."),
                LessonSection("Worked Example", "`total = 3 * 750 + 2 * 125` computes three notebooks and two pens, then stores the value for later checks."),
                LessonSection("Faded Example", "If a ticket costs 350, four tickets cost `4 * ____`."),
            ],
            [
                RetrievalSpec("What is 7 + 8?", ["15"], f"{sid}.retrieval", "15"),
                RetrievalSpec("What is 6 * 9?", ["54"], f"{sid}.retrieval", "54"),
            ],
            [
                ExerciseSpec(
                    "Write `ticket_total(price, quantity)` so it returns total cost.",
                    "def ticket_total(price, quantity):\n    # student scaffold: compute price times quantity\n    return None",
                    "def ticket_total(price, quantity):\n    return price * quantity",
                    "code_check('ticket_total', ticket_total, [((350, 4), 1400), ((125, 2), 250)], skill_id=SKILLS[1]['id'], store=store)",
                    ["Total means repeated equal price.", "Use multiplication.", "Return `price * quantity`."],
                    f"{sid}.implementation",
                    "Compute a Total",
                )
            ],
            "Write a discount function that returns price after a percentage discount.",
        )
    if filename == "math_00_pre_algebra.ipynb":
        return (
            ["Apply order of operations.", "Use fractions as division.", "Connect proportions to multiplication."],
            [
                LessonSection("Micro-Lesson", "Pre-algebra is arithmetic with structure. Parentheses bind first, then multiplication and division, then addition and subtraction."),
                LessonSection("Worked Example", "`2 + 3 * (10 - 6)` becomes `2 + 3 * 4`, then `2 + 12`, then `14`."),
                LessonSection("Faded Example", "`5 + 2 * (9 - 4)` first evaluates the parentheses to ____."),
            ],
            [
                RetrievalSpec("In 2 + 3 * 4, which operation happens first?", ["multiplication", "*", "multiply"], f"{sid}.retrieval", "multiplication"),
                RetrievalSpec("What does 3/4 mean as division?", ["3 divided by 4", "3/4", "3 over 4"], f"{sid}.retrieval", "3 divided by 4"),
            ],
            [
                ExerciseSpec(
                    "Write `fraction_of(numerator, denominator, amount)`.",
                    "def fraction_of(numerator, denominator, amount):\n    # student scaffold: multiply amount by the fraction\n    return None",
                    "def fraction_of(numerator, denominator, amount):\n    return numerator / denominator * amount",
                    "code_check('fraction_of', fraction_of, [((3, 4, 20), 15), ((1, 2, 50), 25)], skill_id=SKILLS[1]['id'], store=store)",
                    ["A fraction of an amount means multiply.", "Build the fraction with division.", "Use `numerator / denominator * amount`."],
                    f"{sid}.implementation",
                    "Fraction of a Quantity",
                )
            ],
            "Scale a recipe that uses 3/4 cup per batch to any number of batches.",
        )
    return (
        ["Read functions as input-output rules.", "Build tables.", "Connect formulas to graphs."],
        [
            LessonSection("Micro-Lesson", "A function turns each allowed input into an output. A table lists pairs; a graph places those pairs on axes."),
            LessonSection("Worked Example", "For f(x) = 2x + 1, f(3) = 7, so (3, 7) is on the graph."),
            LessonSection("Faded Example", "For g(x) = 4x - 2, g(5) = ____."),
        ],
        [
            RetrievalSpec("If f(x) = 2x + 1, what is f(3)?", ["7"], f"{sid}.retrieval", "7"),
            RetrievalSpec("In y = 3x + 2, what number gives the repeated change?", ["3", "slope"], f"{sid}.retrieval", "3"),
        ],
        [
            ExerciseSpec(
                "Write `build_table(fn, xs)` to return `(x, fn(x))` pairs.",
                "def build_table(fn, xs):\n    table = []\n    # student scaffold: append one pair for each x\n    return table",
                "def build_table(fn, xs):\n    table = []\n    for x in xs:\n        table.append((x, fn(x)))\n    return table",
                "code_check('build_table', build_table, [((lambda x: 2*x + 1, [0, 1, 2]), [(0, 1), (1, 3), (2, 5)])], skill_id=SKILLS[1]['id'], store=store)",
                ["Loop over inputs.", "Call the function on each input.", "Append `(x, fn(x))`."],
                f"{sid}.implementation",
                "Build a Table",
            )
        ],
        "Create a table for a taxi rule with a base fee plus price per kilometer.",
    )


def _generic_lesson(filename: str, title: str, level: int, track: str) -> LessonSpec:
    topic = topic_from_title(title)
    sid = skill_base(filename)
    objectives = [
        f"Explain the core idea of {topic}.",
        f"Trace a small {topic} example by hand before coding.",
        f"Implement a compact Python helper for {topic}.",
        f"Use tests and sanity checks to verify behavior.",
    ]
    sections = [
        LessonSection(
            "Micro-Lesson",
            f"{topic} is best learned as a loop between representation, procedure, and verification. First name the state you are tracking, then describe the update rule, then test the rule on a small case where the answer can be checked by hand.",
        ),
        LessonSection(
            "Worked Example",
            f"For a small {topic} problem, write the inputs, predict one step manually, and only then translate the step into Python. This keeps the code connected to the mathematics instead of becoming a memorized recipe.",
        ),
        LessonSection(
            "Faded Example",
            f"When solving a new {topic} task, fill these blanks: state = ____, update = ____, stopping condition = ____, check = ____.",
        ),
    ]
    retrieval = [
        RetrievalSpec(
            "What is the first thing to identify before implementing an algorithmic or mathematical procedure?",
            ["state", "the state", "inputs", "representation"],
            f"{sid}.retrieval",
            "state",
        ),
        RetrievalSpec(
            "Why should you test on a tiny example before a large one?",
            ["sanity check", "debugging", "verify", "catch errors", "easier to inspect"],
            f"{sid}.retrieval",
            "sanity check",
        ),
    ]
    exercise = ExerciseSpec(
        f"Implement `lesson_summary()` so it returns the topic and three habits used in {topic}.",
        "def lesson_summary():\n    topic = ''\n    habits = []\n    # student scaffold: fill topic and three habits\n    return {'topic': topic, 'habits': habits}",
        f"def lesson_summary():\n    topic = {topic!r}\n    habits = ['represent the state', 'trace a small case', 'verify with checks']\n    return {{'topic': topic, 'habits': habits}}",
        f"summary = lesson_summary()\ncheck('topic recorded', summary['topic'], {topic!r}, skill_id=SKILLS[1]['id'], store=store)\ncheck('three habits', len(summary['habits']), 3, skill_id=SKILLS[1]['id'], store=store)",
        ["Name the notebook topic exactly.", "Use three short action phrases.", "Return a dictionary with keys `topic` and `habits`."],
        f"{sid}.implementation",
        "Summarize the Method",
    )
    return LessonSpec(
        id=notebook_id(filename),
        filename=filename,
        title=title,
        level=level,
        track=track,
        objectives=objectives,
        prerequisites=[],
        skills=[f"{sid}.retrieval", f"{sid}.implementation", f"{sid}.transfer"],
        lesson_sections=sections,
        retrieval=retrieval,
        exercises=[exercise],
        transfer_challenge=f"Adapt the same representation-update-check pattern to a fresh {topic} example that is not shown in this notebook.",
    )


def build_specs() -> list[LessonSpec]:
    rows = [*FOUNDATION_LESSONS, *MATH_LESSONS, *ALGORITHM_LESSONS]
    specs: list[LessonSpec] = []
    previous_skills: list[str] = []
    for index, (filename, title, level, track) in enumerate(rows):
        if track == "Foundations":
            objectives, sections, retrieval, exercises, transfer = _foundation_detail(filename)
            sid = skill_base(filename)
            skills = [f"{sid}.retrieval", f"{sid}.implementation", f"{sid}.transfer"]
            if filename == "math_00_diagnostic.ipynb":
                skills = [f"{sid}.retrieval", f"{sid}.transfer"]
        else:
            spec = _generic_lesson(filename, title, level, track)
            objectives = spec.objectives
            sections = spec.lesson_sections
            retrieval = spec.retrieval
            exercises = spec.exercises
            transfer = spec.transfer_challenge
            skills = spec.skills
        next_notebook = rows[index + 1][0] if index + 1 < len(rows) else None
        spec = LessonSpec(
            id=notebook_id(filename),
            filename=filename,
            title=title,
            level=level,
            track=track,
            objectives=objectives,
            prerequisites=previous_skills[-2:],
            skills=skills,
            lesson_sections=sections,
            retrieval=retrieval,
            exercises=exercises,
            transfer_challenge=transfer,
            next_notebook=next_notebook,
        )
        specs.append(spec)
        previous_skills = skills
    return specs
