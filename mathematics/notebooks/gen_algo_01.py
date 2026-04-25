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
COLAB=cell("code","# Google Colab Setup\n!pip install -q icecream line_profiler\nfrom icecream import ic\nprint('Ready ✅')")

def algo_01():
    return [
cell("markdown","# Algorithms 01: Introductory Coding\n\n**Learning Objectives:**\n1. Review basic control flow (loops, if/else) without using external libraries\n2. Solve common algorithmic primitives from scratch\n3. Learn basic testing methodologies\n4. Develop strong debugging habits using print statements\n\n**Prerequisites:** Basic programming familiarity\n**Estimated time:** 120 minutes\n**Textbook:** *Justin Skycak — Intro to Algorithms & Machine Learning* Chapter 1"),
COLAB,
cell("markdown","---\n## Phase −1 — Theoretical Foundation\n\n### The Math Academy / Eurisko Philosophy\n> 📖 *From Algorithms Ch. 1:* Write the following functions from scratch. Don’t use any external libraries or any built-in functions that allow you to bypass the use of for loops, while loops, or if statements in nontrivial ways. In particular, don’t use `Set` or `Counter`.\n\nIn this course, we build everything from the ground up. Before you can use a library to sort an array, you must write the sorting algorithm yourself. This develops deep algorithmic intuition.\n\n### Debugging Principles\n1. **Print out everything.** Within the function you're debugging, print every manipulation. Bugs hide where you don't expect them.\n2. **Identify the first discrepancy.** Manually trace what the code *should* do step-by-step, and see where the printed output deviates from your manual trace."),
cell("markdown","### Comprehension Check ✅\n1. Why are we forbidden from using Python's `set()` to find the intersection of two arrays?\n2. What is the most effective tool for debugging when your code produces the wrong answer?\n\n<details><summary>💡 Answers</summary>\n\n1. Because using `set()` abstracts away the algorithmic logic of searching and comparing elements. By writing it from scratch, you learn how intersection actually works under the hood.\n2. Print statements! (`print()` or `ic()` from the icecream library) to trace the state of variables at every step.\n</details>"),
cell("markdown","---\n## Phase 0 — Math Foundation Practice\n\nBefore writing code, let's trace an algorithm manually.\n\n### 🎯 Your Turn: Trace `get_intersection`\nSuppose `array1 = [3, 1, 4]` and `array2 = [4, 5, 3]`.\nTrace how you would find the intersection without using `set()`.\n\n| Step | Action | Output Array |\n|---|---|---|\n| 1 | Look at `3` in array1. Is `3` in array2? Yes. | `[3]` |\n| 2 | Look at `1` in array1. Is `1` in array2? No. | `[3]` |\n| 3 | Look at `4` in array1. Is `4` in array2? Yes. | `[3, 4]` |\n\nWrite a simple loop to verify this trace computationally."),
cell("code","def simple_intersection(a1, a2):\n    out = []\n    # YOUR CODE HERE: use a for loop to check elements of a1 against a2\n    pass\n\n# assert simple_intersection([3, 1, 4], [4, 5, 3]) == [3, 4]\n# print('Phase 0 passed ✅')"),
cell("markdown","---\n## Phase 1 — Micro-Scaffolded Algorithm Construction\n\nNow we will implement the 6 core exercises from Chapter 1. Remember: **No imports, no `set()`, no `Counter()`.**"),
cell("markdown","### Exercise 1: `check_if_symmetric(string)`\nReturn `True` if a string is a palindrome, `False` otherwise. Ignore capitalization."),
cell("code","def check_if_symmetric(string):\n    '''Return True if string is a palindrome, ignoring case.'''\n    # YOUR CODE HERE\n    pass\n\n# Tests:\n# assert check_if_symmetric('racecar') == True\n# assert check_if_symmetric('Racecar') == True\n# assert check_if_symmetric('hello') == False"),
cell("markdown","### Exercise 2: `convert_to_numbers(string)`\nReturn an array of numbers corresponding to letters: space=0, a=1, b=2, etc."),
cell("code","def convert_to_numbers(string):\n    '''Convert string to an array of integers.'''\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# assert convert_to_numbers('a cat') == [1, 0, 3, 1, 20]"),
cell("markdown","### Exercise 3: `get_intersection(array1, array2)`\nReturn elements in both arrays, with NO duplicates in the output."),
cell("code","def get_intersection(array1, array2):\n    '''Return intersection without duplicates.'''\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# assert sorted(get_intersection([1, 2, 2, 3], [2, 3, 4])) == [2, 3]"),
cell("markdown","### Exercise 4: `get_union(array1, array2)`\nReturn elements in either array, with NO duplicates."),
cell("code","def get_union(array1, array2):\n    '''Return union without duplicates.'''\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# assert sorted(get_union([1, 2], [2, 3])) == [1, 2, 3]"),
cell("markdown","### Exercise 5: `count_characters(string)`\nReturn a dictionary counting occurrences of each character (case-insensitive)."),
cell("code","def count_characters(string):\n    '''Return a dict of char counts.'''\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# assert count_characters('A cat') == {'a': 2, ' ': 1, 'c': 1, 't': 1}"),
cell("markdown","### Exercise 6: `is_prime(N)`\nCheck if N > 1 is prime by testing divisors up to floor(N/2)."),
cell("code","def is_prime(N):\n    '''Return True if N is prime, else False.'''\n    if N <= 1: return False\n    # YOUR CODE HERE\n    pass\n\n# Tests:\n# assert is_prime(2) == True\n# assert is_prime(4) == False\n# assert is_prime(17) == True"),
cell("markdown","---\n## Phase 2 — Experimental Verification\n\n### Pathological Case: Time Complexity of `is_prime`\nWhat happens if we test a huge prime number? Let's use `%timeit` to see how long our algorithm takes."),
cell("code","# Try to check a very large prime number: 15485863 (the 1 millionth prime)\nimport time\nstart = time.time()\n# is_prime(15485863) # uncomment to test\nprint(f\"Time taken: {time.time() - start:.4f} seconds\")"),
cell("markdown","### 🔍 Reflection\n1. If we use the condition `n <= N/2`, we check $\\approx 7.5$ million numbers.\n2. How could we optimize this bound? (Hint: Think about factors appearing in pairs).\n\n<details><summary>💡 Answer</summary>\n\nFactors come in pairs. If $A \\times B = N$, one of them must be $\\leq \\sqrt{N}$.\nSo we only need to check up to $\\lfloor \\sqrt{N} \\rfloor$. For $N=15485863$, $\\sqrt{N} \\approx 3935$. This reduces the loop from 7.5 million iterations to 4 thousand!\n</details>"),
cell("markdown","---\n## Phase 3 — Olympiad Extension\n\n### Challenge: The Sieve of Eratosthenes\nIf you need to find *all* prime numbers up to $M$, calling `is_prime()` $M$ times is too slow.\nThe Sieve of Eratosthenes finds all primes up to $M$ efficiently. Implement it from scratch."),
cell("code","def sieve_of_eratosthenes(M):\n    '''Return a list of all primes up to M.'''\n    # Create a boolean array [True] * (M+1)\n    # YOUR CODE HERE\n    pass\n\n# Test:\n# assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"),
cell("markdown","### Chalkboard Defense\nExplain why `get_intersection` takes $O(N^2)$ time if implemented with nested loops (or `in` on lists), and how you could make it $O(N \\log N)$ using sorting, or $O(N)$ using dictionaries (which are allowed as long as you don't use `set()`).\n\n*(Write your defense below)*\n\n<details><summary>💡 Sketch</summary>\n\nIf we loop over `array1` (length $N$) and for each element, scan `array2` (length $N$) using `in`, the total operations are $N \\times N = N^2$.\nIf we use a dictionary to store elements of `array2` first ($O(N)$), dictionary lookups are $O(1)$. So looping through `array1` and checking the dictionary takes $O(N)$. Total time: $O(N)$.\n</details>\n\n---\n📚 **Next:** Algorithms 02 (Computational Math & Base Conversions)")
    ]

if __name__=="__main__":
    save(algo_01(),os.path.join(OUT,"01_introductory_coding.ipynb"))
    print("Notebook 01 done.")
