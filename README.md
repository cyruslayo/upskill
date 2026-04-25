# Introduction to Algorithms and Machine Learning

Welcome to the interactive, from-scratch curriculum for algorithms and machine learning! 

Based on the highly rigorous pedagogy of **The Math Academy Way** combined with **The Soviet Mathematical Tradition**, this curriculum takes you from basic variables and loops all the way to backpropagation and neuroevolution—all without relying on "black box" external machine learning libraries.

## Pedagogical Principles

This curriculum is an interactive mathematical laboratory that synthesizes two highly effective educational philosophies:

1. **The Math Academy Way**: Emphasizes minimizing cognitive load, coding algorithms from scratch, micro-scaffolding, interleaved practice, and spaced repetition to build procedural fluency and talent rapidly.
2. **The Soviet Mathematical Tradition**: Emphasizes axiomatic rigor, experimental mathematics, guided discovery, and non-routine "Olympiad-level" problem solving to build profound theoretical understanding and algorithmic resilience.

## The 5-Phase Notebook Architecture (Lesson Plan)

Every notebook in this curriculum follows a strict 5-Phase progression:

### Phase -1: The Theoretical Proof (Kiselev/Gelfand Rigor)
*   **Goal**: Guided discovery and axiomatic proof before any code is written.
*   **Instruction**: Use the provided Markdown or code cell to derive a formula or theorem symbolically using LaTeX or the `sympy` library.

### Phase 0: Math Foundation Practice
*   **Goal**: Mastering the abstract math mechanics in isolation.   
*   **Instruction**: Write base Python code for the specific math operation (e.g., dot product, chain rule, algebraic inverse, inequalities) required for the upcoming algorithm, bridging the gap between theory and application.

### Phase 1: Micro-Scaffolded Algorithm Construction (Math Academy)
*   **Goal**: Building the core algorithm from scratch with minimized cognitive load.
*   **Instruction**: Complete the step-by-step coding cells without using external ML libraries. Engage with **Interleaved Practice** and **Spaced Repetition** exercises built into the flow.

### Phase 2: Experimental Verification & Visualization (Arnold's Trivium)
*   **Goal**: Building geometric intuition and exposing algorithmic flaws.
*   **Instruction**: Execute the verification cells. Compare your from-scratch results against industry standards (like `scikit-learn` or `numpy.linalg`). The notebook will intentionally feed your algorithm a breaking edge-case (pathological data) to force an experimental failure. Use interactive plots (`plotly`, `matplotlib`) to visualize the failure.

### Phase 3: Olympiad Extension & Chalkboard Defense
*   **Goal**: Non-routine problem solving and oral defense proxy.   
*   **Instruction**: Complete the Olympiad Task, a 0-scaffolding coding cell where you must invent a workaround for the failure observed in Phase 2. Finally, write a rigorous mathematical defense of your algorithmic choices and time complexity in the Chalkboard Defense Markdown cell.

## Learning Path

The curriculum is structured into 43 Main Track Notebooks and 7 Math Foundations Notebooks. 

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
- `mathematics/notebooks/`: Contains the 43 student-facing Jupyter Notebooks and 7 Math Foundations Notebooks.
- `mathematics/solutions/`: Contains the completed, fully-coded versions for reference (Instructor Keys).
- `mathematics/textbooks/`: Markdown and PDF textbooks acting as foundational references.
- `datasets/`: Toy datasets (CSV files) loaded in later regression and classification modules.

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
4. Open the `mathematics/notebooks/` directory and start with `01_introductory_coding.ipynb`! Note that every notebook includes a Google Colab setup cell, so you can easily run them in the cloud.