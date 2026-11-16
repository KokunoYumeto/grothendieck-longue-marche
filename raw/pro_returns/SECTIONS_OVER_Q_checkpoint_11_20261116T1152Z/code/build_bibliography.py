#!/usr/bin/env python3
"""Assemble the inspected bibliography fragments without duplicate keys."""
from pathlib import Path
import re

WORK = Path(__file__).resolve().parents[1]
TARGET = WORK / "SECTIONS_OVER_Q_references.bib"
BASE = WORK / "notes" / "base_references.bib"

def entries(path):
    text = path.read_text()
    starts = list(re.finditer(r"(?m)^@\w+\{([^,]+),", text))
    return {
        match.group(1): text[match.start(): starts[i+1].start() if i+1 < len(starts) else len(text)].strip()
        for i, match in enumerate(starts)
    }

if not BASE.exists():
    old = entries(TARGET)
    keys = ["Prompt2026", "MilneCFT", "SerreGC", "Clark2006"]
    BASE.write_text("\n\n".join(old[key] for key in keys) + "\n")

sources = [BASE] + [WORK / "notes" / f for f in (
    "root_references.bib", "birational_references.bib",
    "legendre_references.bib", "local_agent_references.bib",
    "metabelian_references.bib",
)]
merged = {}
for path in sources:
    for key, entry in entries(path).items():
        if key in merged:
            raise ValueError(f"Duplicate source key {key} in {path}")
        if not re.search(r"\b(?:verified|unverified)\b", entry, re.I):
            raise ValueError(f"Missing verification note for {key}")
        merged[key] = entry
TARGET.write_text("\n\n".join(merged.values()) + "\n")
output = f"Wrote {len(merged)} unique entries from {len(sources)} source fragments.\nEvery entry has a verified/unverified note.\n"
(WORK / "code" / "build_bibliography_output.txt").write_text(output)
print(output, end="")
