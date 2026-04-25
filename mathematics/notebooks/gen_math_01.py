import json, uuid, os

def cell(t, src):
    c = {"cell_type":t,"id":uuid.uuid4().hex[:8],"metadata":{},"source":src.rstrip("\n").split("\n")}
    if t=="code": c["execution_count"]=None; c["outputs"]=[]
    return c

def save(cells, path):
    nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.10.0"}},"nbformat":4,"nbformat_minor":5}
    with open(path,"w",encoding="utf-8") as f: json.dump(nb,f,indent=1,ensure_ascii=False)
    print(f"  OK {path} ({os.path.getsize(path)//1024}KB)")

OUT = os.path.dirname(os.path.abspath(__file__))

COLAB = cell("code","# Google Colab Setup\n!pip install -q sympy matplotlib plotly ipywidgets\nimport sympy as sp; sp.init_printing()\nimport numpy as np, matplotlib.pyplot as plt\nprint('Ready ✅')")

# ═══════════════════════════════════════════════════════════════
# MATH 01 — Algebra: Linear Equations
# Source: justinmath-algebra.md §1.1–1.5
# ═══════════════════════════════════════════════════════════════
def math_01():
    return [
        cell("markdown",
"# Math 01: Algebra — Linear Equations\n"
"\n"
"**Learning Objectives** — By the end of this notebook you will be able to:\n"
"1. Define what a linear equation is and identify its components\n"
"2. Solve single-variable linear equations using inverse operations\n"
"3. Recognise the three solution cases (unique, none, infinitely many)\n"
"4. Translate algebraic solutions into Python code from scratch\n"
"5. Verify solutions computationally and handle pathological edge cases\n"
"\n"
"**Prerequisites:** Basic Python (variables, functions, if/else)  \n"
"**Estimated time:** 90 minutes  \n"
"**Textbook reference:** *Justin Skycak — Algebra*, Part 1 §1.1–1.5"),

        COLAB,

        cell("markdown",
"---\n"
"## Table of Contents\n"
"1. [Phase −1: Theoretical Foundation](#phase-1)  \n"
"2. [Phase 0: Math Foundation Practice](#phase-0)  \n"
"3. [Phase 1: Algorithm Construction](#phase-1-algo)  \n"
"4. [Phase 2: Experimental Verification](#phase-2)  \n"
"5. [Phase 3: Olympiad Extension](#phase-3)"),

        # ── PHASE −1 ──────────────────────────────────────────
        cell("markdown",
"---\n"
"<a id='phase-1'></a>\n"
"## Phase −1 — Theoretical Foundation (Kiselev / Gelfand Rigor)\n"
"\n"
"### What is a linear equation?\n"
"\n"
"A **linear equation** is an equality containing only addition, subtraction,\n"
"multiplication and division — no exponents, roots, or transcendentals.\n"
"\n"
"$$ax + b = c \\qquad (a,\\,b,\\,c \\in \\mathbb{R},\\; a \\neq 0)$$\n"
"\n"
"**Axiom (Additive & Multiplicative Inverse):** For every real number $r$,\n"
"there exists $-r$ such that $r + (-r) = 0$, and for $r\\neq 0$ there exists\n"
"$r^{-1}$ such that $r \\cdot r^{-1} = 1$.\n"
"\n"
"These two axioms are the *entire engine* behind solving any linear equation:\n"
"we apply inverse operations to both sides until the variable is isolated."),

        cell("markdown",
"### Guided Proof — Uniqueness of the Solution\n"
"\n"
"**Theorem.** If $a \\neq 0$, the equation $ax + b = c$ has exactly one solution $x = \\frac{c-b}{a}$.\n"
"\n"
"*Proof.*\n"
"1. Subtract $b$ from both sides (additive inverse): $ax = c - b$\n"
"2. Divide both sides by $a$ (multiplicative inverse, valid since $a\\neq 0$): $x = \\frac{c-b}{a}$\n"
"3. Uniqueness: suppose $x_1,x_2$ both satisfy the equation.  \n"
"   Then $ax_1 + b = c = ax_2 + b \\Rightarrow ax_1 = ax_2 \\Rightarrow x_1 = x_2$. $\\square$"),

        cell("code",
"# Verify the proof symbolically with SymPy\n"
"import sympy as sp\n"
"\n"
"x, a, b, c = sp.symbols('x a b c')\n"
"equation = sp.Eq(a*x + b, c)\n"
"solution = sp.solve(equation, x)\n"
"print('Symbolic solution:', solution)  # [(c - b)/a]\n"
"\n"
"# Verify: substitute back\n"
"check = (a * solution[0] + b).simplify()\n"
"print('Substitution gives:', check, '== c ?', sp.simplify(check - c) == 0)"),

        cell("markdown",
"### The Three Cases\n"
"\n"
"| Case | Condition | What happens algebraically | Example |\n"
"|---|---|---|---|\n"
"| **Unique solution** | $a \\neq 0$ | Variable isolates to one value | $2x+3=7 \\Rightarrow x=2$ |\n"
"| **No solution** | $a=0,\\; b \\neq c$ | Variable vanishes, leaving a false statement | $0x+3=7 \\Rightarrow 3=7$ ✗ |\n"
"| **Infinitely many** | $a=0,\\; b=c$ | Variable vanishes, leaving a true statement | $0x+5=5 \\Rightarrow 5=5$ ✓ |\n"
"\n"
"> 📖 *From Algebra §1.1:* 'Most linear equations have a single solution. We find it by\n"
"> performing operations on both sides to isolate the variable.'"),

        cell("markdown",
"### Comprehension Check ✅\n"
"Before continuing, answer in your head:\n"
"1. Why do we need $a \\neq 0$ for a unique solution?\n"
"2. Give an example of a linear equation with no solution.\n"
"3. What does \"infinitely many solutions\" look like geometrically on a number line?\n"
"\n"
"<details><summary>💡 Hints</summary>\n"
"\n"
"1. If $a=0$, dividing by $a$ is undefined — we lose the variable entirely.  \n"
"2. $5x + 3 = 5x + 7$ → subtract $5x$: $3 = 7$ (false).  \n"
"3. Every real number satisfies the equation — the \"solution set\" is the whole number line.\n"
"</details>"),

        # ── PHASE 0 ──────────────────────────────────────────
        cell("markdown",
"---\n"
"<a id='phase-0'></a>\n"
"## Phase 0 — Math Foundation Practice\n"
"\n"
"### Worked Example: Solving a Multi-Step Equation\n"
"\n"
"Solve $3(x + 2) - 4 = 11$ step by step.\n"
"\n"
"| Step | Operation | Result |\n"
"|------|-----------|--------|\n"
"| Start | — | $3(x+2) - 4 = 11$ |\n"
"| Distribute | $3 \\cdot x + 3 \\cdot 2$ | $3x + 6 - 4 = 11$ |\n"
"| Simplify | $6 - 4 = 2$ | $3x + 2 = 11$ |\n"
"| Subtract 2 | additive inverse | $3x = 9$ |\n"
"| Divide by 3 | multiplicative inverse | $x = 3$ |\n"
"\n"
"**Verification:** $3(3+2)-4 = 3(5)-4 = 15-4 = 11$ ✓"),

        cell("code",
"# Worked example — run this cell to see the step-by-step solution\n"
"a_val, b_val, c_val = 3, 2, 11  # 3(x+2) - 4 = 11 → 3x + 6 - 4 = 11 → 3x + 2 = 11\n"
"# Rearranged: a_eff*x + b_eff = c  where a_eff=3, b_eff=2, c=11\n"
"x_solution = (c_val - b_val) / a_val\n"
"print(f'Solution: x = ({c_val} - {b_val}) / {a_val} = {x_solution}')\n"
"print(f'Check: 3*({x_solution}+2) - 4 = {3*(x_solution+2)-4}')"),

        cell("markdown",
"### 🎯 Your Turn — Solve by Hand, then Verify in Code\n"
"\n"
"Solve each equation on paper first, then fill in the function below to check computationally.\n"
"\n"
"1. $5x - 7 = 18$\n"
"2. $-2x + 10 = 4$\n"
"3. $4(x - 3) + 2 = 14$"),

        cell("code",
"def solve_linear(a, b, c):\n"
"    \"\"\"Solve ax + b = c for x. Return the solution or raise if a == 0.\"\"\"\n"
"    # YOUR CODE HERE\n"
"    pass\n"
"\n"
"# Tests — uncomment after implementing:\n"
"# assert solve_linear(5, -7, 18) == 5.0,  'Problem 1 failed'\n"
"# assert solve_linear(-2, 10, 4) == 3.0,  'Problem 2 failed'\n"
"# assert solve_linear(4, -10, 14) == 6.0, 'Problem 3 (after expanding) failed'\n"
"# print('All Phase 0 tests passed ✅')"),

        cell("markdown",
"<details><summary>💡 Hint</summary>\n"
"\n"
"The formula is $x = \\frac{c - b}{a}$. But what should you do when $a = 0$?\n"
"Consider raising a `ValueError`.\n"
"</details>"),

        cell("markdown",
"### Common Mistakes ⚠️\n"
"1. **Forgetting to distribute** — $3(x+2) \\neq 3x + 2$, it's $3x + 6$\n"
"2. **Sign errors with negatives** — when subtracting a negative: $x - (-3) = x + 3$\n"
"3. **Dividing before subtracting** — always undo addition/subtraction first, *then* multiplication\n"
"4. **Ignoring the $a=0$ case** — your code should handle this gracefully"),

        # ── PHASE 1 ──────────────────────────────────────────
        cell("markdown",
"---\n"
"<a id='phase-1-algo'></a>\n"
"## Phase 1 — Micro-Scaffolded Algorithm Construction\n"
"\n"
"Now we build a **complete linear equation solver** from scratch — no libraries.\n"
"This solver is the foundation for cryptography breaking in Notebook 07.\n"
"\n"
"### Step 1: Basic Solver\n"
"Write `solve_linear(a, b, c)` that handles all three cases."),

        cell("code",
"def solve_linear(a, b, c):\n"
"    \"\"\"\n"
"    Solve ax + b = c for x.\n"
"    \n"
"    Returns:\n"
"        float: the unique solution if a != 0\n"
"    Raises:\n"
"        ValueError: if a == 0 (no solution or infinitely many)\n"
"    \"\"\"\n"
"    # YOUR CODE HERE\n"
"    pass"),

        cell("code",
"# ── Step 1 Verification ──\n"
"# Uncomment after implementing:\n"
"# assert solve_linear(2, 3, 7) == 2.0\n"
"# assert solve_linear(1, 0, 5) == 5.0\n"
"# assert solve_linear(-3, 9, 0) == 3.0\n"
"# try:\n"
"#     solve_linear(0, 3, 7)\n"
"#     assert False, 'Should have raised ValueError'\n"
"# except ValueError:\n"
"#     pass\n"
"# print('Step 1 passed ✅')"),

        cell("markdown",
"### Step 2: Multi-Step Solver\n"
"Solve $a(x + b) + c = d$ for $x$.\n"
"\n"
"*Strategy:* Expand → rearrange into standard $Ax + B = C$ form → call `solve_linear`."),

        cell("code",
"def solve_complex_linear(a, b, c, d):\n"
"    \"\"\"\n"
"    Solve a(x + b) + c = d for x.\n"
"    Expand: ax + ab + c = d  →  ax + (ab+c) = d\n"
"    \"\"\"\n"
"    # YOUR CODE HERE — hint: reuse solve_linear!\n"
"    pass"),

        cell("code",
"# ── Step 2 Verification ──\n"
"# assert solve_complex_linear(3, 2, -4, 11) == 3.0\n"
"# assert solve_complex_linear(2, -1, 5, 9) == 3.0\n"
"# print('Step 2 passed ✅')"),

        cell("markdown",
"### Step 3: Batch Verifier (Interleaved Practice)\n"
"\n"
"Write a function that takes a list of $(a,b,c)$ triples,\n"
"solves each one, plugs the answer back in, and reports whether each is correct.\n"
"\n"
"*This revisits loops and list-building from Notebook 01.*"),

        cell("code",
"def verify_batch(problems):\n"
"    \"\"\"\n"
"    problems: list of (a, b, c) tuples for ax + b = c\n"
"    Returns: list of (x, is_correct) tuples\n"
"    \"\"\"\n"
"    results = []\n"
"    for a, b, c in problems:\n"
"        # YOUR CODE HERE\n"
"        pass\n"
"    return results\n"
"\n"
"# Test:\n"
"# problems = [(2,3,7), (5,-7,18), (-2,10,4), (1,0,0)]\n"
"# for (x, ok) in verify_batch(problems):\n"
"#     print(f'x={x:.2f}  correct={ok}')"),

        cell("markdown",
"### Step 4: Spaced Repetition — Slope-Intercept Connection\n"
"\n"
"> 📖 *From Algebra §1.2:* A two-variable linear equation $y = mx + b$ graphs as a straight line.\n"
"> The slope $m$ tells how steep it is; the y-intercept $b$ is where it crosses the y-axis.\n"
"\n"
"The solution to $ax + b = c$ is geometrically the **x-coordinate where the line $y = ax + b$\n"
"crosses the horizontal line $y = c$**.\n"
"\n"
"Write a function that plots this geometric interpretation."),

        cell("code",
"def plot_linear_solution(a, b, c):\n"
"    \"\"\"Plot y = ax + b and y = c, marking their intersection.\"\"\"\n"
"    import matplotlib.pyplot as plt\n"
"    import numpy as np\n"
"    \n"
"    x_sol = (c - b) / a\n"
"    x_range = np.linspace(x_sol - 5, x_sol + 5, 200)\n"
"    \n"
"    fig, ax_plot = plt.subplots(figsize=(8, 5))\n"
"    ax_plot.plot(x_range, a * x_range + b, 'b-', linewidth=2, label=f'y = {a}x + {b}')\n"
"    ax_plot.axhline(y=c, color='r', linestyle='--', linewidth=1.5, label=f'y = {c}')\n"
"    ax_plot.plot(x_sol, c, 'ko', markersize=10, zorder=5)\n"
"    ax_plot.annotate(f'  x = {x_sol:.2f}', (x_sol, c), fontsize=12, fontweight='bold')\n"
"    ax_plot.set_xlabel('x'); ax_plot.set_ylabel('y')\n"
"    ax_plot.set_title(f'Geometric Solution of {a}x + {b} = {c}')\n"
"    ax_plot.legend(); ax_plot.grid(True, alpha=0.3)\n"
"    plt.tight_layout(); plt.show()\n"
"\n"
"# Run it:\n"
"plot_linear_solution(2, 3, 7)"),

        # ── PHASE 2 ──────────────────────────────────────────
        cell("markdown",
"---\n"
"<a id='phase-2'></a>\n"
"## Phase 2 — Experimental Verification & Visualization\n"
"\n"
"### What We're Testing\n"
"Our `solve_linear` function uses exact arithmetic: $x = (c-b)/a$.\n"
"But floating-point numbers on a computer are *approximations*.\n"
"Can we find inputs where floating-point arithmetic gives the **wrong** answer?"),

        cell("code",
"# ── Experiment 1: Floating-point precision limits ──\n"
"# Try very large and very small coefficients\n"
"import numpy as np\n"
"\n"
"test_cases = [\n"
"    (1e15, 1e15, 2e15,   'large coefficients'),\n"
"    (1e-15, 1e-15, 2e-15, 'tiny coefficients'),\n"
"    (1e15, -1e15, 1,      'catastrophic cancellation'),\n"
"    (1e-300, 0, 1e-300,   'near underflow'),\n"
"]\n"
"\n"
"for a, b, c, label in test_cases:\n"
"    x = (c - b) / a\n"
"    residual = abs(a * x + b - c)\n"
"    print(f'{label:30s}  x={x:20.6e}  residual={residual:.2e}')"),

        cell("code",
"# ── Experiment 2: The Pathological Case ──\n"
"# When (c - b) suffers catastrophic cancellation\n"
"a = 1.0\n"
"b = 1e16\n"
"c = 1e16 + 1  # True answer: x = 1\n"
"\n"
"x_computed = (c - b) / a\n"
"print(f'Expected: x = 1.0')\n"
"print(f'Computed: x = {x_computed}')\n"
"print(f'Error:    {abs(x_computed - 1.0)}')\n"
"print()\n"
"print('⚠️  When b and c are very close in magnitude but huge,')\n"
"print('    (c - b) loses precision due to catastrophic cancellation.')"),

        cell("code",
"# ── Visualization: Error growth ──\n"
"import matplotlib.pyplot as plt\n"
"import numpy as np\n"
"\n"
"scales = np.logspace(0, 16, 100)\n"
"errors = []\n"
"for s in scales:\n"
"    b_val = s\n"
"    c_val = s + 1.0  # true x = 1.0\n"
"    x_comp = (c_val - b_val) / 1.0\n"
"    errors.append(abs(x_comp - 1.0))\n"
"\n"
"plt.figure(figsize=(9, 5))\n"
"plt.loglog(scales, errors, 'r-', linewidth=2)\n"
"plt.xlabel('Scale of b and c', fontsize=12)\n"
"plt.ylabel('Absolute Error in x', fontsize=12)\n"
"plt.title('Catastrophic Cancellation in Linear Equation Solving', fontsize=13)\n"
"plt.grid(True, alpha=0.3)\n"
"plt.tight_layout()\n"
"plt.show()"),

        cell("markdown",
"### 🔍 Reflection\n"
"1. At what scale does the error become non-negligible?\n"
"2. Why does `(c - b)` lose precision when both are ≈ $10^{16}$?\n"
"3. Could using `decimal.Decimal` or `fractions.Fraction` help?\n"
"\n"
"<details><summary>💡 Answer</summary>\n"
"\n"
"IEEE 754 `float64` has ~15–17 significant digits. When $b \\approx c \\approx 10^{16}$,\n"
"the difference $c - b = 1$ occupies the 17th digit — beyond precision.\n"
"Using `Fraction` or `Decimal` with sufficient precision eliminates this.\n"
"</details>"),

        # ── PHASE 3 ──────────────────────────────────────────
        cell("markdown",
"---\n"
"<a id='phase-3'></a>\n"
"## Phase 3 — Olympiad Extension & Chalkboard Defense\n"
"\n"
"### Olympiad Challenge: Exact-Arithmetic Solver\n"
"\n"
"Build a version of `solve_linear` that uses Python's `fractions.Fraction`\n"
"to return **exact** rational answers, immune to floating-point errors.\n"
"\n"
"Then solve this system that would break a float-based solver:\n"
"\n"
"$$\\frac{1}{3}x + \\frac{1}{7} = \\frac{10}{21}$$\n"
"\n"
"The exact answer is $x = 1$. Does your float solver agree?"),

        cell("code",
"# ── Olympiad Extension: Exact Solver ──\n"
"# Build this WITHOUT any scaffolding.\n"
"from fractions import Fraction\n"
"\n"
"def solve_linear_exact(a, b, c):\n"
"    \"\"\"Solve ax + b = c using exact rational arithmetic.\"\"\"\n"
"    # YOUR CODE HERE\n"
"    pass\n"
"\n"
"# Test: solve (1/3)x + 1/7 = 10/21\n"
"# x = solve_linear_exact(Fraction(1,3), Fraction(1,7), Fraction(10,21))\n"
"# print(f'Exact: x = {x}')\n"
"# print(f'Float: x = {(10/21 - 1/7) / (1/3)}')  # may not be exactly 1.0"),

        cell("markdown",
"### Chalkboard Defense\n"
"\n"
"Write a formal defense addressing:\n"
"\n"
"1. **Correctness:** Prove that `solve_linear(a,b,c)` returns the unique root of $ax+b=c$ for all $a\\neq 0$.\n"
"2. **Time Complexity:** What is the Big-O of your solver? (Hint: it's $O(1)$ — why?)\n"
"3. **Numerical Stability:** Under what conditions does the floating-point solver fail,\n"
"   and how does the `Fraction`-based solver fix this?\n"
"\n"
"*Write your defense below using LaTeX:*"),

        cell("markdown",
"**Defense:**\n"
"\n"
"*(Your formal mathematical defense here)*\n"
"\n"
"<details><summary>💡 Example defense structure</summary>\n"
"\n"
"**Claim 1 (Correctness).** For $a \\neq 0$, `solve_linear(a,b,c)` returns $x^* = (c-b)/a$.\n"
"Substituting: $a \\cdot \\frac{c-b}{a} + b = (c-b) + b = c$. ✓\n"
"\n"
"**Claim 2 (Complexity).** The function performs 1 subtraction and 1 division: $O(1)$ time.\n"
"\n"
"**Claim 3 (Stability).** When $|b| \\approx |c| \\gg 1$, the subtraction $c - b$ suffers\n"
"catastrophic cancellation. The `Fraction` solver avoids this because it performs\n"
"exact integer arithmetic on numerators and denominators.\n"
"</details>"),

        cell("markdown",
"---\n"
"### 📚 Further Reading\n"
"- *Algebra* §1.2–1.5: Slope-intercept form, point-slope form, linear systems\n"
"- *The Math Academy Way* Ch. 14: Minimizing Cognitive Load & Micro-Scaffolding\n"
"- **Next notebook:** Math 02 (Calculus — Derivatives) builds on algebraic manipulation"),
    ]

# ═══════════════════════════════════════════════════════════════
# Generate
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    save(math_01(), os.path.join(OUT, "math_01_algebra_linear_equations.ipynb"))
    print("Done.")
