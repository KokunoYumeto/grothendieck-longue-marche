# Independent audit of D.70

**Verdict: PASS.** I read the complete current proof and metadata, including the final conclusion for every finite two-subgroup. No mathematical correction is required. This audit treats D.68 and the final integral assertion D.69y--z as the already independently checked inputs; their executed certificates were rerun in the preceding audits. D.70 makes no new finite-computation assertion.

## Actual filling and induced automorphisms

The two based covering cusps are exactly \(d_0=c^q\) and \(d_1=xc^qx^{-1}\). In the actual dihedral quotient, the image of \(c\) generates the rotation group, so the choice of \(g'\in\{1,x\}\) and the integer \(k\) in the proof is possible. The displayed element
\[
n=\alpha(g)f_0^{-1}c^{-k}(g')^{-1}
\]
lies in \(N\), and substituting it gives the stated conjugation formula without a change of the peripheral exponent or base path. Applying the inverse action gives equality of the closed normal cusp kernel.

The full quotient \(N/K\) is the completion of the actual filled discrete surface by the finite-target universal property. Restricting those targets to finite two-groups gives its specified maximal pro-two quotient. Thus the group \(P\) is the closed genus-\(q\) surface pro-two group, and the induced \(b\) is an actual automorphism, not just an outer class. The rank-two minus-identity summand proves that \(b\) has order exactly two.

The injection of the dual character module consists precisely of characters vanishing on both \(d_i\). The converse factorization through \(N/K\) and then through \(P\) is valid because the target is pro-two. The same argument with finite coefficients verifies the mod-two comparison.

## Integral deck action and surface pairing

The odd rotation deck action extends over the two actual filled points and preserves their oriented surface. Its averaging projector is integral over \(\mathbb Z_2\). The cusp restriction maps are rotation-invariant, hence vanish on the nontrivial deck summand \(W_2\). On the invariant part, restriction and transfer reduce the filling condition to \(\xi(B)=\xi(C)\), because the actual covering degree \(q\) is a two-adic unit.

D.69's dual matrix convention therefore gives minus identity on the remaining averaged rank-two summand and identity on \(W_2\). Reduction modulo two is identity on the whole closed character module.

The deck projector is self-adjoint for the actual cup pairing: the adjoint of a deck operator is its inverse, and inversion permutes the terms of the average. Its two summands are orthogonal integral direct summands. The block-diagonal Gram determinant argument proves unimodularity on each summand. In particular the nonzero \(W_2\) contains two integral \(b\)-fixed characters with nonzero reduced cup product.

## Degree-three cohomological obstruction

Every mod-two character extends to \(P\rtimes_b C_2\) by assigning zero to the specified section. This gives permanent representatives for every class in \(E_2^{0,1}\); the quotient character is permanent because the section splits inflation. The surface class is a product of two of the extended first-cohomology classes. These generators generate the entire second-page algebra of the multiplicative Hochschild--Serre sequence, so all differentials vanish. The class \(u\eta\) in bidegree \((1,2)\) survives and is nonzero.

The two integral fixed characters have actual \(\mathbb Z_2\)-valued extensions. Consequently they vanish on every order-two subgroup of the semidirect product. Each such subgroup is a section, and the displayed inverse maps give its normalizer exactly as \(C_P(T)\times T\).

For a section \(T=\langle n\tau\rangle\), the action on \(P\) is the actual involution \(\operatorname{Inn}(n)b\). Its integral homology action is the same nonidentity action as that of \(b\). Thus the fixed-subgroup conclusion of Kochloukova--Zalesskii applies separately to every section, with no assumption that all sections are conjugate. Each fixed group is free pro-two and has vanishing degree-two mod-two cohomology.

Both integral characters restrict to the fixed-group factor of every normalizer. Their cup is therefore zero on every normalizer. Brown restriction is injective in degree three: \(P\) is open of cohomological dimension two and every finite subgroup injects into the quotient \(C_2\), excluding \(C_2^2\). It forces \(u\widetilde\theta\widetilde\psi=0\), whereas its associated graded term is the nonzero \(u\eta\) above. This is the required contradiction.

Only injectivity of Brown restriction is used. No finite-dimensional upgrade or normalizer-closure assertion is needed here.

## Primary source reinspection

I independently reopened the original author PDF:

https://mat.unb.br/~pz/arquivos/Claus3.pdf

Kochloukova--Zalesskii, *Automorphisms of pro-p groups of finite virtual cohomological dimension*: Theorem 2 (printed page 3) gives the required profinite restriction embedding for degrees strictly greater than the cohomological dimension of the open subgroup, under the absence of \(C_p^2\). Corollary 2 (printed page 2) and its Section 2 proof (printed pages 4--5) give the free pro-p fixed subgroup in a Demushkin group. The proof explicitly uses infinite index for a nonidentity finite p-group of actual automorphisms. The integral minus-identity summand verifies that nonidentity requirement for every section used in D.70.

## Final scope and finite two-subgroups

The contradiction excludes each negative odd coordinate of a quartic multiplier. The previously established square-one relation and positive dyadic coordinate then imply the global unit is one. D.50 lists exactly \(1,C_2,C_4,V_4,D_8\); their elements have orders one, two, or four. D.43 handles all order-two elements and D.70 handles all order-four elements. Hence every element of every listed finite two-subgroup has the global sign prescribed by its dyadic multiplier.

The text correctly retains the unresolved scalar cubic branch, arbitrary finite-action conjugacy, and recognition of the full fixed subgroups. The conclusion does not use any of these unresolved assertions.
