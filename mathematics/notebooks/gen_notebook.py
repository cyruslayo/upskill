"""Notebook generator utility — converts a list of (cell_type, source) tuples into valid .ipynb JSON."""
import json, uuid, sys, os

def md(source):
    """Create a markdown cell tuple."""
    return ("markdown", source)

def code(source):
    """Create a code cell tuple."""
    return ("code", source)

def build_notebook(cells):
    """Convert list of (type, source_str) into valid nbformat-4 JSON."""
    nb_cells = []
    for ctype, src in cells:
        cell = {
            "cell_type": ctype,
            "id": uuid.uuid4().hex[:8],
            "metadata": {},
            "source": src.split("\n")  # keep as list of lines
        }
        if ctype == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
        nb_cells.append(cell)
    return {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def save(notebook_dict, filepath):
    """Write notebook dict to .ipynb file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(notebook_dict, f, indent=1, ensure_ascii=False)
    print(f"  ✅ Wrote {filepath} ({os.path.getsize(filepath)//1024}KB)")

# ── Shared Colab setup cell ──────────────────────────────────────────
COLAB_SETUP = code(
    "# ── Google Colab Setup ─────────────────────────────────────────\n"
    "# Run this cell first if you are on Google Colab.\n"
    "!pip install -q sympy matplotlib plotly ipywidgets line_profiler ipytest icecream\n"
    "\n"
    "import os, sys\n"
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "import sympy as sp\n"
    "sp.init_printing(use_unicode=True)\n"
    "\n"
    "print('Environment ready ✅')"
)
