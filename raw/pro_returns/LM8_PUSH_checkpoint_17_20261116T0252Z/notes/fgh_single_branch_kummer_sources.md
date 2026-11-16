# Single-branch Kummer argument: verified primary sources and scope

Status: notes-only candidates A.78 and A.79, pending root integration authorization. The original exploratory composite and its model-precision predecessor are preserved. No numerical computation is a premise of either proof; all local-ring, group and divisor identities are proved symbolically in the text.

## Verified sources

- **verified:** Stacks Project Lemma 15.116.4, Tag 0BRM, https://stacks.math.columbia.edu/tag/0BRM . Opened/read as turn1232view0 (also turn1223view1). Applied only to the characteristic-zero horizontal discrete valuation. It is not applied to the mixed-characteristic surface or used to remove vertical ramification.
- **verified:** Stacks Project Lemma 54.4.3, Tag 0C5H, https://stacks.math.columbia.edu/tag/0C5H . Opened/read as turn1229view0. Resolves a rational map from a regular surface to a proper target by closed-point blowups outside the existing morphism domain. This supplies the actual domination comparison; its intermediate models need not have reduced special fibre.
- **verified:** Stacks Project Lemmas 54.17.1–2, Tag 0C5Q, https://stacks.math.columbia.edu/tag/0C5Q . Opened/read as turn1229view1. Proper birational regular-surface comparisons factor into point blowups.
- **verified:** Stacks Project Lemma 55.8.5, Tag 0CD9, https://stacks.math.columbia.edu/tag/0CD9 . Opened/read as turn1229view3. A regular proper model contracts exceptional curves of the first kind to a minimal regular model.
- **verified:** Stacks Project Lemma 55.14.5, Tag 0CDG, https://stacks.math.columbia.edu/tag/0CDG . Opened/read as turn1232view2. Existence of a semistable model implies that the minimal regular model is semistable. Together with the positive-genus main component and constant-image descent, this retains the smooth Kummer neighborhood and its actual map to the old good model.
- **verified:** Stacks Project Lemma 55.14.3, Tag 0CDE, https://stacks.math.columbia.edu/tag/0CDE . Opened/read as turn1232view3. Nodal surfaces resolve by blowups at singular points; these do not alter a pre-existing smooth neighborhood.
- **verified:** Yu Yang, *p-groups, p-rank, and semistable reduction of coverings of curves*, author primary https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf . Complete Definitions 1.5, Proposition 1.6 and Remark 1.6.1 (author pp.9–10), Theorem 1.9 (p.11), and Proposition 1.4 read. Fresh opens turn1241view2/turn1242view2, earlier turn1219view1, and exact local text read. The theorem is used only after the new point is smooth and unmarked. Remark 0.1.1's warning for arbitrary marked or singular fibres is retained; no such unrestricted assertion is cited.
- **verified:** Michel Raynaud, *p-groupes et réduction semi-stable des courbes*, original printed pp.179–180, https://page-one.springer.com/pdf/preview/10.1007/978-0-8176-4576-2_7 . Successfully reopened through the earlier indexed source as turn1227view0/1 and turn1232view1 (direct URL attempts had failed). Proposition 1(i)–(ii) is read in full. In A78 it is applied only on the regular open X minus P, where the sole possible branch divisor is the smooth vertical divisor. Its constant inertia quotient gives the connected étale D/I cover of the punctured special base and the purely inseparable residue comparison. Original Theorem 1 concerns unramified generic covers and is not directly applied to the ramified cover.
- **verified:** Claus Lehr–Michel Matignon, *Automorphisms of curves and stable reduction*, Theorem 6.13, published p.154 / author p.21, https://arxiv.org/pdf/math/0411059 . Fresh exact theorem read as turn1242view0, full source turn1241view0. Only the nilpotent, separated-horizontal-branch potential-good-Jacobian/tree assertion is used. Generic characteristic zero supplies its generic tameness hypothesis. No marked-fibre slope conclusion is imported.
- **verified:** Richard Crew, *Etale p-covers in characteristic p*, Corollary 1.8, printed pp.35–36, https://www.numdam.org/item/CM_1984__52_1_31_0.pdf . Fresh exact context read as turn1242view1, full source turn1241view1; page images had been independently viewed in the preceding A69 audit. The formula is used on a smooth proper component cover, not a semistable whole curve.
- **verified:** Dupuy–Rabinoff, Theorem 1.1 and Proposition 3.2, primary previously opened in the A71/A74/A76 audits (including root turn1196view0). A79 uses precisely the same relative compact-type Abel map, including node extension and rational components, followed by the actual good-Jacobian homomorphism. Its changed residue-prime hypotheses are checked explicitly.

## New deductions, not quoted theorems

1. Jet interpolation constructs an actual global Kummer curve with local completed ring R[[z]].
2. Contractions preserve the actual map to the positive-genus good base: each rational contracted curve has constant image; the proper graph image is finite birational over a normal contraction target.
3. Horizontal inertia is removed, while vertical ramification may remain. Raynaud then applies at the new unmarked smooth point.
4. Actual source-map resolution dominates each old positive-genus component by a positive-genus component in the new vertical fibre. Rational exceptional curves cannot dominate it.
5. For the global one-point cover of a rank-zero base, Raynaud's inertia quotient and the smooth one-point Deuring–Shafarevich formula force rank zero on every main component.
6. Cyclic derived group makes actual inertia normal and equal to the full derived group, producing actual p-primary cusp differences by elliptic pullback. This hypothesis is separate from the general rank-zero conclusion.
7. The coprime abelian factor is treated by an actual connected isogeny pullback, not by fixed-element lifting or an unspecified component.

## Scope retained

Mixed characteristic (0,p), positive-genus good base, one horizontal branch section through the local point, and no other branch reduction there are essential stated hypotheses. The arithmetic application uses a supersingular place of E: 2 or an odd prime congruent to 3 modulo 4. The universal Task A.5 remains Open. Arbitrary p-group inertia does not acquire a cusp-divisor relation merely from A78.


## Registration update

A.78 and A.79 were authorized by root after full root, DE and PBC proof/source audits and registered on 2026-11-16. Candidate status and SB display labels were changed editorially in the canonical copies; precise Stacks citations were attached. Exact source/canonical hashes and diffs are in notes/fgh_A78_A79_integration.json. No numerical computation is a premise.
