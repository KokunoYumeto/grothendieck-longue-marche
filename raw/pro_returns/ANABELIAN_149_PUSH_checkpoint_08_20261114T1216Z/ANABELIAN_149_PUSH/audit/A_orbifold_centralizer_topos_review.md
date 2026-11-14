# Independent review: the orbifold centralizer fibre criterion

**Reviewer:** `/root/topos`. **Date:** 14 November 2026. **Outcome:** the candidate proof passes this review; no precise gap found. This review does not modify Part A or enlarge the asserted class beyond the stated prime-to-p Galois hypotheses.

## Material independently opened

I read the complete `audit/A_orbifold_centralizer_candidate.md`, the integrated statements and proofs A.8, A.21, and the relevant beginning of A.22. I independently opened Boggi–Zalesskii, *A restricted Magnus property for profinite surface groups*, <https://arxiv.org/pdf/1408.5419>, Lemma 3.1(i)–(ii), printed pp. 7–8, including its proof. The source defines a class S to be closed under subgroups, homomorphic images and extensions, and explicitly assumes a torsion-free normal subgroup with quotient in S. It proves both malnormality/self-normalization of finite orbifold decomposition groups and containment of **every** nontrivial finite subgroup in one of them. The proof first handles solvable finite subgroups, then proves all Sylow subgroups cyclic and uses the resulting solvability; its conclusion is not limited to solvable input groups.

## 1. Geometric exactness and the admissible completion

Let B° be the complement of the branch locus and C° its inverse image. Since the geometric Galois group G has prime-to-p order, the induced prime-to-p topology on the kernel of the punctured cover is the full one. More explicitly, a finite prime-to-p quotient of the kernel can be replaced by the intersection of its finitely many G-conjugate kernels; the resulting extension by G still has prime-to-p order. Thus the geometric prime-to-p kernel is the prime-to-p fundamental group of C°.

Filling C° kills exactly the local inertia at every missing point. In the group of B°, these are the conjugates of the powers x_b^{e_b}. Their closed normal subgroup inside the kernel is already normal under the whole punctured group: its conjugates simply permute all the points above the branch fibres. Consequently the quotient has the claimed exact sequence

\[
1\longrightarrow \Pi_C^{(p')}\longrightarrow \Gamma\longrightarrow G\longrightarrow1.
\]

The inertia of order e_b embeds in G, because its image is the actual stabilizer of a point of the tame Galois cover. The standard prime-to-p surface presentation therefore produces a discrete orbifold group mapping onto G with all prescribed torsion orders retained. Its kernel is the corresponding torsion-free surface group. Riemann–Hurwitz gives positive orbifold Euler measure from g(C)≥2. This supplies the exact torsion-free-normal-subgroup hypothesis of Boggi–Zalesskii. There is no illicit inference from a full profinite theorem to a different completion.

In the unramified case the same theorem gives torsion-freeness of Gamma, since the list of finite orbifold inertia groups is empty.

## 2. Arithmetic exactness and local intersections

After a finite constant extension defining G, the cover C°→B° is a genuine G-torsor over the base field, so its arithmetic fundamental group has a quotient onto the constant group G. Taking the geometrically prime-to-p quotient preserves this quotient and the corresponding kernel for the same prime-to-p cofinality reason. The power-inertia normal subgroup is stable under the full arithmetic group: Galois permutes the branch points and acts on tame generators by unit powers. Its arithmetic quotient consequently has both exact sequences displayed in the candidate, retaining the **full** constant-field Galois group.

For a rational ramified point R, a local arithmetic decomposition group at f(R), after killing the e_bth-power inertia, has kernel I_R over G_k. Its map into G restricts injectively to I_R. The subgroup arising from the actual point R belongs to E and maps isomorphically to G_k. Hence

\[
D_R=I_R\rtimes s_R(G_k),\qquad D_R\cap E=s_R(G_k).
\]

The intersection is an equality of the selected embedded subgroups, not only a statement about outer conjugacy: if i s_R(\sigma) maps trivially to G, injectivity on I_R gives i=1. Rationality of R is what permits the point complement to project onto all of G_k. A finite constant extension can supply rationality and trivialize the finite inertia action. In fact, when the deck action and R are already rational, its faithful tangent character takes values in the ground field; adjoining the relevant roots of unity is harmless and makes the intended centralization explicit.

For the normalizer equality, choose d in D_R with the same arithmetic image as a normalizer element gamma. Then gamma d^{-1} lies in the geometric group and normalizes I_R, so Boggi–Zalesskii puts it in I_R. Thus N_{Gamma_ar}(I_R)=D_R. This uses only a proved geometric self-normalizer statement and surjectivity D_R→G_k, rather than assuming a separate arithmetic inertia theorem.

For a geometric conjugate inertia, normality of E makes its intersection with E the correspondingly conjugated actual point section. The image of the geometric conjugator in G sends R to the actual point on C involved. Conjugation by the remaining Pi-component changes only the path. This keeps the later equality of point sections correctly based.

## 3. Triviality of the geometric point-section centralizer

The independent weight argument is especially clean. Given a nontrivial h commuting with the actual point section, choose an open characteristic N detecting h and form H=\overline{\langle N,h\rangle}. The subgroup H is stable under the section, and H/N is a nontrivial finite cyclic quotient. The pointed finite étale neighbourhood defined by Hs(G_k) has geometric prime-to-p group H. Therefore h has nonzero image in H^ab, since it maps nontrivially to H/N.

On the other hand it is Frobenius-fixed. For this proper smooth curve, H^ab is the product of the prime-to-p Tate modules of its Jacobian. On each rational Tate module the eigenvalues of Frobenius have weight one and none is 1; each integral Tate module is torsion-free. Thus Frobenius minus one is injective on the full product. This contradiction proves the required centralizer vanishing over every finite constant extension.

This argument does not assume that h survives in the abelianization of the original Pi. The detecting abelianization is that of H, chosen using h. It also avoids reliance on the earlier torsion-compatible deck-transformation argument if the author wants a single self-contained proof.

## 4. The finite centralizer and the second constant extension

If equal point sections P,Q lie in one Galois fibre, a deck element g sends P to Q. A geometric lift gamma of g acts on E by that deck automorphism. The assumed geometric equality of the point sections permits adjustment by an element of Pi so that gamma centralizes the selected s_P exactly. If P≠Q, gamma is nonidentity.

The centralizer H=C_Gamma(s_P(G_k)) injects into G, because its kernel is the just-proved trivial centralizer in Pi. It is therefore finite. The finite-subgroup theorem places it in a unique maximal inertia I. Since s_P centralizes H, every arithmetic conjugate of I still contains nontrivial H; malnormality forces it to equal I. Thus s_P normalizes I.

After making its actual point R rational and splitting inertia, the normalizer and intersection identities give s_P(G_L) contained in s_R(G_L). Both project isomorphically onto G_L, so they are the **same homomorphism** with the chosen paths. Applying the stipulated fibre criterion over L gives f(P)=f(R). The Galois property now matters: since R is ramified, every point in its fibre, including P, is ramified.

The final step correctly takes a second finite extension. Choose the inertia I_P with path compatible with the original representative s_P. After trivializing its finite action, I_P centralizes s_P(G_L). The larger centralizer H_L remains finite by the weight argument and contains both the original gamma and nontrivial I_P. Its containing maximal inertia J must equal I_P by malnormality. Thus gamma lies in I_P, so g fixes P. This contradicts Q=gP≠P. There is no assumption that the inertia I first found was already the inertia of P, and no tacit retention of a centralizer identity under extension: the centralizer is explicitly recomputed as H_L and its finiteness reproved uniformly.

## 5. Scope of the consequences

A ramified prime-to-p Galois cover of a genus-one curve has a branch fibre with one common nontrivial index. A.21 gives exactly the stipulated fibre property over every finite constant extension. Riemann–Hurwitz forces ramification when g(C)≥2. This proves the elliptic-quotient consequence without an ordinary/supersingular or commutativity assumption.

For a hyperbolic base already satisfying A1 uniformly, functoriality gives the fibre property. For a solvable Galois quotient of a genus-zero curve, the normal-subgroup induction decreases the group order in each case: quotient group G/N for a hyperbolic intermediate, the elliptic consequence for genus one, and subgroup N for a genus-zero intermediate. Prime-order groups are precisely the earlier cyclic base case. The induction is valid.

Spreading the finite group action and tame quotient, with disjoint rational sections, fits A.8 after shrinking; the tame degree and quotient genera remain in the proved class. The open-curve consequence follows by the proper compactification quotient. None of this applies to an arbitrary tame map whose geometric Galois closure has p-divisible order, or automatically supplies the nonsolvable genus-zero case.

**Recommendation:** promote the stated fibre criterion and its specified consequences. Retain the prime-to-p Galois condition and the explicit second constant extension. The two-letter reuse of S for branch locus and group class can be changed for readability, but it is not a mathematical gap.
