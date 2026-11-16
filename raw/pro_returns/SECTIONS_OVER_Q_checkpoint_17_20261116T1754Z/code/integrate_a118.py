#!/usr/bin/env python3
"""Idempotent integration of the independently audited odd-place theorem.

The caller first integrates A117.  This script then locates that actual
source input, inserts A118 immediately after it, and updates only the
named metadata/report/audit records.  It does not build a PDF.
"""

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
    if r"\begin{statement}{A.117}" in (work / candidate).read_text():
        anchor = r"\input{" + candidate + "}"
        break
assert anchor is not None, "A117 must be integrated before A118."
entry = r"\input{sections/odd_quartic_subset_norm.tex}"
if entry not in source:
    source = source.replace(anchor, anchor + "\n" + entry)
paper.write_text(source)

metadata_path = work / "notes/register_metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["A.118"] = {
    "answers": "A9; A12; A15; L14; L20",
    "depends_on": "A.85; A.96; actual cyclic quartic-to-quadratic norm map; Kedlaya Theorem4.1.2; exact odd valuation and unit calculations",
    "uses_local_theorem": "no; explicit local norms and the proved local reciprocity isomorphism",
    "manuscript_passages": "cote149; scans56–58,126–127; arbitrary finite quartic old-coordinate initialization",
    "notes": "For any number of factors, w_i^4=x+(1−x)d_i and product d_i=−r² imply (x,2r)=0 over every odd Q_p and R. Gives exact local constancy of every A96 common quartic character on arbitrary old covers, using the actual two-point and root-coordinate maps. For a rationally pointed old cover the A85 finite-character test reduces to the dyadic evaluations. No dyadic vanishing, global Jacobian-class vanishing or completed initialization is asserted.",
}
metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")

report_path = work / "SECTIONS_OVER_Q_report.md"
report = report_path.read_text()
items = {"A9", "A12", "A15", "L14", "L20"}
detail = ("A.118 proves odd and real constancy for every quartic common "
          "character with any number of old coordinates; for rationally "
          "pointed old covers the exact finite initialization test is "
          "therefore concentrated at two.")
lines = report.splitlines()
for index, line in enumerate(lines[:55]):
    if not any(line.startswith("| " + item + " |") for item in items):
        continue
    parts = line.split(" | ")
    if "A.118" not in parts[1]:
        parts[1] += ", A.118"
    line = " | ".join(parts)
    if detail not in line:
        assert line.endswith(" |")
        line = line[:-2] + " " + detail + " |"
    lines[index] = line
report = "\n".join(lines) + "\n"
heading = "## All odd-place quartic subset characters"
if heading not in report:
    report += ("\n" + heading + "\n\n" + stamp +
        ": A.118 proves a local norm identity for arbitrarily many "
        "fourth-power equations. When p is one modulo four, their literal "
        "cyclic quartic norms put (ir)² in the norm group; the actual "
        "restriction from C4 to C2 and −2i=(1−i)² then make 2r a quadratic "
        "norm. When p is three modulo four, the normalized-unit and "
        "valuation equations either make x a square or force the even "
        "valuation required by the unramified quadratic norm. The real "
        "assertion follows from positivity.\n\n"
        "For two old local points the displayed root-coordinate ratios "
        "give exactly these equations. A.96 supplies every common quartic "
        "character, so their evaluations are constant at every odd place "
        "and at infinity. With a rational old base point the constants "
        "are one global class, and reciprocity reduces the full A.85 "
        "finite-character sum to its dyadic value. This applies to the "
        "actual cubic Belyi source and arbitrary other finite puncture "
        "sets. It does not remove the dyadic obstruction, which is the "
        "remaining calculation on that source. The finite certificate "
        "checks five symbolic identities and 7,350 literal Hilbert "
        "evaluations through thirteen odd primes, with all sampled "
        "quartic product classes retained. Root and local_preprint "
        "independently audited the complete proof.\n")
report_path.write_text(report)

marker = "A118 complete norm and character audit"
audit = (stamp + " " + marker +
    ": root and local_preprint independently passed the full saved proof. "
    "Checked cyclic quartic degree and literal norm identities, the actual "
    "C4-to-C2 restriction, inversion, every normalized-unit and valuation "
    "case for p3mod4, the unramified norm group, real positivity, all "
    "two-point/root maps, individual quadratic norms, every A96 negative "
    "subset, and the exact rational-base reciprocity reduction. The "
    "primary Kedlaya Theorem4.1.2 was reopened. The executed certificate "
    "passes five symbolic identities, 2,913 actual rational x values, "
    "6,661 input quartic classes, 11,440 generated product states and "
    "7,350 actual local-root/Hilbert checks at thirteen odd primes. "
    "Dyadic vanishing and completed initialization are not inferred.\n")
for name in ("notes/hour8_root_audits.md", "notes/root_progress.md"):
    path = work / name
    old = path.read_text() if path.exists() else "# Eighth-hour mathematical audits\n"
    if marker not in old:
        path.write_text(old + "\n" + audit)

output = ("Integrated A118 immediately after A117. All-odd-place quartic "
          "subset norm theorem and exact dyadic reduction recorded. "
          "No PDF build performed.\n")
Path(__file__).with_name("integrate_a118_output.txt").write_text(output)
print(output, end="")
