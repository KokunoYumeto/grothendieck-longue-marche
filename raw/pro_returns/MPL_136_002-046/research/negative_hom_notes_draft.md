# Research draft: homogeneous maps, negative degrees, and divisibility

Prepared from the frozen transcription, after the context was opened. No scan images were consulted by this research worker, and no transcription file was changed. Locators below are **TeX-file lines**, not manuscript line counts. `Hua` means **Hua, modernised reading of cote 136**, `context/hua_project/136.modern.tex`; its page *n* corresponds to archive scan *n*+1. All supplied same-cote notes and unreviewed register claims remain leads rather than independent certification.

## Itemized notes

### NH01 — The factorial calculation supplies the unit needed later

**Kind:** unpursued implication / unproved claim. **Source:** 136/035, TeX lines 3–25; 136/043, lines 5–11. **Cue:** `\nu_p((n+1)!)=` and the final valuation `=0`.

The completed computation on 035 shows why the coefficient of `T_{r+1}` in 043 is `p` times a unit, while the separate `(n+1)!` line remains unfinished and must not be treated as a completed induction. Hua, “Le théorème sur M ⊗_k S” (its p. 34 = scan 035), already makes the link to its p. 42 = scan 043; these pages support that link and add the physical evidence that one attempted calculation was abandoned. This bears on **Hua, findings register, 136-shadow-full-faithfulness**, and **gap g1048** only through the arithmetic used by the graded-module arguments, not as a proof of the latter’s derived or multiplicative assertions.

### NH02 — The shifted adjunction is present, but its next specialization is unfinished

**Kind:** unproved claim / unfinished calculation. **Source:** 136/037, TeX lines 4–27, resumed at 136/039, lines 4–13. **Cue:** `Hom^d(M^*,\varphi_NN^*)` and “Supposons”.

The displayed chain identifies degree-*d* maps into the truncation right adjoint with maps out of `τ_{N-d}M^*`, under the recorded support condition on `N^*`; the subsequent specialization stops with incomplete equalities. Hua, “Homomorphismes homogènes entre tronqués” (pp. 36–38 = scans 037–039), supplies a coherent continuation, while `same_cote_136/MPL_136_235-281_notes.md`, N17 and N22 (scans 244–252, 275), discusses the later explicit adjoints and the nonnegative unit; this is an earlier instance, not an additional proof of their whole categorical construction. It bears on **Hua 136-shadow-full-faithfulness** and the finite-tail part cited within **gap g1048**, whose all-integer-graded and derived versions require separate hypotheses.

### NH03 — The cancelled Cayley fragment is not evidence for a surviving construction

**Kind:** withdrawn in the same text / reading question. **Source:** 136/037, TeX lines 38–59, cancelled lower block. **Cue:** “Diagramme de Cayley”; “Mot … `g_i` + origine”.

The group, generators, arrows and labelled graph belong to a cancelled block, so their presence should be indexed without making them a step in the live truncation proof. Hua, “Homomorphismes homogènes entre tronqués,” footnote to its p. 36 (= scan 037), also calls this a reversed and cancelled Cayley calculation; the present transcription adds its actual surviving labels instead of merely mentioning it. No specific RESULTS_STATE entry directly addresses this cancelled fragment; **WG2 §2.4 #5** supplies only the packet’s planning context, and the fragment establishes neither a connection to the GT or finite-model runs nor a definition of “ombre” or “tubulure”.

### NH04 — The first Hom case corrects a threshold, not merely a sign

**Kind:** withdrawn in the same text / unproved claim. **Source:** 136/039, TeX lines 21–33. **Cue:** deleted `d≥0`, replaced by “Supposons d'abord `d≥β−α`”.

The corrected threshold says that every source degree already maps into the retained target tail; the formula is `mT^(j) ↦ c_{d,j}u(m)T^(d+j)`, not a coefficient-free shift. Hua, “Homomorphismes homogènes entre tronqués,” case (a), restates this correction, and `same_cote_136/MPL_136_235-281_notes.md`, N22 (scans 252, 275), provides the later weighted extension argument rather than permission to remove the binomial coefficient. This supports **Hua 136-shadow-full-faithfulness** at nonnegative degree and bears on **gap g1048** as evidence that recovering maps already retains the weight coefficients.

### NH05 — The intermediate Hom case contains an endpoint discrepancy

**Kind:** reading question / internal mathematical discrepancy. **Source:** 136/041, TeX lines 14–24. **Cue:** the last displayed equation `c_{d,β-d}u=0`, followed by `α≤j<β-d`.

The two written conditions differ by one endpoint, and the strict inequality is the one expressing that output degrees below `β` must vanish. Hua, “Homomorphismes homogènes entre tronqués,” case (b), footnote to its p. 40 (= scan 041), explicitly replaces the final equation by the index `β-d-1`; that is a proposed mathematical correction, while both frozen readings remain intact here. This is a precise qualification to the graded-map interpretation behind **Hua 136-shadow-full-faithfulness**, with no effect by itself on the already claimed finite-tail result cited in **gap g1048**.

### NH06 — A characteristic-two test shows that the endpoint changes the answer

**Kind:** own idea. **Confidence:** high, by direct multiplication in the divided-power ring. **Source:** 136/039, TeX line 32; 136/041, lines 14–24. **Cue:** `mT^(j) ↦ c_{d,j}u(m)T^(d+j)`.

Take `k=M=N=F₂`, `α=1`, `β=3`, `d=1`: multiplication by `T` gives a nonzero degree-one map `τ₁S→τ₃S`, because its degree-one source term maps to `2T^(2)=0`, whereas `T^(2)` maps to `3T^(3)=T^(3)`. The extra endpoint would impose `3u=0` and incorrectly kill this map, so this example independently tests the correction already identified by Hua in “Homomorphismes homogènes entre tronqués” (p. 40 = scan 041). Searches of the four supplied same-cote notes found no copy of this particular example; it adds a concrete diagnostic to **Hua 136-shadow-full-faithfulness** and **gap g1048**, without a novelty claim.

### NH07 — The negative-degree calculation has a sign convention that must be stated

**Kind:** reading question. **Source:** 136/041, TeX lines 27–38; 136/043, lines 23–35; 136/045, lines 30–34. **Cue:** “c) `d<0`”; “un hom de degré `d<p^r`”; `S^(p^s-d)`.

Scan 043 writes a map “de degré d” but places its value in degree `p^s-d`, and 045 states the result for `Hom^{-d}` with `d>0`; a clean reconstruction must therefore rename the positive size of the negative shift instead of silently identifying all occurrences of `d`. Hua, “Homomorphismes homogènes entre tronqués,” case (c), adopts degree `−d`, `0<d<p^r`; its later “Modules gradués : la mise au propre” (p. 298, reported scan 299) returns to the coefficient relation for negative-degree maps. These are contextual clarifications of the scope of **Hua 136-shadow-full-faithfulness**, whose nonnegative unit does not exclude extra negative components; see also `same_cote_136/MPL_136_235-281_notes.md`, N22 (scans 252, 275), and **gap g1048**.

### NH08 — The p-typical basis assertion needs digit bounds

**Kind:** unproved claim / reading question. **Source:** 136/043, TeX lines 13–17. **Cue:** “a comme base” and `Σi_αp^α≥p^r`, “i.e.” some `i_α≠0` for `α≥r`.

The equivalence and basis description require the monomial exponents to be base-*p* digits, `0≤i_α<p`, with finite support; without those bounds, a power of a lower generator can already have weight at least `p^r`. Hua, “Homomorphismes homogènes entre tronqués” (p. 42 = scan 043), uses the p-typical generators but does not spell out this missing qualification, while its “Coefficients binomiaux modulo p” (pp. 19–22 = scans 020–023) supplies the relevant digit framework. This sharpens the arithmetic context of **Hua 136-shadow-full-faithfulness** and the finite-tail component of **gap g1048**, rather than asserting a new theorem about shadows.

### NH09 — The listed relations are necessary but not a complete module presentation

**Kind:** own idea / diagnostic of an unproved claim. **Confidence:** high under the literal S-module presentation interpretation; the explicit kernel element below proves the issue. **Source:** 136/043, TeX lines 19–33. **Cue:** “les relations sont” and “est donné par … avec les relations”.

Over `F₂`, the divided-power algebra has the p-typical presentation `S=F₂[T₀,T₁,…]/(T_i²)`, and retaining only the displayed relations for the tail ideal gives `⊕_{s≥r}S/(T_s)e_s`. The element `T_{r+1}e_r−T_re_{r+1}` is nonzero there but maps to zero in `τ_{2^r}S`, so cross-generator syzygies are missing if the list is asserted to be sufficient. Hua, “Homomorphismes homogènes entre tronqués” (p. 42 = scan 043), repeats the relation list; this diagnostic qualifies that interpretation and **Hua 136-shadow-full-faithfulness** without refuting the negative-degree argument, which only needs the written relations as necessary conditions. No corresponding syzygy diagnostic was found in the supplied same-cote notes; the explicit proof is in the companion appendix, and **gap g1048** remains a separate derived/multiplicative question.

### NH10 — Coherent divisions are stronger than membership in every p-power image

**Kind:** unpursued implication / corrected interpretation credited to Hua. **Source:** 136/045, TeX lines 17–27. **Cue:** `ξ_s=pν'_sξ_{s+1}` and “la partie divisible”.

The written recurrence supplies one compatible infinite chain, not merely a separately chosen root at every finite depth: multiplying `ξ_s` by the accumulated unit factors produces `y_s=py_{s+1}`, whose generated k-submodule is p-divisible. This is the repair already given by **Hua, modernised reading of cote 136**, “Homomorphismes homogènes entre tronqués” (p. 44 = scan 045), and the pages support it more strongly than the intermediate inclusion in `∩_h p^hM` alone. It bears on **Hua 136-shadow-full-faithfulness** by explaining the negative-degree boundary; it does not establish the unrestricted derived reconstruction in **gap g1048**.

### NH11 — The intersection named in the proposition need not be divisible

**Kind:** own idea, explicit witness for a correction already identified by Hua. **Confidence:** high, by a generators-and-relations proof. **Source:** 136/045, TeX line 30. **Cue:** `N₀=∩_{n∈N*}nN`, “plus grand sous-module divisible”.

For a prime p, let `A=⟨x,y_n (n≥1) | px=0, p^ny_n=x⟩`: then `x≠0`, `A/⟨x⟩≅⊕_{n≥1}Z/p^n`, and `∩_{m≥1}mA=⟨x⟩≅Z/p`, which is not divisible. The proof in the appendix supplies a concrete witness for Hua’s already stated correction in “Homomorphismes homogènes entre tronqués” (p. 44 = scan 045), rather than presenting the distinction as a new observation. Searches found no such witness in the supplied same-cote notes; the result qualifies the negative-degree scope surrounding **Hua 136-shadow-full-faithfulness**, and does not rederive the finite-tail theorem referenced by **gap g1048**.

### NH12 — The literal global factorization can be retained with the intersection as target

**Kind:** own idea / proof repair. **Confidence:** high for the explicitly stated coefficient argument in the appendix; no claim that the target is divisible. **Source:** 136/043, TeX line 3; 136/045, lines 30–32. **Cue:** local base “une `Z_p`-algèbre” versus “Soit k un anneau comm.”.

Hua, “Homomorphismes homogènes entre tronqués” (pp. 42–44 = scans 043–045), restricts its corrected divisible-target proposition to a p-local base because that is the calculation written on the page. For arbitrary k, localization at each integer prime nevertheless puts every output coefficient in all integer multiples of the localized target, so testing its class in `N/nN` gives global membership in `N∞=∩_{n≥1}nN` and the written factorization through `N∞⊗_kS`. This adds a route from the local calculation to the proposition’s literal intersection target, while leaving the stronger replacement by the global maximal divisible submodule unasserted. It bears on **Hua 136-shadow-full-faithfulness** and the coefficient-category cautions of **gap g1048**; it is not supplied by, or a reproof of, the latter’s settled finite-tail statements.

### NH13 — Independence of the truncation bound follows from the earlier support argument

**Kind:** unproved claim / proof route. **Source:** 136/045, TeX line 30, compared with 136/037, lines 4–16. **Cue:** “indépendant … du choix de α”.

For a map of degree `−d`, the condition `α≥d` ensures that every output degree is nonnegative, so the nonnegative unit for `N⊗S` can be used in the shifted adjunction of 037. Choosing a common target cutoff `β` with `β+d` beyond two source cutoffs identifies both Hom groups with the same maps from `τ_{β+d}M_S` to `τ_βN_S`, giving the stated canonical independence. Hua’s “Homomorphismes homogènes entre tronqués” (pp. 36–44 = scans 037–045) contains the ingredients, while `same_cote_136/MPL_136_235-281_notes.md`, N22 (scans 252, 275), records the nonnegative-unit scope; this is a link between those ingredients under **Hua 136-shadow-full-faithfulness**, not a new claim about **gap g1048**’s infinite quotient.

### NH14 — The torsion-base corollary has a direct bounded-exponent reason

**Kind:** unpursued implication. **Source:** 136/045, TeX line 34. **Cue:** “Si `N₀=0`, p. ex. k de torsion”.

For a unital torsion ring k, its unit has some finite additive order e, hence `eN=0` for every k-module and `∩_{n≥1}nN=0`; the displayed negative-Hom vanishing then follows from the literal intersection-target factorization. Hua, “Homomorphismes homogènes entre tronqués” (p. 44 = scan 045), retains the torsion-base corollary after changing the target to a divisible submodule; the elementary exponent observation shows why the corollary itself survives the target distinction. This supplies an arithmetic boundary case for **Hua 136-shadow-full-faithfulness** and should not be mistaken for a positive solution of **follow-ups @305**’s integral homotopy question.

### NH15 — One claim in Hua’s footnote conflicts with the frozen reading

**Kind:** reading question. **Source:** 136/045, TeX lines 30–32. **Cue:** `Hom^{-d}(τ_αM_{S_k},N_{S_k})` compared with `Hom^{-d}(τ_αM_{S_k},N_{0S_k})`.

Hua, “Homomorphismes homogènes entre tronqués,” footnote (iii) to its p. 44 (= scan 045), says that the two members of the isomorphism are identical on the page. The independently frozen transcription instead distinguishes `N_{S_k}` and `N_{0S_k}`, so that proposed textual defect is not confirmed here and must not be imported into the transcript. This qualifies the use of Hua’s interpretation alongside **Hua 136-shadow-full-faithfulness**; the substantive intersection/divisibility defect in NH10–NH12 is independent of this reading disagreement.

## Standing-question contribution

No new explicit phrase such as “à vérifier”, “sauf erreur”, “je présume”, or “admis” occurs in the live prose of these six frozen pages. The incomplete equalities on 035 and 037, the unfinished negative-degree chain on 041, and the corrected/deleted threshold on 039 are recorded above as unfinished arguments or withdrawals, not relabelled as explicit authorial uncertainty; `\unsure` marks are editorial doubt and are not Grothendieck’s own question marks. The isolated uncertain superscript following `N₀` on 045 is a reading question, not a secure self-flag.

The leaves carry lower marginal numbers 34, 36, 38, 40, 42, 44 at scans 035, 037, 039, 041, 043, 045 respectively. “Diagramme de Cayley” occurs in the cancelled block of 037; there is no new title sheet or explicit page-count statement in this subset. Root is responsible for collating these with the other pages’ pagination and the reused typed leaves.

## Context-search record

`negative_hom_searches.json` records a separate search query for every NH item, all supplied textual context files searched, matching line counts and short locators, and source SHA-256 hashes. A no-hit result is restricted to this supplied corpus; no inaccessible earlier proof, Lean file, or source mentioned by a context note was treated as if it had been inspected. Mathematical diagnostics above use elementary calculations from the displayed formulas, not claims imported from an external literature search.
