import os
import glob
import nbformat as nbf

os.makedirs('solutions', exist_ok=True)
notebooks = glob.glob('notebooks/*.ipynb')

for nb_path in notebooks:
    filename = os.path.basename(nb_path)
    sol_path = os.path.join('solutions', filename)
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
        
    # Insert a banner at the top of the notebook
    banner_cell = nbf.v4.new_markdown_cell("# 🟢 INSTRUCTOR SOLUTION KEY 🟢\nThis is the solution branch. Use this to check your work if you get stuck.")
    nb.cells.insert(0, banner_cell)
    
    for cell in nb.cells:
        if cell.cell_type == 'code':
            if 'pass' in cell.source:
                cell.source = cell.source.replace('pass', '# TODO: Reference instructor solution implementation here\n    return None')
                
    with open(sol_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

print(f"Generated solution templates for {len(notebooks)} notebooks in solutions/ directory.")