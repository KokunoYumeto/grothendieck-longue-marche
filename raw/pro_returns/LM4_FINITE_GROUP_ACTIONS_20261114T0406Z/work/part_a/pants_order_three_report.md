# D.42: order-three full pants multipliers

The completed proof is in pants_order_three.tex, with structured metadata and a new primary bibliography entry in the adjacent files.

## Actual automorphisms of closed surface completions

For every genus at least two and prime p, a finite-order actual automorphism of p-power order that acts trivially on primary integral homology is the identity. The proof first passes to the maximal pro-p quotient. Morales's Propositions2.14–2.15 give torsion-free lower-central quotients and trivial intersection, so the derivation maps on the automorphism filtration make the IA kernel torsion-free.

For the full group, the named quotient of its semidirect product to the direct product of the pro-p quotient with Cp induces a mod-p cohomology ring isomorphism. The fundamental surface class multiplied by a periodic Cp class survives under Brown restriction to some section normalizer. Its nonzero restriction forces injectivity of first-cohomology restriction by the surface cup pairing. That one factor exhausts the total dimension 2g+2, yielding one section class and a fixed subgroup with first rank2g and nonzero second cohomology.

The fixed subgroup equals the whole group by an explicit index argument. Nonzero second cohomology makes every sufficiently small transition between open neighborhoods have degree prime to p. Transfer then makes all first-cohomology restrictions injective. An infinite-index subgroup would force unbounded covering genera inside a finite-dimensional first cohomology group. An open subgroup with the same first rank has index one.

This statement concerns actual automorphisms. The order-three outer action below is lifted by D.27 before it is used.

## Exact cyclic cover

At a nontrivial multiplier coordinate q, its reduction zeta is a primitive cube root. The character at the three cusps is (zeta,1,zeta²). Its invariance is checked directly against the scalar multiplier times the three-cycle. The q-fold cover has three boundary circles and genus (q-1)/2.

Filling gives the specified closed surface quotient. Its deck module is computed from the intermediate Cq amalg Cq extension: the kernel generators are v_i=y^i z y^(-i-r), with r=zeta². The first filled cusp gives the index cycle 0,r,...,(q-1)r; the final cusp gives the negative cycle -r-j(r+1). Both use every generator once. Consequently the final filling changes no first homology, and the deck module is Q3[X]/Phi_q.

Its coefficient fields are unramified over Q3 and contain no nontrivial cube root of one. A commuting order-three operator on this multiplicity-one module is therefore the identity. The actual closed-surface theorem makes the filled automorphism the identity on the full profinite group. The canonical orientation-line filling comparison retains the original multiplier, giving the contradiction. Thus every order-three full pants action has multiplier one.

The finite-subgroup corollary uses D.32's injection into S3 x C2. Every possible order is1,2,3, or6. The involution results give the global sign in order2, and an order6 element is the product of its commuting order2 and order3 powers. Every finite subgroup therefore has orientation image contained in the two global units.

## Primary sources checked

- Ismael Morales, On the profinite rigidity of free and surface groups, Mathematische Annalen390 (2024),1507–1540, DOI[10.1007/s00208-023-02785-6](https://link.springer.com/article/10.1007/s00208-023-02785-6). The complete publisher PDF and HTML were opened. Propositions2.14–2.15 and their proofs, printed pages1515–1516, provide the precise pro-p lower-central statement and completion maps.
- Dessislava Kochloukova and Pavel Zalesskii, Automorphisms of pro-p groups of finite virtual cohomological dimension, QJM58 (2007),47–51. The complete [seven-page author manuscript](https://mat.unb.br/~pz/arquivos/Claus3.pdf) was reopened. Theorem2 on manuscript page3 is explicitly stated for profinite groups and every finite virtual p-cohomological dimension d, with restriction injective for degrees above d. Section1.1 explains the finite-dimensional-source passage to a finite product and the normalizer Kunneth calculation.

## Executed verification

code/pants_order_three.py passed all22 cases: both primitive cube roots at each prime q congruent to1 modulo3 through97. It checks the exact free-product words, invariant character, deck action, integral identities T^q=I and Phi_q(T)=0, cyclicity, square-free reduction modulo3, and Frobenius factor degrees. These computations verify the displayed finite formulas; the text supplies the all-prime proof.
