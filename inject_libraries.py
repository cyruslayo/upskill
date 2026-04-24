import nbformat as nbf
import os
import glob

def inject_cells_at_end(filename, new_cells_data):
    filepath = os.path.join('notebooks', filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} (not found)")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
        
    new_cells = []
    for c_type, content in new_cells_data:
        if c_type == "md":
            new_cells.append(nbf.v4.new_markdown_cell(content))
        elif c_type == "code":
            new_cells.append(nbf.v4.new_code_cell(content))
            
    nb.cells.extend(new_cells)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Enhanced {filename}")


# 1. 04_simulating_randomness.ipynb -> Matplotlib Histogram Visualization
enhancement_04 = [
    ("md", "## Phase: Visualization & Intuition (matplotlib)\nLet's visualize the distribution of our simulated coin flips to see the bell curve emerge."),
    ("code", "import matplotlib.pyplot as plt\nimport numpy as np\n\n# Assuming you ran sim_probability for a range of heads:\n# (This is scaffolded code you can adapt to your results)\n# flips = np.random.binomial(n=10, p=0.5, size=1000)\n# plt.hist(flips, bins=11, density=True, alpha=0.6, color='b')\n# plt.title('Distribution of Heads in 10 Coin Flips')\n# plt.xlabel('Number of Heads')\n# plt.ylabel('Probability')\n# plt.show()")
]
inject_cells_at_end("04_simulating_randomness.ipynb", enhancement_04)

# 2. 10_single_variable_gd.ipynb -> IPywidgets Interactivity & Matplotlib
enhancement_10 = [
    ("md", "## Phase: Active Learning (ipywidgets + matplotlib)\nLet's make the learning rate interactive! Drag the slider to see how changing the learning rate changes the gradient descent path."),
    ("code", "import matplotlib.pyplot as plt\nimport numpy as np\nfrom ipywidgets import interact, FloatSlider\n\ndef plot_gd(alpha=0.1):\n    x = np.linspace(-5, 5, 100)\n    y = x**2  # Example function\n    plt.plot(x, y, label='f(x) = x^2')\n    \n    # Scaffold for plotting steps (x_steps, y_steps)\n    # plt.scatter(x_steps, y_steps, color='red')\n    # plt.plot(x_steps, y_steps, color='red', linestyle='--')\n    \n    plt.title(f'Gradient Descent Path (alpha={alpha})')\n    plt.legend()\n    plt.show()\n\ninteract(plot_gd, alpha=FloatSlider(value=0.1, min=0.01, max=1.0, step=0.05));")
]
inject_cells_at_end("10_single_variable_gd.ipynb", enhancement_10)

# 3. 16_k_means_clustering.ipynb -> Pandas Rendering and Matplotlib
enhancement_16 = [
    ("md", "## Phase: Data Debugging & Visualization (pandas & matplotlib)\nUse pandas to render the clustered data nicely, and matplotlib to see the centroids."),
    ("code", "import pandas as pd\nimport matplotlib.pyplot as plt\n\n# Example of rendering data\n# df = pd.DataFrame(points, columns=['x', 'y'])\n# df['cluster'] = assigned_clusters\n# display(df.head()) # Renders a beautiful HTML table\n\n# plt.scatter(df['x'], df['y'], c=df['cluster'], cmap='viridis')\n# plt.scatter(centroids[:,0], centroids[:,1], color='red', marker='X', s=200, label='Centroids')\n# plt.legend()\n# plt.show()")
]
inject_cells_at_end("16_k_means_clustering.ipynb", enhancement_16)

# 4. 23-25_regression_pseudoinverse.ipynb -> Scikit-Learn Verification & LaTeX Display
enhancement_23 = [
    ("md", "## Phase: Dynamic Math (IPython.display)\nLet's dynamically render your calculated weights as a mathematical formula."),
    ("code", "from IPython.display import display, Math\n\n# Assuming weights = [w0, w1, w2]\n# formula = f'y = {w0:.2f} + {w1:.2f}x_1 + {w2:.2f}x_2'\n# display(Math(formula))"),
    ("md", "## Phase: Verification (scikit-learn)\nUse scikit-learn to confirm your from-scratch pseudoinverse implementation produces the exact same weights as industry-standard linear regression."),
    ("code", "from sklearn.linear_model import LinearRegression\nimport numpy as np\n\n# model = LinearRegression()\n# model.fit(X, Y)\n# print('Sklearn Weights:', model.coef_, model.intercept_)\n# assert np.allclose(your_weights, sklearn_weights) # Verify!")
]
inject_cells_at_end("23-25_regression_pseudoinverse.ipynb", enhancement_23)

# 5. 31_bfs_dfs.ipynb -> NetworkX Visualization
enhancement_31 = [
    ("md", "## Phase: Geometric Intuition (networkx)\nVisualize the graph you are traversing to verify your BFS/DFS order."),
    ("code", "import networkx as nx\nimport matplotlib.pyplot as plt\n\n# G = nx.Graph()\n# G.add_edges_from([(1,2), (1,3), (2,4), (3,4)])\n# nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')\n# plt.show()")
]
inject_cells_at_end("31_bfs_dfs.ipynb", enhancement_31)

print("Injected library enhancements into select notebooks.")
