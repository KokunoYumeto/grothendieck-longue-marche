#!/usr/bin/env python3
"""Refresh only the mechanical harness input list from currently saved pages."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
harness = root / "records" / "compile_harness.tex"
text = harness.read_text(encoding="utf-8")
marker = r"\begin{document}"
if text.count(marker) != 1:
    raise SystemExit("Expected one document opening in the separate compile harness.")
preamble = text.split(marker, 1)[0] + marker + "\n"
pages = sorted((root / "pages").glob("MPL_138_090-133_138_scan[0-9][0-9][0-9].tex"))
harness.write_text(preamble + "\n".join(r"\input{pages/" + p.name + "}" for p in pages)
                   + "\n" + r"\end{document}" + "\n", encoding="utf-8")
print(f"Compile harness now includes {len(pages)} page fragments.")
