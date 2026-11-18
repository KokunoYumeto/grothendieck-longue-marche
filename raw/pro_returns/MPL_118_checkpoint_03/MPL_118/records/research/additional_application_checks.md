# Additional application checks: MPL118-C13 and MPL118-C14

**Reviewer:** /root/bisite_mapping; GPT-6 Astra Pro; reasoning effort inherited and not exposed.  
**Scope:** Targeted mathematical checks of the frozen text of scans 019 and 039–040; no image inspection, transcription changes, or wider contextual proof audit.

| ID | Verdict | Essential qualification |
|---|---|---|
| MPL118-C13 | Valid under the actual nonempty-infimum/minimum-stage hypotheses | A nonempty small index poset then has a least element. Mere connectedness of a general index poset is insufficient. |
| MPL118-C14 | Valid for a Grothendieck opfibration with the stated open-part isomorphism | Opcartesian lifts give the cross-Hom bijection and the ordinary pushout universal property; a splitting is unnecessary. |

## MPL118-C13 — The aspherical-stage corollary

**Frozen evidence.** Scan 039 requires that in I, the infima `\inserted{(des parties non vides)}` exist, and states that each object's membership set I(x) has a least element. Scan 040 asks:

> `Si les $X_i$ sont \inserted{$\underline W$-}asphériques et $I$ connexe, alors $X$ est $\underline W$-asphérique`

The following application uses the written strong indexing assumptions and the filtration comparison already reviewed as C03. It does not replace those assumptions with connectedness alone.

### Why the point comparison satisfies the hypotheses

Suppose I is small and nonempty and every nonempty subset has an infimum. The subset consisting of all of I is an admissible nonempty subset. Thus

\[
0_I=\inf(I)
\]

exists and satisfies 0_I≤i for every i∈I. It is the least element, hence an initial object of the index category. In particular I is connected; connectedness adds no condition here.

Give the one-object category e the constant filtration Y_i=e for every i. This filtration covers e and preserves every nonempty infimum, because every corresponding intersection is e. Its unique object's membership set is all of I and has minimum 0_I. Equivalently, the constant stage map e→I with value 0_I has inverse image e over every principal lower set I/i. Each Y_i is both an open and a closed full subcategory of e.

The unique functor f:X→e respects these filtrations. Its stage restrictions are exactly X_i→e, which belong to W by the assumed W-asphericity of the X_i. C03 therefore applies to f and gives X→e∈W. This verifies the marginal corollary under the actual hypotheses; it does not resolve or alter the uncertain notation following “On prend Y_i=…” in the transcription.

### Boundary under weaker indexing assumptions

If only a connected index and minimum stages for the objects of X are retained, the conclusion can fail. Let I be the poset of nonempty proper faces of a triangle: its three vertices and three edges, ordered by incidence. Set X=I and X_i=I/i, the full principal lower set. These are increasing full sieves, cover X, and give each object x minimum stage x. Every X_i has terminal object i, so every stage is W∞-aspherical.

Nevertheless NI is a six-cycle: it has six vertices, six nondegenerate edges, and no higher nondegenerate simplices. Thus X has the homotopy type of S¹ and is not W∞-aspherical, although I is connected. This I lacks the required nonempty infima, and the constant point filtration has no minimum stage. Therefore the example does not contradict C03 or the application above.

For more general indexing, a suitable replacement condition is W-asphericity of I together with a stage map whose comma categories are the X_i: Theorem A then places X→I in W, and composition gives X→e∈W. The word “connected” by itself does not supply this stronger condition. Requiring only some or only finite infima also does not justify the least-element argument as written; any conclusion in that weaker setting needs its own argument.

**Prior-work credit and context.** This is an application check of the filtration material already treated in the supplied Hua modernized reading, “Filtrations (pages 38 et 39),” as identified by the root's context audit. It uses the separately reviewed C03 repair and makes no new claim about the general filtration theorem. The related contextual location is `context/companion/chunks/DER_XVI.tex`, Chapter XVI §1, relative Loc (3 bis), manuscript pp.3–8.

## MPL118-C14 — Ordinary pushout along a closed piece

**Frozen evidence.** Scan 019 fixes a full closed subcategory Y′⊂X′, its open complement U′, the inverse images Y=f⁻¹(Y′) and U=f⁻¹(U′), and an isomorphism U→U′. It asks:

> `\uline{Mais} supposons que $f$ soit cofibré, le carré est-il cocartésien ?`

The proposed test is the cross-Hom colimit, and the written proof stops after `Surjectif` and the beginning of the fixed-arrow discussion. Here “cofibré” is read as the requested Grothendieck opfibration assumption.

### Cross-Hom normal form from opcartesian lifts

Fix u′∈U′ and its unique corresponding u∈U. Let g:Y→Y′ be the restriction of f. For y′∈Y′, consider

\[
\theta:\operatorname*{colim}_{(y,\beta)\in g/y'}
\operatorname{Hom}_X(u,y)
\longrightarrow \operatorname{Hom}_{X'}(u',y'),
\qquad [\alpha,\beta]\longmapsto\beta f(\alpha).
\]

An object of g/y′ is a pair y∈Y and β:f(y)→y′. Its morphisms act on the displayed Hom sets by postcomposition. This is the ordinary set colimit in the manuscript's formula.

For any ξ:u′→y′, choose an opcartesian lift λ_ξ:u→t with f(t)=y′. Then t∈Y and [λ_ξ,id] maps to ξ, giving surjectivity.

Now take any representative [α:u→y, β:f(y)→y′] mapping to ξ. Lift β opcartesianly from y to obtain h:y→z over β. Since f(z)=y′, both y and z lie in Y. The morphism (y,β)→(z,id) in g/y′ identifies [α,β] with [hα,id]. Because hα lies over ξ, the opcartesian property of λ_ξ supplies a unique vertical k:t→z with

\[
f(k)=\mathrm{id}_{y'},\qquad k\lambda_\xi=h\alpha.
\]

The corresponding vertical morphism in g/y′ then identifies [hα,id] with [λ_ξ,id]. Every representative mapping to ξ is therefore the same colimit element. This proves injectivity as well as surjectivity. No coherent choice of lifts and no split opfibration are needed.

### The ordinary universal property

Because Y′ is a full cosieve, U′ is a full sieve and there are no arrows from Y′ to U′. The same holds for Y and U. Thus X′ is determined by its two full pieces and the sets of crossing arrows from U′ to Y′. The open piece U′ is already identified with U; the other piece is Y′. The bijection θ says exactly that the crossing arrows are freely obtained from those of X followed by arrows in Y′, subject to the identifications already imposed by Y.

Explicitly, let a:X→Z and b:Y′→Z agree on Y, so a|Y=b g. On U′, define the extension by a through U≅U′, and on Y′ use b. A crossing arrow represented by [α,β] is sent to b(β)a(α). The defining colimit relations hold because a|Y=b g, and the bijection θ makes this assignment well-defined for every crossing arrow. Composition is respected by postcomposition in Y′ and precomposition in U′, the same operations used in the Hom diagram. There are no compositions crossing back from Y′ into U′. The resulting functor extends both a and b and is unique, because the two pieces and these crossing representatives exhaust all objects and arrows of X′.

Hence the canonical map from the ordinary categorical pushout is an isomorphism:

\[
X\amalg_Y Y'\ \cong\ X'.
\]

This proves the ordinary pushout assertion. It is separate from any homotopy-pushout or weak-equivalence-preservation claim and does not use the following paragraph's proposed description by a strict functor X′→Cat.

### Why the opfibration condition matters

Without it, take X′=[1], U′={0}, Y′={1}, and X=U={0} with f the inclusion. Then Y=∅ and U→U′ is an isomorphism, but X⊔_Y Y′ is the discrete two-object category, not [1]. The missing crossing arrow 0→1 has no lift from X. This also confirms the elementary negative case preceding the positive question in scan 019.

**Prior-work credit and context.** Credit belongs to the supplied Hua discussion of cofibred open–closed gluing and to the already established contextual overlap: `context/companion/chunks/DER_XIIb-a.tex`, Chapter XII §V.1.1, manuscript pp.59–60, Proposition 1, describes the crossing-Hom/profunctor data; `context/companion/chunks/DER_XIIb-b.tex`, Chapter XII §V, manuscript pp.147–149, discusses the related gluing statement and the cartesian/aspherical-fibre alternative. This check completes only the ordinary cross-Hom argument on scan 019 and does not re-audit those broader contextual results.

## Event scope

The event file records four actual application checks: the strong-hypothesis proof of C13, its connected-index boundary counterexample, the nonsplit-opfibration proof of C14, and its no-lift boundary counterexample. No event claims that a source register or a whole contextual theorem was independently proved.

**Recorded:** 2026-11-18T03:18:28+00:00.  
**Frozen combined SHA-256, unchanged:** `63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149`.
