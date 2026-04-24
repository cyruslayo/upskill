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

# 1. 15_reduced_row_echelon_form.ipynb
cells_15 = [
    ("md", "## Phase 0: Math Foundation Practice - Elimination\nBefore writing an algorithm to compute RREF, practice manually coding a single variable elimination step between two linear equations (From `justinmath-linearAlgebra.md` Section 1.5)."),
    ("code", "def eliminate_variable(eq1, eq2, var_index):\n    # Return the resulting equation after eliminating the variable at var_index\n    pass")
]
insert_cells("15_reduced_row_echelon_form.ipynb", cells_15)

# 2. 22_simplex_method.ipynb
cells_22 = [
    ("md", "## Phase 0: Math Foundation Practice - Linear Inequalities\nThe Simplex Method is fundamentally built on satisfying systems of linear inequalities (From `justinmath-algebra.md` Section 3.4). Write a function to check if a given point satisfies a list of inequality constraints."),
    ("code", "def satisfies_inequalities(point, inequalities):\n    # Return True if the point satisfies all inequalities\n    pass")
]
insert_cells("22_simplex_method.ipynb", cells_22)

# 3. 34_decision_trees.ipynb
cells_34 = [
    ("md", "## Phase 0: Math Foundation Practice - Logarithms\nDecision Trees use Entropy to split data, which relies heavily on calculating logarithms of probabilities (From `justinmath-algebra.md` Section 6.2). Write a function to safely compute `p * log2(p)`."),
    ("code", "import math\n\ndef safe_p_log_p(p):\n    # Compute p * log2(p), handling the case where p=0\n    pass")
]
insert_cells("34_decision_trees.ipynb", cells_34)
