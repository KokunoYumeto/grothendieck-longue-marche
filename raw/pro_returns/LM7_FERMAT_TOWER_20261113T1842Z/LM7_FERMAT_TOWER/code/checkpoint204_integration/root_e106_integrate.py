"""Integrate the completely audited E106 result into the working manuscript."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "LM7_FERMAT_TOWER"
AUTHOR = ROOT / "research_e106"
AUDIT = ROOT / "root_e106_audit"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + "\n"

manifest = read(AUTHOR / "ledger/e_next_ordinary_manifest.json")
audit = read(AUDIT / "audit.json")
assert audit["status"] == "PASS" and audit["statement"] == "E.106"
assert sha(AUTHOR / "ledger/e_next_ordinary_manifest.json") == audit["author_manifest_sha256"]
for row in manifest["files"]:
    assert sha(AUTHOR / row["path"]) == row["sha256"], row["path"]
assert not (BASE / "sections/E_next_ordinary_classes.tex").exists()

pending = {}
reasons = {}
mapping = []
def prep(target, content, why):
    pending[target] = content.encode() if isinstance(content, str) else content
    reasons[target] = why

for p in sorted(AUTHOR.rglob("*")):
    if not p.is_file() or "__pycache__" in p.parts:
        continue
    relative = p.relative_to(AUTHOR)
    target_relative = relative
    if relative == Path("ledger/e_next_ordinary_coverage.json"):
        target_relative = Path("ledger/e106_staging") / p.name
    if relative.parts[:2] == ("ledger", "e106_original_author_freeze"):
        target_relative = Path("code/e106_original_author_freeze") / p.name
    target = BASE / target_relative
    assert not target.exists(), target
    prep(target, p.read_bytes(), "Frozen E106 proof, mathematical program, actual output, complete input or author metadata.")
    mapping.append({"frozen_path": str(relative), "archive_path": str(target_relative),
                    "frozen_sha256": sha(p)})

detail = (
    "E.106 evaluates the third ordinary tower layer through the actual ninth-to-cubic character square on E101's complete unit norm lattice. "
    "Its six arithmetic characters have rank4, so Cl(B3){3}=C9^2+C3 and the old transvection is zero. "
    "The actual horizontal class maps give Cl(L3){3}=C9+C3 and prime3 order3. "
    "Every adjacent and horizontal ideal norm/extension map, all six S-prime classes and the entire principal S-divisor lattice are evaluated. "
    "The horizontal ordinary-unit norm is onto; the vertical ordinary norm quotients are C3^5 and C3^3, with kernels C3+Z3^54 and C3+Z3^18. "
    "The finite exponent a3 is1. Later ordinary layers and the eventual all-level h remain active at this statement."
)

prep(BASE / "ledger/root_e106_audit.json", enc(audit), "Complete root proof, source and copied-execution audit.")
prep(BASE / "ledger/root_e106_audit.md", (AUDIT / "README.md").read_bytes(), "Human-readable root verification scope.")
rp = BASE / "ledger/e_next_ordinary_results.json"
rows = json.loads(pending[rp])
assert len(rows) == 1 and rows[0]["id"] == "E.106"
rows[0]["where_proved"] += "; ledger/root_e106_audit.json and code/e106_root_rebuild"
rows[0]["notes"] += " The complete root proof and mathematical source review passed. The fresh copied run returned exit0 and its entire JSON/Python stdout/GP stdout agree byte for byte, with no exclusions. All36 refreshed author-manifest files were verified; the historical wrapper output is explicitly a new isolated replay."
prep(rp, enc(rows), "Attach the actual completed root audit to the result ledger.")
rp = BASE / "ledger/e_next_ordinary_report.md"
report = pending[rp].decode()
report += "\n## Completed root verification\n\n" + detail + "\n\n"
report += "The root auditor read the complete420-line proof and both final mathematical programs. A fresh copied execution recertified B1, recomputed the literal prime7/73 Frobenii, and rechecked every finite map. All three complete output files agree byte for byte, with no exclusions. The actual root proof/source audit is ledger/root_e106_audit.json. The unit Herbrand input has additionally been checked against Milne VII3.1 and its complete proof. No unreceived peer review is asserted.\n"
prep(rp, report, "Record completed proof, primary-source and fresh-execution verification.")

p = BASE / "LM7_FERMAT_TOWER_paper.tex"
t = p.read_text()
marker = r"\input{sections/E_two_prime_full_family.tex}"
assert t.count(marker) == 1
prep(p, t.replace(marker, marker + "\n" + r"\input{sections/E_next_ordinary_classes.tex}"), "Register the audited E106 section.")

p = BASE / "sections/E.tex"
t = p.read_text()
a = t.index(r"\begin{statement}{E.23}")
b = t.index(r"\end{statement}", a)
addition = r"""

E.106 determines the complete third ordinary layer:
$\operatorname{Cl}(B_3)\{3\}=C_9^2\oplus C_3$ and
$\operatorname{Cl}(L_3)\{3\}=C_9\oplus C_3$.
The ninth-to-cubic character square on the complete
ordinary-unit norm lattice has rank four, so the previous
transvection vanishes. Every actual class norm and extension,
all six S-prime columns, the entire principal S-divisor
lattice and their inverses are evaluated. The horizontal
ordinary-unit norm is onto. The vertical ordinary norm
quotients are $C_3^5$ and $C_3^3$, and both norm kernels
are explicit. Thus the third finite exponent is one;
the later ordinary layers and eventual exponent remain
active at this stage. These conclusions supersede the
third-layer alternatives recorded in the earlier milestones.
"""
prep(p, t[:b] + addition + t[b:], "Update the exact completed case at the original open task.")

p = BASE / "code/assemble.py"
t = p.read_text()
needle = "\ne_rows = []\n"
assert t.count(needle) == 1
block = "\ne_deps['E.23'].append('E.106')\ne_notes['E.23'] += " + repr(" " + detail) + "\n"
t = t.replace(needle, block + needle)
needle = "(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')"
assert t.count(needle) == 1
block = (
    "if (BASE/'sections/E_next_ordinary_classes.tex').exists():\n"
    "    for row in e_coverage:\n"
    "        if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
    "            if 'E.106' not in row['statement_ids']: row['statement_ids'].append('E.106')\n"
    "        if row['task'] in ('E.d','E.follow-up-4'):\n"
    "            row['outcome'] += " + repr("; " + detail) + "\n"
    "            row['remaining_step'] = " + repr(
        "evaluate unrestricted coupled global ramification and particular joint origins outside the completed two-prime families; "
        "continue higher wild cubic stages and higher odd-primary and rational nonabelian quartic targets; "
        "evaluate other-primary and mixed sources, later ordinary norm/class layers, eventual exponent h and phase modulo3^h") + "\n"
)
prep(p, t.replace(needle, block + needle), "Keep the33-task ledger synchronized with the completed third-layer result.")

p = BASE / "code/package.py"
t = p.read_text()
needle = "        ('qa', {'.json', '.jpg', '.md'}),"
assert t.count(needle) == 1 and "('inputs'," not in t
prep(p, t.replace(needle, "        ('inputs', {'.json', '.out', '.bin'}),\n" + needle),
     "Include all six complete portable E106 inputs in the final archive and its hash/read-back checks.")

p = BASE / "ledger/d_original_source_recheck.md"
t = p.read_text()
t += "\nA separate public bibliographic-API route checked OpenAlex, Semantic Scholar and Crossref by the exact Ihara1986 and Coleman1989 DOIs (turn873view0--3 and turn874view0--2). The retrieval service could not open these endpoints. A targeted Semantic Scholar/title search (turn875search family) supplied no readable original. These are access/retrieval outcomes only; the three requested-original proof statuses remain unchanged. No access restriction was bypassed.\n"
prep(p, t, "Retain the actual additional source-access attempt without upgrading proof verification.")

allowed = {BASE / name for name in ["LM7_FERMAT_TOWER_paper.tex", "sections/E.tex", "code/assemble.py",
                                   "code/package.py", "ledger/d_original_source_recheck.md"]}
for p in pending:
    assert not p.exists() or p in allowed, p
changes = []
for p, data in pending.items():
    before = sha(p) if p.exists() else None
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    changes.append({"path": str(p.relative_to(BASE)), "before_sha256": before,
                    "after_sha256": sha(p), "reason": reasons[p]})

dst = BASE / "code/e106_root_rebuild"
assert not dst.exists()
shutil.copytree(AUDIT, dst, ignore=shutil.ignore_patterns("__pycache__"))
with (dst / "README.md").open("a") as f:
    f.write("\n## Archived paths\n\nThe exact historical audit drivers retain their original staging paths. The main owned source is code/e_next_unit_characters.py, its GP source is adjacent, and all six required inputs are in the archive's inputs directory. No previous audit output is overwritten by this integration.\n")
with (BASE / "code/README.md").open("a") as f:
    f.write("\n\n## E106: third ordinary tower layer\n\nRun `python code/e_next_unit_characters.py --gp /absolute/path/to/gp` from any directory after extraction. The program uses the six complete files in the archive's inputs directory; Python3, SymPy and PARI/GP are required. It recertifies the B1 input, computes the two actual prime Frobenii, and verifies the entire character/class-map certificate. Complete author and root outputs are retained. The historical wrapper output is a new isolated replay, labelled with its exact provenance.\n")

(BASE / "ledger/e106_integration.json").write_text(enc({
    "status": "PASS", "statement": "E.106", "root_audit_sha256": sha(AUDIT / "audit.json"),
    "frozen_to_archive_path_mapping": mapping, "changes": changes,
    "original_tasks_still_active": ["D.13", "D.19", "E.23"],
    "build_status": "Working-manuscript integration; the next full PDF/build/render/package checkpoint is separate."
}))
print(enc({"status": "PASS", "statement": "E.106", "changed_files": len(changes),
           "complete_inputs": 6, "mathematical_source_changes": []}))
