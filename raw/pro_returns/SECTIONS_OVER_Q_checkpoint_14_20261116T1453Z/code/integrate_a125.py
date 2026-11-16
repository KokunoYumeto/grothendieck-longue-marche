#!/usr/bin/env python3
"""Idempotently integrate the audited arbitrary-odd/cubic octic theorem."""

from pathlib import Path
import datetime
import json
import re

work = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M UTC")
paper = work / "SECTIONS_OVER_Q_paper.tex"
source = paper.read_text()
anchor = None
for candidate in re.findall(r"\\input\{(sections/[^}]+)\}", source):
    if r"\begin{statement}{A.124}" in (work / candidate).read_text():
        anchor = r"\input{" + candidate + "}"
        break
assert anchor is not None, "A124 must be integrated before A125."
entry = r"\input{sections/cubic_source_eighth_initialization.tex}"
if entry not in source:
    source = source.replace(anchor, anchor + "\n" + entry)
paper.write_text(source)

metadata_path = work / "notes/register_metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["A.125"] = {
    "answers": "A9; A12; A15; L14; L20",
    "depends_on": "A.85; A.118; A.120; A.121; exact A.123 field-factor maps; cyclic local norms and residue-character calculations",
    "uses_local_theorem": "no; exact local reciprocity, finite-field characters and integral valuation equations",
    "manuscript_passages": "cote149; scans56–58,126–127; full finite octic initialization on the exact cubic source",
    "notes": "Proves odd and real constancy of every common octic character for arbitrary rational old coefficient sets, without a reduction hypothesis. The two-point/mixed-root maps retain the actual quadratic character, and all odd residue cases are checked. The cubic source has zero dyadic evaluation for every A121 character by exact root-coordinate, depth and norm maps. Hence every rationally pointed cubic-source old cover admits finite exponent-eight initialization preserving any finite prescribed old-point set. No completed or across-exponent compatibility is inferred.",
}
metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")

report_path = work / "SECTIONS_OVER_Q_report.md"
report = report_path.read_text()
items = {"A9", "A12", "A15", "L14", "L20"}
detail = ("A.125 proves odd and real constancy for every octic common "
          "character on arbitrary old covers and full finite exponent-eight "
          "initialization on the exact cubic Belyi source, including its "
          "bad prime three and every mixed character.")
lines = report.splitlines()
for index, line in enumerate(lines[:55]):
    if not any(line.startswith("| " + item + " |") for item in items):
        continue
    parts = line.split(" | ")
    if "A.125" not in parts[1]:
        parts[1] += ", A.125"
    line = " | ".join(parts)
    if detail not in line:
        assert line.endswith(" |")
        line = line[:-2] + " " + detail + " |"
    lines[index] = line
report = "\n".join(lines) + "\n"
heading = "## All odd octic characters and the cubic-source finite step"
if heading not in report:
    report += ("\n" + heading + "\n\n" + stamp +
        ": A.125 proves odd-place constancy for every common octic "
        "character of an arbitrary old coefficient cover. Exact "
        "two-point equations retain each global mixed-relation root "
        "up to a local square. The proof treats every odd residue "
        "class: cyclic degree-eight norms when the eighth roots of "
        "unity are present; the weighted quartic-residue/valuation "
        "cancellation when p is five modulo eight; and the actual "
        "local image of i in the old squareclass field when p is "
        "three modulo four. Square first entries and all negative "
        "relations are treated separately. This includes old covers "
        "with colliding reductions. The real comparison is exact too.\n\n"
        "On the cubic Belyi source the old fourth-power valuation "
        "partition still applies, while eighth powers strengthen its "
        "depth bounds. The actual affine and inversion fibre maps "
        "retain every character of the same common field. Lower "
        "quartic norm conditions, the complete A121 mixed relation "
        "list and literal one-factor norms settle every dyadic case. "
        "A85 then initializes one rational eighth-power coefficient "
        "while preserving any finite specified old-point set. "
        "The certificate includes 17,616 odd mixed-character checks, "
        "2,800 actual dyadic old-point pairs, 13,824 mixed-depth "
        "implications and 2,568 evaluations from 112 literal global "
        "common fields, including 688 order-four evaluations and "
        "an actual cross-disc old-point pair at three. Root and "
        "local_preprint independently audited the full proof. "
        "The statement retains finite exponent-eight scope.\n")
report_path.write_text(report)

marker = "A125 complete arbitrary-odd and cubic octic audit"
audit = (stamp + " " + marker +
    ": root and local_preprint independently passed the saved proof. "
    "Checked the exact two-point and mixed-root square corrections, "
    "inversion, Frobenius table, cyclic-eight/quadratic norm map, "
    "all p5mod8 residue and valuation cases, the actual local i-field "
    "contradiction at p3mod4, square first entries and real signs. "
    "Checked all cubic dyadic affine/inversion field-factor maps, "
    "the full mixed relation list, depth-three exponent restriction, "
    "one-factor norm transitivity and A85 finite-point scope. "
    "The executed certificate passes 2,900 sampled odd x values, "
    "1,548 norm/field cases, 10,940 product states, 17,616 mixed "
    "character checks, 2,206 dyadic centres in 976 octic fibres, "
    "2,800 actual old-point pairs, 13,824 mixed-depth implications "
    "and 2,568 global-character evaluations from 112 fibres, "
    "including 688 order-four evaluations and the exact bad-three "
    "cross-disc pair (39368/3,19682/3). Root reran the certificate. "
    "No completed compatibility or full-section consequence is inferred.\n")
for name in ("notes/hour8_root_audits.md", "notes/root_progress.md"):
    path = work / name
    old = path.read_text() if path.exists() else "# Eighth-hour mathematical audits\n"
    if marker not in old:
        path.write_text(old + "\n" + audit)

output = ("Integrated A125 after A124 and before A126: all odd octic "
          "characters and finite cubic-source exponent-eight initialization. "
          "No PDF build performed.\n")
Path(__file__).with_name("integrate_a125_output.txt").write_text(output)
print(output, end="")
