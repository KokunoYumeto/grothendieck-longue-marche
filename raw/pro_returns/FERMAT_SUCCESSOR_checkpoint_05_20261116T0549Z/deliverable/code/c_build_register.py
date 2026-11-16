"""Build the Part C contribution to the statement register.

This records mathematical proof status separately from source-opening status.
It does not verify any inherited numerical certificate.
"""
import json
import re
from pathlib import Path

base = Path(__file__).resolve().parents[2]
tex_path = base / "deliverable/sections/C_main.tex"
text = tex_path.read_text() + "\n" + (base / "deliverable/sections/C_scope_refutation.tex").read_text()
headings = re.findall(r"\\begin\{statement\}\{(C\.\d+)\}\{([^}]*)\}\{([^}]*)\}", text)
details = {
    1: ("C.1;C.3;C.4", "Finite-group character theory; explicit proof", "Independent reconstruction of LM7_PUSH D.50; preserves all subgroup counts and generation."),
    2: ("C.1;C.3;C.4", "C.1; compactness; profinite Hopficity", "Whole relative automorphism and literal conjugators, not finite-level or endomorphism-only lifting."),
    3: ("C.1", "Milne V.7.5; Hain-Matsumoto 8.5; Marin 4.1-4.3; c_cubic_cm_image.py", "Primary sources opened. Exact CM image and arithmetic commutator proved. Does not by itself certify fixed modular frame identification."),
    4: ("C.1", "C.2;C.3;C.5; coprime complement conjugacy", "Automorphism and compatible conjugators proved. CM pair (I,[i]) now certified by C.5's based modular stack comparison."),
    5: ("C.1", "C.2-C.4; Hain Example 3.14 and sections 3.6,8.4; Milne III pp.102-103; Herfort-Ribes B'", "Based modular-to-fixed-fibre comparison proved, including the unique pure frames and one global sign. Task C.1 closed; LM7 D.19(ii) gives Delta nonzero on the gentle group."),
    6: ("C.2;Lead 6", "C.4-C.5; C.18 reconstruction of LM7_PUSH E.58 and E.65 (R13,R14)", "Parity and subgroup-membership consequences. Quotient already in pure-pronilpotent action kernel; not asserted Galois."),
    7: ("C.2;Lead 6", "C.6;C.18; independent c_g3_frame_test.py, full centralizer enumeration on the Q576 graph", "Every E.58 lift is identity on G2 and nonidentity on G3; every D.46 lift is nonidentity on G2 and identity on G3. Exact fibre-product pattern on G6 proved. One actual Galois element realizes the entire adelic CM pair of the quotient. Complete E.58 G3 matrix and all-level source-action Galois equality remain undetermined."),
    8: ("C.3", "Rank-nullity; read LM7 D.60-D.65", "Correction to R17: numbers are selected small-character dimensions. Numerical ranks not independently rerun."),
    9: ("C.3", "C.2;C.4; LM7 D.61,D.63-D.65 change modules; unresolved Lead 6", "Full-lift existence forces vanishing only modulo induced changes; equality with tower's allowed changes remains unproved."),
    10: ("C.4", "LM7 D.32,D.45 source definitions; c_cm_obstruction.py", "D.32 record not a quotient of B/R_nil(F); corrected relative source K or N. Exact finite nonnilpotence certificate run."),
    11: ("C.4", "C.1;C.2; any certified finite nonlifting hypothesis", "Conditional contrapositive with all three lower conjugator images prescribed. Explicit invariant linear characters for D.32/D.45 are constructed in C.12."),
    12: ("C.4", "Full c_replay_obstructions.py replay; c_central_refinements.py; c_cusp_centralizer_scope.py; Efrat Proposition4.4", "Normalized no-lift certificates independently rerun; explicit central C2 refinements constructed. New finite counterexample: allowing a lower cusp-centralizer frame raises D45 correction rank47 to56 and gives an actual automorphism of B/D10F retaining the lower action. Arbitrary-cusp-frame whole-relative nonextension is not proved. Task C.4 is proved in its source normalized sense, but its wider genuine-peripheral wording requires this qualification."),
    13: ("C.5", "R16: LM7_PUSH D.2,D.52 with D.20,D.21,D.51 inputs; C.1-C.2; Furusho Cor.0.3,Thm.0.5,section5", "Conditional on R16 existence exactly as task permits. Primary gamma bound opened; rank-two coefficient check run. No unconditional new profinite strictness claim."),
    14: ("C.5", "Cyclotomic grading calculation; read LM6 A.49,A.56,A.58", "Positive-weight R16 classes cannot centralize G_Q. R18 scope corrected: no commuting third-derived lifts, not no arbitrary peripheral lifts."),
    15: ("C.6", "C.18 E.58 reconstruction; Enriquez Thm.8.1; Nakamura-Tsunogai-Yasuda Prop.4.4,Prop.4.13,Thm.4.16; C.26-C.28", "Gamma alone is insufficient; folded pentagon blindness, exact affine sieves, and structural perfect-image blindness proved. Primary NTY2010 frame comparison is explicitly Galois-only, although its triangle-cover beta action applies to full GT. Full beta-to-integral-CM comparison remains open."),
    16: ("C.7;Lead 7", "Normalized frame definitions; mod-2 centralizer computation; c_cm_obstruction.py", "Literal unrestricted integral norm-one product refuted by global Gaussian i; C.18 gives the exact corrected surjectivity theorem."),
    17: ("C.7;Lead 7", "Elementary index-two subgroup argument; D8 exact action certificate", "Field-intersection sublemma proved independently; combined with actual CM reciprocity images in C.18."),
    18: ("C.7;Lead 7;C.1;C.2", "C.2;C.5;C.16-C.17; Lozano-Robledo Cor.3.4,Cor.3.7,Thm.4.1; Milne Thm.3.10; Marin rigidity; c_corrected_cm_image.py", "Corrected level-two norm-one product is the whole gentle image. Galois image is its index-two parity kernel, and image of ker Delta equals that kernel. Independent E.58 reconstruction supplies the other coset; E.65 full character reconstructed with continuity and invariance. No claim that parity classifies Galois elements in the full gentle group."),
    19: ("C.2;Lead 8;C.8", "Herfort-Ribes Thm.B'; Kochloukova-Zalesskii Thm.2 section1.1; closed-subgroup pants-cover rank proof", "Primary sources opened; full proof of H torsion-freeness. Faithfulness uses Brown and full profinite cover homology, not pro-prime detection."),
    20: ("C.2;Lead 8;C.8", "C.19; Boggi 2026 Thm.C(iii),Prop.2.4 inspected but its intersection-of-closures step unproved; Boggi-Zalesskii Thm.A(iii)", "Neither lift's membership decided. Proved conditional reduction: the full A5 centralizer equality would force K trivial and exclude both lifts. Published September 2026 source still contains the exact intersection gap; no false-theorem assertion made."),
    21: ("C.8", "Harbater-Schneps; Enriquez; Marin; Nakamura-Tsunogai-Yasuda2010; Dolgushev-Guynee; Lochak-Schneps primary sources opened", "Known statements reduced to exact uses. NTY2010 full-GT versus Galois-only quantifiers checked in full primary PDF. Corrects referee's attribution of Lochak-Schneps question1.4."),
    22: ("C.8", "Bounded two-engine primary-literature search on 2026-11-16", "No complete character/torsion classification or unconditional literature strictness theorem established; no priority claim."),
    25: ("C.4", "C.12; independent c_cusp_centralizer_scope.py exact finite witness", "Overbroad D45 next-layer exclusion is refuted when the cusp may be conjugated. Explicit same-lower-action automorphism supplied. Strongest proved corrected exclusion fixes cusp frame1; no whole-relative existence inference."),
    26: ("C.6", "Exact integral c_folded_pentagon.py; two-cycle and commutator identities", "The folded B4-to-SL2 test is identically true for every gentle pair at every modulus, including E.58. This says nothing about other finite braid quotients."),
    27: ("C.6", "c_affine_pentagon_probe.py and independent c_affine_pentagon_verify.py", "Actual common derived images exhaustively enumerated at moduli3,4,5,8, with literal words and all six two-/three-cycle substitutions. Pentagon is nontrivial at3,5 but preserves the base-image sets. The mod3 target is the existing LM7_PUSH E.17 Ferrari target; no new whole-CM-fibre claim."),
    28: ("C.6", "Elementary subdirect-product proof; c_burau_pentagon_probe.py; independent c_burau_perfect_certificate.py, both twenty- and sixty-coordinate versions", "New structural obstruction to this finite approach: perfect common braid image is independent of every finite solvable source. Explicit reduced-Burau F11 target has perfect common derived image of order120*1320^3, independently proved via four small factors and separating words, retaining all six necessary-gentle substitutions. Every prescribed G6 conjugator value has a commutator representative satisfying this finite pentagon; no full-GT existence inference.")
}
rows = []
for ident, statement, status in headings:
    number = int(ident.split(".")[1])
    answers, depends, notes = details[number]
    rows.append({
        "id": ident,
        "statement": statement,
        "status": status,
        "where_proved": ("sections/C_scope_refutation.tex, Statement " if number >= 25 else "sections/C_main.tex, Statement ") + ident,
        "depends_on": depends,
        "answers": answers,
        "notes": notes,
        "source_verification": "See work/c_references.bib: verified means source opened; inherited proof dependencies and unrun computations separately identified."
    })
assert len(rows) == 26
assert set(details) == {int(x["id"].split(".")[1]) for x in rows}
out = base / "work/c_rows.json"
out.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
print("Wrote", len(rows), "Part C statement rows.")
print("Statuses:", {s: sum(x["status"] == s for x in rows) for s in sorted({x["status"] for x in rows})})
print("Coverage:", sorted({a for r in rows for a in r["answers"].split(";")}))
print("Source opening is not represented as independent proof verification.")
