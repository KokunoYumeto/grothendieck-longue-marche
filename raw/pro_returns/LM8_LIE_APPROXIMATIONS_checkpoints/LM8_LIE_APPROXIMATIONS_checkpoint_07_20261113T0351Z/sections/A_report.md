INCOMPLETE: unrestricted profinite finite-action realization in A(e) remains under investigation.

| Requested task | Statements | Outcome/state |
|---|---|---|
| Item 1, finite-action L-groups | A.1–A.18 | Discrete assertion proved; geometric-closure realization enlarged; unrestricted profinite realization unresolved |
| A(a), definitions | A.1, A.2, A.13 | Precise discrete/profinite definitions; PiL heading not an independent definition; LT uniqueness refuted and repaired |
| A(b), realization theorem | A.3–A.5 | Every hyperbolic discrete L extension realized, including ineffective and reversing actions |
| A(b), finite program | A.7, A.8, A.10 | Exhaustive within declared closed-genus-two and signature boxes; not an exhaustive unbounded-puncture or orientation-reversing action enumeration |
| A(c), realization ambiguity | A.6, A.9 | Aut/Out marking torsors and geometric orbit spaces; three examples |
| A(d), centralizers and Teichmüller groups | A.3, A.4, A.7–A.9 | Centralizer criterion proved; proposed modular characterization refuted; ineffective gerbe automorphisms retained |
| A(e), profinite counterparts | A.11–A.18 | Definitions, centralizers and torsors proved; realization proved in the entire geometric closure for S1,1 and for solvable finite groups in oriented genus≤2 closures; bare free-profinite analogue refuted; arbitrary peripheral action unresolved |

## Main mathematical decisions

The manuscript's colimit is over invariant loop structures on normal finite-index surface groups. The defining surface is hyperbolic. An orientation line is retained without selecting its generator; choosing one defines the direct subgroup. A.3 reduces the finite extension to its outer action using an explicit pullback in Aut(P)×Q and applies Kerckhoff's Nielsen realization theorem. This does not assume that the extension splits. The centralizer of P is exactly the ineffective finite kernel.

The product of two closed genus-two surface groups exposes a defect in the germ-only LT definition: either factor satisfies the empty-peripheral existence condition and they are not commensurable. The correction is to retain the defining commensurability class as data. The same defect persists profinitely.

The modular characterization proposed on scans185–188 fails already for C2*C4 with its one cusp. Its index-four torsion-free kernel is the once-punctured-torus group, its oriented outer L-group is trivial, and all finite-index subgroup centralizers are trivial. Its abelianization has order8, distinguishing it from PSL2(Z). The valid modular facts are separately proved: all six epimorphisms C2*C3→S3 are conjugate, their kernel is characteristic, and the full discrete L automorphism group is PGL2(Z).

The profinite proof does not import center-freeness from the earlier AI return. It derives it from the faithful action of a finite deck group on rational first homology of a regular surface cover. The same argument proves that centralizers of open subgroups vanish, yielding the full profinite centralizer criterion without assuming a profinite unique-roots theorem. Boggi–Zalesskii Proposition3.6 supplies the precise peripheral normalizer theorem needed for the profinite definition.

The arithmetic action on [(P1−{0,1,∞})/S3] makes the full continuous outer L-group surject onto Zhat units. Thus replacing the profinite automorphism group by its discrete counterpart loses actual arithmetic automorphisms. This counterexample does not decide whether every finite subgroup can be realized geometrically.

## Finite computations actually run

`python code/a_small_actions.py` completed successfully. It constructs multiplication tables for all24 groups of order≤12, validates associativity and inverses, and exhausts generating vectors for all42 Riemann–Hurwitz-admissible faithful closed genus-two group/signature rows. Exactly17 rows are realizable. All normal subgroups of the finite acting groups are enumerated, giving126 ineffective pullback rows. These are existence rows, not Hurwitz-orbit counts.

The separate box has quotient genus0–2, puncture count0–3, at most3 cone points, and cone orders2–12. It contains4368 signatures, 4258 hyperbolic signatures and66 bad orbifold signatures. The program outputs its exact scope and full tables. “Genus≤2” alone permits arbitrarily many punctures, hence infinitely many surface types even for the trivial finite group; no finite table can exhaust that literal interpretation.

Artifacts: `code/a_small_actions.py`, `.json`, `.out`, `code/a_small_signatures.csv`; metadata regenerates with `python code/a_c_metadata.py`.

## Source verification and readings

Kerckhoff (1983), Theorem5, its finite-type discussion in §4, and Theorem7 were opened in the original paper. Orientation-reversing classes are explicitly allowed. The relative-boundary Dehn–Nielsen–Baer statement was checked as Theorem2.3 in the authors' Bering–Qing–Wigglesworth paper. The original Maclachlan–Harvey source cited there was not opened; no independent assertion is attributed to it. Boggi–Zalesskii's Definition1.3 and Proposition3.6 were checked in the original arXiv text, including the algebraically-simple restriction.

Actual supplied images inspected for Part A: scans4,183,185,186,188,193. Other passages were read in the checked transcription. Images179–182 and189–192 are not supplied. The damaged list of excluded types and the (0,1)≅Z phrase are recorded as doubtful; the mathematical results explicitly use 2g−2+n>0, rather than presenting an invented decipherment as text. All manuscript references use cote140-4, section, folio and scan.

## Precise unresolved step and attempted routes

A.12 asks for an invariant discrete hyperbolic surface lattice for an arbitrary finite subgroup of the continuous peripheral outer group, up to conjugacy by a continuous peripheral automorphism. The center-free extension classification solves the problem after such a lattice is given; it does not produce one. Finite monodromy enumeration can certify only discrete actions. The primary peripheral-normalizer theorem recovers cusps and permits restriction, but also does not construct a lattice. LM3 B.8–B.11 distinguish extendible specified discretizations from arbitrary ones; their failure of surjectivity cannot be turned into either a proof or a counterexample to existence of some invariant lattice. LM4 was not supplied.

The additional attack on Fhat2, with its (0,3) and (1,1) structures, now yields the following concrete results.

A.16 gives an explicit involution x↦x^λ,y↦y, where λ is −1 at the prime2 and +1 at every odd prime. Its semidirect product has prime-dependent free rank in its abelianization, so it cannot be the completion of any finitely generated discrete group. This refutes a blanket full-profinite analogue of pro-p Nielsen realization. Every induced action on an individual free pro-prime quotient is nevertheless geometric. A48-element metabelian quotient detects failure of the standard torus peripheral condition; tripod homology detects failure even after an arbitrary marking change. Thus this is not passed off as a genuinely peripheral counterexample.

A.17 proves that every finite subgroup of the entire geometric closure for S1,1 is conjugate to a discrete finite subgroup. Bux–Ershov–Rapinchuk's Main Theorem identifies the closure with completed GL2(Z), and Zalesskii–Melnikov's original Theorem3.10 puts every finite subgroup into a vertex group of the profinite dihedral amalgam. All injectivity/nondegeneracy hypotheses are checked. Effective images have nine possible abstract types, all realized. This result is stronger than assuming the action already preserves the initial dense lattice. It constructs a suitable changed marking for any finite subgroup in the closure.

The September2026 theorem of Boggi, Theorem5.1(i), also gives the analogous result for finite solvable subgroups of the oriented geometric closure for every hyperbolic surface of genus≤2. The finite-solvable restriction is retained. The source's “full” mapping class group is orientation preserving and allows puncture permutations; it does not include arbitrary orientation reversal.

A.18 proves necessary global orientation and integral-character tests and explains the remaining obstruction. Tripod realization would force every finite subgroup of GT to be trivial or C2 and would rule out all torsion in its multiplier-one subgroup. The injection into pure peripheral Out is proved explicitly. This is a logical implication, not a claimed classification of torsion in GT. Schneps's1997 torsion question is cited only historically, not as proof of current literature-wide openness. The current2025/2026 finite-subgroup results apply to completions of specified discrete groups; the2026 GT action theorem does not classify finite subgroups of GT. The Herfort–Zalesskii2013 virtual-freeness theorem is pro-p and cannot bypass A.16.

The exact unresolved step is now membership, up to peripheral conjugacy, of an arbitrary finite peripheral subgroup in a geometric closure, or an actual peripheral finite-order counterexample. A surjective cyclotomic multiplier map does not supply finite-order lifts of finite-order units. No literature-wide claim that A.12 is open is made; it remains unresolved in this return.

## Additional exact computation

`python code/a_profinite_obstructions.py` passed. It exhausts all48 elements and all110592 associativity triples of (Z/4)²⋊C3, all48 conjugators of the commutator, all10 subgroups of D8 and all16 subgroups of D12. It records the modulo12 integral-trace obstruction and the nine abstract subgroup types. These finite certificates are exhaustive in their stated groups. They neither enumerate profinite automorphisms nor test the infinite invariant-lattice assertion. Output: `code/a_profinite_obstructions.json` and `.out`.

No priority claim is made. Status counts at this checkpoint:11 Proved,2 Known,4 Refuted,1 Open.
