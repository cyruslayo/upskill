import nbformat as nbf
import os

def create_notebook(title, cells_content, filename):
    nb = nbf.v4.new_notebook()
    
    cells = []
    # Title
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

# Notebook 08
nb8_title = "Notebook 08: Solving Magic Squares via Backtracking"
nb8_cells = [
    ("md", "## Concept Introduction\nSolving Magic Squares using a Backtracking algorithm to optimize the brute force approach."),
    ("md", "## 1. Micro-Scaffolding: Validating a Square\nWrite a function to check if a partially filled square is valid so far."),
    ("code", "def is_valid(square):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: Backtracking\nWrite `solve_magic_square(square)` using backtracking instead of generating all possibilities (like brute force)."),
    ("code", "def solve_magic_square(square):\n    # Write your backtracking algorithm here\n    pass"),
    ("md", "## 3. Spaced Repetition: Roulette Wheel Search\nInstead of checking possibilities in a fixed order, use Roulette Wheel Selection (from Notebook 05) to pick the next number to try randomly but weighted towards smaller numbers."),
    ("code", "def solve_magic_square_stochastic(square):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb8_title, nb8_cells, "08_backtracking_magic_squares.ipynb")

# Notebook 09
nb9_title = "Notebook 09: Estimating Roots via Bisection and Newton-Raphson"
nb9_cells = [
    ("md", "## Concept Introduction\nUsing numerical methods to estimate roots of functions.\n\n## Targeted Math Foundations\nFrom `justinmath-calculus.md` Section 1.3 (Derivatives and the Difference Quotient):\nThe derivative is the function's slope. Newton-Raphson uses the derivative `f'(x)` to find where `f(x) = 0`."),
    ("md", "## 1. Micro-Scaffolding: Bisection Search\nWrite `bisection_search(f, low, high, tolerance)` to find the root by repeatedly halving the interval."),
    ("code", "def bisection_search(f, low, high, tolerance):\n    # Write your code here\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Difference Quotient\nWrite a function `derivative(f, x, dx)` that approximates the derivative using the difference quotient."),
    ("code", "def derivative(f, x, dx=1e-5):\n    # Write your code here\n    pass"),
    ("md", "## 3. Interleaved Practice: Newton-Raphson Method\nWrite `newton_raphson(f, initial_guess, tolerance)` to find the root using the derivative."),
    ("code", "def newton_raphson(f, initial_guess, tolerance):\n    # Write your code here\n    pass"),
    ("md", "## 4. Spaced Repetition: Recursive Newton-Raphson\nWrite a recursive version of `newton_raphson` (like your recursive Fibonacci from Notebook 03)."),
    ("code", "def newton_raphson_recursive(f, current_guess, tolerance):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb9_title, nb9_cells, "09_estimating_roots.ipynb")

# Notebook 10
nb10_title = "Notebook 10: Single-Variable Gradient Descent"
nb10_cells = [
    ("md", "## Concept Introduction\nUsing the derivative to find the local minimum of a function.\n\n## Targeted Math Foundations\nFrom `justinmath-calculus.md` Section 1.8 (Finding Local Extrema):\nThe minimum of a function occurs where the derivative is 0. Gradient descent iteratively moves in the direction opposite to the derivative."),
    ("md", "## 1. Micro-Scaffolding: Gradient Descent Step\nWrite a function that takes a current `x`, computes the derivative, and updates `x` by moving `-alpha * derivative`."),
    ("code", "def gradient_descent_step(f, x, alpha):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: Gradient Descent Loop\nWrite `gradient_descent(f, initial_x, alpha, tolerance, max_iters)` to repeatedly step until convergence."),
    ("code", "def gradient_descent(f, initial_x, alpha, tolerance, max_iters):\n    # Write your code here\n    pass"),
    ("md", "## 3. Spaced Repetition: Bisection for Extrema\nCan you find the local minimum of a convex function by finding the root of its derivative using `bisection_search` from Notebook 09?"),
    ("code", "def minimize_via_bisection(f, low, high, tolerance):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb10_title, nb10_cells, "10_single_variable_gd.ipynb")

# Notebook 11
nb11_title = "Notebook 11: Multivariable Gradient Descent"
nb11_cells = [
    ("md", "## Concept Introduction\nExtending gradient descent to multiple variables.\n\n## Targeted Math Foundations\nFrom `justinmath-linearAlgebra.md` Section 1.1 (N-Dimensional Space):\nVectors can be added component-wise. Scalars multiply into vectors. Multivariable Gradient Descent relies on the gradient, a vector of partial derivatives."),
    ("md", "## 1. Micro-Scaffolding: Partial Derivatives\nWrite `partial_derivative(f, point, i, dx)` that computes the difference quotient with respect to the `i`th dimension."),
    ("code", "def partial_derivative(f, point, i, dx=1e-5):\n    # Write your code here\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Gradient Vector\nWrite `gradient(f, point, dx)` that returns an array (vector) of partial derivatives."),
    ("code", "def gradient(f, point, dx=1e-5):\n    # Write your code here\n    pass"),
    ("md", "## 3. Interleaved Practice: Multivariable Gradient Descent\nWrite `multivariable_gd(f, initial_point, alpha, tolerance, max_iters)`."),
    ("code", "def multivariable_gd(f, initial_point, alpha, tolerance, max_iters):\n    # Write your code here\n    pass"),
    ("md", "## 4. Spaced Repetition: Multivariable Cartesian Grid Search\nUse `calc_cartesian_product` to generate a grid of initial points, and run Multivariable GD from each point to find the global minimum."),
    ("code", "def global_minimum_search(f, search_ranges):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb11_title, nb11_cells, "11_multivariable_gd.ipynb")

# Notebook 12
nb12_title = "Notebook 12: Selection, Bubble, Insertion, and Counting Sort"
nb12_cells = [
    ("md", "## Concept Introduction\nImplementing and comparing O(n^2) basic sorting algorithms and O(n) counting sort."),
    ("md", "## 1. Micro-Scaffolding: Selection Sort\nWrite `selection_sort(arr)` finding the minimum in the remaining array and swapping."),
    ("code", "def selection_sort(arr):\n    # Write your code here\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Bubble Sort\nWrite `bubble_sort(arr)` iterating and swapping adjacent elements."),
    ("code", "def bubble_sort(arr):\n    # Write your code here\n    pass"),
    ("md", "## 3. Micro-Scaffolding: Insertion Sort\nWrite `insertion_sort(arr)` picking the next element and inserting it into the sorted portion."),
    ("code", "def insertion_sort(arr):\n    # Write your code here\n    pass"),
    ("md", "## 4. Micro-Scaffolding: Counting Sort\nWrite `counting_sort(arr, max_val)` for arrays of positive integers up to `max_val`."),
    ("code", "def counting_sort(arr, max_val):\n    # Write your code here\n    pass"),
    ("md", "## 5. Spaced Repetition: Sorting Simulated Data\nUse your Monte Carlo simulation (Notebook 04) to generate 1000 random integers and sort them using Counting Sort."),
    ("code", "def sort_simulated_data():\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb12_title, nb12_cells, "12_basic_sorting.ipynb")

# Notebook 13
nb13_title = "Notebook 13: Merge Sort and Quicksort"
nb13_cells = [
    ("md", "## Concept Introduction\nImplementing faster O(n log n) sorting algorithms: Merge Sort and Quicksort."),
    ("md", "## 1. Micro-Scaffolding: Merge Helper\nWrite a function `merge(left, right)` that merges two sorted arrays into one sorted array."),
    ("code", "def merge(left, right):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: Merge Sort\nWrite `merge_sort(arr)` using recursion and the `merge` helper. Compare recursion here to Notebook 03."),
    ("code", "def merge_sort(arr):\n    # Write your code here\n    pass"),
    ("md", "## 3. Micro-Scaffolding: Partition Helper\nWrite `partition(arr, low, high)` for Quicksort."),
    ("code", "def partition(arr, low, high):\n    # Write your code here\n    pass"),
    ("md", "## 4. Interleaved Practice: Quicksort\nWrite `quicksort(arr, low, high)` recursively."),
    ("code", "def quicksort(arr, low=0, high=None):\n    # Write your code here\n    pass"),
    ("md", "## 5. Spaced Repetition: Searching a Sorted Array\nOnce sorted, use a variant of Bisection Search (Notebook 09) called Binary Search to find an element in the sorted array."),
    ("code", "def binary_search(sorted_arr, target):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb13_title, nb13_cells, "13_advanced_sorting.ipynb")

print("Generated notebooks 8-13")
