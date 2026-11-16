"""One-shot root-authorized A81 registration after full independent audits."""
from pathlib import Path
import difflib
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
draft = root / "notes/fgh_A81_draft.tex"
canonical = root / "sections/A_noncm_prym_double_covers.tex"
assert not canonical.exists()
old = draft.read_text()
new = old.replace("% Notes-only A.81 candidate; full root/independent audit required.",
                  "% A.81: full root and DE proof audits PASS; exact statement precision audited.")
new = new.replace("{A.81}{Open}", "{A.81}{Proved}")
assert new.count("\\[") == new.count("\\]")
canonical.write_text(new)
diff = root / "notes/fgh_A81_registration_editorial.diff"
diff.write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
    fromfile="notes/fgh_A81_draft.tex", tofile="sections/A_noncm_prym_double_covers.tex")))
files = [canonical, diff]
a = root / "sections/A.tex"
text = a.read_text()
needle = "\\input{sections/A_wreath64_genus_two.tex}"
assert text.count(needle) == 1
a.write_text(text.replace(needle, needle + "\n\\input{sections/A_noncm_prym_double_covers.tex}"))
files.append(a)
rowfile = root / "notes/fgh_A81_row.json"
row = json.loads(rowfile.read_text())
row.update(status="Proved", where_proved="sections/A_noncm_prym_double_covers.tex",
           statement="All-prime fixed inertia for original packets on every actual genus-two double cover of an elliptic curve 2-primary isogenous to E, branched at two distinct isogeny-kernel points, with non-CM elliptic Prym. Every nontrivial closed procyclic subgroup with arithmetic normalizer of open G_L-image is contained in conjugate cusp inertia. This includes every wild 2-power torsion enlargement of the explicit A80 curve.",
           notes="Registered after full root and DE proof audits PASS, including exact A59 normalizer statement precision. Actual translated quadratic compositum proves two-group closure without a split-extension assumption, and the actual sigma-h quotient identifies the Prym. Every changed degree/model/path/partial-kernel hypothesis is checked. No new numerical premise: A80 exact canonical certificates are reused. Odd primes permit every finite-field cusp packet; coefficient2 retains the original PartA/A22 scope. No cofinality, finite-refinement or fixed-lift claim; universal A45 remains Open.")
register = root / "notes/a_results.json"
rows = json.loads(register.read_text())
assert not any(r["id"] == "A.81" for r in rows)
register.write_text(json.dumps(rows + [row], indent=2, ensure_ascii=False) + "\n")
rowfile.write_text(json.dumps(row, indent=2, ensure_ascii=False) + "\n")
files += [register, rowfile]
frontier = root / "sections/A_general_cover_frontier.tex"
before = frontier.read_text()
needle = "without claiming fixedness for all subgroups of its genus-seventeen\nGalois closure.\n"
assert before.count(needle) == 1
after = before.replace(needle, needle + r"""
A.81 proves the same conclusions for any actual genus-two double
cover of an elliptic curve two-primary isogenous to the base,
branched at two isogeny-kernel points and with non-CM elliptic
Prym. In particular all wild two-power torsion enlargements of
the A.80 curve are included, with degree \(2\cdot4^{r+1}\)
and \(2\cdot4^{r+1}-2\) cusps. Each is treated through its
actual degree-two model and two-group closure; no fixed-element
transfer through the affine open immersion is asserted.
""")
frontier.write_text(after)
fdiff = root / "notes/fgh_A81_frontier_editorial.diff"
fdiff.write_text("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
    fromfile="A45-before-A81", tofile="A45-after-A81")))
files += [frontier, fdiff]
notes = root / "notes/fgh.md"
notes.write_text(notes.read_text() + "\n\n## A.81 registered, 2026-11-16 02 UTC\n\nFull root and DE audits passed for the actual genus-two double-cover/non-CM Prym family. The statement includes the explicit fixed-group equality and exact open-normalizer containment condition. The wild 2-power enlargements of A80 form an unbounded degree family on the same proper genus-two curve. All changed actual-closure, model, path and prime/packet gates are proved; no new numerical premise was introduced. Universal A45 remains Open. See notes/fgh_A81_integration.json and the preserved statement/registration diffs.\n")
files.append(notes)
sources = root / "notes/fgh_A81_sources.md"
sources.write_text(sources.read_text() + "\n## Registration\n\nRoot authorized canonical A81 after full root and DE proof audits, including the exact statement-precision diff. The old candidate and all source scope notes remain preserved. Registration changes only status/header; no numerical code was added because every actual explicit certificate is already A80's executed canonical certificate. Exact hashes/diffs are in notes/fgh_A81_integration.json.\n")
files.append(sources)
ledger = {"status": "PASS", "authorization": "Root final A81 approval against candidate 0ce62301ea6eecb07c3647f91028c56975230941d4ab4130da20087cc9c91800; full DE independent PASS.",
          "candidate": str(draft.relative_to(root)), "candidate_sha256": sha(draft),
          "canonical": str(canonical.relative_to(root)), "canonical_sha256": sha(canonical),
          "editorial_diff": str(diff.relative_to(root)),
          "statement_precision_diff": "notes/fgh_A81_statement_precision.diff",
          "computation_scope": "No new numerical premise; exact executed A80 canonical certificates reused.",
          "changed_paths": [str(p.relative_to(root)) for p in files],
          "hashes": {str(p.relative_to(root)): sha(p) for p in files}}
(root / "notes/fgh_A81_integration.json").write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"status": "PASS", "canonical_sha256": ledger["canonical_sha256"],
                  "changed_paths": ledger["changed_paths"]}, indent=2))
