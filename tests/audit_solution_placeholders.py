"""Report legacy instructor solution placeholders.

This is an audit, not a failing validation. The new source-of-truth Level 0
solution notebooks are complete; older legacy solution notebooks were migrated
into the interactive shell and still need content-authoring passes to replace
their historical placeholder bodies.
"""
from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "mathematics" / "solutions"
OUT = ROOT / "curriculum" / "solution_backlog.json"


def main() -> int:
    backlog = []
    for path in sorted(SOLUTIONS.glob("*.ipynb")):
        if path.name.startswith("math_00"):
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        functions = []
        for index, cell in enumerate(nb.get("cells", []), 1):
            text = "\n".join(cell.get("source", []))
            if "TODO: Reference instructor solution implementation here" in text:
                names = re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)", text, flags=re.M)
                functions.extend(names or [f"cell_{index}"])
        if functions:
            backlog.append({
                "notebook": path.name,
                "placeholder_count": len(functions),
                "items": functions,
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "schema_version": 1,
        "description": "Legacy solution cells that still require authored answers.",
        "total_notebooks": len(backlog),
        "total_placeholders": sum(item["placeholder_count"] for item in backlog),
        "backlog": backlog,
    }, indent=2), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"legacy solution placeholders: {sum(item['placeholder_count'] for item in backlog)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

