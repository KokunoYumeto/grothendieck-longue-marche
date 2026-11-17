#!/usr/bin/env python3
"""Assemble doubts mechanically, without resolving readings.

Required inputs: root-written notation and legibility prose, plus an explicit
default-confidence policy. Page TeX and page JSON files are read-only.
Example:
  python records/assemble_doubts.py --notation records/notation_preamble.md \
    --legibility records/legibility_note.md --default-confidence low
"""
import argparse
import html
import json
import re
from collections import defaultdict
from pathlib import Path

PREFIX = "MPL_64_002-039"
CONFIDENCES = {"high", "medium", "low"}

def without_comments(text):
    result = list(text)
    i = 0
    while i < len(result):
        if result[i] == "\\":
            i += 2
        elif result[i] == "%":
            while i < len(result) and result[i] != "\n":
                result[i] = " "
                i += 1
        else:
            i += 1
    return "".join(result)

def argument(text, offset):
    while offset < len(text) and text[offset].isspace():
        offset += 1
    if offset >= len(text) or text[offset] != "{":
        raise ValueError("Expected a braced macro argument")
    start, depth = offset, 1
    offset += 1
    while offset < len(text):
        if text[offset] == "\\":
            offset += 2
            continue
        if text[offset] == "{":
            depth += 1
        elif text[offset] == "}":
            depth -= 1
            if depth == 0:
                return text[start+1:offset], offset+1
        offset += 1
    raise ValueError("Unclosed macro argument")

def alternatives(value):
    pieces = []
    start = depth = i = 0
    while i < len(value):
        if value[i] == "\\":
            i += 2
            continue
        if value[i] == "{":
            depth += 1
        elif value[i] == "}":
            depth -= 1
        elif value[i] == "|" and depth == 0:
            pieces.append(value[start:i].strip())
            start = i+1
        i += 1
    pieces.append(value[start:].strip())
    return pieces[0], " | ".join(pieces[1:])

def current_markers(path, macro="unsure"):
    text = without_comments(path.read_text(encoding="utf-8"))
    result = []
    for found in re.finditer(r"\\" + re.escape(macro) + r"(?![A-Za-z])", text):
        value, _ = argument(text, found.end())
        reading, alt = alternatives(value)
        result.append({"line": text.count("\n", 0, found.start())+1,
                       "argument": value, "reading": reading, "alternatives": alt})
    return result

def recorded_doubt(value):
    if isinstance(value, dict):
        return {"position": str(value.get("position", value.get("line", ""))),
                "reading": str(value.get("reading", "")),
                "alternatives": str(value.get("alternatives", value.get("alternative", ""))),
                "confidence": str(value.get("confidence", ""))}
    if isinstance(value, list) and len(value) == 4:
        return dict(zip(("position", "reading", "alternatives", "confidence"), map(str, value)))
    raise ValueError("Unsupported recorded-doubt structure")

def cell(value, code=False):
    value = html.escape(str(value)).replace("|", "&#124;").replace("\n", " ⏎ ")
    return f"<code>{value}</code>" if code and value else value

def table(rows):
    output = ["| Cote | Scan | Approximate line or position | Reading | Alternatives | Confidence |",
              "|---|---|---|---|---|---|"]
    for scan, location, reading, alt, confidence in rows:
        output.append("| 64 | " + str(scan) + " | " + cell(location) + " | "
                      + cell(reading, True) + " | " + cell(alt, True)
                      + " | " + cell(confidence) + " |")
    return "\n".join(output)

def resolve(root, value):
    path = Path(value)
    return path if path.is_absolute() else root/path

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--notation", required=True)
    parser.add_argument("--legibility", required=True)
    parser.add_argument("--default-confidence", required=True, choices=sorted(CONFIDENCES))
    parser.add_argument("--output")
    parser.add_argument("--report")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    notation = resolve(root,args.notation).read_text(encoding="utf-8").rstrip()
    legibility = resolve(root,args.legibility).read_text(encoding="utf-8").rstrip()
    if not notation or not legibility:
        raise ValueError("The primary reader's notation and legibility inputs must be nonempty")
    record_rows = {}
    abbreviations = defaultdict(set)
    for path in sorted((root/"records").glob("scan[0-9][0-9][0-9].json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        scan = int(raw.get("scan",path.stem.removeprefix("scan")))
        record_rows[scan] = [recorded_doubt(v) for v in raw.get("doubts",[])]
        for value in raw.get("abbreviations",[]):
            if not isinstance(value,list) or len(value)!=2:
                raise ValueError(f"{path.name}: unsupported abbreviation record")
            abbreviations[tuple(map(str,value))].add(scan)
    active, history, conflicts, illegible = [], [], [], []
    illegible_word_estimate = 0
    historical_count = unmatched_count = page_count = 0
    for path in sorted((root/"pages").glob(f"{PREFIX}_64_scan[0-9][0-9][0-9].tex")):
        scan = int(path.stem[-3:])
        page_count += 1
        markers = current_markers(path)
        for marker in current_markers(path,"illegible"):
            count = marker["argument"]
            if count.strip().isdigit():
                illegible_word_estimate += int(count.strip())
            illegible.append((scan,f"TeX line {marker['line']}; estimated {count} words",
                              "\\illegible{"+count+"}","",args.default_confidence))
        records = record_rows.get(scan,[])
        current_keys = {(m["reading"].strip(),m["alternatives"].strip()) for m in markers}
        for marker in markers:
            key = (marker["reading"].strip(),marker["alternatives"].strip())
            matches = [r for r in records if (r["reading"].strip(),r["alternatives"].strip())==key]
            values = {r["confidence"] for r in matches if r["confidence"] in CONFIDENCES}
            if len(values)==1:
                confidence = next(iter(values))
            else:
                confidence = args.default_confidence
                unmatched_count += 1
                if len(values)>1:
                    conflicts.append({"scan":scan,"line":marker["line"],
                                      "recorded_confidences":sorted(values)})
            active.append((scan,f"TeX line {marker['line']}",marker["reading"],
                           marker["alternatives"],confidence))
        for index,row in enumerate(records,1):
            key = (row["reading"].strip(),row["alternatives"].strip())
            if key in current_keys:
                label = "Recorded doubt; exact current marker match"
            else:
                label = "Historical record; no exact current marker match"
                historical_count += 1
            location = f"{label}; record {index}; {row['position']}"
            confidence = row["confidence"] if row["confidence"] in CONFIDENCES else args.default_confidence
            history.append((scan,location,row["reading"],row["alternatives"],confidence))
    abbreviation_lines = ["| Abbreviation | Recorded possible expansion | Scans |","|---|---|---|"]
    for (abbr,expansion),scans in sorted(abbreviations.items(),key=lambda item:item[0]):
        abbreviation_lines.append(f"| {cell(abbr,True)} | {cell(expansion)} | "
                                  +", ".join(map(str,sorted(scans)))+" |")
    sections = [
        notation,
        "# Current reading doubts\n\n"
        "Every current `\\unsure{...}` marker is listed below, including nested-brace "
        "arguments. Approximate lines refer to the individual page TeX files. "
        "Exact recorded reading/alternative pairs supply their recorded confidence; "
        f"otherwise the primary reader's explicit assembly policy assigns **{args.default_confidence}**. "
        "This mechanical policy does not resolve any reading.\n\n"+table(active),
        "# Illegible spans\n\n"
        "Every current illegible-word marker is retained below, including markers within "
        "deletions. Word counts are the primary reader's estimates recorded in the "
        "transcription; the assembler does not verify or change them.\n\n"+table(illegible),
        "# Recorded doubts and reading history\n\n"
        "All page-record doubts are retained here. “Historical record” means that "
        "the recorded reading/alternative pair has no exact match among that page's "
        "current `\\unsure` markers. This string comparison does not establish "
        "that a doubt has been resolved; abbreviated records can also fail an exact match.\n\n"
        +table(history),
        "# Abbreviations\n\n"
        "Expansions below are the page records' proposed expansions. Different recorded "
        "expansions are preserved without choosing between them.\n\n"+"\n".join(abbreviation_lines),
        "# Legibility assessment\n\n"+legibility,
    ]
    destination = resolve(root,args.output or f"{PREFIX}_doubts.md")
    report = {"pages":page_count,"current_markers":len(active),"recorded_doubts":len(history),
              "illegible_spans":len(illegible),"estimated_illegible_words":illegible_word_estimate,
              "historical_no_exact_match":historical_count,
              "current_markers_using_default_confidence":unmatched_count,
              "explicit_default_confidence":args.default_confidence,
              "conflicting_exact_record_confidences":conflicts,
              "abbreviation_expansion_pairs":len(abbreviations),
              "output":str(destination),"dry_run":args.dry_run}
    if not args.dry_run:
        destination.write_text("\n\n".join(sections)+"\n",encoding="utf-8")
        if args.report:
            resolve(root,args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
