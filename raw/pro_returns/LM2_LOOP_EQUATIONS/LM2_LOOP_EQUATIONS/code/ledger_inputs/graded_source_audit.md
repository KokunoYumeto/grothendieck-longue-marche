# Graded-equation contribution and audit

| Requested item | Statements | Outcome in this contribution |
|---|---|---|
| B(d), exact graded definition and dimensions | B.g1–B.g4, B.g7, B.g12 | Partly settled for the entire manuscript system; proved for the precisely defined formal loop-and-symmetry envelope. The actual profinite associated graded is only shown to inject. |
| Recent results 1 | B.g1–B.g4, B.g12 | Partly settled: two separate exact spaces computed through 12; no unsupported descent of congruence conditions. |
| Recent results 2 | B.g3–B.g5, B.g7 | Proved in the corrected formulation: first excess 4 for two/three alone, 7 after special identity; no computed violation of the Galois lower bound. |
| Recent results 3 | B.g6–B.g9, B.g12 | Partly settled: typed completion chain, direct special-from-pentagon proof, conditional equality and precise audit. Root's condition register assigns each manuscript condition. |
| Recent results 4 | B.g13 and the preceding one-line answer | No level-2/4 identification found; a concrete distinction between integral incidence reduction and naive reduction of hyperplanes is proved. |
| B(f), pro-l torsion and explicit solutions | B.g5, B.g10–B.g11, B.g14–B.g15 | Partly settled: complete pro-l finite subgroup order classification, rational and finite nilpotent witnesses, explicit additive formal exponential; actual infinite pro-l/profinite lift unresolved. |

## Principal correction

The review's dimensions `0,0,1,0,1,0,2,1` are correct for S3-invariant **special outer derivations**. They are not the dimensions of equations (1.2) and (1.3) alone. The latter have raw dimensions

`1,0,1,1,2,3,6,10,19,33,62,112`

in weights 1–12; the weight-one line is removed by the normalized commutator condition. The special invariant dimensions are

`0,0,1,0,1,0,2,1,4,2,9,7`.

The missing condition is

`[x,psi(x,y)]-[x+y,psi(-x-y,y)]=0`.

This condition is the infinitesimal consequence of loop preservation and outer S3 commutation; naive homogeneous leading terms of the two group cocycles do not encode the subsequent lifting constraints. We prove this equivalence rather than assuming it. A concrete weight-four polynomial satisfying the two naive linear equations fails to lift in the very next weight; the exact linear system has ranks 4 and 5. This directly demonstrates why the naive graded substitution is insufficient.

The normalized formal space Wlac in this contribution is explicitly the special invariant envelope. We do not assert that every element is the leading term of a profinite solution. Any paper convention equating the actual associated graded with this envelope would erase the remaining lifting problem and must not be used.

## Explicit witnesses and computations run

- `graded_dimensions.py`: exact Lyndon brackets, rational nullspaces through weight12, independent Witt/S3-character check, CSV and integer witnesses.
- `graded_pentagon_witness.py`: verifies the t4 free-fiber derivation representation and evaluates explicit weight7 polynomials. The concise seven-term witness has pentagon coefficient16 at `aaaaabcb` in its action on `a`. Full images are printed to JSON.
- `graded_first_lifts.py`: exact first higher-order group-cocycle check. Weight4 cannot extend to5; weight7 extends to8 with zero eighth coefficient. A complete left-kernel inconsistency certificate is supplied for weight4.
- `graded_rational_jets.py`: compatible genuine group (I),(II) jet through12, using the actual negative BCH logarithm. The even corrections vanish; F9 and F11 have 46 and160 nonzero Lyndon coefficients, common denominator divisors720 and8640. The successful system has242 unknowns and rank229. Both complete associative defects are zero.
- `graded_lazard13.py`: independent modular verification in the finite free class12 Lazard group overF13, of order13^747. Two/three group defects are zero, the normalized substitution is an automorphism, and the seventh-weight pentagon defect coefficient is3 modulo13.
- `graded_preprint_audit.py`: 63 source commutator identities of OpenAI Lemma3.3; 13 rational B3 codimension-two flats; 13,104 exact integer deletion-incidence checks on words of length0 through5. All passed.
- `graded_greedy_jets.py`: preserved unsuccessful mathematical attempt. Setting free coefficients to zero too early creates a tenth-weight obstruction for that choice; this is not a counterexample to existence of another jet. Its output is explicitly distinguished from the successful coupled solve.
- `graded_global_attempt.py` and `graded_block_attempt.py`: preserved larger exact elimination attempts interrupted after constructing the systems or confirming lower blocks. Their partial outputs are not used as proofs. The successful smaller odd-correction solve supersedes them.

The finite Lazard example is **not** one of the requested SL2/S3/S4/A5/PSL2(F7) quotients, and no such substitution should be made in the root report. It is the precise additional nilpotent finite case established by this contribution. No infinite integral lift is claimed. The first uncomputed rational correction is weight13; at prime13 the class<prime Lazard argument also stops there.

## Torsion result and its limits

The normalized lambda=1 pro-l kernel is torsion free by a separated first-nonzero-derivation argument overZ_l. It is also pro-l. Thus a finite subgroup injects into the torsion subgroup of Z_l^times. For odd l all divisor orders of l−1 occur in the arithmetic pro-l image by the coprime complement argument, and at a fixed order all finite subgroups of the full pro-l solution group are conjugate by the kernel. At2 only orders1 and2 occur, with complex conjugation giving order2; we do not assert conjugacy at2. These facts do not classify full profinite torsion and do not give explicit f-coordinates for the odd-prime complements.

We also give an explicit infinite characteristic-zero **additive graded formal** symmetry exp(D_q7) outside GRT1. Its three peripheral logarithms obey x+y+z=0. No unverified Kashiwara–Vergne or associator comparison is used to identify it with an element of GT0(k), much less of a pro-l or profinite group.

## Sources opened and checks

Opened primary attached texts: Harbater–Schneps (2000), definitions/Main Theorem/Propositions2–4; Drinfeld (1990), original Russian Sections4–5 and especially Propositions5.5–5.7; Hain–Matsumoto (2003), Theorems7.3,8.4,9.2,9.8,A.6, Proposition9.6, Lemma8.5, Remark8.6, CorollaryA.10; Brown (2012), Theorem1.1, its stated Conjecture1 consequence and Section1.1. We read the relevant review code only as a comparison, then implemented independent calculations.

OpenAI (2026) Sections2–5 were read and partially audited in detail; the special-identity proof is reproduced in full. The source commutator tables and bounded deletion identities were independently verified. The all-weight transferred pentagon, Proposition3.2, remains imported as **claimed, steps not checked by us** beyond the checks stated in the paper. Sections6–8, especially7.1, are not imported as checked. The conditional consequence of Corollary5.4 is proved without pretending the preprint has been certified.

The supplied Willwacher v4 preprint was opened and its introductory results and start of proof read. Its complete proof is **claimed, steps not checked by us**. The attached Lean comparator was opened and ends with `sorry`; this says nothing against an unprovided formalization, but it is not a proof in the attached package.

The two early live search attempts in this contribution, one using each search engine, returned503 service errors. In the final root review the primary arXiv landing page for2610.15592 was successfully opened and its version4 date28October2026 confirmed. No theorem proof or contemporary literature-status assertion is inferred from a landing page or community report. The bibliography marks opened attached primaries as verified and states exactly which portions were inspected.

## Files for root integration

- `sections/B_graded.tex`: fifteen claims B.g1–B.g15, with the proof and audit text.
- `work/graded_results.json`: fifteen statement rows.
- `work/graded_readings.json`: the mathematical correction to the review's unverified identification; explicitly not a paleographic decision.
- `work/graded_refs.bib`: six bibliography entries, each marked verified by opening the supplied primary text, with scope notes.

All claims in this contribution are either proved, explicitly imported with exact statement numbers and reductions, refuted by an exact certificate, or left open with the verified finite range and exact remaining step. We claim no priority.

## Final finite strengthening, B.g15

The finite characteristic quotient of order13^747 is now proved to contain a genuine non-arithmetic outer equation solution, not merely a Lie-level obstruction. The actual P4 conjugation action on its normal free rank-three fibre descends to the class8 exponent13 BCH quotient N3. Its central full twist acts trivially, so the finite action factors through P4/Z=pi1(M0,5). The IA target has class at most7 and exponent13; the group pentagon therefore retains exactly the computed seventh-weight defect, coefficient3 modulo13. `graded_braid_transfer.py` checks the inverse Artin braid relation, all six degree-one chord actions and the central full-twist cancellation in exact reduced free words. A centralizer argument in N2 shows that normalized representatives of the same outer class differ only in top degree12, which vanishes in the class7 pentagon target. Thus passing to outer classes does not restore arithmeticity. This still does not prove that the finite solution lifts to the full profinite GT0 group.
