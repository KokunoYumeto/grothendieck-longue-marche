#!/usr/bin/env python3
"""Reproduce per-note searches of the supplied, post-freeze context.

This script reads text sources only. It never opens scan images, performs OCR,
or writes a transcription. Its output lists locators, not reproduced sources.
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
CONTEXT = WORK / "context"
NOTES = ROOT / "MPL_57_089-132_notes.md"
FILES = sorted(
    p for p in CONTEXT.rglob("*")
    if p.is_file() and (p.suffix in {".md", ".tex"} or p.name == "oda_text.txt")
)


def locators(path: Path):
    cote = scan = None
    heading = ""
    pdf_page = 1
    table = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if path.name == "oda_text.txt":
            pdf_page += line.count("\f")
            heading = (
                "PDF page 1, bibliographic cover" if pdf_page == 1
                else f"PDF page {pdf_page}, printed page {pdf_page + 61}"
            )
        m = re.search(r"\\cotefile\{([^}]+)\}", line)
        if m:
            cote, scan = m.group(1), None
        m = re.search(r"\\scanpage\{([^}]+)\}", line)
        if m:
            scan = m.group(1)
        if re.match(r"#{1,4}\s", line):
            heading = re.sub(r"^#+\s*", "", line)[:125]
        if re.match(r"\\(?:sub)?section\*?\{", line):
            heading = line.strip()[:150]
        table[number] = (
            f"cote {cote}, scan {scan}" if cote and scan
            else heading or "opening material"
        )
    return table


def entries(text: str):
    matches = list(re.finditer(r"^### ([A-Z]\d{2}[ab]?) — (.+)$", text, re.M))
    out = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[match.end():end]
        search = re.search(r"^\*\*Search:\*\* (.+)$", block, re.M)
        if not search:
            raise ValueError(f"No search terms in {match.group(1)}")
        out.append({
            "id": match.group(1),
            "title": match.group(2),
            "terms": [v.strip() for v in search.group(1).split("|") if v.strip()],
            "type": "substantive note",
        })
    for line in text.splitlines():
        if not re.match(r"\| [ST]\d{2} —", line):
            continue
        # The title row has an escaped literal pipe, so protect it before split.
        cells = [v.strip() for v in line.replace(r"\|", "⟦PIPE⟧").split("|")[1:-1]]
        if len(cells) != 4:
            raise ValueError(f"Unexpected standing-table layout: {line}")
        ident = cells[0].split(" —", 1)[0]
        out.append({
            "id": ident,
            "title": cells[0].replace("⟦PIPE⟧", "|"),
            "terms": [v.strip() for v in cells[3].split(";") if v.strip()],
            "type": "standing-question row",
        })
    if len({entry["id"] for entry in out}) != len(out):
        raise ValueError("Duplicate note/standing-row identifier")
    return out


def priority(entry, path, line, locator):
    ident = entry["id"]
    group = ident[0]
    # Prefer the directly corresponding Hua passage while preserving a full
    # corpus search and its total counts.
    windows = {
        "W": (1270, 1750), "A": (1270, 1399), "B": (1399, 1538),
        "C": (1538, 1588), "D": (1588, 1651), "E": (1651, 1706),
        "F": (1, 105), "S": (1270, 1750), "T": (1270, 1750),
    }
    if path.name == "57.modern.tex":
        low, high = windows[group]
        return (0 if low <= line <= high else 1, line)
    if path.name.endswith("_transcription.tex"):
        if group == "W":
            preferred = "cote 47" if ident in {"W01", "W02"} else "cote 44"
        else:
            preferred = {"A": "cote 54", "B": "cote 44",
                         "C": "cote 54", "D": "cote 16",
                         "E": "cote 47", "F": "cote 16"}.get(group, "cote 47")
        return (0 if preferred in locator else 1, line)
    return (0, line)


def main():
    text = NOTES.read_text(encoding="utf-8")
    note_entries = entries(text)
    maps = {str(p): locators(p) for p in FILES}
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report = [
        "# Per-note context searches", "", f"Generated: {stamp}", "",
        "All searches occurred after the transcription freeze. The corpus is "
        "limited to the supplied context text files and text extracted from the "
        "supplied Oda paper; no scan OCR or other Library material is used.",
        "",
        "Method: ripgrep, case-insensitive fixed-string OR matching, one search "
        "for each substantive note and each standing-question row. Counts are "
        "matching lines, not mathematical occurrences; all matching locators "
        "are retained in context_note_searches.json. This Markdown report gives "
        "up to six locators per file, preferring the relevant Hua section.",
        "",
        "The substantive note itself supplies the file/scan comparison and "
        "whether the current pages add, restate, differ or leave no close match. "
        "A zero hit is not proof that an equivalent formulation is absent.",
        "",
        "## Corpus", "",
    ]
    report += [f"- {p.relative_to(WORK)}" for p in FILES]
    report.append("")
    raw = {"generated_utc": stamp, "method": "rg -n -i -F, OR across terms",
           "corpus": [str(p.relative_to(WORK)) for p in FILES], "entries": []}
    for entry in note_entries:
        args = ["rg", "-n", "-i", "-F", "--no-heading", "--with-filename"]
        for term in entry["terms"]:
            args += ["-e", term]
        args += [str(p) for p in FILES]
        result = subprocess.run(args, text=True, capture_output=True, check=False)
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr)
        found = defaultdict(list)
        term_counts = Counter()
        # pdftotext emits form-feed characters inside physical text lines;
        # splitlines() would split those and lose ripgrep's file/line prefix.
        for line in result.stdout.split("\n"):
            if not line:
                continue
            pathstr, lineno, snippet = line.split(":", 2)
            number = int(lineno)
            for term in entry["terms"]:
                if term.casefold() in snippet.casefold():
                    term_counts[term] += 1
            found[pathstr].append({
                "line": number,
                "locator": maps[pathstr].get(number, ""),
            })
        record = dict(entry)
        record["matching_lines"] = sum(len(v) for v in found.values())
        record["term_matching_lines"] = {t: term_counts[t] for t in entry["terms"]}
        record["files"] = {
            str(Path(p).relative_to(WORK)): v for p, v in found.items()
        }
        raw["entries"].append(record)
        report += [
            f"## {entry['id']} — {entry['title']}", "",
            f"Type: {entry['type']}.",
            "Search: " + " | ".join(entry["terms"]) + ".",
            f"Total matching lines: {record['matching_lines']}.", "",
            "Per-term matching-line counts: " +
            "; ".join(f"{t}: {term_counts[t]}" for t in entry["terms"]) + ".", "",
        ]
        for p in FILES:
            hits = found.get(str(p), [])
            if not hits:
                report.append(f"- {p.relative_to(WORK)}: 0 matching lines.")
                continue
            selected = sorted(hits, key=lambda h: priority(entry, p, h["line"], h["locator"]))[:6]
            refs = "; ".join(
                f"line {h['line']} ({h['locator'].replace('|', '/')})" for h in selected
            )
            report.append(f"- {p.relative_to(WORK)}: {len(hits)} matching lines; {refs}.")
        report.append("")
    dest = ROOT / "records"
    (dest / "context_note_searches.md").write_text("\n".join(report)+"\n", encoding="utf-8")
    (dest / "context_note_searches.json").write_text(
        json.dumps(raw, ensure_ascii=False, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps({
        "entries": len(note_entries),
        "substantive_notes": sum(e["type"] == "substantive note" for e in note_entries),
        "standing_rows": sum(e["type"] == "standing-question row" for e in note_entries),
        "context_files": len(FILES),
        "zero_hit_entries": [e["id"] for e in raw["entries"] if not e["matching_lines"]],
        "generated_utc": stamp,
    }))


if __name__ == "__main__":
    main()
