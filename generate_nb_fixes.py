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
    print(f"Created/Updated {filename}")

# Notebooks 23-25 (Updated)
create_notebook("Notebook 23-25: Regression via Pseudoinverse", [
    ("md", "## Concept Introduction\nImplementing regression using matrices. Includes power, exponential, and logistic regression transformations."),
    ("md", "## 1. Micro-Scaffolding: Pseudoinverse\nWrite a function to compute the pseudoinverse of a matrix."),
    ("code", "def pseudoinverse(X):\n    pass"),
    ("md", "## 2. Interleaved Practice: Polynomial Regression\nImplement polynomial regression using the pseudoinverse."),
    ("code", "def polynomial_regression(X, Y, degree):\n    pass"),
    ("md", "## 3. Micro-Scaffolding: Logistic & Exponential Transformations\nWrite helper functions to transform the target variable `Y` (e.g., logit function for logistic regression, natural log for exponential regression) before applying the pseudoinverse."),
    ("code", "import math\n\ndef transform_exponential(Y):\n    pass\n\ndef transform_logistic(Y):\n    pass"),
    ("md", "## 4. Spaced Repetition: Nonlinear Functions\nFit a nonlinear function by combining multiple features and using the pseudoinverse."),
    ("code", "def nonlinear_regression(X, Y, functions):\n    pass")
], "23-25_regression_pseudoinverse.ipynb")

# Notebooks 27-28 (Updated)
create_notebook("Notebook 27-28: Regression via Gradient Descent", [
    ("md", "## Concept Introduction\nGradient descent applied to multiple regression, including interaction terms."),
    ("md", "## 1. Micro-Scaffolding: Loss Function Gradient\nCompute the gradient of the MSE loss function with respect to weights."),
    ("code", "def mse_gradient(X, Y, weights):\n    pass"),
    ("md", "## 2. Interleaved Practice: Multiple Regression GD\nImplement multiple linear regression using gradient descent."),
    ("code", "def multiple_regression_gd(X, Y, alpha, iters):\n    pass"),
    ("md", "## 3. Micro-Scaffolding: Interaction Terms\nWrite a function to expand your feature matrix `X` by generating interaction terms (e.g., multiplying feature 1 by feature 2)."),
    ("code", "def add_interaction_terms(X):\n    pass"),
    ("md", "## 4. Spaced Repetition: Multivariable Gradient Descent\nUse your `multivariable_gd` function from Notebook 11 to optimize the weights directly with the interaction terms included."),
    ("code", "def optimize_weights_gd(X, Y):\n    pass")
], "27-28_regression_gradient_descent.ipynb")

# Notebooks 40-42 (New split)
create_notebook("Notebook 40-42: Neuroevolution (Fogel's Tic-Tac-Toe & Blondie24)", [
    ("md", "## Concept Introduction\nReimplementing Fogel's Tic-Tac-Toe paper and standard Blondie24 using Multi-Layer Perceptrons. Focuses on co-evolution without an absolute fitness function."),
    ("md", "## 1. Micro-Scaffolding: Co-Evolutionary Fitness\nWrite a function where neural networks play games against each other to determine relative fitness, rather than using a static evaluation function."),
    ("code", "def evaluate_relative_fitness(population):\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Neural Network Board Evaluator\nModify your Neural Network from Notebook 35 to evaluate board states for Checkers or Tic-Tac-Toe."),
    ("code", "def evaluate_board_mlp(board_state, nn_weights):\n    pass"),
    ("md", "## 3. Interleaved Practice: Evolutionary Algorithm\nImplement the selection, crossover, and mutation steps to evolve neural network weights based on tournament survival."),
    ("code", "def evolve_population_tournament(population, fitness_scores):\n    pass"),
    ("md", "## 4. Spaced Repetition: Complete Blondie24 Loop\nCombine Neuroevolution with the Minimax game tree (Notebook 37) to train an AI to play Checkers."),
    ("code", "def train_blondie24_agent(generations):\n    pass")
], "40-42_neuroevolution.ipynb")

# Notebook 43 (New Convolutional)
create_notebook("Notebook 43: Convolutional Neuroevolution", [
    ("md", "## Concept Introduction\nImplementing Convolutional Neural Networks (CNNs) from scratch to evaluate spatial board states for Blondie24."),
    ("md", "## 1. Micro-Scaffolding: 2D Convolutional Filter\nWrite a function to apply a 2D filter (kernel) over a 2D matrix (board state) using a specified stride. No external libraries allowed."),
    ("code", "def apply_convolution_2d(matrix, kernel, stride=1):\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Pooling Layer\nWrite a function to apply max pooling to the output of your convolutional layer to reduce spatial dimensions."),
    ("code", "def max_pooling_2d(matrix, pool_size=2):\n    pass"),
    ("md", "## 3. Interleaved Practice: CNN Board Evaluator\nCombine your convolution, pooling, and MLP (Notebook 35) layers to evaluate a board state."),
    ("code", "def evaluate_board_cnn(board_state, conv_weights, mlp_weights):\n    pass"),
    ("md", "## 4. Spaced Repetition: Evolutionary CNN Training\nUse your evolutionary algorithm from Notebook 40-42 to evolve the weights of the convolutional filters and the dense layers."),
    ("code", "def train_convolutional_blondie24(generations):\n    pass")
], "43_convolutional_blondie24.ipynb")

print("Generated gap-filling notebooks.")
