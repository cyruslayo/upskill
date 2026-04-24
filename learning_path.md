# Learning Path: Introduction to Algorithms and Machine Learning

This learning path maps the chapters from the core text to Jupyter Notebooks, incorporating spaced repetition, interleaved practice, and targeted math foundations.

## Math Foundations Track
Focus: Learning the underlying mathematics from start to finish, built from scratch using the Math Academy pedagogical principles.

*   **Math Notebook 01: Algebra - Linear Equations** (Reference: `justinmath-algebra.md` Sec 1.1)
*   **Math Notebook 02: Calculus - Derivatives & Power Rule** (Reference: `justinmath-calculus.md` Sec 1.3, 1.4)
*   **Math Notebook 03: Calculus - Chain Rule** (Reference: `justinmath-calculus.md` Sec 1.5)
*   **Math Notebook 04: Calculus - Local Extrema** (Reference: `justinmath-calculus.md` Sec 1.8)
*   **Math Notebook 05: Linear Algebra - Vectors and Dot Products** (Reference: `justinmath-linearAlgebra.md` Sec 1.1, 1.2)
*   **Math Notebook 06: Linear Algebra - Matrices and Transformations** (Reference: `justinmath-linearAlgebra.md` Sec 3.1, 3.2)
*   **Math Notebook 07: Calculus - Differential Equations (Euler)** (Reference: `justinmath-calculus.md` Sec 3.2)

---

## Part I: Hello World
Focus: Basic coding structures, loops, conditionals, arrays, functions, without external libraries.

*   **Notebook 01: Introductory Coding Exercises**
    *   **Goal**: Basic Python functions from scratch (checking symmetry, character counts, primes).
    *   **Pedagogy**: Micro-scaffolding for each function.
*   **Notebook 02: Number Systems**
    *   **Goal**: Converting binary, decimal, hexadecimal.
    *   **Pedagogy**: Spaced repetition of loops and array manipulations from Notebook 01.
*   **Notebook 03: Recursive Sequences**
    *   **Goal**: Generating recursive sequences (Collatz, Fibonacci) iteratively and recursively.
    *   **Pedagogy**: Interleave iterative and recursive implementations.
*   **Notebook 04: Simulating Randomness**
    *   **Goal**: Monte Carlo simulations, estimating coin flip probabilities.
    *   **Pedagogy**: Micro-scaffolding to build custom simulation functions.
*   **Notebook 05: Roulette Wheel Selection**
    *   **Goal**: Sampling from discrete probability distributions.
    *   **Pedagogy**: Spaced repetition of probability estimation from Notebook 04.
*   **Notebook 06: Cartesian Product**
    *   **Goal**: Implement Cartesian product of arrays.
    *   **Pedagogy**: Interleaved practice applying Cartesian products to earlier sequence concepts.

## Part II: Searching and Sorting
Focus: Algorithmic thinking, search strategies, and foundational machine learning concepts (Gradient Descent).

*   **Notebook 07: Brute Force Search & Cryptography**
    *   **Goal**: Linear-encoding cryptography, brute force search.
    *   **Math Reference**: Algebra (Linear Equations) - `justinmath-algebra.md` Section 1.1.
*   **Notebook 08: Backtracking**
    *   **Goal**: Solving Magic Squares.
    *   **Pedagogy**: Micro-scaffolding to structure the recursive backtracking logic.
*   **Notebook 09: Estimating Roots**
    *   **Goal**: Bisection Search and Newton-Raphson Method.
    *   **Math Reference**: Calculus (Derivatives) - `justinmath-calculus.md` Sections 1.3, 1.4.
*   **Notebook 10: Single-Variable Gradient Descent**
    *   **Goal**: Optimization and local/global minima.
    *   **Math Reference**: Calculus (Finding Local Extrema) - `justinmath-calculus.md` Section 1.8.
*   **Notebook 11: Multivariable Gradient Descent**
    *   **Goal**: Optimization in multiple dimensions.
    *   **Math Reference**: Linear Algebra (Vectors) - `justinmath-linearAlgebra.md` Section 1.1.
*   **Notebook 12: Basic Sorting**
    *   **Goal**: Selection, Bubble, Insertion, and Counting Sort.
    *   **Pedagogy**: Interleaved practice of multiple sorting algorithms and time complexity estimation.
*   **Notebook 13: Advanced Sorting**
    *   **Goal**: Merge Sort and Quicksort.
    *   **Pedagogy**: Spaced repetition comparing performance with basic sorting algorithms.

## Part III: Objects
Focus: Classes, Object-Oriented Programming, and applying them to math and modeling.

*   **Notebook 14: Basic Matrix Arithmetic**
    *   **Goal**: Matrix addition, subtraction, transpose, and multiplication.
    *   **Math Reference**: Linear Algebra (Matrices) - `justinmath-linearAlgebra.md` Section 3.1, 3.2.
*   **Notebook 15: Reduced Row Echelon Form (RREF)**
    *   **Goal**: Computing RREF, inverses, and determinants.
    *   **Math Reference**: Linear Algebra (Elimination) - `justinmath-linearAlgebra.md` Section 1.5, 3.4.
*   **Notebook 16: K-Means Clustering**
    *   **Goal**: Unsupervised learning for clustering data.
    *   **Pedagogy**: Micro-scaffolding to build distance and cluster assignment functions.
*   **Notebook 17: Tic-Tac-Toe and Connect Four**
    *   **Goal**: Modeling games using objects.
    *   **Pedagogy**: Interleaved practice modeling two different games with similar turn-based logic.
*   **Notebook 18: Euler Estimation**
    *   **Goal**: Numerical solutions for differential equations.
    *   **Math Reference**: Calculus (Differential Equations) - `justinmath-calculus.md` Section 3.2.
*   **Notebook 19: SIR Model For the Spread of Disease**
    *   **Goal**: Applying Euler estimation to the SIR epidemiological model.
    *   **Pedagogy**: Spaced repetition of Euler estimation from Notebook 18.
*   **Notebook 20: Hodgkin-Huxley Model**
    *   **Goal**: Modeling action potentials in neurons.
    *   **Pedagogy**: Interleaved integration of complex differential equations.
*   **Notebook 21: Hash Tables**
    *   **Goal**: Implementing Hash Tables and understanding buckets.
    *   **Pedagogy**: Micro-scaffolding hashing and indexing.
*   **Notebook 22: Simplex Method**
    *   **Goal**: Optimization algorithm for linear programming.
    *   **Math Reference**: Algebra (Inequalities) - `justinmath-algebra.md` Section 3.4.

## Part IV: Regression and Classification
Focus: Supervised learning models.

*   **Notebook 23-25: Linear, Polynomial, and Nonlinear Regression via Pseudoinverse**
    *   **Goal**: Implementing regression using matrices, including Logistic and Exponential data transformations.
*   **Notebook 26: Overfitting and Bias-Variance Tradeoff**
    *   **Goal**: Cross-validation techniques.
    *   **Pedagogy**: Interleaved testing of different regression models.
*   **Notebook 27-28: Regression via Gradient Descent**
    *   **Goal**: Gradient descent applied to multiple regression, including Interaction Terms.
    *   **Pedagogy**: Spaced repetition of Gradient Descent from Part II.
*   **Notebook 29: K-Nearest Neighbors**
    *   **Goal**: Implementing KNN classification.
    *   **Pedagogy**: Spaced repetition of distances from K-Means (Part III).
*   **Notebook 30: Naive Bayes**
    *   **Goal**: Probabilistic classification.
    *   **Pedagogy**: Micro-scaffolding probability distributions.

## Part V: Graphs
Focus: Graph theory and Neural Networks.

*   **Notebook 31: Breadth-First and Depth-First Traversals**
    *   **Goal**: Graph traversal algorithms.
    *   **Pedagogy**: Interleaved DFS and BFS implementations.
*   **Notebook 32-33: Shortest Paths and Dijkstra's Algorithm**
    *   **Goal**: Distance finding in unweighted and weighted graphs.
    *   **Pedagogy**: Micro-scaffolding for priority queues and distances.
*   **Notebook 34: Decision Trees**
    *   **Goal**: Classification with trees.
    *   **Math Reference**: Algebra (Logarithms) - `justinmath-algebra.md` Section 6.2.
    *   **Pedagogy**: Interleaved logic with recursion.
*   **Notebook 35-36: Neural Network Regressors & Backpropagation**
    *   **Goal**: Building simple neural networks.
    *   **Math Reference**: Calculus (Chain Rule) - `justinmath-calculus.md` Section 1.5.

## Part VI: Games
Focus: AI game playing algorithms.

*   **Notebook 37-39: Minimax and Game Trees**
    *   **Goal**: Implementing Minimax and Heuristic evaluation for Tic-Tac-Toe/Connect Four.
    *   **Pedagogy**: Spaced repetition using game logic from Notebook 17.
*   **Notebook 40-42: Neuroevolution (Fogel's Tic-Tac-Toe & Blondie24)**
    *   **Goal**: Co-evolutionary training without explicit fitness and standard MLP evaluation.
    *   **Pedagogy**: Interleaved practice combining neural networks and game logic.
*   **Notebook 43: Convolutional Neuroevolution**
    *   **Goal**: Implementing 2D Convolutional layers from scratch for board evaluation.
    *   **Pedagogy**: Micro-scaffolding the spatial filtering mechanics.