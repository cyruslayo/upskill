# Introduction to Algorithms and Machine Learning

Welcome to the interactive, from-scratch curriculum for algorithms and machine learning.

This repo now ships as a Colab-first learning environment with retrieval practice, spaced review, staged hints, mastery tracking, and instructor solution notebooks. The curriculum still follows the original blend of **The Math Academy Way** and **The Soviet Mathematical Tradition**, but the notebooks now actively support recall, feedback, and progression rather than just exposition.

## Pedagogical Principles

This curriculum is an interactive mathematical laboratory that synthesizes two highly effective educational philosophies:

1. **The Math Academy Way**: Emphasizes minimizing cognitive load, coding algorithms from scratch, micro-scaffolding, interleaved practice, and spaced repetition to build procedural fluency and talent rapidly.
2. **The Soviet Mathematical Tradition**: Emphasizes axiomatic rigor, experimental mathematics, guided discovery, and non-routine "Olympiad-level" problem solving to build profound theoretical understanding and algorithmic resilience.

## Notebook Architecture

The notebooks use a retrieval-first structure:

1. Retrieve prerequisite ideas before the lesson.
2. Read a short micro-lesson and worked example.
3. Solve faded examples and independent practice.
4. Run checks and record confidence.
5. Reveal hints only after an attempt.
6. End with cumulative review and the mastery dashboard.

The older 5-phase lesson framing still appears inside many notebooks, but it now sits inside this retrieval loop instead of replacing it.

## Interactive Learning Environment

This repo now includes a Colab-first interactive layer:

- `learning_tools.py` provides progress tracking, retrieval checks, spaced review scheduling, staged hints, and mastery dashboards.
- `curriculum/skills.json` defines the skill registry used by the review system.
- `mathematics/notebooks/clean_specs.py` defines the lesson specs for the rebuilt curriculum.
- `mathematics/notebooks/generate_clean_notebooks.py` is the source-of-truth generator for all student and instructor notebooks.
- `mathematics/legacy/notebooks/` and `mathematics/legacy/solutions/` preserve the pre-rebuild notebooks.
- `curriculum/legacy_solution_bank.py` remains as a reference helper for older implementations.
- Progress is stored in Google Drive when running in Colab, with a local JSON fallback.

The intended learning loop is:

1. Retrieve prerequisite knowledge before reading.
2. Study a short micro-lesson and worked example.
3. Complete faded examples and independent practice.
4. Run active checks and record confidence.
5. Use staged hints only after a real attempt.
6. End with cumulative review and the mastery dashboard.

## Learning Path

The curriculum is structured into a Level 0 foundations ramp, 7 Math Foundations notebooks, and the algorithms and machine-learning sequence. Every current notebook is generated from the same clean spec format, and the combined notebooks remain combined where the original curriculum did that intentionally.

### Level 0: Foundations Track
Focus: absolute fundamentals before algebra and algorithms.
*   **Diagnostic**: Placement and prerequisite recall.
*   **Math 00A**: Python Arithmetic and Variables.
*   **Math 00B**: Pre-Algebra Foundations.
*   **Math 00C**: Functions, Tables, and Graphs.

### Math Foundations Track
Focus: Learning the underlying mathematics from start to finish, built from scratch.
*   **Math Notebook 01**: Algebra - Linear Equations
*   **Math Notebook 02**: Calculus - Derivatives & Power Rule
*   **Math Notebook 03**: Calculus - Chain Rule
*   **Math Notebook 04**: Calculus - Local Extrema
*   **Math Notebook 05**: Linear Algebra - Vectors and Dot Products
*   **Math Notebook 06**: Linear Algebra - Matrices and Transformations
*   **Math Notebook 07**: Calculus - Differential Equations (Euler)

### Part I: Hello World
Focus: Basic coding structures, loops, conditionals, arrays, functions, without external libraries.
*   **Notebooks 01-06**: Introductory Coding, Number Systems, Recursive Sequences, Simulating Randomness, Roulette Wheel Selection, Cartesian Product.

### Part II: Searching and Sorting
Focus: Algorithmic thinking, search strategies, and foundational machine learning concepts (Gradient Descent).
*   **Notebooks 07-13**: Brute Force Search & Cryptography, Backtracking, Estimating Roots, Single & Multivariable Gradient Descent, Basic & Advanced Sorting.

### Part III: Objects
Focus: Classes, Object-Oriented Programming, and applying them to math and modeling.
*   **Notebooks 14-22**: Basic Matrix Arithmetic, Reduced Row Echelon Form, K-Means Clustering, Tic-Tac-Toe/Connect Four, Euler Estimation, SIR Model, Hodgkin-Huxley Model, Hash Tables, Simplex Method.

### Part IV: Regression and Classification
Focus: Supervised learning models.
*   **Notebooks 23-30**: Linear, Polynomial & Nonlinear Regression via Pseudoinverse, Overfitting & Bias-Variance Tradeoff, Regression via Gradient Descent, K-Nearest Neighbors, Naive Bayes.

### Part V: Graphs
Focus: Graph theory and Neural Networks.
*   **Notebooks 31-36**: Breadth-First and Depth-First Traversals, Shortest Paths & Dijkstra's Algorithm, Decision Trees, Neural Network Regressors & Backpropagation.

### Part VI: Games
Focus: AI game playing algorithms.
*   **Notebooks 37-43**: Minimax and Game Trees, Neuroevolution (Fogel's Tic-Tac-Toe & Blondie24), Convolutional Neuroevolution.

## Project Structure
- `mathematics/notebooks/`: Contains the generated student-facing notebooks.
- `mathematics/solutions/`: Contains the completed instructor solution notebooks for the same set.
- `mathematics/legacy/`: Contains archived notebooks from before the clean rebuild.
- `mathematics/textbooks/`: Markdown and PDF textbooks acting as foundational references.
- `datasets/`: Toy datasets (CSV files) loaded in later regression and classification modules.
- `curriculum/`: Shared curriculum metadata, the legacy solution bank, and the notebook completion indexes.
- `tests/`: Validation and audit checks for the learning runtime and notebook generation.

## Setup & Installation
1. Install Python 3.10+
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Open the `mathematics/notebooks/` directory and start with `math_00_diagnostic.ipynb`. From there, the dashboard will route you to the right starting point. Every notebook includes a Google Colab setup cell, so you can run the curriculum in the cloud.

## Regeneration and Validation

Archive the current notebooks before replacing canonical paths:

```bash
mkdir mathematics\legacy\notebooks mathematics\legacy\solutions
copy mathematics\notebooks\*.ipynb mathematics\legacy\notebooks\
copy mathematics\solutions\*.ipynb mathematics\legacy\solutions\
```

Regenerate every student notebook, instructor solution notebook, and curriculum metadata file:

```bash
python mathematics/notebooks/generate_clean_notebooks.py
```

Validate the generated notebooks:

```bash
python tests/validate_interactive_notebooks.py
```

Run the unit tests. On this Windows setup, use `PYTHONPATH=.` and disable the pytest cache to avoid local cache-directory permission noise:

```bash
$env:PYTHONPATH='.'; pytest -q -p no:cacheprovider tests\test_learning_tools.py tests\test_legacy_solution_bank.py
```
