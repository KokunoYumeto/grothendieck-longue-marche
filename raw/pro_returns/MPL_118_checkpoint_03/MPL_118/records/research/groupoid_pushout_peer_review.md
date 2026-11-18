# MPL118-C07 — Fundamental groupoids and ordinary categorical pushouts

**Independent check:** GPT-6 Astra Pro, research subagent `/root/residue_new_mapping`; inherited effort is not exposed. Frozen-text and source-based research only; no image reading or transcription change.

## Verdict and manuscript target

The proposed proof is correct. For an ordinary pushout in Cat of \(A\xrightarrow{i}B\) and \(A\xrightarrow{g}A'\), if \(i\) is injective on objects and \(g\) induces an equivalence of fundamental groupoids, then the induced \(B\to B\amalg_AA'\) also induces an equivalence of fundamental groupoids. Thus the expectation in 118/023 holds for both open and closed subcategory inclusions, with no Dwyer or Grothendieck-opfibration hypothesis.

The frozen sentence is: “Il semble vrai pourtant que si \(g\) induit une … \(1\)-équiv., i.e. équiv. sur les groupoïdes fondamentaux, alors \(f\) aussi.” The deletion and final question marks remain in `MPL_118/pages/MPL_118_118_scan023.tex`; this review supplies a justification in the notes, not a replacement reading.

## Argument checked

Use the **object-preserving groupoid completion** \(\Pi C=C[\operatorname{Mor}(C)^{-1}]\), not a skeletal representative. A functor from \(C\) to a groupoid extends uniquely across this localization, so \(\Pi\) is left adjoint to the inclusion \(\mathrm{Gpd}\hookrightarrow\mathrm{Cat}\) and preserves ordinary pushouts. Moreover, \(\operatorname{Ob}(\Pi C)=\operatorname{Ob}(C)\). Consequently

\[
 \Pi(B\amalg_AA')\cong\Pi B\amalg_{\Pi A}\Pi A'
\]

and \(\Pi i\) is injective on objects. It need not be faithful; faithfulness is unnecessary for the following step.

Coyne–Noohi, *Singular Chains on Topological Stacks I*, §8.1, printed pp. 13–14, specify the ordinary model structure on groupoids with equivalences as weak equivalences and object-injective maps as cofibrations; Proposition 8.4 states left properness. Applying that statement to the last pushout, \(\Pi g\) is a weak equivalence and \(\Pi i\) a cofibration, so the induced \(\Pi B\to\Pi(B\amalg_AA')\) is an equivalence. [Primary text](https://webspace.maths.qmul.ac.uk/b.noohi/papers/ChainsStI.pdf).

Finally, groupoid completion is the fundamental groupoid of the nerve restricted to its vertices: generators are edges and the two-simplex relations impose composition. Its equivalences are exactly bijections on connected components and isomorphisms on fundamental groups at all basepoints. This identifies the conclusion with the manuscript’s explicit meaning of “1-équivalence”. No higher homotopy conclusion follows.

## Existing supplied result and credit

This is **not presented as a new theorem**. The supplied companion already states the relevant positive conclusion in `context/companion/chunks/DER_XIIb-a.tex`, comment p114 “The endpoint product is not a cofibration”, final paragraph (line 2346). It says that a pushout along an object-injective functor has the same fundamental groupoid as the cofibred category of the span, and invokes the corresponding consequence for \(W_1\) and localizers containing it; its proof is not reproduced there. The present check verifies the narrower \(W_1\) application to scan 023 by the primary model-category reference.

`context/notes/RESULTS_STATE.md`, line 397, records **POLES H.5**, supplied status **Proved (the return’s claim)**, “The precise boundary for all sieves to be cofibrations”, and refers to **TOTASPH F.25, F.28–F.30**. The selected excerpt truncates its object-injective clause, so this review does not pretend to have read the full original return or revalidate the wider equivalence theorem. The companion’s explicit statement and the primary source suffice for the targeted application.

The companion’s `DER_XIX.tex`, comment p32 “The existence question after Chapter XIX”, also explicitly identifies the fundamental groupoid with groupoid completion and explains why an analogous conclusion fails for full weak homotopy equivalences. That distinction agrees with the two levels of assertion on scan 023.

Recorded 2026-11-18T03:13:31+00:00.
