#!/usr/bin/env python3
"""Extract precisely the numbered statements included in the manuscript.

Metadata is maintained separately in notes/register_metadata.json. Missing
metadata is an error, so an added theorem cannot silently lose its outcome row.
The statement column retains the exact mathematical LaTeX of each assertion.
"""
from pathlib import Path
import csv
import json
import re

WORK = Path(__file__).resolve().parents[1]
META = json.loads((WORK / "notes" / "register_metadata.json").read_text())
TOKEN = re.compile(r"\\begin\{statement\}|\\input\{([^}]+)\}")

def group(text, pos):
    while text[pos].isspace():
        pos += 1
    if text[pos] != "{":
        raise ValueError(f"Expected a group at {text[pos:pos+80]}")
    start = pos + 1
    depth = 1
    pos += 1
    while depth:
        if text[pos] == "{" and text[pos-1] != "\\":
            depth += 1
        elif text[pos] == "}" and text[pos-1] != "\\":
            depth -= 1
        pos += 1
    return text[start:pos-1], pos

def read_statements(path, stack=()):
    if path in stack:
        raise ValueError(f"Recursive input {path}")
    text = path.read_text()
    for token in TOKEN.finditer(text):
        # Ignore commented input tokens.
        line_start = text.rfind("\n", 0, token.start()) + 1
        if "%" in text[line_start:token.start()]:
            continue
        if token.group(1):
            yield from read_statements(WORK / token.group(1), stack + (path,))
            continue
        identifier, pos = group(text, token.end())
        status, pos = group(text, pos)
        title, pos = group(text, pos)
        end = text.index(r"\end{statement}", pos)
        statement = re.sub(r"\s+", " ", title + ". " + text[pos:end]).strip()
        if identifier not in META:
            raise ValueError(f"No metadata for {identifier}")
        m = META[identifier]
        yield {
            "id": identifier,
            "statement": statement,
            "status": status,
            "where_proved": str(path.relative_to(WORK)) + ": " + identifier,
            "depends_on": m["depends_on"],
            "answers (item or lead)": m["answers"],
            "uses_local_theorem (yes or no, and where)": m["uses_local_theorem"],
            "manuscript_passages (cote; scan)": m["manuscript_passages"],
            "notes": m["notes"],
        }

rows = list(read_statements(WORK / "SECTIONS_OVER_Q_paper.tex"))
ids = [row["id"] for row in rows]
if len(ids) != len(set(ids)):
    raise ValueError("Duplicate numbered statement")
if any(row["status"] not in {"Proved", "Refuted", "Known", "Open"} for row in rows):
    raise ValueError("Unexpected status")
with (WORK / "SECTIONS_OVER_Q_results.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
counts = {s: sum(r["status"] == s for r in rows) for s in ("Proved", "Refuted", "Known", "Open")}
output = f"Extracted {len(rows)} unique numbered statements from active inputs.\nStatus counts: {counts}\nAll rows have explicit item, dependency, local-theorem and manuscript metadata.\n"
(WORK / "code" / "build_register_output.txt").write_text(output)
print(output, end="")
