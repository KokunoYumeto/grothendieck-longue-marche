# Exact modular and CM comparison record

This note records the actual maps checked during the E.25–E.28 investigation and the exact comparison not supplied by those maps. The finite results are in sections/E_geometry_agent.tex and sections/E_boundary_agent.tex.

## The full-GT Ferrari map

Let q:B4→B3 send tau1,tau3 to tau1 and tau2 to tau2, and let j:B3→B4 be the first-three-strand inclusion. The based GT braid action used by the finite Ferrari programs sends tau1 to tau1^lambda, tau2 to f(tau1²,tau2²)^−1 tau2^lambda f(tau1²,tau2²), and tau3 to f(omega3,tau3²)^−1 tau3^lambda f(omega3,tau3²), where omega3=(tau1 tau2)^3.

The image q(omega3) is central in B3. Since f is a commutator word, q(f(omega3,tau3²))=1. Comparing the three generator images proves the actual identity q alpha4=alpha3 q. The section j is also equivariant on its generators. Thus K=ker(q) and its semidirect product with j(B3) carry this actual full-GT action.

For xi1=tau3 tau1^−1 and c=f(omega3,tau3²), both arguments of c commute with tau1, and q(c)=1. Hence alpha(xi1)=c^−1 xi1^lambda c exactly. The induced first column on K^ab is lambda e1. The tau1 covariance determines the second column in the specified K basis. The boundary word [xi1,xi2]=omega4 omega3^−2 has the required power image. These statements use the literal quotient and inclusion; they do not identify this normalization with an elliptic section chosen from another basepoint.

Nakamura's 2013 primary source gives q and the Ferrari generators in §5.4, formulas (5.4.3)–(5.4.4). Its §5.7, printed pp.457–458, uses relation (IV) in the Tate/Weierstrass comparison. The actual Galois basepoint shift contains h_sigma=omega2^(4rho2) omega3^(−4rho2) omega4^(rho2). Retaining this factor is necessary when comparing those based representations.

## The triangle-cover path comparison

NTY III Proposition4.4 gives the full-GT triangle-cover Tate action. Theorem4.16 identifies it with the equianharmonic normalizer coordinate on the Galois subgroup, using the stated paths. Formula(4.8) retains rho_K=rho3/2−2rho2+(−5lambda±5)/12, with the source's branch choice. Proposition4.13 and the scope statement on printed p.432 do not provide that identity for every full-GT element.

The finite common CM field in the retained matrix convention is M'=Q(i,(3/4)^(1/4)). Adjoining the specified square root of2 gives its comparison with Q(i,3^(1/4)); no unlabelled identification of these fields is used. Likewise the intrinsic cubic cover in E.26 compactifies to u³+v³=1. Its exact proper homology maps are proved directly, without substituting a different j=0 twist.

Enriquez's Elliptic associators, arXiv1003.1012v3, Proposition2.20 constructs an explicit full-profinite-GT section into the elliptic group. Proposition8.6 compares the arithmetic normalization using Galois formulas (80)–(81). The checked statements do not add the missing all-GT Ferrari/triangle path identity. The 2026 Lochak–Nakamura–Schneps preprint, §8, likewise does not supply the needed cutting-map comparison.

## Three specified coefficient constructions

D.5's coefficient is literal: c_N is the y-coordinate of delta_N(f), and rho_N^dist=−c_N is its defined negative coordinate. Its full-GT distribution identity is Enriquez's opened theorem. The exact double-cover comparison in the NS generator convention is c_2(f_sigma)=+kappa_2(sigma). Simultaneous inversion of x and y changes the sign, through the commuting delta_2 square proved in D.5. The earlier arithmetic-sign sentence is preserved and corrected in research/BC_kummer_two_sign_audit.md and research/checkpoint07_kummer_sign_prior_passages.json.

Nakamura–Schneps (Inventiones141(2000),503–560), Definition5.1, defines a full-GT extension from the abelianization of its specified word g_F. Proposition5.3 identifies it with −A_F(−1,1) on the subgroup satisfying (III′). Remark6.2 derives the matrix relation beta=−8rho2 alpha using (IV). I independently opened those passages. Their proofs retain those hypotheses.

Marin's profinite matrix construction provides a matrix-defined extension, agreeing with the arithmetic character in its normalization. No checked formula here identifies it with the literal distribution coefficient on the entire full-GT source. In particular the mod24 matrix and mod12 coefficient in E.25 are both retained, but no extra equality between them is inserted.

The earlier scan concerned the proposed equality of full-GT extensions. The subsequent literal double-cover audit found and corrected D.5's arithmetic sign, while retaining the full-GT distribution identity. E.6 and E.25 use only the induced maps (q delta_N,c_N). E.29, E.38 and their later comparisons use the actual NS Theorem2.5 matrices and positive-root character directly; their matrices and labels are unchanged. The preliminary proposed numerical exclusion from identifying extensions remains withdrawn.

## Finite results and remaining comparison

E.25 evaluates all five mod24/mod12 distribution maps jointly. Every retained CM row has actual N_B′ corrections satisfying the finite identities, with all four residues of −c3 modulo4. This proves the exact finite fibre calculation, without producing a full-GT element.

E.26 proves the proper Fermat quotient factors through the specified homology tower and proves the full boundary quotient detects an explicit killed commutator. E.28 computes the boundary correction lattice, extends all retained points through every two-power boundary level, and glues every multiplier-one E.24 point with that entire tower by explicit gamma5 words. The joint maps are proved surjective directly; no invariance of the Ferrari source kernel is presumed.

The unresolved modular route still requires a based morphism identifying the full-GT Ferrari normalization with the triangle CM coordinate, including the displayed phase. The established actions, finite quotients and common Galois restriction supply the precise objects for this comparison; they do not evaluate it.

## Primary sources inspected

- Enriquez, Elliptic associators, https://arxiv.org/pdf/1003.1012, v3, Proposition2.20, Proposition8.6 and §9.
- Nakamura, On Arithmetic Monodromy Representations of Eisenstein Type in Fundamental Groups of Once Punctured Elliptic Curves, PRIMS49(2013),413–496, https://ems.press/content/serial-article-files/41205, §§5.4,5.7,5.9.
- Nakamura–Tsunogai–Yasuda III, author-uploaded PDF: https://www.researchgate.net/profile/Hiroaki-Nakamura-2/publication/232010902_Harmonic_and_equianharmonic_equations_in_the_Grothendieck-Teichmuller_group_III/links/55555a0108ae6fd2d821ce39/Harmonic-and-equianharmonic-equations-in-the-Grothendieck-Teichmueller-group-III.pdf .
- Nakamura–Schneps, On a subgroup of the Grothendieck–Teichmüller group acting on the tower of profinite Teichmüller modular groups, https://www.researchgate.net/publication/227209468_On_a_subgroup_of_the_Grothendieck-Teichmuller_group_acting_on_the_tower_of_profinite_Teichmuller_modular_groups, Definition5.1/Proposition5.3, pp.522–524, and Remark6.2, pp.525–526. Root must reopen this exact source before citing its web references.
- Lochak–Nakamura–Schneps, February2026 preprint, https://arxiv.org/pdf/2602.12462, Theorem1.1 and §8.

The search and scope history is also retained in research/BCF4_agent.md; no novelty or priority claim is made.
