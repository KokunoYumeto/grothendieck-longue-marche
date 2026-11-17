#!/usr/bin/env python3
"""Record actual per-note searches of the supplied post-freeze context.

This script never reads or writes scan images or transcription files.
It records locations and counts, not copies of the supplied context.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

PACKAGE = "MPL_93_221-236+161-5"
WORK = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", type=Path, required=True)
    args = parser.parse_args()
    context = args.context.resolve()
    files = [
        context / "README.md",
        context / "notes/RESULTS_STATE.md",
        context / "same_cote_93/MPL_93_002-046_notes.md",
        context / "hua_project/README.md",
        context / "hua_project/93.modern.tex",
        context / "hua_project/161-5.modern.tex",
    ]
    if not all(p.is_file() for p in files):
        raise SystemExit("The six supplied context files must be present.")
    note_file = WORK / f"{PACKAGE}_notes.md"
    text = note_file.read_text()
    matches = list(re.finditer(r"^### ([A-Z]\d{2}) — (.+)$", text, re.M))
    ids = [m.group(1) for m in matches]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate note IDs.")
    rows = []
    issues = []
    for ix, match in enumerate(matches):
        end = matches[ix+1].start() if ix+1 < len(matches) else len(text)
        block = text[match.end():end]
        directives = re.findall(r"<!-- context-search: (.*?) -->", block)
        if len(directives) != 1:
            raise SystemExit(f"{match.group(1)}: expected one context-search directive")
        terms = json.loads(directives[0])
        if not isinstance(terms, list) or not terms or not all(isinstance(t, str) and t for t in terms):
            raise SystemExit(f"{match.group(1)}: invalid search terms")
        cmd = ["rg", "--json", "--ignore-case", "--fixed-strings"]
        for term in terms:
            cmd += ["-e", term]
        cmd += [str(p) for p in files]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode not in (0, 1):
            raise SystemExit(result.stderr)
        locations = defaultdict(list)
        term_counts = Counter()
        for line in result.stdout.splitlines():
            event = json.loads(line)
            if event["type"] != "match":
                continue
            data = event["data"]
            path = str(Path(data["path"]["text"]).relative_to(context))
            locations[path].append(data["line_number"])
            line_text = data["lines"]["text"].casefold()
            for term in terms:
                if term.casefold() in line_text:
                    term_counts[term] += 1
        for marker in ("**Location:**", "**Kind:**", "Context comparison:"):
            if marker not in block:
                issues.append(f"{match.group(1)}: missing {marker}")
        if "**Kind:** own idea." in block and "**Confidence:**" not in block:
            issues.append(f"{match.group(1)}: own idea lacks confidence")
        rows.append({
            "note": match.group(1),
            "title": match.group(2),
            "searched_utc": utc(),
            "tool": "rg --json --ignore-case --fixed-strings",
            "terms": terms,
            "matching_lines_per_term": dict(term_counts),
            "match_count": sum(map(len, locations.values())),
            "matched_locations": dict(sorted(locations.items())),
            "scope": "All six supplied context files; full files read separately after freeze.",
            "interpretation": "The note supplies the semantic comparison; keyword matches are not evidence of agreement.",
        })
    output = WORK / "records/context_searches.jsonl"
    output.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    report = {
        "created_utc": utc(),
        "notes_sha256": hashlib.sha256(note_file.read_bytes()).hexdigest(),
        "notes": len(rows),
        "ids": ids,
        "notes_without_any_keyword_match": [r["note"] for r in rows if not r["match_count"]],
        "issues": issues,
        "context_files": {
            str(p.relative_to(context)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files
        },
        "search_record": "records/context_searches.jsonl",
    }
    (WORK / "records/research_notes_validation.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    with (WORK / "progress.log").open("a") as log:
        log.write(f"{utc()} completed actual per-note context searches: {len(rows)} notes, {len(files)} supplied context files; {len(issues)} metadata issues\n")
    print(json.dumps({
        "notes": len(rows), "issues": issues,
        "no_keyword_match": report["notes_without_any_keyword_match"],
        "record": str(output),
        "match_range": [min(r["match_count"] for r in rows), max(r["match_count"] for r in rows)],
    }, indent=2))
    if issues:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
