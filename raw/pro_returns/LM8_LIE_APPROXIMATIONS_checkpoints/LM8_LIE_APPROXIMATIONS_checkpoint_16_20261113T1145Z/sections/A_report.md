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

## Canonical finite-order equations and the first quotient obstructions

A.19 removes an outer-versus-actual-automorphism ambiguity in the pure tripod case. Every pure common-multiplier outer class has a unique representative

\[
x\longmapsto x^u,\qquad y\longmapsto f^{-1}y^u f,\qquad f\in\widehat F_2'.
\]

The normalization is a group section: the composition conjugator is \(f\phi(g)\), which remains in the closed commutator subgroup. Consequently exact finite outer order lifts to exact finite automorphism order. Its order-\(n\) equations are \(u^n=1\) and \(f\phi(f)\cdots\phi^{n-1}(f)=1\). For multiplier one, the third peripheral conjugator can also be normalized into the commutator subgroup and has the same norm-one property. This additional normalization is essential in the first nonnilpotent exclusion.

A direct integral Magnus-series proof shows that a finite-order automorphism of a free pro-prime group which is the identity on integral abelianization is the identity. A.19 applies this to the actual normalized representative, avoiding any inference that torsion-freeness survives a quotient by inner automorphisms. Thus a hypothetical multiplier-one finite pure action is invisible in every free pro-prime quotient. The normalized conjugators themselves also vanish there.

A.20 proves a sharp restriction on the simplest proposed mixed-sign example. The simultaneous-power substitution \(x\mapsto x^u,\ y\mapsto y^u\) is fully peripheral exactly for the two diagonal signs. Evaluate it at two reflections in \(D_{2m}\): their product is \(r\), whereas the required peripheral power is \(r^u\), which is conjugate to \(r\) only for \(u\equiv\pm1\pmod m\). Requiring this for all \(m\) forces one global sign. The mixed unit that is \(-1\) at 2 and \(+1\) at every odd prime nevertheless gives a peripheral action on the maximal pronilpotent quotient, and its powered-product conjugacy condition holds in every finite nilpotent quotient. It fails in \(D_{24}\), since \(r^7\) is neither \(r\) nor \(r^{-1}\).

The GAP computation code/a_tripod_finite.g exhausts all ordered pairs in every SmallGroups isomorphism type of order 1–48: 250 groups and 293009 ordered pairs. There are no failures below order 24; at order 24, exactly identifiers 3, 4, 6, 8, 12 fail, with 432 failing pairs in total. Thus 24 is the minimum finite witness order for this fixed mixed unit and \(f=1\). This is a catalogue-dependent exhaustive finite conclusion, not a claim about all possible peripheral conjugators. The actual runtime reports GAP 4.15.1 and SmallGrp 1.7.0; both versions and the package installation path are printed in the raw output. The package's official manual §1.1 and §1.3 supplies the complete-catalogue scope.

A.21 isolates the smallest new unresolved case as a nontrivial solution of the displayed system (A–I): a pure tripod involution with multiplier one. It supplies an exact finite lifting criterion using fully invariant finite quotients obtained from all finite groups up to a bounded order. A solution at every level above a fixed nonidentity residue produces a coherent profinite solution by compactness. The proof does not assume that arbitrary finite solutions lift or that transition maps are surjective.

The first nonnilpotent exclusion is stronger than testing individual pro-prime quotients. Every solution of (A–I) has trivial \(f\) in every evaluation to \(S_3\). The proof handles all possible generating-pair types and uses the derived third conjugator. The relatively free rank-two quotient obtained from all 36 evaluations in \(S_3\) has order 972 and derived subgroup order 27. All 27 possible \(f\) values were tested: two satisfy the involution norm, nine admit the third conjugator in the derived subgroup, and only the identity satisfies both.

The independent Python implementation code/a_tripod_checks.py reconstructs this universal \(S_3\) quotient from the six-element multiplication table, checks every substitution on all generator edges, and reproduces all counts. Adding the third conjugator's norm leaves the identity pair \((f,h)\) alone. It also independently checks the \(D_{24}\) multiplication certificate, all 13824 associativity triples and all 24 conjugators, and validates the GAP output. Both programs passed. Their outputs are code/a_tripod_finite.out, code/a_tripod_checks.json, and code/a_tripod_checks.out; the GAP stderr file is empty.

The exact residual is the existence or nonexistence of a nontrivial coherent solution of (A–I) whose conjugator is invisible in every pro-prime quotient and in the universal \(S_3\) quotient. A finite obstruction at some higher level would rule out a prescribed residue. No uniform finite obstruction bound has been proved. Mixed finite orientation multipliers with nontrivial conjugators, and conjugacy of multiplier-minus-one involutions to the geometric reflection, remain additional cases of A.12. The simple \(f=1\) mixed candidate has been excluded completely; it is not a peripheral counterexample.

## A complete involution at the profinite metabelian stage

A.22 advances the pure multiplier-one test beyond a list of excluded finite quotients. It constructs a continuous outer involution on the full free profinite metabelian quotient

\[
M=\widehat F_2/\overline{[\widehat F_2',\widehat F_2']}.
\]

This involution fixes \(x\), conjugates \(y\) and \(xy\) by elements of \(M'\), and satisfies both norm equations exactly. It is invisible in every maximal pro-prime quotient and every evaluation to \(S_3\), but it induces a noninner involution on a preserved quotient of order 75. Thus the existing pro-prime and universal-\(S_3\) exclusions do not eliminate this complete metabelian solution.

The Alexander-module input was checked in the original Chen–Deligne preprint (2017, arXiv:1710.05532v1): Proposition 3.2.1 gives the profinite Magnus embedding, Proposition 4.1.2 describes the completed ring, and Corollary 4.1.5 proves \(M'=Rc\), freely generated over \(R=\widehat{\mathbb Z}[[\widehat{\mathbb Z}^{\,2}]]\) by \(c=[x,y]\). The construction uses this actual profinite module theorem. It does not assume that the extension of the abelianization splits.

A compatible normalized Haar idempotent first projects the prime-to-5 abelian factor to \(C_3\), with both \(X\) and \(Y\) mapping to its generator. Its nontrivial character idempotent gives a summand

\[
eR=\mathbb Z_5[\zeta_3][[s_1,s_2]],\qquad
X=\zeta_3(1+s_1),\quad Y=\zeta_3(1+s_2).
\]

Here \(\mathbb Z_5[\zeta_3]=W(\mathbb F_{25})\) is the unramified quadratic integer ring. The elements \(X-1,Y-1,XY-1\) are units in this summand. With zero extension to the complementary summand, set

\[
r=\frac{-2e}{(X-1)(Y-1)},\qquad
s=\frac{X(Y-1)r}{XY-1},\qquad f=c^r,\quad h=c^s.
\]

The induced automorphism acts on \(M'\) by \(a=1-2e\). Therefore \((1+a)r=(1+a)s=0\), giving both norm identities and exact order two. Division occurs only in the specified summand; the full completed ring is not treated as a domain. The averaging elements are proved compatible in every finite quotient, so the construction is continuous on the full metabelian group.

The finite certificate is \(G=\mathbb F_{25,\mathrm{add}}\rtimes C_3\), where the order-three generator multiplies by \(\zeta_3\). Send \(x\) to \((0,1)\) and \(y\) to \((1,1)\). They generate all 75 elements, and the involution descends to \((v,i)\mapsto(-v,i)\). The generator formulas explicitly prove preservation of the quotient kernel. Inner automorphisms act on the additive radical by \(1,\zeta_3,\zeta_3^2\); none acts by \(-1\). This proves outerness of the finite action and of the original metabelian involution.

The exact standalone program code/a_metabelian_involution.py passed. It checks all 421875 associativity triples, all 5625 automorphism multiplication pairs, all 75 possible inner conjugators, all displayed peripheral and norm identities, and 15 declared finite Haar-idempotent cases with projection compatibilities. Outputs are code/a_metabelian_involution.json and code/a_metabelian_involution.out. These are exhaustive certificates for the stated finite cases. Existence and continuity on the infinite metabelian group are supplied by the proof.

The remaining task is now especially concrete: lift this specified involution from \(M\) to \(\widehat F_2\), preserving the three peripheral conditions and exact order two, or exhibit a finite nonmetabelian obstruction above its order-75 certificate. A successful full lift would refute A.12 already in the pure tripod \(C_2\) case. A failure of this candidate would not settle all of A.12. Neither conclusion is asserted here. The metabelian group is not itself a profinite surface group. Supplement A.23 now proves that this specified solution survives the class-two pro-5 quotient of the index-three kernel, including its nontrivial central second derived subgroup. Its compatible finite reductions have orders 3*5^(10n). A.24 further proves the complete class3/class4 families, of dimensions4 and20 over Z5, and shows that only one class3 point extends to class4. Integral class5 with all20 preceding parameters and the remaining full profinite quotients are the next tests; the supplement has its own result and computation ledgers.

No priority claim is made. Current status counts: 15 Proved, 2 Known, 4 Refuted, 1 Open. The A ledger can be regenerated without changing Part C using python code/a_c_metadata.py --only-a.
