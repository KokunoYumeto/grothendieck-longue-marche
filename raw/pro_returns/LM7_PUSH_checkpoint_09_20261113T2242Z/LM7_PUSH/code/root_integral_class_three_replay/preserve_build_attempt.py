#!/usr/bin/env python3
"""Keep a named immutable build attempt, its source inputs, and failure reason."""
from pathlib import Path
import hashlib
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
name, reason = sys.argv[1:3]
assert name.replace("_", "").isalnum()
dest = BUILD / name
dest.mkdir(exist_ok=False)
for path in BUILD.iterdir():
    if path.is_file() and path.suffix in {
        ".log", ".json", ".aux", ".toc", ".out", ".bbl", ".blg", ".fls", ".pdf"
    }:
        shutil.copy2(path, dest/path.name)
for name in ("LM7_PUSH_paper.tex", "LM7_PUSH_references.bib", "LM7_PUSH_results.csv"):
    shutil.copy2(ROOT/name, dest/name)
shutil.copytree(ROOT/"sections", dest/"sections")
shutil.copy2(ROOT/"code/build_paper.py", dest/"build_paper_used.py")
record = {"reason": reason, "source_snapshot": "Active project inputs at preservation time",
          "files": [{"file": str(p.relative_to(dest)),
                     "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                    for p in sorted(dest.rglob("*")) if p.is_file()]}
(dest/"preservation_manifest.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({"directory": str(dest.relative_to(ROOT)),
                  "reason": reason, "preserved_files": len(record["files"])}, indent=2))
