# D.31: finite groups in geometric completions

## Proved result

Every finite nonsolvable subgroup of the positive punctured-sphere geometric completion is abstractly A5. Its puncture action consists of at most one orbit of each exceptional size 12,20,30 and any number of free orbits of size60. In the extended sphere completion the nonsolvable abstract groups are A5 and A5×C2. In genera one and two, with arbitrary puncture number and orientation reversal, every finite subgroup is solvable.

The proof does not supply conjugacy of a completed A5 subgroup into the discrete sphere mapping class group or the full A5 centralizer equality. Those exact maps remain the open part of F.7.

## Completed maps checked

1. A finitely generated kernel and a good quotient give an exact completed extension. The proof works modulo each characteristic finite-index subgroup of the kernel, centralizes the resulting finite normal group, uses goodness to split the finite central extension over a finite-index subgroup, and takes the core of a complement. This directly verifies the induced topology on the original kernel.
2. Capping the boundary of a punctured disc gives the braid central extension of a sphere puncture stabilizer. The full twist maps to (n−1)(n−2) in braid abelianization, so its full Zhat topology is retained. Finite pullbacks have a central open Zhat, and transfer embeds each pullback into Zhat because the ambient completed braid group is torsion-free. The finite quotient is therefore cyclic.
3. The same transfer works with the central diagonal torus Zhat². Total strand homology sends the diagonal translation subgroup to n times Z² and proves its full induced topology. A finite subgroup of the quotient braid completion is consequently abelian.
4. The genus-two puncture-forgetting kernel is the torsion-free completion of a surface braid group; finite groups inject after forgetting. The hyperelliptic quotient has finite kernel C2, detected on homology modulo3, and quotient the sphere group with six punctures. The sphere orbit bound excludes nonsolvable finite images there.
5. The genus-one forgetting kernel is the completed quotient of the torus braid group by diagonal Z². Its finite subgroups are abelian, and the quotient is the completed SL2(Z), whose finite subgroups are cyclic by D.8. Orientation reversal adds an extension of index at most2.

The small sphere cases n=0,1,2 are explicit: positive groups 1,1,C2 and extended groups of order at most4. The branch-point solvability lemma is stated for a nonempty set of 1≤b≤3 points. The pure completed sphere group is torsion-free by its ordered-configuration description, proving faithfulness of each finite puncture-permutation action.

## Exact finite-group reduction

Prime-power comparison gives cyclic odd Sylow subgroups and cyclic or dihedral Sylow2 groups. It also retains the geometric normalizer image in Aut(Cp), which is contained in the two exponents ±1. A nontrivial finite solvable normal subgroup has a characteristic normal p-subgroup. The quotient of its completed normalizer preserves the two or three branch points of the geometric p-group cover; a finite group there has cyclic pointwise branch stabilizer and solvable permutation image. This forces the original finite group to be solvable, so a nonsolvable finite group has trivial solvable radical.

The original Gorenstein–Walter 1962 Theorem I is sufficient. Its extra hypothesis is proved: for a central Sylow2 involution z, the quotient of C_G(z) by z preserves the two branch points. Its pointwise kernel is cyclic, and the corresponding preimage is abelian of index at most2. Its odd part is a cyclic normal 2-complement. The theorem then gives PSL2(q), PGL2(q), A7 or a 2-group modulo an odd normal subgroup. A least-prime transfer argument proves solvability of groups with all Sylows cyclic, so the odd normal subgroup is trivial. C3² excludes A7, the additive defining-field subgroup forces q prime, and the diagonal normalizer action leaves only PSL2(5). The exact isomorphism to A5 is conjugation on its five Sylow2 groups.

For the extended sphere group, conjugation on the positive A5 embeds an extension with trivial centralizer into Aut(A5)=S5. The group S5 has a C5 normalizer inducing all four automorphisms of C5, violating the completed ±1 bound. A nontrivial centralizer gives the direct product with a negative C2.

## Primary sources actually inspected

- Gorenstein–Walter, *On finite groups with dihedral Sylow 2-subgroups*, Illinois J. Math.6(4)(1962),553–593, DOI10.1215/ijm/1255632706. The original41-page scan was opened; page553's TheoremI and its V4 footnote were visually checked. Page554 confirms the dihedral-centralizer specialization. No unchecked formulation of the later1965 trilogy is used.
- Bigelow–Budney, *The mapping class group of a genus two surface is linear*, Algebraic & Geometric Topology1(2001),699–708, DOI10.2140/agt.2001.1.699. The full original article was opened. Lemma2.2 pp701–702 and Propositions3.2–3.3 pp703–704 give precisely the capping and hyperelliptic maps used.
- Fadell–Neuwirth, *Configuration spaces*, Math. Scand.10(1962),111–118, DOI10.7146/math.scand.a-10517. The publisher's eight-page original scan was opened, with Theorems1 and3 and the surface/asphericity calculations inspected. The publisher metadata confirms1962; one search OCR incorrectly rendered the year1982.
- The existing R-BZ and R-Boggi references supply the already audited prime-power comparison and genus-at-most-two goodness. F.7's prime-power topology argument avoids the disputed all-finite closure-intersection step.

## Executed certificate

`code/sphere_completion_restriction.py` was executed successfully. It enumerates projective matrices at p=3,5,7,11,13 and verifies the entire unipotent normalizer automizer. The PSL2 orders are 12,60,168,660,1092; automizer orders are 1,2,3,5,6. The PGL2 automizer orders are 2,4,6,10,12. At p5 the five Sylow2 groups give an injective degree-five action with60 even permutations. The two displayed generating matrices act as (1 2 4 3 5) and (2 4)(3 5).

The independent permutation calculation gives C5 automizer exponents {1,4} in A5 and {1,2,3,4} in S5, two fixed points in each exceptional transitive coset action, and an explicit C3² in A7. JSON and captured stdout are saved with the script. The program certifies these finite calculations; the all-prime and full-completion assertions are proved in the TeX.

Root independently read the D.31 proof and the original Gorenstein–Walter statement, then requested the explicit small-n and nonempty-branch-set clarifications; these have been applied.
