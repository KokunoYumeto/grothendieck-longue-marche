#!/usr/bin/env python3
"""Record the audited fourth-hour results in the required outcome ledger."""
from pathlib import Path

work = Path(__file__).resolve().parents[1]
path = work / 'SECTIONS_OVER_Q_report.md'
text = path.read_text()
rows = {
 'A5': ('A.10–A.11, A.25–A.27, A.29, A.32, A.38, A.40, A.42–A.66, A.68, A.71–A.72, A.75, A.77',
 'Open as a whole: infinite-support ordinary ghosts exist and all lift to full profinite class two. Actual full integral lifts exist at every fixed nilpotent depth and every prescribed finite Magnus modulus; the pair can depend on depth. A.68 retains the full generalized-Jacobian Tate module of each fixed abelian cover. A.72 gives joint local point matching in each fixed finite geometric quotient with full abelianization, including the modular levels. A.71 reduces a fixed-pair full metabelian lift to its full pro-prime lifts. A.75 computes each full obstruction and proves that its augmentation-ideal compatibility term vanishes. A.77 makes one fixed ordinary pair pass all individual root-torsor norm tests in the stated coefficient range and identifies the remaining coherent-norm class. A fixed ordinary pair with all full metabelian obstructions zero remains unconstructed.'),
 'A6': ('A.9, A.49, A.74',
 'Refuted universal all-prime assertion and prime independence by point5 over Q5. A.74 proves the precise general odd-prime comparison: for x in pZ_p, its full Legendre congruence image equals that of the explicit tangent Theta_p(x), while the pro-p abelian quotient first separates them at p^vp(x). Actual full cuspidal parameter projections remain coherent.'),
 'A7': ('A.14–A.18, A.24, A.31, A.34–A.41, A.45, A.49, A.53–A.54, A.56, A.63–A.64, A.67, A.70, A.74, A.78',
 'Open in general: integral labeled realization and the exact geometric conjugator criterion are proved. A.63 recognizes all parameters with lambda or1−lambda=±2^m and their six transforms; A.64 adds ±16p^n under full H-conjugacy. A.70 isolates every rational realization after its explicit finite Kummer enlargement N_lambda. A.78 fixes every ordinary potentially multiplicative local value to lambda exactly and confines all remaining relative exponents to actual cuspidal places, with specified label vectors,24-divisibility and unit-square equations. Recognition from H alone still requires solving these simultaneous equations.'),
 'A12': ('A.2–A.6, A.44, A.47–A.50, A.57, A.69, A.73, A.76',
 'Refuted as printed. Every fixed finite puncture set has an ordinary, nonrational ghost with infinite support and a full class-two lift. A.69 and A.73 give nonconstant joint-character obstructions to prescribed finite-level new-coordinate initialization at every exponent divisible by four. A.76 proves that their exact local tuples already fail to have completed old coordinates, and that every nontrivial completed deviation from a rational point is detected on a positive-density Chebotarev subset. One compatible ordinary tuple for all rational punctures remains unconstructed.'),
 'A15': ('A.25–A.27, A.31, A.38, A.40, A.43, A.46, A.51–A.52, A.55–A.66, A.68–A.69, A.71–A.73, A.75–A.77; B.4–B.5',
 'Open: the continuous cup,24-element class-two fibre, exact weight-three residues, fixed-depth integral lifts and fixed-finite-quotient local matching are proved. A.75 computes the full metabelian Fox obstruction and removes its augmentation-ideal compatibility term for a fixed pair. A.77 gives exact coherent-norm comparisons for an actual quotient. Full countersign sufficiency and the requested relative-sign classification remain.'),
 'L10': ('A.25–A.27, A.38, A.40, A.43–A.44, A.46, A.50–A.66, A.68, A.71–A.72, A.75, A.77',
 'Open: actual full class-two lifts, ordinary integral lifts at each fixed nilpotent depth, and joint local matching for every fixed finite modular quotient with full abelianization are proved. The modular compactifications after pullback are X(6),X(4),X(10),X(14), of genera1,0,13,49. A.71 and A.75 identify the full fixed-pair metabelian problem exactly with its coefficient-prime finite-weight obstruction classes; the extra augmentation-ideal lim1 term vanishes. A.77 proves individual norm-level survival for one fixed pair in its stated range, retaining its coherent-norm class. The full same-pair metabelian lift remains unresolved.'),
 'L14': ('A.25–A.27, A.31, A.55–A.66, A.68–A.69, A.71–A.73, A.75–A.77; B.4–B.5',
 'Open: actual continuous obstruction classes, finite-quotient comparisons, joint-character counterexamples and full Alexander/norm maps are computed. The augmentation-ideal compatibility term in A.75 vanishes; coefficient-power and norm-kernel compatibility maps retain their explicitly stated scope. No full countersign or relative-sign classification is claimed.'),
 'L16': ('A.18, A.67, A.74, A.78',
 'Refuted by explicit good ordinary curves over Q17 with symplectically isomorphic integral Tate modules and different j. A.74 gives full congruence point-to-cusp comparisons on every odd-prime cusp disc, together with exact finite Kummer separation. A.78 proves the positive ordinary potentially multiplicative recognition statement with the full labeled integral comparison.'),
}
lines = text.splitlines()
changed = []
for i, line in enumerate(lines):
    if not line.startswith('| '):
        continue
    cells = line.split('|')
    key = cells[1].strip()
    if key in rows and len(cells) == 5:
        statements, outcome = rows[key]
        lines[i] = f'| {key} | {statements} | {outcome} |'
        changed.append(key)
text = '\n'.join(lines) + '\n'
assert set(changed) == set(rows)
new = (
'A.77 identifies the actual quotient obtained by abelianizing the kernel of the first pro-prime Kummer coordinate. Its coefficient modules are the permutation modules of the compatible radical root torsors, and continuous Shapiro identifies their transition maps with field norms. Every ordinary pair with v3(A)=1 passes each individual odd-prime norm test, including coefficient3: the full affine Galois group is metacyclic with zero Schur multiplier, so the opened Hoshi–Yamasaki theorem applies. The norm polynomial gives the required local elements and the scalar correction supplies completed global preimages. The remaining inverse limit is represented by the exact norm-kernel class, with no compactness inference for the completed prime lattices. Root and local-agent audits passed.\n\n'
'A.78 proves exact equality with the realized parameter at every ordinary potentially multiplicative place. The full coefficient system fixes the positive Tate valuation, equality of the full Kummer class fixes the Tate parameter, and the scalar centralizer preserves the ordered two-torsion labels. The original Tate coordinate series supplies the dyadic closest-pair calculation. Under full H-conjugacy, all relative Kummer exponents are supported only at actual cuspidal places; each has its fixed label vector, is divisible by24, and satisfies the displayed unit-square formula. The simultaneous local regular-coordinate equations remain explicit. Root and birational audits passed, and the exact dyadic certificate was rerun.\n\n'
)
if 'A.77 identifies the actual quotient obtained' not in text:
    text = text.replace('## Source audits and corrections\n', new+'## Source audits and corrections\n')
path.write_text(text)
message = f'Updated {len(changed)} outcome rows and integrated the audited A77/A78 descriptions.\nMain A1 remains Open; report begins INCOMPLETE.\n'
(work/'code'/'update_hour4_report_output.txt').write_text(message)
print(message, end='')
