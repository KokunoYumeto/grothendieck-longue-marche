"""Search only the supplied, post-freeze context for each numbered research note.

This script never reads scan images and never writes a transcription file.
The JSONL journal keeps bounded excerpts, full match counts and exact query terms.
"""
from pathlib import Path
import json
import re
import unicodedata
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / "context"
NOTES = ROOT / "MPL_154_001-045_notes.md"
OUT = ROOT / "records/context_searches.jsonl"


def normalized(value):
    value = value.replace("’", "'").replace("−", "-").replace("–", "-")
    return "".join(c for c in unicodedata.normalize("NFKD", value)
                   if not unicodedata.combining(c)).casefold()


def main():
    text = NOTES.read_text()
    entries = list(re.finditer(r"^### ([A-Z]\d{2}) — (.+)$", text, re.M))
    files = sorted(p for p in CONTEXT.rglob("*")
                   if p.is_file() and p.suffix in {".md", ".tex"})
    assert len(files) == 6, "Search scope must remain the six supplied context files"
    sources = [(p, p.read_text().splitlines()) for p in files]
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    rows = []
    for i, match in enumerate(entries):
        end = entries[i + 1].start() if i + 1 < len(entries) else len(text)
        block = text[match.end():end]
        tag = re.search(r"<!-- search: (.*?) -->", block)
        assert tag, f"Missing context-search terms for {match.group(1)}"
        terms = [v.strip() for v in tag.group(1).split(";") if v.strip()]
        searches = []
        total = 0
        for term in terms:
            needle = normalized(term)
            matches = []
            count = 0
            for path, lines in sources:
                retained = 0
                for line_number, line in enumerate(lines, 1):
                    haystack = normalized(line)
                    if needle not in haystack:
                        continue
                    count += 1
                    if retained < 2:
                        pos = haystack.find(needle)
                        start = max(0, pos - 100)
                        excerpt = line[start:start + 440]
                        matches.append({
                            "file": str(path.relative_to(CONTEXT.parent)),
                            "line": line_number,
                            "excerpt": excerpt,
                            "excerpt_is_partial": start > 0 or start + 440 < len(line),
                        })
                        retained += 1
            total += count
            searches.append({"term": term, "matching_lines": count,
                             "retained_matches_max_two_per_file": matches})
        rows.append({"note": match.group(1), "title": match.group(2),
                     "searched_utc": timestamp,
                     "scope": [str(p.relative_to(CONTEXT.parent)) for p in files],
                     "normalization": "casefold, accents removed, apostrophe/dash variants",
                     "queries": searches, "total_matching_lines_with_repetition": total,
                     "interpretation": "Matches are retrieval leads; the note states the verified relation and its limits."})
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    print(json.dumps({"notes_searched": len(rows), "context_files": len(files),
                      "zero_hit_notes": [r["note"] for r in rows if not r["total_matching_lines_with_repetition"]],
                      "journal": str(OUT), "searched_utc": timestamp}, ensure_ascii=False))


if __name__ == "__main__":
    main()
