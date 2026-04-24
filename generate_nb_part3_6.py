import nbformat as nbf
import os

def create_notebook(title, cells_content, filename):
    nb = nbf.v4.new_notebook()
    cells = []
    cells.append(nbf.v4.new_markdown_cell(f"# {title}"))
    for c_type, content in cells_content:
        if c_type == "md":
            cells.append(nbf.v4.new_markdown_cell(content))
        elif c_type == "code":
            cells.append(nbf.v4.new_code_cell(content))
    nb['cells'] = cells
    os.makedirs('notebooks', exist_ok=True)
    with open(f'notebooks/{filename}', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Created {filename}")

# Notebooks 14-22 (Objects)
create_notebook("Notebook 14: Basic Matrix Arithmetic", [
    ("md", "## Concept Introduction\nMatrix addition, subtraction, transpose, and multiplication."),
    ("md", "## 1. Micro-Scaffolding: Matrix Addition\nWrite a function to add two matrices."),
    ("code", "def matrix_add(A, B):\n    pass"),
    ("md", "## 2. Interleaved Practice: Matrix Multiplication\nWrite a function to multiply two matrices."),
    ("code", "def matrix_multiply(A, B):\n    pass"),
    ("md", "## 3. Spaced Repetition: Recursive Determinant\nWrite a function to compute the determinant of a matrix recursively."),
    ("code", "def determinant(A):\n    pass")
], "14_basic_matrix_arithmetic.ipynb")

create_notebook("Notebook 15: Reduced Row Echelon Form (RREF)", [
    ("md", "## Concept Introduction\nComputing RREF, inverses, and determinants."),
    ("md", "## 1. Micro-Scaffolding: RREF Helper Functions\nWrite a function to swap rows and scale a row."),
    ("code", "def swap_rows(M, r1, r2):\n    pass\n\ndef scale_row(M, r, scalar):\n    pass"),
    ("md", "## 2. Interleaved Practice: RREF\nWrite a function to compute RREF of a matrix."),
    ("code", "def rref(M):\n    pass"),
    ("md", "## 3. Spaced Repetition: Inverse via RREF\nCompute the inverse of a matrix using your RREF function."),
    ("code", "def inverse(M):\n    pass")
], "15_reduced_row_echelon_form.ipynb")

create_notebook("Notebook 16: K-Means Clustering", [
    ("md", "## Concept Introduction\nUnsupervised learning for clustering data."),
    ("md", "## 1. Micro-Scaffolding: Distance Function\nWrite a function to compute the distance between two points."),
    ("code", "def distance(p1, p2):\n    pass"),
    ("md", "## 2. Interleaved Practice: Cluster Assignment\nWrite a function to assign points to the nearest cluster centroid."),
    ("code", "def assign_clusters(points, centroids):\n    pass"),
    ("md", "## 3. Spaced Repetition: K-Means Algorithm\nCombine your functions to implement the full K-Means algorithm."),
    ("code", "def k_means(points, k, iters):\n    pass")
], "16_k_means_clustering.ipynb")

create_notebook("Notebook 17: Tic-Tac-Toe and Connect Four", [
    ("md", "## Concept Introduction\nModeling games using objects."),
    ("md", "## 1. Micro-Scaffolding: Tic-Tac-Toe Board\nCreate a class to represent a Tic-Tac-Toe board."),
    ("code", "class TicTacToe:\n    pass"),
    ("md", "## 2. Interleaved Practice: Connect Four Board\nCreate a class for Connect Four using similar logic."),
    ("code", "class ConnectFour:\n    pass"),
    ("md", "## 3. Spaced Repetition: Game Loop\nWrite a loop to allow random players to play against each other."),
    ("code", "def random_game_loop(game):\n    pass")
], "17_tic_tac_toe_connect_four.ipynb")

create_notebook("Notebook 18: Euler Estimation", [
    ("md", "## Concept Introduction\nNumerical solutions for differential equations."),
    ("md", "## 1. Micro-Scaffolding: Single-Variable Euler\nWrite a function for single-variable Euler estimation."),
    ("code", "def euler_estimation(f, initial_val, dt, steps):\n    pass"),
    ("md", "## 2. Interleaved Practice: Multivariable Euler\nExtend your function to multivariable Euler estimation."),
    ("code", "def multivariable_euler(f_list, initial_vals, dt, steps):\n    pass"),
    ("md", "## 3. Spaced Repetition: Estimating Roots\nUse your Newton-Raphson implementation from Notebook 09 to find a root, comparing with Euler method."),
    ("code", "# Compare Newton-Raphson and Euler estimation")
], "18_euler_estimation.ipynb")

create_notebook("Notebook 19: SIR Model For the Spread of Disease", [
    ("md", "## Concept Introduction\nApplying Euler estimation to the SIR epidemiological model."),
    ("md", "## 1. Micro-Scaffolding: SIR Equations\nWrite functions representing the SIR differential equations."),
    ("code", "def dS_dt(S, I, beta, N):\n    pass\n\ndef dI_dt(S, I, beta, gamma, N):\n    pass\n\ndef dR_dt(I, gamma):\n    pass"),
    ("md", "## 2. Interleaved Practice: SIR Simulation\nSimulate the model using your multivariable Euler estimator."),
    ("code", "def simulate_sir(S0, I0, R0, beta, gamma, days, dt):\n    pass"),
    ("md", "## 3. Spaced Repetition: Multivariable GD\nUse multivariable gradient descent (from Notebook 11) to optimize `beta` and `gamma` based on target data."),
    ("code", "def optimize_sir_params(data):\n    pass")
], "19_sir_model.ipynb")

create_notebook("Notebook 20: Hodgkin-Huxley Model", [
    ("md", "## Concept Introduction\nModeling action potentials in neurons."),
    ("md", "## 1. Micro-Scaffolding: Ion Channels\nImplement functions for the sodium and potassium ion channel currents."),
    ("code", "def I_Na(V, m, h):\n    pass\n\ndef I_K(V, n):\n    pass"),
    ("md", "## 2. Interleaved Practice: Full Neuron Model\nSimulate the full Hodgkin-Huxley equations using Euler estimation."),
    ("code", "def simulate_neuron(I_ext, dt, steps):\n    pass"),
    ("md", "## 3. Spaced Repetition: K-Means\nCluster the voltage outputs over time to identify distinct action potential states using K-Means."),
    ("code", "# Apply K-Means from Notebook 16")
], "20_hodgkin_huxley.ipynb")

create_notebook("Notebook 21: Hash Tables", [
    ("md", "## Concept Introduction\nImplementing Hash Tables and understanding buckets."),
    ("md", "## 1. Micro-Scaffolding: Hash Function\nWrite a simple hash function for strings."),
    ("code", "def hash_string(string, num_buckets):\n    pass"),
    ("md", "## 2. Interleaved Practice: Hash Table Class\nImplement a Hash Table class with insert, get, and delete methods."),
    ("code", "class HashTable:\n    pass"),
    ("md", "## 3. Spaced Repetition: Character Counts\nRe-implement `count_characters` from Notebook 01 using your custom Hash Table."),
    ("code", "def count_characters_hashed(string):\n    pass")
], "21_hash_tables.ipynb")

create_notebook("Notebook 22: Simplex Method", [
    ("md", "## Concept Introduction\nOptimization algorithm for linear programming."),
    ("md", "## 1. Micro-Scaffolding: Slack Variables\nWrite a function to introduce slack variables to a linear program."),
    ("code", "def add_slack_variables(constraints):\n    pass"),
    ("md", "## 2. Interleaved Practice: Simplex Pivot\nImplement the pivot step for the Simplex method."),
    ("code", "def simplex_pivot(tableau):\n    pass"),
    ("md", "## 3. Spaced Repetition: Reduced Row Echelon Form\nNotice how the pivot step relates to computing RREF. Implement full Simplex method using this logic."),
    ("code", "def simplex_method(objective, constraints):\n    pass")
], "22_simplex_method.ipynb")

# Notebooks 23-25
create_notebook("Notebook 23-25: Regression via Pseudoinverse", [
    ("md", "## Concept Introduction\nImplementing regression using matrices."),
    ("md", "## 1. Micro-Scaffolding: Pseudoinverse\nWrite a function to compute the pseudoinverse of a matrix."),
    ("code", "def pseudoinverse(X):\n    pass"),
    ("md", "## 2. Interleaved Practice: Polynomial Regression\nImplement polynomial regression using the pseudoinverse."),
    ("code", "def polynomial_regression(X, Y, degree):\n    pass"),
    ("md", "## 3. Spaced Repetition: Nonlinear Functions\nFit a nonlinear function by combining multiple features and using the pseudoinverse."),
    ("code", "def nonlinear_regression(X, Y, functions):\n    pass")
], "23-25_regression_pseudoinverse.ipynb")

# Notebook 26
create_notebook("Notebook 26: Overfitting and Bias-Variance Tradeoff", [
    ("md", "## Concept Introduction\nCross-validation techniques."),
    ("md", "## 1. Micro-Scaffolding: Train-Test Split\nWrite a function to split data into training and testing sets."),
    ("code", "def train_test_split(X, Y, ratio):\n    pass"),
    ("md", "## 2. Interleaved Practice: Cross-Validation\nImplement K-fold cross-validation to evaluate your regression models."),
    ("code", "def k_fold_cross_validation(X, Y, model, k):\n    pass"),
    ("md", "## 3. Spaced Repetition: Analyzing Error\nCompute the Mean Squared Error (MSE) of the models to observe bias and variance."),
    ("code", "def compute_mse(Y_true, Y_pred):\n    pass")
], "26_overfitting_bias_variance.ipynb")

# Notebooks 27-28
create_notebook("Notebook 27-28: Regression via Gradient Descent", [
    ("md", "## Concept Introduction\nGradient descent applied to multiple regression."),
    ("md", "## 1. Micro-Scaffolding: Loss Function Gradient\nCompute the gradient of the MSE loss function with respect to weights."),
    ("code", "def mse_gradient(X, Y, weights):\n    pass"),
    ("md", "## 2. Interleaved Practice: Multiple Regression GD\nImplement multiple linear regression using gradient descent."),
    ("code", "def multiple_regression_gd(X, Y, alpha, iters):\n    pass"),
    ("md", "## 3. Spaced Repetition: Multivariable Gradient Descent\nUse your `multivariable_gd` function from Notebook 11 to optimize the weights directly."),
    ("code", "def optimize_weights_gd(X, Y):\n    pass")
], "27-28_regression_gradient_descent.ipynb")

# Notebook 29
create_notebook("Notebook 29: K-Nearest Neighbors", [
    ("md", "## Concept Introduction\nImplementing KNN classification."),
    ("md", "## 1. Micro-Scaffolding: Nearest Neighbors\nWrite a function to find the K nearest points to a target point."),
    ("code", "def get_neighbors(training_data, target, k):\n    pass"),
    ("md", "## 2. Interleaved Practice: KNN Classifier\nImplement the full KNN classification algorithm by choosing the majority class among neighbors."),
    ("code", "def knn_classify(training_data, labels, target, k):\n    pass"),
    ("md", "## 3. Spaced Repetition: Distance Functions\nReuse your distance functions from K-Means (Notebook 16) and test the effect on KNN accuracy."),
    ("code", "# Test different distance functions for KNN")
], "29_k_nearest_neighbors.ipynb")

# Notebook 30
create_notebook("Notebook 30: Naive Bayes", [
    ("md", "## Concept Introduction\nProbabilistic classification."),
    ("md", "## 1. Micro-Scaffolding: Probability Distributions\nCompute prior probabilities and conditional probabilities for a dataset."),
    ("code", "def compute_probabilities(data, labels):\n    pass"),
    ("md", "## 2. Interleaved Practice: Naive Bayes Classifier\nImplement the full Naive Bayes classification algorithm."),
    ("code", "def naive_bayes_classify(target, priors, conditionals):\n    pass"),
    ("md", "## 3. Spaced Repetition: Coin Flips\nUse Naive Bayes to classify whether a sequence of coin flips is biased or fair (referencing Notebook 04)."),
    ("code", "# Classify coin flips sequence")
], "30_naive_bayes.ipynb")

# Notebook 31
create_notebook("Notebook 31: Breadth-First and Depth-First Traversals", [
    ("md", "## Concept Introduction\nGraph traversal algorithms."),
    ("md", "## 1. Micro-Scaffolding: BFS Queue\nImplement Breadth-First Search using a queue."),
    ("code", "def bfs(graph, start_node):\n    pass"),
    ("md", "## 2. Interleaved Practice: DFS Stack\nImplement Depth-First Search iteratively using a stack, and recursively."),
    ("code", "def dfs_iterative(graph, start_node):\n    pass\n\ndef dfs_recursive(graph, node, visited=None):\n    pass"),
    ("md", "## 3. Spaced Repetition: Connected Components\nUse BFS or DFS to find all connected components in a graph, storing them in your Hash Table from Notebook 21."),
    ("code", "def find_connected_components(graph):\n    pass")
], "31_bfs_dfs.ipynb")

# Notebooks 32-33
create_notebook("Notebook 32-33: Shortest Paths and Dijkstra's Algorithm", [
    ("md", "## Concept Introduction\nDistance finding in unweighted and weighted graphs."),
    ("md", "## 1. Micro-Scaffolding: Priority Queue\nImplement a simple priority queue to retrieve the node with minimum distance."),
    ("code", "class PriorityQueue:\n    pass"),
    ("md", "## 2. Interleaved Practice: Dijkstra's Algorithm\nImplement Dijkstra's Algorithm to find the shortest path in a weighted graph."),
    ("code", "def dijkstra(graph, start_node):\n    pass"),
    ("md", "## 3. Spaced Repetition: Shortest Path via BFS\nShow that BFS finds the shortest path on an unweighted graph, and compare the result with Dijkstra's."),
    ("code", "def unweighted_shortest_path_bfs(graph, start_node):\n    pass")
], "32-33_shortest_paths_dijkstra.ipynb")

# Notebook 34
create_notebook("Notebook 34: Decision Trees", [
    ("md", "## Concept Introduction\nClassification with trees."),
    ("md", "## 1. Micro-Scaffolding: Information Gain\nWrite a function to compute entropy and information gain for splitting data."),
    ("code", "def calculate_entropy(labels):\n    pass\n\ndef information_gain(data, labels, split_feature):\n    pass"),
    ("md", "## 2. Interleaved Practice: Building the Tree\nImplement a recursive function to build the decision tree nodes."),
    ("code", "def build_decision_tree(data, labels):\n    pass"),
    ("md", "## 3. Spaced Repetition: Tree Traversal\nTraverse the generated decision tree using DFS to print its structure (referencing Notebook 31)."),
    ("code", "def print_tree_dfs(node):\n    pass")
], "34_decision_trees.ipynb")

# Notebooks 35-36
create_notebook("Notebook 35-36: Neural Network Regressors & Backpropagation", [
    ("md", "## Concept Introduction\nBuilding simple neural networks."),
    ("md", "## 1. Micro-Scaffolding: Forward Pass\nImplement the forward pass for a multi-layer perceptron."),
    ("code", "def forward_pass(inputs, weights, biases):\n    pass"),
    ("md", "## 2. Interleaved Practice: Backpropagation\nCompute the gradients using backpropagation for regression loss."),
    ("code", "def backpropagation(inputs, outputs, target, weights, biases):\n    pass"),
    ("md", "## 3. Spaced Repetition: Gradient Descent Optimization\nUse gradient descent (Notebook 10/11) to update the weights based on the backpropagation gradients."),
    ("code", "def train_network(X, Y, epochs, alpha):\n    pass")
], "35-36_neural_networks.ipynb")

# Notebooks 37-39
create_notebook("Notebook 37-39: Minimax and Game Trees", [
    ("md", "## Concept Introduction\nImplementing Minimax and Heuristic evaluation for Tic-Tac-Toe/Connect Four."),
    ("md", "## 1. Micro-Scaffolding: Minimax Algorithm\nWrite a basic recursive Minimax function."),
    ("code", "def minimax(state, depth, is_maximizing):\n    pass"),
    ("md", "## 2. Interleaved Practice: Alpha-Beta Pruning\nEnhance your Minimax function with alpha-beta pruning."),
    ("code", "def alphabeta(state, depth, alpha, beta, is_maximizing):\n    pass"),
    ("md", "## 3. Spaced Repetition: Connect Four Evaluation\nImplement a heuristic evaluation function for the Connect Four board built in Notebook 17."),
    ("code", "def evaluate_connect_four(state):\n    pass")
], "37-39_minimax_game_trees.ipynb")

# Notebooks 40-43
create_notebook("Notebook 40-43: Neuroevolution (Blondie24)", [
    ("md", "## Concept Introduction\nReimplementing Blondie24 using neural networks."),
    ("md", "## 1. Micro-Scaffolding: Neural Network Board Evaluator\nModify your Neural Network from Notebook 35 to evaluate board states."),
    ("code", "def evaluate_board_nn(board_state, nn_weights):\n    pass"),
    ("md", "## 2. Interleaved Practice: Evolutionary Algorithm\nImplement the selection, crossover, and mutation steps to evolve neural network weights."),
    ("code", "def evolve_population(population, fitness_scores):\n    pass"),
    ("md", "## 3. Spaced Repetition: Complete Blondie24 Loop\nCombine Neuroevolution with the Minimax game tree (Notebook 37) to train an AI to play Checkers or Tic-Tac-Toe."),
    ("code", "def train_blondie24_agent(generations):\n    pass")
], "40-43_neuroevolution.ipynb")

print("Generated notebooks 14-43")