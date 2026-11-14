# Independent review of the formation-closure reconstruction candidate

Reviewer: degeneration agent. Date: 14 November 2026.

Reviewed text: audit/F_proformation_reconstruction_candidate.md, proposed F.44, Sections 1–10. The underlying full support-two construction was also reread in sections/F.tex, F.24; the arithmetic predicates were compared with sections/F_solvable_closure_extension.tex, F.43.

**Conclusion: the new extension passes in its stated sufficient-class scope.** In particular, survival of a literal alternating subgroup in the specialization kernel is enough; no solvable-residual containment is needed or justified. This review supplies no intrinsic converse for F.9 and no priority claim.

## 1. The alternating subgroup and the actual commutators

The closure assumptions imply that a proper class \(\mathcal C\) excludes every sufficiently large alternating group. Indeed every finite group embeds in a symmetric group, and \(S_m\) embeds in \(A_{m+2}\) by the parity-correcting action on two additional letters. If \(\mathcal C\) contained arbitrarily large \(A_n\), subgroup closure would put every finite group in \(\mathcal C\).

In the pencil construction, the spanning-tree gauge gives a **literal** \(S_n\subset H\), with zero coordinate labels. This is stronger than a surjection from \(H\) to \(S_n\), and is exactly what the coordinate calculation uses. F.24 proves the literal inclusion from decorated transpositions. Its remaining branch generators give elements \(u\in H\cap N^n\) of support at most two, whose labels collectively generate \(N\). Full \(N^n\) is neither assumed nor needed.

The specialization subgroup
\[
J=\operatorname{Gal}(\Omega L/L)
\]
is normal in \(H\), since \(L/F\) is Galois. Its quotient \(H/J\) is in \(\mathcal C\). The kernel of \(A_n\to H/J\) is normal in the simple group \(A_n\). If the kernel were trivial, \(A_n\) would be a subgroup of a group in \(\mathcal C\), contradicting hereditary closure and the choice of \(n\). Thus \(A_n\subset J\).

For a chosen coordinate \(i\) in the support of \(u\), there is a literal \(\tau\in A_n\) with \(\tau^{-1}(i)\) outside that support: the complement is nonempty and \(A_n\) is transitive. With the convention \([u,\tau]=u\tau u^{-1}\tau^{-1}\), normality gives
\[
[u,\tau]\in J,
\qquad
[u,\tau]\in N^n,
\qquad
[u,\tau]_i=u_i u_{\tau^{-1}(i)}^{-1}=u_i.
\]
The first inclusion uses \(u\in H\), \(\tau\in J\), and \(J\triangleleft H\); it does **not** require \(u\in J\). The second follows directly in the semidirect product because the permutation component cancels and all labels of \(u\) lie in \(N\). Conjugation by the literal \(S_n\subset H\) preserves \(J\) and transports the isolated coordinate labels. Since those labels generate \(N\), the coordinate projection \(J\cap N^n\to N\) is surjective at every coordinate.

The constant-field quotient is also retained. The equality \(M\cap L=F\) gives \(J\to P\) surjective. If \(h\in J\) has a prescribed \(P\)-image, choose a literal even permutation moving \(h(i)\) back to \(i\). Multiplication by that element produces an element of \(J_i=J\cap\operatorname{Stab}(i)\) with the same \(P\)-image. Hence \(J_i\to G\) contains \(N\) and maps onto \(P\), so it is surjective. The literal even permutation has trivial constant image, and no perfectness assumption on \(P\) is used.

These steps isolate every required factor, including factors of \(N\) that themselves belong to \(\mathcal C\). They do not attempt to force those factors to survive by simplicity. They survive through the commutator coordinate calculation after \(A_n\) has survived.

## 2. Constants and missing arithmetic extensions

For \(C_0=K\cap\overline{\mathbf Q}\), regularity of \(K/C_0\) identifies conjugates and gives
\[
K^{\mathcal C}\cap\overline{\mathbf Q}=C_0^{\mathcal C}.
\]
For the nontrivial inclusion, if an algebraic number lies in a finite Galois \(\mathcal C\)-extension of \(K\), its entire normal closure over \(C_0\) lies there. Its group is a quotient after regular base change, hence belongs to \(\mathcal C\).

For an \(S_n\)-extension of \(C_0\), the intersection with \(C_0^{\mathcal C}\) is exactly its quadratic \(A_n\)-fixed field. Any larger Galois subextension would have a quotient in which the simple \(A_n\) survives, contrary to subgroup closure. The quadratic subextension is present because cyclic groups belong to \(\mathcal C\). Consequently \([k\overline{\mathbf Q}:k]\) is infinite. A finitely generated extension \(L/k\) cannot contain this algebraic extension, since its relative algebraic closure of \(k\) is finite. The resulting missing finite Galois **number field** is the precise constant-field input needed by the Gauss valuation argument.

All finite descent fields can contain \(K\) and the prescribed finite data while still satisfying \(L=Fk\). Then \(L/F\) is Galois pro-\(\mathcal C\), by the closed-subgroup property. The same construction applies after finite extension of \(L\).

## 3. Radical closure and the fixed field at every root level

The radical-closure argument uses extension closure and all finite abelian groups in \(\mathcal C\). Adjoining all conjugate radicals over a finite Galois \(\mathcal C\)-extension gives a finite Galois extension with abelian kernel, hence still in \(\mathcal C\).

In the divisibility calculation, \(\sigma\in\operatorname{Gal}(Mk/k)\) and \(\tau\in\operatorname{Gal}(Mk/F)\), with \(F=MS\), commute because they commute separately on \(M\) and on \(k\), which generate \(Mk\). The field \(M\) is normal over the initial finitely generated base, \(\sigma\) fixes \(k\), and \(\tau\) fixes \(M\) and preserves the normal field \(k\). Thus \(\sigma z/z\) lies in the single fixed finitely generated field \(F\), independently of the root exponent. This is exactly the uniformity needed to invoke \(D(F^\times)=1\). No assertion that \(\operatorname{Gal}(Mk/k)\) is solvable appears.

The normal proper model argument therefore gives \(D(L^\times)=k^\times\), also after finite extension. The proof correctly treats the finite relative constant field before applying the finite-extension divisibility calculation.

## 4. The remaining reconstruction predicates

The Gauss valuation step retains the missing number field, a nontrivial action on the finite constant field, a fixed finitely generated field containing the actual evaluated value, commuting automorphisms on the compositum, and norms to the fixed model field. These are precisely the predicates used by F.43. Nothing in the valuation or norm calculation requires a solvable Galois group.

The generalized Albanese argument still descends Jannsen's comparison to a finitely generated field; it is not applied to \(K^{\mathcal C}\). Normality gives the action on coinvariants, and the newly proved finite arithmetic-quotient detection gives the spanning statement for point Kummer images. Restriction to a finite-index subgroup does not change the rational span of a homomorphism into a characteristic-zero vector space. The later curve norm, unit-divisor, unbounded-degree, and point-function arguments retain their stated hypotheses.

The invocation of CHW is in the actual pinned, closed-point-preserving convention and relies on its precise criterion, rather than treating agreement of point functions as an independent full-topos theorem.

## 5. Arbitrary subfields and the virtual formulation

Given a subfield \(k_0\subset L\), the relative constants \(C\) of \(\mathbf Q(B)\) in the finite descent field are finite over \(\mathbf Q(B)\). Regularity and normality place the normal closure of each \(C(a)/C\), \(a\in k_0\), inside \(L\), with group in \(\mathcal C\). Hence \(k_0\subset C^{\mathcal C}\). The extension used for descent is algebraic, as required.

For the converse description, there are finitely many conjugates of \(C^{\mathcal C}\), indexed by the finitely many embeddings of \(C\). After adjoining the finite normal closure \(C'\), each **base change** \(C'(C^{\mathcal C})^\sigma/C'\) is pro-\(\mathcal C\). Their compositum is pro-\(\mathcal C\) over \(C'\), and its quotient containing the normal closure of \(k_0\) is virtually pro-\(\mathcal C\). I suggested spelling out “base change” here, since an individual conjugate need not itself contain \(C'\); this is an exposition clarification, not a mathematical gap.

## 6. Strictness beyond the virtually prosolvable class

The class defined by bounding the orders of nonabelian simple composition factors is hereditary: intersect a subgroup with a composition series, then refine the subgroup factors. A subgroup of a bounded-order simple factor has composition factors of at most that order; a subgroup of a cyclic prime factor is cyclic or trivial. Quotient and extension closure follow from composition series. Thus \(\mathcal C_{60}\) satisfies all hypotheses and contains \(S_5\).

The map \(x\mapsto x^5-x\) has four simple critical points with distinct critical values. Its finite branch transpositions generate a connected transposition graph, hence \(S_5\). Equality of geometric and arithmetic monodromy gives a regular \(S_5\)-extension of \(\mathbf Q(t)\). Full-group Hilbert specialization after constant base change gives successively jointly disjoint \(S_5\)-extensions of \(\mathbf Q\).

Their product is a quotient of \(\operatorname{Gal}(\mathbf Q^{\mathcal C_{60}}/\mathbf Q)\). The image of every open subgroup is open in that product and contains all factors outside a finite set. It consequently has an \(S_5\)-quotient and cannot be prosolvable. Since every finitely generated subfield of this algebraic extension is a number field, the virtual description in F.43 excludes this field from that earlier sufficient class. The claimed strict extension is valid.

No new source theorem is introduced by this review. The new group and field deductions are checked above; the exact primary geometric and reconstruction inputs remain the already opened sources listed in the candidate.
