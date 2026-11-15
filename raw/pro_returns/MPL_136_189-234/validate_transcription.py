"""Structural checks only; this script does not read or interpret scan images."""
from pathlib import Path
import collections
import csv
import re

ROOT = Path(__file__).resolve().parent
PREFIX = "MPL_136_189-234"
EXPECTED = set(range(189, 235)) - {214}

def validate():
    paths = sorted((ROOT / "pages").glob("*.tex"))
    assert {int(re.search(r"scan(\d+)", p.name)[1]) for p in paths} == EXPECTED
    for p in paths:
        text = p.read_text()
        scan = int(re.search(r"scan(\d+)", p.name)[1])
        assert re.findall(r"\\scanpage\{(\d+)\}", text) == [str(scan)], p.name
        stack = []
        i = 0
        while i < len(text):
            c = text[i]
            if c == "\\":
                # A control symbol, including escaped braces, consumes two characters.
                if i + 1 < len(text) and not text[i + 1].isalpha():
                    i += 2
                    continue
            if c == "%":
                end = text.find("\n", i)
                i = len(text) if end < 0 else end
                continue
            if c == "{":
                stack.append(i)
            elif c == "}":
                assert stack, (p.name, "extra closing brace", text[:i].count("\n") + 1)
                stack.pop()
            i += 1
        assert not stack, (p.name, "unclosed braces", [text[:i].count("\n") + 1 for i in stack])
        environments = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
            if m[1] == "begin":
                environments.append(m[2])
            else:
                assert environments and environments.pop() == m[2], (p.name, m[0])
        assert not environments, (p.name, environments)
        assert len(re.findall(r"(?<!\\)\$", text)) % 2 == 0, (p.name, "odd dollar count")
        assert len(re.findall(r"(?<!\\)\\\[", text)) == len(re.findall(r"(?<!\\)\\\]", text)), (p.name, "display delimiters")
        assert r"\documentclass" not in text
    rows = list(csv.DictReader((ROOT / f"{PREFIX}_inventory.csv").open()))
    assert {int(r["scan"]) for r in rows} == EXPECTED
    kinds = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
    sheet_kinds = {"text", "reused_typed", "cancelled_draft", "cover"}
    for r in rows:
        assert r["transcribed"] == "yes" and r["cote"] == "136"
        assert r["kind"] in kinds and r["sheet_kind"] in sheet_kinds
    for scan in EXPECTED:
        these = [r for r in rows if int(r["scan"]) == scan]
        assert [int(r["element"]) for r in these] == list(range(1, len(these) + 1)), scan
    log = (ROOT / "progress.log").read_text()
    assert set(map(int, re.findall(r"^136 scan (\d+) done ", log, re.M))) == EXPECTED
    assert set(map(int, re.findall(r"^scan (\d+) audited ", log, re.M))) == EXPECTED
    combined = "\n".join(p.read_text() for p in paths)
    assert combined.startswith("\\cotefile{136}\n\\scanpage{189}")
    assert combined.count(r"\cotefile{") == 1
    combined_path = ROOT / f"{PREFIX}_transcription.tex"
    if "transcription frozen " in log:
        assert combined_path.read_text() == combined, "Frozen combined file differs from page concatenation"
    else:
        combined_path.write_text(combined)
    print(f"Validated {len(paths)} pages, {len(rows)} inventory elements, and both reading logs.")
    print("Sheet counts:", dict(collections.Counter(next(r['sheet_kind'] for r in rows if int(r['scan']) == scan) for scan in sorted(EXPECTED))))

if __name__ == "__main__":
    validate()
