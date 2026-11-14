# E.41: all unramified cubic sections

## Completed result

For the full rank-ten geometric pro-3 group N, its metabelian quotient N/N'', and the quotient N/gamma3(I_Q) marked at the single rational cusp Q=B0, the entire section set unramified outside 3 is computed as a compatible product of explicit finite-rank lattice cokernels. This strengthens E.34 from existence above all unramified abelian classes to coordinates for every full section in that family.

The geometric quotients and their kernels are the actual maps in E.41.23. The arithmetic origin is the based tangent of E.34. A normalized cocycle has a(c)=1 and is freely specified by its value x at the actual Frobenius generator tau; the value at c tau c is c(x). Its residual conjugation action is w x tau(w)^(-1), w in W^c.

Each successive parameter is the explicit cokernel of (T_r-1)(1+J_r), computed from the complete rank-ten V action. No further stabilizer quotient occurs. Continuous Hall-zero lifts and Smith representatives produce a compatible normal form in every degree. Compactness and the vanishing of every twisted stabilizer prove the inverse-limit bijection and a noncanonical homeomorphism of pointed profinite spaces with the product of these cokernels. The product does not assert a group law on the original section set.

## Integral comparisons proved

The metabelian Fox comparison is proved in the pro-3 category. The completed group algebra of a free pro-3 group is identified with the complete noncommutative power-series ring, with its actual (3,augmentation)-adic topology. The last-letter resolution, completed induced-module comparison and continuous Fox map identify N'/N'' with the closed syzygy kernel in Lambda^10. Homogeneous Koszul exactness proves K intersect m^(k+1) Lambda^10 = m^k K. Thus the integral Chen lattice and its completion are connected by an explicit topological isomorphism.

For the single-cusp marked quotient, Magnus expansions show that gamma3(I_Q) has at least three occurrences of the marked variable. Integral Lazard elimination supplies the reverse inclusion of initial ideals, by actual lifted commutators. The retained Hall words form a torsion-free integral basis in every degree.

## Exact computations and files

- `sections/E_unramified_sections.tex`: statement E.41 and proof.
- `ledger/e_unramified_results.json`: one proved entry, complete required fields.
- `ledger/e_unramified_refs.bib`: three additional opened primary references.
- `code/e_unramified_sections.py`, `.out`, `.json`: executed successfully.

The program constructs the degree-four exact action and cocycle matrices in all three bases, with Python integer sparse arithmetic. It verifies conjugation squared equals the identity, the exact conjugation traces, B_r C_r=3^r I, and the split Frobenius conjugacy. The JSON stores the bases and sparse matrices. Rank and character tables are evaluated through degree ten.

At degree four the full, marked, and metabelian ranks are 2475, 2466, and 1485. Their complex-conjugation traces are -21, -22, and -3, and the free ranks of the new section-coordinate factors are 1248, 1244, and 744. The proven torsion bound is 3^6 in this degree, so modulus3^7 suffices for a Smith evaluation. No degree-four torsion list is asserted without performing that further computation. The finite matrix itself gives the exact group presentation.

The first three factors agree for the three actual quotients:

1. Z3^6 plus C3^3.
2. Z3^24 plus C3^9 plus C9^5.
3. Z3^166 plus C3^7 plus C9^56 plus C27^25 plus C81^3.

## Opened primary passages

Papadima--Suciu, *Chen Lie algebras*, arXiv math/0307087 version1, Corollary5.6 and Theorem6.2 with (6.3)--(6.4), pp11--12: integral Lie and Koszul comparison maps.

Satoh, *On the lower central series of a free abelian by polynilpotent group*, Kyoto preprint2010-05, section2.4, equation(2) and following basis, p5: integral Chen basis and rank formula. The pro-3 passage is proved separately in E.41.

Stoehr, *Bases, filtrations and module decompositions of free Lie algebras*, author preprint section2, p3: Lazard elimination over an arbitrary commutative ring.

Existing opened E.40 sources supply the free pro-p integral graded theorem and Witt character formula.

## Exact remaining scope

E.41 evaluates all sections whose geometric cocycle factors through G_Q,{3,infinity}. It does not replace the full ramified section problem. E.39 gives actual additional inertia coordinates and correction words; E.38 already exhibits ramified classes passing the full intrinsic class-two test and failing class three and the further metabelian/marked quotients. Further work on those ramified higher obstruction images must retain these coordinates and maps.
