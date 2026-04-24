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

# Notebook 01
nb1_title = "Notebook 01: Introductory Coding Exercises"
nb1_cells = [
    ("md", "## Concept Introduction\nIn this notebook, we practice basic coding structures without external libraries, focusing on arrays, loops, and conditions."),
    ("md", "## 1. Micro-Scaffolding: Checking Symmetry\nWrite a function `check_if_symmetric(string)` that returns `True` if a string is symmetric (reads the same forwards and backwards) and `False` otherwise. Ignore capitalization."),
    ("code", "def check_if_symmetric(string):\n    # Write your code here from scratch\n    pass\n\n# Tests\nprint(check_if_symmetric('racecar'))\nprint(check_if_symmetric('hello'))"),
    ("md", "## 2. Micro-Scaffolding: Character Counts\nWrite a function `count_characters(string)` that returns a dictionary with character counts. Ignore capitalization."),
    ("code", "def count_characters(string):\n    # Write your code here from scratch\n    pass\n\n# Tests\nprint(count_characters('racecar'))"),
    ("md", "## 3. Micro-Scaffolding: Primes\nWrite a function `is_prime(N)` that checks if a number is prime."),
    ("code", "def is_prime(N):\n    # Write your code here from scratch\n    pass\n\n# Tests\nprint(is_prime(7))\nprint(is_prime(10))"),
    ("md", "## 4. Interleaved Practice\nWrite a function `symmetric_prime_counts(string)` that uses `count_characters` and checks if the count of each character is a prime number using `is_prime`."),
    ("code", "def symmetric_prime_counts(string):\n    # Write your code here combining previous logic\n    pass")
]
create_notebook(nb1_title, nb1_cells, "01_introductory_coding.ipynb")

# Notebook 02
nb2_title = "Notebook 02: Number Systems"
nb2_cells = [
    ("md", "## Concept Introduction\nConverting between binary, decimal, and hexadecimal number systems."),
    ("md", "## 1. Micro-Scaffolding: Binary to Decimal\nWrite a function `binary_to_decimal(string)` that converts a binary string to a decimal representation string."),
    ("code", "def binary_to_decimal(string):\n    # Write your code here from scratch\n    pass\n\n# Test\nprint(binary_to_decimal('11010'))  # Should be '26'"),
    ("md", "## 2. Micro-Scaffolding: Decimal to Hexadecimal\nWrite a function `decimal_to_hexadecimal(string)`."),
    ("code", "def decimal_to_hexadecimal(string):\n    # Write your code here from scratch\n    pass"),
    ("md", "## 3. Interleaved Practice: Binary to Hexadecimal\nCombine your logic to convert binary directly to hexadecimal."),
    ("code", "def binary_to_hexadecimal(string):\n    # Write your code here\n    pass"),
    ("md", "## 4. Spaced Repetition: Palindromic Binary\nWrite a function `is_binary_symmetric(string)` that converts a decimal string to binary, and checks if the resulting binary string is symmetric. Use logic from Notebook 01."),
    ("code", "def is_binary_symmetric(decimal_string):\n    # Your spaced repetition code here\n    pass")
]
create_notebook(nb2_title, nb2_cells, "02_number_systems.ipynb")

# Notebook 03
nb3_title = "Notebook 03: Recursive Sequences"
nb3_cells = [
    ("md", "## Concept Introduction\nGenerating recursive sequences like Collatz and Fibonacci sequences, both iteratively and recursively."),
    ("md", "## 1. Micro-Scaffolding: Iterative Fibonacci\nWrite a function that generates the first `n` terms of the Fibonacci sequence iteratively."),
    ("code", "def fibonacci_iterative(n):\n    # Write your code here\n    pass"),
    ("md", "## 2. Micro-Scaffolding: Recursive Fibonacci\nWrite a function that returns the `n`th term of the Fibonacci sequence recursively."),
    ("code", "def fibonacci_recursive(n):\n    # Write your code here\n    pass"),
    ("md", "## 3. Interleaved Practice: Collatz Sequence\nGenerate the Collatz sequence. Start with a number `N`. If even, take half. If odd, multiply by 3 and add 1. Do this iteratively until reaching 1."),
    ("code", "def collatz_sequence(N):\n    # Write your code here\n    pass"),
    ("md", "## 4. Spaced Repetition: Prime Collatz\nFind how many terms in the Collatz sequence of `N` are prime numbers. You must implement or reuse `is_prime` from Notebook 01."),
    ("code", "def count_prime_collatz(N):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb3_title, nb3_cells, "03_recursive_sequences.ipynb")

# Notebook 04
nb4_title = "Notebook 04: Simulating Randomness"
nb4_cells = [
    ("md", "## Concept Introduction\nUsing Monte Carlo simulations to estimate probabilities, specifically coin flips."),
    ("md", "## 1. Micro-Scaffolding: Simulating a Coin Flip\nWrite a function to simulate a coin flip using a random number generator (you may use `random` from the standard library here for the base generator)."),
    ("code", "import random\ndef flip_coin():\n    # Return 'heads' or 'tails'\n    pass"),
    ("md", "## 2. Interleaved Practice: Simulating Probability\nWrite `sim_probability(num_heads, num_flips)` that simulates many trials to find the probability of getting exactly `num_heads` in `num_flips`."),
    ("code", "def sim_probability(num_heads, num_flips, trials=1000):\n    # Write your simulation here\n    pass"),
    ("md", "## 3. Spaced Repetition: Binary Coin Flips\nTreat 'heads' as 1 and 'tails' as 0. Simulate 5 flips to create a binary string, then convert that string to decimal. Repeat this 100 times and find the average decimal value."),
    ("code", "def average_binary_flips():\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb4_title, nb4_cells, "04_simulating_randomness.ipynb")

# Notebook 05
nb5_title = "Notebook 05: Roulette Wheel Selection"
nb5_cells = [
    ("md", "## Concept Introduction\nSampling from an arbitrary discrete probability distribution using roulette wheel selection."),
    ("md", "## 1. Micro-Scaffolding: Cumulative Distribution\nWrite a function to convert a probability distribution list into a cumulative distribution list."),
    ("code", "def get_cumulative_distribution(distribution):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: Sampling an Index\nWrite `sample_index(distribution)` that generates a random decimal and selects the appropriate index based on the cumulative distribution."),
    ("code", "import random\ndef sample_index(distribution):\n    # Write your code here\n    pass"),
    ("md", "## 3. Spaced Repetition: Simulating the Distribution\nLike in Notebook 04, simulate 1000 samples from `[0.4, 0.2, 0.2, 0.2]` and return the observed frequencies."),
    ("code", "def verify_distribution():\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb5_title, nb5_cells, "05_roulette_wheel.ipynb")

# Notebook 06
nb6_title = "Notebook 06: Cartesian Product"
nb6_cells = [
    ("md", "## Concept Introduction\nImplementing the Cartesian product of multiple arrays to understand array manipulation and combinations."),
    ("md", "## 1. Micro-Scaffolding: 2D Cartesian Product\nWrite a function that takes two arrays and returns their Cartesian product (all combinations)."),
    ("code", "def cartesian_product_2d(arr1, arr2):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: N-Dimensional Cartesian Product\nWrite `calc_cartesian_product(ranges)` that takes an array of arrays and returns their Cartesian product. Remember to copy arrays properly."),
    ("code", "def calc_cartesian_product(ranges):\n    # Write your code here\n    pass"),
    ("md", "## 3. Spaced Repetition: Sampling from Cartesian Product\nGiven a Cartesian product space, pick a random element using uniform probability over all elements (use logic from Roulette Wheel)."),
    ("code", "def sample_from_cartesian(ranges):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb6_title, nb6_cells, "06_cartesian_product.ipynb")

# Notebook 07
nb7_title = "Notebook 07: Brute Force Search & Cryptography"
nb7_cells = [
    ("md", "## Concept Introduction\nWe explore brute force search by breaking a linear-encoding cipher.\n\n## Targeted Math Foundations\nFrom `justinmath-algebra.md` Section 1.1 (Solving Linear Equations):\nA linear equation contains only addition, subtraction, multiplication, and division. E.g., `y = 2x + 3`.\nTo solve it, we isolate the variable by performing the inverse operations."),
    ("md", "## 1. Micro-Scaffolding: Linear Encoding\nWrite `encode_string(string, a, b)` that encodes characters into numbers using `f(x) = ax + b` (where space=0, a=1, b=2, etc.)."),
    ("code", "def encode_string(string, a, b):\n    # Write your code here\n    pass"),
    ("md", "## 2. Interleaved Practice: Decoding & Brute Force Search\nWrite `decode_numbers(numbers, a, b)` that attempts to decode an array of numbers. Then write a loop to search for `a` and `b` that produce a valid readable message."),
    ("code", "def decode_numbers(numbers, a, b):\n    # Write your code here\n    pass\n\ndef brute_force_decode(numbers):\n    # Write your brute force search here\n    pass"),
    ("md", "## 3. Spaced Repetition: Cartesian Product Search\nUse `calc_cartesian_product` from Notebook 06 to generate the search space for `(a, b)` instead of nested loops."),
    ("code", "def brute_force_with_cartesian(numbers):\n    # Spaced repetition practice\n    pass")
]
create_notebook(nb7_title, nb7_cells, "07_brute_force_crypto.ipynb")

print("Generated notebooks 1-7")
