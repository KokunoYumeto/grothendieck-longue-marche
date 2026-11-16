#!/usr/bin/env python3
"""Idempotently integrate the independently audited cubic fibre comparison."""

from pathlib import Path
import datetime
import json

work = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M UTC")

paper = work / "SECTIONS_OVER_Q_paper.tex"
source = paper.read_text()
anchor = r"\input{sections/relative_norm_forms_agent.tex}"
entry = r"\input{sections/cubic_belyi_fibre.tex}"
assert anchor in source
if entry not in source:
    source = source.replace(anchor, anchor + "\n" + entry)
paper.write_text(source)

metadata_path = work / "notes/register_metadata.json"
metadata = json.loads(metadata_path.read_text())
metadata["A.114"] = {
    "answers": "A5; A9; A12; A14; A15; L12; L14; L20",
    "depends_on": "A.76; A.97; exact Kummer composita and Chebotarev; displayed cubic Belyi cover and its sign torsor",
    "uses_local_theorem": "no",
    "manuscript_passages": "cote149; scans56–58,126–127; exact finite source-cover comparison before transporting a puncture obstruction",
    "notes": "Completed Kummer classes vanishing at all nonsplit primes of a nontrivial quadratic field have at most its one explicitly classified cyclotomic-primary component. Gives the actual degree-three cover from the five-punctured line and its full Selmer-fibre bijection when the sign class is nontrivial and either the primary exception is absent or every prescribed finite local centre is rational. Retains geometric conjugacy, real Selmer lifting and the D=1 exclusion. No obstructed completed tuple on this source is asserted.",
}
metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")

report_path = work / "SECTIONS_OVER_Q_report.md"
report = report_path.read_text()
items = {"A5", "A9", "A12", "A14", "A15", "L12", "L14", "L20"}
detail = ("The explicit cubic Belyi cover has a proved full Selmer-fibre "
          "bijection in its nontrivial-sign range, using quadratic-coset "
          "Kummer detection and the stated rational-centre exception. "
          "An obstructed completed tuple on that exact source remains unconstructed.")
lines = report.splitlines()
for index, line in enumerate(lines[:55]):
    if not any(line.startswith("| " + item + " |") for item in items):
        continue
    parts = line.split(" | ")
    if "A.114" not in parts[1]:
        parts[1] += ", A.114"
    line = " | ".join(parts)
    if detail not in line:
        assert line.endswith(" |")
        line = line[:-2] + " " + detail + " |"
    lines[index] = line
report = "\n".join(lines) + "\n"
heading = "## The cubic Belyi source and quadratic-coset detection"
if heading not in report:
    report += ("\n" + heading + "\n\n" + stamp +
        ": A.114 proves that a completed multiplicative class trivial at every "
        "unramified nonsplit prime of a nontrivial quadratic field has no "
        "primary component except possibly the unique coefficient prime whose "
        "cyclotomic tower contains that field. The proof treats both actual "
        "Kummer compositum cases, the coherent two-primary signs and the full "
        "exception list; explicit idempotent classes prove the remaining "
        "exception is necessary.\n\n"
        "The polynomial27T²(1−T)/4 is treated on its actual source, P1 minus "
        "0,1,2/3,−1/3,infinity. Its monic fibre cubic has discriminant "
        "(4/9)²3t(1−t). Local ordinary fibres give fixed letters; Chebotarev "
        "eliminates three-cycles, and a nontrivial global sign leaves exactly "
        "one global fixed sheet. The lifted full section retains the real "
        "point-or-cusp condition. At nonsplit sign primes its old coordinates "
        "are the prescribed ones. The coset lemma recovers them globally "
        "outside the one possible coefficient, and A.97/A.76 remove that "
        "exception when the prescribed finite centres are rational. This "
        "proves the specified full Selmer-fibre bijection. The trivial-sign "
        "case is explicitly excluded, and no source obstruction is inferred. "
        "The next arithmetic problem is to construct an obstructed completed "
        "tuple on this same five-punctured source.\n")
report_path.write_text(report)

audit_marker = "A114 source and certificate audit"
audit = (stamp + " " + audit_marker +
    ": root and local_preprint independently passed the complete saved proof. "
    "Checked both Kummer translation/compositum cases; the positive-real-root "
    "abelian argument and coherent two-sign limit; every cyclotomic exception "
    "and explicit invisible primary class; the exact cubic, discriminant and "
    "Kummer maps; unique geometric fixed-coset lifting; finite and real Selmer "
    "transfer; and A97/A76 recovery with its rational-centre scope. The retained "
    "certificate passed all6 S3 subgroups,4946 translation derangements,1342 "
    "internal quadratic-coset checks,13 exact Gauss-sum squares,16 unit-square "
    "quotients and4872 local power tests. No source obstruction or general "
    "H-only recognition is asserted.\n")
for name in ("notes/hour7_root_audits.md", "notes/root_progress.md"):
    path = work / name
    text = path.read_text()
    if audit_marker not in text:
        path.write_text(text + "\n" + audit)

output = ("Integrated A114 after A113: exact quadratic-coset detection and "
          "specified cubic-cover Selmer fibres. Both A1 assertions and the "
          "actual obstructed tuple on this source remain open.\n")
Path(__file__).with_name("integrate_a114_output.txt").write_text(output)
print(output, end="")
