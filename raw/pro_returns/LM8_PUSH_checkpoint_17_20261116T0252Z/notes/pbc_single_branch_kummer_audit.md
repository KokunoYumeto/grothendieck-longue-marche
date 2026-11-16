# Independent single-branch Kummer audit

Status: **PASS** for the complete local structural proof.

Audited file: `notes/fgh_single_branch_kummer_draft.tex`; SHA256 `76f07253e404516127ff08ce569651318e136ff80f0c95a06a25213d6c1c6dfb`; 260 lines.

Complete local Kummer/model/domination proof in the 260-line candidate; global consequence and arithmetic application also read, with their source audit independently allocated to DE/root. No canonical registration by this auditor.

## global jet

PASS. A horizontal ample divisor away from P supplies sections of O(nD); relative H1 vanishing for nD-2P prescribes the zero constant jet and a generating conormal jet. The resulting rational t is regular near P, has divisor P near x and unit derivative, so other horizontal zeros and poles avoid x.

## actual connected normalization

PASS. The valuation-one zero at P makes z^e=t irreducible even after algebraic closure of the coefficient field. The completed normalization at x is R[[z]], with a single underlying special point above x. Excellence/finite normalization and regularity of completion identify the actual local normalization.

## base change and main component

PASS. The smooth completed ring persists under finite DVR extension. Since d(bar t) is nonzero, adjoining its p^a-th root gives the full purely inseparable residue extension of degree p^a. In a one-variable function field over a perfect field this is a Frobenius twist, so its smooth normalization has the same positive genus.

## minimal regular model

PASS. Resolve away from the retained smooth open after the chosen finite base extension. Stacks0CD9 contracts rational exceptional curves to a minimal regular model; 0CDG makes that model semistable once semistable reduction exists. The positive-genus main component cannot be contracted. No exceptional curve contains x, and successive contractions remain isomorphisms near its image.

## actual morphism descent

PASS. Every contracted rational curve maps constantly to the positive-genus smooth special base, including inseparable maps by Luroth. The graph image over each contraction is proper with finite fibres and birational to the normal contracted model, hence finite birational and an isomorphism. Thus the morphism to X descends. Since the original retained fibre above x is a singleton and all operations are away from it, the final fibre is exactly that same singleton.

## horizontal abhankyar only

PASS. The discrete valuation at the generic horizontal branch has residue characteristic zero. The Kummer base change has ramification index e, so Stacks0BRM removes its inertia. This makes the generic pullback cover unramified at that point, without asserting mixed-characteristic surface etaleness. Connected pullback components remain Galois with a subgroup of the original p-group.

## actual semistable cover

PASS. Yang Proposition1.6 extends the actual generic cover over the fixed pointed semistable base after finite coefficient extension. Auxiliary marking can be chosen away from x. Definition1.5 permits nonfinite special fibres; Theorem1.9 applies precisely at the retained nonmarked smooth point.

## domination of old components

PASS. Resolve the actual generic map from a connected pullback component to the old source using point blowups of a regular surface (Stacks0C5H), after resolving nodal surfaces. Proper generically finite surjectivity supplies a component dominating each old B. Every new exceptional component is rational, and no rational curve can dominate positive-genus B even inseparably. Thus a genuine positive-genus component of the new semistable source dominates B and lies over x by the commuting actual maps and singleton base fibre.

## p rank transfer

PASS. Finite maps between smooth component normalizations cannot increase p-rank on the target: purely inseparable maps preserve it; for the separable part, Jacobian norm is surjective, and the rational p-divisible-group exact sequence gives the inequality. Thus the new zero-rank component forces the old component to have zero rank.

## Primary source verification

- https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf — Definition1.5 and Proposition1.6, printed p9; Theorem1.9, printed p11; verified: opened and relevant text read. Retrieval refs: turn1245view0, turn1246view2, turn1246view3, turn1247view2.
- https://stacks.math.columbia.edu/tag/0BRM — Lemma15.116.4, Abhyankar lemma; verified: opened and full statement/proof read. Retrieval refs: turn1245view1.
- https://stacks.math.columbia.edu/tag/0CD9 — Lemma55.8.5; verified: opened and full statement/proof read. Retrieval refs: turn1247view0.
- https://stacks.math.columbia.edu/tag/0CDG — Lemma55.14.5; verified: opened and full statement/proof read. Retrieval refs: turn1247view1.
- https://stacks.math.columbia.edu/tag/0C5H — Lemma54.4.3; verified: opened and full statement/proof read. Retrieval refs: turn1247view3.
- https://stacks.math.columbia.edu/tag/0C5Q — Lemmas54.17.1 and54.17.2; verified: opened and relevant text read. Retrieval refs: turn1247view4.

## Scope and preservation

The important correction is the actual morphism X-prime to X with singleton fibre over x, not only a generic function-field map. The corrected draft proves that property. It uses Abhyankar only at the horizontal characteristic-zero valuation and retains possible vertical ramification. Positive-genus domination is established by an actual proper map after point blowups; the argument makes no arbitrary finite-map extension claim for stable models. No canonical file was changed by this audit.
