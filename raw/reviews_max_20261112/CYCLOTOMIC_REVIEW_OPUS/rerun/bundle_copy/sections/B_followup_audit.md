# Follow-up audit: C5, C8, B7, and B11

Completed 12 November 2026. No changes made to `C_root.tex`.

## C5: finite-kernel goodness proof

The finite-kernel argument is valid. Given a characteristic finite-index subgroup N of the finitely generated fibre group P, put A=P/N and Q=G/N. The centralizer C_Q(A) has finite index, maps to a finite-index subgroup B1 of B0, and has kernel exactly Z(A). Thus its extension is genuinely central, and its class lies in H²(B1,Z(A)) with trivial action. A continuous normalized cocycle on the profinite completion with finite coefficients factors through a finite quotient: uniform continuity and a sufficiently small common open normal subgroup give this factorization in both variables. Its restriction to the kernel of that finite quotient is the zero cocycle. Consequently the class vanishes on a finite-index B2. A splitting over B2 gives a finite-index subgroup of C_Q(A) disjoint from Z(A). Because C_Q(A) intersects A in Z(A), it is disjoint from A as well. Its inverse image in G therefore meets P exactly in N. This proves that P has its full profinite topology inside G. Finite-quotient correspondence proves the right exactness after completion.

The proof as initially read needed three citation or explanation additions, rather than a change of conclusion:

1. Goodness of the finite-index subgroup B1 is not stated in Bresciani Lemma 10.9. Cite his Lemma 10.10, which explicitly gives commensurability invariance of “very good.”
2. A free discrete group's length-one free resolution proves finite cohomology and the FL condition, but does not alone prove goodness. Supply the comparison: H¹ of a finite module is computed by derivations determined freely on a free basis, both before and after profinite completion; H^q vanishes for q>=2 for the discrete free group and free profinite group. The latter is the cohomological-dimension-one/projectivity fact. Alternatively use Hoshi Proposition 2.4 directly.
3. For an arbitrary characteristic-zero algebraically closed field, an embedding of a field of definition in C also uses invariance under algebraically closed field extension. Bresciani Lemma A.22 supplies it, citing SGA 1 XIII Proposition 4.6. SGA 1 XII.5.1 then supplies the complex comparison.

An independent exact primary result now opened is Hoshi 2014 Proposition 2.4(i),(ii), published pp.169–172. It proves both C5 maps under the stated normality and characteristic-zero hypotheses, and even for a relative hyperbolic polycurve over a normal base not already assumed to be a tower. The optional insertion is `sections/C5_hoshi_source.tex`.

## C8: nonvanishing now proved, not left as an obligation

The replacement `sections/C8_hoshi.tex` proves that the local map j_x has nonzero image for every normal-crossings compactification of a hyperbolic polycurve. It proves more precisely that the diagonal T→T^{I(x)}→π1(U_barK) is nonzero. The diagonal is invariant under branch permutations, so it yields a nonzero subgroup of the cyclotomic centralizer of every local section even before all branches become rational.

The key source is Hoshi 2014 Lemma 2.8, published pp.175–176. For a relative hyperbolic curve Y/S with S connected noetherian separated normal over a characteristic-zero field, a map from the fraction field of a strictly henselian DVR over S extends over the DVR exactly when its induced map to π1(Y) is trivial. Induction on the tower gives this criterion for U. An explicit arc at a boundary point uses the map of completed local rings z_i↦t for all boundary parameters and z_j↦0 for the remaining coordinates. Its punctured group maps by the diagonal. Vanishing would extend the same generic-point map to U; separatedness would force equality with the original arc into the compactification, contradicting its boundary closed point. This is a proof of the local nonvanishing task, without a section-surjectivity assumption.

The original blowup counterexample remains valid: local map T²→I0 is (m,n)↦m+n, kernel the antidiagonal. The converse requirement is now stated concretely. It already contains section surjectivity for curves through the maps from C×U03 to C: pair an arbitrary section of C with a fixed cusp section of U03. The product has nonzero centralizer, and a boundary-local factorization in the product compactification would make the first coordinate a point or cusp section.

## Carlson–Corwin 2611.09080v1

Downloaded and read the primary PDF, including visual verification of p.10. The PDF is `background/literature/B_sources/Carlson_Corwin_2611.09080v1.pdf`; extracted text and the p.10 rendering are beside it. Theorem 3.7 proves independence of the **closure** of the boundary section set. Proposition 4.12 says C_X ⊂ closure(𝒞_{X,f}), with an essential bar that pdftotext drops. Proposition 3.4 computes the local group and its Galois action, with the branch permutation action retained. Proposition 4.11 gives the exact equivalence between independence of the raw inductive cuspidal data for all polycurves and the curve section conjecture, under the stated injectivity hypotheses. The local nonvanishing proof above additionally uses Hoshi's valuative criterion; it does not infer nonvanishing from the rank of the local torus.

## B7: inverse-limit birational centralizer

The proof is valid with the cited R2 extension AE1. Specific checks:

- Every finite separable extension of K(X) is unramified on some nonempty K-open of X, so the maps E_L→E_U give the stated inverse limit; the same finite-cover argument on the geometric kernels gives P_L.
- Once z is detected on U0, it stays nonzero on all finer opens. A newly removed interior point has inertia killed on U0, so it cannot be the selected cusp; otherwise Stix Proposition 11 identifies the image cusp. Applying this to each pair of comparable opens proves compatibility.
- Each finite normalization of X occurs at some level. The compatible local DVRs form a directed valuation ring with fraction field Lbar. The section fixes that valuation, and its fixed underlying geometric point has residue K.
- Stix Lemma 10 identifies the *same* birational local inertia I_v with the cusp inertia at every hyperbolic open deleting the point. This makes the comparison maps on those inertia groups isomorphisms, justifying the passage from one coordinate of w∈C to equality w∈I_v throughout the inverse limit.
- Uniqueness also covers a second alleged decomposition valuation: choose a common hyperbolic open deleting both centres, apply the unique cusp result there, and then all refinements. Arithmetic equality follows from B6, not from an unstated property of the quotient.

No change of conclusion was required.

## B11: packet and scheme reconstruction

The proof is valid; two precision additions have been made in the owned file `sections/B_birational.tex`:

1. Define the packet set over K′ explicitly as conjugacy classes of nonzero centralizers. Restriction leaves each I_v unchanged. Thus the colimit is a colimit of packet *labels*, not a colimit of elements of the H¹ torsors. Define the G_K-action by conjugation with a lift in E_L and verify independence of that lift.
2. Expand independence of the auxiliary set J. On a common refinement J1∪J2, fill precisely the labelled cusps J\Ji. Its π1 is the quotient killing those cusp inertias, by the finite-normalization argument. The resulting affine hyperbolic curve therefore has the specified group isomorphism to the independently reconstructed curve for Ji. Tamagawa's strong Isom theorem makes this a unique curve isomorphism; unique extension to smooth compactifications and the same cusp labels make the filled opens and their inclusion maps compatible. This uses an actual group isomorphism, rather than applying the Isom theorem directly to a noninvertible quotient map.

The quotient R_U is correct: the inertia groups labelled by geometric points of U account for all closed-point inertia in the normalization of U. For a regular curve in characteristic zero, killing those groups is exactly finite étaleness. The reconstruction only claims determination up to K-isomorphism with compatible inclusion maps; it does not claim an effective algorithm or universal existence of a nonzero centralizer for arbitrary birational sections.
