"""Load final research-note metadata and the canonical Markdown bodies.

After the review, source-derived exposition is kept once in the canonical
notes file; this reader preserves reproducible locators and context searches
without duplicating the literature summaries in executable source code.
It never opens images or writes a transcription file.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
N = json.loads((ROOT / "records" / "note_definitions.json").read_text(encoding="utf-8"))
canonical = (ROOT / "MPL_137_002-044_notes.md").read_text(encoding="utf-8")
blocks = {
    match.group(1): match.group(3).split("**Kind:** ", 1)[1].split("\n\n", 1)[1].strip()
    for match in re.finditer(
        r"^## (R\d{3}) — ([^\n]+)\n(.*?)(?=^## |\Z)",
        canonical, re.MULTILINE | re.DOTALL)
}
for note in N:
    note["body"] = blocks[note["id"]]
if __name__ == "__main__":
    print(json.dumps({"notes": len(N), "canonical": str(ROOT / "MPL_137_002-044_notes.md")}))
