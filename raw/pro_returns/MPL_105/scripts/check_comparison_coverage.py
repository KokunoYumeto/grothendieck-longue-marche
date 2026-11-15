#!/usr/bin/env python3
"""Check comparison heading IDs without interpreting the notes.

Usage: python scripts/check_comparison_coverage.py [--root WORK_DIRECTORY]

Every comparison heading must have the exact Markdown shape:
    ### <ID> — <nonempty title>

Only headings with the STRATA, PATHS, BISITE, RESIDUE or NEW_RESULTS ID prefix are
treated as comparison headings. Other note IDs, including Rnn, Snn, Tnn and Qnn,
are ignored. Code fences are ignored. This script writes reports only; it never changes the
notes, page fragments, combined transcription, frozen hashes, or progress log.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


COMPARISON_PREFIXES = ("STRATA", "PATHS", "BISITE", "RESIDUE", "NEW_RESULTS")
COMPARISON_START = re.compile(r"^(?:" + "|".join(COMPARISON_PREFIXES) + r")(?=$|[ \t])")


def visible_lines(text):
    fence_character = None
    fence_length = 0
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            sequence = fence.group(1)
            if fence_character is None:
                fence_character = sequence[0]
                fence_length = len(sequence)
            elif sequence[0] == fence_character and len(sequence) >= fence_length:
                fence_character = None
            continue
        if fence_character is None:
            yield number, line


def save_reports(root, report):
    records = root / "records"
    records.mkdir(parents=True, exist_ok=True)
    json_path = records / "comparison_coverage.json"
    md_path = records / "comparison_coverage.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Comparison heading coverage", "", f"Generated: {report['generated_utc']}", "",
        f"Status: **{report['status']}**.", "",
        "This report checks Markdown heading structure and ID coverage only, restricted to the STRATA, PATHS, BISITE, RESIDUE and NEW_RESULTS prefixes. Other note headings are ignored. It does not evaluate the content or adequacy of any comparison. No manuscript image or context source was opened.", "",
    ]
    if report.get("notes_sha256"):
        lines.extend([f"Notes SHA-256: `{report['notes_sha256']}`.", ""])
    lines.extend(["| ID group | Expected | Exactly once | Missing | Repeated |", "|---|---:|---:|---:|---:|"])
    for group, counts in report.get("groups", {}).items():
        lines.append(f"| {group} | {counts['expected']} | {counts['exactly_once']} | {counts['missing']} | {counts['repeated']} |")
    lines.append("")
    if report.get("status") == "notes_absent":
        lines.extend(["`MPL_105_notes.md` was absent; no note headings were inspected. Run the checker again after the notes are written.", ""])
    if report.get("specification_errors"):
        lines.extend(["## Specification errors", ""])
        lines.extend(f"- {error}" for error in report["specification_errors"])
        lines.append("")
    if report.get("missing_ids"):
        lines.extend(["## Missing IDs", "", ", ".join(f"`{identifier}`" for identifier in report["missing_ids"]), ""])
    if report.get("duplicate_ids"):
        lines.extend(["## Repeated expected IDs", ""])
        for identifier, locations in report["duplicate_ids"].items():
            lines.append(f"- `{identifier}`: lines {', '.join(map(str, locations))}.")
        lines.append("")
    if report.get("unexpected_ids"):
        lines.extend(["## Unexpected IDs", ""])
        for identifier, locations in report["unexpected_ids"].items():
            lines.append(f"- `{identifier}`: lines {', '.join(map(str, locations))}.")
        lines.append("")
    if report.get("malformed_headings"):
        lines.extend(["## Malformed comparison headings", ""])
        for item in report["malformed_headings"]:
            lines.append(f"- Line {item['line']}, `{item['id']}`: {item['issue']}.")
        lines.append("")
    if report.get("status") == "pass":
        lines.extend(["Every expected ID occurs in exactly one correctly formed comparison heading. No unexpected comparison IDs or malformed comparison headings were detected.", ""])
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return [str(json_path), str(md_path)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    expected_path = root / "records/expected_comparison_ids.json"
    notes_path = root / "MPL_105_notes.md"
    report = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "status": "specification_error", "specification_errors": [], "groups": {},
        "missing_ids": [], "duplicate_ids": {}, "unexpected_ids": {},
        "malformed_headings": [], "expected_heading_lines": {},
    }
    try:
        expected_bytes = expected_path.read_bytes()
        groups = json.loads(expected_bytes.decode("utf-8"))
        if not isinstance(groups, dict) or not groups:
            raise ValueError("Expected a nonempty group-to-ID-list object")
        for name, identifiers in groups.items():
            if not isinstance(identifiers, list) or any(not isinstance(i, str) or not i or i != i.strip() for i in identifiers):
                raise ValueError(f"Invalid ID list for group {name}")
        ordered_ids = [identifier for identifiers in groups.values() for identifier in identifiers]
        repeated_spec = [identifier for identifier, count in collections.Counter(ordered_ids).items() if count != 1]
        if repeated_spec:
            raise ValueError("Repeated IDs in the expected specification: " + ", ".join(repeated_spec))
        report["expected_specification_sha256"] = hashlib.sha256(expected_bytes).hexdigest()
        report["expected_total"] = len(ordered_ids)
    except (OSError, UnicodeError, ValueError) as exc:
        report["specification_errors"].append(str(exc))
        paths = save_reports(root, report)
        print(json.dumps({"status": report["status"], "reports": paths, "errors": report["specification_errors"]}, indent=2))
        return 2

    if not notes_path.is_file():
        report["status"] = "notes_absent"
        report["groups"] = {name: {"expected": len(ids), "exactly_once": 0, "missing": len(ids), "repeated": 0}
                            for name, ids in groups.items()}
        paths = save_reports(root, report)
        print(json.dumps({"status": "notes_absent", "expected_total": len(ordered_ids), "reports": paths}, indent=2))
        return 2

    notes_bytes = notes_path.read_bytes()
    notes = notes_bytes.decode("utf-8")
    report["notes_sha256"] = hashlib.sha256(notes_bytes).hexdigest()
    expected = set(ordered_ids)
    known_start = re.compile(r"^(" + "|".join(re.escape(i) for i in sorted(expected, key=len, reverse=True)) + r")(?=$|[ \t—–:\-])")
    locations = collections.defaultdict(list)
    unexpected = collections.defaultdict(list)
    headings_total = 0
    for number, line in visible_lines(notes):
        heading = re.match(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t]*$", line)
        if not heading:
            continue
        level, body = len(heading.group(1)), heading.group(2)
        headings_total += 1
        shape = re.fullmatch(r"### (.+?) — (\S.*)", line)
        if shape:
            identifier, title = shape.groups()
            if not COMPARISON_START.match(identifier):
                continue
            if identifier in expected:
                locations[identifier].append(number)
            else:
                unexpected[identifier].append(number)
            continue
        known = known_start.match(body)
        if known:
            report["malformed_headings"].append({
                "line": number, "id": known.group(1),
                "issue": "Expected exactly '### <ID> — <nonempty title>'",
            })
        elif level == 3 and COMPARISON_START.match(body):
            candidate = re.match(r"(?:" + "|".join(COMPARISON_PREFIXES) + r")(?:[ \t]+[A-Za-z0-9_.-]+)?", body)
            identifier = candidate.group().strip()
            unexpected[identifier].append(number)
            report["malformed_headings"].append({
                "line": number, "id": identifier,
                "issue": "Unexpected ID or malformed spacing/title in comparison heading",
            })

    report["headings_inspected"] = headings_total
    report["expected_heading_lines"] = {identifier: locations[identifier] for identifier in ordered_ids}
    report["missing_ids"] = [identifier for identifier in ordered_ids if not locations[identifier]]
    report["duplicate_ids"] = {identifier: locations[identifier] for identifier in ordered_ids if len(locations[identifier]) > 1}
    report["unexpected_ids"] = dict(unexpected)
    for name, identifiers in groups.items():
        report["groups"][name] = {
            "expected": len(identifiers),
            "exactly_once": sum(len(locations[i]) == 1 for i in identifiers),
            "missing": sum(not locations[i] for i in identifiers),
            "repeated": sum(len(locations[i]) > 1 for i in identifiers),
        }
    has_errors = any(report[key] for key in ("missing_ids", "duplicate_ids", "unexpected_ids", "malformed_headings"))
    report["status"] = "fail" if has_errors else "pass"
    paths = save_reports(root, report)
    print(json.dumps({
        "status": report["status"], "expected_total": len(ordered_ids), "groups": report["groups"],
        "missing": len(report["missing_ids"]), "repeated": len(report["duplicate_ids"]),
        "unexpected": len(report["unexpected_ids"]), "malformed": len(report["malformed_headings"]),
        "reports": paths,
    }, indent=2))
    return int(has_errors)


if __name__ == "__main__":
    raise SystemExit(main())
