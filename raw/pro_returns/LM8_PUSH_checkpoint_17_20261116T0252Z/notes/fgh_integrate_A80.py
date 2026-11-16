"""One-shot authorized A80 integration; retain the audited candidate unchanged."""
from pathlib import Path
import difflib
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
draft = root / "notes/fgh_A80_draft.tex"
canonical = root / "sections/A_wreath64_genus_two.tex"
assert not canonical.exists()
old = draft.read_text()
new = old.replace("% Notes-only A.80 candidate. No canonical integration before full audits.",
                  "% A.80: full root and independent proof/source/code audits PASS.")
new = new.replace("{A.80}{Open}", "{A.80}{Proved}")
for name in ("frontier", "map", "prym"):
    new = new.replace(f"notes/fgh_wreath64_{name}_certificate.py", f"code/a_wreath64_{name}.py")
new = new.replace("Their JSON and stdout are retained.",
                  "Their JSON and stdout are retained; the read-only aggregate replay is\n\\path{code/a_wreath64_genus_two.py}.")
assert new.count("\\[") == new.count("\\]")
canonical.write_text(new)
diff = root / "notes/fgh_A80_registration_editorial.diff"
diff.write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
    fromfile="notes/fgh_A80_draft.tex", tofile="sections/A_wreath64_genus_two.tex")))
files = [canonical, diff]
replays = []
for name in ("frontier", "map", "prym"):
    source = root / f"notes/fgh_wreath64_{name}_certificate.py"
    target = root / f"code/a_wreath64_{name}.py"
    assert not target.exists()
    target.write_bytes(source.read_bytes())
    p = subprocess.run([sys.executable, str(target)], cwd=root, capture_output=True, text=True, check=True)
    assert not p.stderr
    target.with_suffix(".out").write_text(p.stdout)
    assert target.with_suffix(".json").read_bytes() == source.with_suffix(".json").read_bytes()
    replays.append({"source": str(source.relative_to(root)), "canonical": str(target.relative_to(root)),
                    "identical_source": sha(source) == sha(target), "whole_json_byte_equal": True})
    files += [target, target.with_suffix(".json"), target.with_suffix(".out")]
source = root / "notes/fgh_A80_certificate.py"
target = root / "code/a_wreath64_genus_two.py"
aggregate = source.read_text().replace('root / f"notes/fgh_wreath64_{name}_certificate.py"',
                                     'root / f"code/a_wreath64_{name}.py"')
target.write_text(aggregate)
p = subprocess.run([sys.executable, str(target)], cwd=root, capture_output=True, text=True, check=True)
assert not p.stderr
target.with_suffix(".out").write_text(p.stdout)
files += [target, target.with_suffix(".json"), target.with_suffix(".out")]
aggregate_diff = root / "notes/fgh_A80_certificate_registration.diff"
aggregate_diff.write_text("".join(difflib.unified_diff(source.read_text().splitlines(True), aggregate.splitlines(True),
    fromfile=str(source.relative_to(root)), tofile=str(target.relative_to(root)))))
files.append(aggregate_diff)

a = root / "sections/A.tex"
text = a.read_text()
needle = "\\input{sections/A_cyclic_derived_closures.tex}"
assert text.count(needle) == 1
a.write_text(text.replace(needle, needle + "\n\\input{sections/A_wreath64_genus_two.tex}"))
files.append(a)
row = json.loads((root / "notes/fgh_A80_row.json").read_text())
row.update(status="Proved", where_proved="sections/A_wreath64_genus_two.tex",
           depends_on=["A.22", "A.38", "A.41", "A.59", "A.78"],
           notes="Full root and DE proof/source/exact-code audits PASS, with PBC focused all-weight audit PASS. Actual wreath closure and Prym quotient; two persistent ordinary Frobenius fields prove non-CM. A positive-distance E-block kernel with all Prym handles retained, followed by actual SL2 invariance and A38, proves fixedness without assuming every cusp has a rational companion. Only the stated natural genus-two intermediate is settled; universal A45 remains Open.")
register = root / "notes/a_results.json"
rows = json.loads(register.read_text())
assert not any(r["id"] == "A.80" for r in rows)
register.write_text(json.dumps(rows + [row], indent=2, ensure_ascii=False) + "\n")
rowfile = root / "notes/fgh_A80_row.json"
rowfile.write_text(json.dumps(row, indent=2, ensure_ascii=False) + "\n")
files += [register, rowfile]

frontier = root / "sections/A_general_cover_frontier.tex"
before = frontier.read_text()
needle = "that fixed-group frontier and the universal question remain\nopen.\n"
assert before.count(needle) == 1
after = before.replace(needle, needle + r"""

A.80 settles the actual natural genus-two degree-eight intermediate
of the wreath closure \(C_2\wr C_4\), whose derived subgroup
is noncyclic. The remaining marked configuration has component
degrees \((2,0)\), and a cusp can lie on the positive-genus
Prym tail. An exact partial-distance kernel removes the original
elliptic handles while retaining the Prym handles; its non-CM
\(\mathrm{SL}_2\) action then makes every fixed grade Tate.
This settles that actual intermediate at every coefficient prime,
without claiming fixedness for all subgroups of its genus-seventeen
Galois closure.
""")
after = after.replace("No replacement kernel theorem covering these cases is proved here.",
    "A.80 supplies a partial-distance replacement for its actual non-CM\nelliptic Prym configuration. No general replacement covering all\nthese remaining cases is proved here.")
assert after != before
frontier.write_text(after)
frontier_diff = root / "notes/fgh_A80_frontier_editorial.diff"
frontier_diff.write_text("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
    fromfile="A45-before-A80", tofile="A45-after-A80")))
files += [frontier, frontier_diff]
notes = root / "notes/fgh.md"
notes.write_text(notes.read_text() + "\n\n## A.80 registered, 2026-11-16 02 UTC\n\nFull root and DE proof/source/code audits passed; PBC independently checked the complete partial-distance and Tate arguments. The actual natural genus-two wreath intermediate now has both required all-prime assertions. Its new kernel proof permits a positive-genus cusp path with a non-CM Prym block. Exact candidates, source ledgers, independent audits and every original certificate are preserved. Canonical copies were reexecuted with whole-result equality. Scope remains this actual intermediate; universal A.45 is Open. See notes/fgh_A80_integration.json.\n")
files.append(notes)
sources = root / "notes/fgh_A80_sources.md"
sources.write_text(sources.read_text() + "\n## Registration\n\nRoot authorized A.80 after full independent proof/source/code audits. Candidate text remains unchanged; canonical changes are status and executable path editorials only. Exact diffs, canonical executions and hashes are recorded in notes/fgh_A80_integration.json. Existing verified bibliography entries suffice; no new source entry was required.\n")
files.append(sources)
ledger = {"status": "PASS", "authorization": "Root full A80 audit and explicit integration authorization; DE full independent PASS; PBC focused complete-proof gate PASS.",
          "candidate": str(draft.relative_to(root)), "candidate_sha256": sha(draft),
          "canonical": str(canonical.relative_to(root)), "canonical_sha256": sha(canonical),
          "editorial_diff": str(diff.relative_to(root)), "canonical_replays": replays,
          "aggregate_replay": "code/a_wreath64_genus_two.py",
          "changed_paths": [str(p.relative_to(root)) for p in files],
          "hashes": {str(p.relative_to(root)): sha(p) for p in files}}
(root / "notes/fgh_A80_integration.json").write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"status": "PASS", "canonical_sha256": ledger["canonical_sha256"],
                  "changed_paths": ledger["changed_paths"]}, indent=2))
