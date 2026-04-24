import os
import glob
import nbformat as nbf

def process_notebooks():
    notebook_files = glob.glob('notebooks/*.ipynb')
    
    for filepath in notebook_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = nbf.read(f, as_version=4)
            
        # 1. Inject Phase -1: The Theoretical Proof at the beginning (after the first title cell)
        # We find the index after the first markdown cell that starts with "# "
        insert_idx = 1
        for i, cell in enumerate(nb.cells):
            if cell.cell_type == 'markdown' and cell.source.startswith('#'):
                insert_idx = i + 1
                break
                
        # Check if Phase -1 already exists to prevent duplication
        has_phase_minus_1 = any("Phase -1: The Theoretical Proof" in c.source for c in nb.cells)
        if not has_phase_minus_1:
            phase_minus_1_md = nbf.v4.new_markdown_cell(
                "## Phase -1: The Theoretical Proof (Kiselev/Gelfand Rigor)\n"
                "**Goal**: Guided discovery and axiomatic proof before any code is written.\n"
                "Use the cell below to write a formal LaTeX proof or use `sympy` to mathematically prove the core theorem of this notebook before proceeding."
            )
            phase_minus_1_code = nbf.v4.new_code_cell(
                "import sympy as sp\n# Write your symbolic proof or derivation here\n# e.g., sp.diff(sp.Symbol('x')**2, sp.Symbol('x'))"
            )
            nb.cells.insert(insert_idx, phase_minus_1_code)
            nb.cells.insert(insert_idx, phase_minus_1_md)

        # 2. Hide Boilerplate: Wrap visualization and verification code in <details>
        for cell in nb.cells:
            if cell.cell_type == 'markdown' and ("Phase: Visualization" in cell.source or "Phase: Verification" in cell.source or "Phase: Data Debugging" in cell.source or "Phase: Geometric Intuition" in cell.source):
                if "<details>" not in cell.source:
                    cell.source = f"<details><summary>Click to view helper code instructions</summary>\n\n{cell.source}\n\n</details>"
        
        # 3. Inject Phase 2: Experimental Verification & Phase 3: Olympiad Extension at the end
        has_phase_2 = any("Phase 2: Experimental Verification & Visualization" in c.source for c in nb.cells)
        if not has_phase_2:
            phase_2_md = nbf.v4.new_markdown_cell(
                "## Phase 2: Experimental Verification & Visualization (Arnold's Trivium)\n"
                "**Goal**: Building geometric intuition and exposing algorithmic flaws.\n"
                "Use `matplotlib`, `plotly`, `%%timeit`, and `%lprun` to experimentally verify your algorithm's complexity and visualize its failure on pathological data."
            )
            phase_2_code = nbf.v4.new_code_cell(
                "# Use %%timeit to profile your algorithm's time complexity\n# Visualize a pathological edge case where your algorithm fails"
            )
            nb.cells.append(phase_2_md)
            nb.cells.append(phase_2_code)
            
        has_phase_3 = any("Phase 3: Olympiad Extension" in c.source for c in nb.cells)
        if not has_phase_3:
            phase_3_md = nbf.v4.new_markdown_cell(
                "## Phase 3: Olympiad Extension & Chalkboard Defense\n"
                "**Goal**: Non-routine problem solving and oral defense proxy.\n"
                "1. Invent a workaround for the failure observed in Phase 2.\n"
                "2. Write a rigorous mathematical defense of your algorithmic choices and time complexity below."
            )
            phase_3_code = nbf.v4.new_code_cell(
                "# Implement your Olympiad-level workaround here without scaffolding\npass"
            )
            phase_3_defense = nbf.v4.new_markdown_cell(
                "### Chalkboard Defense\n*Write your formal mathematical defense here using LaTeX.*"
            )
            nb.cells.append(phase_3_md)
            nb.cells.append(phase_3_code)
            nb.cells.append(phase_3_defense)
            
        # Add basic imports at the top if they are missing
        has_imports = any("import sympy" in c.source for c in nb.cells if c.cell_type == 'code')
        if not has_imports:
            imports_code = nbf.v4.new_code_cell(
                "import numpy as np\nimport sympy as sp\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom icecream import ic\nfrom tqdm.notebook import tqdm\nimport ipytest\nipytest.autoconfig()"
            )
            nb.cells.insert(insert_idx, imports_code)

        with open(filepath, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)

    print(f"Successfully processed and injected Hybrid Soviet-Math Academy structures into {len(notebook_files)} notebooks.")

if __name__ == '__main__':
    process_notebooks()
