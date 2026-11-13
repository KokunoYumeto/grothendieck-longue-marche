#!/usr/bin/env python3
"""Preserve the stale-input build before repairing the recursive TeX path."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
DEST = BUILD / "checkpoint05_second_stale_source"
DEST.mkdir(exist_ok=False)
files = []
for path in BUILD.iterdir():
    if path.is_file() and (path.suffix in {".log", ".json", ".aux", ".toc", ".out", ".bbl", ".blg"}
                           or path.name == "LM7_PUSH_paper.pdf"):
        shutil.copy2(path, DEST / path.name)
        files.append({"file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
shutil.copy2(ROOT / "code/build_paper.py", DEST / "build_paper_used.py")
reason = {
    "reason": "TEXINPUTS used build// before the current directory. The second checkpoint05 build therefore selected the preserved first draft main source and sections.",
    "source_snapshot_selected": "build/checkpoint05_first_complete",
    "delivered_as_current": False,
    "repair": "Use explicit nonrecursive root and build paths, an absolute main source, and verify the recorder input manifest against every active included section.",
    "files": files,
}
(DEST / "reason.json").write_text(json.dumps(reason, indent=2)+"\n")
print(json.dumps(reason, indent=2))
