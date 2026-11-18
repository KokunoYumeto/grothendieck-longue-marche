#!/usr/bin/env python3
"""Record the second work period without changing mathematical statuses."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
p = root / 'SECTION_GHOSTS_report.md'
t = p.read_text()
rows = {
'A.2': ('A.2; A.20–A.21; B.25–B.26; E.66–E.68', 'Undecided. For a fixed pair, full survival requires compatible sections matching the actual local point classes at every nonzero-support place away from the coefficient prime. At coefficient three, all fixed-ramification H2 kernels vanish; only the successive simultaneous H1 matching conditions remain. This is a smaller gate, not an all-depth survivor. Next: decide those conditions for one fixed ordinary ghost.'),
'A.3': ('A.2–A.3; A.30–A.31; E.66–E.68; E.123–E.126', 'Undecided for every prime. Coefficient three now has zero fixed-ramification H2 in every weight. For the constructed support pattern with p congruent to minus one modulo three and v3(p²−1)=1, odd matching layers are automatic, and each even matching layer asks whether all local discrepancy vectors pull back to one global vector; two places witness failure. Full geometric Frobenius freedom at a rational base does not solve these equalities at frozen support primes. Next: compute the effect of odd-layer choices on the following even discrepancies.'),
'A.4': ('A.22–A.29; B.20–B.26; E.66–E.68; E.123–E.125', 'Class-two and class-three continuous tests, including strict c0, are explicit. Boundary matching leaves a finite fixed-ramification H2 kernel; at coefficient three this kernel is zero in every weight. Higher matching remains a separate constraint, specialized to even-layer vector equalities for the constructed support pattern. The obstruction is not decided for every class of every original A.44 output.'),
'B.2': ('E.35–E.38; E.60–E.65; E.70–E.72; E.118–E.125', 'The exact original scaled-factorial exclusion, arbitrary-prefix class-three failure, smaller class-three construction constants, and selected later fixed-depth failures are proved. The order32 exclusion is a first failure of specified local point matching, while unrestricted class-two sections still exist. The complete first-exclusion table remains undecided for the closed remainders and certain original constructions whose dependencies are absent. Next: complete those audits and test the even-layer remainder.'),
'B.3': ('E.20; E.30–E.38', 'Exact fixed-depth and finite-quotient survival are reconstructed, and selected outputs have explicit later failures. This does not prove that every output allowed by A.65 or A.72 fails. E.34 proves rational convergence for the selected increasing-depth construction and identifies the divisibility obstruction to keeping one nonzero ordinary exponent in that sufficient construction. The universal assertion remains undecided.'),
'C.2': ('C.1–C.3; E.110–E.126', 'Odd-prime cover genera and the prime-two exception are proved. The elliptic compact and affine abelian tests at three are reconstructed; even exact coefficient-three point matching in the affine abelian cover does not imply a full pro-three section. The compact-passing remainder and general-prime Selmer computations remain undecided. Next: compare the new even-matching families with further proper-cover quotients.'),
'C.3': ('C.4; A.8; E.50–E.59', 'The compact-system separation lemma and several exact LM4 symmetry counterexamples are independently proved. LM7 central lifting has been recovered and re-proved, including its finite count. Selected positive all-refinement clauses and the GT parity-vanishing configuration comparisons remain pending. No common universal ghost-exclusion theorem has been established.'),
'E.1': ('A.20–A.31; B.20–B.26; E.20; E.30–E.72; E.101–E.126', 'Every prior claim used as a proved input has a new proof in its stated scope. The historical register separates completed reconstructions, partial checks, and missing dependencies. Fixed-depth and exact low-depth audits are now written. Remaining original claims are retained as pending and are not used as authorities.'),
'E.2': ('notes/historical_audit.csv; Part E audit table', 'The complete demanded list has a row. The register currently has 87 historical rows:70 confirmed and17 pending. Missing dependencies include the original harmonic triple and continuous obstruction certificates, some literal class-four constants, and parts of the GT/LM4 positive tower arguments. Local source checks and independent special-case proofs do not certify those entire claims. Next: recover or re-prove each missing step.'),
'L.4': ('A.23–A.24; B.23–B.26; E.66', 'Invisible continuous classes exist, but no universal nonzero first obstruction has been proved. In particular, at coefficient three a boundary-matched predecessor has zero fixed-ramification H2 obstruction in every weight. Its possible failure to preserve boundary matching is a separate H1 condition. Thus this lead cannot be settled merely by pointing to the existence of lim-one classes.'),
'L.5': ('C.1–C.5; C.7–C.8; A.8; E.50–E.59', 'Compact finite separation and exact symmetry counterexamples are proved in their own scopes. Full GT parity vanishing and its explicit finite compiler require further configuration comparisons that have not yet been certified from the available files. The proposed common rigid-object theorem and a universal target for ordinary section ghosts remain undecided.'),
}
out=[]
for line in t.splitlines():
    if line.startswith('| '):
        key=line.split('|')[1].strip()
        if key in rows:
            refs,state=rows[key]
            line=f'| {key} | {refs} | {state} |'
    out.append(line)
t='\n'.join(out)+'\n'
t=t.replace('# SECTION_GHOSTS research report — first-hour work in progress', '# SECTION_GHOSTS research report — ongoing work')
t=t.replace('The independent historical audit continues; an unfinished audit does not refute an earlier theorem.', 'The independent historical audit continues; an unfinished audit does not refute an earlier theorem. At coefficient three, the remaining all-depth gate is now specifically simultaneous boundary matching, because E.66 eliminates the fixed-ramification second-cohomology kernel in every weight.')
t=t.replace('## Typesetting and preservation', '''## Second work period: completed reductions and audits

E.66 proves H²(G_{Q,{3,infinity}}, Z/3^n(w))=0 and its integral continuous counterpart for every weight. The proof treats the two mod-three parities separately, passes through the literal finite coefficient exact sequences, and removes the inverse-limit error using finite first cohomology. E.67 computes the complete global first cohomology in the weights used here. E.68 records exactly what localization at the coefficient prime can and cannot prescribe.

E.123 constructs a modified ordinary family with all pro-three class-two boundary matches. E.124 proves that odd matching layers are automatic for that support pattern. E.125 uses the rational base (5/16,11/16) to make every nonzero-support prime have the same minimal three-adic denominator. At each even weight, matching is then equivalent to equality of all pulled-back local discrepancy vectors, and failure has a two-place witness. These are reductions of the compatibility issue; existence of a class-four section is not counted as resolution or progress toward the main limit assertion by itself.

E.126 proves that the actual rational point cocycle at5/16 has the whole free geometric pro-three group in the kernel of the based Galois action. Inertia at5 and11 supplies the two Frattini generators. This gives full finite geometric Frobenius freedom while retaining the actual higher arithmetic action. It gives neither one prime satisfying infinitely many independent Frobenius conditions nor a compatible ghost tower.

E.40–E.43 re-prove the finite-puncture construction and the exact local nonordinary property of A.196. E.70–E.72 reconstruct the genus-two cyclic-eight cover, its projected norm Selmer bound, every one of the eight local sheets at1129, and the distinction between failure of local matching and failure of unrestricted lifting. The original same-pair class-four claim still requires its literal construction audit.

E.50–E.59 re-prove the available LM4 symmetry statements and the recovered LM7 central lifting argument. The original finite verifiers were restored with their witness hashes checked and executed. The positive full-tower clauses are not inferred from their finite negative detectors. In B.45 the proved assertion is that the allowed set contains a whole coset; it need not equal that coset.

E.60–E.65 retain the earlier constructions' exact exponents and constants. They also repair the overstrong local assertion that an entire odd two-adic shell maps bijectively: the required map is two-to-one there, while a specified half-shell maps bijectively onto the same image. The recursion needs the resulting surjectivity.

The retrieved LM4 checkpoint and its background supplied original proof bodies and small verifier files. They are not copied wholesale into this deliverable. Attempts to retrieve the missing SECTIONS_OVER_Q checkpoint found only its initial background bundle. Personal Context reported that it is disabled. These are recorded retrieval limits, not evidence that the missing proofs are false.

The user's first progress review is due at approximately05:45UTC /06:45CET, three hours after work began. Reviews then recur hourly. Two consecutive reviews without an open row changing status or a main question reducing to a strictly smaller gate require the final incomplete package. No such review has yet occurred; the work continues.

## Typesetting and preservation''')
p.write_text(t)

metadata=root/'notes/root_results.csv'
with metadata.open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['id','status','depends_on','answers','checks','uses_local_theorem','manuscript_passages','notes'])
    data=[
      ('E.40','E.102','E.1; E.2','SECTIONS_OVER_Q A.47: confirmed','Exact maximal-abelian radical-field input.'),
      ('E.41','E.40','E.1; E.2','SECTIONS_OVER_Q A.48: confirmed','Finite prescribed puncture set; ordinary completed tuples, not full sections.'),
      ('E.42','A.25; E.41','E.1; E.2','SECTIONS_OVER_Q A.50: confirmed','Continuous class-two lifting with all pairwise forgetful maps.'),
      ('E.43','none','B.2; E.1; E.2','GT_TOWER_CHECK C.2.3: confirmed; SECTIONS_OVER_Q A.196: local clause only','Over Q(cuberoot3), the prescribed mod-nine frame is nonordinary and noncuspidal. Global nonvanishing is not certified here.'),
      ('E.70','A.25','B.2; E.1; E.2','SECTIONS_OVER_Q A.209: projected Selmer and order32 exclusion confirmed; final same-pair class-four clause pending','Excludes everywhere specified local point matching. Does not assert an empty unrestricted class-two fibre.'),
      ('E.71','E.70; E.102','B.2; E.1; E.2','GT_TOWER_CHECK C.2.2: confirmed','First local-matching failure is class two; unrestricted class-two sections still exist.'),
      ('E.72','E.71','B.2; E.1; E.2','GT_TOWER_CHECK C.2.4: confirmed','No local third obstruction at1129 for any coefficient prime; full local pro-prime lifting away coefficient1129.'),
    ]
    for sid,deps,answers,checks,note in data:
        w.writerow([sid,'Proved',deps,answers,checks,'no','',note])
print('Updated report and precise root statement metadata.')
