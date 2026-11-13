# Part 4 contribution: checked results and source routing

Eight numbered statements are in `sections/boundary.tex`; corresponding result and reading rows are `notes/boundary_results.csv` and `notes/boundary_readings.csv`. The bibliography fragment is `notes/boundary_references.bib`. Mathematical programs and actual output are `code/boundary_checks.py` and `code/boundary_checks_output.json`.

## Corrections that affect other parts

1. The literal `pi_0(D)` category in the prompt need not exist. Connected components do not preserve the Segal fibre products. The free quotient `(C^4 x C*)/C2`, with `(12)(34)` on coordinates and `w -> -w`, gives two triple-flag components over one composable pair of arrow components, with distinct composites. Use every flag component as a semisimplicial set, then its simplex category.
2. Remove `D_0=X` from the boundary indexing. Including it introduces the cone apex. For stable graphs remove the no-edge graph and normalize total edge length to one.
3. The usual dual complex is coarse. A graph category retaining all automorphisms has a different classifying space. In `(g,n)=(1,1)`, that classifying space is `BC2`, but the boundary complex is a point. The full tropical moduli space is a cone, whereas the dual complex is its unit-volume link.
4. The manuscript scan149133 actually shows `U_infty`. The proposed nerve-lemma statement applies to `D`; this is a mathematical correction, not grounds to silently transcribe `D`.
5. The compact non-equivalence needs `D` nonempty. For an empty divisor both link and complex are empty.
6. Weight statements require an algebraic proper pair (or some independently specified mixed Hodge context). They do not have their asserted meaning for an arbitrary complex analytic manifold.
7. Compactification independence is proved for smooth proper algebraic varieties and stacks; in the analytic category the factorization theorem requires a bimeromorphic identification. We have not claimed that an arbitrary biholomorphism of analytic open parts extends bimeromorphically. Do not enlarge this scope silently.

## Proof mechanisms

- The correct coarse maquette is the component semisimplicial realization of all strict branch flags. Normalized closed flag spaces realize `D`; corresponding closed oriented faces realize `L`. Local coordinate radial contractions prove the augmentations are equivalences. Ordinary quotient of branch-permutation simplices gives the usual symmetric Delta-complex.
- For the homotopy fibre over `b`, use the left Kan extension formula along the simplex category's groupoid completion: colimit of the full space-valued diagram over pairs `(flag component, path to b)`. Fibres are not generally individual strata. The triangle of lines gives an infinite wedge of 2-spheres over its dual circle.
- Admissible blow-ups give stellar subdivision when the centre is a stratum closure; otherwise they give cone extensions contracting by moving the exceptional vertex to the barycentre of the branches containing the centre. Barycentres are monodromy-invariant, so this proof descends through branch permutations.
- Weight zero of the closed divisor is the component incidence row of the proper intersection spectral sequence. The exact link sequence `H_D^k(X) -> H^k(D) -> H^k(L) -> H_D^{k+1}(X)` and `H_D^a(X) = H^{2n-a}(D)^vee(-n)` show all support groups have weights at least `a`; their weight zero vanishes. Hence the closed-divisor weight zero maps isomorphically to that of the link. Pair exactness gives compact supports; duality gives top weight, including Tate twist.
- Genus-zero tree complexes are explicitly isomorphic to laminar-subset Whitehouse complexes, allowing exact application of Readdy Theorem4.7. This is a complete reduction, not an unsupported use of the curve complex theorem.

## Exact computations

`boundary_checks.py` completed successfully. It enumerates the C2 flag counterexample, finite stable-split complexes, exact integer Smith forms, loop-graph automorphisms and the normalized C2 bar boundary, and line/conic normal circle-bundle cokernels.

- n=4: f=(3), 3 components.
- n=5: f=(10,15), connected, H1=Z^6.
- n=6: f=(25,105,105), connected; relative triangle boundary after spanning-tree collapse is 81 x 105, Smith form has 81 entries all1; H1=0, H2=Z^24.
- One-loop graph: two automorphisms; d2=[2], H1(BC2)=Z/2; coarse point H1=0.
- Line/conic: normal degrees 1 and4, boundary-map Smith entries1 and4; pi1 links0 andZ/4.

These finite complexes are not the infinite curve complex or its lifted rank-selected posets. Their homology is not presented as independent verification of Part5(b).

## Verified sources, all opened

- Payne (2013), published PDF https://web.ma.utexas.edu/users/sampayne/pdf/BoundaryComplex.pdf : Theorem1.1; Proposition4.2; Theorem4.4; Stepanov lemma and Remark5.1, published p307. Web refs turn11view0, turn12view1, turn15view2.
- Thuillier (2006), full preprint dated28 July2006 https://epub.uni-regensburg.de/561/1/10-2006.pdf : Theorem3.25, Proposition4.5, Theorem4.6 (pp41--44 in the preprint). Web refs turn15view0, turn16view0. Published2007 metadata opened at https://link.springer.com/article/10.1007/s00229-007-0094-2 (turn13view2). Do not assign preprint numbering to the journal. The publication itself is verified bibliographically; the mathematical proof was checked in the full2006 text.
- AKMW (2002), published PDF https://personal.math.ubc.ca/~karu/papers/semist.pdf : Theorem0.3.1, especially(6), includes compact complex manifolds and bimeromorphic maps. Web refs turn13view0, turn15view1.
- Harper (2017), https://arxiv.org/pdf/1706.07999 : Theorems1.1--1.2, characteristic0 hypothesis Section1.4. Web refs turn28view0, turn29view2.
- Durfee--Saito (1990), https://www.numdam.org/item/CM_1990__76_1-2_49_0.pdf : Definitions2.7--2.8, Propositions2.9 and3.5. Web refs turn13view1, turn16view1, turn40view1.
- Chan--Galatius--Payne (2021), published PDF https://web.ma.utexas.edu/users/sampayne/pdf/TopWeightCohomologyOfMg.pdf : Definition5.2, Lemma5.4, Corollaries5.6--5.7, Theorem5.8; published pp586--588. Web refs turn42view0, turn43view0--2. Earlier preprint https://web.ma.utexas.edu/users/sampayne/pdf/GraphHomology.pdf also opened, same numbering verified in publication.
- Abramovich--Caporaso--Payne (2015), arXivv2 https://arxiv.org/pdf/1212.0373 : Theorem1.2.1, Corollary7.2.2, Section7.3. Publisher metadata https://www.numdam.org/item/ASENS_2015__48_4_765_0/ . Web refs turn29view1, turn39view0, turn40view2, turn25search0.
- Readdy (2005), https://arxiv.org/pdf/math/0511420 : unnumbered Whitehouse definition in Section2, preprintp3; Theorem4.7 and Theorem5.2. Author publication list https://www.ms.uky.edu/~readdy/papers.html . Web refs turn25view1, turn28view2, turn40view0, turn41search3.
- Feichtner (2006), https://msp.org/pjm/2006/227-2/pjm-v227-n2-p02-s.pdf : Theorem3.1, Corollary3.2. Web refs turn25view0, turn28view3.

No priority claim is made. The component-Segal counterexample is an explicit calculation made for this task. Before writing it we checked the supplied dictionary and the symmetric-Delta/branch-monodromy treatments in CGP and ACP; that is not a comprehensive novelty search.
