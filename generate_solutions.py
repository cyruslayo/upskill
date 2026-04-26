"""Generate real instructor solution notebooks for source-of-truth lessons.

The old implementation replaced ``pass`` with TODO placeholders. That made the
solution notebooks look complete while still being empty. The interactive
generator now owns exercise scaffolds, tests, hints, and full solutions.
"""
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parent
GENERATOR = ROOT / "mathematics" / "notebooks" / "interactive_generator.py"


if __name__ == "__main__":
    runpy.run_path(str(GENERATOR), run_name="__main__")
    print("Generated source-of-truth student notebooks and real instructor solutions.")
