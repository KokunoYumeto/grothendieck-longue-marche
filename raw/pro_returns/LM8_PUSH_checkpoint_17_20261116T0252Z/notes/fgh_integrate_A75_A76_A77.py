#!/usr/bin/env python3
"""Authorized integration after checkpoint15 release and all full audits."""
from pathlib import Path
import difflib
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
changed = []

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(rel, text):
    (root / rel).write_text(text)
    changed.append(rel)

specs = [
    (75, "e287d5c6b92735b189199a6579b3c4b80ae86e585ec750162fe65dad48e0927f",
     "A_modular_two_power", "a_modular_two_power",
     "both cusp assertions for modular two-group closures"),
    (76, "b271501e3966da29889faf5297c0a4654c59acc72ab2aeef968dbea59bd88f87",
     "A_cyclic_index_two_abelian", "a_cyclic_index_two_abelian",
     "the whole cyclic-index-two class and its odd abelian extensions"),
    (77, "7752d6addfa2162f0008ee82049a7a062420e4791b865ac6df809614a662e6e0",
     "A_commutator_order_two", "a_commutator_order_two",
     "both cusp assertions when the geometric commutator has order at most two"),
]
new_rows = []
section_inputs = []
records = []
for n, sha, section_name, code_name, title in specs:
    draft_rel = f"notes/fgh_A{n}_draft.tex"
    draft = root / draft_rel
    assert digest(draft) == sha
    original = draft.read_text()
    lines = original.splitlines()
    lines[0] = f"% A.{n}: full root and DE proof/source/exact-certificate audits PASS."
    canonical = "\n".join(lines) + "\n"
    canonical = canonical.replace(
        f"\\begin{{statement}}{{A.{n}}}{{Open}}{{Candidate: {title}}}",
        f"\\begin{{statement}}{{A.{n}}}{{Proved}}{{{title[0].upper() + title[1:]}}}")
    canonical = canonical.replace(
        "\\begin{proof}[Candidate proof, pending complete independent audits]", "\\begin{proof}")
    canonical = canonical.replace(
        "\\begin{proof}[Candidate proof, conditional on the audited A.75 candidate]", "\\begin{proof}")
    canonical = canonical.replace(f"notes/fgh_A{n}_certificate.py", f"code/{code_name}.py")
    assert f"\\begin{{statement}}{{A.{n}}}{{Proved}}" in canonical
    assert "Candidate proof" not in canonical and "{Open}" not in canonical
    section_rel = f"sections/{section_name}.tex"
    put(section_rel, canonical)
    delta = "".join(difflib.unified_diff(original.splitlines(True), canonical.splitlines(True),
                   fromfile=draft_rel, tofile=section_rel))
    put(f"notes/fgh_A{n}_registration_editorial.diff", delta)

    original_code = (root / f"notes/fgh_A{n}_certificate.py").read_text()
    code = original_code.replace(f"A.{n}, unregistered", f"A.{n}, registered after full audits")
    code_rel = f"code/{code_name}.py"
    put(code_rel, code)
    with (root / f"code/{code_name}.out").open("w") as output:
        subprocess.run([sys.executable, str(root / code_rel)], stdout=output,
                       stderr=subprocess.STDOUT, check=True)
    changed.extend([f"code/{code_name}.json", f"code/{code_name}.out"])
    before = json.loads((root / f"notes/fgh_A{n}_certificate.json").read_text())
    after = json.loads((root / f"code/{code_name}.json").read_text())
    assert before["status"] == after["status"] == "PASS"
    before.pop("candidate", None)
    after.pop("candidate", None)
    assert before == after

    row_rel = f"notes/fgh_A{n}_row.json"
    original_row = (root / row_rel).read_text()
    put(f"notes/fgh_A{n}_row_before_registration.json", original_row)
    row = json.loads(original_row)
    row["status"] = "Proved"
    row["where_proved"] = section_rel
    row["notes"] = {
        75: "Registered after full root and DE proof/source/exact-code audits PASS. The unmarked proper stable-tree argument excludes an ordinary anti-Prym; the actual central elliptic quotient gives two-primary cusp differences. Every actual intermediate, prime and permitted packet is included; universal A.45 remains Open.",
        76: "Registered after full root and DE proof/source/exact-code audits PASS, with A.75 proved. The complete cyclic-index-at-most-two classification includes small orders, and the actual connected odd-isogeny pullback preserves rational companion paths. All intermediates are included; no product of two nonabelian Sylow factors or cofinality claim is made.",
        77: "Registered after full root and DE proof/source/exact-code audits PASS. Actual faithful quotient curves and the surjective sum of Jacobian pullbacks prove special rank zero for the two-group source. Actual degree-two cusp divisors and coprime isogeny path comparison handle every intermediate and the automatic odd abelian factors. The whole product of quotient Jacobians is not asserted isogenous to the source. Universal A.45 remains Open.",
    }[n]
    put(row_rel, json.dumps(row, indent=2) + "\n")
    new_rows.append(row)
    section_inputs.append(f"\\input{{{section_rel}}}")

    source_rel = f"notes/fgh_A{n}_sources.md"
    source_text = (root / source_rel).read_text()
    put(f"notes/fgh_A{n}_sources_before_registration.md", source_text)
    paragraphs = source_text.split("\n\n")
    paragraphs[1] = (f"Registered as A.{n} after full root and DE proof/source/exact-certificate audits PASS. "
        f"Canonical proof `{section_rel}` and exact rerun `code/{code_name}.py/.json/.out`. "
        f"The original audited draft and certificate remain preserved. "
        f"Editorial changes are recorded in `notes/fgh_A{n}_registration_editorial.diff`.")
    source_text = "\n\n".join(paragraphs)
    if n == 77:
        source_text += ("\n\nverified: root freshly read the exact primary Serre–Tate Theorem1/Corollary2 "
            "printed493 through the indexed original source, refs turn1208search4/turn1208view0. "
            "Root full ledger is notes/root_A77_audit.md/.json; the prior direct-PDF readability "
            "limitation is retained above as historical provenance.\n")
    put(source_rel, source_text)
    records.append({"id": f"A.{n}", "status": "Proved; all full audits PASS",
        "draft_preserved": draft_rel, "draft_sha256": sha,
        "canonical_section": section_rel, "canonical_certificate": code_rel,
        "certificate_rerun": "PASS; every JSON field equal except registered-status metadata",
        "editorial_delta": f"notes/fgh_A{n}_registration_editorial.diff",
        "root_audit": f"notes/root_A{n}_audit.md", "secondary_audit": f"notes/de_A{n}_audit.md"})

p = root / "sections/A.tex"
s = p.read_text()
needle = "\\input{sections/A_two_group_abelian_products.tex}"
assert s.count(needle) == 1 and all(x not in s for x in section_inputs)
put("sections/A.tex", s.replace(needle, needle + "\n" + "\n".join(section_inputs)))

p = root / "notes/a_results.json"
rows = json.loads(p.read_text())
assert not any(row["id"] in {"A.75", "A.76", "A.77"} for row in rows)
rows.extend(new_rows)
put("notes/a_results.json", json.dumps(rows, indent=2) + "\n")

p = root / "sections/A_general_cover_frontier.tex"
s = p.read_text()
needle = ("factors as well. Products of two nonabelian Sylow factors,\n"
          "arbitrary two-groups and the universal question remain\n"
          "outside these conclusions.")
assert needle in s
replacement = """factors as well.
A.75 completes every actual modular two-group closure and
every intermediate. Its unmarked proper stable-tree argument
rules out an ordinary anti-factor by a generically fixed-point-free
outside involution; no marked-fibre slope assertion is assumed.
A.76 combines these four families into the exact class of
two-groups with a cyclic subgroup of index at most two, including
the small orders and every odd abelian extension through the
actual connected isogeny pullback.
A.77 further completes every geometric closure whose commutator
subgroup has at most two elements, with all intermediates and
the automatic odd abelian factors. Actual faithful quotient
curves supply a surjective sum of Jacobian pullbacks, giving
special rank zero for the two-group source. The order-thirty-two
example has genus nine and sixteen cusps and lies outside the
cyclic-index-two class. Products of two nonabelian Sylow factors,
arbitrary two-groups and the universal question remain outside
these conclusions."""
put("sections/A_general_cover_frontier.tex", s.replace(needle, replacement))

p = root / "notes/fgh.md"
s = p.read_text()
s += ("\n\n## A75–A77 registered after checkpoint15 release\n\n"
      "All three complete proofs passed root and DE independent proof/source/code audits. "
      "Canonical certificates were rerun and agree in every mathematical JSON field. "
      "A75 settles modular closures; A76 gives the complete cyclic-index-at-most-two "
      "class with odd abelian factors; A77 extends to actual closures with commutator "
      "order at most two. Drafts, original outputs and exact editorial diffs are retained. "
      "Universal A45 remains Open; no general two-group special-rank theorem is inferred.\n")
put("notes/fgh.md", s)

for rel in changed:
    if rel.endswith(".tex"):
        data = (root / rel).read_bytes()
        text = data.decode()
        assert not any(c < 32 and c not in (9, 10) for c in data)
        assert text.count("\\[") == text.count("\\]")

record = {"status": "REGISTERED; parent release and all full approvals received",
    "statements": records, "bibliography_changed": False,
    "global_register_report_or_pdf_changed": False,
    "changed_files": {rel: digest(root / rel) for rel in changed}}
put("notes/fgh_A75_A76_A77_integration.json", json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "registered": [x["id"] for x in records],
                  "changed_files": len(changed), "canonical_sections": {
                      x["id"]: digest(root / x["canonical_section"]) for x in records}}, indent=2))
