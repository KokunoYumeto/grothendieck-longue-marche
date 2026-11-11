# Dictionary, loop-equation, adelic and splitting contribution

| Task | Statements | Outcome |
|---|---|---|
| A(a) | A.1–A.5, B.m5 | proved in corrected notation; the literal smaller-target outer condition is refuted |
| A(b) | A.1, A.2, A.5 | literal identifications refuted; rigidified Legendre, primed modular group and all ten avatars established |
| A(c) | A.3, B.m2 | proved: GT0 is the pure outer quotient; genuine M groups are extensions |
| A(d) | A.4, D.5; dictionary_matrices.py | proved for the displayed matrix dictionary; all requested levels and additional levels tested |
| B(a) | B.m1, B.m3–B.m6 | full loop and normalized φ systems derived, with generation and target qualifications retained |
| B(b), Lead 1 | B.m2, B.m3, B.m5–B.m6 | proved exact equivalence of §46 with I,II; §47 is a separately typed compatibility |
| B(f), centralizer subtask | B.m7 | proved from the precise known fixed-subgroup input: complex conjugation self-centralizing already in GT0 |
| C(b), projective congruence subtask | C.d1–C.d2 | proved for every actual GT0 solution; raw finite cocycle solutions need not lift |
| C(d), item 3 adelic subtask | C.d3–C.d5 | partly settled: full adelic group and homomorphism constructed; projection to U onto; simultaneous two-factor image unresolved |
| D(a) | D.1 | exact extension and withdrawn formulation identified |
| D(b), item 4 | D.1–D.4, D.6–D.7 | partly settled: existence and normalized uniqueness proved; both strict normalizer and strict order-three torus uniqueness refuted; classification up to conjugacy remains open with explicit H1/H2 reduction |
| D(c) | D.5 | proved: plus norm for the manuscript's trace-one R; requested finite checks complete |
| E contribution | B.m3, B.m5–B.m7, C.d1–C.d5, D.1–D.7; condition inventory | all provided conditions typed and reduced; unresolved φ lifting and adelic image must remain on parent ledger |

## Files and statement counts

Four source sections: `A_dictionary.tex`, `B_manuscript.tex`, `C_algebraic.tex`, `D_splittings.tex`. There are **24** manually numbered statements: **12 Proved, 5 Known, 5 Refuted, 2 Open**. The matching structured ledger is `work/dictionary_results.json`; its identifiers and statuses were programmatically checked against every claim environment in those four files. `work/dictionary_readings.json` contains **22** editorial rows. `work/dictionary_refs.bib` adds four explicitly audited references; existing arithmetic references supply the independently opened survey and Minamide–Nakamura metadata where needed.

## Main deductions

1. The literal prompt erases two essential distinctions. The level-two elliptic moduli stack is a neutral μ2-gerbe over the Legendre line; its rigidification is that line. The tripod group is free rank two, while the primed orbifold group is C2*C3. The checked manuscript retains these distinctions.
2. In §46 the pure outer centralizer is GT0. The normalizer is S3×GT0; the genuine automorphism groups are nontrivial geometric extensions. The change of notation from §45 to §46 is recorded rather than identified silently.
3. The direct change of variables is x=ell1, y=ell0 and f=y^(−b) xi x^(−a), where xi_ab=a[x]+b[y], a+b=nu. Gauge sends (a,b) to (a−n,b+n). The normalized inverse is xi=y^nu f, eta=y^nu f x^(−nu). Substitution proves both directions of I and II; the topological generation/automorphism condition is retained.
4. Genuine profinite torsion conjugacy excludes the local scalar branch that a bare adelic cocycle can retain. It gives the global lift trace(xi R)=1 and the upper triangular implementing matrix V=[[mu,mu B],[0,1]]. Consequently every actual GT0 element preserves every projective congruence kernel before descent is assumed. The SL2 sign on the S-image remains explicit.
5. The scan198(73) norm comparison omits delta. Complex conjugation already disproves its printed form modulo3. Correct norms imply the signs modulo3 and4 algebraically; class field theory interprets them but is not needed for this implication.
6. The full adelic group is an intrinsic fiber product of two normalizers and GL2. With K=SJ, a=(1−delta)/2, A=alpha K^a, its coordinates are (A^−1 V, beta^−1 V, f^−1 V), modulo three separate global signs. They multiply componentwise. This resolves the scan193 domain warning: A belongs to B even when alpha lies in FJ. The inverse construction chooses V=diag(mu,1); all other choices are the stated gauge. Bad fibers at2 and3 remain in the integral group schemes.
7. Strict uniqueness of the S-normalizer section fails modulo7. Strict uniqueness of the R-torus section also fails: lift the adelic matrix with R² at3 and I elsewhere, and conjugate the section. Its abelianization is nonzero modulo3; an element with mu3=4 distinguishes the sections modulo characteristic abelian9. Their congruence matrices agree at every level because the R-centralizer is commutative. These counterexamples are conjugate sections, so the global H1 classification is not thereby decided.
8. The norm in scan209 is c²+cd+d² because the specified R has trace+1. At3 the point c=d=1 is singular for the correct plus norm and would be invertible under the wrong minus norm. The supplied correction-list parenthetical favoring minus is itself incorrect for this fixed matrix.
9. Literal Λ∈F in scan229 is not an outer invariant: Int(x) requires Λ=sx^−1 outside F, detected modulo2. Ordinary outer compatibility needs target-inner conjugacy by B. Strict normalized compatibility is a different, fully proved condition.
10. The alternate cyclic φ equation (47) and transposition equation (49) are equivalent by checking the free bases (y,z) and (y,x). For (57),(58), the conjunction is proved equivalent; “either” without standing hypotheses is not asserted. The normalized finite label i is determined by i=nu mod2, hence by mu mod4; j′ is still a separate finite reduction label.
11. Lochak–Schneps Proposition4(i),(ii), opened in the primary article, gives the fixed-subgroup input for c. The supplied proof uses only relationII. Our explicit normalized-coordinate and global matrix argument gives the GT0 conclusion and corrects scan253's nu=±1 to nu=0 or−1.

## Computations actually run

`LM2_LOOP_EQUATIONS/code/dictionary_matrices.py`, standard Python only, with `.out` and `.json`:

- Nine levels: 2,3,4,5,6,7,8,12,24. Tests R³=−I, S²=−I, Linfty L1 L0=−I, cyclic/transposition action on loops, J S J^−1=−S, and both P060 first-return words.
- Exhaustive GL2 centralizer enumeration at all nine levels, including all matrices at2,3,4; centralizer sizes3,6,12 at those required levels.
- Restricted C2 section counts: 1,6,4,16,6,28,24,48,288; corresponding S-algebra-normalizing counts:1,2,4,4,2,4,8,16,32. These are explicitly restriction-to-C2 counts, not counts over an invented finite GT domain.
- Explicit level7 normalizer counterexample, including a word L0^(−2)L1L0^(−2) for its conjugator.
- Witt ranks through12:2,1,2,3,6,9,18,30,56,99,186,335. H1/H2 under C2 computed from the actual parity action on each free Lie module.
- Adelic reconstruction of288 valid normalizer triples at3 and1152 at5, across all four sign pairs. At each prime,256 products and512 associativity triples passed; associativity is also proved intrinsically through the normalizer fiber product.
- Missing-delta and smaller-conjugator counterexamples printed.
- Order-three splitting check: projective mod3 group order12, derived subgroup order4, R² outside it; all72 vectors modulo9 nonzero modulo3 survive multiplication by−3.

## Sources and scans actually opened

Read the corrected transcription, with detailed use of LM_P060 and both first returns, LM_P068-069, the §43–44 checked packages, LM_C3-169-187, LM_C3-188-206, LM_C3-207-225, LM_C3-226-244 and LM_C3-245-263, plus the beginning of §48. The subsection, folio and scan pointers are retained in the source sections and ledger. The condition inventory does not substitute LM3's conclusions for the primary definitions.

Visually inspected available images140-3/18,19,20,209,213,217,229,230,231,237,245. Additional images for many cited pages (including193,198,250,253) are absent from the supplied scan subset; those uses are explicitly checked-transcription uses, not claims of scan inspection.

Opened the supplied Harbater–Schneps primary paper, especially Main Theorem(a), §1.2 Proposition2/Theorem1, §1.3 Propositions3–4/Theorem2 and their proofs; Minamide–Nakamura p8 for the actual cited Herfort–Ribes torsion theorem; Schneps's survey §1.4(1). After search recovered from earlier HTTP503 failures, opened Farb–Margalit version5.0, Theorems4.6 and8.8 and surrounding proofs, and Lochak–Schneps1997, Proposition4(i),(ii), §2 proof on printedp581. We checked the exact hypotheses and reductions used, not every imported theorem of these works.

Herfort–Ribes1985 is deliberately marked **unverified primary**: its theorem is corroborated in the supplied primary sources, but attempts to open its own proof through EuDML, DigiZeitschriften and publisher endpoints failed. Bibliographic metadata was confirmed on Ribes's publication page. No theorem-number guess is used for an unopened centralizer subclaim.

## Exact limits

C.d5 leaves full simultaneous realization of the two adelic normalizer factors undecided, already in the determinant-one fiber over U=I and its mod3 shadow. Constructing every adelic matrix point does not solve the profinite conjugator and generation lifting problem. D.6 leaves sections up to geometric conjugacy undecided, including the constrained H1 over C(3); the first global abelian coefficient module is Zhat(1)^2. The H2 lifting obstruction and H1 choice torsor are derived, and the C2 restrictions computed. The root's full finite/characteristic computation ledger supplies the larger finite-image tasks; this contribution does not claim that its restricted counts answer all of B(e).

No priority is claimed. This is AI-produced proof work by GPT-6 Astra, OpenAI, ChatGPT Pro mode.
