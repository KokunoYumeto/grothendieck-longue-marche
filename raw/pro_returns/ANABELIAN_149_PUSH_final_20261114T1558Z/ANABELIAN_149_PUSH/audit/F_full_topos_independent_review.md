# Independent review of the final Qsolv Gm topos step

Reviewer: Part F agent (/root/topos). The finite-field agent supplied the theorem draft in audit/F_finite_field_rigidity_review.md; root and the Part F agent independently accepted it. The complete proofs are now integrated as F.20–F.23 in sections/F.tex with rows in audit/F_results.json. This note records the independent checks, not a second source of theorem numbering.

## Arithmetic finite-quotient detection

The common-constant wreath group is essential. For a connected finite G-Galois cover over an open rational curve, write N for the geometric group and P=G/N for the arithmetic constant group. Over k=Qsolv, P is perfect. Descend the cover and its entire G-action to a number field F⊂k so its base change is still connected; its constant field M satisfies M∩k=F. Then k is the maximal solvable extension of F: the normal closure over Q of a solvable extension of F has solvable Galois group, since the normal closure of F/Q is solvable.

The ordered n-fold fibre product of the covering curve over its common constant field M, restricted to distinct base coordinates, is itself an H-Galois cover of the unordered configuration base, with

H = (G ×_P ··· ×_P G) ⋊ S_n.

The source must not first be quotiented by S_n and then called H-Galois; that quotient has a smaller degree. The unordered base is an open of affine n-space. The total source is geometrically connected over M and connected over F, so Hilbert irreducibility yields full arithmetic group H, even though the cover is not geometrically connected over F.

After base change to k the group is H∞, the solvable residual. Literal A_n is perfect for n≥5 and lies in H∞. Commutators of N^n with A_n give balanced tuples with an arbitrary element of N in one chosen coordinate. The image of H∞ in P×S_n is P×A_n. Multiplying by a literal A_n element cancels the permutation without changing the P-image. Thus the intersection of H∞ with a coordinate stabilizer projects onto all G, not merely its geometric subgroup N. This proves the required closed-point detection statement.

## Relative conjugacy and the generic limit

For a finite target quotient Q of G_{k(t)}, extend its finite generic cover over a target open V. F.19 gives φ⁻¹(V)=f⁻¹(V)=U, so both maps factor through π1(U). Apply detection to their joint image H⊂Q×Q. Its arithmetic quotient is a quotient of G_k and hence perfect.

At a detecting closed point x, equality of the two geometric point values identifies the two point-source morphisms as relative geometric morphisms. This is the field-source reconstruction statement in CHW Section 3. With generic and closed geometric base points lying over the same chosen kbar point, the resulting conjugator belongs to the geometric kernel of π1(V). It conjugates the entire two D_x homomorphisms, rather than separately conjugating their individual elements. Surjectivity D_x→H therefore gives a single global conjugator modulo Q.

Lift each finite conjugator to G_{kbar(t)}. The sets of geometric elements conjugating the two generic maps modulo Q are closed. Common target quotients give the finite-intersection property, so compactness supplies one geometric conjugator for all finite quotients. Consequently the generic topos isomorphism is compatible with BG_k. The generic functor itself can be defined without a hidden factorization theorem: every finite generic cover extends over some open, and pulling back and taking its generic fibre is independent of shrinking. This gives the continuous generic Galois homomorphism.

## Generic identity determines the whole curve topos

The exact representability input was opened: CHW Appendix A, theorem preceding Corollary A.9 and Corollary A.9. A geometric morphism with topologically noetherian source sends every separated quasicompact étale scheme to another such scheme. Its proof uses constructibility, the complemented diagonal, and the fact that a separated quasi-finite étale algebraic space is a scheme. There is no unproved representability or coherence assumption.

SGA1 I Proposition 10.1 was also opened in the complete supplied source. A separated étale chart over a normal connected curve is canonically an open in the finite normalization in its generic algebra. All components dominate the base; no extra vertical components occur. Thus a topos endomorphism with an identified generic identity sends each chart to an open in the same normalization.

To show its point map is the identity, suppose a closed point x maps to y≠x (including a generic y). Choose a rational function r with v_x(r)=1 and v_y(r)=0 when y is closed. CRT on a common affine neighbourhood, or Riemann–Roch, gives such r. The normalization in z²=r has no étale point over x, while its maximal étale locus has a nonempty geometric fibre at y, or degree two at the generic point. Pullback would simultaneously have a nonempty fibre at x and be an open in a normalization with no étale point over x, a contradiction.

For the maximal étale locus Z of any finite normalization, its pullback is an open subspace of Z. Since the base point map is now fixed, the two finite geometric fibres have equal cardinality at every point; the open subspace is all Z. The induced sliced endomorphism of Z has generic identity under this canonical identification. Apply the same ramification argument on each normal connected component of Z: it fixes all its points and therefore every open subobject V⊂Z. Every separated qc étale chart is such an open. Generic uniqueness of morphisms to a separated target gives naturality of these identifications. Since these charts form a basis (CHW Lemma A.4), this identifies the full inverse-image functors.

For a finite étale f:X→Y and a morphism φ with the same relative generic map, an equivalent reduction is available. The finite étale X-scheme φ*(X) has the diagonal degree-one generic component of f*(X). By normality, that component extends to a section. It lifts φ to a generic-identity endomorphism of X via the slice-topos universal property. The preceding argument makes the lift the identity and hence φ=f. For f(t)=ct^m, m≠0, the finite étale hypothesis holds in characteristic zero.

## Primary passages actually opened

- CHW supplied TeX, Appendix A, labels `thm:every_coherent_geometric_morphism_between_etale_topoi_of_qcqs_schemes_is_induced_by_a_morphism_of_sites`, `cor:every_geometric_morphism_between_topologically_noetherian_schemes_is_coherent`, and `lem:separated_and_separated_finitely_presented_etale_sites_are_bases`.
- SGA1 complete main source, Exposé I Proposition 10.1, approximately lines 2028–2050.
- Serre, *Topics in Galois Theory*, second edition (A K Peters, 2007), primary CNRS-hosted PDF https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf, Proposition 3.3.1 p. 23 and Theorem 3.4.1 p. 25. The Galois specialization statement assumes irreducibility over the number field and does not impose geometric irreducibility; these are the final F.20 citations.
- Poonen, *Rational Points on Varieties* (AMS GSM 186, 2017), author-hosted PDF https://math.mit.edu/~poonen/papers/Qpoints.pdf, Appendix B.4 pp. 297–298: simultaneous Hilbert irreducibility and global fields Hilbertian, with Fried–Jarden 13.4.2 and Serre Chapter 9 references.
- Stix, *On cuspidal sections of algebraic fundamental groups*, Proposition 11 and Corollary 12, primary PDF p. 5, also opened as an alternative inertia-normalizer route. They have no nontrivial-Kummer-field assumption. This alternative is not needed for the normalization proof.
