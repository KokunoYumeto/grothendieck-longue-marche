"""Read-only audit and aggregate checks; never assembles, freezes, or compiles.

Default: check approved pages and preserved comparison inputs, and fully check
each completed audit. Pending audits are reported without being treated as done.
--aggregates: also compare deterministic generated data with current reports.
--final: require all 23 audits, aggregate consistency, and all 24 frozen hashes.

No project module with write effects is imported. All expected output is formed
in memory; this script has no file-writing path. Aggregate prose introductions
are intentionally excluded, but tables, page sections, counts, source addenda,
and the combined transcription are checked. Rebuild with assemble.py separately
when those generated data are stale; this validator never performs that rebuild.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import csv
from datetime import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PREFIX = "SP84_C13_149"
TOKEN_PATTERN = re.compile(r"\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]")
BOX_FIELDS = ["box", "kind", "x0", "y0", "x1", "y1"]
READING_FIELDS = ["box", "reading"]
DIFF_FIELDS = ["box", "operation", "first_start", "first_end", "second_start",
               "second_end", "first_tokens", "second_tokens", "first_reading",
               "second_reading"]
ADJ_FIELDS = ["box", "first_reading", "second_reading", "final_reading",
              "evidence", "changed", "crop", "pixel_box"]


class IntegrityError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise IntegrityError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_rows(path, fields, delimiter="\t"):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter=delimiter)
        require(reader.fieldnames == fields, f"{path.name}: unexpected columns")
        result = list(reader)
    require(all(None not in row and all(v is not None for v in row.values())
                for row in result), f"{path.name}: malformed row width")
    return result


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_comments(source):
    lines = []
    for line in source.splitlines():
        for index, char in enumerate(line):
            if char != "%":
                continue
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                cursor -= 1
            if (index - cursor - 1) % 2 == 0:
                line = line[:index]
                break
        lines.append(line)
    return "\n".join(lines)


def check_environment_nesting(source, label):
    clean = strip_comments(source)
    stack = []
    # Tokenizing commands also prevents the second slash in \\begin from being
    # mistaken for a begin command after a TeX line-break command.
    for token in re.finditer(r"\\[A-Za-z]+|\\.", clean):
        command = token.group()
        if command not in (r"\begin", r"\end"):
            continue
        argument = re.match(r"\s*\{([^{}]+)\}", clean[token.end():])
        line = clean.count("\n", 0, token.start()) + 1
        require(argument is not None,
                f"{label}:{line}: malformed {command} environment argument")
        name = argument.group(1)
        if command == r"\begin":
            stack.append((name, line))
        else:
            require(stack and stack[-1][0] == name,
                    f"{label}:{line}: end{{{name}}} does not match "
                    f"{stack[-1] if stack else 'an open environment'}")
            stack.pop()
    require(not stack, f"{label}: unclosed environments {stack}")


def token_differences(first, second):
    result = []
    for a, b in zip(first, second):
        left = TOKEN_PATTERN.findall(a["reading"])
        right = TOKEN_PATTERN.findall(b["reading"])
        matcher = difflib.SequenceMatcher(None, left, right, autojunk=False)
        for operation, i, j, k, end in matcher.get_opcodes():
            if operation == "equal":
                continue
            result.append({"box": a["box"], "operation": operation,
                           "first_start": str(i), "first_end": str(j),
                           "second_start": str(k), "second_end": str(end),
                           "first_tokens": " ".join(left[i:j]),
                           "second_tokens": " ".join(right[k:end]),
                           "first_reading": a["reading"],
                           "second_reading": b["reading"]})
    return result


def check_rectangle(value, label):
    require(isinstance(value, (list, tuple)) and len(value) == 4
            and all(type(x) is int for x in value)
            and 0 <= value[0] < value[2] and 0 <= value[1] < value[3],
            f"{label}: invalid original-pixel rectangle")


def load_crop_rectangles(root):
    """Read explicitly recorded source rectangles; never infer them from names.

    Canonical crop manifests and the recovered first-crop table supply direct
    rectangles.  Scope supplements supply their own recorded rectangles.
    Explicit full-extent derivation links allow a rotated/resized view to use
    its source crop's rectangle.  Legacy rotation-only rows in the scope TSV
    have no numeric rectangle and are not treated as coordinate evidence.
    """
    rectangles = {}

    def add(crop, rectangle, provenance):
        require(isinstance(crop, str) and crop, f"{provenance}: missing crop path")
        check_rectangle(rectangle, f"{provenance}/{crop}")
        value = tuple(rectangle)
        require(crop not in rectangles or rectangles[crop] == value,
                f"{crop}: conflicting source rectangles in crop manifests")
        rectangles[crop] = value

    direct_tables = sorted((root / 'second').glob('*_crop_manifest.tsv'))
    first = root / 'documentation/first_crop_coordinates.tsv'
    if first.exists():
        direct_tables.append(first)
    for path in direct_tables:
        with path.open(encoding='utf-8', newline='') as stream:
            reader = csv.DictReader(stream, delimiter='\t')
            require({'crop', 'x0', 'y0', 'x1', 'y1'} <= set(reader.fieldnames or []),
                    f"{path.name}: missing source-rectangle columns")
            for row in reader:
                add(row['crop'], [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')], path.name)
    scope = root / 'documentation/audit_scope_crops.tsv'
    if scope.exists():
        with scope.open(encoding='utf-8', newline='') as stream:
            for row in csv.DictReader(stream, delimiter='\t'):
                values = [row.get(k) for k in ('x0', 'y0', 'x1', 'y1')]
                if all(isinstance(v, str) and re.fullmatch(r'\d+', v) for v in values):
                    add(row['crop'], list(map(int, values)), scope.name)
    for path in sorted((root / 'documentation').glob('*_supplement_crops.json')):
        for row in read_json(path):
            add(row['crop'], row['box'], path.name)
    derivations = root / 'documentation/adjudication_crop_derivations.json'
    if derivations.exists():
        for row in read_json(derivations):
            require(row.get('scope') == 'same_original_rectangle',
                    f"{derivations.name}: unsupported derived-view scope")
            source = row['source_crop']
            require(source in rectangles,
                    f"{derivations.name}: source crop has no recorded rectangle: {source}")
            require(row.get('evidence'), f"{derivations.name}: missing derivation evidence")
            add(row['crop'], rectangles[source], derivations.name)
    return rectangles


def reader_name(value):
    return str(value or "").rstrip("/").rsplit("/", 1)[-1]


def check_audit(root, report, final=False, crop_rectangles=None):
    n = report["scan"]
    stem = f"149_scan{n:03d}"
    directory = root / "second"
    provenance_path = directory / f"{stem}_comparison_provenance.json"
    if not provenance_path.exists():
        require(not final and not report.get("audited"),
                f"{stem}: missing comparison provenance")
        return {"scan": n, "status": "pending comparison", "input_hashes": 0}
    provenance = read_json(provenance_path)
    require(provenance.get("scan") == n, f"{stem}: provenance scan mismatch")
    expected_hashes = provenance.get("sha256", {})
    require(set(expected_hashes) == {"boxes", "first", "second"},
            f"{stem}: incomplete comparison-input hashes")
    for kind, expected in expected_hashes.items():
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                f"{stem}: malformed {kind} hash")
        path = directory / f"{stem}_{kind}.tsv"
        require(sha256(path) == expected, f"{stem}: frozen {kind} hash changed")
    boxes = read_rows(directory / f"{stem}_boxes.tsv", BOX_FIELDS)
    first = read_rows(directory / f"{stem}_first.tsv", READING_FIELDS)
    second = read_rows(directory / f"{stem}_second.tsv", READING_FIELDS)
    ids = [row["box"] for row in boxes]
    require(ids and len(ids) == len(set(ids)) and all(ids),
            f"{stem}: empty or duplicate neutral box IDs")
    require(ids == [row["box"] for row in first] == [row["box"] for row in second],
            f"{stem}: missing, extra, or reordered reading boxes")
    for box in boxes:
        check_rectangle([int(box[k]) for k in ("x0", "y0", "x1", "y1")],
                        f"{stem}/{box['box']}")
    require(all(row["reading"].strip() for row in first + second),
            f"{stem}: an empty box reading")
    differences = read_rows(directory / f"{stem}_token_differences.tsv", DIFF_FIELDS)
    require(differences == token_differences(first, second),
            f"{stem}: saved token differences do not reproduce frozen inputs")
    result = {"scan": n, "status": "pending adjudication", "input_hashes": 3,
              "boxes": len(ids), "token_spans": len(differences)}
    if not report.get("audited"):
        require(not final, f"{stem}: audit is not complete")
        return result
    require(reader_name(report.get("second_reader"))
            and reader_name(report.get("second_reader")) != reader_name(report.get("reader")),
            f"{stem}: independent reader is missing or is the first reader")
    datetime.strptime(report["audit_completed_utc"], "%Y-%m-%d %H:%M:%S UTC")
    adjudications = read_rows(directory / f"{stem}_adjudications.tsv", ADJ_FIELDS)
    different = {row["box"] for row in differences}
    adjudicated = [row["box"] for row in adjudications]
    require(len(adjudicated) == len(set(adjudicated)),
            f"{stem}: duplicate adjudication IDs")
    require(set(adjudicated) == different,
            f"{stem}: adjudications must equal the differing-box set")
    first_by_id = {row["box"]: row["reading"] for row in first}
    second_by_id = {row["box"]: row["reading"] for row in second}
    if crop_rectangles is None:
        crop_rectangles = load_crop_rectangles(root)
    verified_rectangles, unmapped_crops = 0, []
    for item in adjudications:
        label = f"{stem}/{item['box']}"
        require(item["first_reading"] == first_by_id[item["box"]]
                and item["second_reading"] == second_by_id[item["box"]],
                f"{label}: adjudication input readings differ from frozen TSVs")
        require(item["evidence"].strip() and item["final_reading"].strip(),
                f"{label}: missing evidence or final reading")
        require(item["changed"] in ("yes", "no"), f"{label}: invalid changed flag")
        crop = (root / item["crop"]).resolve()
        require(crop.is_relative_to(root.resolve()) and crop.is_file(),
                f"{label}: crop is missing or outside the edition")
        rectangle = ast.literal_eval(item["pixel_box"])
        check_rectangle(rectangle, label)
        if item['crop'] in crop_rectangles:
            require(tuple(rectangle) == crop_rectangles[item['crop']],
                    f"{label}: adjudication evidence rectangle {tuple(rectangle)} "
                    f"does not match recorded source rectangle {crop_rectangles[item['crop']]} "
                    f"for {item['crop']}")
            verified_rectangles += 1
        else:
            unmapped_crops.append(item['crop'])
    counts = {"audit_boxes_read": len(ids), "audit_differing_boxes": len(different),
              "audit_token_spans": len(differences),
              "audit_changed_boxes": sum(item["changed"] == "yes" for item in adjudications)}
    for key, expected in counts.items():
        require(report.get(key) == expected, f"{stem}: {key} does not match preserved records")
    result.update(status="audited", changed_boxes=counts["audit_changed_boxes"],
                  evidence_rectangles_verified=verified_rectangles,
                  unmapped_evidence_crops=sorted(set(unmapped_crops)))
    return result


def cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value if value is not None else "").replace("|", "&#124;").replace("\n", "<br>")


def table(fields, rows):
    return ("| " + " | ".join(fields) + " |\n| " + " | ".join("---" for _ in fields)
            + " |\n" + "".join("| " + " | ".join(cell(row.get(k, "")) for k in fields)
                                   + " |\n" for row in rows))


def check_aggregates(root, reports):
    """Compare deterministic data, without invoking or importing assemble.py."""
    issues = []
    documents = {}

    def document(name):
        if name not in documents:
            documents[name] = (root / name).read_text(encoding="utf-8")
        return documents[name]

    def mismatch(name, detail):
        issues.append(f"{name}: {detail}; rebuild aggregates separately")

    def csv_check(name, fields, expected, delimiter="\t"):
        actual = read_rows(root / name, fields, delimiter)
        expected = [{key: str(row.get(key, "") if row.get(key, "") is not None else "")
                     for key in fields} for row in expected]
        if actual != expected:
            mismatch(name, "generated rows differ from current reports")

    def table_check(name, fields, rows):
        expected = table(fields, rows).strip()
        lines = document(name).splitlines()
        starts = [i for i, line in enumerate(lines) if line == "| " + " | ".join(fields) + " |"]
        if len(starts) != 1:
            mismatch(name, f"missing/duplicate table headed {fields}")
            return
        end = starts[0]
        while end < len(lines) and lines[end].startswith("| "):
            end += 1
        if "\n".join(lines[starts[0]:end]).strip() != expected:
            mismatch(name, f"table headed {fields} differs")

    def page_sections_check(name, expected):
        pieces = re.split(r"(?m)^## Scan ([0-9]{3})\n", document(name))
        actual_ids = pieces[1::2]
        if actual_ids != list(expected):
            mismatch(name, "missing, extra, duplicate, or reordered scan sections")
        for scan, section in zip(actual_ids, pieces[2::2]):
            if scan not in expected or section.strip() != expected[scan].strip():
                mismatch(name, f"scan {scan} section differs")

    counts, all_changes, collation, decisions = [], [], [], []
    inventory, doubts, hand, abbreviations, checks, notation = [], [], [], [], [], []
    note_sections, change_sections = {}, {}
    for report in reports:
        n = report["scan"]
        scan = f"{n:03d}"
        changes = [x for x in report.get("changes", []) if x.get("against_C") or x.get("against_H")]
        counts.append({"scan": scan, "against C": sum(bool(x.get("against_C")) for x in changes),
                       "against H": sum(bool(x.get("against_H")) for x in changes),
                       **{level: sum(x["confidence"] == level for x in changes)
                          for level in ("high", "medium", "low")}, "places": len(changes)})
        display = []
        for item in changes:
            all_changes.append(dict(item, scan=n))
            evidence = item["evidence"]
            if item.get("crop", "page") != "page":
                evidence += f" Crop: `{item['crop']}`; original pixels {tuple(item.get('box', []))}."
            if item.get("audit_first") is not None:
                evidence += f" Independent audit: first `{item['audit_first']}`; second `{item.get('audit_second', '')}`."
            display.append({"place": item["place"], "C": item.get("C", ""), "H": item.get("H", ""),
                            "final": item["final"], "scan evidence": evidence, "confidence": item["confidence"]})
            if item.get("against_H"):
                collation.append({"folder": "149", "their_page": n - 1, "our_scan": n,
                                  "line": item["place"], "their_reading": item.get("H", ""),
                                  "codex_reading": item.get("C", ""), "final_reading": item["final"],
                                  "scan_shows": evidence, "kind": item["kind"],
                                  "marked_in_H": "yes" if item.get("marked_in_H") else "no",
                                  "confidence": item["confidence"]})
        section = table(["place", "C", "H", "final", "scan evidence", "confidence"], display)
        audit_path = root / f"second/149_scan{n:03d}_adjudications.tsv"
        if audit_path.exists():
            audit_rows = read_rows(audit_path, ADJ_FIELDS)
            changed = [{"box": x["box"], "first reading": x["first_reading"],
                        "independent reading": x["second_reading"], "final reading": x["final_reading"],
                        "scan evidence": x["evidence"] + " Crop: `" + x["crop"] + "`"
                        + ("; original pixels " + x["pixel_box"] if x.get("pixel_box") else "")}
                       for x in audit_rows if x.get("changed") == "yes"]
            section += "\n### Changes after the independent reading\n\n"
            section += (table(["box", "first reading", "independent reading", "final reading", "scan evidence"], changed)
                        if changed else "No reading was changed by the independent comparison.\n")
            section += ("\nAll token differences, including retained readings and differences of representation, "
                        f"are recorded in `second/149_scan{n:03d}_adjudications.tsv`. "
                        "Certainty-only changes in this audit table are not added to the substantive witness counts.\n")
        unresolved = report.get("doubts", [])
        section += "\nUnresolved: " + ("; ".join(f"{x['place']}: `{x['reading']}`" for x in unresolved)
                                        if unresolved else "none identified.") + "\n"
        change_sections[scan] = section
        for item in report.get("decisions", []):
            crop = item.get("crop", "page")
            decisions.append({"id": item["id"], "cote": "149", "scan": n, "decision": item["decision"],
                              "reading": item["reading"], "what the ink shows": item["evidence"],
                              "crop": crop + (f" {tuple(item.get('box', []))}" if crop != "page" else ""),
                              "confidence": item["confidence"]})
        inventory.extend(report.get("inventory", []))
        doubts.extend(dict(x, scan=scan) for x in unresolved)
        hand.extend(report.get("hand", []))
        abbreviations.extend(dict(x, scan=scan) for x in report.get("abbreviations", []))
        checks.extend(report.get("checks", []))
        notes = report.get("notes", "")
        note_sections[scan] = "\n\n".join(map(str, notes)) if isinstance(notes, list) else str(notes)
        for item in report.get("notation", []):
            notation.append({"scan": scan, "written form": item["written"], "rendering": item["rendering"],
                             "meaning / evidence": item["meaning"] + "; " + item["evidence"]})
    # Approved reports already retain the original per-scan MARKS order. This
    # check therefore remains usable in the ZIP without the excluded inputs.
    csv_check("decisions.tsv", ["id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"], decisions)
    csv_check(f"{PREFIX}_collation.tsv", ["folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence"], collation)
    csv_check(f"{PREFIX}_inventory.csv", ["scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"], inventory, ",")
    csv_check("CHECK_EVENTS.tsv", ["statement_id", "date", "who", "type", "outcome"], checks)
    page_sections_check(f"{PREFIX}_notes.md", note_sections)
    page_sections_check(f"{PREFIX}_changes.md", change_sections)
    count_fields = ["scan", "against C", "against H", "high", "medium", "low", "places"]
    total = {"scan": "TOTAL", **{key: sum(x[key] for x in counts) for key in count_fields[1:]}}
    table_check(f"{PREFIX}_changes.md", count_fields, counts + [total])
    consequential = "\n".join(f"- Scan {x['scan']:03d}, {x['place']}: `{x['final']}` — {x['evidence']}"
                               for x in all_changes if x.get("mathematical"))
    consequential = consequential or "No mathematical correction identified in pages finalized so far."
    match = re.search(r"(?ms)^## Consequential readings\n(.*?)(?=^## Scan [0-9]{3}\n|\Z)", document(f"{PREFIX}_changes.md"))
    if match is None or match.group(1).strip() != consequential.strip():
        mismatch(f"{PREFIX}_changes.md", "consequential-reading list differs")
    notation_fields = ["scan", "written form", "rendering", "meaning / evidence"]
    table_check("notation_current.md", notation_fields, notation)
    table_check(f"{PREFIX}_doubts.md", notation_fields, notation)
    table_check(f"{PREFIX}_doubts.md", ["scan", "place", "reading", "alternatives", "confidence", "reason"], doubts)
    grouped = {}
    for item in abbreviations:
        grouped.setdefault((item["form"], item["expansion"]), []).append(item["scan"] + ": " + item.get("place", ""))
    abbreviation_rows = [{"form": key[0], "proposed expansion": key[1], "places": "; ".join(value)}
                         for key, value in grouped.items()]
    table_check(f"{PREFIX}_doubts.md", ["form", "proposed expansion", "places"], abbreviation_rows)
    table_check(f"{PREFIX}_hand_log.md", ["habit", "pages", "consistency", "misread"], hand)
    categories = ["Symbols and indices", "Words", "Omissions", "Drawings and diagrams", "Readable ink left as illegible",
                  "Insertions put in the wrong place", "Struck text", "Abbreviations expanded, spelling modernised",
                  "Text that is not on the page", "Other"]
    category_counts = Counter(x.get("error_category", "Other") for x in all_changes)
    feedback_rows = [{"kind": category, "places": category_counts[category],
                      "locations": "; ".join(f"{x['scan']:03d}/{x['id']}" for x in all_changes
                                              if x.get("error_category", "Other") == category)} for category in categories]
    table_check(f"{PREFIX}_sheet_feedback.md", ["kind", "places", "locations"], feedback_rows)
    legibility = root / "legibility_note.md"
    if legibility.exists():
        suffix = "\n## Legibility and limits\n\n" + legibility.read_text(encoding="utf-8")
        if not document(f"{PREFIX}_doubts.md").endswith(suffix):
            mismatch(f"{PREFIX}_doubts.md", "legibility note differs")
    addendum = root / "feedback_addendum.md"
    if addendum.exists() and not document(f"{PREFIX}_sheet_feedback.md").endswith("\n" + addendum.read_text(encoding="utf-8")):
        mismatch(f"{PREFIX}_sheet_feedback.md", "feedback addendum differs")
    combined = "\\cotefile{149}\n\n" + "\n".join((root / f"pages/149_scan{x['scan']:03d}.tex").read_text(encoding="utf-8").rstrip() + "\n" for x in reports)
    if document(f"{PREFIX}_transcription.tex") != combined:
        mismatch(f"{PREFIX}_transcription.tex", "combined transcription differs from pages")
    return issues


def check_freeze(root):
    manifest = read_json(root / "documentation/frozen_sha256.json")
    datetime.strptime(manifest["frozen_utc"], "%Y-%m-%d %H:%M:%S UTC")
    expected_paths = [f"pages/149_scan{n:03d}.tex" for n in range(5, 28)] + [f"{PREFIX}_transcription.tex"]
    actual_pages = [str(path.relative_to(root)) for path in sorted((root / "pages").glob("149_scan*.tex"))]
    require(actual_pages == expected_paths[:-1], "final freeze has missing or extra transcription pages")
    expected = manifest.get("sha256", {})
    require(set(expected) == set(expected_paths), "final freeze must cover exactly 23 pages and the combined transcription")
    for name in expected_paths:
        require(sha256(root / name) == expected[name], f"frozen transcription changed: {name}")
    return len(expected_paths)


def validate(root, final=False, aggregates=False):
    issues, audit_results, checked_pages = [], [], []
    crop_rectangles = load_crop_rectangles(root)
    reports = [read_json(p) for p in sorted((root / "reviews").glob("149_scan*.json"))]
    reports = [x for x in reports if x.get("root_approved")]
    scans = [x["scan"] for x in reports]
    if final and scans != list(range(5, 28)):
        issues.append("final validation requires approved scans005–027 exactly")
    if not reports:
        issues.append("no approved reports found")
    for report in reports:
        n = report["scan"]
        try:
            page = root / f"pages/149_scan{n:03d}.tex"
            source = page.read_text(encoding="utf-8")
            require(f"\\scanpage{{{n}}}" in source, f"{page.name}: scan header missing")
            check_environment_nesting(source, page.name)
            checked_pages.append(n)
        except (OSError, ValueError, IntegrityError) as exc:
            issues.append(str(exc))
        try:
            audit_results.append(check_audit(root, report, final, crop_rectangles))
        except (OSError, ValueError, SyntaxError, KeyError, TypeError, IntegrityError) as exc:
            issues.append(f"scan{n:03d}: {exc}")
    aggregate_checked = aggregates or final
    if aggregate_checked:
        try:
            issues.extend(check_aggregates(root, reports))
        except (OSError, ValueError, KeyError, TypeError, IntegrityError) as exc:
            issues.append(f"aggregate validation: {exc}")
    frozen_files = 0
    if final:
        try:
            frozen_files = check_freeze(root)
        except (OSError, ValueError, KeyError, TypeError, IntegrityError) as exc:
            issues.append(f"final freeze verification: {exc}")
    return {"status": "failed" if issues else "passed", "mode": "final" if final else "progress",
            "read_only": True, "approved_pages": len(reports), "environment_pages_checked": len(checked_pages),
            "comparison_input_hashes_verified": sum(x["input_hashes"] for x in audit_results),
            "completed_audits_checked": [x["scan"] for x in audit_results if x["status"] == "audited"],
            "pending_audits": [x["scan"] for x in audit_results if x["status"] != "audited"],
            "token_spans_checked": sum(x.get("token_spans", 0) for x in audit_results),
            "evidence_rectangles_verified": sum(x.get("evidence_rectangles_verified", 0) for x in audit_results),
            "unmapped_evidence_crops": sorted({p for x in audit_results for p in x.get("unmapped_evidence_crops", [])}),
            "aggregates_checked": aggregate_checked, "frozen_transcription_files_verified": frozen_files,
            "issues": issues}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition-root", type=Path, default=ROOT, help="edition directory (default: this script's parent edition)")
    parser.add_argument("--aggregates", action="store_true", help="compare generated data with current approved reports")
    parser.add_argument("--final", action="store_true", help="require all audits, aggregates, and the final freeze; run only after completion")
    args = parser.parse_args(argv)
    try:
        result = validate(args.edition_root.resolve(), args.final, args.aggregates)
    except (OSError, ValueError, KeyError, TypeError, IntegrityError) as exc:
        result = {"status": "failed", "read_only": True, "issues": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
