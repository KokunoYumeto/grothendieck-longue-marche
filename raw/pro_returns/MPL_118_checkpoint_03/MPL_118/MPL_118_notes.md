# MPL 118 — Research notes after the frozen transcription

## Scope, evidence and reading conventions

The primary reader personally transcribed and then personally audited all 38 supplied scans, in order, without OCR or delegated image reading. The 38 page files and the combined fragment were frozen at **2026-11-18 02:41:21 UTC**; the research context was opened at **02:41:34 UTC**. Research assistants subsequently compared the frozen text with the supplied context and challenged selected mathematical arguments; they did not read the manuscript images or alter the transcription.

Every manuscript locator below means **Montpellier cote 118, PDF scan number**, not the archive's pencilled foliation. Hua's page number is normally one less than this scan number. A quotation in backticks is a literal fragment of the frozen TeX; a short quotation in quotation marks retains the manuscript's wording but may omit surrounding TeX formatting. The uncertainty marks in the transcription remain authoritative: a mathematical discussion of a possible reading does not settle its letters.

The dossier mappings at the end cover **all 255 supplied statements** and **all 12 numbered NEW_RESULTS entries plus its 3 “Known after all” entries**. “Partial” means a clause occurs with less scope; “analogue” means a related construction or question occurs; “absent” means the actual statement was not found in the complete frozen text, even when nearby vocabulary is recorded. None of those labels endorses the supplied Proved, Refuted, Known or Open status: those are claims of their source unless an explicitly identified review is reported there.

Notes are one to four sentences each; source and evidence metadata are separate from the note. Detailed proofs of the few arguments actually checked are in the linked research records, while `CHECK_EVENTS.tsv` distinguishes those checks from textual comparison and background use. No proof certificates mentioned by Hua were supplied or executed here, and no unpublished return omitted from the context was treated as read.

**Technical boundary.** The combined frozen fragment accidentally has two consecutive `\cotefile{118}` commands at its opening; the page files are unaffected. This assembly defect was discovered only after context access and has deliberately not been repaired, in obedience to the freeze; see `records/technical_qa/FROZEN_ASSEMBLY_LIMITATION.md`. Static delimiter and diagram checks passed, but the available TeX installation could not compile the validation wrapper, so no claim of successful rendering is made.

## The three historical questions

### MPL118-H01 — Where does the strong W(7) first appear?

**Kind:** reading question. **118 evidence:** scans 015, 020–023; “Fonctorialité si … dans … W” (015), “Mais attention” (023). **Context:** `context/companion/chunks/DER_XIIb-a.tex`, XII §V.2.1, ms. 75–78; `context/NEW_RESULTS.md`, result 8; `context/NEW_RESULTS.md`, result 8, referring to TOTASPH A.13; RESULTS_STATE TOTASPH A.9; primary edition [DER-XII-V] below.

No strong reverse-excision W(7) occurs in 118: the integral's objectwise invariance on 015 and the conditional comparison on 021 are forward statements, while the ordinary-pushout failure on 023 concerns a different assertion. The first explicit strong form located in the supplied edited chapter sequence is XII §V.2.1: W7bis on ms. 75–76 is a biconditional, and W7 on ms. 76–77 uses a two-out-of-three condition among the cube's three comparison assertions. The claim for the usual weak equivalences on ms. 78 is accompanied by an admission that its formal verification has not been done, and the reviewed counterexample reported as TOTASPH A.13/NR8 is carried here as prior work, without re-running its proof or accepting NR8's wider classification language. This is a located attestation in the supplied material, not a proof of chronological priority across the archive.

### MPL118-H02 — “Totally aspherical implies filtered”

**Kind:** reading question. **118 evidence:** scans 033–036, “tot. … asphérique”; 039, `\deleted{filtrant}`. **Context:** `context/companion/chunks/DER_II-a.tex`, ms. 36–36ter; `DER_XIIb-a.tex`, XII §V.2.3, ms. 88–89; NEW_RESULTS 11, referring to TOTASPH C.5–C.10; RESULTS_STATE TOTASPH C.10 and POLES H.2; DOSSIER RESIDUE F.1 and STRATA G.2; primary editions [DER-II] and [DER-XII-V].

The implication “totalement asphérique ⇒ filtrant” is absent from 118, whose product discussion uses asphericity of products of representables and whose filtration theorem cancels the word “filtrant”. The supplied later text raises the filteredness question at II ms. 36, withdraws its proposed negative Proposition 2.19 at ms. 36bis–36ter, and renews the conjecture there. XII ms. 88–89 explicitly distinguishes its ordinary-final-image notion of totality from the earlier Pursuing Stacks notion, so the two meanings cannot be identified from the shared adjective. The reviewed Δinj lead in TOTASPH C.5–C.10/NR11 belongs to that later quantifier problem and is credited without re-derivation; neither it nor these notes establishes an archive-wide first date.

### MPL118-H03 — Did he have relative Theorem A in 1983?

**Kind:** reading question. **118 evidence:** scan 026, “Cela résulte alors de loc. 3” over a common discrete base J; scan 040, `f_{/i}:X_{/i}\mathbin{-}Y_{/i}` and “donc on gagne par L3”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, ms. 1–8, Loc (3) versus (3 bis); RESULTS_STATE GALOIS B.1/B.3; DOSSIER RESIDUE B.8/B.10; primary [PS], §64, manuscript pp. 164–165; [MPL-CATALOG].

These two applications show the relative common-base principle being used as an available tool in 118, although its complete axiom is not written out there and the filtration application needs the repair in C03. They do not prove the calendar-year assertion: 118 is undated, the reused notice on 018 is dated 28 April 1983, and the catalogue's “from 1983” description dates the dossier only broadly. Cote 117's contents were not supplied or inspected, so its 1983 catalogue date cannot establish what theorem it contains. In the primary Pursuing Stacks text §64, L4 is the absolute slice statement and L5 is a separate fibrewise axiom for cartesian functors between fibrations; that explicit formulation prevents silently importing modern relative Theorem A into every 1983 use of the words “basic localizer”.

## Targeted mathematical checks and their limits

### MPL118-C01 — The integral does commute with strict base change

**Kind:** unpursued implication. **118:** scan 020, “Ce diagramme est-il cartésien ? À vérifier !”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, ms. 3–8, fibrewise invariance; Hua, modernised reading of cote 118, “Quand le carré est-il cocartésien ?”; related POLES B.2. **Check record:** `records/research/targeted_proof_peer_review.md`, C01.

For a strict diagram D:K→Cat/B, the two categories (∫D)×_B B′ and ∫(D×_B B′) are canonically isomorphic by changing the parentheses of their tagged objects and arrows. This supplies the categorical identification asked for on 020, but universal membership in W still requires a weak-equivalence comparison for every pulled-back diagram. It proves no general commutation of ordinary Cat pushouts with pullbacks.

### MPL118-C02 — The cartesian opfibration comparison

**Kind:** unpursued implication. **118:** scan 021, “un diagramme cartésien, avec … des cofibrations”; “isom. à la catégorie ponctuelle”; margin “au lieu de ponctuelle, il suffit qu'elle soit … asphérique”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, ms. 3–8; `DER_XIIb-b.tex`, §V, ms. 147–149; RESULTS_STATE 118-pushout-along-cofibrations-in-cat and POLES B.2. **Check record:** `records/research/targeted_proof_peer_review.md`, C02.

The literal cartesian-square hypothesis makes the integral fibre the span integral of A×C→A and A×C→C, and the opfibration hypothesis makes the total comparison an opfibration. When one fibre is the point, that integral retracts onto the cone on the other fibre, exactly explaining the surviving deformation-retraction margin. For a relative basic localizer, replacing a W-aspherical factor by the point also validates the marginal weakening, using product closure and objectwise invariance of the integral. No cocartesian hypothesis is needed for this comparison theorem; the checked scope therefore improves the candidate formulation credited to Hua without importing his extra hypothesis into the ink.

### MPL118-C03 — Repairing the lax filtration triangle

**Kind:** own idea. **Confidence:** high, because the replacement, transformations and comma retractions were checked independently. **118:** scans 039–040, `f(X_i)\subset Y_i` and “s'identifie à … donc on gagne par L3”. **Context:** `context/companion/chunks/DER_XVI.tex`, relative Loc (3 bis), ms. 3–8; Hua, modernised reading of cote 118, “Filtrations (pages 38 et 39)”; DOSSIER RESIDUE B.10. **Check record:** `records/research/targeted_proof_peer_review.md`, C03.

Hua already points out the missing strict commutation: compatible filtrations give ψf≤φ, not ψf=φ, even when all stage maps are weak equivalences. My repair is to replace X by RX=∫_i X_i and Y similarly, so Rf is strictly over I and each forgetful map RX→X is a homotopism using the minimum stage of an object. The comma category (RX)/i retracts onto X_i, allowing relative Theorem A and two-out-of-three to prove f∈W under the retained minimum-stage hypotheses. This repairs this application only and is not asserted as a new theorem about arbitrary covers or arbitrary filtered colimits.

### MPL118-C04 — The groupoid example refutes the connected repair

**Kind:** unpursued implication. **118:** scan 036, “Mais un A … 0-connexe … est alors … asphérique” followed by “Prenons p.ex. … un groupoïde”. **Context:** RESULTS_STATE 118-groupoid-products-not-totally-aspherical; Hua, modernised reading of cote 118, “Le lemme des pages 32 à 35”; [CIS-2006], Proposition 4.3.2, p. 168; [CIS-CORRECTION]. **Check record:** `records/research/root_secondary_peer_review.md`, C04.

For W=W∞, the ordinary weak homotopy equivalences, and a group G, a G-set map is a weak equivalence on categories of elements precisely when it is an equivariant bijection, since equivalence of the action groupoids forces a bijection on orbits and equality of stabilizers. Thus W_BG is closed under finite products while BG, for nontrivial G, is connected and non-aspherical; the page's own example defeats the immediately preceding connectedness assertion, although no written “Non” occurs there. This is credited to Hua's finding, not claimed as a new discovery, and the author of the cited literature proposition explicitly confirmed that its implication (g)⇒(c) needs another hypothesis. The formal certificate named by Hua was not supplied or executed.

### MPL118-C05 — Product comparisons and the empty-category exception

**Kind:** unpursued implication. **118:** scan 035, `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}`. **Context:** RESULTS_STATE 118-product-condition-iv; Hua, modernised reading of cote 118, “Le lemme des pages 32 à 35”; [MALT-2020], §1.7, Proposition 1.7.1 and Definition 1.7.2. **Check record:** `records/research/root_secondary_peer_review.md`, C05.

The displayed comma identification is correct: the arrows to the chosen a- and b-elements determine the two presheaf elements uniquely, leaving the category of elements of the product of the two representables. Absolute Theorem A then gives the product comparison from asphericity of these categories. The diagram's binary/finite equivalence additionally needs the nullary comparison A→e, and A=∅ with ordinary weak equivalences is the exceptional counterexample to the unqualified equivalence. Hua already states this exception; the present check confirms its application to the literal diagram.

### MPL118-C06 — Infinite products: an existing counterexample applies

**Kind:** unpursued implication. **118:** scans 034, 036–037, “si on savait qu'un produit infini …” and “ce n'est pas évident”. **Context:** `context/companion/chunks/DER_VI-b.tex`, comment dgrb266, ms. 131–132; `DER_XVIII-c.tex`, comment dgrb1045, ms. 222–223; DOSSIER PATHS D.16; [THOM-1980], introduction, pp. 307–308. **Check record:** `records/research/root_checks.md`, C06.

The finite-fence counterexample is already in the supplied companion and answers the manuscript's strict-product question negatively for W∞. Although every finite fence P_n is contractible, in ∏P_n the endpoint sequences (0)_n and (n)_n cannot be connected by a finite zigzag, because a zigzag of length m moves every coordinate by at most m edges. This is an application of the supplied example, not an independent discovery or a new proof of PATHS D.16, and it does not deny existence of products in the localized homotopy category. Thomason's 1980 introduction independently warns that ordinary infinite products of categories need not have the expected homotopy groups.

### MPL118-C07 — The fundamental-groupoid pushout expectation

**Kind:** unpursued implication. **118:** scan 023, “Il semble vrai pourtant que si g induit une … 1-équiv. … alors f aussi”. **Context:** `context/companion/chunks/DER_XIIb-a.tex`, comment p114, final paragraph; RESULTS_STATE POLES H.5, whose supplied excerpt is truncated; Hua, modernised reading of cote 118, “Mais attention”; [COYNE-NOOHI], §8.1, Proposition 8.4. **Check record:** `records/research/groupoid_pushout_peer_review.md`, C07.

The expectation is correct, more generally when the pushout leg i is any object-injective functor. Groupoid completion Π₁ preserves pushouts and object sets, so Π₁i is a cofibration in the groupoid model structure, and left properness carries the equivalence Π₁g to Π₁f. The supplied companion already states the relevant object-injective/W₁ conclusion at XII ms. 114, and POLES H.5 signals the wider boundary; these receive credit, while the omitted full return is not treated as inspected. This conclusion concerns 1-equivalences and does not repair the failure for all weak homotopy equivalences.

### MPL118-C08 — A precise choice in the suspension example

**Kind:** own idea. **Confidence:** high for the explicit choice, because the suspension homology calculation is immediate; no novelty is claimed. **118:** scan 023, “prendre p.ex. … un groupoïde … avec Π₁≠1”. **Context:** Hua, modernised reading of cote 118, “Mais attention”; `context/companion/chunks/DER_XIIb-a.tex`, §V.2.1, ms. 75–78; NEW_RESULTS 8, referring to TOTASPH A.13; RESULTS_STATE TOTASPH A.9. **Check record:** `records/research/root_checks.md`, C08.

Taking Z=BC₂, or Bℤ, makes the page's double-cone example decisive: its suspension has nonzero second reduced homology, whereas the collapsed pushout for connected Z is an interval. The condition Π₁(Z)≠1 alone should not be read as a universal sufficient condition for noncontractibility of the suspension; nonzero H₁ is a safe explicit choice. This clarification concerns the ordinary pushout example and neither repeats nor identifies it with the later reviewed acyclic reverse-excision counterexample in NR8.

### MPL118-C09 — What the telescope actually proves

**Kind:** unproved claim. **118:** scans 040–041, “Par calcul des fractions” and “donc on gagne!!”. **Context:** RESULTS_STATE 118-strong-saturation; Hua, modernised reading of cote 118, “La saturation (pages 39 et 40)”; `context/companion/chunks/DER_XVI.tex`, saturation discussion in §1; [CIS-2006], Proposition 4.2.4, p. 162. **Check record:** `records/research/root_checks.md`, C09.

Once the displayed sequence of open immersions with consecutive two-step composites in W exists, the even and odd subsequences and the repaired filtration theorem do make both maps to the telescope weak equivalences. The manuscript has not completed all ingredients for constructing that sequence in Cat: its fraction calculus, homotopy-to-weak-equivalence passage and chosen factorizations remain dependencies. The theorem of strong saturation is known, as Hua already records, but the surviving 041 argument is not a self-contained proof from the abbreviated axioms on 015. The entire earlier proof on 040 is deleted and must not be combined with 041 as though both were live proofs.

### MPL118-C10 — Strong saturation descends to W_A formally

**Kind:** unpursued implication. **118:** scan 040, “Cor Pour ∀ A, W_A est saturé”. **Context:** RESULTS_STATE 118-strong-saturation; Hua, modernised reading of cote 118, “La saturation (pages 39 et 40)”; [CIS-2006], Proposition 4.2.4, p. 162. **Check record:** `records/research/root_secondary_peer_review.md`, C10.

If W is strongly saturated and W_A is its inverse image under the category-of-elements functor i_A, the induced functor Hot_A→Hot sends an invertible image of u to an invertible image of i_Au. Strong saturation of W then gives i_Au∈W and hence u∈W_A. This verifies the corollary for every A without an additional asphericity hypothesis, while leaving the separate proof of strong saturation of W outside this formal argument.

### MPL118-C11 — The literal sum assertion needs a hypothesis on W

**Kind:** own idea. **Confidence:** high, because the explicit two-component example was checked independently. **118:** scan 036, “La condition (ii) est visiblement stable par sommes”. **Context:** `context/companion/chunks/DER_XVI.tex`, §2, comment dgrb838, ms. 9–10; DOSSIER RESIDUE B.11; Hua, modernised reading of cote 118, “Le lemme des pages 32 à 35”. **Check record:** `records/research/targeted_proof_peer_review.md`, C11.

Hua's objection to condition (iv) does not address the literal condition (ii), but the latter also needs qualification when W is arbitrary. Apply the already supplied nonemptiness localizer W_ne to A=e⊔e: the map (*,∅)→(*,*) is in W_A, while multiplying by (∅,*) produces ∅→* on categories of elements and leaves W_A. Each individual point component does satisfy product stability, so this checks a new application of the companion's existing counterexample to the exact sum assertion. For W∞, componentwise detection makes the sum assertion valid, and the notes make no claim to have discovered W_ne or re-proved RESIDUE B.11.



### MPL118-C12 — The attaching weak immersion can also fail under pushout

**Kind:** unpursued implication. **118:** scans 015 and 023, “mais j'ignore si i∈W implique i′∈W”, then “Non”. **Context:** `context/companion/chunks/DER_XIIapp.tex`, ms. 14–15, comment dgrb657, “The pushout is a three-sphere”; `DER_XIIb-a.tex`, ms. 107 and comment dgrb534; RESULTS_STATE POLES H.5; primary XII §V.2, Proposition 11 and XII appendix. **Check record:** `records/research/weak_sieve_pushout_peer_review.md`, C12.

The explicit double-cone diagram on 023 addresses failure of g∈W⇒f∈W, whereas the separate negative claim about i∈W⇒i′∈W needs another example. The supplied XII appendix provides one: V=(0→a,0→b) includes as a full sieve and weak equivalence into V with a terminal object adjoined, but its indicated pushout has S³ homotopy type while the other input is contractible. The sieve and weak-equivalence properties were checked here; the existing corrected S³ calculation is credited to the companion and carried as background, with opposites giving the closed-immersion case. The historical appendix's erroneous fundamental-group calculation and its overbroad localizer extension are not adopted.

### MPL118-C13 — The aspherical-filtration corollary under the written hypotheses

**Kind:** unpursued implication. **118:** scan 040 margin, “Cor? Si les X_i sont … asphériques et I connexe”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, relative Loc (3 bis), ms. 3–8; Hua, modernised reading of cote 118, “Filtrations (pages 38 et 39)”; compare DOSSIER RESIDUE B.10. **Check record:** `records/research/additional_application_checks.md`, C13.

Under 039's actual hypothesis that every nonempty subset of the nonempty small poset I has an infimum, I has a least element inf(I). The constant point filtration therefore satisfies the same minimum-stage and intersection conditions, and C03 applied to X_i→e proves X→e∈W; connectedness is redundant under these stronger indexing assumptions. Connectedness by itself does not suffice after weakening them: the proper-face poset of a triangle is connected, all its principal downsets are contractible, and its union has circle homotopy type. This checks the manuscript's specific corollary without upgrading it to an unrestricted connected-cover theorem.

### MPL118-C14 — Completing the cross-Hom proof for the open–closed square

**Kind:** unpursued implication. **118:** scan 019, “Mais supposons que f soit cofibré” and the unfinished “(ii) Pour … fixé”. **Context:** `context/companion/chunks/DER_XIIb-a.tex`, §V.1.1, ms. 59–61; `DER_XIIb-b.tex`, ms. 147–149; Hua, modernised reading of cote 118, “Quand le carré est-il cocartésien ?”; related DOSSIER STRATA D.1/D.2 and RESIDUE I.5. **Check record:** `records/research/additional_application_checks.md`, C14.

The asserted ordinary pushout is valid for an opfibration f:X→X′ whose restriction over the open complement U′ is an isomorphism. Each cross arrow u′→y′ has an opcartesian lift from the unique u over u′, and the universal factorization of such lifts gives both surjectivity and injectivity of the displayed colimit of cross-Hom sets. Together with the unchanged internal Hom sets and the absence of arrows from the closed part into the open part, this proves the pushout universal property. A split cleavage is unnecessary, and the argument makes explicit the step which 019 begins but does not finish.



## Further claims, constructions and contextual links

### MPL118-M01 — The class lattices are a programme, not a proved classification

**Kind:** unproved claim. **118:** scans 003 and 005, the two inclusion lattices and the labels “str”, “stable by intersection”. **Context:** `context/companion/chunks/DER_XI-XIIa.tex`, XII §III, ms. 26–52; DOSSIER BISITE A.15, B.7–B.11; Hua, modernised reading of cote 118, “Les treillis (pages 2 et 4)”.

The diagrams announce many inclusions, strictness claims and exceptions to intersection or base-change closure without providing individual proofs. Scan 009 supplies definitions for some of the labels, but the entire lattice cannot be certified by replacing it with a later diagram of modern fibration classes. In particular, the later BISITE B.9 threshold concerning Sm∩Pr⊂Fib_W shows why the weak-equivalence class has to be stated before generalizing the boxed inclusion beyond the usual W∞ case.

### MPL118-M02 — Serre maps, fibres and universal weak equivalences

**Kind:** unproved claim. **118:** scan 005, “A Serre map is in W iff … fibers are aspheric” and “universellement”; scan 009, the arbitrary-arrow-over-Y definition of S. **Context:** `context/companion/chunks/DER_XI-XIIa.tex`, XII §III, ms. 28–36; `DER_XIIc-a.tex`, §4, ms. 208–218; DOSSIER BISITE A.2/A.15/B.7.

The asserted equality S∩W=S∩T identifies weak Serre maps with universal weak equivalences, and the fibre test is part of the handwritten programme. Its later intrinsic-fibration counterpart has the same over-base quantifier, but a proof needs the applicable fibrewise criterion and the specified localizer. The present package records the antecedent statement without validating every equality in the lattice.

### MPL118-M03 — Properness and derived base change

**Kind:** unproved claim. **118:** scan 009, “La cat. des rel. d'une flèche … est asph.” and “R^i f_* … aux chgt de base … quelc.”. **Context:** `context/companion/chunks/DER_XI-XIIa.tex`, XII §III, Proposition 3/Definition 2, ms. 26–28, and Propositions 6–7, ms. 31–36; DOSSIER STRATA D.3/D.4 and BISITE A.9/F.2.

This is a substantive precursor of the proper/smooth base-change criteria: the page places lift-category asphericity beside commutation with derived direct image. The coefficient theory, quantification over coefficients and precise direction of the dual formula are not supplied here, so the diagram is not a proof of the later derivator-level statement. The uncertain “strong” and the question-marked arrows are retained as reading and proof limitations rather than normalized into a six-operation formalism.

### MPL118-M04 — Weak Serre conditions and the double-comma window

**Kind:** unproved claim. **118:** scan 009, WSC defined by `X_{/b}\to X_{/b'}` in W, and WSB by the double-comma comparison. **Context:** `context/companion/chunks/DER_XI-XIIa.tex`, XII §III, ms. 42–52; DOSSIER BISITE A.15 and B.1; Hua, modernised reading of cote 118, “Les caractérisations (page 8)”.

The one-sided comma condition, its opposite and the two-sided WSB window distinguish three claims which the early lattice says are not interchangeable. Their displayed equivalence with replacement or local-constancy conditions is largely asserted, so a proof must preserve the comma variance and the class of allowed base changes. The later hot/weak/intrinsic terminology is a comparison aid, not a literal expansion of WSC, WSF or the uncertain final letters in the manuscript.

### MPL118-M05 — Opposite-category symmetries

**Kind:** unproved claim. **118:** scan 009, `C=F^{\circ}`, `S=S^{\circ}`, `\mathrm{Sm}=\mathrm{Pr}^{\circ}`; scan 015, “Dualité (y compris …)”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, Rappel 1, ms. 1–3; DOSSIER RESIDUE B.6 and BISITE A.11.

The notes explicitly aim to make the weak-equivalence theory invariant under passage to opposites and to pair properness with smoothness. The equality W=W° is listed as a programme item, not derived from the abbreviated Loc 1–3 axioms on these pages. The later return's precise axiom package is therefore only a partial match, even where the same equation appears literally.

### MPL118-M06 — Discrete maps versus homotopical properties

**Kind:** unproved claim. **118:** scan 014, “proper discret ⇒ cofib”, “smooth discret ⇒ fibration”, and the two explicit nonimplications involving Serre. **Context:** `context/companion/chunks/DER_XI-XIIa.tex`, XII §III, ms. 26–40; `DER_VII-c.tex`, ms. 150–152, comment dgrb404; DOSSIER STRATA D.6/D.7 and PATHS E.3–E.5.

The page sharply separates a strict lifting property from a homotopical condition and says discreteness bridges the former proper/smooth distinction. No counterexample proving either Serre nonimplication is worked out on this sheet. This is useful antecedent evidence for the later path-fibration distinctions, but it is not one of those later constructions or proofs.

### MPL118-M07 — Comma factorizations are not yet Serre replacements

**Kind:** unpursued implication. **118:** scans 011–014, “Fib”, “Cofib”, and “not … yet Serre”. **Context:** `context/companion/chunks/DER_XIIc-a.tex`, §4, ms. 209–218; DOSSIER RESIDUE C.1–C.6 and BISITE C.1/C.3; Hua, modernised reading of cote 118, “Les deux factorisations par les catégories comma”.

The explicit comma-category factorizations anticipate later replacement constructions, while the handwritten warning excludes identifying them with fully homotopical or intrinsic replacements. Hua's connection with Street's free fibration is a credited modern interpretation; no universal property from Street's paper was independently checked here. The adjacent adjunction and cofibre questions remain separate items in the self-flag register.

### MPL118-M08 — Monomorphisms, sieves and cosieves

**Kind:** unproved claim. **118:** scans 012 and 014, “imm. ouvertes”, “imm. fermées”, “discrete fibration”, and “discrete cofibration”. **Context:** `context/companion/chunks/DER_I-a.tex`, ms. 49–50 and 58–59, comments dgrb25/dgrb30; `DER_XIIb-a.tex`, §V.1.1, ms. 59–61; DOSSIER STRATA D.7 and BISITE A.9.

The diagrams locate open and closed immersions among the discrete fibration/opfibration classes and distinguish them from arbitrary monomorphisms. The corrections in the table matter: treating every mono as an immersion or every immersion as a modern model cofibration would erase the distinctions used by the pushout counterexamples. The later sieve/cosieve vocabulary is explanatory only and does not replace the frozen English and French labels.

### MPL118-M09 — Weak Loc 1 and the unexpanded Loc 2–3

**Kind:** reading question. **118:** scan 015, “Loc 1 sous forme faible”, clauses a–c, and the bare names “Loc 2, Loc 3”. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, ms. 1–3; [PS], §64, manuscript pp. 164–165; RESULTS_STATE GALOIS B.1/B.3 and BISITE A.1.

The written third clause assumes gf=id as well as fg∈W, rather than stating every modern retract or saturation axiom. Loc 2 and Loc 3 are named but not expanded, so their content is inferred only from subsequent applications such as 026 and 040. Hua's expanded axioms are a useful reconstruction which must remain outside the transcription and outside any claim that all modern axioms were explicitly stated here.

### MPL118-M10 — Functoriality of the span integral

**Kind:** unproved claim. **118:** scan 015, “Fonctorialité si … dans … W”, the isomorphism-leg homotopism assertion and the weak-equivalence-leg corollary. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, Proposition 1.3, ms. 3–8; RESULTS_STATE POLES B.2; Hua, modernised reading of cote 118, “Le programme (pages 14 et 15)”.

These are forward invariance claims for the Grothendieck construction of a span, and the page does not give their complete proof. Under a relative localizer they are consistent with the fibrewise integral mechanism used in C02. Their relation to Thomason's homotopy-colimit theorem is credited to Hua; the 1979 bibliographic record was located, but the full proof of that theorem was not audited here.

### MPL118-M11 — The empty-or-point complementary fibre condition

**Kind:** unproved claim. **118:** scan 015 margin, “l'une … soit ∅, l'autre … isom. à Δ₀” and “cocartésien … tt chgt de base”. **Context:** `context/companion/chunks/DER_XIIb-b.tex`, §V, ms. 147–149; DOSSIER BISITE B.5/B.6; Hua, modernised reading of cote 118, “Le programme (pages 14 et 15)”.

This margin strengthens the fibre hypothesis to a complementary empty/point condition and then asserts a strict pushout stable under every base change. That condition should not be confused with 021's weaker “one fibre is the point” comparison theorem. The later gluing passage is a nearby counterpart, while the strict universal pushout assertion on 015 is not independently proved in this run.

### MPL118-M12 — Presheaf pushouts and categories of elements

**Kind:** unproved claim. **118:** scans 015 and 022, the mono pushout, “cartésien et cocartésien”, and the two W_A preservation implications. **Context:** `context/companion/chunks/DER_XIIb-b.tex`, §V, ms. 147–149; `DER_XVI.tex`, §2; DOSSIER RESIDUE B.10 and BISITE B.5/B.6.

The presheaf assertion is deliberately stronger than the unrestricted Cat statement, because the category-of-elements image carries the additional discrete lifting structure used on 021–022. The notes also use preservation of colimits and fibre products by i_A, which should be understood with the canonical categories of elements and their projections. A modern model-category identification is not required by the handwritten argument, and none is silently inserted.

### MPL118-M13 — The open–closed gluing bifunctor

**Kind:** unpursued implication. **118:** scan 017, `H_X:U^\circ\times Y\longrightarrow(\mathrm{Ens})` and the cross-arrow family into Hom_Z. **Context:** `context/companion/chunks/DER_XIIb-a.tex`, §V.1.1, ms. 59–61, Proposition 1/comment dgrb507; README's STRATA C.1 planning lead; DOSSIER STRATA D.1/D.2 and RESIDUE I.5; Hua, modernised reading of cote 118, “Le sorite des recollements (page 16)”.

The page explicitly records the cross-arrow bifunctor needed to reconstruct a category from its open and closed pieces, so the plan's bimodule/collage lead does have an occurrence in 118. Hua's identification as a profunctor collage is credited to him, and the later Proposition 1 supplies the matching contextual language. This evidence does not supply the enhanced stratification or cohomological gluing theorems bundled into the dossier's later rows.

### MPL118-M14 — Gluing functors and homotopies

**Kind:** unproved claim. **118:** scan 017, “stable par produits” and the homotopy-preserving gluing observations. **Context:** `context/companion/chunks/DER_XIIb-a.tex`, §V.1.1, ms. 59–61; DOSSIER RESIDUE I.5; Hua, modernised reading of cote 118, “Le sorite des recollements (page 16)”.

The sheet sketches how functors preserving the open–closed decomposition are described by their restrictions plus compatible cross-arrow maps. Its assertion that the construction respects products and homotopies is not accompanied by all coherence checks. These are ordinary categorical gluing data, not yet recollement of derived categories or a six-functor formalism.

### MPL118-M15 — Fractions and the changing handedness

**Kind:** reading question. **118:** scans 015 and 024, “calcul des fractions à gauche”; scan 027, “calcul des fractions à droite”. **Context:** `context/companion/chunks/DER_XIIc-a.tex`, ms. 228–229, comment dgrb607, referring to §V Definition 2(c), ms. 109–110; DOSSIER PATHS B.5/D.8/D.17; Hua, modernised reading of cote 118, “La catégorie homotopique comme catégorie de fractions (pages 23 à 25)”.

The change of word is literal and has not been harmonized after the fact. The displayed roofs and common weak targets need to determine the intended orientation before using the general finite-colimit lemma or the saturation proof. The supplied later rectification results remain background analogies and do not fill the missing Cat argument merely because both use fractions.

### MPL118-M16 — The abstract factorization and interval axioms

**Kind:** unproved claim. **118:** scan 025, conditions (i)–(iv), especially the factorization through a homotopism and the endpoint map `X\amalg X\longrightarrow X\times I_\alpha`. **Context:** `context/companion/chunks/DER_XIIc-a.tex`, ms. 228–229, comment dgrb607; DOSSIER PATHS D.8/D.17; Hua, modernised reading of cote 118, “La catégorie homotopique comme catégorie de fractions (pages 23 à 25)”.

The sheet extracts a finite list of hypotheses sufficient for its fraction-calculus strategy, but their verification in each intended category is not completed. Hua's analogy with Brown's categories of fibrant objects, after duality, is useful and credited; the full content of Brown's paper was not independently checked here. In particular, an analogy of axioms does not establish the later intrinsic-cofibration or inverse-diagram rectification theorems.

### MPL118-M17 — Passing first to homotopisms

**Kind:** unproved claim. **118:** scan 025 margin, the comparison `W^{-1}M=\overline W^{-1}\overline M`. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, homotopism discussion, ms. 3–8; DOSSIER RESIDUE B.5/B.7; Hua, modernised reading of cote 118, “La catégorie homotopique comme catégorie de fractions (pages 23 à 25)”.

This formal localization comparison depends on every homotopism being in W, a compatibility assumption the margin explicitly includes. It does not say that the quotient by homotopy already inverts every weak equivalence. The difference becomes essential for the infinite-coproduct discussion on 029–031.

### MPL118-M18 — Coproduct closure uses the common-base axiom

**Kind:** unpursued implication. **118:** scan 026, “Cela résulte alors de loc. 3” and the triangle to J. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, Loc (3 bis), and §2, ms. 9–10; DOSSIER RESIDUE B.8/B.11/B.12; RESULTS_STATE GALOIS B.3.

For a discrete base J the displayed local slices are precisely the separate summands, so this is direct evidence that a relative version of the local axiom is being used. It establishes the forward sum closure needed by the manuscript's strategy, not reflection of membership in W from a coproduct to each summand. The latter distinction is exactly what matters to the W_ne qualification in C11.

### MPL118-M19 — Finite coproducts after localization

**Kind:** unproved claim. **118:** scan 027, “les sommes directes finies existent” and the general lemma about finite colimits under fractions. **Context:** `context/companion/chunks/DER_XVI.tex`, §2, ms. 9–10; DOSSIER RESIDUE B.12; Hua, modernised reading of cote 118, “Les sommes dans Hot (pages 26 à 30)”.

The finite conclusion is supported by the common-target fraction method and the finite-homotopy synchronization on the next page. The arbitrary-finite-colimit lemma is stated more broadly than the application and still requires the appropriate handedness and existence assumptions. The margin removing “finies” is an expectation whose later difficulties are explicitly recorded, not a completed infinite version of this proof.

### MPL118-M20 — The finite synchronization mechanism

**Kind:** unpursued implication. **118:** scan 028, “un … intervalle” and “N assez grand pour convenir pour tous les j”. **Context:** `context/companion/chunks/DER_XIII-a.tex`, ms. 55–56, comment dgrb709; DOSSIER PATHS D.16; Hua, modernised reading of cote 118, “Les sommes dans Hot (pages 26 à 30)”.

The proof uses finiteness exactly to bound the number of elementary homotopies uniformly across the summands. Scan 029 isolates the failure of that bound for an infinite family, anticipating the mechanism of the later bounded-zigzag obstruction. It does not contain the later circle-poset or Kaledin comparison theorem.

### MPL118-M21 — The common weak target lemma is a missing ingredient

**Kind:** unproved claim. **118:** scan 031, “une … famille d'équivs. faibles” and the proposed common `Y\xrightarrow{\alpha}Y'`. **Context:** `context/companion/chunks/DER_XVI.tex`, §2, ms. 9–10; `DER_XIII-a.tex`, ms. 55–56; DOSSIER RESIDUE B.12 and PATHS D.16/D.17.

The common-target lemma would synchronize representatives of maps in the localization, but its proof depends on the weak-equivalence behavior of the proposed amalgams and their passage to a limit. The generic open/closed pushout failures on 023 mean those steps cannot be justified by unrestricted immersion gluing alone. The following Kan-type warning further separates synchronization of representatives from synchronization of homotopies.

### MPL118-M22 — The finite-product corollary and its target category

**Kind:** reading question. **118:** scans 032–035, “Corollaire 2”, “A catégorie test stricte”, and the margin “il suffit … tot. … asph.”. **Context:** RESULTS_STATE 118-product-condition-iv and 118-groupoid-products-not-totally-aspherical; Hua, modernised reading of cote 118, “Les produits finis (pages 31 à 36)”; [MALT-2020], §1.7.

The manuscript progressively separates preservation into Hot_A from preservation by the category-of-elements functor into Hot(W). Its provisional repeated Hot_A on 033 and the explicit Hot(W) on 035 must not be flattened into one identical condition. Total asphericity is a sufficient weakening of strict testness for the product comparison, but product stability of W_A alone has the groupoid obstruction in C04.

### MPL118-M23 — Representable tests for product stability

**Kind:** unproved claim. **118:** scan 034, “pour ceci il suffit de le voir pour Z dans A”. **Context:** `context/companion/chunks/DER_XVI.tex`, relative Loc (3 bis), ms. 3–8; [MALT-2020], §1.7; RESULTS_STATE 118-product-condition-iv.

This reduction uses local testing over the category of elements of Z, so it should not be justified merely by saying every presheaf is a colimit of representables. The manuscript's asphericity hypothesis makes the projection comparisons weak equivalences and supplies the proposed argument. The needed relative/local mechanism is part of the hypothesis tracking, not an automatic consequence of arbitrary colimit preservation by W.

### MPL118-M24 — The corrected converse with asphericity

**Kind:** unpursued implication. **118:** scan 034, “si A asph, alors (ii bis) … (i)” and “prendre f:a→e”. **Context:** RESULTS_STATE 118-groupoid-products-not-totally-aspherical and 118-product-condition-iv; Hua, modernised reading of cote 118, “Le lemme des pages 32 à 35”; [MALT-2020], §1.7.

The added asphericity hypothesis is essential to this converse and is not refuted by the nontrivial-group example on 036. The proposed test uses the representable-to-terminal maps, which are in W_A when A is aspherical, and then multiplies them by representables. This is a materially different statement from the later unsupported replacement of asphericity by connectedness.

### MPL118-M25 — Finite products directly in Cat

**Kind:** unproved claim. **118:** scan 036, “marche directement dans (Cat)” because a finite product of W-maps lies in W. **Context:** `context/companion/chunks/DER_XVI.tex`, §2, Proposition 2.5, ms. 10; DOSSIER RESIDUE B.8; RESULTS_STATE GALOIS B.3.

The closure assertion is compatible with the relative localizer framework used elsewhere on these pages, but is not justified here from an explicitly written axiom list. The later absolute/relative separation in RESIDUE B.8 prevents exporting it to every class satisfying only literal absolute Theorem A. Its extension to infinite products is separately questioned and answered negatively for strict W∞ products by the supplied example in C06.

### MPL118-M26 — The presheaf filtration corollary

**Kind:** unproved claim. **118:** scan 040, “Idem dans un … A”, using i_A and arbitrary colimits and fibre products. **Context:** `context/companion/chunks/DER_XVI.tex`, §1, ms. 3–8; Hua, modernised reading of cote 118, “Filtrations (pages 38 et 39)”; DOSSIER RESIDUE B.10.

The intended transfer follows the category-of-elements functor, but the hypotheses on intersections and minimum stages still need to survive that transfer. The corrected Cat argument C03 must be used before claiming the corollary follows from the displayed strict triangle. No unrestricted theorem about all presheaf covers or all filtered colimits is inferred from this short assertion.

### MPL118-M27 — A sharp-map analogy with a precise quantifier

**Kind:** unpursued implication. **118:** scan 009, S preserves every weak arrow between objects over Y under pullback. **Context:** Hua, modernised reading of cote 118, “Les caractérisations (page 8)”; [REZK], §2, Definition of sharp maps; DOSSIER BISITE A.2/A.15.

Hua's comparison with Rezk's sharp maps is supported by the same arbitrary-over-base pullback quantifier, which was checked in Rezk's primary text. The later name and the model-category setting belong to the comparison, not to Grothendieck's wording. Rezk's higher-simplex tests also do not by themselves resolve the handwritten question about testing only Δ₁ base changes.

### MPL118-M28 — Dwyer maps as a repair, with a scope boundary

**Kind:** unpursued implication. **118:** scan 023, “Il n'est pas vrai dans Cat”. **Context:** Hua, modernised reading of cote 118, “Mais attention”; [THOM-1980], Definition 4.1 and Proposition 4.3; RESULTS_STATE TOTASPH F.27 and DOSSIER RESIDUE F.6.

Hua correctly points toward strengthening the immersion class rather than treating every ordinary pushout as homotopical. Dwyer maps are the credited later comparison, while the separate open problem about their composition recorded in TOTASPH F.27/RESIDUE F.6 is not solved by anything in 118. This note does not claim the full theorem or that open item was re-proved here.

### MPL118-M29 — Conflicting return bookkeeping remains visible

**Kind:** reading question. **118:** scans 039–040 are the nearest filtration material, not an occurrence of the later comparison theorem. **Context:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P3; `context/notes/RESULTS_STATE.md`, CATHOT E.26.

PATHS C.P3 claims that the three CATHOT E.26 comparisons are settled, while the supplied RESULTS_STATE entry still calls CATHOT E.26 open. Both statuses are preserved as source claims in the mapping. The 118 filtration argument neither adjudicates that discrepancy nor supplies the omitted proofs.



# MPL 118 — STRATA and PATHS statement mapping

**Author:** GPT-6 Astra Pro. **Effort:** inherited/not exposed. **Generated:** 2026-11-18T03:18:09+00:00.

This appendix covers all **10 STRATA + 76 PATHS** rows of the supplied dossier against the frozen 118 transcription. Every supplied status remains the originating run’s claim. This work compares texts and definitions; it does not validate proofs or resolve the modern results.

The frozen transcription was read in full, as were `context/README.md` and `context/notes/RESULTS_STATE.md`. Relevant companion and Pursuing Stacks passages are identified below. No images, OCR, manuscript edits, or renewed transcription were used.

## Coverage and interpretation

| Relation | Count |
|---|---:|
| exact | 0 |
| partial | 3 |
| analogue | 10 |
| absent | 73 |
| contradicted | 0 |

**Absent** means no form on the supplied 118 pages; any evidence under an absent row is explicitly **nearest related only**. An **analogue** shares a construction, distinction, or method; a **partial** match identifies a substantive part but not the whole statement. No row is classified exact or contradicted.

The note kind **reading question** denotes the comparison question here, not an attribution of a question to Grothendieck. Confidence on an **own idea** concerns the textual analogy alone. Each comparison note has one to four sentences.

## Material findings

- **STRATA D.3, STRATA D.4, STRATA D.7:** The proper-lift criterion, proper/smooth base-change table, and sufficient open/closed inclusion directions have partial forms on scan009 and scan012.
  Context: `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100).; `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294).; `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085).; `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790).
- **STRATA D.6, PATHS E.3, PATHS E.4, PATHS E.5:** Scan014 explicitly separates proper/smooth Serre properties from strict categorical cofibration/fibration; scans011–012 provide comma replacements with a stated not-yet-Serre limitation, not the later endpoint models.
  Context: `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280).; `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790).
- **PATHS D.16:** Scan029 explicitly identifies unbounded lengths of elementary homotopies in an infinite family; this supports a close analogy with the later bounded-winding obstruction, without supplying its circle-poset or Kaledin claims.
  Context: `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253).
- **PATHS B.5, PATHS D.8, PATHS D.17:** Scans024–026 give finite factorization/pushout/interval conditions for left fractions; they do not state the later intrinsic cofibration axioms or rectification theorems.
  Context: `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045).; `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565).
- **STRATA G.2, PATHS A.5, PATHS A.6, PATHS A.7, PATHS E.12:** The product/diagonal usage of total asphericity on scans033–036 must not be identified with the later all-outgoing-functors definition; XII §V.2.3, Definition1, ms.88–89 contains an explicit terminology warning.
  Context: `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197).
- **PATHS C.P3:** The dossier claims that the CATHOT E.26 comparisons are settled, while RESULTS_STATE still labels CATHOT E.26 Open; this is a supplied-record status tension, not a mathematical adjudication from 118.
  Context: `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837).

## Statement-by-statement comparison

### STRATA D.1 — Exceptional adjunction chains and support images

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A pointed Der 1–4 presheaf derivator has the exceptional adjunction chains j^? ⊣ j_! ⊣ j^* ⊣ j_* and i_! ⊣ i^* ⊣ i_* ⊣ i^!, with the stated support images.

**Supplied locator:** I ms.1–9; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 15.

**Comparison note:** No form of the pointed-derivator adjunction chains is stated on the supplied 118 pages. The nearest material is the open–closed decomposition and its bifunctor H_X on scan017, which concerns ordinary categories and gives neither j^? nor i^! or their support images.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.50–52, dgrb26, Fully faithful direct image and extension by a terminal object (file lines 1992–2050). Supplied text and AI commentary; no proof validation.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA D.2 — Coherent support sequences and stable recollement

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed derivators have coherent support fibre/cofiber sequences and the bicartesian open-closed square; stable strong derivators have the associated triangulated recollement.

**Supplied locator:** I ms.2–9; Lead 4 exactness clauses. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 16.

**Comparison note:** No fibre/cofibre support sequence or stable triangulated recollement appears on the supplied 118 pages. Scan017 supplies category-gluing data, while scans019–023 discuss categorical pushout comparisons; neither is a statement about a pointed derivator’s coherent support square.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**Nearest related only — 118 scan021, fragment line 22:**

```tex
Ce foncteur est une cofibration, à fibres les
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.50–52, dgrb26, Fully faithful direct image and extension by a terminal object (file lines 1992–2050). Supplied text and AI commentary; no proof validation.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA D.3 — Proper and smooth poset maps via exact lifts

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** A poset map is W_infinity-proper exactly when all outgoing exact lifting posets are weakly contractible, and smooth exactly when all incoming ones are weakly contractible.

**Supplied locator:** I ms.53–56; Lead 4 map classification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 17.

**Comparison note:** Scan009 explicitly puts properness in equivalence with asphericity of the category of lifts of a base arrow with prescribed source, so the proper half of the later lift criterion has an identifiable categorical form here. The smooth column is largely left blank and the finite-poset specialization is not separately formulated; the fuller poset statement is in Pursuing Stacks §137.

**Manuscript evidence — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.4 — Proper/smooth strict base change and detection

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** Strict-pullback right base change holds if the vertical functor is proper or the base-change functor smooth; left base change has the dual conditions, and universal space-valued tests detect them.

**Supplied locator:** I ms.49–59; VI ms.162–169; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 18.

**Comparison note:** Scan009 links properness to commutation of R^i f_* with arbitrary base change and places the smooth base-change criterion in the parallel column. It does not state the complete derivator-level dual mate theorem or detection by universal space-valued tests, and its extra implication toward preservation of weak equivalences is marked with a question.

**Manuscript evidence — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**Manuscript evidence — 118 scan009, fragment line 15:**

```tex
\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449); **BISITE A.19** (Proved (the return's claim); line 381); **GALOIS D.2** (Proved (the return's claim); line 392).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.5 — Failure of naive geometric characterizations

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Topological properness, strict-versus-homotopy-fibre comparison, or stratified local product structure characterize categorical properness and smoothness for finite posets.

**Supplied locator:** Ib-C003; I ms.53–59; GALOIS D.9; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 19.

**Comparison note:** No form of the claimed finite-poset counterexamples to the proposed geometric characterizations occurs on the supplied 118 pages. Scan009 supplies categorical lift and base-change criteria, but no comparison with topological properness or a stratified local product structure.

**Nearest related only — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.6 — Diamond: smooth/proper without opfibration or bundle

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The four-object diamond map to [1] is proper and smooth and a Grothendieck fibration, but is neither an opfibration nor a locally trivial topological fibre bundle.

**Supplied locator:** VIc-C008 strictness comparison; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 20.

**Comparison note:** Own comparison: scan014 explicitly distinguishes proper Serre maps from cofibrations and smooth Serre maps from fibrations, anticipating the need to separate homotopical and strict lifting properties. The four-object diamond and the bundle assertion are absent, so this is a shared distinction rather than the dossier’s example.

**Confidence in this own comparison:** high — The nonimplications are explicit; no identification of a particular witness is made.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.7 — Poset inclusions, projections, and image conditions

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** Full poset inclusions are proper precisely for cosieves and smooth precisely for sieves; product projections have both properties and images obey the stated component conditions.

**Supplied locator:** I ms.54–56; Lead 4 examples and edge cases. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 21.

**Comparison note:** The diagrams in scans009 and012 place open immersions among fibrations and closed immersions among cofibrations, with F⇒Sm and C⇒Pr recorded explicitly. This supplies the sufficient inclusion direction, but not the full necessity statement for poset inclusions, the product-projection assertion, or the stated image conditions.

**Manuscript evidence — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**Manuscript evidence — 118 scan012, fragment line 43:**

```tex
\text{open immersions}\longleftrightarrow X^\circ\xrightarrow{\varphi}\Delta^1=[0\longrightarrow1]
```

**Manuscript evidence — 118 scan012, fragment line 49:**

```tex
\text{Closed immersions}\longleftrightarrow X\xrightarrow{\varphi}\Delta^1
```

**RESULTS_STATE links:** **STRATA 0.1** (Proved (the return's claim); line 400); **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.8 — Finite-poset coefficient dictionary and geometric base change

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The finite-poset coefficient dictionary transports intrinsic base change; closed inclusions and finite product projections admit the specified ambient geometric interpretation, while arbitrary monotone maps do not.

**Supplied locator:** Lead 4 constructible base-change comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 22.

**Comparison note:** No form of the finite-poset constructible-coefficient dictionary or its ambient geometric comparison is given on the supplied 118 pages. The nearest item is the categorical proper/smooth base-change table on scan009, without a stratified geometric realization or constructible coefficients.

**Nearest related only — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**RESULTS_STATE links:** **STRATA A.4** (Proved (the return's claim); line 378); **BISITE G.10** (Proved (the return's claim); line 385); **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.9 — Slice-target and specialization-order corrections

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The smoothness fibre-inclusion target at I ms.54 is y\X; with downsets open, the compatible closure formula at XII ms.59 is y in closure{x} when x<=y.

**Supplied locator:** I ms.54; XII ms.59. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 23.

**Comparison note:** The two corrections refer to different manuscripts, I ms.54 and XII ms.59, and neither corrected formula is stated as such on the supplied 118 pages. Scan009 contains related comma-category notation with marked reading doubts, but that does not authorize importing the later correction into its frozen text.

**Nearest related only — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **STRATA 0.1** (Proved (the return's claim); line 400).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA G.2 — Later totality and universal simplicial colimits

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Total W-infinity asphericity is exactly the canonical homotopy-colimit to strict-colimit equivalence for every simplicial diagram on a connected base.

**Supplied locator:** XII ms.88–89; TOTASPHB.11. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 24.

**Comparison note:** No form of the universal simplicial homotopy-colimit/strict-colimit criterion occurs on the supplied 118 pages. Scans033–036 use total asphericity in the product/diagonal sense, whereas XII §2.3 Definition1 at ms.88–89 quantifies over all outgoing functors and expressly warns that its notion differs from Pursuing Stacks, so the shared term is not a match.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**Nearest related only — 118 scan035, fragment line 12:**

```tex
(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}
```

**RESULTS_STATE links:** **TOTASPH A.2** (Known (the return's claim); line 404); **TOTASPH A.7** (Known (the return's claim); line 405); **TOTASPH C.10** (Refuted (the return's claim); line 408); **TOTASPH D.7** (Open (the return's claim); line 353).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.P1 — Path components recover localized Hom

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path-category component set is the ordinary localized Hom-set, naturally and compatibly with composition.

**Supplied locator:** VII ms.65–74. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 32.

**Comparison note:** No form of the full path-category component theorem is stated on the supplied 118 pages. Scan024 gives a left-fraction calculus after quotienting by interval homotopy, but it neither defines the all-type path category nor identifies its component set.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS A.P2 — Sequential path model and Grothendieck roof

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The exact sequential model is connected to the all-type category by the specified fibred Grothendieck roof; both legs are weak equivalences for preorder-cofinal path sequences.

**Supplied locator:** VII ms.99–110. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 33.

**Comparison note:** No all-type/sequential path roof occurs on the supplied 118 pages. The sequential system in scan041 is a chain of open immersions used for saturation, not a cofinal sequence of path types.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.1 — Fibred/opfibred comparison span

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The fibred and opfibred Grothendieck constructions give the specified span C <- C_u -> C_infinity; no general direct C -> C_infinity functor is supplied.

**Supplied locator:** VII ms.99-110; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 34.

**Comparison note:** No form of the span C←C_u→C_infinity or its missing direct comparison is given on the supplied 118 pages. The Fib(f) factorizations of scans011–014 are different constructions and do not supply that span.

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.2 — Filtered Cat-colimit comparison

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** For every filtered indexing category A and every D:A->Cat, the canonical Grothendieck-total-category to Cat-colimit functor is a weak equivalence; the sequential fibred version follows by opposites.

**Supplied locator:** VII ms.108-109; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 35.

**Comparison note:** Own comparison: scans039–040 give an argument for invariance of specified unions of open or closed subcategories by asserting an identification of stage maps with comma maps and invoking L3. The strict-triangle step has the lax-commutation gap addressed by the separate repair in MPL118-C03. This restricted passage-to-the-limit argument does not assert that every filtered Cat-diagram has its Grothendieck total category weakly equivalent to its strict colimit.

**Confidence in this own comparison:** high — The union hypotheses and L3 conclusion are explicit; no universal filtered-diagram conclusion is inferred.

**Manuscript evidence — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.565–567, discussion of Thomason’s total-category description of integration (file lines 516–615). Supplied Pursuing Stacks text; no theorem attributed to 118 from this separate source.

### PATHS A.3 — Cofinal base functors detected by all fibred diagrams

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** A base functor u:J->T induces weak equivalences of fibred total categories for every strict F:T^op->Cat iff every u/t is weakly contractible.

**Supplied locator:** VII ms.99-110; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 36.

**Comparison note:** Own comparison: the asserted comma-map identification and appeal to L3 on scan040 exhibit the same intended fibrewise-to-total method used in the dossier’s base-change criterion. The strict-triangle step needs the separate lax-commutation repair in MPL118-C03, and the universal quantification over all F and converse characterization of u/t are absent from 118.

**Confidence in this own comparison:** medium — The common method is explicit, but the quantified theorem and its converse are not stated.

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **GALOIS B.3** (Proved (the return's claim); line 377).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.4 — Preorder cofinality does not suffice

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Preorder cofinality plus homotopy of parallel reindexing maps does not imply the total/sequential comparison is a weak equivalence.

**Supplied locator:** VII ms.99-109; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 37.

**Comparison note:** No form of the counterexample combining preorder cofinality with homotopic reindexing maps occurs on the supplied 118 pages. The ordered-index filtration theorem on scans039–040 adds infimum and intersection hypotheses and does not discuss discarded parallel-arrow information.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.5 — Delta_inj: totality does not ensure Cat-colimit correctness

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Total W_infinity-asphericity of A does not make every Cat-valued colimit homotopically correct: for Delta_inj and D([n])=B N^(n+1), the total category has integral H_k=Z in every degree whereas the Cat colimit has type S1.

**Supplied locator:** After TOTASPH correction; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 38.

**Comparison note:** The Delta_inj diagram and its integral-homology versus circle calculation have no form on the supplied 118 pages. The total-asphericity discussion in scans033–036 is about products of representables, not the later universally quantified totality used by this row.

**Nearest related only — 118 scan035, fragment line 12:**

```tex
(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}
```

**RESULTS_STATE links:** **TOTASPH C.10** (Refuted (the return's claim); line 408); **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.
- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.6 — Delta_inj is exact and total but not filtered

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Delta_inj has exact abelian-group-valued colimits and is totally W_infinity-aspherical but is not filtered.

**Supplied locator:** TOTASPH C.7-C.10 verification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 39.

**Comparison note:** No Delta_inj example, exactness of abelian-group colimits, or totality-versus-filteredness theorem occurs on the supplied 118 pages. The similarly named condition on scans033–036 belongs to the earlier product/diagonal terminology and cannot be substituted for the dossier’s totality hypothesis.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **TOTASPH C.10** (Refuted (the return's claim); line 408); **PRETOT A.12** (Proved (the return's claim); line 398); **RESIDUE F.3** (Proved (the return's claim); line 399).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.7 — Filtered, correct-Cat-colimit, and total shape classes

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For nonempty connected shapes, filtered categories are contained in the universally correct Cat-colimit shapes, which are strictly contained in the totally W_infinity-aspherical shapes.

**Supplied locator:** Part A; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 40.

**Comparison note:** No form of this chain of shape classes or its strictness assertion appears on the supplied 118 pages. Scans039–040 treat special filtrations, and scans033–036 concern a different total-asphericity notion, so neither gives the requested classification.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351); **TOTASPH C.10** (Refuted (the return's claim); line 408).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.8 — Open classification of universally correct Cat-colimit shapes

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An exact intrinsic classification of universally correct Cat-colimit shapes, including whether all connected such shapes are filtered, remains unresolved here.

**Supplied locator:** Part A. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 41.

**Comparison note:** The supplied 118 pages do not formulate or settle the intrinsic classification of universally correct Cat-colimit shapes. Their passage-to-the-limit theorem applies to the specific open/closed filtrations of scans039–040 and does not test arbitrary Cat-valued diagrams.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.9 — Finite weak equivalence without categorical homotopy inverse

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The last-element map sd P->P for the six-face triangle-boundary poset is a weak equivalence with no inverse modulo zigzags of natural transformations; all 456 reverse monotone maps have degree zero.

**Supplied locator:** POLES D.6 verification; VIIc-A046; V-I066. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 42.

**Comparison note:** The subdivision map of the triangle-boundary face poset and the enumeration of 456 reverse maps have no form on the supplied 118 pages. Scans029–031 distinguish interval homotopy from localization by a different, infinite-family obstruction.

**Nearest related only — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS B.1 — Full and weak-vertical path diagrams

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full and weak-vertical path diagrams and their literal inclusion are well-defined and strictly compatible with concatenation.

**Supplied locator:** VII ms.27–78. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 43.

**Comparison note:** No full/weak-vertical path diagram or concatenation-compatible inclusion is defined on the supplied 118 pages. Scan024’s fraction calculus is the nearest localization discussion, without marked internal vertical arrows.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.2 — Restricted paths and hammock localization

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The restricted all-type Grothendieck nerve maps weakly equivalently to the hammock mapping simplicial set by a strict composition-compatible reduction.

**Supplied locator:** Lead1 weak-vertical identification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 44.

**Comparison note:** No hammock mapping simplicial set or restricted all-type comparison occurs on the supplied 118 pages. The fraction calculus on scan024 does not provide the stronger composition-compatible nerve comparison.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.3 — Full/restricted inclusion need not be an isomorphism

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The inclusion J need not be an isomorphism of categories, even when the marking is saturated.

**Supplied locator:** Lead1 forcing claim. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 45.

**Comparison note:** No form of the inclusion J or its counterexample occurs on the supplied 118 pages. Strong saturation is stated on scan040, but saturation alone is not an occurrence of a theorem about J.

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.4 — Extreme markings make J a weak equivalence

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If Sigma is contained in the isomorphisms, the full all-type category is discrete in Cat hot and J is a weak equivalence; if all arrows are marked J is the identity.

**Supplied locator:** Lead2. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 46.

**Comparison note:** No statement about the markings consisting of isomorphisms or all arrows, or the resulting path inclusion J, occurs on the supplied 118 pages. The ordinary localization formula on scan024 does not specialize an all-type path construction.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.5 — Homotopy fraction calculi on the restricted side

**Supplied status:** claim (return: Known). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Homotopy fraction calculi identify the restricted short-fraction categories; two-out-of-three forces their vertical arrows marked.

**Supplied locator:** Part B HCF/model/fibrant-object sufficient statements on restricted side. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 47.

**Comparison note:** Own comparison: scans024–026 develop a left-fraction calculus from factorization, pushout stability, and separating intervals, making a concrete precursor to short-fraction methods. They do not identify restricted path categories or use two-out-of-three to force hammock vertical arrows to be marked.

**Confidence in this own comparison:** high — A fraction calculus and its hypotheses are explicit; the comparison is methodological, not an identification of path models.

**Manuscript evidence — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS B.6 — Full path comparison split monic in Hot

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path space maps coherently to the localization mapping space; its composite with J is the hammock comparison, so J is split monic in Hot.

**Supplied locator:** VII ms.68–70;PartB partial comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 48.

**Comparison note:** No coherent full-path map, hammock composite, or split monomorphism J in Hot occurs on the supplied 118 pages. Their localization discussion concerns ordinary fraction representatives rather than localization mapping spaces.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.7 — Grid-sweep padding of a backward square

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An arbitrary backward commuting square becomes a weak-vertical hammock between mixed boundary paths after identity padding.

**Supplied locator:** PartB grid-sweep reduction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 49.

**Comparison note:** No grid-sweep reduction of an arbitrary backward square to a weak-vertical hammock appears on the supplied 118 pages. The common finite interval used in scan028 serves a coproduct homotopy argument and has no marked-hammock interpretation there.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.8 — Open unrestricted-vertical path comparison

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Whether J is always a weak equivalence, including wide/two-out-of-three/saturated/HCF/model/Brown variants beyond B.4.

**Supplied locator:** PartB central unrestricted-vertical comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 50.

**Comparison note:** The general weak-equivalence question for J is not formulated or settled on the supplied 118 pages. Fraction calculus after homotopy quotienting, as on scan024, does not itself answer the full-versus-restricted path comparison.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.9 — Bounded finite search on path comparisons

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All 132 bounded full/restricted path-category comparisons in the specified finite search have equal H0 and H1 over F2.

**Supplied locator:** PartB requested finite search. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 51.

**Comparison note:** The 132 finite comparisons and their F2 homology calculations have no form on the supplied 118 pages. No finite computational search or numerical path-category homology table occurs in this manuscript.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.P1 — Contractible type-map categories and enriched composition

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The category of increasing endpoint-preserving maps between two types is empty or categorically contractible and supports strict enriched composition.

**Supplied locator:** VII ms.86–94. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 52.

**Comparison note:** No category of endpoint-preserving maps between path types or strict enriched composition is constructed on the supplied 118 pages. The finite interval synchronization on scan028 concerns homotopies of maps from a coproduct, not the category of interval types.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.P2 — Reachability-preorder descent of full paths

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path-space diagram descends coherently to the reachability preorder; both the ordinary type index and any preorder-cofinal sequence are homotopy final there.

**Supplied locator:** VII ms.99–123. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 53.

**Comparison note:** No full-path diagram over a reachability preorder or comparison with a cofinal type sequence occurs on the supplied 118 pages. The ordered filtration index of scans039–040 is an unrelated construction with explicit infimum assumptions.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.P3 — Three CATHOT E.26 comparisons claimed settled

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All three specified general comparisons in CATHOT E.26 hold for arbitrary wide markings.

**Supplied locator:** CATHOT E.26(1),(2),(3);VIIc-A046 in Hot;V-I066 in Hot. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 54.

**Comparison note:** None of the three general path-type comparisons is stated on the supplied 118 pages. The dossier labels this PATHS row Proved while RESULTS_STATE still lists CATHOT E.26 as Open; both are supplied run statuses, and the filtration argument of scans039–040 does not adjudicate them.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.P4 — Mixed-sign padding and block-independent composition

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Every block containing both signs gives weak padding maps, the canonical associative unital composition in Hot, and block-independent operations.

**Supplied locator:** CATHOT E.27;IX-037 raw path composition;VII ms.125–127. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 55.

**Comparison note:** No mixed-sign block theorem or canonical associative path composition is stated on the supplied 118 pages. Scan028 uses a common interval for finitely many homotopies but contains no block-independent multiplication in Hot.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.P5 — Four-object crown defeats Cat-hot invertibility

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The actual q_L need not be invertible in Cat hot, already for a four-object crown with all arrows marked.

**Supplied locator:** VIIc-A046 in Cat hot;V-I066 strong independence inference. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 56.

**Comparison note:** The map q_L and its four-object crown counterexample have no form on the supplied 118 pages. The warning about nonuniform homotopy lengths in scan029 concerns infinite coproducts rather than this finite comparison.

**Nearest related only — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.1 — All-type Cat enrichment, nerves, and Segal model

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The raw all-type path categories form a strictly unital associative Cat-enrichment; their nerves and product-preserving Kan replacements give a simplicial category and a Segal model.

**Supplied locator:** IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 57.

**Comparison note:** No all-type Cat-enrichment, product-preserving Kan replacement, or Segal model is constructed on the supplied 118 pages. The tentative Kan-type condition mentioned on scan031 concerns a common target for fraction representatives, not enrichment.

**Nearest related only — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.2 — Weak-vertical hammocks model simplicial localization

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Weak-vertical hammocks give a composition-compatible model of simplicial localization; this theorem alone does not replace arbitrary vertical arrows.

**Supplied locator:** IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 58.

**Comparison note:** No weak-vertical hammock model or simplicial-localization theorem occurs on the supplied 118 pages. Scan024 concerns an ordinary category of fractions, a weaker and different level of structure.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.3 — Pointed Cartesian composition versus smash units

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed Cartesian composition cannot give the intended zero-preserving units unless identities equal zero; smash composition has the correct unit S0.

**Supplied locator:** IX-044; IX-049. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 59.

**Comparison note:** The zero-preserving Cartesian-composition obstruction and smash-unit S0 statement have no form on the supplied 118 pages. Their finite-product discussion concerns Hot and presheaf localizations, without pointed mapping objects or absorbing zeros.

**Nearest related only — 118 scan032, fragment line 3:**

```tex
les produits finis existent
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.4 — Pointed simplicial mapping spaces with strict zero

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Cofibrant-fibrant objects in a pointed simplicial model category supply Kan mapping spaces with strict absorbing zero, smash composition, and S0-units.

**Supplied locator:** IX-044; IX-049; IX-052. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 60.

**Comparison note:** No pointed simplicial model category, cofibrant-fibrant mapping space, strict absorbing zero, or smash composition occurs on the supplied 118 pages. The word cofibration in the early classification tables denotes categorical opfibration, so it does not supply this model-categorical result.

**Nearest related only — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS C.5 — Quillen fundamental groupoid of a mapping complex

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Quillen’s fundamental groupoid agrees naturally with that of the derived mapping complex under cofibrant/fibrant replacement; specified vertices and basepoint paths determine the corresponding pi1 comparisons.

**Supplied locator:** IX-040; IX-041; IX-072. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 61.

**Comparison note:** No derived-mapping-complex comparison with Quillen’s fundamental groupoid occurs on the supplied 118 pages. Scan023 mentions equivalence of fundamental groupoids for a proposed pushout property, not the homotopy groups of a mapping space.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.6 — Coherent loop/suspension identities and adjunction

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed infinity categories with the required pullbacks and pushouts have mapping-space loop/suspension formulas; a pointed derivator has the corresponding adjunction and exact morphisms.

**Supplied locator:** IX-084; IX-087. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 62.

**Comparison note:** No mapping-space loop formula, suspension adjunction in a pointed derivator, or exact morphism theorem occurs on the supplied 118 pages. The cones and cofibres noted in scans011–014 are ordinary categorical constructions and questions, without the claimed pointed formalism.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.

### PATHS C.7 — Pi1 representability does not force loop formulas

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Representability of all pi1 mapping functors does not imply the mapping-space loop formulas.

**Supplied locator:** IX-084; tests (a) and (c). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 63.

**Comparison note:** No form of the representability counterexample or the associated loop formulas appears on the supplied 118 pages. The isolated fundamental-groupoid question on scan023 concerns gluing rather than representability of mapping functors.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.8 — Truncated derived Hom for complexes of modules

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For complexes of modules over a commutative ring k, truncated derived Hom takes values in D^{<=0}(k), with derived-tensor composition, units, and the prescribed mapping-space homotopy groups.

**Supplied locator:** IX-061; IX-065; IX-070. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 64.

**Comparison note:** The derived-Hom object in D^{<=0}(k), derived-tensor composition, and its units and homotopy groups have no form on the supplied 118 pages. No complexes of modules or coefficient-ring construction occurs in the mathematical notes.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.9 — Open additive relative-category enhancement

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The general additive relative-category proposal has not been proved from the manuscript’s unspecified additional axioms, or merely from finite-sum closure of a saturated weak class.

**Supplied locator:** IX-061; IX-065; IX-070. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 65.

**Comparison note:** No additive relative-category construction or its additional axioms is formulated on the supplied 118 pages. Their statements about coproducts and saturation in Cat and presheaf categories do not assert an additive or derived-Hom enhancement.

**Nearest related only — 118 scan027, fragment line 3:**

```tex
les sommes directes finies existent
```

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.10 — Open pointed and ind-category full-path refinements

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The literal pointed and pointed-ind-category refinements of stabilized full paths remain unresolved in the stated generality.

**Supplied locator:** IX-044; IX-049; IX-052; IX-072. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 66.

**Comparison note:** No pointed or pointed-ind-category refinement of stabilized full paths occurs on the supplied 118 pages. A sequential open-immersion construction is used for saturation in scan041, without stabilized path ind-objects.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357); **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS D.1 — Typed and size-bounded IX recognition tests

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Typed, size-bounded versions of IX tests (a), (b), (c); distinguish both representability directions and the two readings of homotopes in (b).

**Supplied locator:** IX ms.22-23; IX-080. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 67.

**Comparison note:** No form of the IX tests (a), (b), and (c), their two representability directions, or their size-bounded formulation occurs on the supplied 118 pages. The ordinary fraction calculus on scan024 does not identify these mapping-functor tests.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.2 — Five-arrow identity-marked example rectifies

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The five-arrow pointed category with identity weak equivalences rectifies every small shape and satisfies the tests and Kaledin enhancement; the contrary clause of Lead 3 is false.

**Supplied locator:** IX ms.23; IX-080; Lead 3; CATHOT E.14; Kaledin addendum (iii). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 68.

**Comparison note:** The five-arrow pointed category, its identity marking, and its claimed all-shape rectification have no form on the supplied 118 pages. Thus these pages neither supply the example nor adjudicate the contrary Lead 3 clause.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.3 — Finite products force a finite category to be a preorder

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A finite category with all finite products is a preorder; if pointed it is equivalent to the terminal category. The IX finite example lacks x times x.

**Supplied locator:** IX ms.23. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 69.

**Comparison note:** No form of the finite-category counting argument, the pointed terminality conclusion, or the missing product in the IX example appears on the supplied 118 pages. Scan032 concerns existence and preservation of finite products in localized presheaf categories, without assuming the category itself finite.

**Nearest related only — 118 scan032, fragment line 3:**

```tex
les produits finis existent
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.4 — Rectifiability yields the constant-diagram mapping formula

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Rectifiability on a specified shape class implies H_ab(A)=[BA,Map_L(M,W)(a,b)] naturally, hence constant-diagram test (b).

**Supplied locator:** IX ms.22; IX-080; Lead 3. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 70.

**Comparison note:** No form of the comparison H_ab(A)=[BA,Map_L(M,W)(a,b)] or its consequence for test (b) occurs on the supplied 118 pages. They do not formulate rectification of diagrams over a specified class of shapes.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.5 — Six-object suspension-poset restriction counterexample

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For a six-object suspension poset X and a weak equivalence Y to the finite parallel-arrow category B, restriction H_ss(B) to H_ss(Y) is not surjective.

**Supplied locator:** VII-c ms.134 companion; IX-080. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 71.

**Comparison note:** The six-object suspension poset, finite parallel-arrow category, and non-surjective restriction map have no form on the supplied 118 pages. Scan023 mentions fundamental groupoids in a pushout question, without this suspension-poset construction.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.6 — Loop identities imply the corresponding representability

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Each higher loop identity (c) implies its associated representability (a); pointed infinity-category pullbacks/pushouts give the coherent identities; finite-poset (b) does not force both adjoint operations.

**Supplied locator:** IX-081, IX-088; IX ms.22-25. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 72.

**Comparison note:** No form of the higher loop identities, either representability direction, or the finite-poset limitation appears on the supplied 118 pages. Their cone and cofiber questions do not formulate coherent pointed infinity-category pullback or pushout identities.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.7 — Known finite and all-shape rectification frameworks

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Cisinski finite derivable categories rectify finite inverse/direct shapes; full ABC categories and suitably complete Quillen model categories rectify all shapes in their universe.

**Supplied locator:** Lead 3; Part D(2). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 73.

**Comparison note:** No Cisinski finite derivable, ABC, or Quillen model-category rectification theorem occurs on the supplied 118 pages. The factorization and interval conditions in scans025–026 are used for a left-fraction calculus, a different conclusion from rectification at inverse/direct or arbitrary shapes.

**Nearest related only — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Nearest related only — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS D.8 — Finite intrinsic cofibration axioms imply rectification

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Initial object, pushouts, two out of three, and enough intrinsic cofibrations imply CF1-CF4 and rectification at finite direct categories; no finite-poset counterexample under those hypotheses.

**Supplied locator:** XII ms.228-234,272; POLES A.8-A.9/G.26 addendum (i)-(iv). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 74.

**Comparison note:** Own comparison: scan025 explicitly combines factorization through a distinguished arrow class, a pushout stability condition, interval endpoint inclusions, and finite colimits to obtain left fractions. This resembles the finite cofibration input of the later result, but 118 neither defines intrinsic cofibrations by their universal preservation property nor states CF1–CF4 or finite-direct rectification.

**Confidence in this own comparison:** medium — Several structural hypotheses overlap explicitly, but the arrow class, exact axioms, and conclusion differ.

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Manuscript evidence — 118 scan025, fragment line 31:**

```tex
avec $i\in\unsure{\mathcal M|\mathcal A}$, $h$ homotopisme
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.
- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.

### PATHS D.9 — Enough intrinsic cofibrations does not imply all cofibrancy

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The diamond lattice has enough intrinsic cofibrations but noncofibrant objects; finite sets with isomorphisms show CF5 and CF6 do not follow from the finite axioms.

**Supplied locator:** POLES addendum (i). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 75.

**Comparison note:** No form of the diamond-lattice or finite-set examples, or the independence of CF5 and CF6, appears on the supplied 118 pages. The generic pushout warning on scan023 is not one of these examples and uses the manuscript’s separate categorical setting.

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS D.10 — Cubical rectification does not imply finite-poset rectification

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Rectification at all cubes does not imply finite-poset rectification: the six-element circle face poset with every arrow weak misses degree two at its own shape.

**Supplied locator:** Part D(3) cubical test. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 76.

**Comparison note:** The six-element circle face poset, all-arrow marking, and missed degree-two map have no form on the supplied 118 pages. No implication from cubical tests to finite-poset rectification is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.11 — Finite simplicial sets fail rectification at BZ

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite simplicial sets rectify finite posets but fail at BZ because strict finite automorphisms have finite order and a Nielsen monodromy has infinite order. The opposite is BK-fibrant with the same failure.

**Supplied locator:** Part D(3) finite posets versus BZ and BK question. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 77.

**Comparison note:** No form of the finite-simplicial-set, infinite-order Nielsen monodromy, or opposite BK-fibrant example appears on the supplied 118 pages. The Kan-type condition proposed on scan031 concerns simultaneous homotopies and does not give this rectification counterexample.

**Nearest related only — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.12 — Nine-vertex fence rectifies without BK fibrancy

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The nine-vertex contractible fence with all arrows weak rectifies all shapes but fails BK fibrancy through an explicit unfillable inner horn in Ex squared of its nerve.

**Supplied locator:** Part D(3) converse BK question. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 78.

**Comparison note:** The nine-vertex fence, the specified inner horn of Ex squared, and their claimed rectification consequence have no form on the supplied 118 pages. No BK fibrancy test occurs there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.13 — Ordinary relative-poset localization need not rectify

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A relative poset localization of an ordinary category need not rectify: finite circle P presents BZ; explicit countable signed-face orbit poset Q presents BC2 and fails rectification at the finite category BC2.

**Supplied locator:** STRATA B.8 addendum; Part D(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 79.

**Comparison note:** Neither the finite circle presentation of BZ nor the countable signed-face orbit presentation of BC2 occurs on the supplied 118 pages. Scan024’s ordinary localization and left-fraction statements do not assert that all diagram categories rectify.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.14 — Kaledin shape classes and extension scope

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Audit of Kaledin v3 shapes, definitions, representation and extension scope: Pos is finite chain dimension, Pos+ left-bounded, Pos+- left-finite; finite posets alone are not his base.

**Supplied locator:** Recent results Kaledin; GALOIS F.5 addendum. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 80.

**Comparison note:** No Kaledin Pos, Pos+, or Pos+- shape class, finite-chain-dimension condition, or extension-scope audit occurs on the supplied 118 pages. Their finite-family homotopy argument does not formulate any such recognition theorem.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.15 — Naive Kaledin enhancement and coherent comparisons

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The naive family on Kaledin Pos (respectively Pos+) is enhanced iff its canonical comparisons to coherent L(M,W) diagram categories are equivalences; the representing infinity-category is L(M,W), by Kaledin plus localization universality.

**Supplied locator:** Recent results Kaledin (i),(iv); Part D(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 81.

**Comparison note:** No form of the Kaledin enhancement criterion or the representing infinity-category assertion occurs on the supplied 118 pages. They discuss ordinary localizations, without the family of coherent diagram-category comparisons used by this row.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.16 — Unbounded finite zigzags obstruct infinite additivity

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The circle relative poset fails additivity at the countably infinite discrete poset because finite zigzags yield bounded winding sequences; the finite IX category with W identities fails no enhancement axiom.

**Supplied locator:** Recent results Kaledin (ii),(iii). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 82.

**Comparison note:** Own comparison: scans028–031 isolate the failure of a uniform finite homotopy length in an infinite family, explicitly requiring at least n elementary homotopies for its nth pair on scan029. This is the same bounded-length obstruction that motivates the dossier’s winding-sequence argument, but the circle relative poset, Kaledin additivity axiom, and identity-marked IX example are absent from 118.

**Confidence in this own comparison:** high — The manuscript explicitly names the unbounded lengths and their infinite-coproduct consequence; only that mechanism is compared.

**Manuscript evidence — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**Manuscript evidence — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**Manuscript evidence — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS D.17 — Later Cof axioms and filtered-colimit upgrades

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Later Grothendieck Cof0-Cof3 and quillenisable classes imply finite-direct rectification; full Cof4 implies ABC and all-relative-universe rectification and homotopy left Kan extensions. Filtered-colimit stability of W upgrades intrinsic cofibrations.

**Supplied locator:** XIII ms.7-12,50-59; XVII ms.39-40; XIX ms.33-38,48; Part D(4). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 83.

**Comparison note:** Own comparison: scans025–026 give finite factorization/pushout/interval conditions for left fractions, while scans039–041 use special open or closed filtrations and L3 in the saturation argument. These supply related ingredients, but the named Cof0–Cof4 axioms, quillenisable classes, ABC recognition, all-shape rectification, and homotopy Kan extensions are not stated in 118.

**Confidence in this own comparison:** medium — The common finite and limiting ingredients are explicit; the later abstract packages and stronger conclusions are absent.

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Manuscript evidence — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364); **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.
- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS D.18 — Accessible Cat localizers and Thomason rectification

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Accessible fundamental localizers on Cat admit left proper Thomason models and rectify all relative-small shapes; enough intrinsic fibrations is a stricter properness condition. Pointed tests are applied to pointed objects.

**Supplied locator:** POLES G.24/E.2 addendum; Part D(2),(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 84.

**Comparison note:** No accessibility hypothesis, Thomason model structure, or all-shape rectification theorem occurs on the supplied 118 pages. Their localizer axioms and saturation theorem do not establish model-category existence or the stronger intrinsic-fibration condition.

**Nearest related only — 118 scan015, fragment line 8:**

```tex
si deux parmi $g,f,gf$ dans $\underline W$, le 3e l'est
```

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** **GALOIS B.13** (Open (the return's claim); line 345); **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS D.19 — Locally constant Set restriction fails two out of three

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The fully faithful locally constant restriction class for Set fails two out of three on e to BC2 to e, so descent cannot substitute for the finite cofib axioms.

**Supplied locator:** GALOIS A.5 addendum; Part D(1). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 85.

**Comparison note:** No form of the e→BC2→e counterexample or the fully faithful locally constant Set-restriction class appears on the supplied 118 pages. Scan015 states a two-out-of-three requirement for the chosen localizer, without deriving a descent class or testing this example.

**Nearest related only — 118 scan015, fragment line 8:**

```tex
si deux parmi $g,f,gf$ dans $\underline W$, le 3e l'est
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.20 — Modern references and coherent versus ordinary arrows

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Resolved Arlin and Fuentes-Keuthan-Kedziorek-Rovelli references, with strict versus pseudonatural scope. Coherent arrow homotopy categories differ from arrows in Ho: Z maps versus one.

**Supplied locator:** Recent results references; STRATA C.7 addendum. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 86.

**Comparison note:** The Arlin and Fuentes–Keuthan–Kedziorek–Rovelli reference audit and the Z-versus-one arrow comparison have no form on the supplied 118 pages. Their ordinary homotopy localization does not identify a coherent arrow homotopy category with, or distinguish it from, arrows in Ho.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.21 — Kaledin Pos comparisons detect coherent localization

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If R_(A times J) is an equivalence for every Kaledin Pos shape J, the specified infinity-localization comparison L(M^A) to Fun(NA,L(M)) is an equivalence.

**Supplied locator:** GALOIS mapping-space upgrade suggestion. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 87.

**Comparison note:** No form of the all-J condition on R_(A times J), or the resulting infinity-localization equivalence with Fun(NA,L(M)), occurs on the supplied 118 pages. No canonical coherent diagram comparison is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.22 — Remaining intrinsic recognition and IX comparison questions

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Exact unresolved targets: finite-only and cardinal-only intrinsic recognition, finite-product-test upgrade, BK finite-shape sufficiency, intrinsic cofib without initial object, full IX test equivalence/c=>b without path comparison, and nonaccessible Cat localizer derivators.

**Supplied locator:** IX-080; Part D(3); recent/additional unresolved questions. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 88.

**Comparison note:** No form of this list of unresolved finite/cardinal, BK, IX, or nonaccessible-derivator targets occurs on the supplied 118 pages. The finite conditions on scan025 and special limit theorem on scans039–040 give neighboring material but do not settle these tests or remove the initial-object hypothesis.

**Nearest related only — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364); **GALOIS B.13** (Open (the return's claim); line 345).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS D.23 — Nonzero-spectrum homology localizers lack intrinsic fibrations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For every nonzero spectrum E, its homology localizer lacks enough intrinsic fibrations: free-group nullity plus an identity-homology nonsurjective endomorphism separates W_E from its aspherical generation.

**Supplied locator:** POLES C.4-C.5 addendum; Part D(2) cofibration-fibration asymmetry. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 89.

**Comparison note:** No spectrum-homology localizer, free-group nullity argument, or nonsurjective identity-homology endomorphism appears on the supplied 118 pages. The fibration/cofibration classification there uses categorical lifting notions and does not prove the claimed failure of enough intrinsic fibrations.

**Nearest related only — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**RESULTS_STATE links:** **RESIDUE D.9** (Open (the return's claim); line 365).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS D.K1 — Acyclic CW maps are epimorphisms in Hot

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An acyclic map of small CW spaces is an epimorphism in the unpointed homotopy category, with weakly equivalent double-pushout codiagonal.

**Supplied locator:** GALOIS B.9 verification; CATHOT E.17 reduction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 90.

**Comparison note:** No form of the small-CW acyclic-map epimorphism theorem or double-pushout codiagonal assertion occurs on the supplied 118 pages. Their categorical pushout comparison and warning do not impose CW hypotheses or analyze this codiagonal.

**Nearest related only — 118 scan022, fragment line 10:**

```tex
diagramme cocartésien dans un $\widehat A$, avec $Y\hookrightarrow X$ mono
```

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K2 — Embedding groups in large simple acyclic groups

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Every small group embeds in a simple nonabelian integrally acyclic group of any prescribed infinite small cardinality at least its size.

**Supplied locator:** GALOIS B.10 verification; KT_mu. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 91.

**Comparison note:** No embedding into a simple nonabelian integrally acyclic group, or prescribed-cardinality construction, occurs on the supplied 118 pages. The groupoid example in scans033–036 concerns a different product/asphericity question.

**Nearest related only — 118 scan036, fragment line 7:**

```tex
alors dans $\widehat A$ $\underline W_A$ est formé des seuls iso
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K3 — KT_mu acyclic BG presentations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** KT_mu holds: every connected small CW complex has an acyclic BG presentation whose perfect kernel is killed by every homomorphism to any group of size at most mu.

**Supplied locator:** GALOIS B.11 verification; KT_mu; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 92.

**Comparison note:** No form of KT_mu, acyclic BG presentations of CW complexes, or the specified perfect-kernel annihilation condition appears on the supplied 118 pages. The dossier’s claimed reduction for CATHOT E.17 is therefore carried only as contextual background.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K4 — Homotopy-invariant ind-presheaves factor through groupoids

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If a presheaf ind-represented by a nonempty small filtered system of categories modulo natural transformations inverts W_infinity on all small shapes, it inverts W_1 and the specified groupoid-completion unit is an ind-isomorphism with the same indexing category.

**Supplied locator:** GALOIS B.12 verification; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 93.

**Comparison note:** No ind-represented presheaf theorem or same-index groupoid-completion ind-isomorphism occurs on the supplied 118 pages. The sequential construction on scan041 serves saturation and does not formulate an all-small-shape invariance assumption.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K5 — All-small-shape invariance forces a one-type

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All-small-shape homotopy invariance of the constant-to-constant localization Hom functor for a small relative category forces factorization through Pi_1; if represented by a space, that space is a 1-type.

**Supplied locator:** V ms.44-46; Lead 3 size correction; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 94.

**Comparison note:** No form of the constant-to-constant localization Hom theorem or its representing-space one-type conclusion occurs on the supplied 118 pages. The fundamental-groupoid question on scan023 concerns a pushout property rather than all-shape invariance.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS E.1 — All-arrow endpoint fibres realize path spaces

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The checked CATHOT all-arrows theorem identifies exact endpoint fibres with path spaces, even translation with identity in Hot, and the one-sided constant-tail maps as weak equivalences.

**Supplied locator:** CATHOT E.20-E.25; VIIc-C004; VIIc-C005. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 95.

**Comparison note:** No all-type path category, even-translation comparison, or constant-tail map appears on the supplied 118 pages. The Fib(f) constructions of scans011–014 are ordinary comma constructions and are explicitly marked as not yet Serre.

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.2 — Strictly monoidal categorical loop model

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The all-type categorical loop model is strictly monoidal, natural in pointed functors, and realizes the loop space with its A-infinity multiplication.

**Supplied locator:** Part E; IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 96.

**Comparison note:** No all-type categorical loop model or claim about its A-infinity multiplication occurs on the supplied 118 pages. Their discussion of intervals and ordinary homotopy does not specify a strictly monoidal loop construction.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS E.3 — All-type endpoints need not have strict lifting properties

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The all-type endpoint functor is smooth but can fail properness and both strict Grothendieck lifting properties, already for X=[1].

**Supplied locator:** VII ms.161-166; Part E; STRATA path test. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 97.

**Comparison note:** Own comparison: scan014 explicitly records that smooth Serre maps need not be fibrations and proper Serre maps need not be cofibrations, distinguishing homotopical properties from strict Grothendieck lifting. It contains neither the all-type endpoint functor nor the X=[1] witness, and does not assert the row’s failure of properness.

**Confidence in this own comparison:** medium — The lifting distinction is explicit, but the endpoint construction and the smooth-versus-proper counterexample are absent.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.4 — Eventual endpoints smooth and proper without strict bifibration

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The eventual alternating endpoint functor is smooth and proper but need not be a Grothendieck fibration or opfibration.

**Supplied locator:** Part E; filtered-union lifting distinction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 98.

**Comparison note:** Own comparison: scan014’s explicit nonimplications already require separating proper/smooth Serre conditions from categorical cofibration/fibration. The eventual alternating path category and its filtered-union endpoint construction are absent, so 118 gives the general distinction rather than this witness.

**Confidence in this own comparison:** high — The relevant nonimplications are written explicitly; no claim of an identical path model is made.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.5 — Smooth proper categorical mapping-path factorization

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Every functor has a natural categorical mapping-path factorization into a nerve weak equivalence followed by a smooth proper functor whose strict fibres are homotopy fibres.

**Supplied locator:** Part E; XII ms.188-207. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 99.

**Comparison note:** Own comparison: scans011–014 factor a functor through Fib(f), with a retraction described as a homotopism and a fibration explicitly marked as not yet Serre. This is a categorical replacement construction, but it does not provide the dossier’s simultaneous smooth/proper conclusion or the strict-fibre homotopy-fibre comparison.

**Confidence in this own comparison:** high — The factorization diagram, homotopism, and stated limitation are visible in the frozen text; the later strengthened conclusion is not imported.

**Manuscript evidence — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**Manuscript evidence — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.6 — Rectangular-band path endpoints fail strict lifting

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For the five-element rectangular-band monoid of type S2, the eventual path endpoint map is neither a strict fibration nor opfibration; the all-type map is not an opfibration.

**Supplied locator:** STRATA E.11 test case. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 100.

**Comparison note:** The five-element rectangular-band monoid, its S2 homotopy type, and the claimed endpoint counterexamples have no form on the supplied 118 pages. Scan014 supplies only the general distinction between Serre/proper/smooth and strict lifting classes.

**Nearest related only — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.7 — Interval pushout-products fail intrinsic cofibration

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For every n>=1 the specified interval pushout-product is a weak equivalence but not an intrinsic W_infinity-cofibration.

**Supplied locator:** POLES H.6; TOTASPH F.23; Part E. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 101.

**Comparison note:** No form of the specified interval pushout-product counterexample for every n appears on the supplied 118 pages. Scan026 requires a separating interval for its fraction argument, and scan023 warns about a categorical pushout statement, but neither defines or disproves this intrinsic W_infinity-cofibration property.

**Nearest related only — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS E.8 — Finite interval cotensors can have incorrect endpoint fibres

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite interval cotensors have a constant-section categorical homotopy equivalence but their exact endpoint fibres need not be the correct path spaces.

**Supplied locator:** Part E; dual interval assertion. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 102.

**Comparison note:** No finite-interval cotensor Fun(I,X), constant-section theorem, or incorrect path-space endpoint-fibre example occurs on the supplied 118 pages. The homotopism of scan012 belongs to the Fib(f) comma replacement and does not assert this cotensor comparison.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.9 — Smooth/proper for one localizer does not control larger ones

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** W_infinity smoothness/properness does not imply universal preservation under strict pullback for a larger localizer.

**Supplied locator:** GALOIS/STRATA localizer qualification; Part E. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 103.

**Comparison note:** No form of the comparison between W_infinity and a larger localizer, or its universal strict-pullback counterexample, occurs on the supplied 118 pages. Scan009 discusses a proper/smooth base-change criterion without making the claimed cross-localizer implication.

**Nearest related only — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**Nearest related only — 118 scan009, fragment line 15:**

```tex
\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*
```

**RESULTS_STATE links:** **GALOIS B.14** (Open (the return's claim); line 359); **BISITE A.19** (Proved (the return's claim); line 381).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.

### PATHS E.10 — Marked components do not determine an exit-path localization

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Components of the marked subcategory alone do not specify a stratification whose exit paths compute general localization mapping spaces.

**Supplied locator:** STRATA proposed general stratified reading. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 104.

**Comparison note:** No form of the proposed stratification by marked-subcategory components, or its failure to compute localization mapping spaces by exit paths, occurs on the supplied 118 pages. The open–closed bifunctor H_X on scan017 glues ordinary categories; it does not encode a marking or an exit-path comparison.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**RESULTS_STATE links:** **STRATA B.2** (Proved (the return's claim); line 401).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### PATHS E.11 — Strict bifibration realizing the rectangular-band path system

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Existence of another strict bifibration realizing the path local system over the rectangular-band monoid remains unresolved here.

**Supplied locator:** STRATA E.11; VIc-C022. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 105.

**Comparison note:** No form of the rectangular-band existence problem, or a construction or exclusion of another strict bifibration, appears on the supplied 118 pages. Scan014 clarifies why strict lifting must be distinguished from smooth/proper behavior, but supplies no solution of the open BISITE B.21 / RESIDUE A.8 problem.

**Nearest related only — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.12 — Fixed-origin paths contractible but not filtered or total

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The checked fixed-origin all-type path category may be contractible without being filtered or totally aspherical; its endpoint functor is final over simply connected bases.

**Supplied locator:** TOTASPH G.1-G.6; XIIba-C005. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 106.

**Comparison note:** No fixed-origin all-type path category or simply-connected-base finality assertion occurs on the supplied 118 pages. Their product/diagonal total-asphericity discussion on scans033–036 also uses a different notion from the later totality invoked in this row.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **TOTASPH A.7** (Known (the return's claim); line 405); **TOTASPH C.10** (Refuted (the return's claim); line 408).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS E.13 — Finite test-object restricted Yoneda is not faithful

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite set-valued restricted Yoneda on finite-category test objects is not faithful: the finitary symmetric-group shift and the identity induce the same tests but are distinct in Hot.

**Supplied locator:** VIIc-C004 faithfulness question; CATHOT F.2 verification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 107.

**Comparison note:** The finitary symmetric-group shift, its agreement with identity on finite set-valued tests, and its distinctness in Hot have no form on the supplied 118 pages. No finite-category restricted-Yoneda faithfulness question is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

## Check events and frozen source

The separate `strata_paths_events.tsv` records 122 actual textual matching/background events: 86 assigned dossier rows, 22 additional RESULTS_STATE references, and 14 companion/Pursuing Stacks context items. Every type is **carried as background without fault found**, with an explicit outcome saying that no mathematical proof was validated. No entry is labeled proof-checked, re-proved, or refuted by this task.

The source hash is unchanged:

```text
63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149
```

The duplicate consecutive cotefile markers in the frozen combined file remain preserved; the primary agent records this mechanical assembly defect.


# BISITE evidence mapping: frozen MPL 118

**Coverage:** 113 of 113 supplied BISITE rows. Relations: absent 73, analogue 30, partial 10.

**Scope.** This is a textual comparison after the transcription freeze of 18 November 2026 at 02:41:21 UTC; context was opened at 02:41:34 UTC. No scan images were inspected and no frozen transcription file was changed. All supplied statuses remain claims of the earlier return; no mathematical proof was independently checked.

**How to read the notes.** “Partial” means an actual clause is visible but the later theorem adds material scope or conclusions; “analogue” means a related construction or question only. “Absent” is explicit absence from the whole frozen transcription, not a refutation of the contextual claim. Exact TeX quotations retain uncertainty and deletion macros. Every item has its own context locator and related state IDs; related IDs are not proof certificates.

**Main distinctions.** Scan 009 gives an exact categorical precursor of the intrinsic pullback-preservation definition and the strongest proper/smooth cohomological base-change statements. Scans 011–014 explicitly distinguish ordinary replacements from Serre fibrations. The modern simplicial, strict higher categorical, enhanced derivator, stable duality and geometric applications largely have no direct statement in this manuscript.

## BISITE A.1 — Historical and modern localizer axioms

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 015 gives a weak Loc 1 list with the restricted equation gf=id, while scan 040 invokes relative slices in its use of L3 and states saturation. It does not give the later XVI separation of moderate saturation, retract closure, strong saturation, absolute Theorem A, and relative Theorem A; these formulations must not be retroactively identified.

- **MPL 118 scan 015:** `c) $gf=\mathrm{id}$ et $fg\in\underline W\Rightarrow f,g\in\underline W$)`
- **MPL 118 scan 040:** `donc on gagne par L3.`
- **MPL 118 scan 040:** `L'ens. $\underline W$ est saturé`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.1, line 115; supplied locator: XVI ms.1--3; context/companion/chunks/DER_XVI.tex — Chapter XVI §1, manuscript pp.1–3: literal Loc(1)–Loc(3 bis).

**RESULTS_STATE:** GALOIS B.1, GALOIS B.3 (related claims; not rechecked).

## BISITE A.2 — Intrinsic fibrations preserve every over-base W-map

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 009 defines S by precisely the arbitrary-arrow-over-Y pullback quantifier used in the categorical special case of intrinsic Fib_W. The extension to arbitrary categories with pullbacks and the separate closure and retract statements are not established in these pages.

- **MPL 118 scan 009:** `\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.2, line 116; supplied locator: XII ms.207--209; GALOIS D.1; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14 (related claims; not rechecked).

## BISITE A.3 — Coarse, universal, and fine relative equivalences

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The manuscript distinguishes W, universal preservation, and aspherical/coaspherical subclasses, providing an earlier vocabulary for the comparison. It does not define the three slice-localizer classes W_S, W_S^u, and W_S^L or prove their stated inclusion and saturation properties.

- **MPL 118 scan 005:** `=W\cap WSC`
- **MPL 118 scan 009:** `\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.3, line 117; supplied locator: XII ms.210,220; GALOIS A.5; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.4 — Localization of pullback and postcomposition adjunctions

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The S condition explicitly controls raw pullback of weak equivalences over a base. No descended adjunction between the later fine localized slices, nor the complete two-variance assertion, is written in the frozen text.

- **MPL 118 scan 009:** `\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.4, line 118; supplied locator: XII ms.226--227,248; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.5 — Universal saturation of admissible tests

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No definition of L-hat, idempotence theorem, or maximality among test classes occurs in the frozen text. The corrected all-further-base-changes quantifier belongs to the cited XII discussion and its commentary.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.5, line 119; supplied locator: XII ms.222; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.6 — Corrected transporter Galois connection

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No transporter–kernel Galois connection or pair of inverse order-reversing correspondences is present. The diagrams of arrow classes do not state the later closure-operator theorem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.6, line 120; supplied locator: II ms.83--89, (6.7); context/companion/chunks/DER_II-b.tex — Chapter II §6, manuscript pp.83–89: transporters, kernels and stabilizers.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.7 — Composition criterion for closed transporter pairs

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No closed transporter pair, stabilizer criterion, or necessary-and-sufficient composition test is stated. The contextual proposition is not a manuscript conclusion merely because the early notes organize several map classes.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.7, line 121; supplied locator: II Proposition 6.1, ms.88--89; context/companion/chunks/DER_II-b.tex — Chapter II §6, manuscript pp.83–89: transporters, kernels and stabilizers.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.8 — Transporters need not compose

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The four-object ordered-set transporter counterexample is absent. No failure of composition for that specific transporter construction is formulated in the frozen text.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.8, line 122; supplied locator: II first versions (6.2)--(6.5); context/companion/chunks/DER_II-b.tex — Chapter II §6, manuscript pp.83–89: transporters, kernels and stabilizers.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.9 — Smooth and proper stabilizers; conjectural complementarity

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 009 gives the proper fibre-to-comma criterion, exchanges proper and smooth by opposition, and boxes Sm∩Pr⇒S. It does not define the general stabilizers or mixed transporters of II, and its displayed categorical inclusion cannot be promoted to the later arbitrary-localizer axiom qualified by peut-être at XII 225–226.

- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`
- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`
- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.9, line 123; supplied locator: II ms.66,89; XII ms.225--226; context/companion/chunks/DER_II-b.tex — Chapter II §4, manuscript pp.65–68; §6, p.89: stabilizer definition and cancelled comparison; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE A.10 — Three distinct fibre axioms

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The a/b/c localization and fibre-invariance axioms of XII 215–218 are not formulated. The manuscript's many fibration adjectives do not supply that specific logical comparison or its strong-saturation qualification.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.10, line 124; supplied locator: XII ms.215--218; XIIc B055--B065; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.11 — Enough intrinsic fibrations gives exact fibre invariance

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 005 states the Serre-map identity relating weak equivalence, aspherical fibres, and universality, including a lower diagram ending in uW with a reading uncertainty. The general theorem deducing Fib_W∩W=W^u and fibrewise invariance from a factorization hypothesis is absent.

- **MPL 118 scan 005:** `S\cap W=S\cap T`
- **MPL 118 scan 005:** `W\cap S\\=T\cap S=\unsure{uW}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.11, line 125; supplied locator: XIII ms.10--11; XVI 4.4.1; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14 (related claims; not rechecked).

## BISITE A.12 — Functorial replacement preserves intermediate localizations

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The Fib(f) and cylinder constructions provide explicit replacements and homotopisms. Their qualification but not yet Serre prevents identifying them with the functorial intrinsic-fibrant replacement required for the later theorem about every intermediate category.

- **MPL 118 scan 011:** `\uline{but not yet Serre}`
- **MPL 118 scan 012:** `\text{closed section}\\\text{and \uline{homotopism}}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.12, line 126; supplied locator: XII ms.217--218; XIIc B060--B065; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.13 — Fibre axioms a and b do not imply c

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The six-object counterexample separating the three abstract fibre axioms is absent. Neither those axioms nor the specific failure of localization through intermediate subcategories is exhibited.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.13, line 127; supplied locator: XII ms.207,217--218; XIIc B062; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §4, manuscript pp.207–218: intrinsic fibrations and fibre axioms.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.14 — Paired fine relative-type axioms

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The opposite smooth/proper classes and their intersection are visible in scan 009. The L/P systems, their two finer equivalence classes, and the additional localization-equivalence axiom have not yet been formulated here.

- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`
- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.14, line 128; supplied locator: XII ms.225--227; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE A.15 — Four fibration classes and reference-localizer tests

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

The manuscript explicitly separates Grothendieck fibrations from Serre maps and records smooth/proper intersection as a further class. It does not contain XVI's contractible-test quantifiers, reference-localizer versions of Loc 7, or the four-class axiom table.

- **MPL 118 scan 011:** `\uline{but not yet Serre}`
- **MPL 118 scan 009:** `\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.`
- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.15, line 129; supplied locator: XVI ms.27--41; POLES A.5--A.6; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14 (related claims; not rechecked).

## BISITE A.16 — Implications among three fibration tests

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No A(F)⇒B(F)⇒C(F) theorem or transfer through a reference replacement class appears. The partial-order pictures do not express these quantifiers on maps between relative objects.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.16, line 130; supplied locator: XVI 4.4.1,4.4.9,4.4.10; POLES A.13--A.14; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14 (related claims; not rechecked).

## BISITE A.17 — Brown hypotheses make the three tests equivalent

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The specified Brown hypotheses and the equivalence of all three fibration tests are absent. No result with those terminal-map, factorization, and closure assumptions is supplied by the cylinder sketches.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.17, line 131; supplied locator: XVI 4.4.3; POLES A.13; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14 (related claims; not rechecked).

## BISITE A.18 — Weak constant-coefficient fibrations fail composition

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No rational constant-coefficient composition counterexample is present. The WSC/WSF notation concerns explicitly displayed categorical tests and cannot be treated as this later derivator counterexample.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.18, line 132; supplied locator: I ms.117--118; GALOIS D.3; context/companion/chunks/DER_I-b.tex — Chapter I, manuscript pp.79–81, 102, 117–123: D-fibrations, constant versus local coefficients and composition.

**RESULTS_STATE:** BISITE A.19, GALOIS D.2 (related claims; not rechecked).

## BISITE A.19 — Asymmetric local-coefficient repair

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 009 relates a constant-coefficient higher direct image to local constancy, with two words retained as uncertain readings. It does not state the repaired full-faithfulness implication, the weaker upstairs constant-coefficient conclusion, or a theorem of equivalence on all local systems.

- **MPL 118 scan 009:** `$R^i f_*(\unsure{c^t})$ loc \unsure{constants}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.19, line 133; supplied locator: I ms.79--81,117--123; GALOIS D.2; context/companion/chunks/DER_I-b.tex — Chapter I, manuscript pp.79–81, 102, 117–123: D-fibrations, constant versus local coefficients and composition.

**RESULTS_STATE:** BISITE A.19, GALOIS D.2 (related claims; not rechecked).

## BISITE A.20 — Proper does not imply locally constant fibres

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The endpoint inclusion {1}→[1] as a counterexample to local constancy is not stated in this form. Properness, Serre conditions, and closed immersions are distinguished, but no complete derivator coefficient assertion follows from that distinction.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.20, line 134; supplied locator: I ms.102; Ib-C003; GALOIS D.9; STRATA D.5; context/companion/chunks/DER_I-b.tex — Chapter I, manuscript pp.79–81, 102, 117–123: D-fibrations, constant versus local coefficients and composition.

**RESULTS_STATE:** BISITE A.19, GALOIS D.2 (related claims; not rechecked).

## BISITE A.21 — Products and strict pullbacks in localized fibrant slices

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 032 claims finite products in the absolute category Hot(W), followed by hypotheses for presheaf models. It does not state the relative fibrant-slice theorem or the comparison of a strict pullback with a homotopy pullback along an intrinsic-fibration leg.

- **MPL 118 scan 032:** `les produits finis existent`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.21, line 135; supplied locator: XII ms.241--248; context/companion/chunks/DER_XIIc-b.tex — Chapter XII, manuscript pp.240–261: products and homotopy-cartesian constructions.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.22 — Weak Quillen axioms give intrinsic factorizations

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 025 lists cylinder, factorization, and amalgamation assumptions used in a calculus-of-fractions argument. These are not the XIII weak Quillen M2/M′/M″ axioms and do not identify trivial cofibrations with C∩W.

- **MPL 118 scan 025:** `On a utilisé les choses suivantes`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.22, line 136; supplied locator: XIII ms.7--12,27--28; PATHS D.17; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §§2–6, manuscript pp.7–12, 27–29, 44–59: Quillen structures and diagram variances.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.23 — Diagram lifting, Kan variance, and fibrancy

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The diagram-category lifting adjunctions and comma conditions for Kan extension are absent. The adjoint notation in the elementary cylinder construction does not concern the later diagram-category theorem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.23, line 137; supplied locator: XIII ms.45--50; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §§2–6, manuscript pp.7–12, 27–29, 44–59: Quillen structures and diagram variances.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.24 — Ordinary finite limits need not preserve objectwise W

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No counterexample to preservation of objectwise weak equivalences by ordinary finite limits or ordinary Kan extension is given. The discussion of finite products in Hot(W) has different input and does not establish this negative assertion.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.24, line 138; supplied locator: XIII ms.45--50; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §§2–6, manuscript pp.7–12, 27–29, 44–59: Quillen structures and diagram variances.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.25 — Noetherian sober Alexandrov posets are finite

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No noetherian–sober Alexandrov finiteness theorem appears. The ordered indexing sets used for filtrations are not analyzed under those topological hypotheses.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.25, line 139; supplied locator: XIII ms.60--67; context/companion/chunks/DER_XIII-b.tex — Chapter XIII §6, manuscript pp.61–72: indexing hypotheses and Kan extensions; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §6, manuscript p.60: start of the indexing-hypothesis discussion.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.26 — Finite diagram control does not give all small Kan extensions

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The FinSet-with-isomorphisms counterexample to unrestricted Kan-extension existence is absent. Questions about infinite sums in Hot(W) do not state this model-category obstruction.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.26, line 140; supplied locator: XIII ms.50--59; PATHS D.9; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §§2–6, manuscript pp.7–12, 27–29, 44–59: Quillen structures and diagram variances.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.27 — Closed exact weak Quillen structures are model structures

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No closed exact weak Quillen recognition theorem, retract-closure argument, or equality of both trivial classes is stated. The fraction-calculus assumptions of scan 025 remain a different package.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.27, line 141; supplied locator: XIII ms.27--29,57; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §§2–6, manuscript pp.7–12, 27–29, 44–59: Quillen structures and diagram variances.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.28 — Uniform diagram models yield derived right Kan extensions

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No theorem deriving right Kan extensions from uniform diagram model structures appears. The exact admissibility and pointwise comma-category hypotheses of the contextual statement are absent.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.28, line 142; supplied locator: XIII ms.57--72; context/companion/chunks/DER_XIII-b.tex — Chapter XIII §6, manuscript pp.61–72: indexing hypotheses and Kan extensions; context/companion/chunks/DER_XIII-a.tex — Chapter XIII §6, manuscript p.60: start of the indexing-hypothesis discussion.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.29 — Polarity joins require closure

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The formal Galois-polarity join formula and its closure operation are absent. Lattice drawings for selected arrow classes do not provide that abstract result.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.29, line 143; supplied locator: II section 5, ms.69--80, especially (5.20); context/companion/chunks/DER_II-b.tex — Chapter II §5, manuscript pp.69–80, especially (5.20): formal polarity.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.30 — Unions of composition-closed classes can fail closure

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No example showing that a union of composition-closed arrow classes need not be composition-closed is supplied. The contextual correction concerns II's formal class calculus, not a stated proposition here.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.30, line 144; supplied locator: II ms.65--67; context/companion/chunks/DER_II-b.tex — Chapter II §4, manuscript pp.65–67; §6, pp.83–86: closure of admissible arrow classes.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE A.31 — Bisite is a programme requiring extra directed data

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Opposition and the two presheaf/covariant-set descriptions are visible in scans 009 and 012. The word bisite and the later question about recovering two fine theories from an arbitrary model category are absent, so this is a precursor in directed structure rather than the later programme itself.

- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`
- **MPL 118 scan 012:** `\text{discrete fibrations}\longleftrightarrow\widehat X`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.31, line 145; supplied locator: VI ms.81--84; XII ms.222--225; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE A.32 — Absolute Theorem A does not imply relative Theorem A

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** unpursued implication.

Scan 040 applies L3 to the slice maps f/i, while scan 015 states only its short weak Loc 1 list. This confirms the importance of preserving the relative form actually used, but neither the absolute/relative independence theorem nor its finite-groupoid witness is present.

- **MPL 118 scan 040:** `donc on gagne par L3.`
- **MPL 118 scan 015:** `c) $gf=\mathrm{id}$ et $fg\in\underline W\Rightarrow f,g\in\underline W$)`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.32, line 146; supplied locator: XVI Loc (1,2,3)/(3 bis); POLES A.16; context/companion/chunks/DER_XVI.tex — Chapter XVI §1, manuscript pp.1–3: literal Loc(1)–Loc(3 bis).

**RESULTS_STATE:** GALOIS B.1, GALOIS B.3 (related claims; not rechecked).

## BISITE A.33 — Converse cocartesian detection needs conservativity

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** unpursued implication.

Scan 023 warns that unrestricted categorical pushouts do not preserve the displayed weak equivalences, and scan 021 separately requires a cartesian square with specified cofibrations. Neither is the later XII 273–275 converse-detection statement, and no f0,f3 versus f1,f2 conservativity criterion is supplied here.

- **MPL 118 scan 023:** `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}`
- **MPL 118 scan 021:** `un diagramme cartésien, avec $i',f$ des cofibrations,`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.33, line 147; supplied locator: XII ms.273--275; POLES G.17--G.18; context/companion/chunks/DER_XIIc-b.tex — Chapter XII, manuscript pp.273–275: conservative converse to cocartesian detection; context/companion/chunks/DER_XIIb-b.tex — Chapter XII §V, manuscript pp.147–149, Corollary 2: gluing along an open immersion, with a cartesian alternative hypothesis.

**RESULTS_STATE:** POLES B.2 (related claims; not rechecked).

## BISITE A.34 — Stabilizers are not generally antitone

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No antitonicity claim for Stab(A), cancelled proof, or counterexample occurs. The erroneous II stabilizer programme is a contextual comparison only.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE A.34, line 148; supplied locator: II cancelled section 4, ms.65--68; context/companion/chunks/DER_II-b.tex — Chapter II §4, manuscript pp.65–68; §6, p.89: stabilizer definition and cancelled comparison.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.1 — Comma tests, opposition, and enhanced fine classifiers

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 009 uses both comma constructions and opposition to compare map properties. It does not define weak equivalences between arbitrary objects of Cat/S by the two comma tests, nor identify their enhanced localizations with space-valued functor categories.

- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`
- **MPL 118 scan 009:** `\forall b\to b'\text{ dans }Y,\ (X_{/b}\to X_{/b'})\in W`
- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.1, line 149; supplied locator: VI ms.81--84; XII ms.222; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.2 — Literal simplicial slices need quasicategorical bases

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

There is no simplicial covariant/contravariant slice criterion or restriction to quasicategorical bases. The interval symbol Δ1 in the frozen text is used for categorical homotopy and tests, not for this model-theoretic assertion.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.2, line 150; supplied locator: Lead 1; VI ms.81--84; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.3 — Nerve recognition of enhanced fine theories

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No nerve-induced equivalence of the two enhanced fine theories appears. In particular, the manuscript makes no corresponding right-Quillen claim about a Cat presentation.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.3, line 151; supplied locator: Lead 1; VI ms.81--84; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.4 — Naive simplicial slice tests fail on an inner horn

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The Λ²₁ counterexample over a nonfibrant simplicial base is absent. No literal simplicial slice test is proposed in the frozen text.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.4, line 152; supplied locator: Lead 1.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.5 — Proper/smooth naming reverses in the Lurie comparison

**Supplied status:** claim (return: Known). **Relation:** analogue. **Kind:** unpursued implication.

The proper fibre-to-overcategory criterion and its smooth opposite occur in scan 009. The comparison with Cisinski's or Lurie's terminology is later contextual information and is not written in the manuscript.

- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`
- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.5, line 153; supplied locator: I ms.54; XII ms.224--225; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.6 — Smooth/proper are maximal universal fine base changes

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 009 pairs proper and smooth criteria with universal cohomological base-change statements. It does not prove maximality for the two fine localizers or state the theorem for every fundamental localizer.

- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`
- **MPL 118 scan 009:** `R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}`
- **MPL 118 scan 009:** `\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.6, line 154; supplied locator: XII ms.222; II ms.66 and 88--89; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.7 — Bifibration, smooth/proper, and intrinsic classes are strict

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

The inclusion Sm∩Pr⇒S is explicit, and scan 014 warns that proper Serre does not imply a Grothendieck cofibration, with a dual warning. The complete pair of strict inclusions, its witnesses, and its precise W∞ restriction are not all established by these diagrams.

- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`
- **MPL 118 scan 014:** `\text{but proper Serre}\not\Rightarrow\text{cofib}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.7, line 155; supplied locator: XII ms.225--226; STRATA D.5--D.6; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.8 — Eventually constant fences resolve based path spaces

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No category of eventually constant integer fences or contractible-total-space path resolution is defined. The finite interval concatenations used in the homotopy discussion serve a different purpose.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.8, line 156; supplied locator: VII ms.161--169; PATHS E.9; context/companion/chunks/DER_VII-c.tex — Chapter VII, manuscript pp.161–169, as located by the supplied dossier: paths and endpoint comparisons.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.9 — Complementarity holds exactly at the minimal or total localizer

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The boxed smooth-and-proper implication is an early categorical version of the desired complementarity. No classification of all fundamental localizers satisfying it is stated, and the box cannot be read as such a classification.

- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.9, line 157; supplied locator: XII ms.225--226; POLES E.5; STRATA G.5; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.10 — Truncation localizers refute unrestricted complementarity

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No EC2→BC2 truncation-localizer counterexample or family of n-type failures appears. The unrestricted-localizer claim is not an explicit theorem in the frozen text.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.10, line 158; supplied locator: XII ms.225--226; POLES C.8--C.9; STRATA G.3--G.4; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.11 — Homology-spectrum complementarity fails for coverings

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The three-sheeted covering witness for every nonzero homology spectrum is absent. The text's categorical Serre terminology supplies no coefficient-spectrum calculation.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.11, line 159; supplied locator: XII ms.225--226; POLES C.10; PATHS E.9; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.12 — A finite bifibration fails two intrinsic fibration tests

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The fourteen-object, one-hundred-arrow bifibration and its W1/rational-local-system calculations are absent. No matching finite example is described.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.12, line 160; supplied locator: GALOIS D.4--D.5; XII ms.225--226; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.13 — Coverings preserve one-type and rational-local-system equivalences

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 012 recognizes discrete Serre maps as étale coverings. It does not state the separate W1 and rational-local-system preservation claims, and those coefficient distinctions cannot be inferred from the label alone.

- **MPL 118 scan 012:** `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.13, line 161; supplied locator: GALOIS D.3; POLES C.10; PATHS E.9; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.14 — Cohomological fibrations and proper maps are incomparable

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** unpursued implication.

Scan 009 distinguishes properness from its weak Serre-comma condition and notes a constant-coefficient local-constancy interpretation. It does not give the two counterexamples proving incomparability for the later derivator classes.

- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`
- **MPL 118 scan 009:** `$R^i f_*(\unsure{c^t})$ loc \unsure{constants}`
- **MPL 118 scan 009:** `\forall b\to b'\text{ dans }Y,\ (X_{/b}\to X_{/b'})\in W`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.14, line 162; supplied locator: I ms.117--118; GALOIS D.2 and D.9; context/companion/chunks/DER_I-b.tex — Chapter I, manuscript pp.79–81, 102, 117–123: D-fibrations, constant versus local coefficients and composition; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests.

**RESULTS_STATE:** BISITE A.19, GALOIS D.2 (related claims; not rechecked).

## BISITE B.15 — Finite examples classify competing fibration notions

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The finite Galois examples and the classification table are absent. The early inclusion diagrams are not that table and carry neither the same coefficient hypotheses nor the same witnesses.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.15, line 163; supplied locator: GALOIS D.3--D.5; I ms.117--123; context/companion/chunks/DER_I-b.tex — Chapter I, manuscript pp.79–81, 102, 117–123: D-fibrations, constant versus local coefficients and composition.

**RESULTS_STATE:** BISITE A.19, GALOIS D.2 (related claims; not rechecked).

## BISITE B.16 — Accessible coefficients recognize the two enhanced theories

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No recognition theorem by Fun(NS±,Spaces_W) for accessible coefficients appears. The manuscript does not distinguish existence of the formal localizers from such an enhanced identification.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.16, line 164; supplied locator: VI ms.81--84; XII ms.222--226; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE B.17 — Truncation fibrations have a homotopy-pullback criterion

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No n-type homotopy-pullback characterization or elementary π0 criterion for Fib_Wn appears. The strict Serre pullback definition is not specialized to truncation coefficients.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.17, line 165; supplied locator: POLES C.8--C.9; STRATA G.4.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.18 — Homology fibration bounds and ordinal tests

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** self-flagged.

Scan 005 explicitly questions whether Δ1 base changes suffice to detect the Serre condition, even with aspherical fibres. This is only a testing analogue: no homology-spectrum lower and upper bounds or finite-ordinal criterion is stated.

- **MPL 118 scan 005:** `Even if fibers are aspheric, the Serre condition cannot be tested by only taking base-changes $\Delta_1\to\unsure{Y}$ ?`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.18, line 166; supplied locator: POLES C.10; XII ms.225--226; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE B.19 — Full fence mapping paths give smooth/proper factorizations

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The manuscript factors maps through ordinary Fib(f) and cylinder constructions, while explicitly marking the former not yet Serre. It supplies neither the full-fence construction nor the later natural smooth/proper factorization theorem and its [1] limitation.

- **MPL 118 scan 011:** `\uline{but not yet Serre}`
- **MPL 118 scan 012:** `\text{closed section}\\\text{and \uline{homotopism}}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.19, line 167; supplied locator: VII ms.161--169; PATHS E.4--E.5; context/companion/chunks/DER_VII-c.tex — Chapter VII, manuscript pp.161–169, as located by the supplied dossier: paths and endpoint comparisons.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.20 — Reversing path words does not repair all endpoint classes

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

There is no path-word reversal construction or the specified walking-arrow counterexample. The dual cylinders in scans 011–014 do not state this negative result about the all-type endpoint.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.20, line 168; supplied locator: VII ms.161--166; PATHS E.3; context/companion/chunks/DER_VII-c.tex — Chapter VII, manuscript pp.161–169, as located by the supplied dossier: paths and endpoint comparisons.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.21 — Strict bifibration representative over a rectangular-band monoid

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

The five-element rectangular-band monoid and its path-space local system do not occur. The smooth/proper and bifibration sketches do not settle or sharpen the contextual open construction problem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.21, line 169; supplied locator: STRATA E.11; PATHS E.6 and E.11.

**RESULTS_STATE:** BISITE B.21, RESIDUE A.8 (related claims; not rechecked).

## BISITE B.22 — Maximal simplicial base-change classes for every base

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The all-simplicial-base construction of maximal covariant and contravariant preserving classes is absent. Categorical smooth/proper opposition cannot supply the requisite fibrant replacements and enhanced simplicial comparisons.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE B.22, line 170; supplied locator: Lead 1; XII ms.222--226; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE B.22 (related claims; not rechecked).

## BISITE C.1 — Presheaf slices and two category-of-elements fine classes

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scans 012 and 022 use presheaves as discrete fibrations and the category-of-elements functor, including its compatibility with pullbacks. The slice-presheaf isomorphism and the two specified fine inverse-image classes are not formulated, and no identification with simplicial fine theories is asserted.

- **MPL 118 scan 022:** `$\varinjlim$) et cartésien (car $i_A$ commute aux produits fibrés)`
- **MPL 118 scan 012:** `\text{discrete fibrations}\longleftrightarrow\widehat X`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.1, line 171; supplied locator: VI ms.83; XII ms.224--225; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE C.1, BISITE C.3 (related claims; not rechecked).

## BISITE C.2 — Elementwise fine classes have no automatic duality

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No calculation making one elementwise fine class only isomorphisms, or contrasting it with the usual simplicial weak equivalences, occurs. The category-of-elements construction alone does not establish that later counterexample.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.2, line 172; supplied locator: XII ms.224--225; Part C; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE C.1, BISITE C.3 (related claims; not rechecked).

## BISITE C.3 — Elementwise smooth/proper classes cannot generally be exchanged

**Supplied status:** claim (return: Refuted). **Relation:** partial. **Kind:** reading question.

Scan 022 calls the arrows induced from presheaves fibrantes, with that word uncertain in the frozen reading, and uses the discrete-fibration geometry. It does not characterize elementwise proper maps by cartesian naturality squares or prove the nonexistence of an exchange autoequivalence.

- **MPL 118 scan 022:** `sont \unsure{fibrantes}`
- **MPL 118 scan 022:** `$\varinjlim$) et cartésien (car $i_A$ commute aux produits fibrés)`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.3, line 173; supplied locator: XII ms.224--225; Part C; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE C.1, BISITE C.3 (related claims; not rechecked).

## BISITE C.4 — An extra involution can exchange fine theories

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Categorical opposition exchanges smooth and proper in scan 009. The abstract sufficient criterion for an arbitrary model category with a chosen W-preserving involution is not stated.

- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.4, line 174; supplied locator: VI ms.84; XII ms.224--225; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE C.1, BISITE C.3 (related claims; not rechecked).

## BISITE C.5 — Strict higher categorical Theorem A via Street nerves

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No strict n-category, Street nerve, or oplax higher comma Theorem A is present. The ordinary categorical L3 use is not this higher-dimensional result.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.5, line 175; supplied locator: Recent-results family 317; Part C.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE C.6 — Strict n-category fine classes and total reversal

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No strict n-categorical fine relative classes or total-cell-reversal construction appears. The manuscript's opposition is ordinary category opposition.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.6, line 176; supplied locator: Recent-results family 317; XII ms.224--225; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE C.7 — Dimensional oppositions and closure of higher classes

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No dimension-indexed opposition DJ or symmetric-difference composition law is defined. Nothing in the frozen text gives the proposed higher recognition or closure criterion.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.7, line 177; supplied locator: Recent-results family 317; Part C.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE C.8 — The Thomason model structure on strict 2-categories

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No proper combinatorial model structure on 2Cat or c2Sd²/Ex²N2 adjunction occurs. The ordinary Cat constructions do not state this result.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.8, line 178; supplied locator: Recent-results family 317.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE C.9 — Higher model structures identify only the coarse slice

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The conditional higher model-presentation comparison with Spaces/|NS| is absent. No distinction between this higher coarse slice and enhanced higher fine theories is developed here.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.9, line 179; supplied locator: VI ms.83; Recent-results family 317; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE C.10 — Open higher fine recognition and base-change problem

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

The strict n-category fine recognition problem is absent as a formulated question. The ordinary proper/smooth sketches supply no solution to its nerve or higher base-change requirements.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE C.10, line 180; supplied locator: Recent-results family 317; Parts C and E.

**RESULTS_STATE:** BISITE C.10, BISITE F.18 (related claims; not rechecked).

## BISITE E.1 — Formal functoriality of fine slice localization

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The intrinsic Serre definition controls weak equivalences under raw pullback. The family of fine classes W_S^L, all-map postcomposition, and their localized adjunction have not been introduced in the manuscript.

- **MPL 118 scan 009:** `\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.1, line 181; supplied locator: XII ms.207–208, 216–218, 226; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.2 — Arbitrary raw pullback fails for fine equivalences

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No endpoint pullback {1}→[1] along {0} gives the stated fine-localizer counterexample. The manuscript's base-change qualifications are related caution, not this particular assertion.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.2, line 182; supplied locator: XII ms.226; Lead 3; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.3 — Enhanced recognition adds both Kan extensions

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No compact-projective-generator recognition theorem or derivation of the three Kan functors occurs. Formal localization and the displayed ordinary replacements do not supply those enhancement hypotheses.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.3, line 183; supplied locator: VI ms.108–113; XII ms.225–227; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.108–113: Theorem-Scholie 2 and fine/coarse replacement.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.4 — Coefficient localization and comma-exact base change

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 009 records proper and smooth cohomological base-change criteria. The presentable-coefficient localization, exact-comma framework, and coherence of its Kan extensions are later additions absent from the text.

- **MPL 118 scan 009:** `R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}`
- **MPL 118 scan 009:** `\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.4, line 184; supplied locator: VI ms.138–169; XII ms.226; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.138–145: direct images and inverse images; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.5 — Cat, simplicial, and Alexandrov instances need separate comparisons

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No common enhanced recognition theorem for these three ambient categories is stated. The coarse/local-system comparison for W∞ is also absent, despite the use of Cat and presheaf presentations.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.5, line 185; supplied locator: VI ms.81–84, 108–113; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.108–113: Theorem-Scholie 2 and fine/coarse replacement.

**RESULTS_STATE:** WG2 §3.2 #7, STRATA 0.1 (related claims; not rechecked).

## BISITE E.6 — Coarse slice is not local systems for every localizer

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The W0 and BC2 counterexample to the unrestricted coarse/local-system comparison does not appear. The manuscript does not make that all-localizer identification.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.6, line 186; supplied locator: VI ms.108–113; arbitrary-W lead; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.108–113: Theorem-Scholie 2 and fine/coarse replacement.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.7 — Intrinsic replacements give finite homotopy limits

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The notes discuss finite products in Hot(W) and ordinary categorical replacements. They do not state a Brown or derivable-category theorem for localized fibrant slices, and their products should not be expanded into all finite homotopy limits or fine Kan operations.

- **MPL 118 scan 032:** `les produits finis existent`
- **MPL 118 scan 011:** `\uline{but not yet Serre}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.7, line 187; supplied locator: XII ms.240–261; XIII ms.7–12; PATHS D.8,D.17,D.18; context/companion/chunks/DER_XIIc-b.tex — Chapter XII, manuscript pp.240–261: products and homotopy-cartesian constructions.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14, WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.8 — Accessible factorization, nullification, and right properness

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No accessibility, nullification, or aspherical-generation characterization of intrinsic factorizations occurs. The local test-category assumptions used in fraction calculus are a different issue.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.8, line 188; supplied locator: XVI Loc (7 F); POLES E.2–E.3; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14, WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.9 — Path endpoints give functorial intrinsic factorization

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The manuscript juxtaposes replacement constructions and the smooth/proper-to-Serre implication. It does not construct the required path endpoint in both classes with a universal-W source map, so the later sufficient factorization theorem is not available from these sketches.

- **MPL 118 scan 011:** `\uline{but not yet Serre}`
- **MPL 118 scan 009:** `\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.9, line 189; supplied locator: XVI Loc (7 F); PATHS E.5; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14, WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.10 — Groupoid bases collapse fine and coarse one-type theories

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

Although groupoids occur in scan 036 in a presheaf-product discussion, the fine/coarse one-type collapse and inversion-of-variance theorem are absent. That groupoid observation concerns a different weak-equivalence class on a presheaf category.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.10, line 190; supplied locator: VI ms.83–84; OpenAI family 312 lead; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.11 — Replacement data imply all three fibre axioms

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The recorded retractions and homotopisms suggest the role of replacements. They do not verify the specific natural replacement data yielding a/b/c or the equivalence for every intermediate slice category.

- **MPL 118 scan 011:** `\uline{but not yet Serre}`
- **MPL 118 scan 012:** `\text{closed section}\\\text{and \uline{homotopism}}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.11, line 191; supplied locator: XII ms.217–218; XIIc B062; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.12 — Two fibre axioms do not imply the third

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The six-object failure of a+b⇒c is absent, just as for the duplicate contextual formulation BISITE A.13. This row remains separately accounted for and is not treated as a fresh proof.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.12, line 192; supplied locator: XII ms.217–218; XIIc B062; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.219–227: fine relative types, saturation of tests and paired classes.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.13 — Ordinary homotopy categories lose coherent gluing information

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** unpursued implication.

Scan 017 keeps an actual bifunctor and a bifunctorial homotopy as part of ordinary categorical gluing data. It does not give the derived walking-arrow nonfaithfulness counterexample or a theorem about coherent gluing after passage to homotopy categories.

- **MPL 118 scan 017:** `H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.13, line 193; supplied locator: PATHS D.20; STRATA C.7; context/companion/chunks/DER_XIIb-a.tex — Chapter XII §V.1.1, manuscript pp.59–60, Proposition 1: ordinary open–closed profunctor gluing.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE E.14 — Accessible intrinsic factorization is a modality/nullification condition

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The modality, local-cartesian-closure, and nullification comparison is absent. No claim identifying its left class with all of W is made or refuted in the frozen text.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE E.14, line 194; supplied locator: POLES E.2–E.3 modality/LCC comparison; context/companion/chunks/DER_XVI.tex — Chapter XVI §4, manuscript pp.27–41 and the cited §4.4 clauses: Loc(7) fibration tests.

**RESULTS_STATE:** GALOIS B.7, GALOIS B.14, WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.1 — Derivator axioms give Kan extensions and exact pasting

**Supplied status:** claim (return: Known). **Relation:** analogue. **Kind:** unpursued implication.

The notes already refer to higher direct images and their base changes. They contain no Der 1–4 axiom system, pointwise Kan-extension theorem, or exact-pasting result, and no stable derivator is introduced.

- **MPL 118 scan 009:** `R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.1, line 195; supplied locator: I; VI ms.138–169; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.138–145: direct images and inverse images; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations; context/companion/chunks/DER_I-a.tex — Chapter I, manuscript pp.53–55: homotopically proper/smooth maps and categorical lifting tests.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.2 — Proper-right and smooth-left base change with converses

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 009 explicitly connects properness with arbitrary base change of R^i f_* and smoothness of the base-change map with commutation past R^i g_*. This is a direct precursor of the corresponding right comparison in presheaf variance, but the full two-adjunction theorem, coefficient-universal converses, and all stated horizontal variants are not proved here.

- **MPL 118 scan 009:** `R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}`
- **MPL 118 scan 009:** `\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*`
- **MPL 118 scan 009:** `(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.2, line 196; supplied locator: VI ms.138–169; STRATA D.4; context/companion/chunks/DER_XI-XIIa.tex — Chapter XII §III, manuscript pp.26–40: lifting categories, proper/smooth criteria, universal comma transport and weak tests; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.138–145: direct images and inverse images; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations; context/companion/chunks/DER_I-a.tex — Chapter I, manuscript pp.53–55: homotopically proper/smooth maps and categorical lifting tests.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.3 — Not every strict square satisfies base change

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** self-flagged.

The manuscript questions the strength of restricted base-change tests and marks several preservation implications with question marks. It does not supply the later finite-coefficient endpoint counterexample to universal strict-square exactness.

- **MPL 118 scan 005:** `Even if fibers are aspheric, the Serre condition cannot be tested by only taking base-changes $\Delta_1\to\unsure{Y}$ ?`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.3, line 197; supplied locator: Lead 3.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.4 — Left projection formula needs smoothness or local constancy

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No tensor product, internal left projection formula, or local-constant-coefficient alternative is stated. Ordinary product calculations for categories do not give the asserted monoidal derivator formula.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.4, line 198; supplied locator: Lead 3; VI projection formulas; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.138–145: direct images and inverse images; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.5 — Monoidality alone does not imply every projection formula

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No monoidal counterexample to an all-map internal projection formula is given. The frozen text has no coefficient tensor formalism to which this assertion could apply directly.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.5, line 199; supplied locator: Lead 3.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.6 — Right projection formulas need dualizability or finite fibres

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No dualizable-coefficient right projection formula or homotopy-finite-fibre criterion occurs. The manuscript's finite products in Hot(W) do not provide these stable coefficient hypotheses.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.6, line 200; supplied locator: Lead 3.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.7 — Internal Hom exchange is controlled by mates

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

There is no internal-Hom exchange formula or mate-coherence calculation for derived adjunctions. The set-valued crossing Hom bifunctor in scan 017 is an ordinary categorical object with a different role.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.7, line 201; supplied locator: VI exchange formulas; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.138–145: direct images and inverse images; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.8 — Index opposition and coefficient opposition have distinct roles

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** reading question.

Scan 009 explicitly exchanges the two ordinary categorical map classes by opposition. It does not define the opposite derivator or reverse coefficient categories, so the adjunction reversal formulas cannot be inferred from base opposition alone.

- **MPL 118 scan 009:** `\mathrm{Sm}=\mathrm{Pr}^{\circ}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.8, line 202; supplied locator: VI ms.84; context/companion/chunks/DER_VI-b.tex — Chapter VI, manuscript pp.81–84: two fine theories, opposite variance and the bisite programme; commentary dgrb239.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.9 — Open/closed Kan extensions and stable recollement

**Supplied status:** claim (return: Known). **Relation:** analogue. **Kind:** unpursued implication.

The manuscript develops the ordinary open–closed decomposition through a crossing Hom bifunctor, with sieves and cosieves visible in the preceding diagrams. It contains no extension-by-zero Kan chains, stable fibre/cofibre triangles, or strong-derivator triangulation theorem.

- **MPL 118 scan 017:** `H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}`
- **MPL 118 scan 012:** `\text{discrete fibrations}\longleftrightarrow\widehat X`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.9, line 203; supplied locator: I; VI open–closed formulas; context/companion/chunks/DER_VI-c.tex — Chapter VI, manuscript pp.146–169: adjunction, base-change and open/closed operations; context/companion/chunks/DER_XIIb-a.tex — Chapter XII §V.1.1, manuscript pp.59–60, Proposition 1: ordinary open–closed profunctor gluing.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.10 — Correspondences on the smooth class give operations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No enhanced correspondence category or lax monoidal b!a* formalism is defined. The integrated span used for an ordinary categorical gluing comparison does not provide the asserted six-operation construction.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.10, line 204; supplied locator: Lead 3; Mann correspondence question; context/companion/chunks/DER_XIIb-b.tex — Chapter XII §V, manuscript pp.147–149, Corollary 2: gluing along an open immersion, with a cartesian alternative hypothesis.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.11 — Cohomological étaleness and ambidexterity are different

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

The equations f!=f* and their cohomological étale interpretation are absent. The étale-covering label in scan 012 supplies no stable ambidexterity or trivial-twist theorem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.11, line 205; supplied locator: Lead 3 terminology.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.12 — Smooth maps need not have smooth diagonals

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No diagonal-closure counterexample or later geometric-setup restriction to discrete fibres is stated. The intersection diagram for proper and smooth maps does not address diagonal closure.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.12, line 206; supplied locator: Mann versus later geometric-setup conventions.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.13 — Multiderivators and two-multicorrespondence formalism

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

The Hörmann multiderivator comparison and its distinction from an infinity enhancement are absent. The ordinary gluing diagrams are not a two-multicorrespondence formalism.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.13, line 207; supplied locator: Hörmann comparison.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.14 — Relative calibrations depend on coefficients

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

The cohomological criteria in scan 009 already attach proper and smooth labels to two base-change behaviors. The Anel–Weinberger calibration construction and the theorem for specified indexed coefficient categories are later contextual comparisons, not manuscript results.

- **MPL 118 scan 009:** `R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}`
- **MPL 118 scan 009:** `\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.14, line 208; supplied locator: Anel–Weinberger comparison; context/companion/chunks/DER_XIIc-a.tex — Chapter XII §5, manuscript pp.224–226: proposed complementary smooth/proper classes; commentary dgrb604; context/companion/chunks/DER_I-a.tex — Chapter I, manuscript pp.53–55: homotopically proper/smooth maps and categorical lifting tests.

**RESULTS_STATE:** WG2 §3.2 #7 (related claims; not rechecked).

## BISITE F.15 — Genus-zero multicurves and constructible exit categories

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No moduli of genus-zero curves, multicurve category, or exit-path constructible-sheaf comparison occurs. This geometric application has no manuscript form in cote 118.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.15, line 209; supplied locator: STRATA genus-zero comparison.

**RESULTS_STATE:** WG2 §Summary #3, EXIT_TOWER E.41 (related claims; not rechecked).

## BISITE F.16 — Forgetting a mark is proper but not smooth

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No marking-forgetting map or BZ lifting obstruction is present. Categorical proper/smooth terminology alone gives no evidence for this geometric example.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.16, line 210; supplied locator: STRATA forgetting-mark question.

**RESULTS_STATE:** WG2 §Summary #3, EXIT_TOWER E.41 (related claims; not rechecked).

## BISITE F.17 — Geometric direct images satisfy the proper boundary comparison

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No geometric boundary direct-image calculation or genus-zero moduli base-change square occurs. The generic R^i f_* notation cannot be substituted for that specified geometric theorem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.17, line 211; supplied locator: STRATA geometric direct image and boundary base change.

**RESULTS_STATE:** WG2 §Summary #3, EXIT_TOWER E.41 (related claims; not rechecked).

## BISITE F.18 — Open higher-indexed derivator base-change problem

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

No extension of derivators to strict higher indexing categories is proposed or checked. The ordinary categorical base-change criteria do not settle the higher Der 4 question.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.18, line 212; supplied locator: Strict nCat-indexing question.

**RESULTS_STATE:** BISITE F.18, BISITE C.10 (related claims; not rechecked).

## BISITE F.19 — Stable cohomological properness of discrete fibrations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No characterization of discrete fibrations by finite-bifibration stable ambidexterity appears. The ordinary discrete (co)fibration observations do not contain the coefficient-sensitive properness theorem.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE F.19, line 213; supplied locator: Mann proper-class question.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.1 — Stability converts homotopy-finite limits into weighted colimits

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No stable derivator, action of spectra, or commuting homotopy-limit/colimit theorem occurs. The finite products in Hot(W) are an unstable ordinary localization result with different hypotheses.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.1, line 214; supplied locator: Lead 4 stable-derivator input.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.2 — Covariant spectral dualizing weight computes limits

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No spectral representables, dualizing weight wS, or derived-coend formula is defined. The manuscript supplies no weighted expression for a right Kan extension.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.2, line 215; supplied locator: Lead 4 dualizing-object and limit-colimit clause.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.3 — Pointwise dualizing twists already fail on one arrow

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The walking-arrow counterexample to a pointwise dualizing-object twist is absent. No such twist is proposed in the manuscript.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.3, line 216; supplied locator: Lead 4 exaggerated objectwise interpretation.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.4 — Kernel coends control transitivity and exact base change

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** unpursued implication.

Scan 017 uses a set-valued profunctor to encode ordinary crossing arrows. It does not define spectral Kan kernels, their derived coend composition, or dualizing-weight transitivity, so the resemblance concerns the type of indexing data only.

- **MPL 118 scan 017:** `H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}`

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.4, line 217; supplied locator: Part G compatibility and transitivity; context/companion/chunks/DER_XIIb-a.tex — Chapter XII §V.1.1, manuscript pp.59–60, Proposition 1: ordinary open–closed profunctor gluing.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.5 — Dualizing weights do not restrict arbitrarily

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No dualizing weight or unrestricted-restriction counterexample is present. The ordinary categorical pullbacks discussed here do not make that stable weight comparison.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.5, line 218; supplied locator: Part G unrestricted dualizing-weight base change.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.6 — Finite coefficient duality reverses diagram variance

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No Spanier–Whitehead duality, perfect-complex duality, or coefficient-ring opposition occurs. Category opposition in scan 009 must not be read as coefficient duality.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.6, line 219; supplied locator: Part G suitable finiteness subcategories.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.7 — Finite EI does not suffice for every stable coefficient theory

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The BC2/F2 obstruction to preservation of countable coproducts is absent. The manuscript's unrelated uncertainty about infinite coproducts after ordinary localization is not this stable coefficient counterexample.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.7, line 220; supplied locator: Part G finite EI scope.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.8 — Invertible group order yields finite-group norm ambidexterity

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No norm transformation, finite-group coefficient hypothesis, or equivalence on unbounded complexes is stated. The groupoid example about products has no such ambidexterity conclusion.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.8, line 221; supplied locator: Part G coefficient-sensitive finite EI class.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.9 — Upper intervals characterize the canonical finite-poset transform

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No Gorenstein-star upper-interval condition or canonical spectral transform VP appears. The finite-product discussion does not classify stable diagram equivalences.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.9, line 222; supplied locator: Lead 4 corrected equivalence; Part G finite posets.

**RESULTS_STATE:** BISITE G.10, STRATA A.4, BISITE D.13 (related claims; not rechecked).

## BISITE G.10 — Least-vertex realization has opposite-poset exits

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

No least-vertex stratification of |NP| or exit-path infinity-category is constructed. The later geometric dictionary therefore has no direct manuscript form here.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.10, line 223; supplied locator: STRATA A.4 A.5; Part G prerequisite dictionary.

**RESULTS_STATE:** BISITE G.10, STRATA A.4, BISITE D.13, STRATA 0.1 (related claims; not rechecked).

## BISITE G.11 — Verdier duality can leave minimum-constructible sheaves

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

The [1] counterexample about minimum constructibility and the canonical covariant transform is absent. The name Verdier on the reused thesis notice is unrelated documentary text, not a discussion of duality.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.11, line 224; supplied locator: Lead 4 unconditional geometric identification.

**RESULTS_STATE:** BISITE G.10, STRATA A.4, BISITE D.13 (related claims; not rechecked).

## BISITE G.12 — A conditional geometric sheaf/cosheaf Verdier identification

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No cosheaf pushforward, covariant Verdier duality, or face-poset upper-interval hypothesis is present. The categorical open–closed gluing calculation does not establish the later geometric identification.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.12, line 225; supplied locator: Part G positive geometric identification.

**RESULTS_STATE:** BISITE G.10, STRATA A.4, BISITE D.13 (related claims; not rechecked).

## BISITE G.13 — The fixed-weight finite-limit formula does not extend unstably

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

No fixed-colimit-weight obstruction for finite limits of spaces is given. The manuscript's unstable homotopy framework does not by itself prove this negative claim.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.13, line 226; supplied locator: Part G unstable clause.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## BISITE G.14 — Tree reflection functors give further stable equivalences

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

No reflection functor, tilting argument, or equivalence across orientations of a finite tree occurs. None of the map-class diagrams asserts a stable equivalence of diagram categories.

**Manuscript evidence:** Explicit absence; no matching scan quotation.

**Context:** context/DOSSIER_STATEMENTS_WITH_STATUS.md — BISITE table, row BISITE G.14, line 227; supplied locator: Lead 4 Groth-Stovicek contribution.

**RESULTS_STATE:** No separately matching RESULTS_STATE identifier located; the BISITE inventory records the return as unreviewed.

## Check-event scope

All 113 rows have an event in `bisite_events.tsv`, under **carried as background without fault found**. Each outcome explicitly says **textual comparison only; mathematical proof not checked**. The record reports comparisons actually performed; it adds no proof-check or counterexample-verification event.

Recorded 2026-11-18T03:06:26+00:00; GPT-6 Astra Pro; inherited reasoning effort is not exposed. Frozen combined SHA-256: `63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149`.


# RESIDUE: all 56 supplied statements

Author: GPT-6 Astra Pro; effort inherited and not exposed. Recorded 2026-11-18T02:58:19+00:00.

Scope: 56 records; exact: 0; partial: 5; analogue: 9; absent: 42; contradicted: 0.

This is a comparison with the frozen text, not a new proof audit. Every supplied status remains a claim of its source. “Absent” assigns no manuscript quotation to the result itself; nearby evidence is explicitly separated. The frozen transcription was not edited.

The key distinction is between the product/diagonal totality used in 118/033–036 and ordinary-final-image totality in XII ms. 88–89. Likewise, a triangle over a common base in 118 is not silently weakened to the literal absolute Theorem A of the later dossier.

## RESIDUE B.1 — Component-dependent W† separates absolute and relative Theorem A

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 235; XVI ms.1–3.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.
- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No component-dependent W†, retract counterexample, or computation of its strong saturation occurs in 118. The saturation assertion at 118/040 is a nearby topic, while 118/026 uses a comparison over a common base; neither identifies the dossier’s literal absolute-axiom class.

## RESIDUE B.2 — Isomorphisms after killing maps factoring through S¹

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 236; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No quotient by maps factoring through S¹, zero-morphism construction, or characterization by homotopy retracts of S¹ occurs in 118. The ordinary localization and saturation discussion is only related background.

## RESIDUE B.3 — Strong saturation does not force relative Theorem A: Wcirc

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 237; XVI ms.1–3, Loc(1bis)/(1ter)+absolute Loc(3).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.
- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No rational-degree circle class Wcirc or its relative-Theorem-A counterexample is present. The theorem at 118/040 cannot be read as a refutation of the supplied row, because 118/026 and 118/040 use comparisons over a common base rather than specifying only the later absolute axiom.

## RESIDUE B.4 — Finite poset witness against relative Theorem A for Wcirc

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 238; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No ten-object to six-object poset map over a three-object base, or degree-two H₂ calculation, occurs in the manuscript. The triangle at 118/026 supplies only a structural comparison with relative Theorem A, not that finite witness.

## RESIDUE B.5 — Homotopies, adjunctions, and initial objects under the literal axioms

**Supplied status:** claim (return: Known)
**Relation:** partial. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 239; XVI Rappel1.2, ms.3.

**Manuscript evidence:**

- **118/025**: `car les homotopismes sont dans $W$` — Homotopisms are explicitly treated as weak equivalences.
- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The explicit sentence at 118/025 supplies the homotopism-in-W portion, and 118/011–014 link the replacement constructions with adjoints and retractions. The full conclusion about naturally homotopic functors, simultaneous membership in W, and initial objects under precisely absolute Loc (3) is not proved or stated with that package here.

## RESIDUE B.6 — Opposition invariance W=W° under absolute Theorem A

**Supplied status:** claim (return: Known)
**Relation:** partial. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 240; XVI Rappel1, ms.2.

**Manuscript evidence:**

- **118/015**: `\uline{Dualité} (y compris $\underline W=\underline W^\circ$)` — The equality is stated in an outline, without the dossier’s complete hypothesis package.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The equation W=W° is written verbatim in the outline at 118/015. This is a direct textual antecedent of the conclusion, but the manuscript does not there spell out or verify the dossier’s exact literal absolute-axiom hypotheses.

## RESIDUE B.7 — Weak and strong split-fibration forms of Proposition 1.3

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 241; XVI Proposition1.3, ms.3–8.

**Manuscript evidence:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.
- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, Proposition 1.3, ms. 3–8. Replacement by split fibrations and the separate weak/relative statements.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The ordinary fibration/cofibration replacements at 118/011–014 and the basewise application at 118/026 are structural analogues of the two parts of XVI Proposition 1.3. Neither equivalence of axiom systems is formulated in 118, and the page’s explicit “but not yet Serre” qualification must be retained.

## RESIDUE B.8 — Absolute localizer axioms do not ensure finite-product stability

**Supplied status:** claim (return: Refuted)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 242; XVI Rappel2.3 and Proposition2.4, ms.9–10.

**Manuscript evidence:**

- **118/032**: `les produits finis existent` — Finite-product existence in the homotopy category is asserted.
- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 8–11; Proposition 2.1, Corollary 2.2, Rappel 2.3, Proposition 2.4, Lemma 2.5. Sums, products, and their hypotheses; companion comments at p9 and p10 distinguish closure from reflection.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The finite-product conclusion being audited appears at 118/032–036, so the later correction is directly relevant to its hypotheses. No counterexample to product stability under only absolute Loc (3) is given here, and the relative use of loc. 3 at 118/026 prevents importing that weaker hypothesis package silently.

## RESIDUE B.9 — Literature distinction between weak and fundamental localizers

**Supplied status:** claim (return: Known)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 243; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §1, ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), Rappels 1 and 1.2. Axiom distinctions and their supplied companion commentary; not the dossier counterexamples.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The later bibliographic distinction between absolute and relative Theorem A is absent from 118. Its common-base application of loc. 3 is the useful manuscript comparison; the Cisinski and Maltsiniotis references remain supplied context rather than independently checked sources in this ledger.

## RESIDUE B.10 — Remaining historical audit of products, decomposition, and Mayer–Vietoris

**Supplied status:** claim (return: Open)
**Relation:** partial. **Note kind:** self-flagged.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 244; no item-specific locator supplied.

**Manuscript evidence:**

- **118/034**: `Cela marcherait pour les produits infinis, si on savait qu'un produit infini` — The extension to infinite products is explicitly conditional.
- **118/029**: `Il semble \uline{faux} que $(\mathrm{Cat})\longrightarrow\overline{\mathrm{Cat}}$ commute aux sommes infinies` — The homotopism quotient is distinguished from the subsequent weak-equivalence localization.
- **118/021**: `au lieu de ponctuelle, il suffit qu'elle soit $\underline W$-asphérique` — A margin weakens the point-fibre hypothesis in the specific opfibration gluing argument.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 8–11; Proposition 2.1, Corollary 2.2, Rappel 2.3, Proposition 2.4, Lemma 2.5. Sums, products, and their hypotheses; companion comments at p9 and p10 distinguish closure from reflection.
- `context/companion/chunks/DER_XVI.tex` — XVI §3, 3.2–3.7, ms. 19–27. Mayer–Vietoris and reversibility; context for the later audit and reversible-localizer questions.
- `context/companion/chunks/DER_XV-b.tex` — XV §9, Propositions 9.4–9.13, ms. 122–133 bis. Decomposition and connectivity statements, including the companion comment on the collapse argument.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The conditional infinite-product passage at 118/034–037, the doubts about infinite sums at 118/029–031, and the gluing discussion at 118/019–023 supply earlier versions of several questions in the proposed audit. They do not complete an audit of XVI ms. 1–27 or XV §9, and their relative comparison arguments do not settle the missing summand-reflection claim.

## RESIDUE B.11 — Finite coproduct closure plus filtered colimits does not imply full Loc (4)

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 245; XVI ms.9, Corollary2.2 parenthesis.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.
- **118/039**: `$I$ un ordonné \deleted{filtrant}` — The word “filtered” is deleted in the filtration statement; additional filtration conditions occur on the page.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 8–11; Proposition 2.1, Corollary 2.2, Rappel 2.3, Proposition 2.4, Lemma 2.5. Sums, products, and their hypotheses; companion comments at p9 and p10 distinguish closure from reflection.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No distinction between coproduct closure and reflection to every summand is stated as the dossier’s counterexample in 118. The forward coproduct argument at 118/026 and the specially conditioned filtration argument at 118/039–040 do not assert full Loc (4).

## RESIDUE B.12 — Formal decomposition, finite localization products, and summand restriction

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 246; XVI2.1,2.2 principal clause,2.5 finite intended version,2.6; XV9.4 formal equivalences,9.5,9.6.

**Manuscript evidence:**

- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.
- **118/032**: `les produits finis existent` — Finite-product existence in the homotopy category is asserted.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 8–11; Proposition 2.1, Corollary 2.2, Rappel 2.3, Proposition 2.4, Lemma 2.5. Sums, products, and their hypotheses; companion comments at p9 and p10 distinguish closure from reflection.
- `context/companion/chunks/DER_XV-b.tex` — XV §9, Propositions 9.4–9.13, ms. 122–133 bis. Decomposition and connectivity statements, including the companion comment on the collapse argument.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** The sums and finite-product calculations in 118 are related precursors to this collection of formal statements. The specific XVI and XV propositions, their minimal identity hypotheses, and their summand-reflection clauses are not all present, so this is not an exact occurrence of the combined dossier row.

## RESIDUE B.13 — π₀ has both adjoints to the discrete-category inclusion after localization

**Supplied status:** claim (return: Known)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 247; XVI second2.8,second2.9,2.11–2.14.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/015**: `\uline{Dualité} (y compris $\underline W=\underline W^\circ$)` — The equality is stated in an outline, without the dossier’s complete hypothesis package.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 12–18; Proposition 2.7 through 2.14. Connectivity and the comparison with discrete categories; a contextual target, not a result found in 118.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No two adjunctions between π₀ and the discrete-category inclusion, or the hypothesis W⊆W₀, are formulated in 118. The opposition outline at 118/015 is merely a nearby duality theme, not this adjunction result.

## RESIDUE B.14 — Elementary cube implications use only Loc (1)

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 248; XVI3.1, ms.18′.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/021**: `au lieu de ponctuelle, il suffit qu'elle soit $\underline W$-asphérique` — A margin weakens the point-fibre hypothesis in the specific opfibration gluing argument.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §3, 3.1, ms. 18′. Elementary cube implications; the later named statement is not written in 118.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No enumeration of the elementary cube implications of XVI 3.1 or proof from Loc (1) alone occurs in 118. The gluing square at 118/021 has separate opfibration and fibre hypotheses and therefore is not the same formal assertion.

## RESIDUE B.15 — Product-closed arrow classes need identities for localization product preservation

**Supplied status:** claim (return: Refuted)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 249; XVI2.5 arbitrary-W literal wording.

**Manuscript evidence:**

- **118/032**: `les produits finis existent` — Finite-product existence in the homotopy category is asserted.
- **118/034**: `Cela marcherait pour les produits infinis, si on savait qu'un produit infini` — The extension to infinite products is explicitly conditional.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 8–11; Proposition 2.1, Corollary 2.2, Rappel 2.3, Proposition 2.4, Lemma 2.5. Sums, products, and their hypotheses; companion comments at p9 and p10 distinguish closure from reflection.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** The product calculations at 118/032–034 concern the same localization operation, but they work with the manuscript’s weak-equivalence classes. They do not exhibit an arbitrary arrow class omitting identities or the finite counterexample to the literal wording of XVI Lemma 2.5.

## RESIDUE B.16 — Near-bijection localizer Wnb retains nontrivial parallel maps

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 250; XVI/XV literal absolute package.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/029**: `Il semble \uline{faux} que $(\mathrm{Cat})\longrightarrow\overline{\mathrm{Cat}}$ commute aux sommes infinies` — The homotopism quotient is distinguished from the subsequent weak-equivalence localization.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 12–18; Proposition 2.7 through 2.14. Connectivity and the comparison with discrete categories; a contextual target, not a result found in 118.
- `context/companion/chunks/DER_XV-b.tex` — XV §9, Propositions 9.4–9.13, ms. 122–133 bis. Decomposition and connectivity statements, including the companion comment on the collapse argument.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No near-bijection class on infinitely many components, finite-coproduct verification, or surviving parallel-map witness is present. The unbounded-homotopy-length example at 118/029 concerns failure of infinite sums in the homotopism quotient and must not be identified with Wnb.

## RESIDUE B.17 — Nontriviality equivalences fail under only absolute Theorem A

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 251; XVI2.7; XV9.9,9.10,9.12,9.13.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/032**: `les produits finis existent` — Finite-product existence in the homotopy category is asserted.
- **118/026**: `Cela résulte alors de loc. 3` — The displayed argument applies the axiom to a triangle over the common base J.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §2, ms. 12–18; Proposition 2.7 through 2.14. Connectivity and the comparison with discrete categories; a contextual target, not a result found in 118.
- `context/companion/chunks/DER_XV-b.tex` — XV §9, Propositions 9.4–9.13, ms. 122–133 bis. Decomposition and connectivity statements, including the companion comment on the collapse argument.

**RESULTS_STATE references:**

- **GALOIS B.1**, line 389: Proved (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.3**, line 377: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No classification of nontrivial localizations or counterexample to the XVI/XV nontriviality equivalences is given in 118. Product and coproduct calculations are relevant to the later proofs, but their occurrence does not resolve the absolute-versus-relative hypothesis issue.

## RESIDUE C.1 — Intrinsic factorization implies universal trivial fibrations and axiom (b)

**Supplied status:** claim (return: Proved)
**Relation:** partial. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 252; no item-specific locator supplied.

**Manuscript evidence:**

- **118/005**: `and also iff it is univ. in $W$` — Universal-weak-equivalence criterion for the manuscript’s Serre class.
- **118/005**: `$S\cap W=S\cap T$` — Serre/weak/trivial-fibre relation, not a theorem for all coefficient localizers.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.
- `context/companion/chunks/DER_XIIc-b.tex` — XII §7, ms. 240–241, footnotes 128–130; comment p240. Left factorization, its scope, and the later homotopy-fibre discussion.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.
- **GALOIS B.14**, line 359: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The manuscript explicitly identifies a Serre weak equivalence with universal membership in W at 118/005, closely matching one conclusion of this row. It does not establish the general theorem from pullbacks, two-out-of-three, and arbitrary weak-equivalence/intrinsic-fibration factorization, nor its slice-level axiom (b).

## RESIDUE C.2 — Nonfunctorial intrinsic factorization preserves all intermediate localizations

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 253; XII ms.215–218,240; XIIc B062 with factorization.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.
- `context/companion/chunks/DER_XIIc-b.tex` — XII §7, ms. 240–241, footnotes 128–130; comment p240. Left factorization, its scope, and the later homotopy-fibre discussion.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No ordinary-and-∞ localization theorem for every intermediate fibrant subcategory is stated in 118. The replacement at 118/011 is explicitly not yet Serre, so it cannot supply the intrinsic-factorization hypothesis of the later result.

## RESIDUE C.3 — Axioms (a) and (b) do not force (c): a five-object counterexample

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 254; XII ms.215–218; XIIc B062 without factorization.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No five-object sixteen-arrow pullback category, comparison of axioms (a), (b), (c), or logical counterexample occurs in 118. Its warning that an ordinary fibration replacement is not yet Serre addresses a different issue.

## RESIDUE C.4 — A bound on objects does not make pullback-category searches finite

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 255; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No exhaustive-search claim, arrow-count bound, one-object pullback-category family, or finite-monomorphism argument is present. The later general-category setting in XII is the relevant context; there is no specific manuscript quotation to attach to this search limitation.

## RESIDUE C.5 — Strictly functorial smooth-and-proper replacement over every base

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 256; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.
- **118/009**: `\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S` — Unqualified smooth/proper-to-Serre implication in the diagram.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 216–218; the subcategory F_{0,S} and perfect representatives. Later replacement setting; does not identify the ordinary fibrations of 118/011 with intrinsic ones.
- `context/companion/chunks/DER_XIIc-b.tex` — XII §7, ms. 240–241, footnotes 128–130; comment p240. Left factorization, its scope, and the later homotopy-fibre discussion.

**RESULTS_STATE references:**

- **BISITE B.21**, line 354: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.14**, line 359: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The functorial ordinary replacements and class diagram in 118 do not construct the asserted coaugmented replacement with both W∞-smooth and W∞-proper values. The “but not yet Serre” annotation is a material limitation on treating those early formulas as the later theorem.

## RESIDUE C.6 — Perfect representatives preserve ordinary and ∞ localizations for every localizer

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 257; XII ms.217, F_0,S.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 216–218; the subcategory F_{0,S} and perfect representatives. Later replacement setting; does not identify the ordinary fibrations of 118/011 with intrinsic ones.

**RESULTS_STATE references:**

- **BISITE B.21**, line 354: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.14**, line 359: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No equivalence theorem for intermediate subcategories containing perfect representatives, uniformly for all fundamental localizers, occurs in 118. The ordinary fibration construction gives a nearby construction to compare, with its explicit Serre qualification retained.

## RESIDUE C.7 — Left intrinsic factorization gives axioms (a)–(c) and derived fibres

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 258; XII ms.240–241, footnotes128–130.

**Manuscript evidence:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.
- **118/005**: `and also iff it is univ. in $W$` — Universal-weak-equivalence criterion for the manuscript’s Serre class.

**Context locations:**

- `context/companion/chunks/DER_XIIc-b.tex` — XII §7, ms. 240–241, footnotes 128–130; comment p240. Left factorization, its scope, and the later homotopy-fibre discussion.
- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.
- **GALOIS B.14**, line 359: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The factorization diagrams at 118/011–014 and universal-weak-equivalence criterion at 118/005 anticipate the ingredients of the later fibre formalism. They do not supply the general implication, derived reindexing identities, or the weakened existence hypothesis of XII footnote 128.

## RESIDUE C.8 — Minimal size of the axiom-(c) counterexample remains unsettled

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 259; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.

**RESULTS_STATE references:**

- **RESIDUE**, line 242: (return, 20261111). Supplied status only; not revalidated here.

**Note:** No minimization problem for a counterexample to axiom (c), and no exhaustive finite-category search, occurs in 118. This remains a supplied open research item, with the XII axiom discussion as context rather than a manuscript solution.

## RESIDUE D.1 — Intrinsic Wn-fibrations detected by truncated homotopy pullbacks

**Supplied status:** claim (return: Known)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 260; XII ms.208,225; XVI §4; I ms.99–100.

**Manuscript evidence:**

- **118/005**: `$S\cap W=S\cap T$` — Serre/weak/trivial-fibre relation, not a theorem for all coefficient localizers.
- **118/005**: `and also iff it is univ. in $W$` — Universal-weak-equivalence criterion for the manuscript’s Serre class.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §§VI.4–5, ms. 208 and 225; intrinsic and relative fibration conditions. Truncation and relative homotopy background for the later classification.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The Serre and universal-base-change criteria at 118/005 and 118/009 are untruncated structural analogues. No τ≤n criterion or complete local test for each Wn is formulated there.

## RESIDUE D.2 — Connecting homomorphism criterion for intrinsic Wn-fibrations

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 261; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/005**: `$S\cap W=S\cap T$` — Serre/weak/trivial-fibre relation, not a theorem for all coefficient localizers.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §§VI.4–5, ms. 208 and 225; intrinsic and relative fibration conditions. Truncation and relative homotopy background for the later classification.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No long exact homotopy sequence, connecting homomorphism πn+1(base)→πn(fibre), or π₁-action criterion at n=0 is present. The manuscript’s aspherical-fibre statement alone does not imply that later classification.

## RESIDUE D.3 — Intrinsic W0-fibrations classified by components and arrow lifts

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 262; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})` — Covering terminology, without a coefficient-dependent monodromy classification.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §§VI.4–5, ms. 208 and 225; intrinsic and relative fibration conditions. Truncation and relative homotopy background for the later classification.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No classification by π₀ of each fibre together with componentwise arrow lifts is stated in 118. Its covering and discrete-fibration terminology is related background, not an occurrence of the W₀ theorem.

## RESIDUE D.4 — Intrinsic fibrations are not a right lifting class for W∞⊆W⊆W0

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 263; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XIIc-a.tex` — XII §VI.4, ms. 208–218; axioms (a), (b), (c), followed by §5 at ms. 218. Intrinsic W-fibrations and intermediate fibrant localizations; companion comments at p215 and p218.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No impossibility theorem for a right lifting class, quantified over all classes of arrows, occurs in 118. The distinction between categorical and Serre fibrations is not itself such a lifting-property counterexample.

## RESIDUE D.5 — Local-coefficient equivalences: π₀, π₁, and universal-cover homology

**Supplied status:** claim (return: Known)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 264; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/005**: `and also iff it is univ. in $W$` — Universal-weak-equivalence criterion for the manuscript’s Serre class.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.

**RESULTS_STATE references:**

- **GALOIS D.2**, line 392: Proved (the return's claim). Supplied status only; not revalidated here.
- **BISITE A.19**, line 381: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No classification for D(k), integral or rational local coefficients, or set/groupoid coefficient stages is given in 118. Its base-change vocabulary is nearby, but it lacks the coefficient-dependent invariants in the supplied statement.

## RESIDUE D.6 — Rational local-coefficient fibrations require only the degree-two boundary

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 265; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/005**: `$S\cap W=S\cap T$` — Serre/weak/trivial-fibre relation, not a theorem for all coefficient localizers.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.
- `context/companion/chunks/DER_XIIc-a.tex` — XII §§VI.4–5, ms. 208 and 225; intrinsic and relative fibration conditions. Truncation and relative homotopy background for the later classification.

**RESULTS_STATE references:**

- **GALOIS D.2**, line 392: Proved (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No rational local-coefficient condition or distinction between the degree-two and higher connecting maps is present. Nothing in the Serre diagram specifies the hypotheses or coefficient theory needed for this result.

## RESIDUE D.7 — General rational local-coefficient and mod-p fibre classification is unsettled

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 266; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/005**: `$S\cap W=S\cap T$` — Serre/weak/trivial-fibre relation, not a theorem for all coefficient localizers.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No rational or mod-p classification with the stated scope, and no analysis of tensoring homotopy boundary maps with a field, occurs in 118. The row is carried with its supplied Open status; no resolution is inferred from the general Serre terminology.

## RESIDUE D.8 — Mod-p homology permits intrinsic coverings with nontrivial p-monodromy

**Supplied status:** claim (return: Refuted)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 267; XII ms.208,225; XVI §4; I ms.99–100.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})` — Covering terminology, without a coefficient-dependent monodromy classification.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No ECp→BCp example or finite-p-group monodromy calculation appears in 118. Its use of “étale covering” does not identify the homology localizer and is not this counterexample.

## RESIDUE D.9 — Arbitrary-spectrum and general homology fibration classification remains open

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 268; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})` — Covering terminology, without a coefficient-dependent monodromy classification.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The manuscript contains no spectrum-dependent classification of intrinsic coverings or of all smooth-and-proper maps. Its class diagram gives context for the question, while the coefficient and monodromy dependencies in the register remain outside these pages.

## RESIDUE D.10 — Forty-eight BISITE B.15 table entries verified by finite examples

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 269; XII ms.208,225; XVI §4; I ms.99–100; BISITE B.15 (all 48 entries).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/009**: `\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S` — Unqualified smooth/proper-to-Serre implication in the diagram.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.
- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No 48-entry table or the collection of finite witnesses occurs in 118. The smooth/proper/Serre diagram is not a verification of the later coefficient-by-coefficient table.

## RESIDUE D.11 — Fibration-axiom table for W0, W1, Wn, WQ, D(Q)lc, and W∞

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 270; XII ms.208,225; XVI §4; I ms.99–100.

**Manuscript evidence:**

- **118/009**: `\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S` — Unqualified smooth/proper-to-Serre implication in the diagram.
- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.
- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** The inclusion of smooth-and-proper maps in the Serre class at 118/009 is a direct point of comparison for the table’s last column. The table across several localizers and its Loc (7a), (7b), (7c), and (7F) entries are absent, so the early unqualified diagram must not be read as asserting the table uniformly for every coefficient theory.

## RESIDUE D.12 — Integral and rational intrinsic coverings have trivial monodromy

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 271; XII ms.208,225; XVI §4; I ms.99–100.

**Manuscript evidence:**

- **118/012**: `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})` — Covering terminology, without a coefficient-dependent monodromy classification.

**Context locations:**

- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.
- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The covering terminology at 118/012 is related to the objects being classified. No integral-versus-rational-versus-mod-p distinction, trivial-monodromy theorem, or connected-covering classification is stated there.

## RESIDUE F.1 — Final-image totality via all covariant set-valued categories of elements

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 272; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.
- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.

**RESULTS_STATE references:**

- **POLES H.2**, line 396: Proved (the return's claim). Supplied status only; not revalidated here.
- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.5**, line 347: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The all-final-images condition and its criterion using every covariant Set-valued functor do not occur in 118. The totality argument at 118/033–035 uses products of representables, whereas XII Definition 1 at ms. 88–89 explicitly uses another notion; no equivalence of the two is assumed here.

## RESIDUE F.2 — Totality gives common successors and integral affine equalizers

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 273; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.
- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.

**RESULTS_STATE references:**

- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.5**, line 347: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No common-successor theorem or augmentation-one integral linear-combination equalizer is present in 118. Its representable-product condition does not state the final-image hypothesis of this later result.

## RESIDUE F.3 — Totality of Δinj subcategories, injection monoids, and free categories

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 274; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.
- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.

**RESULTS_STATE references:**

- **RESIDUE F.3**, line 399: Proved (the return's claim). Supplied status only; not revalidated here.
- **TOTASPH C.10**, line 408: Refuted (the return's claim). Supplied status only; not revalidated here.

**Note:** No Δinj subcategory indexed by S, FinInj example, self-injection monoid, or free-category classification occurs in 118. The shared word “total” is insufficient to connect these final-image examples with the manuscript’s product criterion.

## RESIDUE F.4 — Totality plus a weak terminal object forces filteredness

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 275; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.
- **118/039**: `$I$ un ordonné \deleted{filtrant}` — The word “filtered” is deleted in the filtration statement; additional filtration conditions occur on the page.

**Context locations:**

- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.

**RESULTS_STATE references:**

- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.7**, line 351: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No weak-terminal-object criterion for filteredness, including the finite-object or universal-Cat-colimit variants, is stated in 118. The deleted “filtrant” at 118/039 concerns a separately conditioned filtration argument and supplies no converse theorem about total shapes.

## RESIDUE F.5 — Connected final-image totality versus exact abelian colimits remains open in the row

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 276; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.
- **118/036**: `$\underline W_A$ est formé des seuls iso` — The groupoid note challenges a product-closure implication, not the later final-image totality claims.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.
- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.

**RESULTS_STATE references:**

- **RESIDUE F.5**, line 347: Open (the return's claim). Supplied status only; not revalidated here.
- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **TOTEX D.20**, line 366: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No assertion about exactness of colim_A on abelian groups occurs in 118. The groupoid warning at 118/036 concerns product closure and asphericity, not the integral affine equalization gap in the supplied Open row; this mapping does not reconcile or reclassify later register summaries.

## RESIDUE F.6 — Total integral presheaves versus weak totality and Dwyer-sieve composition

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 277; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.
- **118/023**: `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}` — The page warns that weak equivalences need not survive the indicated unrestricted open/closed pushout.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, ms. 108–114; Definition 2 and total presheaves. Later total-presheaf and strict-asphericity setting; no implication from 118 products is assumed.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.

**RESULTS_STATE references:**

- **RESIDUE F.6**, line 348: Open (the return's claim). Supplied status only; not revalidated here.
- **TOTASPH F.27**, line 342: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No implication from total W_Z-asphericity of a presheaf to total W∞-asphericity, or composition theorem for Dwyer sieves, is stated in 118. The presheaf-product and pushout discussions are only nearby constructions and do not remove the restricted-action issue recorded in the supplied row.

## RESIDUE F.7 — Universal ordinary Cat-colimit comparison versus filteredness without a weak terminal object

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 278; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/039**: `$I$ un ordonné \deleted{filtrant}` — The word “filtered” is deleted in the filtration statement; additional filtration conditions occur on the page.
- **118/040**: `donc on gagne par L3.` — The filtration argument is a comparison over a common ordered base.

**Context locations:**

- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.

**RESULTS_STATE references:**

- **RESIDUE F.7**, line 351: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** The universal ordinary-Cat-colimit characterization of an arbitrary indexing category is absent. The specific filtration argument at 118/039–040, with “filtrant” deleted and additional infimum/minimum-stage conditions, cannot be used as an answer to that universal question or as the Δinj diagram in the dossier.

## RESIDUE I.1 — Smoothness of a map and its strict diagonal characterizes discrete fibrations

**Supplied status:** claim (return: Proved)
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 279; BISITE F.10–F.12 and F.19.

**Manuscript evidence:**

- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.

**Context locations:**

- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.
- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** The discrete-fibration/presheaf dictionary is explicit at 118/012, and the earlier diagrams relate smoothness to ordinary fibrations. The strict-diagonal criterion and its maximality statement are not formulated, so only the underlying objects have a direct textual match.

## RESIDUE I.2 — Universal space-valued ambidexterity of a discrete fibration forces an isomorphism

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 280; BISITE F.10–F.12 and F.19.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.

**Context locations:**

- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.
- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** No comparison of left and right Kan extensions with unpointed space coefficients, or universal ambidexterity classification, occurs in 118. The discrete-fibration dictionary is the nearest object-level link.

## RESIDUE I.3 — Enhanced presheaf functor on correspondences with smooth right legs

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 281; BISITE F.10–F.12 and F.19.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/017**: `H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}` — An ordinary crossing bifunctor; not an enhanced correspondence formalism.
- **118/009**: `\mathrm{Sm}=\mathrm{Pr}^{\circ}` — Opposition exchanges smooth and proper classes.

**Context locations:**

- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.
- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** No lax symmetric monoidal correspondence functor valued in a presentable closed monoidal ∞-category is constructed in 118. Its crossing bifunctor and smooth/proper duality are ordinary categorical ingredients, not the stated coherent enhancement.

## RESIDUE I.4 — A cancellation failure blocks one six-functor formalism specialization

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 282; BISITE F.10–F.12 and F.19.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.

**Context locations:**

- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.
- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** No use of the source’s citation-key GHIJMann2022, Proposition A.5.10, its cancellation hypothesis, or the stated [1]→* counterexample is present in 118. The occurrence of interval and discrete-fibration diagrams does not supply that modern formalism argument.

## RESIDUE I.5 — Opposition gives the proper-leg covariant formalism and discrete opfibrations

**Supplied status:** claim (return: Proved)
**Relation:** partial. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 283; BISITE F.10–F.12 and F.19.

**Manuscript evidence:**

- **118/009**: `\mathrm{Sm}=\mathrm{Pr}^{\circ}` — Opposition exchanges smooth and proper classes.

**Context locations:**

- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.
- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** The smooth/proper opposition formula is explicit at 118/009, and 118/012 also gives the discrete-cofibration/covariant-functor dictionary. The enhanced correspondence theorem, maximal diagonal-stable proper class, and cohomologically étale $f^!=f^*$ conclusion are not present.

## RESIDUE I.6 — Pointed-space ambidextrous discrete fibrations are component inclusions

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 284; BISITE F.10–F.12 and F.19.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.

**Context locations:**

- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.
- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** No pointed-space coefficient theory or universal ambidexterity classification by unions of components is stated in 118. The manuscript’s discrete and summand terminology gives no equality of the two Kan extensions.

## RESIDUE I.7 — Reversible-localizer classification and a bare-derivator iteration remain open

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 285; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/023**: `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}` — The page warns that weak equivalences need not survive the indicated unrestricted open/closed pushout.
- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §3, 3.2–3.7, ms. 19–27. Mayer–Vietoris and reversibility; context for the later audit and reversible-localizer questions.
- `context/companion/chunks/DER_VIII-X.tex` — X §1, ms. 1–5; D-asphericity and the localizer W_D. Derivator/localizer background; not an iterated enhanced-coefficient construction.

**RESULTS_STATE references:**

- **RESIDUE I.7**, line 352: Open (the return's claim). Supplied status only; not revalidated here.
- **POLES F.14**, line 349: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS G.6**, line 346: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS E.11**, line 360: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No classification of reversible accessible localizers or functorial construction D↦D′ on all bare derivators occurs in 118. The pushout warning and saturation theorem are related localizer material, but neither is the reversibility condition or a coefficient-iteration construction.

## RESIDUE I.8 — Spectral and D(k) ambidexterity characterizes finite discrete bifibrations

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 286; BISITE F.10–F.12 and F.19.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.
- **118/012**: `\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})` — Covering terminology, without a coefficient-dependent monodromy classification.

**Context locations:**

- `context/companion/chunks/DER_I-a.tex` — I, ms. 1–9; open/closed decompositions and the adjoint operations. Ordinary derivator operations, used only as the background for the later enhanced correspondence claims.
- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **WG2 §3.2 #7**, line 449: question or plan item of the war game (round 2; unchecked). Supplied status only; not revalidated here.

**Note:** No finite-discrete-bifibration criterion for spectral or D(k) ambidexterity is given. The ordinary covering discussion at 118/012 has no stable coefficient theory or $f^!=f^*$ identification.

## RESIDUE I.9 — Enhanced iterated local coefficients: spectral and mod-p stages

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 287; Prompt I(3), concrete enhanced second stages for spectra and D(F_p); GALOIS E.8/E.10 independently checked; bare-derivator GALOIS E.11/G.6 remains Open.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.

**Context locations:**

- `context/companion/chunks/DER_VIII-X.tex` — X §1, ms. 1–5; D-asphericity and the localizer W_D. Derivator/localizer background; not an iterated enhanced-coefficient construction.
- `context/companion/chunks/DER_I-b.tex` — I, ms. 99–100 and 117–123; cohomological, homological, and strong D-fibrations. Local coefficients and fibrewise base change; not the dossier classifications.

**RESULTS_STATE references:**

- **GALOIS E.11**, line 360: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS G.6**, line 346: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE I.7**, line 352: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No reflective localization of spaces, second locally constant coefficient stage, or finite iteration theorem occurs in 118. Saturation of W is a different construction and does not resolve the bare-derivator question that the supplied row itself leaves open.

## RESIDUE J.1 — Fine Street localization over an ordinary base viewed as a strict 2-category

**Supplied status:** claim (return: Proved)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 288; VI ms.83; BISITE C.10 and F.18.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/015**: `\uline{Dualité} (y compris $\underline W=\underline W^\circ$)` — The equality is stated in an outline, without the dossier’s complete hypothesis package.
- **118/012**: `\text{discrete fibrations}\longleftrightarrow\widehat X` — Ordinary discrete-fibration/presheaf dictionary.

**Context locations:**

- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **BISITE C.10**, line 367: Open (the return's claim). Supplied status only; not revalidated here.
- **BISITE F.18**, line 355: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No Street nerve, strict 2-category undercategory, or enhanced presheaf localization comparison is stated in 118. Its ordinary opposition and presheaf dictionary provide background only, even when the later result restricts the base to an ordinary category.

## RESIDUE J.2 — Recognition over general strict 2-categories remains unproved

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 289; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **BISITE C.10**, line 367: Open (the return's claim). Supplied status only; not revalidated here.
- **BISITE F.18**, line 355: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No base with nonidentity 2-cells, lax comma recognition theorem, or its obstruction is discussed in 118. The companion’s ordinary bi-site passage supplies the contextual question, with no manuscript evidence resolving the higher version.

## RESIDUE J.3 — Higher pullback classes, lax-comma base change, and four variances remain open

**Supplied status:** claim (return: Open)
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 290; no item-specific locator supplied.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/009**: `\mathrm{Sm}=\mathrm{Pr}^{\circ}` — Opposition exchanges smooth and proper classes.

**Context locations:**

- `context/companion/chunks/DER_VI-b.tex` — VI, ms. 81–84, especially ms. 83 and comment p83 “The extra structure hidden in a categorical base”. Ordinary categorical bi-site and fine localization background; no strict higher-category recognition theorem here.

**RESULTS_STATE references:**

- **BISITE C.10**, line 367: Open (the return's claim). Supplied status only; not revalidated here.
- **BISITE F.18**, line 355: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No strict higher-category pullback-class construction, Der4 lax-comma theorem, or four-variance duality is present in 118. The ordinary-category formula Sm=Pr° is not the higher-cell duality theorem cited in the supplied row.

## Limits

- No scan-image examination by this research agent.
- No proof, finite computation, external bibliographic, or priority check.
- Absence is bounded by the complete frozen 118 transcription; companion excerpts are contextual aids.
- The final-image totality of XII ms. 88–89 is not identified with the product/diagonal totality in 118/033–036.
- Absolute and relative Theorem A are not conflated.
- References to original research returns and reviews in NEW_RESULTS were not supplied as those files and were not opened.


# NEW_RESULTS: all 12 numbered and 3 known-after-all statements

Author: GPT-6 Astra Pro; effort inherited and not exposed. Recorded 2026-11-18T02:58:19+00:00.

Scope: 15 records; exact: 0; partial: 0; analogue: 1; absent: 14; contradicted: 0.

This is a comparison with the frozen text, not a new proof audit. Every supplied status remains a claim of its source. “Absent” assigns no manuscript quotation to the result itself; nearby evidence is explicitly separated. The frozen transcription was not edited.

The key distinction is between the product/diagonal totality used in 118/033–036 and ordinary-final-image totality in XII ms. 88–89. Likewise, a triangle over a common base in 118 is not silently weakened to the literal absolute Theorem A of the later dossier.

## NR1 — Finite-monoid finite type, finite dimension, bounded homology, and trivial universal group

**Supplied status:** Claimed proved; source review status: “not yet (Pro check prompt drafted)”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 18; Numbered result 1.
**Supplied manuscript target:** V ms. 51–52 (Hot₀, "types d'homotopie de type fini"); sharpens G.4 of the CATHOT return, the counterexample to Ben-Bassat's Conjecture 7.1.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 51–52; Hot_0 and types of finite homotopy type. Historical question behind the supplied finite-monoid claims; their proof files are not supplied.

**RESULTS_STATE references:**

- **CATHOT G.17**, line 358: Open (the return's claim). Supplied status only; not revalidated here.
- **FINMON**, line 177: (checkpoint 18, 20261116). Supplied status only; not revalidated here.

**Note:** No finite-monoid homology criterion, universal-group theorem, or classification of finite simply connected realizations occurs in 118. The later finite-type question at V ms. 51–52 is the contextual link; neither the new proof nor the cited Ben-Bassat theorem was checked here.

## NR2 — Miller’s Theorem B under a cohomological bound

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 19; Numbered result 2.
**Supplied manuscript target:** the tool for result 1.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 51–52; Hot_0 and types of finite homotopy type. Historical question behind the supplied finite-monoid claims; their proof files are not supplied.

**RESULTS_STATE references:**

- **FINMON**, line 177: (checkpoint 18, 20261116). Supplied status only; not revalidated here.
- **CATHOT G.17**, line 358: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No theorem about maps BG→X with finite, residually finite, or linear fundamental group and a cohomological bound appears in 118. Its role as a tool for NR1 comes from the supplied list, not from these manuscript pages.

## NR3 — Cardinal Kan–Thurston construction and groupoid presentations of invariant ind-objects

**Supplied status:** Claimed proved; GALOIS B.11–B.12 reported followed in full at medium effort and read by an expert at max; OWN_RESULTS §3 not yet checked.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 20; Numbered result 3.
**Supplied manuscript target:** V ms. 46 is a theorem for "local", false for "fibrant"; VII ms. 129–132 and IX ms. 22–23: invariant path ind-categories see only Π₁.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/034**: `Cela marcherait pour les produits infinis, si on savait qu'un produit infini` — The extension to infinite products is explicitly conditional.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 43–46; invariant ind-objects and Thomason–Kan envelopes. Historical ind-object question; the word “Kan” alone is not evidence for the cardinal Kan–Thurston theorem.

**RESULTS_STATE references:**

- **CATHOT E.17**, line 343: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No cardinality-controlled Kan–Thurston theorem or groupoid presentation of invariant ind-objects occurs in 118. The finite/infinite product discussion and the “Kan” condition elsewhere in 118 are different questions, and the supplied open sequential CATHOT E.17 entry is not reclassified by this mapping.

## NR4 — A sphere-retract criterion for uncountably many maps to S²

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 21; Numbered result 4.
**Supplied manuscript target:** D.6 of CATHOT; V ms. 43–46 (with hunch H3).

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 43–46; invariant ind-objects and Thomason–Kan envelopes. Historical ind-object question; the word “Kan” alone is not evidence for the cardinal Kan–Thurston theorem.

**RESULTS_STATE references:**

- **CATHOT D.6**, line 356: Open (the return's claim). Supplied status only; not revalidated here.
- **S2COUNT**, line 249: (final, 20261116). Supplied status only; not revalidated here.

**Note:** No uncountability theorem for [X,S²], sphere-retract hypothesis, or H¹ calculation appears in 118. The supplied historical CATHOT D.6 question and later S2COUNT summary are retained as context, with no reconciliation or proof review undertaken here.

## NR5 — At least 34 arrows for a finite poset of type RP²

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 22; Numbered result 5.
**Supplied manuscript target:** CATHOT G.8.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 51–52; Hot_0 and types of finite homotopy type. Historical question behind the supplied finite-monoid claims; their proof files are not supplied.
- `context/companion/chunks/DER_XIIapp.tex` — XII appendix, ms. 8–11; the four-object two-sphere example and withdrawn retraction. Concrete finite-category context; no census or lower-bound proof was checked.

**RESULTS_STATE references:**

- **CATHOT G.17**, line 358: Open (the return's claim). Supplied status only; not revalidated here.
- **FINMON**, line 177: (checkpoint 18, 20261116). Supplied status only; not revalidated here.

**Note:** No RP² poset, 34-arrow lower bound, or enumeration establishing it occurs in 118. The older bound in the supplied CATHOT G.17 excerpt is not silently updated from this later headline claim.

## NR6 — Small-category census for S¹, S², and S³, including uniqueness clauses

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 23; Numbered result 6.
**Supplied manuscript target:** XII app. ms. 8–11.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/023**: `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}` — The page warns that weak equivalences need not survive the indicated unrestricted open/closed pushout.

**Context locations:**

- `context/companion/chunks/DER_XIIapp.tex` — XII appendix, ms. 8–11; the four-object two-sphere example and withdrawn retraction. Concrete finite-category context; no census or lower-bound proof was checked.

**RESULTS_STATE references:**

- **CATHOT G.17**, line 358: Open (the return's claim). Supplied status only; not revalidated here.
- **FINMON**, line 177: (checkpoint 18, 20261116). Supplied status only; not revalidated here.

**Note:** No census with minima 4, 5, and 7 arrows, uniqueness theorem, or exhaustive enumeration appears in 118. The cone/suspension discussion at 118/023 is related topology but is not the ten-arrow XII appendix model or a minimality calculation.

## NR7 — A reversible fundamental localizer not detected by spectra

**Supplied status:** Claimed proved; source review status: “not yet (prompt REVERSIBLE_LOCALIZERS drafted)”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 24; Numbered result 7.
**Supplied manuscript target:** POLES F.14 (1); XII §5 and XVI §3: the reversibility axiom does not single out homology theories.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/023**: `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}` — The page warns that weak equivalences need not survive the indicated unrestricted open/closed pushout.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §3, 3.2–3.7, ms. 19–27. Mayer–Vietoris and reversibility; context for the later audit and reversible-localizer questions.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, ms. 75–78; W(7 bis) and Théorème 2. Later strong reverse-gluing statement, distinct from the open/closed pushout warning in 118/023.

**RESULTS_STATE references:**

- **POLES F.14**, line 349: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE I.7**, line 352: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No 2-local-sphere nullity class W_S, RP∞/RP² separation, or stable-closure argument appears in 118. The pushout warning concerns a different direction of implication and does not establish or refute the stated reversible-localizer construction.

## NR8 — The strong XII ms. 78 gluing assertion fails for W∞

**Supplied status:** Claimed proved; source reports a checked and recomputed TOTASPH A.13 counterexample and agreement of the return and expert review.
**Relation:** analogue. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 25; Numbered result 8.
**Supplied manuscript target:** XII Th. 4 Cor. 4 and 5, Cor. of ms. 85, Prop. 7, ms. 105, XIIapp ms. 7, 15.

**Manuscript evidence:**

- **118/023**: `Il n'est pas vrai \uline{dans $\mathrm{Cat}$}` — The page warns that weak equivalences need not survive the indicated unrestricted open/closed pushout.
- **118/021**: `au lieu de ponctuelle, il suffit qu'elle soit $\underline W$-asphérique` — A margin weakens the point-fibre hypothesis in the specific opfibration gluing argument.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, ms. 75–78; W(7 bis) and Théorème 2. Later strong reverse-gluing statement, distinct from the open/closed pushout warning in 118/023.

**RESULTS_STATE references:**

- **TOTASPH A.9**, line 407: Known (the return's claim). Supplied status only; not revalidated here.
- **POLES B.2**, line 393: Proved (the return's claim). Supplied status only; not revalidated here.
- **POLES G.5**, line 395: Refuted (the return's claim). Supplied status only; not revalidated here.

**Note:** The warning and counterexample at 118/023 are an earlier related failure of unrestricted open/closed pushout invariance. They are not the connected acyclic nonaspherical join A⋆{t,s} or a statement of strong W(7 bis), while the positive theorem at 118/021 has explicit opfibration and fibre conditions; the broad dependency sentence in NR8 was not audited here.

## NR9 — Trefoil-complement proof that integral and field homology fail Loc (7 F)

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 26; Numbered result 9.
**Supplied manuscript target:** XVI ms. 105 (Grothendieck: "Je ne hasarderais aucune conjecture").

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/011**: `\uline{but not yet} \uline{Serre}` — Explicit qualification on the ordinary fibration replacement.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §4, ms. 37–39 and the later Loc (7 F) discussion; §7, ms. 105. Fibration axiom variants and the question of enough intrinsic fibrations.

**RESULTS_STATE references:**

- **GALOIS B.7**, line 391: Proved (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE D.9**, line 365: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No trefoil complement, homology-localizer comparison, or failure of enough intrinsic fibrations occurs in 118. Its warning that an ordinary replacement is not yet Serre anticipates a distinction, not the coefficient-specific counterexample at issue.

## NR10 — Simply connected Y inherits final-image totality from its path presheaf

**Supplied status:** Claimed proved; source review status: “not yet”.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 27; Numbered result 10.
**Supplied manuscript target:** XII ms. 102–103, 112.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.

**Context locations:**

- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, ms. 102–103 and 112; path objects and totality. Historical total-path question; it uses Definition 1 at ms. 88–89.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.

**RESULTS_STATE references:**

- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.5**, line 347: Open (the return's claim). Supplied status only; not revalidated here.

**Note:** No assertion for Ch(Y;y₀,−) and simply connected Y is present in 118. The use of totality in its product criterion is not enough to import the later final-image path-presheaf implication.

## NR11 — Δinj refutes total-implies-filtered, with the exact-abelian-colimit bridge

**Supplied status:** Claimed proved; source reports checks at medium and max effort, recomputation, and tracing to Isbell–Mitchell.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 28; Numbered result 11.
**Supplied manuscript target:** II ms. 36–36ter.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.
- **118/039**: `$I$ un ordonné \deleted{filtrant}` — The word “filtered” is deleted in the filtration statement; additional filtration conditions occur on the page.

**Context locations:**

- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.

**RESULTS_STATE references:**

- **TOTASPH C.10**, line 408: Refuted (the return's claim). Supplied status only; not revalidated here.
- **TOTASPH D.7**, line 353: Open (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.3**, line 399: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** Neither Δinj nor the exact-abelian-colimit bridge appears in 118. Its product-based totality at 118/033–035 and the deleted “filtrant” at 118/039 concern different statements, so these pages do not supply the stated counterexample to II ms. 36ter.

## NR12 — RP² cannot be the classifying space of a finite monoid

**Supplied status:** Claimed proved; source reports medium-effort completion and checks, then max-effort rechecking from primary texts.
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 29; Numbered result 12.
**Supplied manuscript target:** sent to the author on 12 Nov 2026.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/companion/chunks/DER_III-V.tex` — V, ms. 51–52; Hot_0 and types of finite homotopy type. Historical question behind the supplied finite-monoid claims; their proof files are not supplied.

**RESULTS_STATE references:**

- **CATHOT G.17**, line 358: Open (the return's claim). Supplied status only; not revalidated here.
- **FINMON**, line 177: (checkpoint 18, 20261116). Supplied status only; not revalidated here.

**Note:** No RP² finite-monoid obstruction or finite-dimensional universal-group theorem occurs in 118. The result’s reported checks and communication to its cited author are supplied provenance only and were not repeated in this mapping.

## NR-K1 — Isbell–Mitchell’s affine filteredness result for the injection category

**Supplied status:** Known after all (source label; no independent literature verification in this ledger).
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 31; Known after all, statement 1.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/035**: `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}` — The criterion uses products of representables; it is not the XII final-image definition.
- **118/039**: `$I$ un ordonné \deleted{filtrant}` — The word “filtered” is deleted in the filtration statement; additional filtration conditions occur on the page.

**Context locations:**

- `context/companion/chunks/DER_II-a.tex` — II, ms. 36–36ter; comment dgrb108, “Total asphericity is not filteredness”. Companion statements on categories of elements, exact abelian colimits, Delta_inj, and the weak-terminal case; treated as supplied claims.
- `context/companion/chunks/DER_XIIb-a.tex` — XII §V.2, Definition 1, ms. 88–89. Totality is defined through every ordinary final image p_!; the edition explicitly distinguishes this from Pursuing Stacks totality.

**RESULTS_STATE references:**

- **TOTASPH C.10**, line 408: Refuted (the return's claim). Supplied status only; not revalidated here.
- **RESIDUE F.3**, line 399: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No affine completion of the injection category or Isbell–Mitchell theorem is stated in 118. The companion’s discussion at II ms. 36–36ter gives the relevant attribution, whereas the manuscript’s product criterion and filtration theorem are only nearby topics.

## NR-K2 — Uniqueness in Nielsen realization attributed to Harvey (1971)

**Supplied status:** Known after all (source label; no independent literature verification in this ledger).
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 31; Known after all, statement 2.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Manuscript scan/quotation:** None; no meaningful item-specific occurrence was found.

**Context locations:**

- `context/NEW_RESULTS.md` — “Known after all”, second statement (Harvey 1971); no chapter or manuscript-page locator supplied. This is the only item-specific supplied reference; Nielsen/Harvey searches in all companion chunks found no match.

**RESULTS_STATE references:**

No item-specific Nielsen or Harvey entry was found in the supplied RESULTS_STATE; no unrelated ID is substituted.

**Note:** No Nielsen realization, mapping-class-group action, or uniqueness theorem appears in 118 or in the searched companion chunks under Nielsen or Harvey. The only supplied specific locator is NEW_RESULTS, “Known after all”, second statement; no related manuscript scan, companion chapter, or RESULTS_STATE item is fabricated.

## NR-K3 — Special localizers are accessible fundamental localizers, attributed to Cisinski Corollary 4.2.22

**Supplied status:** Known after all (source label; no independent literature verification in this ledger).
**Relation:** absent. **Note kind:** reading question.

**Source:** `context/NEW_RESULTS.md`, line 31; Known after all, statement 3.

**Absence:** Absent as stated from the complete frozen MPL_118 transcription; no scan or quotation is assigned as an occurrence of this result.

**Nearest related evidence only:**

- **118/040**: `L'ens. $\underline W$ est saturé` — Strong-saturation theorem announcement; its exact axiom package is not reconstructed here.

**Context locations:**

- `context/companion/chunks/DER_XVI.tex` — XVI §5, ms. 75–79; Loc (9), with XV §8 as its model-category background. Accessibility context; the Cisinski citation in NEW_RESULTS is a supplied bibliographic claim only.

**RESULTS_STATE references:**

- **GALOIS B.13**, line 345: Open (the return's claim). Supplied status only; not revalidated here.
- **GALOIS B.4**, line 390: Proved (the return's claim). Supplied status only; not revalidated here.

**Note:** No equivalence between special localizers and accessible fundamental localizers is stated in 118. Strong saturation at 118/040 is a different property, and the precise Cisinski attribution is carried as supplied rather than checked against the publication.

## Limits

- No scan-image examination by this research agent.
- No proof, finite computation, external bibliographic, or priority check.
- Absence is bounded by the complete frozen 118 transcription; companion excerpts are contextual aids.
- The final-image totality of XII ms. 88–89 is not identified with the product/diagonal totality in 118/033–036.
- Absolute and relative Theorem A are not conflated.
- References to original research returns and reviews in NEW_RESULTS were not supplied as those files and were not opened.
