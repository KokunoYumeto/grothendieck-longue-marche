# A.23–A.24: nonmetabelian lifts through class four

The particular pure peripheral involution constructed in A.22 survives the first nonmetabelian test. Let K be the kernel of the map from the free profinite group on x,y to C3 sending both generators to 1. Its Schreier rank is four. The class-two pro-5 quotient of K has ten BCH coordinates over Z5. Extending by C3 gives an infinite quotient Q of the free profinite group whose second derived subgroup is a central copy of Z5.

A.23 gives explicit rational logarithms of f and h, with denominators powers of 3. They define an involution fixing x, conjugating y and xy, and satisfying both norm equations exactly. The formulas reproduce the A.22 Alexander-module residues, rather than merely finding a different involution. Their order-75 quotient is the same noninner certificate as before, proving that the new lift is outer.

All identities were calculated over both F5 and the rational numbers. The rational identities are integral at 5 and therefore establish the complete infinite class-two pro-5 result. Reduction modulo 5^n gives compatible finite quotients of order 3*5^(10n), with second derived subgroup of order 5^n. At n=1 the group has 29,296,875 elements.

The code checks all basis bracket identities and solves complete linear systems. It does not enumerate every element of the 29-million-element group, and uses no sampling. The class-two BCH construction and its universal property are proved in the section, so the calculation is attached to the intended quotient rather than an unspecified matrix model.

Artifacts: sections/A_nonmetabelian.tex, A_nonmetabelian_results.json, A_nonmetabelian_coverage.json, and code/a_metabelian_lift_class2.py with its finite and 5-adic JSON/text outputs. The two commands are python code/a_metabelian_lift_class2.py and python code/a_metabelian_lift_class2.py --rational.

## A.24: the full class-three and class-four families

Both next stages now admit integral lifts. The free Lie coordinates of the open kernel have ranks 30 and 90; the second derived subgroups have coordinate ranks 13 and 62. The complete affine systems above the fixed class-two pair have the following dimensions.

| Kernel class | Variables | Equations retained | Rank over Q and F5 | Affine dimension over Z5 |
|---|---:|---:|---:|---:|
| 3 | 40 | 140 | 36 | 4 |
| 4 | 160 | 560 | 140 | 20 |

The counts describe conjugator pairs, not distinct automorphisms. Every pair satisfies the prescribed A.22 metabelian residue equations, both exact norm equations, and the exact third peripheral equation. The resulting automorphism and its outer class have exact order two because the same order-75 noninner quotient is preserved.

The complete class-four family projects to exactly one point of the class-three family. In the four free class-three coordinates h_ADC, h_ADD, h_CCD, h_CDD, that point is (-11/486, -1/162, 11/486, -11/486), with standard Lyndon bracketing and A<B<C<D. Modulo 5 it is (4,2,1,4). The initially chosen class-three point with all four parameters zero does not extend. Solving the combined weight-three and weight-four system, rather than fixing that earlier choice, finds the compatible family. All twenty class-four free parameters have degree four.

The construction saves the entire affine particular solution, every nullspace vector, every free-variable coordinate, the sparse matrix and right-hand side, and an exact hash for each system. It runs independently over Q and F5. Every witness and every full kernel-basis coefficient is integral at 5. The independent verifier checks the matrix equations and identity free-column minors and computes modular ranks 36 and 140. Those modular ranks and the independent rational kernel vectors certify the rational ranks in both directions. The saved rational systems reduce exactly to the separately constructed F5 systems.

Reduction modulo 5^n gives 5^(4n) and 5^(20n) conjugator pairs, respectively, and exactly one of the class-three pairs extends. The finite groups have orders 3*5^(30n) and 3*5^(90n). These counts come from complete integral affine systems and unit Smith factors; they are not samples or direct enumerations of the finite groups.

The group/Lie identification is used only in classes strictly below 5. Its exact source was checked in Garaialde Ocaña and González-Sánchez (2014), arXiv:1405.4654v2, §2, Theorem 1(a)–(f), including the free-object construction immediately preceding it. The original 1954 Lazard PDF exceeded the web reader's size limit; no unseen original theorem number is attributed to it.

Additional artifacts are code/a_metabelian_lift_higher.py, code/a_higher_lift_verify.py, all class3/class4 rational and mod5 JSON systems and outputs, and code/a_higher_lift_coordinates.csv. The latter records every coordinate of the class-four witness and the original class-three witness. The separate result JSON files retain all affine bases, not only the chosen witnesses.

The precise next relative test is class five with all twenty preceding free parameters retained. BCH denominators now can contain 5, so the plain integral Lie lattice cannot be used without a correct integral Hall-coordinate comparison. A denominator 5 in a rational answer would not itself be an obstruction. No geometric action or full free profinite lift is inferred from the completed class-four calculation.
