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

# Math Notebook 01
create_notebook("Math 01: Algebra - Linear Equations", [
    ("md", "## Concept Introduction\nFrom *Algebra* Section 1.1: Solving Linear Equations.\nA linear equation is an equality containing only addition, subtraction, multiplication, and division. The goal is to isolate the variable.\n\nExample: `2x + 3 = 7` \n1. Subtract 3 from both sides: `2x = 4`\n2. Divide by 2: `x = 2`"),
    ("md", "## 1. Micro-Scaffolding: Algebraic Inverse\nWrite a function to computationally solve `ax + b = c` for `x`. This is the foundation of cryptography breaking in the AI track."),
    ("code", "def solve_linear(a, b, c):\n    # Return x such that ax + b = c\n    pass"),
    ("md", "## 2. Interleaved Practice: Multi-Step Algebra\nSolve `a(x + b) + c = d` for `x`."),
    ("code", "def solve_complex_linear(a, b, c, d):\n    # Return x\n    pass"),
    ("md", "## 3. Spaced Repetition: Verify via Code\nWrite a loop to test your function by plugging `x` back into `ax + b` and checking if it equals `c`."),
    ("code", "def verify_solution(a, b, c, x):\n    # Return True if correct\n    pass")
], "math_01_algebra_linear_equations.ipynb")

# Math Notebook 02
create_notebook("Math 02: Calculus - Derivatives & Power Rule", [
    ("md", "## Concept Introduction\nFrom *Calculus* Sections 1.3 & 1.4.\nThe derivative represents the instantaneous slope of a function. \nThe **Difference Quotient** approximates it: `f'(x) ≈ (f(x + dx) - f(x)) / dx`.\nThe **Power Rule** provides an exact symbolic formula: if `f(x) = cx^n`, then `f'(x) = c * n * x^(n-1)`."),
    ("md", "## 1. Micro-Scaffolding: Difference Quotient\nWrite a function that estimates the derivative of any function `f` at point `x`."),
    ("code", "def difference_quotient(f, x, dx=1e-5):\n    pass"),
    ("md", "## 2. Interleaved Practice: Power Rule in Code\nWrite a function to return the exact derivative of a polynomial `ax^2 + bx + c` at point `x` without using `dx`."),
    ("code", "def exact_derivative(a, b, c, x):\n    pass"),
    ("md", "## Phase: Visualization & Intuition (matplotlib)\nPlot a parabola and its tangent line to visualize the slope!"),
    ("code", "import matplotlib.pyplot as plt\nimport numpy as np\n# Plot f(x) = x^2 and its tangent line at x=1")
], "math_02_calculus_derivatives.ipynb")

# Math Notebook 03
create_notebook("Math 03: Calculus - Chain Rule", [
    ("md", "## Concept Introduction\nFrom *Calculus* Section 1.5: The Chain Rule.\nThe chain rule allows us to take derivatives of composite functions: `f(g(x))`.\n`d/dx [f(g(x))] = f'(g(x)) * g'(x)`.\nThis is the absolute core of Backpropagation in neural networks!"),
    ("md", "## 1. Micro-Scaffolding: Inner and Outer Gradients\nAssume `g(x) = 2x` and `f(g) = g^2`. Write a function to compute both `g'(x)` and `f'(g)`."),
    ("code", "def inner_g_prime(x):\n    pass\n\ndef outer_f_prime(g):\n    pass"),
    ("md", "## 2. Interleaved Practice: Chain Rule\nCombine them to find the total derivative."),
    ("code", "def chain_rule(x):\n    # Calculate g(x), then use the primes\n    pass")
], "math_03_calculus_chain_rule.ipynb")

# Math Notebook 04
create_notebook("Math 04: Calculus - Local Extrema", [
    ("md", "## Concept Introduction\nFrom *Calculus* Section 1.8.\nLocal extrema (minimums or maximums) occur where the derivative is exactly 0. This concept powers Gradient Descent!"),
    ("md", "## 1. Micro-Scaffolding: Finding the Minima\nWrite a function to algebraically find the minimum of `f(x) = ax^2 + bx + c` by setting its derivative to 0."),
    ("code", "def find_minimum_vertex(a, b, c):\n    # Return the x value where the derivative is 0\n    pass"),
    ("md", "## 2. Spaced Repetition: Verify via Bisection\nUse a bisection search over the exact derivative function to numerically find the root of the derivative, comparing it to your algebraic answer."),
    ("code", "def bisection_root_finding(f_prime, low, high):\n    pass")
], "math_04_calculus_local_extrema.ipynb")

# Math Notebook 05
create_notebook("Math 05: Linear Algebra - Vectors and Dot Products", [
    ("md", "## Concept Introduction\nFrom *Linear Algebra* Sections 1.1 & 1.2.\nVectors are arrays of numbers representing displacement in N-dimensional space. The **Dot Product** is the sum of the products of their corresponding components. It tells us about the angle and projection between vectors."),
    ("md", "## 1. Micro-Scaffolding: Vector Addition & Norm\nWrite functions to add vectors and calculate their magnitude (norm)."),
    ("code", "import math\ndef vector_add(v1, v2):\n    pass\n\ndef vector_norm(v):\n    pass"),
    ("md", "## 2. Interleaved Practice: Dot Product\nWrite a function to calculate the dot product of two vectors of any length."),
    ("code", "def dot_product(v1, v2):\n    pass"),
    ("md", "## 3. Spaced Repetition: Angle Between Vectors\nUse the dot product formula `A dot B = |A| |B| cos(theta)` to find the angle in radians."),
    ("code", "def vector_angle(v1, v2):\n    pass")
], "math_05_linear_algebra_vectors.ipynb")

# Math Notebook 06
create_notebook("Math 06: Linear Algebra - Matrices and Transformations", [
    ("md", "## Concept Introduction\nFrom *Linear Algebra* Sections 3.1 & 3.2.\nMatrices are 2D arrays that act as linear transformations on vectors. Matrix multiplication is an application of many dot products."),
    ("md", "## 1. Micro-Scaffolding: Matrix-Vector Multiplication\nWrite a function to multiply a matrix by a column vector using your dot product function."),
    ("code", "def matrix_vector_mult(M, v):\n    pass"),
    ("md", "## 2. Interleaved Practice: Matrix-Matrix Multiplication\nExtend this to multiply two matrices together."),
    ("code", "def matrix_mult(A, B):\n    pass"),
    ("md", "## Phase: Visualization & Intuition (matplotlib)\nVisualize how a 2x2 matrix transforms a grid of 2D points (scaling and shearing)."),
    ("code", "import matplotlib.pyplot as plt\n# Code to visualize transformation")
], "math_06_linear_algebra_matrices.ipynb")

# Math Notebook 07
create_notebook("Math 07: Calculus - Differential Equations (Euler)", [
    ("md", "## Concept Introduction\nFrom *Calculus* Section 3.2.\nA differential equation relates a state to its rate of change (`dy/dt`). We can estimate the state over time using **Euler's Method**: `y_next = y_current + dy/dt * dt`."),
    ("md", "## 1. Micro-Scaffolding: Rate of Change\nSuppose population growth is `dP/dt = 0.05 * P`. Write the differential equation function."),
    ("code", "def dP_dt(P):\n    return 0.05 * P"),
    ("md", "## 2. Interleaved Practice: Euler Loop\nWrite a loop to estimate the population after 10 years, taking steps of `dt`."),
    ("code", "def euler_population(P0, dt, total_time):\n    pass"),
    ("md", "## Phase: Visualization & Intuition (matplotlib)\nPlot the population curve over time."),
    ("code", "import matplotlib.pyplot as plt\n# Plot the trajectory")
], "math_07_calculus_differential_equations.ipynb")

print("Generated Math Foundations Track notebooks!")
