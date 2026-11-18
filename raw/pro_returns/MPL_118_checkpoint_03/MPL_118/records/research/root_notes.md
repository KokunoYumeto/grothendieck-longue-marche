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

