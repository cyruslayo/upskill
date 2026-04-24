import os
import glob
import nbformat as nbf

def process_colab():
    notebook_files = glob.glob('notebooks/*.ipynb') + glob.glob('solutions/*.ipynb')
    
    colab_setup_md = nbf.v4.new_markdown_cell(
        "## Google Colab Setup\n"
        "Run the following cell to install necessary libraries and generate the toy datasets required for this notebook in the Colab environment."
    )
    
    colab_setup_code = nbf.v4.new_code_cell(
        "# Install external dependencies not pre-installed on Colab\n"
        "!pip install -q line_profiler ipytest icecream\n\n"
        "import os\n"
        "import pandas as pd\n"
        "import numpy as np\n\n"
        "# Generate toy datasets locally for Colab\n"
        "os.makedirs('datasets', exist_ok=True)\n\n"
        "np.random.seed(42)\n"
        "size = 200\n"
        "sqft = np.random.normal(1500, 500, size)\n"
        "beds = np.random.randint(1, 6, size)\n"
        "baths = np.random.randint(1, 4, size)\n"
        "price = 150 * sqft + 10000 * beds + 5000 * baths + np.random.normal(0, 20000, size)\n"
        "pd.DataFrame({'SqFt': sqft, 'Bedrooms': beds, 'Bathrooms': baths, 'Price': price}).to_csv('datasets/housing.csv', index=False)\n\n"
        "heart_rate = np.random.normal(75, 15, size)\n"
        "blood_pressure = np.random.normal(120, 20, size)\n"
        "disease = (heart_rate + blood_pressure > 200).astype(int)\n"
        "pd.DataFrame({'HeartRate': heart_rate, 'BloodPressure': blood_pressure, 'Disease': disease}).to_csv('datasets/medical.csv', index=False)\n\n"
        "emails = ['Win a million dollars now!', 'Meeting agenda for tomorrow', 'URGENT: Account locked, please click here', 'Can we reschedule our lunch?', 'Buy cheap pills online', 'Here is the project report you requested', 'Claim your free vacation today', 'Happy birthday! Hope you have a great day']\n"
        "labels = [1, 0, 1, 0, 1, 0, 1, 0]\n"
        "pd.DataFrame({'Text': emails * 25, 'Spam': labels * 25}).to_csv('datasets/emails.csv', index=False)\n\n"
        "print('Colab environment setup complete!')"
    )
    
    for filepath in notebook_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                nb = nbf.read(f, as_version=4)
                
            # Check if already has colab setup
            if not any("Google Colab Setup" in cell.source for cell in nb.cells):
                # Insert after the main title cell
                insert_idx = 0
                for i, cell in enumerate(nb.cells):
                    if cell.cell_type == 'markdown' and cell.source.startswith('# ') and 'INSTRUCTOR SOLUTION KEY' not in cell.source:
                        insert_idx = i + 1
                        break
                
                # If we didn't find a title, just put it at the top (or after the instructor key)
                if insert_idx == 0:
                    for i, cell in enumerate(nb.cells):
                        if 'INSTRUCTOR SOLUTION KEY' in cell.source:
                            insert_idx = i + 1
                        
                nb.cells.insert(insert_idx, colab_setup_md)
                nb.cells.insert(insert_idx + 1, colab_setup_code)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    nbf.write(nb, f)
        except Exception as e:
            print(f"Failed processing {filepath}: {e}")

    print(f"Successfully added Google Colab setup to notebooks.")

if __name__ == '__main__':
    process_colab()