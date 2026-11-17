# Exact standard mixed-reflection control on the derived free group

Checkpoint36 research beyond the frozen formal slate. This is an elementary control calculation, with a prescribed finite certificate, not a claimed evaluation of the actual general GT-involution class. We claim no literature priority.

Let E be the full free profinite group on X,Y, let E′ be its closed derived subgroup, and use [a,b]=aba⁻¹b⁻¹. The actual standard elliptic involution of A122 is

\[
c(X)=X^{-1},\qquad c(Y)=XYX^{-1}.
\]

It has determinant−1 on the actual abelianization \(E_{ab}=\widehat{\mathbb Z}^{2}\), with matrix diag(−1,1). It is distinct from the simultaneous-inversion involution θ of the based-forgetting note, whose matrix is −I.

We prove the following statements for this exact standard action:

\[
E^c=1,\qquad (E')^c=1,\qquad
H^1(C_2,E';c)\simeq\widehat{\mathbb Z}
\tag{1}
\]

as pointed compact spaces. The explicit parameter map is

\[
n\longmapsto[\delta_n],\qquad
\delta_n=Y^{-n}c(Y^n)=Y^{-n}XY^nX^{-1}.
\tag{2}
\]

In particular the entire derived cohomology is nontrivial even for the standard mixed reflection. This is not the assertion that the specified original elliptic cocycle is nontrivial: for φ=1 its actual base transporter is the identity.

## 1. Actual discrete presentation and completion

First use the discrete free group E₀=F(X,Y), with exactly the same involution. Its semidirect product has presentation

\[
G_0=\langle X,Y,t\mid t^2=1,\ tXt=X^{-1},\ tYt=XYX^{-1}\rangle.
\]

Set v=Xt and Z=tYt. Then v²=1. The last relation gives

\[
vZv^{-1}=XYX^{-1}=Z.
\]

Conversely, in the presentation \(t^2=v^2=[v,Z]=1\), put X=vt and Y=tZt. Then tXt=X⁻¹, and

\[
tYt=Z=vZv^{-1}=XYX^{-1}.
\]

These two changes of generators are inverse. Thus the actual discrete group is

\[
G_0=C_{2,t}*(C_{2,v}\times\mathbb Z_Z).
\tag{3}
\]

The original E₀ has index two, the kernel of the character sending t and v to1 and Z to0. Every finite-index subgroup of E₀ has a finite-index core in G₀. Consequently its full topology is induced, and completion gives exactly

\[
\widehat G_0=E\rtimes_c C_2.
\tag{4}
\]

This also follows directly from the two inverse profinite presentations; no infinite-index completion is identified.

## 2. Entire involution classes and the actual fixed subgroup

In the ordinary Bass–Serre tree of (3), the edge stabilizers are trivial. An involution fixes a vertex: take the center of the finite subtree spanned by an orbit, after the usual barycentric subdivision. A nontrivial vertex stabilizer fixes no adjacent edge, hence has no second fixed vertex. The two vertex types therefore give exactly two conjugacy classes of involutions, represented by t and v. The second vertex group C₂×Z has exactly its one nonidentity torsion element v. A centralizer of t fixes its unique vertex, so \(C_{G_0}(t)=\langle t\rangle\).

The prime-order comparison and centralizer result of Boggi and Zalesskii (2025, Theorem A, its prime-two case) apply to this actual G₀. Here E₀ is a free normal subgroup of finite index and finite rank. Characteristic finite-index subgroups of E₀ show residual finiteness and exact completion. Free-group goodness and the discrete/profinite LHS comparison for the finite quotient give goodness. Finite-rank free resolutions and the finite-group resolution also give the high-degree comparison for every discrete continuous F₂-module, by passage through its finite invariant submodules. Virtual cohomological dimension is one and all required finite-type conditions hold. Thus this is the same completely checked prime-order scope used in A124, with simpler virtually free hypotheses; it does not invoke the disputed nonsolvable finite-subgroup centralizer step.

It follows that \(\widehat G_0\) has precisely those two conjugacy classes of involutions and that

\[
C_{\widehat G_0}(t)=\langle t\rangle.
\tag{5}
\]

Each involution projects nontrivially to G₀/E₀. Full-group conjugacy to t or v can therefore be made E-conjugacy: if a conjugator has odd projection, multiply it on the right by the representative t or v that it conjugates. This removes its projection and leaves its conjugation unchanged. Hence H¹(C₂,E;c) has exactly the two classes represented by1 and X. Equation (5) implies \(E^c=C_{\widehat G_0}(t)\cap E=1\).

The primary proof actually read for this application is the supplied Boggi–Zalesskii source, its definitions and Theorem A, centralizer/normalizer lemmas, full preliminary prime-order lemma, and complete prime-order proof. Those exact ranges and the source hash are recorded in the A124 reviews. No fresh higher-prime-power or whole-paper reading is asserted here.

## 3. The complete derived coefficient space

On Eab, a C₂ cocycle is a vector (x,0), since the norm is (0,2y) and multiplication by2 on \(\widehat{\mathbb Z}\) is injective. Coboundaries are (−2x,0). Therefore

\[
H^1(C_2,E_{ab};c)=C_2,
\]

and the two classes of H¹(C₂,E;c) map to its two different elements. Every E′-valued cocycle consequently belongs to the neutral E-valued class. If a∈E′ is a cocycle, write a=g⁻¹c(g) with g∈E. Its abelianization forces the X-coordinate of g to be zero; let n be its Y-coordinate. There is b∈E′ with g=Yⁿb, so

\[
a=b^{-1}\delta_n c(b).
\]

This proves surjectivity in (2). If δm and δn differ by an E′ coboundary, the two associated E cobounding elements differ by a c-fixed element of E. Equation (5) makes that element1; their abelian Y-coordinates are then equal, so m=n. This also proves injectivity without choosing a continuous cobounding element.

The cocycle set is closed in the compact group E′. Its E′ action is continuous, so the orbit space is compact Hausdorff: the orbit equivalence relation is a compact image and hence closed. The parameter map (2) is continuous, because continuous profinite powers and the quotient map are continuous. A continuous bijection from compact \(\widehat{\mathbb Z}\) to that Hausdorff orbit space is a homeomorphism. This proves (1) at the stated actual topology. The fixed subgroup assertion for E′ follows by inclusion in Eᶜ.

## 4. A prescribed finite check of the nonzero class

Use the actual marked quotient to the dihedral group of order eight acting on {0,1,2,3}:

\[
X:i\mapsto i+1,\qquad Y:i\mapsto-i\quad(\bmod4).
\]

Conjugation by the involution XY induces the exact c action: X↦X⁻¹ and Y↦XYX⁻¹. The derived subgroup is {1,X²}, on which this action is trivial. The image of δ₁ is X²≠1, a cocycle, while every derived coboundary is1. Thus δ₁ is already separated from the neutral derived class by this one actual equivariant finite quotient.

The complete program is `code/check_standard_elliptic_reflection_derived_class36.py`, SHA256 `a81392a638a156526eb303685a2f9a9c34fdfda0d235ccf29f3614862730d988`. Root actually executed it once, with exit0 observed in tool chunk `49abf9`. Its full genuine output is `records/standard_elliptic_reflection_derived_class36.json`; its error file is empty. The complete output was read. It verifies the order-eight group, both generator-action formulas, involutivity and multiplicativity on every group pair, the complete derived subgroup and its coboundary set, and the specified nonzero cocycle. This is one prescribed certificate, with no finite-group search.

## 5. Boundary for the ongoing original problem

This control proves that an assertion of trivial derived C₂ cohomology for every relevant mixed reflection would be false. It supplies the strongest exact statement for this standard action, namely the entire pointed compact space (1). The general actual β₂ and κ₀ in the Brunnian notes are not silently conjugated to this action. Their specified classes, the original third-cusp equation and the original CM frame remain unevaluated.
