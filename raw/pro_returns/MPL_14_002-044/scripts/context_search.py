#!/usr/bin/env python3
"""Record reproducible post-freeze context searches, without changing source files."""
import argparse
import json
import re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--context", type=Path, required=True)
ap.add_argument("--plan", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
args = ap.parse_args()
plan = json.loads(args.plan.read_text())
names = ["MPL_16+47+54+44_transcription.tex", "MPL_16+47+54+44_notes.md", "MPL_16+47+54+44_doubts.md", "README.md", "notes/RESULTS_STATE.md"]
sources = {name: (args.context / name).read_text().splitlines() for name in names}
out = ["# Post-freeze context search ledger", "", "Queries are independent of the frozen transcription; excerpts retain the context's unreviewed status. A zero count records the scope of a search, not a theorem of absence. Full primary manuscripts were read separately before the context was opened.", ""]
for item in plan:
    pat = re.compile(item["pattern"], re.I)
    out += [f"## {item['id']}", "", f"Pattern: `{item['pattern']}`", ""]
    for name, lines in sources.items():
        hits = []
        cote = scan = "—"
        for i, line in enumerate(lines, 1):
            c = re.search(r"\\cotefile\{(\d+)\}", line)
            s = re.search(r"\\scanpage\{(\d+)\}", line)
            h = re.match(r"## (\d+):(\d+):", line)
            if c:
                cote = c.group(1)
            if s:
                scan = s.group(1)
            if h:
                cote, scan = h.groups()
            if pat.search(line):
                hits.append((i, cote, scan, line))
        out += [f"### {name}: {len(hits)} matching lines", ""]
        for i, cote, scan, line in hits[:60]:
            excerpt = line[:520] + (" … [excerpt shortened]" if len(line) > 520 else "")
            anchor = f"cote {cote}, scan {scan}; " if name.endswith("_transcription.tex") else ""
            out.append(f"- {anchor}line {i}: {excerpt}")
        if len(hits) > 60:
            out.append(f"- {len(hits) - 60} additional matches; refine the recorded pattern for targeted reading.")
        out.append("")
args.output.write_text("\n".join(out))
print(f"Recorded {len(plan)} searches in {args.output}")
