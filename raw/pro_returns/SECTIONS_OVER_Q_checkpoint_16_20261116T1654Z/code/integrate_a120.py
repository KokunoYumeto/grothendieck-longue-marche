#!/usr/bin/env python3
"""Idempotently integrate audited finite quartic initialization on A114's source."""

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
    if r"\begin{statement}{A.119}" in (work / candidate).read_text():
        anchor = r"\input{" + candidate + "}"
        break
assert anchor is not None, "A119 must be integrated before A120."
entry = r"\input{sections/cubic_source_quartic_initialization.tex}"
if entry not in source:
    source = source.replace(anchor, anchor + "\n" + entry)
paper.write_text(source)

metadata_path = work / "notes/register_metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["A.120"] = {
    "answers": "A9; A12; A15; L14; L20",
    "depends_on": "A.85; A.96; A.114 actual cubic source; A.118; exact dyadic valuation, affine and inversion maps",
    "uses_local_theorem": "no; explicit quadratic norms and complete dyadic valuation alternatives",
    "manuscript_passages": "cote149; scans56–58,126–127; finite initialization on the exact nonharmonic Belyi source",
    "notes": "For the actual five-punctured source {0,1,2/3,−1/3,infinity}, every quartic negative-subset character has zero dyadic evaluation. The proof gives two general local lemmas, excludes every cross-boundary move, and retains exact affine/root-coordinate and subset-character inversion maps. Combined with A118 and A96, gives a new rational quartic coefficient preserving any finite prescribed old-point set for every rational base R. No higher-exponent or completed initialization is asserted.",
}
metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")

report_path = work / "SECTIONS_OVER_Q_report.md"
report = report_path.read_text()
items = {"A9", "A12", "A15", "L14", "L20"}
detail = ("A.120 proves finite quartic initialization on the exact "
          "five-punctured cubic Belyi source, for every rational old base "
          "and new puncture while preserving any finite prescribed set "
          "of old local points. Higher exponents remain unresolved.")
lines = report.splitlines()
for index, line in enumerate(lines[:55]):
    if not any(line.startswith("| " + item + " |") for item in items):
        continue
    parts = line.split(" | ")
    if "A.120" not in parts[1]:
        parts[1] += ", A.120"
    line = " | ".join(parts)
    if detail not in line:
        assert line.endswith(" |")
        line = line[:-2] + " " + detail + " |"
    lines[index] = line
report = "\n".join(lines) + "\n"
heading = "## Quartic initialization on the actual cubic Belyi source"
if heading not in report:
    report += ("\n" + heading + "\n\n" + stamp +
        ": A.120 completes the dyadic calculation on P1 minus "
        "0,1,2/3,−1/3,infinity, the actual source of A.114. Equal old "
        "valuation vectors make the normalized symbol entry a square. "
        "Deep points at one boundary are handled by an exact quartic "
        "norm or by the even-valuation norm group of the unramified "
        "quadratic extension. A complete six-row valuation table and "
        "two explicit residues modulo16 exclude every change between "
        "different boundary labels. The affine coefficient maps and "
        "the inversion map on all four root coordinates are written "
        "literally; the transformed subset character differs by an "
        "individual norm symbol, which is proved zero.\n\n"
        "A.118 handles every odd and real place, and A.96 supplies "
        "every quartic common character. The exact A.85 criterion "
        "therefore gives one new rational coefficient at exponent "
        "four while preserving any finite collection of prescribed "
        "old local points, for every rational base and new puncture. "
        "The c=R boundary fibre has a rational factor and is treated "
        "separately. This is a same-source finite initialization "
        "result; it does not provide a compatible completed tuple "
        "or remove the higher-exponent problem. Root and local_preprint "
        "independently audited the proof. The retained certificate "
        "checks all15 subset transports, 2,416 actual local-point "
        "pairs and 193,024 Hilbert evaluations.\n")
report_path.write_text(report)

marker = "A120 complete cubic-source quartic audit"
audit = (stamp + " " + marker +
    ": root and local_preprint independently passed the saved proof. "
    "Checked equal-valuation distance bounds, every deep-disc subset, "
    "the literal norm and all shallow parity cases, the complete "
    "six-row valuation table, both cross-label residues modulo16, "
    "all affine coefficient maps, the inversion/root-coordinate "
    "isomorphism and exact inverse, the subset exponent "
    "j+(j mod2)=2ceil(j/2), the individual-character norm correction, "
    "and the exact A85 finite-point conclusion. The executed certificate "
    "passes five symbolic identities, all15 subset maps, 1,118 centres "
    "in288 quartic fibres, every one of2,416 literal local-point pairs, "
    "and193,024 Hilbert checks from96,512 actual negative-square "
    "relations, with both root signs. Higher exponents and completed "
    "initialization remain unresolved.\n")
for name in ("notes/hour8_root_audits.md", "notes/root_progress.md"):
    path = work / name
    old = path.read_text() if path.exists() else "# Eighth-hour mathematical audits\n"
    if marker not in old:
        path.write_text(old + "\n" + audit)

output = ("Integrated A120 after A119: finite quartic initialization "
          "on the exact cubic Belyi source, with actual local-point "
          "prescriptions. No PDF build performed.\n")
Path(__file__).with_name("integrate_a120_output.txt").write_text(output)
print(output, end="")
