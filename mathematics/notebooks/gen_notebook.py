"""Notebook generator utility.

This module keeps the original tuple-to-notebook helpers and adds v1 helpers
for retrieval-first Colab notebooks. New curriculum work should prefer the
source-of-truth exercise shape in ``interactive_generator.py``.
"""
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
    "!pip install -q sympy matplotlib plotly ipywidgets jupyterquiz line_profiler ipytest icecream networkx tqdm\n"
    "\n"
    "import os, sys\n"
    "from pathlib import Path\n"
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "import sympy as sp\n"
    "sp.init_printing(use_unicode=True)\n"
    "\n"
    "repo_root = Path.cwd()\n"
    "if str(repo_root) not in sys.path:\n"
    "    sys.path.insert(0, str(repo_root))\n"
    "\n"
    "try:\n"
    "    from learning_tools import ProgressStore, setup_colab, check, code_check, short_answer_check, hint_box, mastery_dashboard\n"
    "    progress_path = setup_colab()\n"
    "    store = ProgressStore(progress_path)\n"
    "except ModuleNotFoundError:\n"
    "    store = None\n"
    "    print('learning_tools.py not found; core imports are ready, progress tracking is disabled.')\n"
    "\n"
    "print('Environment ready ✅')"
)

def notebook_metadata(notebook_id, title, level, prerequisites=None, skills_taught=None, skills_practiced=None, next_notebook=None):
    """Return a standard metadata code cell for interactive notebooks."""
    payload = {
        "id": notebook_id,
        "level": level,
        "title": title,
        "prerequisites": prerequisites or [],
        "skills_taught": skills_taught or [],
        "skills_practiced": skills_practiced or [],
        "next_notebook": next_notebook,
    }
    return code("NOTEBOOK = " + json.dumps(payload, indent=4))

def retrieval_gate(items):
    """Build a simple retrieval gate from ``(id, skill_id, prompt, accepted)`` tuples."""
    cells = [md("## Before You Learn: Pull From Memory\nAnswer before reading. Retrieval is the point.")]
    for item_id, skill_id, prompt, accepted in items:
        cells.append(md(f"**Recall {item_id}.** {prompt}"))
        cells.append(code(
            "answer = ''\n"
            f"short_answer_check({item_id!r}, answer, {accepted!r}, skill_id={skill_id!r}, confidence=3, store=store)"
        ))
    return cells

def mastery_footer(next_notebook=None):
    """Return the standard end-of-notebook mastery dashboard cell."""
    return code(f"mastery_dashboard(store=store, next_notebook={next_notebook!r})")
