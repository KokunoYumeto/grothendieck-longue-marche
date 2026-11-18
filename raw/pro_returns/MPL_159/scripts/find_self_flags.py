#!/usr/bin/env python3
"""List lexical self-flag/question candidates from frozen page text.

This is a text search, not an image reading or a judgment that a step is
unverified. Deleted, inserted, marginal, and uncertain contexts are reported
mechanically so the primary reader can decide what each candidate means.
Question marks within a reading alternative remain candidates, not assertions
that the manuscript definitely contains a question mark.

    python scripts/find_self_flags.py
    python scripts/find_self_flags.py --write

--write creates only diagnostics/self_flag_candidates.tsv. It never alters the
transcription, research notes, inventory, or any event/progress records.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import unicodedata

from check_tex_structure import argument, strip_comments


PATTERNS = {
    "question_mark": r"\?",
    "interrogative_wording": r"\b(?:comment|pourquoi|questions?|quel(?:le)?s?|peut-on|est-il|y en a-t-il)\b",
    "uncertainty_wording": r"\bsans doute\b|\bon suspecte\b|\b(?:presume|devrait|faudrait|suspecte)\b|\bprobabl\w*\b|\bconject\w*\b|\bil semble\b|\bsauf erreur\b|\badmis\b|\badmet\w*\b|\besper\w*\b|\bje (?:crois|pense|ne sais)\b|\bdoute\b",
    "verification_vocabulary": r"\bverifi\w*\b|\ba prouver\b|\ba montrer\b|\ba etablir\b|\ba voir\b",
    "abbreviated_proof_wording": r"\b(?:il est|c'est) (?:facile|immediat|clair)\b|\bon peut (?:montrer|prouver|etablir)\b|\bon verra\b|\b(?:reste|laisse) a (?:montrer|prouver|verifier|voir)\b",
    "existence_qualification": r"\bs'il y en a\b",
    "correction_wording": r"\bfaux\b|\bfaut corriger\b|\ba corriger\b|\berreur\b|\bnon demontre\w*\b",
}


def normalized(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text) if not unicodedata.combining(c)).lower().replace("’", "'")


def editorial_spans(text: str) -> list[tuple[int, int, str]]:
    spans = []
    i = 0
    while i < len(text):
        if text[i] != "\\":
            i += 1
            continue
        match = re.match(r"\\([A-Za-z@]+|.)", text[i:])
        if not match:
            i += 1
            continue
        after = i + len(match.group(0))
        if match.group(1) in {"deleted", "inserted", "margin", "unsure"}:
            body, end = argument(text, after)
            if body is not None:
                start = after
                while text[start].isspace():
                    start += 1
                spans.append((start + 1, end - 1, match.group(1)))
        i = after
    return spans


def collect(root: Path) -> list[dict]:
    rows = []
    patterns = {name: re.compile(pattern) for name, pattern in PATTERNS.items()}
    for path in sorted((root / "pages").glob("MPL_159_159_scan*.tex")):
        raw = path.read_text(encoding="utf-8")
        text = strip_comments(raw)
        spans = editorial_spans(text)
        scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
        offset = 0
        raw_lines = raw.splitlines()
        for line_number, line in enumerate(text.splitlines(keepends=True), 1):
            norm = normalized(line)
            found = []
            for category, pattern in patterns.items():
                for match in pattern.finditer(norm):
                    contexts = sorted({name for start, end, name in spans
                                       if start <= offset + match.start() < end})
                    found.append((category, line[match.start():match.end()], "+".join(contexts) or "unwrapped"))
            if found:
                rows.append({
                    "file": "159", "scan": scan, "tex_line": line_number,
                    "categories": "; ".join(sorted({value[0] for value in found})),
                    "matched_words_or_signs": "; ".join(dict.fromkeys(value[1] for value in found)),
                    "editorial_contexts": "; ".join(sorted({value[2] for value in found})),
                    "source_text": raw_lines[line_number - 1],
                })
            offset += len(line)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    rows = collect(root)
    counts = Counter(category for row in rows for category in row["categories"].split("; "))
    report = {"candidate_source_lines": len(rows), "categories": dict(counts),
              "scope": "Lexical candidates only; no claim that every hit is an unverified manuscript step."}
    if args.write:
        path = root / "diagnostics/self_flag_candidates.tsv"
        path.parent.mkdir(exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["file", "scan", "tex_line", "categories",
                                   "matched_words_or_signs", "editorial_contexts", "source_text"], delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        report["written"] = str(path)
    else:
        report["candidates"] = rows
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
