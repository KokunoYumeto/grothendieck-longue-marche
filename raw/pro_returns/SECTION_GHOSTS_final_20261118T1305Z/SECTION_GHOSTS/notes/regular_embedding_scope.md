# Regular-prime embedding theorems and the retained matching problem

The dedicated manuscript source is `sections/part_P_regular_embedding_scope.tex`, P.15. It was written after the full independent review of E.209–E.210. The new assertion is a precise scope comparison and a nonzero finite approximation obstruction; no ordinary point-section discrepancy is claimed to realize that obstruction.

## Decisive conclusions

1. The regular-prime projective source in P.4 is the Galois group of the maximal pro-five extension of Q(zeta5) unramified outside five, extended by the order-four cyclotomic quotient. The action factors through it, but an ordinary pair with a nonzero integer valuation at any q other than five does not: its integral Kummer inertia value is nonzero. Finite divisibility of that integer never makes it zero in Z5. Thus projectivity over that quotient does not solve the actual ramified graph problem.
2. Schmidt's Theorem1.1 realizes the old local groups as a free product in a relative kernel. The quotient field in that assertion makes those old places split completely. Extending a map from the kernel still requires equivariance under the outer arithmetic quotient; the theorem does not prescribe new auxiliary inertia to be a named tripod peripheral power. This recovers the relative-kernel limitation already observed by the root agent, now placed next to the exact E.209 comparison.
3. Jarden–Ramiharimanana's TheoremA requires the order of the kernel to be coprime to the number of roots of unity in the finite quotient's field. A quotient retaining the fifth cyclotomic character already contains Q(zeta5), so a five-primary kernel fails that hypothesis. The theorem has genuine finite local approximation when its hypotheses hold; this failure is in the intended arithmetic input, not in the theorem.
4. Liu's restricted-ramification local-global principle has a different cohomological hypothesis from E.209. The literal obstruction is B^(S union T)_(S minus T)(Q,A). Its nonvanishing is possible at a regular prime. For A=F5(3), S={5,infinity}, T={11,31}, the exact dual is the kernel of H1(G_Q,{5,11,31,infinity},F5(2)) -> H1(Q5,F5(2)). The source has dimension2 by the finite residue sequence, the target has dimension1 by local duality and Euler characteristic, and the kernel is nonzero. The real term is zero; there is no local-zero requirement at11 or31; the outside terms are unramified conditions. All these conventions were checked against Liu's definition.

In particular the fourth conclusion does not assert inconsistency of the E.202 matrix, exclude an ordinary pair, or rule out the more specialized discrepancies in B.26. It demonstrates why replacing the matching condition by regular-prime H2 vanishing would be invalid.

## Primary sources opened and exact locators

### Schmidt

English author version, dated16January2009: https://www.mathi.uni-heidelberg.de/~schmidt/papers/marked.pdf. Opened Theorem1.1 and Remarks1.2, authorp2; Proposition7.1 and its free-product proof, authorpp19–20. Relevant live refs: `turn897655766view0`, `turn988866228view1`, `turn541457814view3`. The free product maps to Gal(L/L0), where L=k_(S union S0)^T(p) and L0=k_(S0)^(S union T)(p). It is not asserted to decompose the entire Gal(L/k) as a free product.

Author metadata https://www.mathi.uni-heidelberg.de/~schmidt/papers/schmidt32-en.html was independently opened (`turn541457814view2`). It identifies the published German version in *Journal für die reine und angewandte Mathematik*640(2010),203–235. The existing verified key `RootSchmidt2010` is reused. The German author PDF was also opened at https://www.mathi.uni-heidelberg.de/~schmidt/papers/markiert.de.pdf (`turn850311506view3`); no different theorem scope was inferred from the translation.

### Jarden and Ramiharimanana

Primary author version, dated13June2018: https://www.math.tau.ac.il/~jarden/Articles/paper111.pdf. TheoremA, authorpp3–4, read in full, including finite local set, kernel-conjugacy and the roots-of-unity condition. The preceding comparison with Neukirch and following special cases were also read. Live refs: `turn472273308view0`, `turn477178565view0`, `turn477178565view4`.

Publisher DOI page https://doi.org/10.1112/plms.12126 (`turn897655766search0`) verifies *Proceedings of the London Mathematical Society*117(1)(2018),149–191, first published3April2018. New verified key: `LitJardenRamiharimanana2018` in `literature_matching_references.bib`.

### Liu

Primary author version: https://arxiv.org/pdf/2212.09888, v1 dated19December2022. Opened the notation for the restricted product and dual module; Definition3.1 and Lemma3.2 with proof, authorpp8–9; Lemmas3.4–3.5, authorpp9–10; Lemmas3.6–3.7 with proof, authorpp11–12; Theorem4.1 and Remark4.2, authorp13. Live refs: `turn472273308view1`, `turn988866228view0`, `turn850311506view0`, `turn850311506view1`. The definition and annihilator calculation are retained explicitly in P.15 rather than invoking the phrase local-global principle alone.

Publisher page https://academic.oup.com/imrn/article-abstract/2024/6/5274/7313682 (`turn897655766search1`) and author research page https://sites.google.com/view/yuanliu-homepage/research (`turn541457814view1`) independently verify *International Mathematics Research Notices*2024(6),5274–5325, DOI10.1093/imrn/rnad234. The opened proof locators are from the author version, not an independently opened final publisher PDF. New verified key: `LitLiu2024`.

### Duality and the integral comparison

Milne's https://www.jmilne.org/math/Books/ADTnot.pdf was independently reopened at I.2.6, printedpp30–31 (`turn776469091view0`). The theorem gives the exact annihilator of unramified cohomology for finite unramified modules of order prime to the residue characteristic; those hypotheses hold at every prime outside{5,11,31,infinity}. I.2.3 and I.2.8, pp28 and31, were independently reopened in the E.209–E.210 review. The finite supports sequence and all-weight vanishing used in P.15 are the in-run E.202/E.209 inputs, with their precise finite-coefficient scope retained.

### Additional Riemann-existence check

Kay Wingberg's primary preliminary version,6December2007, https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Riemann-kpi1.pdf was opened. Proposition1.4, authorpp8–9; Theorem2.4, pp13–15; Corollary2.6 and the remarks, pp15–16, retain the relative field and decomposition action in their free products. In the wild case the inertia free product occurs over k_S(p), not over k. Live refs: `turn897655766view1`, `turn472273308view4`, `turn850311506view2`. No publication metadata for this preliminary version was established in this search, so no journal status or separate literature theorem is asserted from it in P.15.

## Searches and unsuccessful retrieval

Search terms included `Schmidt arithmetic Riemann existence theorem pro p free product local extensions primes`, `p rational number field regular prime prescribed local embedding problems ramification free pro p Galois`, `Solving embedding problems with bounded ramification`, and `p-rank of class groups embedding restricted ramification Liu local global principle`. A second search engine verified primary coverage and publication metadata. The author pages, not aggregation sites, supplied the mathematical statements.

A direct filesystem download attempt stalled and was interrupted; no mathematical claim depends on an uninspected local PDF. The web-opened primary texts above were read directly. Temporary downloads, if any, are under `build/regular_matching`, which is excluded from the deliverable checkpoint. No rendered review image was placed in notes.

An additional targeted check opened Liu's *The Realizability Problem with Inertia Conditions*, https://arxiv.org/pdf/1705.03184, v1 dated9May2017 (`turn397906310view1`), including Question1.1/Definition2.1 and Theorem1.3, authorpp1–3. Its named inertia problem prescribes one subgroup at one rational prime; the odd-order case globalizes a local realization. It does not retain the cyclotomic semidirect quotient or prescribe every new ramified inertia and all earlier point-section paths. The abstract record (`turn397906310view0`) and the author's research page identify it as part of the thesis work; no journal publication was verified. No result from that preprint is used as a premise in P.15.

## Review state

Owner full proof/source read is complete. Root completed a full proof read and independently reopened Schmidt Theorem1.1/Proposition7.1, Jarden--Ramiharimanana TheoremA, and Liu Definition3.1/Lemmas3.2/3.7 with full proof. The review is positive; its requested explicit definition of P, pro-p category and missing phi backslash were supplied. The root review is recorded in `literature_matching_check_events.tsv`.

The cohomology agent subsequently completed a positive targeted review of the finite B calculation. That review independently opened Liu arXiv2212.09888v1 Definition3.1/Lemma3.2, authorpp8–9, and Milne ADT I2.6, p30. It checked the exact dual local conditions, the global dimension2 and local dimension1, the real term, and the legitimate G_S^T-module condition. It explicitly did not re-review every Schmidt/Jarden comparison and did not infer an ordinary point-discrepancy counterexample. This scoped completed review is recorded in `literature_matching_check_events.tsv`. P.15 has been integrated by the root agent.
