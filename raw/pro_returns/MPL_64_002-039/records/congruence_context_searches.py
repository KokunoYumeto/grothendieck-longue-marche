#!/usr/bin/env python3
"""Record actual targeted context searches for each suggested context note."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess

root = Path(__file__).resolve().parents[2]
queries = [
    {
        "item": "C64.CX01", "purpose": "Locate the proposed modular cusp and the reported infinity question.",
        "terms": ["RN099-03", "RN101-04", "place à l'infini", "99–101", "99-101"],
        "files": ["context/README.md", "context/MPL_149_091-136_notes.md", "context/notes/RESULTS_STATE.md"]
    },
    {
        "item": "C64.CX02", "purpose": "Find the explicit equivariant quotient problem and credit the existing LM_P057api R17 formula before describing the present canonical model and independent verification.",
        "terms": ["S\\Gamma_{4,2}", "matrices scalaires", "de façon à l'identifier à l'action", "R17. Scan 569", "det(v,Av)", "LM_P057api (scans 561"],
        "files": ["context/LM_140-2_text.tex", "context/LM_140-2_notes.md"]
    },
    {
        "item": "C64.CX03", "purpose": "Distinguish the earlier modular level-four cover conjecture from the finite octahedron group calculation.",
        "terms": ["M_{1,1}[4]", "x^2+y^2+z^2", "modulo des vérifications", "Ce serait bien"],
        "files": ["context/LM_140-2_text.tex"]
    },
    {
        "item": "C64.CX04", "purpose": "Locate the linear/projective lifting comparison and preserve genuine/outer-action typing.",
        "terms": ["C.r3", "extension \\inserted{centrale}", "réduction mod les", "Il faudrait vérifier que l'hom"],
        "files": ["context/LM2_CONGRUENCE_ROWS.md", "context/LM_140-3_text.tex"]
    },
    {
        "item": "C64.CX05", "purpose": "Locate the unipotent cusp model for the independent finite comparison.",
        "terms": ["T_{\\infty}", "unipotent", "sauf erreur", "RN099-03"],
        "files": ["context/LM_140-3_text.tex", "context/MPL_149_091-136_notes.md"]
    },
    {
        "item": "C64.CX06", "purpose": "Check prior statuses and avoid treating a finite calculation as an all-level GT congruence result.",
        "terms": ["C.d1", "C.d5", "LM4_SUCCESSOR B.38", "LM4_SUCCESSOR E.10", "EXIT_TOWER D.19", "B5"],
        "files": ["context/LM2_CONGRUENCE_ROWS.md", "context/notes/RESULTS_STATE.md", "context/README.md"]
    },
    {
        "item": "C64.CX07", "purpose": "Track the previous square-class correction and separate it from finite determinant/sign characters.",
        "terms": ["C.r1", "C.r2", "C.r3", "widehat{\\mathbb Z}^{*2}", "\\mathrm{Cent}", "faire la vérification"],
        "files": ["context/LM2_CONGRUENCE_ROWS.md", "context/LM_140-3_text.tex"]
    },
    {
        "item": "C64.CX08", "purpose": "Check status and scope of previous boundary and extra-coset claims before stating what this packet does not settle.",
        "terms": ["LM6 F.43", "EXIT_TOWER E.24", "LM7_PUSH E.3", "E.49", "normal-crossings", "refereed"],
        "files": ["context/notes/RESULTS_STATE.md", "context/MPL_149_091-136_notes.md"]
    }
]
records = []
for q in queries:
    argv = ["rg", "-n", "-F"]
    for term in q["terms"]:
        argv.extend(["-e", term])
    argv.extend(q["files"])
    p = subprocess.run(argv, cwd=root, capture_output=True, text=True)
    assert p.returncode in (0, 1), p.stderr
    records.append({**q, "argv": argv, "returncode": p.returncode,
                    "hit_count": len(p.stdout.splitlines()), "hits": p.stdout.splitlines()})

# A scoped absence screen is supporting evidence, not a substitute for reading.
argv = ["rg", "-n", "-i", "modulaire|elliptique|Tate|infini|inertie|congruence|niveau|dégénérescence|degenerescence", "MPL_64_002-039_work/pages"]
p = subprocess.run(argv, cwd=root, capture_output=True, text=True)
assert p.returncode in (0, 1), p.stderr
records.append({"item": "C64.CX01/CX08", "purpose": "Frozen packet terminology screen; absence does not establish absence of an implicit argument.",
                "argv": argv, "returncode": p.returncode, "hit_count": len(p.stdout.splitlines()), "hits": p.stdout.splitlines()})
out = {"date_utc": datetime.now(timezone.utc).isoformat(),
       "scope": "Actual searches; selected matches then read in page/section context. Prior notes are research claims, not image evidence.",
       "queries": records}
dest = Path(__file__).with_name("congruence_context_searches.json")
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"path": str(dest), "queries": [{"item": r["item"], "hit_count": r["hit_count"]} for r in records]}, indent=2))
