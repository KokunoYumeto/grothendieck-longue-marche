# Independent audit of the solvable local draft, Sections 3–5

Auditor: fgh_geometry. Date: 15 November 2026.

Scope: `notes/de_prosolvable_local_draft.tex`, Sections 3–5 and the finite-group closure argument from Section 2 used there. **The result below is a scoped proof audit, not a promotion of the candidate local section theorem.** The parent is checking the fixed-point localization, birational section input, and valuation argument separately.

## Verdict

The solvable-monodromy enhancement in Sections 3–5 passes this independent audit. I found no obstruction to the invariant cyclic gluing, equivariant replacement of branch disks, or realization of the specified finite solvable fields in the specified completion. The one requested clarification—local divisor orders are congruent to +1 and -1 modulo ell rather than necessarily equal to them—has been incorporated by the author.

## Primary sources and existing analytic calculations checked

* ABBR, *Lifting harmonic morphisms I*, https://arxiv.org/pdf/1303.4812: Corollary 6.21, printed p.42; Section 7.2–7.3, printed p.43; Theorem 7.4(2), printed p.44; Theorem 7.7, printed p.45. Opened primary references: turn558view0, turn564view0–3. These identify local automorphisms, define the gluing action, and identify the stabilizer of the chosen gluing data with the automorphism group of the lift.
* Mochizuki–Tsujimura, https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf: Theorem A and the compactified-model formulation in its introduction, printed pp.3–4, independently opened as turn567view0. The set Sigma={p,ell} satisfies the stated size and containment hypotheses. Its finite geometric quotients are solvable by Burnside's theorem. The parent's separate source audit covers the exact Proposition 2.4(iv) domination statement.
* Supplied local preprint: `03-patching.tex` in full (local normal form, patching, point transfer, horizontal closure); `04-tame-roots.tex` in full through the first-stage construction; `05-arbitrary-roots.tex` in full; `06-realization.tex` in full. The analytic domains and the chosen completed-residue-field embeddings have been checked rather than replaced by assertions about underlying points.

## Section 3: cyclic actions on graph lifts

At a circuit vertex, the cover y^ell=f has local orders congruent to +1 and -1 at its two circuit marks. If the divisor used to construct f meets a mark, changing the Kummer coordinate by an integral base-parameter power removes that multiple of ell without changing the deck character. Thus the two tangent characters are zeta and zeta^{-1}. In one oriented annular coordinate they define the same deck transformation. Every gluing isomorphism between the corresponding monomial annular covers intertwines those actions; the gluing torsor is cyclic and commutative. At noncircuit edges the edge orbit is free, so one gluing can be transported around its orbit and closes because the lifted local action has exact order ell. Corollary 6.21 supplies this exact local action, including its group law, by uniqueness.

All other marked fibres are free cyclic orbits. Equivariant matching therefore exists even for chords, edges between circuit vertices, and edges to identity-copy vertices. A loop can first be subdivided as in ABBR Theorem 7.7, inserting u↦u^ell; its two inertia characters remain inverse. The resulting graph is connected and satisfies the componentwise Riemann–Hurwitz equality, so it is a tame covering with no punctures and lifts to an étale cover. Its degree ell and lifted faithful cyclic action make it cyclic Galois.

For a separating edge, each side contains either a cycle or a positive-genus component; otherwise stability contradicts the valence count 2N−1. A graph cyclic cover or a connected torsion-line-bundle cover of that component makes each covered side connected. Equivariantly joining their ell boundary fibres produces a cyclic cover, and every former bridge lift is nonseparating. Further cyclic covers can be combined by fibre products. Their normal closure over the original curve is still an ell-group: over the first Galois cover the closure is a subgroup of a product of conjugate ell-groups, with ell-group quotient.

The entire inverse annulus, including its attached balls, is controlled by the tame lift's inverse-skeleton equality. A pulled-back coordinate has Laurent exponent divisible by ell; its unit factor has a root because ell is prime to p. This proves a root on every full inverse annulus, not merely on the skeleton or one sheet.

The irrational-level collar argument survives the pro-Sigma domination replacement: vertices give rational values, and an invertible analytic function on a disk has constant norm in the rational value group. The complement of the finitely many source node annuli is compact, so avoiding one irrational level gives a whole common collar avoiding that complement. No finiteness of the map of models is asserted or needed.

## Section 4: equivariant patching and auxiliary covers

On each overlap, a root of the branch coordinate splits every local factor. The exterior cover is consequently a trivial G-torsor there, not just a cover with one section. Choosing one sheet and using all its G-translates gives an equivariant trivialization. Branch disks are disjoint, so there is no additional triple-overlap condition. Gluing finite étale algebras retains G and algebraizes over the proper base. A connected component is a torsor under its stabilizer subgroup of G and remains surjective over the connected base; that group is solvable.

If the lower cover has solvable Galois closure, the normal closure of the upper solvable cover is an extension of a subgroup of a product of conjugate solvable groups by a solvable group. This justifies solvable closure at every composition used here. It is not a claim that arbitrary finite covers of solvable degree have solvable closure.

The auxiliary cyclic curve has two rational residual components and ell parallel nodes. The toric Jacobian calculation supplies a character of slope one on each annulus. The division cover is a J[m]-torsor, so its connected components are abelian Galois over the auxiliary curve. Its normal closure over the line is therefore solvable. The period-coset argument is valid on the whole division pullback: after a period representative is fixed, two adjusted local lifts differ by an m-torsion period, and the period lattice is torsion-free. The analytic character roots consequently glue on each clopen period-coset piece. The explicit middle-collar bound then removes the residual unit even when p divides m.

The horizontal ramification bound is separate from residue-characteristic tameness. The horizontal completed field is bar(k)((t)), with algebraically closed characteristic-zero residue field. Its finite extensions are cyclic t^{1/e} extensions. Indices dividing ell are preserved by composita, conjugates, normal closure, normalized pullback, and an étale upper map; these are precisely the operations used.

## Section 5: the specified field, not an abstract copy

In the first stage the new patched étale cover descends from C_p to bar(k), preserving its finite group action. Its function field has solvable Galois closure and hence embeds in the universal solvable étale field L. Its H-valued generic point uses both this embedding and the fixed C_p inclusion. The exterior analytic map transfers the entire valued point, including its completed residue-field embedding, to the original ramified curve. This gives a K_0-embedding F→H, not just an analytic point above the chosen base point.

Because F/K_0 is normal and E already contains its specified copy, every image of a primitive element lies in that copy of F. Degree equality then makes the embedded image equal to F itself. Thus the conclusion is the literal inclusion F⊂H inside E. It is independent of whether the embedding initially corresponds to a different prolongation of the valuation; once its image equals F, that subfield has the fixed norm inherited from E.

The second-stage auxiliary cover has solvable closure and horizontal indices dividing ell; the patched upper cover is étale and solvable over it. The first stage therefore applies to its normal closure. The same point-transfer argument realizes every finite solvable Galois F/K_0 in H. All such extensions exhaust B. There is no bound on derived length and no assertion that a nonsolvable extension is obtained in this tower.

For the final decomposition-group map in this section, surjectivity uses transitivity on prolongations and compactness, while injectivity uses B⊂H=completion(L): a valuation-preserving automorphism fixing L extends continuously and fixes H, hence fixes B. Normalizing w(p)=1 makes preservation of the valuation ring equivalent to preservation of this rank-one absolute value.

## Boundary of this audit

No global section-conjecture consequence, no bounded-derived-length consequence, and no application through a nonsolvable Legendre cover is approved by this note. Those require the additional arithmetic arguments listed in the draft. Sections 2, 6, and 7 are outside the primary assigned scope here, except for the elementary finite-group closure lemma and comparisons used above.
