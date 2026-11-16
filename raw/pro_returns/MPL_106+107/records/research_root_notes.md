# MPL_106+107 — research notes

## Scope, evidence, and reading conventions

These notes were written after the transcription was frozen at **2026-11-16 13:43:19 UTC**. The 41 scans were transcribed and visually audited by the principal reader in one stream, without OCR or transcription subagents; the subsequent parallel work concerned only research comparisons against the frozen text. No contextual or mathematical correction has been put back into the transcription.

`106/012` means archive cote 106, PDF scan 12, not manuscript page 12. Manuscript numbers are given separately where useful. Quotations preserve the frozen reading; a quotation containing `\unsure{…}` remains uncertain, and a mathematical reconstruction in these notes is not a replacement reading.

The evidence has four distinct levels: (1) the personally inspected scans and frozen diplomatic transcription; (2) the manuscript-text layer reproduced in the supplied *Les Dérivateurs* companion and *Pursuing Stacks* files, whose underlying scans were not newly inspected here; (3) the companion's interleaved `dcomment`/editorial material and earlier AI research returns; and (4) independently checked arguments or external primary literature. A supplied status such as **Proved**, **Known**, or **Refuted** is the return's claim unless its entry explicitly records an intake or review; these notes do not turn those statuses into independent verifications.

The contextual comparisons below use `context/notes/RESULTS_STATE.md` (abbreviated **RS**), `context/NEW_RESULTS.md`, and `context/DOSSIER_STATEMENTS_WITH_STATUS.md`. The latter has **255 statements**: 10 STRATA, 76 PATHS, 113 BISITE, and 56 RESIDUE; the complete concordance is included below, together with all 12 numbered NEW_RESULTS entries and its three trailing “known after all” notices. Exact source statements and statuses are retained in the concordance, so an absent result is not silently omitted.

The context-search records identify queries, files, and manuscript-page markers. Search locators in a companion file are textual locators, not new scan attestations. No historical priority or date of composition is inferred from a chapter number, an archive cote, a recycled computer listing, or the planning README.

## A. Cote 106: replacement, short fractions, and the unresolved section criterion

### C106-01 — The opening replacement theorem and the axiom boundary

**Location / kind:** 106/002, opening paragraph; unproved claim. **Context search:** CF-AXIOMS and CF-REPLACEMENT; `context/companion/chunks/DER_VI-b.tex`, ms.108–110, Théorème-Scholie 2(I); `context/ps_chapters_VI_VII/ps6.tex`, §125, pp.530–532. **RS:** Hua, findings register, **106-section-criterion-span-faithfulness**, conjecture candidate, intake “new to us”; no selected RS entry separately identifies the exact C1–C3 system.

The opening says “il est connu que” the localization of the cofibrant objects is equivalent to the localization of all objects, and then attempts to construct a quasi-inverse. The analogous fibrant-replacement assertion in VI ms.108–110 is a contextual counterpart, not an identification of hypotheses; the present leaf adds a concrete cofibrant, weak-lifting construction. Rădulescu-Banu (2009, Theorem 6.1.6) supplies a standard precise replacement theorem, but applying it literally requires spelling out the manuscript's abbreviated axioms.

### C106-02 — Independence of the lifted arrow is initially conditional

**Location / kind:** 106/002, after the first weak-lifting diagrams; self-flagged. **Context search:** CF-CANCELLATION and CF-REPLACEMENT; `DER_VI-b.tex`, ms.108–110, especially the distinction between a functorial replacement and one constructed after localization. **RS:** bears on Hua **106-section-criterion-span-faithfulness**, with the same unreviewed candidate status.

After “Je dis qu'il ne dépend pas du choix”, the argument reduces to cancellation of a weak equivalence on two maps between cofibrant objects and explicitly continues “Si ce lemme est valable”. This is a condition on the proposed quasi-inverse, rather than a proof of the cancellation lemma. The context has the dual replacement problem; these pages add the precise cancellation bottleneck and later formulate it as a criterion at 106/006.

### C106-03 — Identity and composition compatibility is asserted before that bottleneck is discharged

**Location / kind:** 106/002, last paragraph, and 106/004, upper diagrams; unproved claim. **Context search:** CF-COMPOSITION and CF-REPLACEMENT; `DER_VII-b.tex`, ms.77–82, path composition, and `DER_VI-b.tex`, ms.108–110. **RS:** related Hua **106-section-criterion-span-faithfulness**; **CATHOT E.26**, Open (return's claim), `CATHOT_results.csv`, VII ms.108–123, concerns a different later comparison.

The sentence “la compatibilité … aux identités et aux compositions est immédiate” presupposes the choice independence just isolated. The diagrams on 106/004 exhibit how two successive lifts are to be compared, but no independent proof of the opening cancellation lemma is supplied there. This is a limited precursor to the all-type path-composition discussion in VII, not a settlement of CATHOT E.26.

### C106-04 — The naturality check is flagged and then actually carried out

**Location / kind:** 106/004, lower half; self-flagged, resolved locally. **Context search:** CF-REPLACEMENT and CF-CANCELLATION; `DER_VI-b.tex`, ms.109–110, the naturality of replacement maps after localization. **RS:** related Hua **106-section-criterion-span-faithfulness**; no new selected RS theorem is proved.

The manuscript says “il faut vérifier que c'est fonctoriel” for the comparison from ΨΦ to the canonical localization functor and immediately computes the required equality using α_y = β_f i_f. Its “cqfd” closes this naturality calculation conditional on the already defined Φ; it does not close the earlier choice-independence question. The context restates the same formal role of natural replacement maps in the dual situation.

### C106-05 — The opening theorem is recast as a cancellation criterion

**Location / kind:** 106/002 and 106/006, “En résumé”; withdrawn in the same text / reformulation. **Context search:** CF-CANCELLATION and CF-REPLACEMENT; `DER_VI-b.tex`, ms.108–110. **RS:** Hua **106-section-criterion-span-faithfulness** is related but concerns the later, different section criterion.

The initial “il est connu” statement at 106/002 is followed at 106/006 by “il f. et s.” and the explicit cancellation condition for Ψ to be an equivalence. This is a change in the status of the attempted proof, not an explicit denial of the standard replacement theorem. The cancellation criterion for the inclusion of cofibrant objects must not be conflated with the section-independence criterion for short fractions at 106/016.

### C106-06 — Restriction to cofibrant objects and pushouts

**Location / kind:** 106/006, bracketed NB; unproved claim. **Context search:** CF-AXIOMS and CF-COUNIVERSAL; `DER_VI-b.tex`, ms.108–110, for the dual restriction, and `ps6.tex`, §125, pp.530–532, for the need for pushouts in a cofibration structure. **RS:** Hua **106-section-criterion-span-faithfulness**, unreviewed candidate; thematic only to **PATHS D.22**, Open, `PATHS_results.csv`, intrinsic cofibrations without an initial object.

The NB says that the induced structure on C_cof again satisfies the abbreviated axioms and that the inclusion preserves the pushouts whose existence is postulated. Under the standard cofibration-category axioms this is the expected closure argument, but the manuscript does not enumerate it. These leaves explicitly assume an initial object at 106/002, so they do not answer the “without initial object” part of PATHS D.22.

### C106-07 — Passing from pushout composition to a category of components

**Location / kind:** 106/006–008; unproved claim. **Context search:** CF-COMPOSITION; `DER_VII-b.tex`, §7, ms.59–82, especially ms.77–82. **RS:** dossier **PATHS A.P1**, supplied Proved claim but not itself selected in RS; related **CATHOT E.26**, Open, VII ms.108–123.

Pushout composition is declared “associative à iso can. près”, and the induced composition on π₀ is declared “associative (str. !)”. The canonical associativity and unit isomorphisms are sufficient at the component level, provided the stated pushouts and comparison morphisms remain inside the roof categories. VII develops the more general all-type path formalism; this packet gives a short-roof version and no full mapping-space comparison.

### C106-08 — Couniversal weak equivalences are proposed as a broader input

**Location / kind:** 106/008, paragraph beginning “Pour l'instant”; unpursued implication. **Context search:** CF-COUNIVERSAL; `DER_XIIb-a.tex`, ms.111–115, the later couniversal/cofibration questions; `ps6.tex`, §125, pp.532–533, the programme based on W alone. **RS:** **TOTASPH F.27**, Open (return's claim), `TOTASPH_results.csv`, XII ms.111–114; **POLES H.5**, Proved (return's claim), `POLES_results.csv`, boundary for all sieves to be cofibrations.

The manuscript suggests retaining the construction when the chosen denominators are couniversal weak equivalences, without insisting that cof = cof_W. This addresses the stability needed to compose the particular roofs, not recognition of every couniversal morphism or closure of dwyerienne sieves under composition. It therefore adds a methodological link to the later open questions without settling them.

### C106-09 — The proposed inverse is obstructed by the cofibration condition

**Location / kind:** 106/008, inverse-search diagrams, and 106/010, first half; withdrawn in the same text. **Context search:** CF-CANCELLATION and CF-COUNIVERSAL; `DER_VII-b.tex`, ms.65–73, inversion of denominators using arbitrary-length paths. **RS:** Hua **106-section-criterion-span-faithfulness**; dossier **PATHS A.P1** (Proved claim, not selected in RS).

The inverse sought through “g?” and “i?” at 106/008 is announced at 106/010 as “l'inverse cherché”, then its proposed connecting diagram is rejected because αi = f need not be a cofibration. The proposed repair βf is also rejected: if cofibrations are monomorphisms and f is not monic, postcomposition cannot make βf monic. This refutes that particular repair, not the possibility of a different zigzag in the roof category or the standard short-fraction theorem.

### C106-10 — Surjectivity is proved separately from faithfulness

**Location / kind:** 106/010, final paragraph; unpursued implication. **Context search:** CF-CANCELLATION and CF-COMPOSITION; `DER_VII-b.tex`, ms.68–73, localization by effects of paths. **RS:** dossier **PATHS A.P1** (Proved claim, not selected); related **CATHOT E.26**, Open, concerns stronger comparisons.

The calculation concluding “OK” shows that the roof (g,i) has image [f]⁻¹ in the localization, and hence establishes the claimed surjectivity on localized arrows using composition. It does not show that this roof is already an inverse inside the component category. The explicit separation between fullness and faithfulness is the useful contribution of these pages to the later path-localization comparison.

### C106-11 — Faithfulness remains explicitly open at the point of revision

**Location / kind:** 106/012, first paragraph; self-flagged. **Context search:** CF-CANCELLATION; `DER_VII-b.tex`, ms.68–73 and ms.82, ordinary localization versus later diagram-category comparisons. **RS:** Hua **106-section-criterion-span-faithfulness**, conjecture candidate; related **CATHOT E.26**, Open, `CATHOT_results.csv`.

“Il n'est pas clair” refers specifically to faithfulness of the component-roof comparison, after bijectivity on objects and surjectivity on arrows. The manuscript relates it to inverting all of W in the roof construction, then changes the definition of that construction. It is therefore inaccurate to read the earlier surjectivity argument as a proof of full faithfulness or of a higher path-space theorem.

### C106-12 — The conjectured weakness of inverting only acyclic cofibrations

**Location / kind:** 106/012, middle; conjecture / expressed doubt. **Context search:** CF-COUNIVERSAL and CF-AXIOMS; `DER_VI-b.tex`, ms.109–112, fine versus coarse localizations, and `ps6.tex`, §125, pp.530–533. **RS:** Hua **106-section-criterion-span-faithfulness**, unreviewed candidate; no exact selected RS statement settles this local question.

The text first says “semble-t-il” about W₀⁻¹C → W⁻¹C and then “Mais je doute” that inverting weak cofibrations suffices. The W₀ in this leaf is W ∩ cof; the fine localizer W₀ in VI has a different definition and must not be identified by notation alone. Under explicit standard cofibration hypotheses the doubt has an elementary positive resolution, recorded separately below as our argument.

### C106-13 — Two definitions of Ch₀ and C̃ must remain separate

**Location / kind:** 106/006 and 106/012; withdrawn in the same text / changed definition. **Context search:** CF-COMPOSITION and CF-AXIOMS; `DER_VII-b.tex`, ms.65–73, allowed backwards arrows; Horel (2016, Introduction). **RS:** Hua **106-section-criterion-span-faithfulness**, candidate; dossier **PATHS A.P1**, Proved claim, not selected in RS.

“Je rectifie donc le tir” replaces roofs with arbitrary forward arrow and backwards acyclic cofibration by roofs whose forward arrow is a cofibration and whose backwards arrow is merely in W. The same symbols Ch₀ and C̃ are reused, so conclusions before and after 106/012 require a comparison and cannot be transferred by notation alone. The standard short-roof literature is a relevant comparison, but the equivalence of these two component presentations is additional reasoning, supplied with explicit hypotheses in the literature-review notes below.

### C106-14 — A cancelled direct inversion argument precedes the harder construction

**Location / kind:** 106/014, upper deleted block and following paragraph; withdrawn in the same text. **Context search:** CF-SECTION and CF-COMPOSITION; `DER_VII-b.tex`, ms.68–73. **RS:** Hua **106-section-criterion-span-faithfulness**, candidate.

The crossed-out claim that the first functor already inverts W is replaced on the same leaf by “qui va être un peu plus délicat” and a factorization-based definition of C → C̃. The deleted calculation remains evidence of an attempted route, not a completed proof. The contextual all-path localization avoids imposing the same short-roof shape, and therefore does not retrospectively validate this deleted argument.

### C106-15 — Choice independence is the outstanding construction problem

**Location / kind:** 106/014, middle and lower paragraphs; self-flagged. **Context search:** CF-SECTION and CF-CANCELLATION; `DER_VI-b.tex`, ms.109–110, ad hoc construction after localization; `DER_VII-b.tex`, ms.82, anticipated comparison theorems. **RS:** Hua **106-section-criterion-span-faithfulness**, candidate.

For the roof obtained by factorization and weak lifting, the text says “il faut montrer que ça ne dépend pas des choix faits” and then “il faut voir qu'ils sont dans une = composante connexe”. A common third factorization is proposed at 106/014 and constructed at 106/016; the remaining issue is independence of the chosen section for one factorization. These leaves thus sharpen the problem rather than merely repeating the earlier general faithfulness question.

### C106-16 — The common refinement and its retained section

**Location / kind:** 106/016, first diagram and following paragraph; unproved claim with construction. **Context search:** CF-SECTION; `DER_VI-b.tex`, ms.104–110, replacement and common inverses. **RS:** related Hua **106-section-criterion-span-faithfulness**; no separate selected RS result.

The coproduct-pushout-factorization diagram supplies the promised common third factorization, and the text says “il est trivial” that a section is inherited if either earlier weak equivalence has one. The section assertion follows by composing a section with the comparison map into the common refinement, but it does not identify the two sections thus obtained. This is exactly why the manuscript next isolates section independence rather than declaring the construction finished.

### C106-17 — The terminal criterion is a conjectural sufficiency statement on the page

**Location / kind:** 106/016, condition (*) and final paragraph; self-flagged / expectation. **Context search:** CF-SECTION and CF-CANCELLATION; `DER_VI-b.tex`, ms.107–110, equality of two inverses after localization; `DER_VII-b.tex`, ms.68–73. **RS:** Hua, findings register, **106-section-criterion-span-faithfulness**, conjecture candidate, intake “new to us”.

Condition (*) asks that the component of the roof (1_x,i) be independent of a section i of f ∈ W. The final words, “comme on doit pouvoir vérifier aisément, en construisant bel et bien le foncteur cherché”, leave the sufficiency proof unwritten; necessity follows from faithfulness because both sections become f⁻¹ after localization. Hua's entry captures the subject of the criterion, but its prose must not be read as evidence that this packet supplies the missing verification.

### C106-18 — Our conditional resolution of the W₀-localization doubt

**Location / kind:** response to 106/012; own idea, verification of a standard consequence. **Confidence:** high under the stated standard hypotheses; the remaining uncertainty is their identification with the manuscript's abbreviated C1–C3. **Context search:** CF-AXIOMS, CF-COUNIVERSAL, CF-SECTION; `DER_VI-b.tex`, ms.107–112, related but different localizations. **RS:** bears on Hua **106-section-criterion-span-faithfulness**; no exact selected RS result is being re-proved.

Assume every object is cofibrant, coproduct inclusions are cofibrations, and every map factors as a cofibration followed by a weak equivalence: for f:X→Y in W, factor (f,1):X⊔Y→Y as X⊔Y→Z→Y, with components j_X,j_Y and retraction r. Both j_X and j_Y are acyclic cofibrations by two-out-of-three, so any functor inverting W ∩ cof sends r to F(j_Y)⁻¹ and f=rj_X to an isomorphism. Hence W₀⁻¹C→W⁻¹C is an equivalence under these hypotheses, without needing to assume the disputed faithfulness of the particular roof category; this is a standard Brown-factorization consequence, not a novelty claim (Brown, 1973, p.421, dual factorization; Rădulescu-Banu, 2009, §1.3).

### C106-19 — Higher mapping data remain an additional problem

**Location / kind:** 106/006–016; unpursued implication. **Context search:** CF-COMPOSITION; `DER_VII-b.tex`, ms.82 and commentary following ms.87–91, ordinary π₀ versus mapping types. **RS:** dossier **PATHS A.P1**, Proved claim; **CATHOT E.26**, Open, VII ms.108–123; these statuses are not reconciled by the packet.

The construction in this packet uses connected components of roof categories, so even a successful faithfulness proof would compute ordinary localized Hom sets only. The nerve of a roof category, its comparison with a hammock localization, and its behaviour under diagram formation require additional theorems of the kind discussed by Horel (2016). This distinction prevents a short-fraction calculation here from being treated as a proof of every PATHS mapping-space claim.

### C106-20 — The W-only programme is a genuine thematic link, not a dating tool

**Location / kind:** 106/008 and 106/012; unpursued implication. **Context search:** CF-AXIOMS and CF-COUNIVERSAL; `ps6.tex`, §125, pp.530–533, dated “13.10.” in the supplied text. **RS:** Hua **106-section-criterion-span-faithfulness**; no selected RS entry fixes the date of these leaves.

The willingness to vary cofibrations while retaining W parallels the *Pursuing Stacks* passage proposing weak equivalences as the basic data and a derivator as the model-independent structure. This contextual link helps explain the mathematical motivation but neither identifies “Brown” with “Baues” nor dates these undated sheets to the dated PS entry. It also supplies no relative Theorem A statement on these pages.

## B. Reading questions raised after freezing

### RQ-01 — Brown in the ink, Baues in the comparison register

**Location / kind:** 106/002, first sentence; reading question. **Context search:** CF-AXIOMS; `ps6.tex`, §125, pp.530–532, explicitly Baues; RS Hua entry explicitly Baues. **RS:** **106-section-criterion-span-faithfulness**, candidate, intake “new to us”.

The frozen reading is underlined “Brown”, with doubtful “C1 . C3|C1 : C3” and “pour mé. C0”, whereas Hua's register calls the assumptions Baues's. The PS context provides a reason to investigate that attribution, not permission to substitute it for the observed name. The exact axiom source remains a reading and bibliographic question; Brown's published fibrant axioms are labelled A–E (1973, pp.420–421), which does not resolve the manuscript numbering.

### RQ-02 — The composition formula at the first roof construction

**Location / kind:** 106/006, final display; reading question. **Context search:** CF-COMPOSITION; `DER_VII-b.tex`, ms.77–82. **RS:** related Hua **106-section-criterion-span-faithfulness**; dossier **PATHS A.P1**, Proved claim.

The frozen formula retains `\unsure{g'g|g'f}` rather than silently choosing the composition suggested by the diagram. The contextual composition formalism makes g′f mathematically natural, but it does not decide the written second letter. This uncertainty concerns the local formula, not the existence of the pushout construction.

### RQ-03 — Identity subscript in the canonical arrow-to-roof map

**Location / kind:** 106/008, f↦(f,Id) display; reading question. **Context search:** CF-COMPOSITION; `DER_VII-b.tex`, ms.68–73. **RS:** related Hua **106-section-criterion-span-faithfulness**.

The frozen reading `\operatorname{Id}_{\unsure{x|y}}` preserves the unresolved subscript. For a roof x→y←y the definition suggests Id_y, but that type check belongs here and cannot settle the ink after the freeze. The later path-localization context has identity insertions but no independent witness to this specific subscript.

### RQ-04 — The direction of β and the role of its section

**Location / kind:** 106/014, factorization diagram and “β a une section i”; reading question. **Context search:** CF-SECTION; `DER_VI-b.tex`, ms.104–110. **RS:** Hua **106-section-criterion-span-faithfulness**.

The drawn β is retained in the same visible direction as the section arrow although the prose calls i its section. A mathematical reconstruction would orient the retraction oppositely, as in standard weak-lifting factorization, but the frozen diagram is unchanged. This is a substantive diagram/prose tension and one of the lower-confidence parts of the packet.

### RQ-05 — Section primes and an occurrence of f rather than f₀

**Location / kind:** 106/016, middle paragraph and the factorization of [f₀,i]; reading question. **Context search:** CF-SECTION; `DER_VI-b.tex`, ms.107–110. **RS:** Hua **106-section-criterion-span-faithfulness**.

The section-prime readings remain explicitly doubtful, and the displayed decomposition retains `(f,Id)` where the intended typed composition appears to require `(f₀,Id)`. Common-refinement arguments in the context explain the intended roles of the maps but do not supply new evidence for the marks on this sheet. Neither potential correction has been introduced into the transcription.

### RQ-06 — Projection subscripts are deliberately cross-labelled

**Location / kind:** 107/004–016, product projections; reading question. **Context search:** HOM-RELATIVE and HOM-TENSOR; `DER_XVIII-a.tex`, ms.63–64. **RS:** dossier **BISITE E.3** and **BISITE F.1/F.4/F.7/F.8**, thematic ordinary precursors; their exact register status is retained in the concordance.

The frozen diagrams use p_B for the projection to A and p_A for the projection to B. Modern conventions or the later companion may invite the opposite naming, but the repeated cross-labelling is retained and used consistently when interpreting the formulas here. Any comparison that silently renames the projections risks changing the meanings of the two relative Hom functors.

### RQ-07 — Two readings of continuity must not be merged

**Location / kind:** 107/014 and 107/017, exclamation marks and duality notation; reading question. **Context search:** HOM-CONTINUITY and HOM-RELATIVE; `DER_XVIII-a.tex`, ms.63–64, original text and separate commentary. **RS:** thematic to **BISITE E.3** and the BISITE F ordinary/enhanced distinctions; no exact selected RS claim supplies a corrected reading.

The page uses `!`, `!!`, superscripts and subscripts, with explicit declarations of what is meant at particular points; these are not interchangeable primes. The later separate-continuity discussion exposes a mathematical distinction between joint and separate continuity, but that distinction cannot be used to normalize the manuscript's notation. The doubtful superscript on the deleted boxed formula at 107/017 remains doubtful.

### RQ-08 — Product symbol in the external-product definition

**Location / kind:** 107/014, definition of L⊠M; reading question. **Context search:** HOM-TENSOR and HOM-CONTINUITY; `DER_XVIII-a.tex`, ms.63–64. **RS:** thematic **BISITE E.3** and **BISITE F.1**; no selected RS statement adjudicates this symbol.

The frozen definition retains an external-product symbol between the two pulled-back factors, where an internal cartesian product is the type-correct candidate. The finite-set tests below examine the evident mathematical interpretation, not an amended transcription of the symbol. The later XVIII discussion is a conceptual parallel, not a second image of this formula.

### RQ-09 — The overwritten codomain does not license a blanket rejection of Yoneda

**Location / kind:** 107/014, fully faithful assertion and proof; reading question. **Context search:** HOM-CONTINUITY; `DER_XVIII-a.tex`, ms.63–64. **RS:** thematic BISITE E–F entries as recorded in the concordance.

The codomain is overwritten toward the presheaf category on Â×B̂, so the assertion must be evaluated with that overwritten text visible. Yoneda on the product category is fully faithful; the false step is the identification of its representable Hom-pair presheaf with the separately extended external-product evaluation. The notes' counterexample targets that identification rather than treating every fully faithful phrase in the passage as the same assertion.

### RQ-10 — The boundary exponent display is schematic and unfinished

**Location / kind:** 107/015, upper formulas and arrow marked “??”; reading question. **Context search:** HOM-TENSOR and HOT-RECTIFY; `DER_XIII-a.tex`, ms.48–50, and `DER_XIII-b.tex`, ms.63–65, ordinary limits, fibrant diagrams, and the corresponding commentary; dossier BISITE presheaf-model entries. **RS:** **BISITE C.1**, Proved (return's claim), `BISITE_results.csv`, VI ms.83 and XII ms.224–225, only a thematic connection.

The display for `(X^{\dot\Delta_n})_0` records a limit of the indicated face data and does not fully specify its indexing diagram; the following Hom(M,a)⇒a arrow carries two question marks. A matching-object interpretation is a possible mathematical explanation, but it does not justify supplying missing indexing arrows or a finished formula. The page remains an exploratory calculation, not a proved general matching-object theorem.

### RQ-11 — Quillen's proposition and the unresolved page numeral

**Location / kind:** 107/021, Quillen reference; reading question. **Context search:** HOT-RECTIFY; `ps6.tex`, §125, and the Quillen material identified in the literature section. **RS:** Hua **107-relative-square-rectification**, conjecture, intake “new to us”.

The frozen citation keeps `Ch. \unsure{II|I}`, proposition 4, and page `\unsure{2.4|2.9}`. The content is consistent with the simplicial homotopy lifting proposition in Quillen's *Homotopical algebra*, but the original printed page number was not independently verified in this run. A modern re-typesetting is identified as such and does not resolve the palaeographic alternatives.

### RQ-12 — Bars on the homotopy-class Hom comparison

**Location / kind:** 107/019, 107/021, and 107/025; reading question. **Context search:** HOT-LIMIT; `DER_III-V.tex`, V ms.44–46, invariant ind-objects, and `DER_VII-b.tex`, ms.82, diagram localizations. **RS:** Hua **107-hot-sequential-colimits**, literature claim; **CATHOT E.17**, Open, `CATHOT_results.csv`, a different variance of sequential question.

The manuscript explicitly introduces the homotopy-class interpretation at 107/021, while later displays sometimes write Hom without the bar. The notes interpret the return to “our initial pb” at 107/025 in that homotopy-category setting, while leaving every bar exactly as transcribed. Literal sets of maps and their π₀ have different limit behaviour; silently inserting bars would hide the very issue under investigation.

### RQ-13 — The last homotopy-extension diagram has uncertain indices and headless strokes

**Location / kind:** 107/025, middle diagrams; reading question. **Context search:** HOT-RECTIFY and HOT-LIMIT; `context/companion/chunks/DER_VII-b.tex`, ms.108–117, and `context/companion/chunks/DER_VII-c.tex`, ms.118–123, contextual coherent-comparison problems. **RS:** Hua **107-hot-sequential-colimits** and **107-relative-square-rectification**; **CATHOT E.26**, Open, remains a distinct question.

The frozen diagram retains `\unsure{i-1|i+1}` at several positions and preserves strokes with no visible arrowhead. The attempted induction suggests i+1, but that is not a reason to replace the first ink reading or to add heads. The general obstruction discussed below does not depend on resolving those local graphical uncertainties.

### RQ-14 — Reused computer listings are independent textual evidence

**Location / kind:** 106/003,005,007,009,011,013,015,017 and 107/002,005,007,009,011,013,015,017,020,022,024,026; reading question / scope. **Context search:** PRINTED, with no hits for PREDONTA, DOCUGRA2, PLOTEDIT, GRAPHI2, or the printed listing dates in the supplied context. **RS:** no selected mathematical entry bears on the code, job logs, or output banners.

The computer listings, job-control text, overprinted banners, and handwritten operational annotations were transcribed as content, not replaced by descriptions. Mathematical or machine-code plausibility has not been used to “repair” doubtful digits, repeated rows, abbreviations, or labels. Printed dates date the production of the reused stock and give a terminus post quem for writing on that same stock, not a date of composition for the whole mathematical dossier.

## C. Standing question: steps the manuscript itself marks as unverified

This register includes local flags even when the page subsequently resolves them. Uncertain readings introduced by the transcriber are not counted as Grothendieck's question marks. Claims merely called “immédiat” or “trivial” are recorded in the itemized notes above and below; the table concentrates on explicit doubts, questions, promises of verification, and unfinished checks.

| Scan | His words or visible flag | What is at issue | State within this packet / detailed note |
|---|---|---|---|
| 106/002, upper margin | `Ho C`, doubtful `Cat. d'obj. cofibrants`, `?` | Working identification or title of the homotopy-category calculation. | Not a completed title theorem; C106-01, RQ-01. |
| 106/002, end | “Si ce lemme est valable” | Cancellation needed for the choice-independent quasi-inverse. | Reformulated as a criterion at 106/006; C106-02, C106-05. |
| 106/003, trial diagram | Arrow labelled `?` | Candidate comparison in the replacement diagrams. | Diagrammatic trial, not a proved lift; related C106-02. |
| 106/004, lower half | “il faut vérifier que c'est fonctoriel” | Naturality of the ΨΦ comparison. | Calculation follows, ending “cqfd”; C106-04. |
| 106/008 | “on veut prouver”, arrows `g?`, `i?` | Inversion of W in the component category. | Specific proposed argument fails at 106/010; C106-09. |
| 106/010 | “Ça marcherait si”, “Ça se présente mal !” | Postcomposing f into a cofibration. | The proposed repair is explicitly rejected; C106-09. |
| 106/012, opening | “il n'est pas clair” | Faithfulness of the short-roof comparison. | Construction revised; C106-11, C106-13. |
| 106/012 | “semble-t-il”, “Mais je doute” | Whether W ∩ cof alone suffices for localization. | No resolution on the page; conditional modern argument C106-18. |
| 106/014 | “il faut montrer que ça ne dépend pas des choix faits” | Independence of factorization and lifting choices. | Reduced at 106/016 to section independence; C106-15. |
| 106/014 | “il faut voir qu'ils sont dans une = composante connexe” | Common-component comparison of two roofs. | Common refinement constructed next; C106-16. |
| 106/014, margin | “On vérifie aisément” | Object bijection and arrow surjection for the revised comparison. | Condensed sketch; not a faithfulness proof; C106-15 and C106-17. |
| 106/016 | “Donc il reste à prouver” | Independence of a chosen section. | Isolated as (*), not proved in this packet; C106-17. |
| 106/016, end | “comme on doit pouvoir vérifier aisément” | Sufficiency of (*) and construction of C→C̃. | Still an expectation on the page; C106-17. |
| 107/003, cancelled draft | Membership `?`, “what about”, “This is easily checked (see below) to be” | Relative-Hom formulas in the initial simplicial draft. | Draft cancelled, calculation unfinished; revised general framework at 107/004–010. |
| 107/006 | “il faut un iso” | Adjunction calculation for Γ_M. | Displayed Hom calculation follows; see relative-Hom notes. |
| 107/008, cancelled words | “Je ne sais pas” | An exploratory qualification in the stability discussion. | Cancelled, with cramped revised text; do not treat as a final negative theorem. |
| 107/015 | Hom(M,a)⇒a with `??`; unfinished final formula | Cotensor/representability and boundary calculations. | Not resolved in these pages; RQ-10. |
| 107/019 | “Filtering … exist in (Hot)?”; “We would like moreover” | Existence of filtered colimits and their preservation by localization. | Only the countable problem is developed; injectivity remains open at 107/025. |
| 107/019 | “We're to check” followed by (i), (ii) | Universal property of X′∞ and weak equivalence u∞. | Distinct tasks; neither should be inferred solely from the other. |
| 107/021 | “Surjectivity of (*)?”; “the question is to find” | Strictly compatible representatives of compatible homotopy classes. | Claimed obtained at 107/023–025 in the terminal-target case. |
| 107/021 | Equalities followed by `?`; “possibly not always satisfied!” | Strictification and compatibility of the two homotopies. | Compatibility becomes the explicit qualification; see square-rectification notes. |
| 107/023 | “All we have to do, is to check” | Choosing compatible homotopies. | Terminal-target special case says “we are through!”; no unqualified general solution. |
| 107/023, cancelled top diagram | Both arrows labelled `cofib?` | A tentative cylinder/cofibration comparison. | Cancelled attempt, not a proved cofibration statement. |
| 107/023, lower diagram | Dashed `h′?`, underlined “non trivial cofibration” | A lift with both endpoints prescribed. | No general lifting conclusion supplied. |
| 107/025 | “To prove it injective”, dashed h with `?` | Extending homotopies compatibly through the sequence. | Left unresolved. |
| 107/025, end | “Is there a retraction … ?”, “not clear at all”, “Ask Ronnie Brown!” | A compatible inverse system of retractions / homotopies. | Final unresolved point of the mathematical text. |

For each row the detailed note supplies the contextual search and RS connection; the scans with only trial diagrams belong to the same explicitly identified argument. The printed JES `???` fields at 107/024 are machine-output text and are not mathematical self-flags.

## D. Standing question: title sheets, numbering, counts, and dating limits

| Scan | Title or heading, with its reading state | Number/count evidence | Interpretation |
|---|---|---|---|
| 106/002 | Marginal `Ho C` and doubtful `Cat. d'obj. cofibrants` followed by `?`. | Manuscript number 1 at the foot. | No separate title sheet or explicit total-page count appears in the retained cote 106 scans. |
| 107/002 | Doubtful “Formalisme” des X⊗M, X^M, Hom_A, Hom_B, doubtful “relatifs\|relatif”, followed by “: une rédaction” and underlined “provisoire”. | Manuscript number 1; reused printed `PAGE 4`. | A title for the first mathematical unit; `PAGE 4` belongs to the assembler listing. |
| 107/018 | “Question des lim→ filtrantes / dans Hot”. | Manuscript number 17. | A second title sheet introducing the sequential-colimit question; no total-page count is written. |
| 106/003, 106/017 | Printed `PAGE 0001`; printed `PAGE 1` twice on the Fortran sheet. | Computer-listing pagination. | These numbers do not count mathematical pages. |
| 107/026 | Printed `PAGE 2`. | Computer-listing pagination. | This is the assembler listing's page number, not the homotopy note's second page. |

### D.1 Complete manuscript-number crosswalk

The foot numbering runs through **1–16** on 106/002–017 and **1–25** on 107/002–026; these observed sequences are not declarations that a separate work contains exactly that many pages. Additional mathematical-unit numbers coexist with them and are preserved below, including doubtful forms.

| Cote | PDF scans | Visible manuscript-number sequence |
|---|---|---|
| 106 | 002–017, respectively | Foot numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16. |
| 106 | 004, 006, 008, 010, 012, 014, 016 | Additional upper numbers 2; `\unsure{7\|3}`; 4); 5); 6); 7); 8). |
| 107 | 002–026, respectively | Foot or sheet numbers 1 through 25. |
| 107 | 004, 006, 008, 010, 012, 014, 016 | Additional letters a, b, c, d, e, f, g. |
| 107 | 019, 021, 023, 025 | Additional circled a, circled b, circled `\unsure{e\|c}`, and enclosed d. |

### D.2 Dates on the reused stock

106/005 and 106/013 carry DOCUGRA2 output dated **24 AUG 82**; 106/007,009,015,017 carry **25 AUG 82** or **08/25/82**, with earlier software or journal-update dates also printed. 107/002,005,020,024,026 carry assembler/job material of **04 JUN 82**, **06/04/82**, or the corresponding job date code. These dates support only the lower bound appropriate to reuse of those sheets; none is a dated mathematical autograph, and the packet does not establish that a claim is an “1983 form”.

**Context search / RS:** PRINTED has no matching listing identifiers in the supplied context; HISTORICAL finds the planning README and dated PS passages but no source that dates this handwriting. The title/count observations therefore add material evidence to the packet without changing any mathematical RS status.

## E. Core conclusions and their limits

The strongest findings of the comparison are the unfinished faithfulness argument in 106, the false unrestricted product-Hom formulas in 107, and the explicit surjectivity/injectivity split in the final sequential-colimit inquiry. Their detailed notes and independently checked counterexamples follow. The full result concordances distinguish direct partial forms, thematic precursors, and absence; a shared word such as “filtered”, “Hom”, or “cofibration” is never sufficient to identify two statements.

Strong W(7), total-aspherical ⇒ filtered, and relative Theorem A are **absent from the frozen 106+107 text**. The bounded first-appearance leads supplied by the other textual sources are stated in the STRATA/PATHS comparison below, with manuscript and commentary layers kept separate. They do not establish first composition or priority across the archive.
