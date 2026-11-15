#!/usr/bin/env python3
"""Check the standing register against frozen TeX; never edit a page."""
from pathlib import Path
import hashlib
import json
import re

WORK = Path(__file__).resolve().parents[1]
REGISTER = WORK / "records/research_standing_register.md"


def cells(row):
    return row.strip("|").strip().split(" | ")


def uncode(value):
    assert value[0] == value[-1] == chr(96), value
    return value[1:-1].replace(r"\|", "|")


def main():
    register = REGISTER.read_text()
    pages = {
        int(path.stem[-3:]): path
        for path in sorted((WORK / "pages").glob("*.tex"))
    }
    assert len(pages) == 40
    texts = {scan: path.read_text() for scan, path in pages.items()}
    counts = {}
    for prefix, expected_count in (("S", 86), ("T", 24)):
        rows = [
            row for row in register.splitlines()
            if re.match(r"^\| " + prefix + r"\d+ \|", row)
        ]
        for row in rows:
            label, scan, line, quote = cells(row)[:4]
            source = texts[int(scan)].splitlines()[int(line) - 1]
            assert uncode(quote) in source, (label, scan, line, quote)
        assert len(rows) == expected_count
        counts[prefix] = len(rows)

    hash_entries = 0
    for line in (WORK / "records/frozen_hashes.txt").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        actual = hashlib.sha256((WORK / relative).read_bytes()).hexdigest()
        assert actual == expected, relative
        hash_entries += 1

    marks_section = register.split("## 4.", 1)[1].split("## 5.", 1)[0]
    mark_rows = [
        row for row in marks_section.splitlines()
        if re.match(r"^\| \d{3} \|", row)
    ]
    for row in mark_rows:
        scan, line_info, mark = cells(row)[:3]
        mark_line = int(line_info.split(";", 1)[0])
        assert uncode(mark) == texts[int(scan)].splitlines()[mark_line - 1]
    assert len(mark_rows) == 40
    assert sum(text.count(r"\mspage{") for text in texts.values()) == 40

    # Count every occurrence, including nested deletions, and locate its span.
    deletions = []
    for scan, text in texts.items():
        for match in re.finditer(re.escape(r"\deleted{"), text):
            start = match.end()
            end = start
            depth = 1
            while depth:
                char = text[end]
                depth += (char == "{") - (char == "}")
                end += 1
            start_line = text.count("\n", 0, match.start()) + 1
            end_line = text.count("\n", 0, end - 1) + 1
            deletions.append((scan, start_line, end_line, text[start:end - 1]))
    deletion_rows = [
        row for row in register.splitlines()
        if re.match(r"^\| D\d+ \|", row)
    ]
    assert len(deletions) == len(deletion_rows) == 155
    for number, (row, expected) in enumerate(zip(deletion_rows, deletions), 1):
        label, scan, span, quote = cells(row)[:4]
        expected_scan, first, last, content = expected
        expected_span = str(first) if first == last else f"{first}–{last}"
        assert label == f"D{number:03}"
        assert int(scan) == expected_scan and span == expected_span, label
        flattened = content.replace("\n", " ⏎ ")
        assert uncode(quote) == flattened[:180], (label, quote, flattened[:180])

    assert "BACKTICK" not in register
    result = {
        "page_files": len(pages),
        "status_rows": counts["S"],
        "typescript_rows": counts["T"],
        "manuscript_page_marks": len(mark_rows),
        "deletion_occurrences_including_nested": len(deletions),
        "all_status_quotes_literal": True,
        "all_deletion_quotes_and_spans_exact": True,
        "frozen_hash_entries_unchanged": hash_entries,
    }
    destination = WORK / "records/research_standing_register_validation.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
