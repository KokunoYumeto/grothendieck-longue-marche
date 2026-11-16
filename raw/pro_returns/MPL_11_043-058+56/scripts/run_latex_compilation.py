#!/usr/bin/env python3
"""Compile scratch wrappers; original page files are only read by TeX."""
import concurrent.futures
import json
import re
import subprocess
from pathlib import Path

QA = Path(__file__).resolve().parent
EXPECTED = [(11, n) for n in range(43, 59) if n != 50] + [
    (56, n) for n in range(2, 40) if n not in {10, 19, 34}
]


def compile_page(key):
    cote, scan = key
    stem = f"check_{cote}_scan{scan:03}"
    result = subprocess.run(
        ["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error",
         "-file-line-error", str(QA / (stem + ".tex"))],
        cwd=QA, capture_output=True, text=True,
    )
    output = result.stdout + result.stderr
    (QA / (stem + ".stdout")).write_text(output, encoding="utf-8")
    lines = output.splitlines()
    diagnostics = []
    for index, line in enumerate(lines):
        if (re.search(r"\.tex:\d+:", line) or line.startswith("!")
                or "Missing character:" in line or "Overfull " in line):
            diagnostics.append("\n".join(lines[max(0, index-1):index+7]))
    return {"cote": cote, "scan": scan, "exit_code": result.returncode,
            "diagnostics": diagnostics}


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(compile_page, EXPECTED))
(QA / "per_page_compilation.json").write_text(
    json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps({
    "pages": len(results),
    "successful": sum(row["exit_code"] == 0 for row in results),
    "errors": [row for row in results if row["exit_code"]],
    "warnings": [row for row in results if not row["exit_code"] and row["diagnostics"]],
}, ensure_ascii=False, indent=2))
raise SystemExit(any(row["exit_code"] for row in results))
