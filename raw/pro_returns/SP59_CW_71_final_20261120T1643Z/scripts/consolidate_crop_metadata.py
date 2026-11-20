#!/usr/bin/env python3
"""Consolidate text-only crop metadata; never open/process/view an image.

Reads exact pixel tuples from the root reader's records, older metadata, and
the append-only crop.py register. Retains prior complete-register tuples.
Explicit root confirmations are separate from descriptive filename aliases.
Rejected numerical candidates are never imported. Missing boxes stay empty.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
BOX = re.compile(r"\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)")
ROTATION = re.compile(r"\brotat(?:e|ed|ion)?\s*(?:by\s*)?([−+-]?\d+(?:\.\d+)?)", re.I)
FIELDS = ["scan", "crop_filename", "label", "element_type", "x0", "y0", "x1", "y1",
          "rotation_deg", "horizontal_mirror", "coordinate_status", "name_association_basis",
          "in_changes_md", "sources", "evidence", "issues", "source_crop", "transform_chain"]
APPENDIX_START = "<!-- BEGIN COMPLETE CROP COORDINATES -->"
APPENDIX_END = "<!-- END COMPLETE CROP COORDINATES -->"


def read_tsv(path):
    if not path.exists():
        return []
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path, rows, fields):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def normalize_rotation(value):
    return format(float(str(value).replace("−", "-")), "g")


def append_changes_table(rows):
    """Update only our marked metadata block, preserving every other byte."""
    grouped = defaultdict(list)
    for row in rows:
        if row["element_type"] == "tight_crop" and row["x0"] != "":
            grouped[(row["scan"], tuple(row[k] for k in ("x0", "y0", "x1", "y1")))].append(row)
    missing = [r for r in rows if r["element_type"] == "tight_crop" and r["coordinate_status"] == "unrecovered"]
    recovery_008 = next((r for r in rows if r["crop_filename"] == "008_slanted.jpg" and r["x0"] != ""), None)
    lines = [APPENDIX_START, "### Complete crop-coordinate register", "",
        "This table consolidates already recorded crop metadata. It adds no image reading, audit event, or transcription decision. Coordinates refer to the original supplied whole-page image. Unknown transformation fields are left unasserted. The detailed provenance is in `crop_register_complete.tsv`.", "",
        f"There are {len(grouped)} distinct documented source boxes below, with {len(missing)} unrecovered tight-crop boxes. Existing-crop rotations are listed separately and do not increase the source-box count.", "",
        "| Scan | Crop identifier | Original pixel box (x0,y0,x1,y1) | Recorded source transformation | Metadata provenance |",
        "| --- | --- | --- | --- | --- |"]
    for (scan, box), items in sorted(grouped.items()):
        labels = "; ".join(f"`{r['crop_filename']}`" for r in items if r["crop_filename"]) or "unnamed recorded box"
        rotations = sorted({r["rotation_deg"] for r in items if r["rotation_deg"] != ""})
        mirrors = sorted({r["horizontal_mirror"] for r in items if r["horizontal_mirror"] != ""})
        transform = "rotation " + "; ".join(rotations) + " degrees" if rotations else "rotation not recorded"
        if "yes" in mirrors:
            transform += "; horizontally mirrored before enlargement"
        basis = "documented per-page tuple; descriptive filename association"
        if any("direct crop.py" in r["name_association_basis"] for r in items):
            basis = "crop.py argument ledger; per-page metadata where present"
        if any("explicit root" in r["name_association_basis"] for r in items):
            basis += "; explicit root confirmation"
        if any("byte-identical" in r["evidence"] for r in items):
            basis = "SIFT/RANSAC registration and unique byte-identical JPEG pipeline replay; explicit root confirmation"
        lines.append(f"| {scan} | {labels} | ({','.join(map(str, box))}) | {transform} | {basis} |")
    lines += ["", "#### Unrecovered metadata", ""]
    if missing:
        lines += ["| Scan | Crop identifier | Original pixel box | Rotation | Status |",
            "| --- | --- | --- | --- | --- |"]
        for row in missing:
            lines.append(f"| {row['scan']} | `{row['crop_filename']}` | unrecovered | unrecovered | Numerical candidates were rejected; no coordinates invented and no new crop made. |")
    else:
        lines += ["None. Every tight-crop source box is now documented."]
    if recovery_008:
        lines += ["", "The earlier `008_slanted.jpg` exception was resolved by numerical feature registration followed by a unique byte-identical replay among 200 nearby geometry-compatible integer boxes: (980,950,1240,1155), rotation -34 degrees, JPEG SHA-256 `20147642b901c8f08f8981f39469d965a2cdbebf06378bc1e77469a42f0f7b98`. Decoded-pixel RMSE is 0.0. This recovers crop metadata only; no new image reading or transcription change was made. The earlier failed correlation searches remain historical and are superseded by `metadata/crop008_exact_replay.md`."]
    lines += ["", "The earlier missing entries `007_pi_D.jpg`, `021_J.jpg`, `021_connexe.jpg`, `021_or.jpg`, and `021_suivantes.jpg` are explicitly included in the complete table. The first is preserved in the earlier doubt record; the other four are root-confirmed numerical metadata recoveries.", "",
        "#### Derivative orientations of the same source crop", "",
        "For scan 033, `033_margin.jpg` was made from the single source box (14,1160,146,1542), initially rotated -90 degrees. The following files rotate that existing crop; none is a second source crop. The final reading orientation is -55 degrees relative to the original image.", "",
        "| Scan | Derivative alias | Source crop | Same original pixel box | Final orientation relative to original | Transformation history |",
        "| --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        if row["element_type"] == "crop_derivative":
            box = ",".join(str(row[k]) for k in ("x0", "y0", "x1", "y1"))
            lines.append(f"| {row['scan']} | `{row['crop_filename']}` | `{row['source_crop']}` | ({box}) | {row['rotation_deg']} degrees | {row['transform_chain']} |")
    halves = [f"`{r['crop_filename']}`" for r in rows if r["element_type"] == "supplied_half_transform"]
    lines += ["", "Supplied-half orientation derivatives, outside the tight-crop count: " + ", ".join(halves) + ".", "", APPENDIX_END]
    block = "\n".join(lines) + "\n"
    target = OUT / "CHANGES_EXTRA.md"
    current = target.read_text() if target.exists() else ""
    if APPENDIX_START in current:
        start = current.index(APPENDIX_START)
        stop = current.index(APPENDIX_END, start) + len(APPENDIX_END)
        current = current[:start] + block.rstrip("\n") + current[stop:]
    else:
        current += ("\n\n" if current and not current.endswith("\n\n") else "") + block
    target.write_text(current)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--append-changes", action="store_true", help="Preserve other CHANGES_EXTRA prose and update the marked coordinate-table block")
    args = parser.parse_args()
    boxes = {}
    conflicts = []
    named = defaultdict(set)
    previous = read_tsv(OUT / "crop_register_complete.tsv")
    derivative_rows = read_tsv(OUT / "metadata/crop_derivative_aliases.tsv")
    derivative_names = {(int(r["scan"]), r["label"]) for r in derivative_rows}

    def add(scan, box, source, evidence="", *, label="", basis="", rotation="", mirror="", in_changes=False):
        scan, box = int(scan), tuple(map(int, box))
        if not (box[0] < box[2] and box[1] < box[3]):
            conflicts.append(dict(scan=scan, crop_filename="", issue="nonpositive box", detail=f"{box}; {source}"))
            return
        key = (scan, box)
        entry = boxes.setdefault(key, dict(sources=set(), evidence=[], names={}, rotations=set(), mirrors=set(), in_changes=False))
        entry["sources"].add(source)
        if evidence and evidence not in entry["evidence"]:
            entry["evidence"].append(evidence)
        if label:
            entry["names"].setdefault(label, set()).add(basis)
            named[(scan, label)].add(box)
        if rotation != "":
            entry["rotations"].add(normalize_rotation(rotation))
        if mirror in ("yes", "no"):
            entry["mirrors"].add(mirror)
        entry["in_changes"] |= in_changes

    # Preserve earlier tuples even if a later record edit removes their citation.
    for row in previous:
        if not row.get("x0") or row.get("element_type") == "crop_derivative" or (int(row["scan"]), row.get("label")) in derivative_names:
            continue
        old_box = [row[k] for k in ("x0", "y0", "x1", "y1")]
        old_sources = row.get("sources", "").split("; ") or ["retained prior complete-register tuple"]
        old_evidence = row.get("evidence", "").split(" || ")
        old_bases = row.get("name_association_basis", "").split("; ")
        for source in old_sources:
            if source:
                add(row["scan"], old_box, source)
        entry = boxes[(int(row["scan"]), tuple(map(int, old_box)))]
        for evidence in old_evidence:
            if evidence and evidence not in entry["evidence"]:
                entry["evidence"].append(evidence)
        for basis in old_bases:
            if row.get("label"):
                entry["names"].setdefault(row["label"], set()).add(basis)
                named[(int(row["scan"]), row["label"])].add(tuple(map(int, old_box)))
        for rotation in row.get("rotation_deg", "").split(";"):
            if rotation:
                entry["rotations"].add(normalize_rotation(rotation))
        entry["mirrors"].update(v for v in row.get("horizontal_mirror", "").split(";") if v in ("yes", "no"))

    # The earlier audit register preserves coordinates whose only source may be a
    # certainty-only doubt row. It contains no accepted numerical-search guesses.
    old_audit = ROOT / "support/crop_box_register.tsv"
    for index, row in enumerate(read_tsv(old_audit), 2):
        add(row["scan"], [row[k] for k in ("x0", "y0", "x1", "y1")],
            f"support/crop_box_register.tsv:{index}; {row.get('other_sources', '')}",
            row.get("first_evidence", ""))

    def prose(path, fixed_scan=None, changes=False):
        if not path.exists():
            return
        scan = fixed_scan
        in_appendix = False
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            if APPENDIX_START in line:
                in_appendix = True
                continue
            if APPENDIX_END in line:
                in_appendix = False
                continue
            if changes:
                heading = re.match(r"## Scan (\d+)", line)
                if heading:
                    scan = int(heading.group(1))
                if in_appendix:
                    table_scan = re.match(r"\|\s*(\d{3})\s*\|", line)
                    if table_scan:
                        scan = int(table_scan.group(1))
                    else:
                        continue
            if scan is None or not (in_appendix or re.search(r"crop|rotat", line, re.I)):
                continue
            matches = list(BOX.finditer(line))
            for index, match in enumerate(matches):
                stop = matches[index + 1].start() if index + 1 < len(matches) else len(line)
                tail = line[match.end():stop].split(";", 1)[0][:180]
                rotation = ROTATION.search(tail) if not in_appendix else None
                add(scan, match.groups(), f"{path.relative_to(ROOT)}:{lineno}", line,
                    rotation=rotation.group(1) if rotation else "", in_changes=changes)

    prose(OUT / "SP59_CW_71_changes.md", changes=True)
    for directory in sorted((OUT / "records").glob("scan*")):
        scan = int(directory.name.removeprefix("scan"))
        for path in sorted(directory.glob("*")):
            if path.suffix in (".tsv", ".md"):
                prose(path, fixed_scan=scan)
    for path in sorted((OUT / "scripts").glob("read[0-9][0-9][0-9].py")):
        prose(path, fixed_scan=int(path.stem[-3:]))

    direct = OUT / "crop_register.tsv"
    for index, row in enumerate(read_tsv(direct), 2):
        add(row["scan"], [row[k] for k in ("x0", "y0", "x1", "y1")],
            f"output/crop_register.tsv:{index}", "crop.py appended its invocation arguments",
            label=row["label"], basis="direct crop.py argument ledger", rotation=row.get("rotation", ""),
            mirror=row.get("mirror", ""))

    confirmations = OUT / "metadata/crop_confirmations.tsv"
    for index, row in enumerate(read_tsv(confirmations), 2):
        add(row["scan"], [row[k] for k in ("x0", "y0", "x1", "y1")],
            f"output/metadata/crop_confirmations.tsv:{index}", row["provenance"],
            label=row["label"], basis="explicit root confirmation or explicit transformation record",
            rotation=row.get("rotation", ""), mirror=row.get("mirror", ""))

    aliases = OUT / "metadata/legacy_crop_labels.tsv"
    for index, row in enumerate(read_tsv(aliases), 2):
        key = (int(row["scan"]), tuple(int(row[k]) for k in ("x0", "y0", "x1", "y1")))
        if key not in boxes:
            conflicts.append(dict(scan=key[0], crop_filename=f"{key[0]:03d}_{row['label']}.jpg",
                                  issue="alias lacks an independent recorded box", detail=str(key[1])))
            continue
        add(key[0], key[1], f"output/metadata/legacy_crop_labels.tsv:{index}",
            label=row["label"], basis=row["association_basis"])

    unresolved = {(int(r["scan"]), r["label"]): r for r in read_tsv(OUT / "metadata/crop_unrecovered.tsv")}
    rows = []
    for (scan, box), entry in sorted(boxes.items()):
        issues = []
        if len(entry["rotations"]) > 1:
            issues.append("conflicting rotation values")
        if len(entry["mirrors"]) > 1:
            issues.append("conflicting mirror values")
        if not entry["names"]:
            issues.append("documented box has no filename association")
        for label, bases in sorted(entry["names"].items()) or [("", set())]:
            filename = f"{scan:03d}_{label}.jpg" if label else ""
            own_issues = issues.copy()
            if label and len(named[(scan, label)]) > 1:
                own_issues.append("same filename associated with multiple boxes")
            if (scan, label) in unresolved:
                own_issues.append("explicitly unrecovered label; candidate must not be adopted")
            row = dict(scan=f"{scan:03d}", crop_filename=filename, label=label, element_type="tight_crop",
                       **dict(zip(("x0", "y0", "x1", "y1"), box)),
                       rotation_deg=";".join(sorted(entry["rotations"])),
                       horizontal_mirror=";".join(sorted(entry["mirrors"])),
                       coordinate_status="documented exact tuple", name_association_basis="; ".join(sorted(bases)),
                       in_changes_md="yes" if entry["in_changes"] else "no",
                       sources="; ".join(sorted(entry["sources"])),
                       evidence=" || ".join(entry["evidence"]), issues="; ".join(own_issues), source_crop="", transform_chain="")
            rows.append(row)
            if own_issues:
                conflicts.append(dict(scan=scan,crop_filename=filename,issue="; ".join(own_issues),detail=str(box)))

    for index, alias in enumerate(derivative_rows, 2):
        scan = int(alias["scan"])
        box = tuple(int(alias[k]) for k in ("x0", "y0", "x1", "y1"))
        source_name = f"{scan:03d}_{alias['source_label']}.jpg"
        if box not in named.get((scan, alias["source_label"]), set()):
            conflicts.append(dict(scan=scan,crop_filename=f"{scan:03d}_{alias['label']}.jpg",issue="derivative source-box mismatch",detail=str(box)))
            continue
        entry = boxes[(scan, box)]
        rows.append(dict(scan=f"{scan:03d}",crop_filename=f"{scan:03d}_{alias['label']}.jpg",label=alias["label"],
                         element_type="crop_derivative",**dict(zip(("x0","y0","x1","y1"),box)),
                         rotation_deg=alias["final_orientation_deg"],horizontal_mirror="",
                         coordinate_status="same source box; no additional crop",
                         name_association_basis="explicit root derivative-alias confirmation",
                         in_changes_md="yes" if entry["in_changes"] else "no",
                         sources=f"output/metadata/crop_derivative_aliases.tsv:{index}",
                         evidence=alias["provenance"],issues="",source_crop=source_name,transform_chain=alias["transform_chain"]))

    filenames = {p.name for p in (ROOT / "crops").glob("*.jpg")}
    # Keep filenames listed in prior metadata after an image-free checkpoint restore.
    filenames.update(row.get("crop_filename", "") for row in previous if row.get("crop_filename"))
    filenames.update(f"{scan:03d}_{label}.jpg" for scan, label in unresolved)
    covered = {row["crop_filename"] for row in rows}
    for filename in sorted(filenames - covered):
        match = re.fullmatch(r"(\d{3})_(.+)\.jpg", filename)
        if not match:
            continue
        scan, label = int(match[1]), match[2]
        half = label.startswith("half_")
        special = unresolved.get((scan, label))
        row = dict.fromkeys(FIELDS, "")
        row.update(scan=f"{scan:03d}",crop_filename=filename,label=label,
                   element_type="supplied_half_transform" if half else "tight_crop",
                   coordinate_status="not a tight crop" if half else "unrecovered",
                   name_association_basis="filename inventory only",in_changes_md="not applicable" if half else "no",
                   sources="filename enumeration only; no image opened",
                   evidence=special["provenance"] if special else "",
                   issues="" if half else "coordinates unrecovered; no inferred box substituted")
        rows.append(row)
    rows.sort(key=lambda r: (int(r["scan"]), r["crop_filename"], str(r["x0"])))
    write_tsv(OUT / "crop_register_complete.tsv", rows, FIELDS)
    write_tsv(OUT / "crop_register_conflicts.tsv", conflicts, ["scan","crop_filename","issue","detail"])

    tight = [r for r in rows if r["element_type"] == "tight_crop"]
    missing = [r for r in tight if r["coordinate_status"] == "unrecovered"]
    omitted = [r for r in tight if r["x0"] != "" and r["in_changes_md"] == "no"]
    summary = ["# Crop register provenance", "",
        f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} from text metadata only.", "",
        f"- {len(boxes)} distinct documented original-image boxes.",
        f"- {len(tight)} tight-crop register rows; {len(missing)} with unrecovered coordinates.",
        f"- {sum(r['element_type']=='supplied_half_transform' for r in rows)} supplied-half transformations, listed separately.",
        f"- {sum(r['element_type']=='crop_derivative' for r in rows)} rotations of an existing crop, listed as derivative aliases, not additional boxes.",
        f"- {len(conflicts)} coordinate/name/transformation conflicts or association gaps.",
        f"- {len(omitted)} documented crop rows are not yet cited by box in the current changes.md.", "",
        "Coordinates are copied as exact tuples from the root reader's per-page records and changes log, the older audit register, direct crop.py argument records, or explicit root confirmations. This consolidation reads text metadata and filenames only. Separately authorized numerical geometry recovery is documented in its own provenance reports. The existing complete register is retained as an additional source on later runs so previously documented tuples cannot disappear silently.", "",
        "Filename association is separate from coordinate provenance. Legacy associations match descriptive filenames to documented places; they are labelled accordingly and are not asserted to be recovered shell commands. Direct argument-ledger entries and root-confirmed numerical recoveries are distinguished in name_association_basis.", "",
        "Empty rotation or mirror fields mean that transformation was not explicitly recorded; they do not assert zero rotation or absence of mirroring. The three mirrored scan-024 strips are supplied by an explicit record. The current crop.py ledger has no mirror column, so its rotation records alone do not settle mirroring.", "",
        "The two failed scan-008 correlation searches remain historical and their rejected candidate coordinates are excluded. The later SIFT/RANSAC registration and unique byte-identical pipeline replay recovered (980,950,1240,1155), with reproducing rotation -34 degrees; root explicitly accepted this provenance. See metadata/crop008_recovery_history.md and metadata/crop008_exact_replay.md. No new image reading or transcription change was made.", "",
        "## Unrecovered tight crops", ""]
    summary += [f"- {r['crop_filename']}: {r['evidence']}" for r in missing] or ["None."]
    summary += ["", "## Recorded boxes not currently in changes.md", ""]
    summary += [f"- {r['crop_filename'] or 'scan '+r['scan']}: ({r['x0']},{r['y0']},{r['x1']},{r['y1']})" for r in omitted] or ["None."]
    summary += ["", "## Regeneration", "", "Run `python output/scripts/consolidate_crop_metadata.py` after further pages are recorded. Add `--append-changes` to update only the marked metadata table in CHANGES_EXTRA.md while preserving all other prose. Run records.py build to incorporate that appendix in changes.md. The consolidator reads text files and image filenames only, writes metadata files, and never modifies pages, readings, per-page records, or audit events.", ""]
    (OUT / "crop_register_complete_notes.md").write_text("\n".join(summary))
    if args.append_changes:
        append_changes_table(rows)
    print(f"Recorded boxes: {len(boxes)}; tight rows: {len(tight)}; unrecovered: {len(missing)}; conflicts: {len(conflicts)}")
    for row in missing:
        print("UNRECOVERED", row["crop_filename"])
    for conflict in conflicts:
        print("CONFLICT", conflict)


if __name__ == "__main__":
    main()
