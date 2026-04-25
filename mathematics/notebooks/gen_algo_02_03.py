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
COLAB=cell("code","# Google Colab Setup\nprint('Ready ✅')")

def algo_02():
    return [
cell("markdown","# Algorithms 02: Number Systems\n\n**Learning Objectives:**\n1. Understand base-2 (binary) and base-16 (hexadecimal) number systems\n2. Convert numbers from base-b to decimal using positional coefficients\n3. Convert decimal numbers to base-b using repeated division\n4. Write modular conversion functions from scratch\n\n**Prerequisites:** Algorithms 01\n**Estimated time:** 90 minutes\n**Textbook:** *Justin Skycak — Intro to Algorithms & Machine Learning* Chapter 2"),
COLAB,
cell("markdown","---\n## Phase −1 — Theoretical Foundation\n\n### Number Systems\n> 📖 *From Algorithms Ch. 2:* We are used to representing numbers using ten characters (0-9). This is called the **decimal** (base-10) system. The **binary** (base-2) system uses two characters (0, 1), and the **hexadecimal** (base-16) system uses sixteen characters (0-9, A-F, where A=10, ..., F=15).\n\n### Converting from Base-b to Decimal\nIf you have a number $x_n x_{n-1} \\dots x_1 x_0$ in base-$b$, its decimal value is:\n$$x_n \\cdot b^n + x_{n-1} \\cdot b^{n-1} + \\dots + x_1 \\cdot b^1 + x_0 \\cdot b^0$$\n\n**Example:** `11010` in binary\n$= 1(2^4) + 1(2^3) + 0(2^2) + 1(2^1) + 0(2^0) = 16 + 8 + 0 + 2 + 0 = 26$.\n\n### Converting from Decimal to Base-b\nRepeatedly compute the highest power of $b$ that is $\\leq$ your number, subtract off the largest multiple of that power, and record the multiple as your digit.\n*(Equivalently, you can repeatedly divide by $b$ and record the remainders, then reverse them).*"),
cell("markdown","### Comprehension Check ✅\n1. What is the decimal value of the hexadecimal number `10`?\n2. What is the highest power of 2 that is less than or equal to 50?\n\n<details><summary>💡 Answers</summary>\n\n1. $1 \\cdot 16^1 + 0 \\cdot 16^0 = 16$.\n2. $2^5 = 32$. ($2^6=64$ is too big).\n</details>"),
cell("markdown","---\n## Phase 0 — Math Foundation Practice\n\n### 🎯 Your Turn: Convert by Hand\n1. Convert binary `1011` to decimal.\n2. Convert decimal `42` to binary.\n\nDo this on paper, then run the cell below to check."),
cell("code","# Check your manual conversions using built-in functions\nprint('1011 in binary ->', int('1011', 2), 'in decimal')\nprint('42 in decimal ->', bin(42)[2:], 'in binary')"),
cell("markdown","---\n## Phase 1 — Algorithm Construction\n\nImplement the following conversion functions from scratch. **Do not use Python's built-in `bin()`, `hex()`, or `int(string, base)` functions.**"),
cell("code","def binary_to_decimal(string):\n    '''Convert a binary string to a decimal integer.'''\n    # YOUR CODE HERE\n    pass\n\n# assert binary_to_decimal('11010') == 26"),
cell("code","def hexadecimal_to_decimal(string):\n    '''Convert a hex string to a decimal integer.'''\n    # Hint: Create a dictionary mapping 'A'->10, 'B'->11, etc.\n    # YOUR CODE HERE\n    pass\n\n# assert hexadecimal_to_decimal('1A') == 26\n# assert hexadecimal_to_decimal('3B07F') == 241791"),
cell("code","def decimal_to_binary(decimal_int):\n    '''Convert a decimal integer to a binary string.'''\n    if decimal_int == 0: return '0'\n    # YOUR CODE HERE\n    pass\n\n# assert decimal_to_binary(26) == '11010'"),
cell("code","def decimal_to_hexadecimal(decimal_int):\n    '''Convert a decimal integer to a hex string.'''\n    # Hint: Need a reverse mapping from 10->'A', 11->'B', etc.\n    # YOUR CODE HERE\n    pass\n\n# assert decimal_to_hexadecimal(26) == '1A'\n# assert decimal_to_hexadecimal(241791) == '3B07F'"),
cell("markdown","### Composition (Interleaved Practice)\nNow reuse your functions to convert between binary and hex!"),
cell("code","def binary_to_hexadecimal(string):\n    # YOUR CODE HERE\n    pass\n\ndef hexadecimal_to_binary(string):\n    # YOUR CODE HERE\n    pass"),
cell("markdown","---\n## Phase 2 — Experimental Verification\n\n### Pathological Case: Converting 0 and Negative Numbers\nOur algorithms assumed positive numbers. What happens if you pass `0` to your `decimal_to_binary` function? What if you pass `-5`? \nIf your code crashes or loops infinitely, modify it to handle `0` gracefully."),
cell("code","# Test your edge cases\n# print(decimal_to_binary(0))\n# print(decimal_to_hexadecimal(0))"),
cell("markdown","---\n## Phase 3 — Olympiad Extension\n\n### Challenge: Base-b Converter\nWrite a universal converter that can convert a string from *any* base $b_1$ to *any* base $b_2$, where $2 \\leq b \\leq 36$ (using 0-9 and A-Z)."),
cell("code","def convert_base(string, b_from, b_to):\n    # YOUR CODE HERE\n    pass\n\n# Test: Convert 'Z' (35 in base-36) to base-2 (100011)\n# assert convert_base('Z', 36, 2) == '100011'"),
cell("markdown","### Chalkboard Defense\nExplain why converting directly from Binary to Hexadecimal (and vice-versa) is much faster than converting through Decimal. How could you exploit this to write a faster `binary_to_hexadecimal` function?\n\n<details><summary>💡 Sketch</summary>\nBecause $16 = 2^4$, every single hexadecimal digit maps *exactly* to a 4-bit binary sequence. You don't need to compute the total value; you can just chunk the binary string into groups of 4 and map them directly (e.g., `1010` -> `A`).\n</details>\n\n---\n📚 **Next:** Algorithms 03 (Recursive Sequences)")
    ]

def algo_03():
    return [
cell("markdown","# Algorithms 03: Recursive Sequences\n\n**Learning Objectives:**\n1. Understand what a recursive sequence is\n2. Compute sequence terms using iterative loops (arrays/variables)\n3. Compute sequence terms using function recursion\n4. Understand the time and space complexity tradeoffs between iteration and recursion\n\n**Prerequisites:** Algorithms 02\n**Estimated time:** 60 minutes\n**Textbook:** *Justin Skycak — Intro to Algorithms & Machine Learning* Chapter 3"),
COLAB,
cell("markdown","---\n## Phase −1 — Theoretical Foundation\n\n### What is a Recursive Sequence?\n> 📖 *From Algorithms Ch. 3:* A **recursive sequence** is a sequence where each term is a function of the previous terms.\n\nExample: Starting with 3, generate each term by doubling the previous term and adding 1. \nSequence: 3, 7, 15, 31, 63, ...\n\nThere are two main ways to compute the $n$-th term computationally:\n1. **Iterative (Bottom-up):** Start at term 1, apply the rule $n-1$ times using a loop.\n2. **Recursive (Top-down):** Define a function that calls *itself*. The function asks for term $n-1$, which asks for term $n-2$, until hitting the **Base Case** (term 1)."),
cell("markdown","### Iterative vs Recursive Tracing\nSuppose we want the 3rd term of the sequence.\n\n**Iterative:**\n- `term = 3` (1st)\n- `term = 2*3 + 1 = 7` (2nd)\n- `term = 2*7 + 1 = 15` (3rd) -> Return 15.\n\n**Recursive:**\n- `f(3)` returns `2 * f(2) + 1`\n  - `f(2)` returns `2 * f(1) + 1`\n    - `f(1)` hits the base case: returns `3`\n  - `f(2)` gets 3, computes `2*3+1 = 7`, returns `7`\n- `f(3)` gets 7, computes `2*7+1 = 15`, returns `15`."),
cell("markdown","### Comprehension Check ✅\n1. What is the base case in the Fibonacci sequence ($F_n = F_{n-1} + F_{n-2}$)?\n2. What happens if a recursive function forgets its base case?\n\n<details><summary>💡 Answers</summary>\n\n1. There are two base cases: $F_1 = 1$ and $F_2 = 1$.\n2. It will call itself forever (infinite loop), eventually crashing with a \"RecursionError\" or \"Stack Overflow\".\n</details>"),
cell("markdown","---\n## Phase 0 — Math Foundation Practice\n\n### 🎯 Your Turn: The Fibonacci Sequence\nThe Fibonacci sequence starts with 0 and 1. Each subsequent term is the sum of the two preceding terms: `0, 1, 1, 2, 3, 5, 8, ...`\n\nFind the 10th term by hand (where 1st term is 0)."),
cell("code","def test_fib():\n    # Replace with your manual answer\n    fib_10 = None\n    # assert fib_10 == 34\n    # print('Phase 0 passed ✅')\ntest_fib()"),
cell("markdown","---\n## Phase 1 — Algorithm Construction\n\n### Step 1: Iterative Implementation\nImplement a function to compute the $n$-th term of the sequence from the chapter: `start=3`, `next = 2*prev + 1`. Use a `for` loop."),
cell("code","def calc_nth_term_iterative(n):\n    '''Return the n-th term using a loop.'''\n    # YOUR CODE HERE\n    pass\n\n# assert calc_nth_term_iterative(4) == 31\n# print('Step 1 passed ✅')"),
cell("markdown","### Step 2: Recursive Implementation\nNow implement the exact same sequence using a recursive function call."),
cell("code","def calc_nth_term_recursive(n):\n    '''Return the n-th term using recursion.'''\n    # YOUR CODE HERE\n    pass\n\n# assert calc_nth_term_recursive(4) == 31\n# print('Step 2 passed ✅')"),
cell("markdown","### Step 3: Recursive Fibonacci (Interleaved Practice)\nImplement the Fibonacci sequence recursively. Remember, you need *two* base cases!"),
cell("code","def fib_recursive(n):\n    '''Return the n-th Fibonacci number (1st=0, 2nd=1).'''\n    # YOUR CODE HERE\n    pass\n\n# assert fib_recursive(10) == 34\n# print('Step 3 passed ✅')"),
cell("markdown","---\n## Phase 2 — Experimental Verification\n\n### Pathological Case: Exponential Time Complexity\nLet's compare the time taken by an iterative vs a recursive Fibonacci function. \n*Warning: This might take a few seconds to run!*"),
cell("code","def fib_iterative(n):\n    a, b = 0, 1\n    for _ in range(n - 1):\n        a, b = b, a + b\n    return a\n\nimport time\nn = 35\nstart = time.time()\nprint(f\"Iterative result: {fib_iterative(n)}\")\nprint(f\"Iterative time: {time.time() - start:.5f}s\")\n\nstart = time.time()\nprint(f\"Recursive result: {fib_recursive(n)}\")\nprint(f\"Recursive time: {time.time() - start:.5f}s\")"),
cell("markdown","### 🔍 Reflection\nWhy is the recursive Fibonacci so absurdly slow? \n\n<details><summary>💡 Answer</summary>\nBecause `fib(35)` calls `fib(34)` and `fib(33)`. But `fib(34)` *also* calls `fib(33)` and `fib(32)`. The number of function calls doubles at each step, resulting in $O(2^n)$ time complexity! The same computations are repeated millions of times.\n</details>"),
cell("markdown","---\n## Phase 3 — Olympiad Extension\n\n### Challenge: Memoization\nWe can fix the recursive function by **caching** (memoizing) results we've already computed. \nCreate a dictionary that stores the results of `fib(n)`. Before computing `fib(n)`, check if it's in the dictionary.\nImplement `fib_memoized(n)` and show that it can compute $n=100$ instantly."),
cell("code","memo = {1: 0, 2: 1}\ndef fib_memoized(n):\n    # YOUR CODE HERE\n    pass\n\n# print(fib_memoized(100))"),
cell("markdown","### Chalkboard Defense\nExplain the space complexity (memory usage) of the iterative Fibonacci versus the recursive Fibonacci. What causes the recursive version to use $O(n)$ memory even without memoization?\n\n<details><summary>💡 Sketch</summary>\nThe iterative version only stores two variables `a` and `b`, so it is $O(1)$ space.\nThe recursive version creates a new function call *stack frame* for each layer of recursion. To compute `fib(n)`, the call stack gets $n$ layers deep before hitting the base case, so it requires $O(n)$ memory.\n</details>\n\n---\n📚 **Next:** Algorithms 04 (Simulating Randomness)")
    ]

if __name__=="__main__":
    save(algo_02(),os.path.join(OUT,"02_number_systems.ipynb"))
    save(algo_03(),os.path.join(OUT,"03_recursive_sequences.ipynb"))
    print("Notebooks 02 and 03 done.")
