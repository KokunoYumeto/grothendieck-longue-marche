#!/usr/bin/env python3
"""Proposed mechanical repairs; default is read-only preview.

Prepared from existing reader decisions. No scans or witnesses are opened.
No image reading, OCR, mathematical judgment, or TeX compilation is performed.
Run with --apply only after the primary reader has reviewed the proposal.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output"
sys.path.insert(0, str(OUT / "scripts"))
import records

CHANGE_SCANS = (7, 17, 21, 22, 23)
SCOPE_TAG = "[Mechanical scope repair]"
SCRIPT_TAG = "# SP59 mechanical repair: separate TeX commands from adjacent letters."

# Filled from the original reader-authored rows during script preparation.
# These are integrity guards, not reading decisions.
EXPECTED_ROW_HASHES = {(7, '71-007-007'): '4ee53517cc237f6800f1ec2b0ea82be9d3f94b6a64e79466bd02a3d22ab1ed3e', (7, '71-007-011'): '9646633defa06f0919723683ca1c9ddc8edca51c477d0f2e57d3eaf59b484c20', (17, '71-017-024'): '1f9b5d0f3cfa89a691d64989ae4fdc65045202a20e72608c96d145e53906d055', (21, '71-021-011'): '8b12345183f904b3286932bdd8dcce0965c6feac76a973a8db57f074555a78aa', (21, '71-021-014'): '3507c652c00f81f0f0cfbcc703fa02de7874891e8da801b05fe31f1cd851cfd2', (21, '71-021-015'): 'ec4402006bfb2f8de29949c2ec76e0cff0f75950bd3dc15e935948bd68771bc8', (21, '71-021-017'): 'f66ab4864775f12692d4cb2e2b362bd544fa84d33b92743f510522ae34393e82', (21, '71-021-018'): '3896de1b8ba1033c371b4ff2e6f7fe56b99b42f9c29d16e973ccf5245465dd12', (22, '71-022-001'): 'c2af44934de0def9823afd4ecb86080e3509b20c097b2478e798709494347e67', (23, '71-023-017'): 'de616318d5596f6de47ae01d1272f815e68a1b3adcf5265e148e331544782a51'}
EXPECTED_INVENTORY_HASHES = {(23, '023-27'): '3dc3fa87275f29168bb1845f17369e4cfdc1be6424cae8552e04a92296759f85', (23, '023-36'): '6c2da1d69dfd0fa616c759467b81d9bdb3665eb51a87f253c0bf24b21deed02f'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def row_hash(row, fields):
    return sha("\0".join(str(row.get(k, "")) for k in fields).encode("utf-8"))


def read_table(path, fields, delimiter="\t"):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        if reader.fieldnames != fields:
            raise RuntimeError(f"Unexpected columns in {path.relative_to(ROOT)}")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise RuntimeError(f"Malformed table: {path.relative_to(ROOT)}")
    return rows


def table_bytes(fields, rows, delimiter="\t"):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, delimiter=delimiter, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def original_row(rows, scan, identifier, inventory=False):
    key = "element" if inventory else "id"
    found = [row for row in rows if row[key] == identifier]
    if len(found) != 1:
        raise RuntimeError(f"Expected exactly one original row {identifier}, found {len(found)}")
    row = found[0]
    guards = EXPECTED_INVENTORY_HASHES if inventory else EXPECTED_ROW_HASHES
    fields = records.INVENTORY_FIELDS if inventory else records.CHANGE_FIELDS
    expected = guards.get((scan, identifier))
    if not expected:
        raise RuntimeError(f"No preparation-time guard for {identifier}")
    if row_hash(row, fields) != expected:
        raise RuntimeError(f"Reader record {identifier} changed after this proposal; rebase the patch rather than overwrite it")
    return row


def split_change(rows, scan, identifier, specifications, redirects, actions):
    names = [identifier + chr(97 + i) for i in range(len(specifications))]
    present = {row["id"] for row in rows}
    if identifier not in present:
        if set(names) <= present:
            return rows  # Already repaired; never overwrite later reader edits.
        raise RuntimeError(f"Neither original {identifier} nor its complete replacement set exists")
    if present.intersection(names):
        raise RuntimeError(f"Original and split forms coexist for {identifier}")
    old = original_row(rows, scan, identifier)
    replacements = []
    for name, changes in zip(names, specifications):
        row = dict(old)
        row.update(changes)
        row["id"] = name
        row["scan_shows"] = row.get("scan_shows", old["scan_shows"]).rstrip() + " " + SCOPE_TAG + " This row isolates the occurrence named in Place; no new visual examination or reading decision is claimed."
        replacements.append(row)
    new = []
    for row in rows:
        new.extend(replacements if row["id"] == identifier else [row])
    redirects.append({"record_type": "change", "old_id": identifier, "new_ids": ";".join(names)})
    actions.append(f"{identifier} -> {', '.join(names)}")
    return new


def split_inventory(rows, identifier, specifications, redirects, actions):
    names = [identifier + chr(97 + i) for i in range(len(specifications))]
    present = {row["element"] for row in rows}
    if identifier not in present:
        if set(names) <= present:
            return rows
        raise RuntimeError(f"Neither original {identifier} nor complete split inventory exists")
    if present.intersection(names):
        raise RuntimeError(f"Original and split inventory coexist for {identifier}")
    old = original_row(rows, 23, identifier, inventory=True)
    replacements = []
    for name, changes in zip(names, specifications):
        row = dict(old)
        row.update(changes)
        row["element"] = name
        replacements.append(row)
    new = []
    for row in rows:
        new.extend(replacements if row["element"] == identifier else [row])
    redirects.append({"record_type": "inventory", "old_id": identifier, "new_ids": ";".join(names)})
    actions.append(f"inventory {identifier} -> {', '.join(names)}")
    return new


def closing_brace(text, opening):
    depth = 0
    i = opening
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise RuntimeError("Unbalanced comparison-cell macro; cannot remove its scope safely")


def without_margins(text):
    """Remove complete margin macro arguments from comparison cells only."""
    pieces = []
    cursor = 0
    for match in re.finditer(r"\\margin\s*\{", text):
        if match.start() < cursor:
            continue
        pieces.append(text[cursor:match.start()])
        cursor = closing_brace(text, match.end() - 1) + 1
    pieces.append(text[cursor:])
    return "".join(pieces).strip()


def repair_021_scope(rows, actions):
    explanations = {
        "71-021-011": "Theorem wording only. The pencil drawing belongs exclusively to 71-021-005 and is absent from this comparison cell.",
        "71-021-014": "Paragraph content excluding marginal marks. The new pencil drawing belongs exclusively to 71-021-006; marginal point annotations are also outside this omission's scope.",
        "71-021-015": "Arc-definition wording excluding the marginal or. ? annotation; the margin is not counted again as a main-text omission.",
        "71-021-017": "Underlying-set wording only. Both comparison cells render aussi without underline markup here; its underline extent belongs exclusively to 71-021-003.",
    }
    for identifier, explanation in explanations.items():
        row = next((r for r in rows if r["id"] == identifier), None)
        if row is None:
            raise RuntimeError(f"Missing scope-repair target {identifier}")
        if SCOPE_TAG in row["scan_shows"]:
            continue
        original_row(rows, 21, identifier)
        for key in ("C", "final"):
            row[key] = without_margins(row[key])
        if identifier == "71-021-017":
            if r"\uline{aussi}" not in row["C"] or r"a\uline{us}si" not in row["final"]:
                raise RuntimeError("The aussi markup changed; rebase the scope repair")
            row["C"] = row["C"].replace(r"\uline{aussi}", "aussi", 1)
            row["final"] = row["final"].replace(r"a\uline{us}si", "aussi", 1)
        row["scan_shows"] += " " + SCOPE_TAG + " " + explanation + " The complete page transcription is unchanged."
        actions.append(f"{identifier}: exclude separately counted annotation material")
    return rows


def remarque_parts(text):
    text = without_margins(text).replace(r"co\uline{up}le", "couple")
    first = r"$\mathrm{I})"
    second = r"$\mathrm{II})$"
    if text.count(first) != 1 or text.count(second) != 1:
        raise RuntimeError("Remarque display boundaries changed; rebase the split")
    start_i, start_ii = text.index(first), text.index(second)
    prose = text[:start_i].strip()
    display_i = text[start_i:start_ii].strip()
    # The semicolon was the old comparison cell's display separator. It is not
    # added to the transcription and need not be carried between separate rows.
    if display_i.endswith(";"):
        display_i = display_i[:-1].rstrip()
    display_ii = text[start_ii:].strip()
    return prose, display_i, display_ii


def repaired_change_rows(scan, rows, redirects, actions):
    if scan == 7:
        places = [
            "Main diagram, boundary-Sigma subscript separator",
            "Main diagram, Delta subscript separator",
            "Main diagram, boundary-Delta subscript separator",
            "Following Sigma formula, left-hand Sigma subscript separator",
            "Following Sigma formula, first Delta argument subscript separator",
            "Following Sigma formula, boundary-Delta argument subscript separator",
        ]
        rows = split_change(rows, scan, "71-007-007", [dict(place=p, C="short dash", H=r"\dots", final="short dash") for p in places], redirects, actions)
        rows = split_change(rows, scan, "71-007-011", [
            dict(place="Lower central column, upper unheaded link", C="upper plain stroke", H="upper arrow", final="upper plain stroke", diff_C="no"),
            dict(place="Lower central column, lower hooked unheaded link", C="lower hooked arrow", H="lower arrow", final="lower hooked unheaded stroke"),
        ], redirects, actions)
        # 71-007-013 is one cancelled diagram fragment: an arrow attached to its
        # Sigma object. Keep that physical unit together and retain all flags.
    elif scan == 17:
        rows = split_change(rows, scan, "71-017-024", [
            dict(place="Divider between the first formula pair and the listed strata", C="slanted divider", final="slanted divider"),
            dict(place="Divider between the lower U_i,U_j,U_k group and the V intersections", C="slanted divider", final="slanted divider"),
        ], redirects, actions)
    elif scan == 21:
        rows = repair_021_scope(rows, actions)
        identifier = "71-021-018"
        old = next((r for r in rows if r["id"] == identifier), None)
        if old is not None:
            original_row(rows, scan, identifier)
            c_parts, f_parts = remarque_parts(old["C"]), remarque_parts(old["final"])
            places = ["Remarque 1, main prose (marginal mark and couple underline excluded)", "Remarque 1, display I (not recomposed in H)", "Remarque 1, opening of II and its cancelled continuation (not recomposed in H)"]
            specs = []
            for i, place in enumerate(places):
                evidence = old["scan_shows"]
                if i == 0:
                    evidence += " The marginal point is outside this main-prose omission. The word couple appears without underline markup in these comparison cells; its underline belongs exclusively to 71-021-004."
                specs.append(dict(place=place, C=c_parts[i], final=f_parts[i], scan_shows=evidence))
            rows = split_change(rows, scan, identifier, specs, redirects, actions)
        elif not {identifier + s for s in "abc"} <= {r["id"] for r in rows}:
            raise RuntimeError("Incomplete existing Remarque split")
    elif scan == 22:
        rows = split_change(rows, scan, "71-022-001", [
            dict(place="Upper drawing, first inner label", C="doubtful Gamma^1/Gamma_1", H="1", final="Gamma^1"),
            dict(place="Upper drawing, second inner label", C="doubtful Gamma^2/Gamma_2", H="2", final="Gamma^2"),
        ], redirects, actions)
    elif scan == 23:
        rows = split_change(rows, scan, "71-023-017", [
            dict(place="Bottom strip, curved lead before the first visibility paragraph", C="curved lead", final="curved lead"),
            dict(place="Bottom strip, vertical side rule before the first visibility paragraph", C="vertical side rule", final="vertical side rule"),
            dict(place="Bottom strip, angular mark beside ouvert in the first visibility paragraph", C="angular mark", final="angular mark"),
            dict(place="Bottom strip, vertical side rule before the second visibility paragraph", C="vertical side rule", final="vertical side rule"),
            dict(place="Bottom strip, vertical side rule after the second visibility paragraph", C="vertical side rule", final="vertical side rule"),
        ], redirects, actions)
    return rows


def count_differences(rows):
    return {
        "C": sum(records.as_bool(r["diff_C"]) for r in rows),
        "H": sum(records.as_bool(r["diff_H"]) for r in rows),
        "places": sum(records.as_bool(r["diff_C"]) or records.as_bool(r["diff_H"]) for r in rows),
    }


def prepare():
    if (OUT / "TRANSCRIPTION_SHA256.tsv").exists():
        raise RuntimeError("The transcription is frozen. Do not apply a text-spacing patch after freeze without primary-reader review")
    changes = {}
    originals = {}
    redirects = []
    actions = []
    deltas = []
    for scan in CHANGE_SCANS:
        path = records.record_dir(scan) / "changes.tsv"
        originals[path] = path.read_bytes()
        rows = read_table(path, records.CHANGE_FIELDS)
        before = count_differences(rows)
        updated = repaired_change_rows(scan, rows, redirects, actions)
        identifiers = [r["id"] for r in updated]
        if len(identifiers) != len(set(identifiers)):
            raise RuntimeError(f"Planned duplicate change ID on scan {scan}")
        after = count_differences(updated)
        deltas.append((scan, {key: after[key] - before[key] for key in before}))
        new_bytes = table_bytes(records.CHANGE_FIELDS, updated)
        if new_bytes != originals[path]:
            changes[path] = new_bytes

    path = records.record_dir(23) / "inventory.csv"
    originals[path] = path.read_bytes()
    inventory = read_table(path, records.INVENTORY_FIELDS, ",")
    inventory = split_inventory(inventory, "023-27", [
        dict(position="left of Definition 2", first_words_or_objects="dot"),
        dict(position="left of n’est pas in Definition 2", first_words_or_objects="comma-shaped mark"),
    ], redirects, actions)
    inventory = split_inventory(inventory, "023-36", [
        dict(position="before first visibility paragraph", first_words_or_objects="curved lead"),
        dict(position="left of first visibility paragraph", first_words_or_objects="vertical side rule"),
        dict(position="beside ouvert in first visibility paragraph", first_words_or_objects="angular mark"),
        dict(position="left of second visibility paragraph", first_words_or_objects="vertical side rule"),
        dict(position="right of second visibility paragraph", first_words_or_objects="vertical side rule"),
    ], redirects, actions)
    if any(r["transcribed"] != "yes" for r in inventory):
        raise RuntimeError("Planned inventory contains an unfinished element")
    new_bytes = table_bytes(records.INVENTORY_FIELDS, inventory, ",")
    if new_bytes != originals[path]:
        changes[path] = new_bytes

    path = OUT / "pages" / records.page_name(23)
    originals[path] = path.read_bytes()
    text = originals[path].decode("utf-8")
    fixed = re.sub(r"\\cupV\b", lambda _: r"\cup V", text)
    fixed = re.sub(r"\\subsetD\b", lambda _: r"\subset D", fixed)
    if fixed != text:
        if not records.brace_balance(fixed)[0]:
            raise RuntimeError("Unexpected brace problem after command-spacing normalization")
        changes[path] = fixed.encode("utf-8")
        actions.append("Scan023 page: separate cup/V and subset/D control-word boundaries only")

    path = OUT / "scripts" / "read023.py"
    originals[path] = path.read_bytes()
    script = originals[path].decode("utf-8")
    if SCRIPT_TAG not in script:
        marker = "record_page(23,"
        if script.count(marker) != 1:
            raise RuntimeError("Cannot locate the unique scan023 save call for the regeneration safeguard")
        line_start = script.rfind("\n", 0, script.index(marker)) + 1
        addition = SCRIPT_TAG + '\nt = t.replace(r"\\cupV", r"\\cup V").replace(r"\\subsetD", r"\\subset D")\n'
        script = script[:line_start] + addition + script[line_start:]
        changes[path] = script.encode("utf-8")
        actions.append("read023.py: normalize those two command boundaries immediately before saving")

    # Aggregate files are regenerated, so they need no manual ID substitutions.
    # A reader-authored cross-reference added since preparation must be reviewed.
    old_ids = {r["old_id"] for r in redirects if r["record_type"] == "change"}
    for path in (OUT / "records").rglob("*"):
        if not path.is_file() or path.name in {"changes.tsv", "inventory.csv"}:
            continue
        text = path.read_text(encoding="utf-8")
        for identifier in old_ids:
            if re.search(re.escape(identifier) + r"(?![A-Za-z0-9])", text):
                raise RuntimeError(f"Reader-authored reference to retired ID {identifier} in {path.relative_to(OUT)}; update its exact target before applying")
    return originals, changes, redirects, actions, deltas


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".mechanical-repair.tmp")
    with temporary.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)


def apply(prepared):
    originals, changes, redirects, actions, deltas = prepared
    if not changes:
        print("No changes needed; the scoped repairs are already present.")
        return
    # Recheck all input bytes before the first mutation; refuse concurrent edits.
    for path, data in originals.items():
        if path.read_bytes() != data:
            raise RuntimeError(f"Concurrent change detected: {path.relative_to(OUT)}")
    timestamp = records.utc_now()
    digest_rows = []
    for path, data in changes.items():
        digest_rows.append({"path": path.relative_to(OUT).as_posix(), "before_sha256": sha(originals[path]), "after_sha256": sha(data), "date_utc": timestamp})
    for path, data in changes.items():
        atomic_write(path, data)

    redirects_path = OUT / "ID_REDIRECTS.tsv"
    redirect_fields = ["record_type", "old_id", "new_ids"]
    existing = read_table(redirects_path, redirect_fields) if redirects_path.exists() else []
    known = {(r["record_type"], r["old_id"]) for r in existing}
    existing.extend(r for r in redirects if (r["record_type"], r["old_id"]) not in known)
    atomic_write(redirects_path, table_bytes(redirect_fields, existing))

    history_path = OUT / "MECHANICAL_REPAIRS.tsv"
    history_fields = ["path", "before_sha256", "after_sha256", "date_utc"]
    history = read_table(history_path, history_fields) if history_path.exists() else []
    history.extend(digest_rows)
    atomic_write(history_path, table_bytes(history_fields, history))
    # Keep the executed repair logic with future checkpoints/final deliverables.
    archived_script = OUT / "scripts" / "repair_bookkeeping.py"
    if Path(__file__).resolve() != archived_script.resolve():
        atomic_write(archived_script, Path(__file__).read_bytes())
    report = ["# Mechanical bookkeeping repair", "", f"Applied {timestamp}.", "", "No image was opened, no reading was decided, and no mathematical assertion was checked by this script. The page transcription changed only at the two documented scan023 TeX command boundaries. All confidence levels and error categories were retained. The upper scan007 link receives diff_C=no because the original grouped row already states that C and the final upper link are identical; the C difference remains on the lower link.", "", "## Operations", ""]
    report.extend("- " + item for item in actions)
    report += ["", "The arrow and attached Sigma in 71-007-013 remain one cancelled diagram fragment. No new difference was introduced there.", "", "ID_REDIRECTS.tsv maps retired grouped IDs to their suffix IDs. Aggregate files were rebuilt from the repaired records. If an original readNNN.py is later rerun, rerun this repair script before final validation; the script will refuse unreviewed changes to its original target rows. The scan023 spacing safeguard is installed in read023.py itself."]
    atomic_write(OUT / "MECHANICAL_REPAIRS.md", ("\n".join(report) + "\n").encode("utf-8"))
    summary = records.build()
    result = records.validate()
    if result["errors"]:
        raise RuntimeError("Post-repair structural errors: " + "; ".join(result["errors"]))
    records.log_event(f"mechanical bookkeeping repairs applied {timestamp}; no new ink readings")
    print("Applied mechanical repairs and rebuilt aggregates.")
    for key, value in summary.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Apply the reviewed plan; without this flag, only print a preview")
    args = parser.parse_args()
    prepared = prepare()
    originals, changes, redirects, actions, deltas = prepared
    print("Proposed actions:")
    for action in actions:
        print("- " + action)
    print("Planned record-count deltas:")
    for scan, delta in deltas:
        print(f"  scan {scan:03d}: C {delta['C']:+}, H {delta['H']:+}, distinct rows {delta['places']:+}")
    print(f"Files to change before aggregate rebuild: {len(changes)}")
    if args.apply:
        apply(prepared)
    else:
        print("READ-ONLY PREVIEW: no files changed. Review the proposal before invoking --apply.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
