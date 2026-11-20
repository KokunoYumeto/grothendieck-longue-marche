#!/usr/bin/env python3
"""List every explicit C uncertainty macro as a coverage aid; no OCR/inference.

Usage: extract_c_marks.py PACKETS_ROOT [SCAN ...]
Writes C_marked_loci.md beside each selected packet's unchanged C.tex.
"""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
packets = [root / f"scan{int(n):03d}" for n in sys.argv[2:]] if len(sys.argv) > 2 else sorted(root.glob("scan[0-9][0-9][0-9]"))
for packet in packets:
    s = (packet / "C.tex").read_text()
    rows = []
    for i, match in enumerate(re.finditer(r"\\(?:unsure|illegible)\{", s), 1):
        j = match.end()
        level = 1
        while j < len(s) and level:
            if s[j] in "{}":
                slash_count = 0
                k = j - 1
                while k >= 0 and s[k] == "\\":
                    slash_count += 1
                    k -= 1
                if slash_count % 2 == 0:
                    level += 1 if s[j] == "{" else -1
            j += 1
        assert level == 0, (packet, match.start())
        line = s.count("\n", 0, match.start()) + 1
        context = s[max(0, match.start() - 90):min(len(s), j + 90)].replace("\n", " ")
        rows.append(f"## C{i:03d} — C.tex line {line}\n\nExact mark: `{s[match.start():j]}`\n\n```tex\n{context}\n```\n")
    header = "# Explicit uncertainty marks in witness C\n\nThis mechanically extracted list supplements C_prior_questions.md. It makes no reading decision. Several marks may belong to the same physical locus and may share one crop/outcome, but every mark requires an explicit resolution or retention.\n\n"
    (packet / "C_marked_loci.md").write_text(header + ("\n".join(rows) if rows else "C.tex contains no unsure or illegible macro.\n"))
    print(f"{packet.name}: {len(rows)} explicit marks")
