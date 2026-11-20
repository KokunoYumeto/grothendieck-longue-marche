#!/usr/bin/env python3
"""Deterministic assembly, blind-reading comparison and TeX structure checks.

This script does not recognize text in images and does not decide readings.
Human-readable decisions are supplied by the readers and adjudicator.
"""
from __future__ import annotations
import argparse
import csv
import difflib
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEM = "SP115_CW_156-7"


def tokens(text: str) -> list[str]:
    """Compare every word, TeX command and punctuation token, ignoring whitespace."""
    return re.findall(r"\\[A-Za-z@]+|\\.|[^\W_]+|[^\s]", text, flags=re.UNICODE)


def table(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def compare() -> None:
    reports = []
    for boxfile in sorted((ROOT / "second").glob("*_boxes.tsv")):
        base = boxfile.name.removesuffix("_boxes.tsv")
        firstfile = boxfile.with_name(base + "_first.tsv")
        secondfile = boxfile.with_name(base + "_second.tsv")
        if not firstfile.exists() or not secondfile.exists():
            continue
        boxes = table(boxfile)
        first = {r["box"]: r["reading"] for r in table(firstfile)}
        second = {r["box"]: r["reading"] for r in table(secondfile)}
        wanted = {r["box"] for r in boxes}
        if set(first) != wanted or set(second) != wanted:
            raise ValueError(f"Box coverage mismatch: {base}; first={wanted-set(first)}; second={wanted-set(second)}")
        rows = []
        for box in boxes:
            key = box["box"]
            a, b = tokens(first[key]), tokens(second[key])
            edits = []
            for kind, a0, a1, b0, b1 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                if kind != "equal":
                    edits.append({"operation": kind, "first_tokens": a[a0:a1], "second_tokens": b[b0:b1],
                                  "first_span": [a0, a1], "second_span": [b0, b1]})
            rows.append({"box": key, "kind": box["kind"], "different": bool(edits),
                         "first": first[key], "second": second[key], "edits": edits})
        result = {"page": base, "boxes": len(rows), "different_boxes": sum(r["different"] for r in rows), "rows": rows}
        (ROOT / "second" / (base + "_comparison.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        reports.append({k: result[k] for k in ["page", "boxes", "different_boxes"]})
    print(json.dumps(reports, ensure_ascii=False, indent=2))


def uncomment(text: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())


def check_tex(path: Path) -> dict:
    text = uncomment(path.read_text(encoding="utf-8"))
    stack = []
    errors = []
    lexemes = re.finditer(r"\\begin\{[^}]+\}|\\end\{[^}]+\}|\\[\[\]\(\)]|\\[A-Za-z@]+|\\.|[{}$]", text)
    math_stack = []
    env_stack = []
    for match in lexemes:
        s = match.group()
        if s == "{":
            stack.append(match.start())
        elif s == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at {match.start()}")
        elif s.startswith("\\begin{"):
            env_stack.append(s[7:-1])
        elif s.startswith("\\end{"):
            name = s[5:-1]
            if not env_stack or env_stack[-1] != name:
                errors.append(f"environment mismatch: {s} at {match.start()}")
            else:
                env_stack.pop()
        elif s in ["\\[", "\\("]:
            math_stack.append(s)
        elif s in ["\\]", "\\)"]:
            expected = {"\\]": "\\[", "\\)": "\\("}[s]
            if not math_stack or math_stack[-1] != expected:
                errors.append(f"math delimiter mismatch: {s} at {match.start()}")
            else:
                math_stack.pop()
        elif s == "$":
            if math_stack and math_stack[-1] == "$":
                math_stack.pop()
            else:
                math_stack.append("$")
    if stack:
        errors.append(f"unclosed braces: {stack}")
    if math_stack:
        errors.append(f"unclosed math delimiters: {math_stack}")
    if env_stack:
        errors.append(f"unclosed environments: {env_stack}")
    return {"file": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "unsure": text.count("\\unsure{"), "illegible": text.count("\\illegible{"),
            "deleted": text.count("\\deleted{"), "inserted": text.count("\\inserted{"), "errors": errors}


def assemble() -> None:
    files = sorted((ROOT / "pages").glob("H156-01_156-7_scan*.tex"))
    combined = "\n\n".join(p.read_text().rstrip() for p in files) + "\n"
    (ROOT / (STEM + "_transcription.tex")).write_text(combined, encoding="utf-8")
    print(f"Assembled {len(files)} page fragments.")


def verify() -> None:
    files = sorted((ROOT / "pages").glob("H156-01_156-7_scan*.tex"))
    combined = ROOT / (STEM + "_transcription.tex")
    report = {"checks": [check_tex(p) for p in files + ([combined] if combined.exists() else [])],
              "expected_scans": list(range(2, 10)), "page_count": len(files)}
    if combined.exists():
        text = combined.read_text()
        report["scan_markers"] = [int(x) for x in re.findall(r"\\scanpage\{(\d+)\}", text)]
        report["cotefile_count"] = text.count("\\cotefile{")
        report["concatenation_matches"] = text == "\n\n".join(p.read_text().rstrip() for p in files) + "\n"
    (ROOT / "review" / "tex_structure_check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["assemble", "compare", "verify"])
    action = parser.parse_args().action
    {"assemble": assemble, "compare": compare, "verify": verify}[action]()
