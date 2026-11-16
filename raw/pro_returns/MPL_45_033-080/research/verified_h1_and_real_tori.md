# Verification memo: neutral H¹ fibre and real maximal tori

Independent mathematical check for the research notes. No scan was viewed and no frozen transcription was changed.

## 1. A singleton neutral fibre does not imply injectivity

Use constant group schemes over R, so the Galois group Gal(C/R) = {1, sigma} acts trivially on their geometric points. For a constant finite group F, the cocycle equation is x² = 1 for x = z(sigma), and cohomology identifies x with its F-conjugates. Thus H¹(R,F) is the pointed set of conjugacy classes of elements of order dividing 2.

Let

\[
V_4=\{1,a,b,c\}\subset S_4,\qquad
a=(12)(34),\quad b=(13)(24),\quad c=(14)(23).
\]

The subgroup V₄ is normal. The subgroup fixing 4 is S₃, intersects V₄ trivially, and has order 6, so S₄ = V₄ ⋊ S₃ with the natural action permuting a,b,c. This semidirect-product action is nontrivial even though the separate Galois action is trivial.

Since V₄ is abelian and every element squares to 1, H¹(R,V₄) has exactly four elements. Conjugation by (123) cycles a → c → b → a, so the three nonidentity classes have the same image in H¹(R,S₄). The full map is:

| Target class in H¹(R,S₄) | S₄ conjugacy-class size | Preimage in H¹(R,V₄) |
|---|---:|---|
| Identity | 1 | {1} |
| Double transposition | 3 | {a,b,c} |
| Transposition | 6 | empty |

These are all the involution classes of S₄. Consequently the map is noninjective although its neutral fibre is the singleton {1}; a nonidentity permutation cannot be conjugate to the identity.

**Verification:** an exhaustive calculation on the 24 permutations confirmed normality, the S₃ complement, all three involution classes, and the displayed fibres. The argument above is also a complete direct proof.

**Scope:** this illustrates the general pointed-set/nonabelian-H¹ issue. Constant finite groups are not the connected semisimple algebraic groups of the manuscript, so the example alone must not be described as a counterexample to a statement carrying those additional hypotheses.

## 2. Two maximal R-tori in SL₂ that are not R-conjugate

Define

\[
T_s=\left\{\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}:t\in\mathbf G_m\right\},
\]

and

\[
T_c=\left\{\begin{pmatrix}a&-b\\b&a\end{pmatrix}:a^2+b^2=1\right\}
      \simeq R^1_{\mathbf C/\mathbf R}\mathbf G_m .
\]

After extending scalars to C, the two eigenvalues in T_c are a+ib and a−ib, whose product is 1. Thus T_c becomes G_m and is an R-torus; T_s is already split.

**Maximality.** Put D = diag(2,1/2) and J = ((0,−1),(1,0)). Direct matrix commutation gives

\[
Z_{\mathrm{SL}_2}(D)=T_s,\qquad
Z_{\mathrm{SL}_2}(J)=T_c .
\]

These calculations remain valid after base extension to C. Any torus containing the respective torus commutes with D or J, so the centralizer equalities prove geometric maximality of both tori.

**Nonconjugacy.** The element J belongs to T_c and has characteristic polynomial X²+1. Every real point of T_s is diagonal with real eigenvalues. If a real matrix conjugated T_c to T_s, it would conjugate J to such a diagonal matrix, which is impossible. They are therefore not even GL₂(R)-conjugate, hence not SL₂(R)-conjugate.

**Exact limit of the counterexample.** Since R is a field, it is a local ring; the pair refutes a statement that *arbitrary* maximal tori are conjugate over every local base. It does not refute existence of maximal tori, conjugacy of maximal split tori, or étale-local conjugacy: both tori exist, only T_s is R-split, and they become conjugate over C. Nor does it refute a statement restricted to maximal tori contained in an R-defined Borel: such Borels in SL₂ stabilize real lines, whereas J has no real invariant line, so T_c is not Borel-compatible.

**Independent primary-source confirmation.** The exact pair appears as Example 4.2.3, p. 12, in Brian Conrad's Winter 2010 course notes, typed by Sam Lichtenstein, dated July 19, 2017. Example 4.1.2 describes the real circle torus, and the preceding Theorem 4.2.1/Remark 4.2.2 distinguish maximal split tori from arbitrary maximal tori. [Official Stanford PDF](https://math.stanford.edu/~conrad/249BW16Page/handouts/alggroups.pdf).

## Suggested short note wording

**H¹ illustration.** For constant V₄ ⊂ V₄ ⋊ S₃ ≅ S₄ over R, cocycles are involutions and equivalence is conjugacy. Hence H¹(R,V₄) has four elements, while its three nonzero elements map to the single double-transposition class in H¹(R,S₄), although the neutral fibre is {1}. This verifies the general warning that a trivial neutral fibre does not imply injectivity; it is a finite-group illustration, not by itself a counterexample within the manuscript's semisimple-group hypotheses.

**Conditional local-torus counterexample.** If the local-base question is meant to assert conjugacy of arbitrary maximal tori, SL₂ over R disproves it: the split diagonal torus and the norm-one circle torus are maximal but not even GL₂(R)-conjugate. The matrix J in the circle torus has nonreal eigenvalues, which proves the nonconjugacy. This does not answer a different question about existence, étale-local conjugacy, or tori required to lie in a Borel defined over the base.

