# Finite centralizer source audit and the A5 finite image

## Exact source step

The complete supplied TeX of Boggi, arXiv:2408.12486v2, was inspected at Proposition `centgood` (published Proposition2.4), its use in the proof of `Gcentconf` in the general case of TheoremA, and the proof of TheoremC. The paper has since appeared in *São Paulo Journal of Mathematical Sciences* **20**, article35, published23 September2026, DOI[10.1007/s40863-026-00558-y](https://link.springer.com/article/10.1007/s40863-026-00558-y). The full publisher HTML was reopened and inspected: Proposition2.4 retains the closure–intersection step, and Lemma3.2 still invokes that proposition. Thus the prompt's prepublication description refers to its supplied snapshot; this audit concerns both the inspected preprint and the published version, without drawing any conclusion from publication status. The complete supplied TeX of Boggi–Zalesskii, arXiv:2406.08639v2, was inspected at Theorem5.1(iii), the prime-subgroup theorem, and the centralizer/normalizer criteria in Section2. The primary arXiv HTML for the latter was also opened.

Both all-finite centralizer proofs display the final equality

    intersection of closures C_G(x_i) = closure of intersection C_G(x_i).

The preceding prime-order or torsion-element centralizer results establish the expression on the left as the ambient centralizer. They do not, by themselves, establish the final equality. No counterexample to the stated source theorem is claimed. The audit records an absent justification and the exact residual finite-refinement problem.

The general branch-removal proof of Boggi's centralizer congruence theorem uses Proposition2.4 as well, so using that theorem for an arbitrary nonsolvable subgroup would not independently repair the centralizer equality. For a p-group, the needed Proposition2.4 application follows directly from Boggi–Zalesskii TheoremA, without any closure-intersection step. This supplies a sound prime-power congruence/topology input.

## Completed solvable proof

The TeX draft proves the solvable result by induction using a characteristic p-primary subgroup of the last nonzero derived term. The prime-power normalizer has its full profinite topology by the preceding checked case. Its quotient by that p-subgroup is a finite-index subgroup of the mapping class group of the decorated quotient surface, again of genus at most two. The normalizer of the remaining solvable quotient is handled by induction and pulled back. The finite-kernel diagram proves the induced topology statement at the same time. Finally, the conjugation homomorphism to the finite group Aut(J) has an open kernel; density of the discrete normalizer in the completed normalizer proves density of the discrete centralizer in that kernel. This proof does not invoke an all-finite centralizer result at an earlier stage.

## New proved A5 comparison at the puncture-permutation level

The puncture set consists of some exceptional orbits of sizes12,20,30 and m free orbits of size60. The ambient completed centralizer and the discrete centralizer have the same permutation image: every exceptional puncture is fixed individually, and the free orbits carry the entire wreath product A5^m semidirect S_m.

For order-three and order-five stabilizers, a positive commuting homeomorphism fixes the two poles because their oriented local rotation numbers differ. Prime-power centralizer comparison transfers this finite permutation constraint to the completion. For an order-two stabilizer, place it in A4. The positive actual centralizer of A4 fixes its branch points and is isotopic to the identity through commuting maps: descend to the quotient sphere with three branch points, isotope there, and lift; the terminal deck transformation belongs to Z(A4)=1. Therefore it fixes all six order-two ramification points. The proved solvable comparison transfers that constraint to the completion. These constraints eliminate the nonidentity element of each two-element transitive permutation commutant.

On free orbits, moving one quotient puncture around loops realizes every deck monodromy in A5, independently for the different orbits. Half-twists exchange quotient punctures. Lifted isotopies commute with A5 and fix the ramification points, yielding the full wreath product inside the discrete centralizer already.

The executed standard-library script `code/a5_centralizer_permutations.py` constructs all60 elements of A5, verifies an order-two/order-three generating pair, computes its coset actions of degrees30,20,12, and checks stabilizer normalizer orders4,6,10 and commutants of order2. The fixed-point constraints leave order1 in each exceptional block. JSON and captured stdout are attached.

## Exact remaining statement

For generators u=(12)(34) and v=(135), the ambient centralizer is the intersection of the two closed cyclic centralizers. Formula(F.7.7) gives the image of that intersection in each finite quotient as an intersection over all finer finite quotients, proved by compactness of explicitly displayed nonempty closed sets. Full centralizer equality is the assertion that these stable images equal the images of the discrete simultaneous centralizer at every level. Only the puncture-permutation level is settled by the new finite calculation. When all punctures lie in exceptional orbits, the discrete A5 centralizer is trivial, so the remaining question is triviality of its pure completed centralizer.

The source theorem is not labelled false. F.6's arithmetic open-image assertion has been independently audited and does not use this completion-centralizer equality.

## Minimal twelve-puncture reduction and tested forgetting maps

For the twelve-point icosahedral action, an A4 subgroup is regular on the puncture set. Its quotient has one free puncture and three branch points. The discrete centralizer is the free group F2 of the quotient three-punctured sphere. Its pure subgroup is the monodromy kernel of index12, namely F13, the fundamental group of the sphere minus the14 A4 ramification points. The checked solvable comparison gives an actual embedded Fhat13 containing the unknown completed A5 centralizer.

There are24 six-point subsets consisting of one C5-fixed pole plus one free five-cycle, and12 seven-point subsets consisting of both poles plus one five-cycle. Each target has discrete C5 centralizer exactly C5, since its quotient has only the two branch points and one free marked point. Prime-power comparison makes the completed pure C5 centralizer trivial. Thus every one of these36 forgetting maps kills the unknown A5 centralizer.

The six-point joint map is provably noninjective even on the discrete F13. In the regular A4 labelling, collision partitions at a ramification point are right cosets gH. The antipodal permutation commuting with A5 is right multiplication by one involution h of A4. Every retained six-point subset has one point from each antipodal pair. Its configuration map therefore extends across both fixed points of h in the parameter sphere. The two corresponding nontrivial peripheral meridians are killed by every six-point forgetting map. Their primitive procyclic completions give the same obstruction to completed injectivity.

The12 seven-point subsets retain collisions at all14 ramification points. The executed program uses all seven cyclic stabilizers in A4 and the correct right-coset partitions. In first homology a ramification meridian is the sum of pair generators inside its collision clusters; the pure sphere target imposes vertex-sum and total-sum relations. Over F101, every seven-point map and their joint map have rank6 from the13-dimensional source, so the joint H1 kernel has dimension7. The two ramification poles for each cyclic stabilizer give identical columns. The six-point joint rank is5. These are calculations of the indicated abelian quotients: they do not identify the kernel of the seven-point group map. No nontrivial A5 centralizer element is produced.

## Exact common-C3 model and discrete cyclic directions

The current F7 proof includes (F.7.10)–(F.7.18), the exact common-C3 comparison retained in the separate `f_second_a4_c3_attack.tex` note. The proved prime-power topology supplies the actual quotient injection on completed centralizers. The six quotient labels, their rational coordinates, beta’s normalized action, and the basepoint transport path are displayed. The residual pure A5 centralizer is exactly the fixed intersection under this action inside the specified embedded Fhat13. The exact matrix certificate passes 180 products and 720 vertex labels. F10 excludes every nonzero profinite power of every nontrivial discrete pure mapping class from the residual centralizer, including the explicit F9 kernel word. The full fixed intersection remains open.
