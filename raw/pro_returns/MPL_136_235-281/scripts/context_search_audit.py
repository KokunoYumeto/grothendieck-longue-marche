#!/usr/bin/env python3
"""Record bounded, reproducible per-note searches of the supplied context.

This is a research trace, not a transcription check. It reads no scan images,
does not invoke OCR, and does not modify any frozen page or combined fragment.
Each row gives all-match counts and up to three sample lines for one file/query.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, hashlib, re, subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--context", type=Path, default=ROOT.parent / "context")
args = parser.parse_args()
context = args.context.resolve()
log = (ROOT / "progress.log").read_text()
assert "transcription frozen " in log and "context opened " in log

QUERIES = {
"N01": ["1975", "1976", "first 45"],
"N02": [r"\mathrm{Fil}", "divided powers", "De~Rham"],
"N03": [r"S^+", "filtered", "De~Rham"],
"N04": ["flasque", r"\Gamma_k", "degener"],
"N05": [r"S^{[i]}", "valuation", "divided powers"],
"N06": [r"\mathbb Z_2", "completion", "divisibility"],
"N07": [r"\mathrm{Gr}", "filtration", "divided powers"],
"N08": ["completion", "inverse limits", "IMPL I1"],
"N09": ["divided powers", "ideal", "binomial"],
"N10": ["divided powers", "ideal", "WG2 §2.4 #5"],
"N11": ["De~Rham", "ground rings", "GALOIS E.11"],
"N12": [r"\Gamma", "divided powers", "operations"],
"N13": ["universal", "prorepresent", "coalgebra"],
"N14": ["De~Rham", "linearization", "WG2 §Week #3"],
"N15": ["topos de De Rham", "faisceautisation", "Illusie"],
"N16": ["Fourier", "Chern", "abelian varieties"],
"N17": ["adjoint", "136-shadow-full-faithfulness", "truncation"],
"N18": ["adjoint", "left exact", "graded"],
"N19": ["136-shadow-full-faithfulness", "fully faithful", "truncation"],
"N20": ["136-shadow-full-faithfulness", "cotrunc", "truncation"],
"N21": ["136-shadow-full-faithfulness", "binom", "binomial"],
"N22": ["136-shadow-full-faithfulness", "binom", "graded"],
"N23": ["negligible", "Neg", "GALOIS E.11"],
"N24": ["filtered", "PRETOT A.12", "TOTEX2 D.1"],
"N25": ["negligible", r"I/I", "divided power"],
"N26": ["bounded", "coproduct", "adjoint"],
"N27": ["cofinal", "proobjects", "136-shadow-full-faithfulness"],
"N28": ["saturat", r"\Ext", "negligible"],
"N29": [r"\Ext", "injective", "adjoint"],
"N30": ["acyclic", "adjoint", "GALOIS E.11"],
"N31": [r"\epsilon", "localization", "fully faithful"],
"N32": ["binom", "adjoint", "136-shadow-full-faithfulness"],
"N33": ["acyclic", "136-shadow-full-faithfulness", "truncation"],
"N34": ["negligible", "filtered", "GALOIS G.6"],
"N35": ["adjoint", "derived", "GALOIS E.11"],
"N36": ["quasi-isomorphism", "adjoint", "exact"],
"N37": ["exact", "adjoint", "136-shadow-full-faithfulness"],
"N38": ["spectral sequence", "acyclic", "derived"],
"N39": ["fully faithful", "adjoint", "GALOIS G.6"],
"N40": ["multiplication", "Steenrod", "monoidal enhancement"],
"N41": ["universal", "quasi-coherent", "GALOIS E.11"],
"N42": [r"\Hom", "exact", "universal"],
"N43": ["tensor", "kernel", "GALOIS E.11"],
"N44": ["binom", "136-shadow-full-faithfulness", "presentation"],
"N45": ["coalgebra", "dual", "finite projective"],
"N46": ["coalgebra", "completed", "WG H6"],
"N47": ["coalgebra", "counit", "cotensor"],
"N48": ["completion", "ground ring", "dual"],
"N49": [r"\exp", "universal", "diagonal maps"],
"N50": ["binomial", "integer-valued", "De~Rham"],
"N51": ["adjoint", "module structure", "De~Rham"],
"N52": ["fpqc", "semisimplicial sheaves", "faisceautisation"],
"N53": ["Steenrod", "six operations", "GALOIS G.6"],
"N54": ["Cartan", "De~Rham", "1976"],
"N55": ["Miller", "De~Rham", "filtration"],
"N56": ["Dwyer", "tame", "ground ring"],
"N57": ["Mandell", "Steenrod", "fully faithful"],
"N58": ["Ekedahl", "integer-valued", "binomial"],
"N59": ["Toën", "schematization", "WG H6"],
"N60": ["Horel", "binomial", "B7"],
"N61": ["algebraiz", "analytic", "13.5.3"],
"N62": ["GAGA", "analytification", "quasi-coherent"],
"N63": [r"\Phi_{K,K'}", "Raynaud", r"\mathbb Q/\mathbb Z"],
"N64": ["Barsotti", "partie fixe", "semistable"],
"N65": ["normalité", "algebraiz", "13.5.3"],
"N66": ["polarisation", "polarization", r"M_n"],
"N67": ["Dieudonn", "inertia", "Witt"],
"N68": ["ramification", "monodrom", "integrality"],
"N69": ["EXTPAN", "extension panach", r"\Ext"],
"N70": ["semi-stable", "semistable", "abelian varieties"],
"N71": ["negligible", "localizing", "Gabriel"],
"N72": [r"\Gamma", "linearization", "136-shadow-full-faithfulness"],
"N73": ["binomial", "divisibility", "multiplication"],
"N74": ["semisimplicial", "Simplex", "PRETOT A.12"],
}
notes = (ROOT / "MPL_136_235-281_notes.md").read_text()
note_ids = re.findall(r"^### (N\d{2}) ", notes, re.M)
assert len(note_ids) == 74 and set(note_ids) == set(QUERIES)
paths_result = subprocess.run(
    ["rg", "--files", str(context), "-g", "*.md", "-g", "*.tex"],
    text=True, capture_output=True, check=True
)
paths = sorted(Path(p) for p in paths_result.stdout.splitlines())
assert {p.name for p in paths} == {
    "README.md", "RESULTS_STATE.md", "PURSUING_STACKS_CONTENTS.md", "ps6.tex", "ps7.tex"
}
rows = []
for note_id, queries in QUERIES.items():
    for query in queries:
        found = False
        for path in paths:
            result = subprocess.run(
                ["rg", "-n", "-i", "--fixed-strings", "--", query, str(path)],
                text=True, capture_output=True
            )
            if result.returncode not in (0, 1):
                raise RuntimeError(result.stderr)
            matches = result.stdout.splitlines()
            if not matches:
                continue
            found = True
            samples = [line.split(":", 1) for line in matches[:3]]
            rows.append([
                note_id, query, str(path.relative_to(context)), len(matches),
                "; ".join(s[0] for s in samples),
                " || ".join(s[1][:350] for s in samples)
            ])
        if not found:
            rows.append([note_id, query, "(no match in supplied research context)", 0, "", ""])
research = ROOT / "research"
research.mkdir(exist_ok=True)
with (research / "context_search_audit.tsv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["note_id", "query", "context_file", "total_matching_lines",
                     "sample_line_numbers", "sample_text_first_three"])
    writer.writerows(rows)
manifest = research / "context_manifest.sha256"
manifest.write_text("".join(
    hashlib.sha256(p.read_bytes()).hexdigest() + "  " +
    str(p.relative_to(context)) + "\n" for p in sorted(context.rglob("*")) if p.is_file()
))
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
with (ROOT / "progress.log").open("a") as f:
    f.write(f"research context search trace completed {now}; "
            f"{len(note_ids)} notes, {sum(map(len, QUERIES.values()))} queries, "
            f"{len(rows)} trace rows; source manifest recorded\n")
print(f"Checked {len(note_ids)} note IDs; "
      f"{sum(map(len, QUERIES.values()))} queries; {len(rows)} trace rows.")
print("Queries without any literal match:", sum(int(r[3]) == 0 for r in rows))
print("No frozen file modified.")

