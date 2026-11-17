# Final read-only review of Hua comparisons and Brauer–Severi notes

**Scope reviewed:** N11–N29, N44–N71, the opening evidence conventions, and the standing/title registers in `MPL_46_002-048_notes.md`. The review used the frozen page `.tex` files and the previously read full `context/hua_project/46.modern.tex`; no manuscript image was viewed and no main note, transcription, combined file, or JSON file was changed. The following are the concrete corrections needed; unlisted notes require no correction on this review's scope.

## R1 — N58: the retraction proves only one implication

**Kind:** mathematical qualification. **Scans:** 045, 047 (Hua pages 44, 46). **Manuscript quotation:** “ayant d'ailleurs une section canonique”; “est représentable ssi”. **State:** WG2 §1.1 #3; LM1_GROUP_SCHEMES_rerun_20261112 B.8.

The final sentence currently attributes the stated *equivalence* of representability to a “retraction/equalizer route,” but a section only gives the implication SystLin representable ⇒ Pic representable. The opposite implication additionally requires the relative representability of λ, which scan045 asserts with the explicit effectivity warning retained in N59. Hua himself separates these two directions in *Systèmes linéaires paramétrés par un schéma de Brauer–Severi (pages 42 à 48)*, immediately after “D'où (page 46)”. Suggested replacement: “In Hua's formal argument, a section makes Pic a retract of SystLin, proving Pic representable if SystLin is representable; the reverse implication additionally requires λ to be relatively representable, whose effective-descent issue is still flagged on scan045.”

**Confidence:** high: if s is a section of λ, Pic is the equalizer of the idempotent sλ and the identity on SystLin, whereas representability of the total functor from that of the base requires representability of λ. This is a formal check, not a proof that the manuscript's λ is representable.

## R2 — N63: the Picard-boundary identification is explicitly Hua's interpretation

**Kind:** attribution/status correction. **Scan:** 047 (Hua page 46; his discussion also uses unsupplied page48/scan049). **Manuscript quotation:** “ξ … ne provenant pas d'un L”; “relation d'incidence can.” **State:** WG2 §1.1 #3.

N63 is labelled “own idea,” but the last paragraph of Hua's same linear-systems subsection explicitly identifies δ(ξ), up to sign, with the Brauer class of the parameter scheme. Relabel this as an attributed Hua interpretation with a proposed own verification, and credit the identification itself to Hua rather than saying that his interpretation only “motivates the check.” Retain the valid refinement in N56: the general Leray boundary lands first in H²(S,G_m), while the finite-rank Brauer–Severi construction gives the represented class in this particular setting. The cocycle comparison remains unwritten on the supplied leaf and should remain a proof obligation here.

**Suggested opening:** “Hua interprets the assertion as identifying the Picard boundary of ξ with the Brauer class of the finite-rank parameter scheme, up to the sign fixed by duality; a comparison of the actual descent cocycles is the verification still to supply.”

## R3 — N12: credit Hua's exact algebra correction

**Kind:** attribution precision. **Scan:** 006 (Hua page5). **Manuscript quotation:** “u a f(g)=b f(ug)”; “b^{-1}a=f(u)u^{-1}”. **State:** LM1_GROUP_SCHEMES_rerun_20261112 B.8, limited comparison.

The mathematical calculation is correct, but the wording “Hua discusses the twisted-conjugacy setup” understates his direct contribution: his footnote in *Torseurs tordus par un endomorphisme : quand forment-ils une gerbe ? (pages 4 à 6)* states precisely the noncommutative defect and the neutral-object argument preserving the Lang criterion. Replace that clause by “Hua explicitly identifies this noncommutative defect and the neutral-object argument in the cited subsection; the calculation is independently checked here.” Keeping **Kind: own verification** is appropriate once the distinction between credit for the interpretation and verification of its algebra is explicit.

## R4 — N11: remove the unrestricted finiteness description

**Kind:** hypothesis correction. **Scans:** 005–007 (Hua pages4–6). **Manuscript quotation:** “G un faisceau en groupes”; “avec une section marquée (G,f)”. **State:** LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8.

Replace “a finite classical instance” by “a concrete classical instance”: the initial torsor/equalizer construction is made for an arbitrary sheaf of groups, and finiteness is not an assumption there. The marked object supplies a neutralization of the N-torsor gerbe once the stated Lang-map epimorphism/gerbe condition is satisfied; if the title is intended to assert that equivalence unconditionally, add that qualification. This also avoids conflict with N14's correct warning about finiteness in the later smooth-group specialization.

## R5 — §IX: two visible headings are absent from the heading register

**Kind:** inventory omission. **Scans:** 005 and 012. **Source:** frozen page files only; no palaeographic reinspection.

Add scan005, text, **“p|φ-structures en général.”** with the first sign uncertain and visible foliation **4**; add scan012, text, **“Frobéniuseries.”** with visible foliation **11**. Both are standalone underlined headings in the frozen text, unlike an inferred modern subject label. These additions do not change the inventory's face counts or the statement that no explicit total page-count was identified.

## Source locators retained for the corrections

- Hua, M., project. (2026). *46.modern.tex*: *Torseurs tordus par un endomorphisme : quand forment-ils une gerbe ? (pages 4 à 6)*, algebra footnote and marked-object passage; *Systèmes linéaires paramétrés par un schéma de Brauer–Severi (pages 42 à 48)*, empty-system footnote, paragraph beginning “D'où (page 46),” and final Leray paragraph. These are supplied interpretative context, not independently authenticated manuscript witnesses.
- Frozen scans005,006,007,012,045,047, in `MPL_46_002-048_work/pages/`.
- No new web source is required for these corrections. The primary references already retained in `hua_comparison.md` and the main notes continue to support the affineness and Brauer–Severi comparisons.
