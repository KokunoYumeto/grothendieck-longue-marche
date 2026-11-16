# Independent audit of D.71

Auditor: `/root/pbc_groups`. Completed2026-11-15 after checkpoint09 source freeze.

**Verdict: PASS.** I read the entire draft `notes/de_onecusp_class2_baire_draft.tex`, checked every new class-two and nonprimitive-peripheral step, and reopened the original primary subgroup source. The full-profinite conclusion explicitly uses the previously proved D.24/D.56; the Baire arithmetic inputs are those independently audited in D.70.

## Primary subgroup input

Opened the author-uploaded original article by Alexander Lubotzky, *Combinatorial group theory for pro-p groups*, Journal of Pure and Applied Algebra25(3),311--325(1982), DOI10.1016/0022-4049(82)90086-X:
https://www.researchgate.net/publication/242982224_Combinatorial_group_theory_for_pro-p_groups .
The page identifies the full text as uploaded by the author. Theorem3.2 and its proof on317--318 assert that a finitely generated closed subgroup of a finite-rank free pro-p group is a free factor of an open subgroup. The adjacent Lemma3.1 and Proposition1.4 give its Frattini/finite-character mechanism. Opened references: `turn878view0`, `turn879view0`.

The draft's proof is valid: choose one normal open subgroup killing the restrictions of finitely many characters of L. The extensions phi(lw)=phi(l) are well-defined homomorphisms on LW, because W is normal and L cap W lies in every selected kernel. This injects the Frattini quotient of L into that of LW. A generating set extends to a basis by the free finite-rank Hopf property. Thus the subgroup argument applies to the actual closed two-generated subgroup used later.

## The actual class-two cusp fibre

The free pro-ell surface group has rank two, with peripheral element c a commutator up to orientation. Its degree-two class is primitive. The integral commutator/Weil pairings give gamma2/gamma3=wedge^2(T_ell E)=Z_ell(1), including ell2 without BCH denominators. The map from actual cusp inertia to this central factor is an isomorphism.

At a marked good place away from ell, the proper Tate module has no fixed vectors because its local ell-primary torsion injects into the finite reduction group. The central Tate line also has no fixed vectors. Hence the actual class-two group has no fixed elements, locally or globally. A zero-abelian class can be conjugated to an I-valued cocycle, and any further conjugator has zero invariant abelian image and lies in I. Its remaining equivalence is exactly the integral I-coboundary relation. This proves the whole Kummer parametrization of the zero-abelian class-two fibre, not merely an injection or a rational comparison.

## The peripheral centralizer and normalizer

The element c has no ell-th root: a hypothetical root has zero abelian image by torsion-freeness and would make the primitive degree-two class divisible by ell. For g commuting with c^b, b nonzero, the closed group <g,c> is free pro-ell with rank at most two. In rank two the two displayed generators form a free basis, and the degree-two Magnus coefficient of [g,c^b] is nonzero b. Thus the rank is one. No ell-th root then forces c itself to generate this procyclic subgroup. This proves C_P(c^b)=<c> even for nonprimitive b.

A normalizer of a nonzero closed subgroup of <c> acts by a unit exponent u. Inner conjugation is trivial on gamma2/gamma3, so b[c]=bu[c]; its primitive torsion-free class forces u=1. The centralizer result applies. Also gamma3 intersects <c> trivially, again by the degree-two class. The argument never treats c as a primitive free generator.

## Exact local and global cocycles

The cusp twist acts trivially by inner conjugation on T2 because c is central there. Thus its T2 action is the reference action, and the fixed-element vanishings apply to conjugators in the exact class-two fibre. That fibre is genuinely H1(G_k,gamma3P;sigma_a), with no extra stabilizer quotient.

At a good place, Hoshi's actual specialized inertia alternative, the unique cusp, and the new centralizer identify any section with nonzero prescribed class-two inertia as a member of that local cusp packet. The local class-two Kummer parametrization identifies its parameter. After the cusp-inertia adjustment the conjugator has fixed T2 image and therefore lies in gamma3P. At zero valuation, nonzero specialized cusp inertia would retain a nonzero primitive degree-two image, which is impossible. The cartesian square gives actual zero inertia. Both local alternatives are therefore assertions about integral gamma3-valued cocycles.

The substitutions in the D.70 Baire proof preserve every necessary property: characteristic Frattini quotients induce the topology of gamma3P; their exponent bounds give uniform finite ramification support for actual reductions; fixed torsion components and deep free Kummer changes preserve finite actions. The class-number perturbation makes the actual Chebotarev witness valuation nonzero without changing the finite cocycle list. Every surviving integral cocycle descends through the compact actual action image. One normal inner cusp-inertia subgroup has trivial fixed subgroup in gamma3P, and its local coboundary kills the whole descended cocycle. Nonprimitive exponents and ell2 are covered.

## Full profinite and requested-curve scope

The actual full class-two geometric quotient is the product of its pro-prime class-two quotients: every finite class-two quotient is nilpotent and splits into Sylow factors, and compactness gives the universal product identification. Arithmetic actions, cocycles, and conjugators are componentwise. The full Kummer packet consequently parametrizes the full zero-abelian class-two fibre.

For the residual product of generic parameters, any actual full section with the prescribed class-two class agrees with the fixed cusp section in every full pro-ell quotient. D.24 applies to these two actual full sections and gives full equality. This applies directly to the specified E:y^2=x^3-x over Q(i), without a replacement curve or field.

All cusp parameters have the same abelian cocycle but are already distinguished at class two. The draft correctly asserts generic singleton CLASS-TWO fibres, while explicitly observing that the entire abelian fibre cannot be a singleton. It computes no first finite obstruction. No mathematical blocker or necessary correction was found.
