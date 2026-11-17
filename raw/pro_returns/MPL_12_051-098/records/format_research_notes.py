#!/usr/bin/env python3
"""Format only the post-freeze research notes; never open a transcription file."""
from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "MPL_12_051-098_notes.md"
text = path.read_text(encoding="utf-8")
# Literal reading alternatives belong in mathematical notation, not table delimiters.
lines = []
for line in text.splitlines():
    if line.startswith("|"):
        line = re.sub(
            r"\\\((.*?)\\\)",
            lambda m: r"\(" + m.group(1).replace("|", r"\mid ") + r"\)",
            line,
        )
    lines.append(line)
text = "\n".join(lines) + "\n"
replacements = {
    "published27October2026": "published 27 October 2026",
    "source12.pdf": "source 12.pdf",
    "Definition5.1": "Definition 5.1",
    "Theorem4.6": "Theorem 4.6",
    "Theorem9.1": "Theorem 9.1",
    "Theorems6.3.3,6.4.1": "Theorems 6.3.3, 6.4.1",
    "Theorem1]": "Theorem 1]",
    "Corollary1]": "Corollary 1]",
    "Corollary2;": "Corollary 2;",
    "numbers13–18": "numbers 13–18",
    "Pages1–67": "Pages 1–67",
    "unavailable24-page": "unavailable 24-page",
    "faces:34 text,2 cancelled_draft,2 reused_typed,1 cover": "faces: 34 text, 2 cancelled_draft, 2 reused_typed, 1 cover",
    "occurrences and3": "occurrences and 3",
    "and11.9.3(ii)": "and 11.9.3(ii)",
    "RS’s18/059": "RS’s 18/059",
    "on16/047": "on 16/047",
    "later18/059": "later 18/059",
    "current051–096": "current 051–096",
}
for old, new in replacements.items():
    text = text.replace(old, new)
text = re.sub(r"\b(scan|scans|Author|foliation)(?=\d)", r"\1 ", text)
path.write_text(text, encoding="utf-8")
print("Formatted research notes only.")
