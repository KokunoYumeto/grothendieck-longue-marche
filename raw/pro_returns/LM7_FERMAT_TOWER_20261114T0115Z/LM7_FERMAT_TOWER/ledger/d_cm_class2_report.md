# D.27: nonabelian refinements of the CM shadows

**Proved progress; the full profinite CM question remains incomplete.**

The finite base is Q=SL2(Z/12)/global +/-1 of order576, and N is the free rank97 kernel of B=C2*C3 onto Q. The two characteristic refinements are H3=B/(gamma3(N)N^3), of order576*3^4753, and H2=B/(gamma3(N)[N,N]^2N^4), of order576*2^4850. The code evaluates actual B words by collapsing the Bass–Serre graph tree to97 generators, then uses exact class-two coordinates. It verifies that every fundamental cycle is the corresponding free generator.

## Exhaustive result for the original selected actions

At3, the4656-dimensional exterior-square layer reduces under exact averaging by the normal order32 subgroup to135 dimensions. The central correction rank is127. Accounting for all34 lower r-centralizer directions raises it to130. At2, the symmetric square-and-commutator layer has4753 dimensions; its correction rank is4737, rises to4738 after the multiplier allowed by m=0 modulo36, and rises to4748 after all52 lower s-centralizer directions. Coprime centralizer lifting accounts for the other elliptic conjugator in each calculation.

The complete3-test leaves four selected actions: the identity, A=I with beta=(9,8;4,9), A=I with beta=(9,4;8,9), and A=I with beta=5I. The complete2-test leaves the identity and A=5I,beta=I. Their intersection is only the identity.

This proves that all23 nonidentity selected actions in D.25 are nongenuine, including its12 selected extra-CM shadows. The proof uses the original Herfort–Ribes torsion theorem (Theorem A onp155, A-prime onpp157–159) to put every genuine completed-braid action into the tested elliptic-conjugacy form. D.25's exact projected centralizer calculations fix the Q coordinates of both conjugators; the added lower-centralizer columns exhaust their remaining freedom. The assertion concerns genuine full lifts. It does not assume that torsion in an arbitrary finite quotient must already be conjugate into its elliptic factors.

The complete compatible abelian-kernel lifts of D.26 remain valid. They now give explicit examples showing that those refinements do not suffice to certify a genuine full lift.

## Alternate witness with the same extra CM pair

The original selected action is only one point of a98-dimensional affine mod2 homology solution space. Five exact quadratic obstruction forms remain after all central and lower-conjugator corrections. The program varies that initial homology solution and checks generation separately.

At trial48 it finds a new action for A=I,beta=(9,8;4,9), with homology masks beta=0x8ca9620ec63b26ee68fbb210 and A=0x60da0c00a2c8c0f44be10df0. All five obstructions vanish, the induced kernel map has rank97, and the multiplier is1. The saved exact central coefficients and lower-centralizer word give an explicit corrected cusp word of470844 letters. Direct full Magnus evaluation yields q=1, zero degree-one coordinate and zero in all4753 degree-two coordinates. This final check is independent of the projected obstruction test.

The original mod3 action for this pair is the identity, with zero class-two central correction. Its prescribed order2 centralizing conjugator lifts through the entire relative pro3 kernel by coprime conjugacy. The alternate action therefore gives an actual automorphism of H2 times_Q P3, not just H2 times_Q H3. The latter finite quotient has order576*2^4850*3^4753. A single cusp gauge gives compatible nonarithmetical finite shadows on its finite characteristic refinements retaining G6 and CM data.

The alternate witness is stored separately; the original D.25 certificates have not been overwritten. Its full profinite lift, higher two-primary refinements, mixed-prime refinements, and the genuine missing CM coset are still unresolved.

## Reproducibility and audit

The complete programs and actual outputs are `code/d_cm_class2.py/.out/.json`, `code/d_cm_class2_two.py/.out/.json`, and `code/d_cm_quadratic_search.py/.out/.json`. The exact free-group models, corrected coefficients, obstruction forms and generation checks are included. Agent A independently audited the formulas and freshly reran all three programs with matching results. Its original-source entry `A_HerfortRibes1985` records the official GDZ PDF, page anchors and visual inspection.

Subsequent exact refinement D.30 rejects the specific central representative recorded here as a genuine full lift, jointly retaining its G6 data. It also constructs a further explicit central replacement with the same homology data that clears the new degree6 test and preserves an infinite compatible tower. The original quotient automorphism proved here remains valid; the old certificate is retained separately.
