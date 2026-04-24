import nbformat as nbf
import os

def insert_cells(filename, cells_to_insert):
    filepath = os.path.join('notebooks', filename)
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
    
    # Insert after the first cell (which is the Concept Introduction)
    new_cells = []
    for c_type, content in cells_to_insert:
        if c_type == "md":
            new_cells.append(nbf.v4.new_markdown_cell(content))
        elif c_type == "code":
            new_cells.append(nbf.v4.new_code_cell(content))
            
    nb.cells = nb.cells[:1] + new_cells + nb.cells[1:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Updated {filename}")

# 1. 07_brute_force_crypto.ipynb
cells_07 = [
    ("md", "## Phase 0: Math Foundation Practice - Algebraic Inverses\nBefore breaking the cipher, practice finding the algebraic inverse of the linear function `f(x) = ax + b` (From `justinmath-algebra.md` Section 1.1)."),
    ("code", "def algebraic_inverse(fx, a, b):\n    # Return x given f(x), a, and b\n    pass")
]
insert_cells("07_brute_force_crypto.ipynb", cells_07)

# 2. 09_estimating_roots.ipynb
cells_09 = [
    ("md", "## Phase 0: Math Foundation Practice - The Power Rule\nBefore estimating roots using numerical approximations, implement the exact symbolic derivative of a quadratic polynomial `f(x) = ax^2 + bx + c` using the Power Rule (From `justinmath-calculus.md` Section 1.4)."),
    ("code", "def power_rule_derivative(a, b, c, x):\n    # Return the exact derivative f'(x) at point x\n    pass")
]
insert_cells("09_estimating_roots.ipynb", cells_09)

# 3. 10_single_variable_gd.ipynb
cells_10 = [
    ("md", "## Phase 0: Math Foundation Practice - Exact Derivatives\nBefore using gradient descent, ensure you can calculate the exact derivative using the Power Rule for optimization steps instead of relying on numerical approximations."),
    ("code", "def exact_derivative_quadratic(a, b, c, x):\n    # Return f'(x) for f(x) = ax^2 + bx + c\n    pass")
]
insert_cells("10_single_variable_gd.ipynb", cells_10)

# 4. 11_multivariable_gd.ipynb
cells_11 = [
    ("md", "## Phase 0: Math Foundation Practice - Vectors and Dot Products\nMultivariable calculus relies heavily on vector operations (From `justinmath-linearAlgebra.md` Section 1.2). Implement a 1D dot product before working with gradients."),
    ("code", "def dot_product(vec1, vec2):\n    # Return the scalar dot product of two arrays\n    pass")
]
insert_cells("11_multivariable_gd.ipynb", cells_11)

# 5. 14_basic_matrix_arithmetic.ipynb
cells_14 = [
    ("md", "## Phase 0: Math Foundation Practice - Vectors and Dot Products\nMatrix multiplication is fundamentally built upon the vector dot product (From `justinmath-linearAlgebra.md` Section 1.2). Implement vector magnitude (norm) and dot product."),
    ("code", "import math\n\ndef vector_norm(vec):\n    pass\n\ndef dot_product(vec1, vec2):\n    pass")
]
insert_cells("14_basic_matrix_arithmetic.ipynb", cells_14)

# 6. 18_euler_estimation.ipynb
cells_18 = [
    ("md", "## Phase 0: Math Foundation Practice - Differential Equations\nBefore estimating over time, write a function to calculate the instantaneous rate of change `dy/dt` for a given state (From `justinmath-calculus.md` Section 3.2)."),
    ("code", "def instantaneous_rate_of_change(state, time, k=0.1):\n    # Example: dy/dt = -k * y\n    pass")
]
insert_cells("18_euler_estimation.ipynb", cells_18)

# 7. 35-36_neural_networks.ipynb
cells_35 = [
    ("md", "## Phase 0: Math Foundation Practice - The Chain Rule\nBackpropagation is entirely based on the Chain Rule (From `justinmath-calculus.md` Section 1.5). Compute the gradient of a simple composite function `f(g(x))` before building a full neural network layer."),
    ("code", "def chain_rule_gradient(df_dg, dg_dx):\n    # Multiply the local gradients to find the overall gradient\n    pass")
]
insert_cells("35-36_neural_networks.ipynb", cells_35)
