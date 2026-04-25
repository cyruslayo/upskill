import json, uuid, os
def cell(t,s):
    c={"cell_type":t,"id":uuid.uuid4().hex[:8],"metadata":{},"source":s.rstrip("\n").split("\n")}
    if t=="code":c["execution_count"]=None;c["outputs"]=[]
    return c
def save(cells,path):
    nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.10.0"}},"nbformat":4,"nbformat_minor":5}
    with open(path,"w",encoding="utf-8") as f:json.dump(nb,f,indent=1,ensure_ascii=False)
    print(f"  OK {path} ({os.path.getsize(path)//1024}KB)")

OUT=os.path.dirname(os.path.abspath(__file__))
COLAB=cell("code","# Google Colab Setup\n!pip install -q sympy matplotlib plotly ipywidgets\nimport sympy as sp; sp.init_printing()\nimport numpy as np, matplotlib.pyplot as plt\nprint('Ready ✅')")

def math_04():
    return [
cell("markdown","# Math 04: Calculus — Local Extrema\n\n**Learning Objectives:**\n1. Use derivatives to find a function's local peaks (maxima) and valleys (minima)\n2. Identify critical points where the derivative is 0 or undefined\n3. Apply the First Derivative Test to classify critical points\n4. Implement an extrema-finding algorithm computationally\n\n**Prerequisites:** Math 02 (Derivatives)\n**Estimated time:** 90 minutes\n**Textbook:** *Justin Skycak — Calculus* §1.8"),
COLAB,
cell("markdown","---\n## Phase −1 — Theoretical Foundation\n\n### Finding Local Extrema\n\n> 📖 *From Calculus §1.8:* Derivatives can be used to find a function’s **local extreme values**, its peaks and valleys. At its peaks and valleys, a function’s derivative is either $0$ (a smooth, rounded peak/valley) or undefined (a sharp, pointy peak/valley).\n\n### Critical Points\nThe points at which a function’s derivative is $0$ or undefined, and the function itself exists, are called **critical points**. We find them by:\n1. Taking the derivative $f'(x)$\n2. Noting any singularities (where $f'(x)$ is undefined)\n3. Setting the derivative to $0$ and solving for $x$\n\n**Example:** $f(x) = x^3 - 3x^2$\n1. $f'(x) = 3x^2 - 6x$\n2. No singularities.\n3. $3x^2 - 6x = 0 \\Rightarrow 3x(x - 2) = 0 \\Rightarrow x = 0, x = 2$\n\nSo the critical points are $x=0$ and $x=2$."),
cell("code","# Finding critical points symbolically\nimport sympy as sp\nx = sp.Symbol('x')\nf = x**3 - 3*x**2\nf_prime = sp.diff(f, x)\n\ncritical_points = sp.solve(sp.Eq(f_prime, 0), x)\nprint(f'Critical points of {f}: {critical_points}')"),
cell("markdown","### Classifying Critical Points (First Derivative Test)\n\nNot all critical points are peaks or valleys; some are **saddle points** (flat terrain on the side of a mountain).\n\nTo classify a critical point $c$, inspect the sign of $f'(x)$ on either side:\n- If $f'$ changes from **+ to -**, it's a **local maximum** (ascending, then descending)\n- If $f'$ changes from **- to +**, it's a **local minimum** (descending, then ascending)\n- If $f'$ does not change sign, it's a **saddle point** (neither)"),
cell("markdown","### Comprehension Check ✅\n1. Find the critical point of $f(x) = x^2 - 4x$.\n2. Is it a maximum or a minimum?\n\n<details><summary>💡 Answers</summary>\n\n1. $f'(x) = 2x - 4 = 0 \\Rightarrow x = 2$\n2. For $x < 2$, $f'$ is negative. For $x > 2$, $f'$ is positive. It changes - to +, so it's a **local minimum**.\n</details>"),
cell("markdown","---\n## Phase 0 — Math Foundation Practice\n\n### 🎯 Your Turn: Find and Classify\n\nFind the critical points of $f(x) = \\frac{x^3}{3} - x$. Classify them using the First Derivative Test.\nDo this on paper, then write code to verify."),
cell("code","def classify_critical_points(f_prime_expr):\n    '''Given a sympy expression for f'(x), return a dictionary\n    mapping each critical point to 'min', 'max', or 'saddle'.\n    '''\n    import sympy as sp\n    x = sp.Symbol('x')\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# x = sp.Symbol('x')\n# f_prime = x**2 - 1\n# print(classify_critical_points(f_prime))"),
cell("markdown","---\n## Phase 1 — Algorithm Construction\n\nNow we will build a numerical algorithm to find local extrema of a black-box Python function, using **Gradient Descent/Ascent** (which will be generalized in Notebook 10).\n\n### Step 1: Gradient Descent (Minima)\nTo find a local minimum, start at a guess and take small steps in the *opposite* direction of the slope."),
cell("code","def find_local_minimum(f, f_prime, x_start, lr=0.1, iters=100):\n    '''Find a local minimum by taking steps proportional to the negative gradient.'''\n    x = x_start\n    # YOUR CODE HERE\n    return x\n\n# Test:\n# min_x = find_local_minimum(lambda x: x**2 - 4*x, lambda x: 2*x - 4, 0.0)\n# assert abs(min_x - 2.0) < 1e-3\n# print('Step 1 passed ✅')"),
cell("markdown","### Step 2: Gradient Ascent (Maxima)\nTo find a local maximum, take steps in the *same* direction as the slope."),
cell("code","def find_local_maximum(f, f_prime, x_start, lr=0.1, iters=100):\n    '''Find a local maximum using gradient ascent.'''\n    x = x_start\n    # YOUR CODE HERE\n    return x\n\n# Test:\n# max_x = find_local_maximum(lambda x: -(x-3)**2, lambda x: -2*(x-3), 0.0)\n# assert abs(max_x - 3.0) < 1e-3\n# print('Step 2 passed ✅')"),
cell("markdown","### Step 3: Finding ALL Extrema by Scanning (Interleaved Practice)\nInstead of starting at one point, scan a grid to find all sign changes in the numerical derivative, then polish them."),
cell("code","def find_all_critical_points(f, search_range, num_points=1000):\n    '''Find all critical points in the given range [start, end].\n    Return a list of (x_val, classification) tuples.\n    '''\n    import numpy as np\n    xs = np.linspace(search_range[0], search_range[1], num_points)\n    # Compute numerical derivative at each point\n    # Look for sign changes in the derivative\n    # YOUR CODE HERE\n    pass"),
cell("markdown","---\n## Phase 2 — Experimental Verification\n\n### Visualization\nLet's visualize the critical points found by our scanner on a bumpy function."),
cell("code","import numpy as np, matplotlib.pyplot as plt\n\ndef bumpy(x): return np.sin(x) + np.sin(3*x)/3\ndef bumpy_prime(x): return np.cos(x) + np.cos(3*x)\n\nxs = np.linspace(0, 2*np.pi, 200)\nplt.figure(figsize=(9,5))\nplt.plot(xs, bumpy(xs), 'b-', lw=2, label='f(x)')\nplt.plot(xs, bumpy_prime(xs), 'g--', lw=1, label=\"f'(x)\")\nplt.axhline(0, color='k', lw=1)\n\n# Assuming find_all_critical_points is implemented:\n# crits = find_all_critical_points(bumpy, (0, 2*np.pi))\n# for c, t in crits:\n#    color = 'ro' if t == 'max' else 'yo'\n#    plt.plot(c, bumpy(c), color, ms=8)\n\nplt.legend(); plt.grid(alpha=0.3); plt.tight_layout(); plt.show()"),
cell("markdown","### Pathological Case: Flat Regions & High Frequency\nWhat happens if the function has infinitely many critical points, or flat regions where $f'(x) = 0$ over an interval?"),
cell("code","def flat_bottom(x): return np.maximum(0, x**2 - 1)\n# Plot flat_bottom and consider how our scanner handles it"),
cell("markdown","---\n## Phase 3 — Olympiad Extension\n\n### Challenge: Second Derivative Test\nThe First Derivative Test requires checking signs. The **Second Derivative Test** says:\n- If $f'(c) = 0$ and $f''(c) > 0$, it's a minimum.\n- If $f'(c) = 0$ and $f''(c) < 0$, it's a maximum.\n- If $f''(c) = 0$, the test is inconclusive.\n\nImplement the Second Derivative Test computationally, using a numerical second derivative."),
cell("code","# YOUR CODE HERE\npass"),
cell("markdown","### Chalkboard Defense\nWrite a formal mathematical defense explaining why the Second Derivative Test works, and why it is inconclusive when $f''(c) = 0$.\n\n<details><summary>💡 Hint</summary>\nConsider $f(x) = x^3$ and $g(x) = x^4$ at $x=0$.\nBoth have $f''(0) = g''(0) = 0$.\nBut $x^3$ is a saddle, and $x^4$ is a minimum!\n</details>\n\n---\n📚 **Next:** Math 05 (Linear Algebra — Vectors) transitions from continuous functions to discrete geometry.")
    ]

if __name__=="__main__":
    save(math_04(),os.path.join(OUT,"math_04_calculus_local_extrema.ipynb"))
    print("Batch 1b done.")
