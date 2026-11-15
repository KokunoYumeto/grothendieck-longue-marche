# MPL_105 — Research notes

## Scope, evidence, and citation conventions

These notes concern all 48 retained scans of Montpellier cote 105: scans 002–053, excluding 009, 024, 029, and 042. The transcription was completed and audited against the images before it was frozen at **2026-11-15 20:35:11 UTC**; the context archive was opened only afterwards. Nothing in the contextual comparison has been used to change the frozen page files or the combined transcription. The primary assistant alone read the manuscript images and wrote the substantive comparisons; assistance was confined to mechanical packaging and validation.

**Evidence levels.** A manuscript assertion, a manuscript proof attempt, an editorial commentary, a research-return claim, and a reported independent review are distinguished throughout. “Claim (return: Proved/Known/Refuted/Open)” below reproduces the supplied register's status, not a fresh certification of its mathematics; where `NEW_RESULTS.md` reports a review, the note says exactly that. The quoted words come from the frozen transcription, with consequential uncertainties retained. A struck-through passage is evidence of an abandoned formulation, not automatically evidence of a mathematical counterexample.

**Locators.** “105/052” means cote 105, PDF scan 052; “ms.” means a number written on the sheet or a manuscript-page reference supplied by the context. Physical locations and quoted incipits are used where reconstructing a numerical manuscript line would create false precision; the frozen fragment's line numbering is not substituted for the manuscript's lineation. Context files generally supply manuscript pages and claim IDs, not the original PDF scan numbers: no context scan number has been invented. Dossier locators are given for each of its 255 rows, including rows for which its manuscript-reference cell is empty.

**Coverage.** Sections below record the principal findings, the author's verification flags, titles and counts, every one of the 12 numbered new-result entries, and every one of the 255 dossier statements separately. “No form found” is a bounded negative finding from this package, not a claim about the rest of the Montpellier archive. Citations follow author–date practice where authorship is identifiable; the supplied research registers are cited by title, ID, and file because their individual return authors and primary proofs are not all present here.

## Principal findings and research connections

### R01 — What this package adds

**Location:** 105/005–040, especially 012–020 and 034–040; 043–053. **Kind:** unpursued implication / source comparison.

The English sequence develops interval-generated lifting classes, Quillen pairs and triples, and a functorial transfinite factorization; the French sequence seeks excision axioms for a derivator and explicitly strengthens W7. The manuscript's own summaries, “We have to develop mainly a criterion to get factorization” (030) and “Forme renforcée de W7 p. 9” (052), identify these two threads without turning either into a finished general theory. They bear directly on the supplied state entries `105-interval-anodyne-generators`, `105-derivator-crible-excision`, PATHS D.18/D.22, TOTASPH A.9/A.13, and RESIDUE I.7; the more remote dossier topics are audited individually below.

### R02 — First mention of the strengthened excision problem

**Location:** 105/043, heading and upper argument; 046, right-hand leaf. **Kind:** self-flagged / unproved claim.

The earliest named occurrence within the retained scans is the uncertain heading “Dém. de W7, W(7bis) et W=WD?” on 043; it names a task rather than stating the full strengthened axiom. An earlier cancelled block on that same scan already contains `q∈W ⇔ q_U∈W`, but its surviving text does not identify this as the complete strengthened two-open inclusion axiom (see Q11). On 046 an isomorphism biconditional is proposed for the cohomology square, but the actual concluding W-statement is only `i'_0 ∈ W_D ⇒ i' ∈ W_D`, and the crucial square assertion is marked “à vérifier.” These are distinct evidentiary stages, relevant to TOTASPH A.9/A.13 and the Hua finding discussed in R15.

### R03 — First explicit reverse W-implication

**Location:** 105/047, opening paragraph. **Kind:** conjecture / unproved claim.

The first explicit reverse inclusion-form implication whose role in the W7 cover argument is identified in the retained text is introduced by “Pour avoir l'implication inverse,” followed by `i ∈ W_D ⇒ i_0 ∈ W_D` and the requirement that the coherent square be cocartesian. The words “il faudrait savoir” and the later “Moralement” make this an identified missing step, not a proof of reversibility from the preceding axioms. Compare `companion/chunks/DER_XIIb-a.tex`, ms. 75–78 and 79, and `notes/RESULTS_STATE.md`, TOTASPH A.9 and POLES B.2: the later context explicitly separates forward gluing from the additional reverse demand.

### R04 — First complete strengthened square axiom

**Location:** 105/052, right-hand leaf, ms. 17, W7 bis. **Kind:** unproved claim / proposed axiom.

The first standalone complete biconditional is W7 bis on 052: `i_a ∈ W ⇔ i'_a ∈ W` and `i_b ∈ W ⇔ i'_b ∈ W`, preceded by “Forme renforcée de W7 p. 9.” Its construction uses the total category associated with a three-object diagram and a square in `Hot_W`; it is more general in presentation than merely spelling out an ordinary union of two sieves. In the supplied companion, XII ms. 75–76 calls the two-open square axiom W(7 bis), so the close relation is substantive, while identification of the two formulations requires the comparison between this total-category construction and the relevant cover square (TOTASPH A.9; `DER_XIIb-a.tex`). A particularly close later form is Proposition 13, XII ms. 125–126 (`DER_XIIb-b.tex`), which explicitly makes that comparison and states the corresponding two biconditionals under strong W(7 bis).

### R05 — The cube changes its name

**Location:** 105/052, lower right, W8 bis; 053, lower half. **Kind:** unproved claim / reading question.

W8 bis on 052 states “Alors deux de ces conditions entraînent la troisième” for the total-category cube, whereas XII ms. 76–78 calls the corresponding two-of-three cube principle W(7), not W8. The first condition's glyph remains `f|f_a` in the frozen transcription; interpreting it as the total map `f` makes the parallel with XII especially transparent, but that contextual attraction does not decide the ink. The comparison therefore records both the structural correspondence and this unresolved reading, against BISITE A.33, RESIDUE B.10/B.14, and TOTASPH A.13.

### R06 — No “totalement asphérique ⇒ filtrant” in cote 105

**Location:** all retained scans, with the nearest different use at 105/018 and 034–040. **Kind:** source comparison; no form found.

No assertion that total asphericity implies filteredness was found in this package; “filtering direct limits” in the model-category construction concerns closure and smallness, not the total-asphericity quantifier. In the supplied context the question is already explicit in `DER_II-a.tex`, ms. 36: “cela implique-t-il que X soit filtrante ?”, and its subsequent ms. 36bis–36ter discussion must be read together with the retractions and renewed conjecture, indexed by II-C-003. `NEW_RESULTS.md` 11 and `RESULTS_STATE.md` TOTASPH C.10 report the Δ_inj counterexample and reviews; cote 105 adds no earlier occurrence or proof, and these materials alone do not establish an archive-wide first date.

### R07 — Chronology cannot be read off recycled paper

**Location:** 105/006–041, printed support dates; 043–053, undated handwriting. **Kind:** reading question / chronological limitation.

The printer records include dates in 1982, but these date the reused printouts, not the act of writing the notes. The context README asks for “1983 forms” across a larger group of cotes; neither its research plan nor the catalogue's “[à partir de 1982]” supplies a dated autograph statement here. Thus R02–R05 establish first occurrences in the order of this package only, while the relationship to the 1990–91 *Dérivateurs* and the dated *Pursuing Stacks* extracts is a textual comparison rather than a demonstrated compositional chronology.

### R08 — Relative Theorem A is not stated here

**Location:** all mathematical leaves, especially 105/045–046. **Kind:** source comparison; no form found.

The construction with `α:X→X̄` and the fibrewise cohomology calculation does not state the general relative Theorem A with a comparison of comma categories over every object of a common base. The phrase “car α:X→X̄ est ∈ W” on 046 is a particular assertion used inside the excision argument, not a replacement for that theorem's hypotheses. The README's question about cotes 117–118 therefore remains outside this package; compare RESULTS_STATE GALOIS B.1/B.3 and dossier BISITE A.32 and RESIDUE B.1–B.4, which carefully distinguish absolute and relative versions.

### R09 — Starting from W and constructing auxiliary classes

**Location:** 105/032, NB; 005–007 and 030. **Kind:** unpursued implication.

“W is given beforehand in a rather tangible way, by cohomological criteria” is an explicit methodological choice, followed by the problem of recovering `TC=C∩W` from generators. It is a close conceptual parallel to *Pursuing Stacks* VI §125, ms. 530–532 (`ps_chapters_VI_VII/ps6.tex`), where the weak equivalences are basic data and the role of auxiliary fibrations and cofibrations is questioned. The latter passage does not by itself verify the construction here, and this note adds a comparison of outlook rather than an identity of proofs (BISITE A.22/A.27; PATHS D.18/D.22).

### R10 — Interval generators are conditional input to a model structure

**Location:** 105/012–018, especially 014, upper and lower paragraphs. **Kind:** unproved claim / method.

The construction `h(i_0,I,ε)` uses monomorphisms and sections of W-aspheric intervals to generate candidate trivial cofibrations, but 014 says “We do not know yet M1 ... nor M5” and temporarily assumes the two factorizations. The closure calculations and universal-interval condition are consequently intermediate pieces of a recognition argument, not an unconditional construction for every localizer. Compare `DER_XIX.tex`, §1, ms. 2–7, and the state entries PATHS D.18/D.22 and BISITE A.27/A.28; the later small-generation theorem supplies a close methodological counterpart, with explicit size hypotheses.

### R11 — Two inclusions, two separate problems

**Location:** 105/016–020, especially 020 opening. **Kind:** unproved claim / unpursued implication.

“We still have to see if W⊂W̃” on 020 separates the reverse inclusion from the preceding conditions aimed at `W̃⊂W`. The proposed reductions `F∩W⊂TF` or `C∩W⊂TC`, and the warning that using only L would force a single particular W, show why the supply of eligible intervals matters. This sharpens the Hua interval-generator claim and bears on PATHS D.18/D.22 and BISITE A.22/A.27: an orthogonality construction and agreement with the prescribed weak equivalences are distinct verification tasks.

### R12 — The factorization theorem keeps its smallness hypothesis

**Location:** 105/034–040, ending of 040. **Kind:** unproved claim / stated open extension.

The final theorem retains a small generating family and ends “Next step is to try to get rid of this,” rather than supplying the promised removal. The attachment construction, accessibility bounds, and functoriality on 034–038 are the substantive progress, closely matching `DER_XIX.tex`, Theorem 1.1, ms. 5–7, whose statement also assumes a small generating family and accessible objects. This is evidence of a method and a remaining size obstacle for PATHS D.22 and RESULTS_STATE GALOIS B.13, not an answer to accessibility for arbitrary derivators or arbitrary fundamental localizers.

### R13 — Filtering colimits versus continuous ordinal composites

**Location:** 105/038, “What about d)?”; 040, lemma. **Kind:** self-flagged / own idea.

The general filtering-limit closure question on 038 is followed by a lemma about a continuous ordinal construction on 040, and the latter should not silently be substituted for every filtered diagram. **Own idea, high confidence:** separate the needed small-object argument into successor attachment and limit-stage compatibility, then test whether the claimed general filtered-colimit closure is actually used; the reason is that compatible fillers along a continuous chain are exactly the data supplied by the transfinite construction. The supplied `DER_XIX.tex`, ms. 2–5 and its commentary on transfinite closure, makes this distinction explicit; it bears on BISITE A.28 and PATHS D.17/D.22 without settling the stronger closure claim.

### R14 — Checking Hua's interval finding

**Location:** 105/012, 014, 016, 018, with continuation 020–022. **Kind:** source comparison.

**Hua, findings register, `105-interval-anodyne-generators`: substantially supported as a description of the construction, with qualifications.** The interval pushout-products, universal-W condition on the Lawvere object, and closure program are present, while 014 still assumes factorization and 020 still asks for agreement with the original W. The register's Ω notation is not a reason to replace the frozen `L_A` reading on 016, and its listed intervening scans 013/015/017 are reused printer faces rather than additional mathematical arguments (`RESULTS_STATE.md`, findings register; see also R10–R12).

### R15 — Checking Hua's excision finding

**Location:** 105/043, 045–047, and 051. **Kind:** source comparison / self-flagged.

**Hua, findings register, `105-derivator-crible-excision`: the forward-excision target and construction are supported, but the description of a completed derivation “from the derivator axioms alone” needs qualification.** The decisive square criterion on 046 is explicitly “à vérifier (ou à ... mettre en axiome ...),” and 047 identifies a further cocartesian requirement for the inverse implication. The later lemma on 051 helps isolate the isomorphism-edge issue, but it does not erase the earlier flag or prove the proposed universal bicartesianness (`RESULTS_STATE.md`, same ID; TOTASPH A.9/A.13; POLES B.2).

### R16 — Coherent squares carry more information than skeletal ones

**Location:** 105/046–047, distinction between σ and the diagramme squelettique. **Kind:** unpursued implication.

The text carefully constructs `σ∈D(Δ¹×Δ¹)` and distinguishes it from the square visible in the value category; 047 asks for cocartesianness of the abstract square. That distinction is a genuine methodological contribution to the later comparison problem `Ho Fun(I,C)→Fun(I,Ho C)`: a commuting diagram of objects alone is not the coherent datum used by a derivator. Compare dossier PATHS D.20 and BISITE E.13 and the companion's Chapter IX diagram discussion; the manuscript anticipates the distinction but gives no general fullness, faithfulness, or rectification theorem.

### R17 — A proposed derivator axiom becomes a stability question

**Location:** 105/049–050, Der 6 and Der 6′. **Kind:** conjecture / own idea.

The manuscript first proposes a specific square condition and then the stronger statement that a square is cartesian if and only if it is cocartesian. **Own idea, high confidence:** examine that stronger proposal in an explicitly pointed stable derivator before extending it to the unpointed homotopy theory of spaces, because the identification of cartesian and cocartesian coherent squares is exactly the extra structure being demanded here. This gives a controlled comparison with STRATA D.2, BISITE G.1, and BISITE A.33; it neither identifies all reversible localizers with stable theories nor supplies the bare-derivator construction left open in RESIDUE I.7.

### R18 — The same-sheet retraction is decisive

**Location:** 105/052, upper left statement and marginal “Complètement faux.” **Kind:** withdrawn in the same text.

The assertion “Tout carré cocartésien est cartésien” in Hot, followed by a π₀ condition for the converse, is explicitly rejected in the margin on the same scan. Both the original statement and the rejection must remain visible when relating 050's proposed Der 6 to 052's Der 8; the package cannot be cited as an unqualified endorsement of stability for Hot. Compare `DER_XIIb-a.tex`, ms. 78–80 and commentary blocks dgrb516–517, NEW_RESULTS 8, and BISITE G.13: those materials explain a related forward/reverse distinction, but do not license replacing this local retraction with a different theorem.

### R19 — The nonformal part of the five-lemma proposal

**Location:** 105/052, Der 8, middle left and margin. **Kind:** self-flagged / own idea.

The author separates the cartesian implication `b+c⇒a`, the cocartesian implication `a+c⇒b`, and the additional `a+b⇒c`, marking the last with “?”. **Own idea, high confidence:** the final implication should be checked as a conservativity assertion for the two remaining vertices, with the coherent square hypotheses kept intact, because ordinary existence of limits and colimits does not by itself state that conservativity. This is the exact issue isolated in BISITE A.33 and RESIDUE B.14, while BISITE G.1 suggests a stable setting in which a triangle argument is a plausible route rather than a proof supplied here.

### R20 — Reverse excision is not a theorem about arbitrary homotopy types

**Location:** 105/047, 050, 052; comparison to XII ms. 78. **Kind:** source comparison / contradiction with a supplied reviewed claim.

The proposed unrestricted reverse implications meet the counterexample reported as reviewed in NEW_RESULTS 8 and TOTASPH A.13: the union of two cones on a connected acyclic noncontractible category can lose the obstruction retained by the intersection. The supplied `DER_XIIb-a.tex`, ms. 78, dgrb517, gives the categorical construction and distinguishes it from the valid forward pushout implication; these notes use that reported and displayed comparison rather than claiming a new counterexample. Cote 105 adds the explicit intermediate doubts and same-sheet withdrawal, not a repair of XII's later unqualified theorem.

### R21 — “Homology only” is too strong a classification conclusion

**Location:** 105/052, W7 bis/W8 bis. **Kind:** own idea / caution about comparison scope.

**Own idea, high confidence:** retain “additional reversibility axiom” as the conclusion of the comparison, because failure for W∞ does not logically classify every localizer that satisfies the strengthened axiom. NEW_RESULTS 7 itself reports an unreviewed reversible localizer not detected by spectra, whereas the wording in NEW_RESULTS 8 says “homology localizers only”; those two claims must not be collapsed into an established classification. This qualification bears on POLES F.14(1) and RESIDUE I.7 and does not decide either open classification.

### R22 — Constant coefficients and locally constant coefficients

**Location:** 105/045–047, especially the expanded coefficient remark on 046 and cancelled clause on 047. **Kind:** conjecture / unpursued implication.

The calculation begins with constant coefficients, 046 emphasizes “pas seulement ξ constant,” and 047 explores a locally constant qualification before striking part of it out. This is evidence that the coefficient scope matters to the proposed reverse argument, not a completed construction of a locally constant derivator or a proof that proper maps preserve locally constant coefficients. Compare RESULTS_STATE GALOIS D.2, BISITE A.19/A.20, and GALOIS E.11/G.6, together with RESIDUE I.7/I.9; the latter's enhanced constructions do not retroactively settle the bare-derivator proposal here.

### R23 — Path-space fibrations remain a cancelled question

**Location:** 105/003, entire cancelled sheet. **Kind:** conjecture / self-flagged.

“Il semblerait que p soit une W∞-fibration” and “C'est une chose à vérifier” follow distinctions between categorical fibrations, cofibrations, and cohomological properness/smoothness. The sheet's question about obtaining a Quillen structure on Cat must not be read as an existing strict bifibration replacement, especially because the exact path-category convention is not developed on this sheet. Compare PATHS E.1/E.3/E.4/E.11, BISITE B.8/B.19/B.21, and RESIDUE C.5: their different full, weak-vertical, and eventual path constructions cannot be identified with `Ch(C)` solely by the notation.

### R24 — Model fibrations and intrinsic fibrations need separate tests

**Location:** 105/003, 022, 030–032. **Kind:** unpursued implication.

The English construction defines F by a right lifting property and adds stability of W under pullback along F as a further requirement; the French cancelled question uses W∞-fibration language without supplying the same identification. Thus the later register's warning that intrinsic fibrations need not form a right lifting class does not contradict a theorem proved here: the package has not shown equality of the two classes. Compare BISITE A.2/A.11/A.22 and RESIDUE D.4, together with the source's “strict Quillen triple” condition 4 on 032.

### R25 — Cofibrations in Cat and monomorphisms in a topos

**Location:** 105/012–018 versus 002–003. **Kind:** reading question / unpursued implication.

The interval pushout-product calculation is explicitly made in a topos with `C=monomorphisms`, whereas the early French leaves concern categories and W∞. Consequently the failure of a particular intrinsic Cat-cofibration pushout-product in PATHS E.7 or TOTASPH F.23 is not a counterexample to the same assertion in the same ambient category on 012. A comparison would have to specify the passage from presheaves to categories of elements and show that it transports the required cofibration class; no such transport theorem is supplied on these pages.

### R26 — Properness here is base-change properness

**Location:** 105/045 and 051, “propre” and “lisse”; 032 condition 4. **Kind:** unpursued implication.

The cofibred replacement on 045 and the map ρ on 051 are used for fibrewise Kan-extension calculations, while 032 asks for base-change stability of weak equivalences. *Pursuing Stacks* VII §§136–137, ms. 569–577 (`ps7.tex`), explicitly separates cohomological properness/smoothness from stronger finiteness and duality requirements. The package therefore bears on STRATA D.3/D.4 and BISITE F.1/F.2, but does not supply the six-operation correspondence theory or geometric proper-map classifications in BISITE F.10–F.19 and RESIDUE I.1–I.8.

### R27 — The dualizing-object expectation has no displayed construction

**Location:** 105/050, middle paragraph. **Kind:** conjecture / unproved claim.

“Je ne vois pas comment l'un impliquerait l'autre” introduces the possible role of a dualizing object in relating the two provisional axioms. No dualizing weight, functor, finiteness criterion, or coherence theorem is then constructed. Compare *Pursuing Stacks* VII §136, ms. 568–570, and dossier BISITE G.2–G.7 and F.10/F.13: these are useful later comparison targets, not formulas already present in cote 105.

### R28 — Shifted derivators are explicitly part of the proposed test

**Location:** 105/051, margin, and 052 Der 8. **Kind:** unpursued implication.

The marginal demand that the condition hold for the shifted derivators D_I shows that the author is seeking a diagramwise axiom, not merely an identity in D(e). This bears on PATHS D.20/D.21 and BISITE E.13/F.13, but does not imply that all diagram categories are recoverable from the value category or that a correspondence enhancement has been supplied. It is a useful constraint on any proposed repair of Der 6/Der 8: the repair should survive shifts, a requirement that can be tested independently of the undecided reverse-excision claim.

### R29 — The last page is a corollary program

**Location:** 105/053, W7 ter/W8 ter. **Kind:** unproved claim / reading question.

The final leaf proposes proper/smooth variants after the general total-category axioms, but writes no proofs of the strengthened conclusions. The suffix remains uncertain between “ter” and “bis,” and the upper Φ diagram visibly has `a→0→b` while the lower one has both `a,b→0`; a later conventional fork is not evidence for changing either drawing. Compare XII ms. 125–126 and 147–149 in `DER_XIIb-b.tex`, and dossier STRATA D.4 and BISITE F.2: they are substantive comparison points whose hypotheses and variances must be matched before identifying the claims.

### R30 — Saturation terminology is being worked out

**Location:** 105/005, 025, cancelled 027, and 028. **Kind:** self-flagged / source comparison.

“mild saturation,” stability under direct factors, the two-sided-composite condition, lifting saturation, and strong saturation at localization occur as distinct, sometimes questioned notions. The explicit doubt on 028 about retract stability and the attribution to Quillen under finite direct/inverse limits should be preserved instead of retrofitting one later standard definition onto every occurrence. This bears on BISITE A.1/A.27/A.29 and RESIDUE B.9, and compares directly with the later distinctions between Q-closure and Q-saturation in `DER_XIX.tex`, ms. 2–7.

### R31 — A proof obligation behind the Lawvere-object criterion

**Location:** 105/016, main argument and diagonal margin. **Kind:** reading question / unproved claim.

The readable main argument reduces `TF⊂W` to a universal-W condition on an injective separating interval, while the difficult annotation culminates in “because the Lawvere object is injective!!!”. The diagonal words about adjoining or embedding remain low-confidence in the transcription, so they cannot carry a reconstructed proof of the universal comparison. The context's Ω formulation in `105-interval-anodyne-generators` is a lead for a later independent proof and an alternative notation to discuss, not authority to replace the ink-first reading `L_A`.

### R32 — A focused continuation of the mathematical investigation

**Location:** 105/020, 032, 040, 047, 052. **Kind:** own idea.

**Own idea, high confidence:** the next useful investigations are the exact equality between interval-generated TC and `C∩W` under stated smallness assumptions, and a hypothesis-by-hypothesis repair of the reverse square/cube axioms, because those are precisely the unresolved transitions marked in the source. The first belongs under PATHS D.18/D.22 and BISITE A.27/A.28; the second under TOTASPH A.13, BISITE A.33, and RESIDUE I.7. This is a research agenda extracted from the manuscript, with no claim of novelty and no re-derivation of the results already reported as reviewed.

### R33 — The coefficient scope of the replacement equivalence

**Location:** 105/045–047, α and the passage beyond constant coefficients. **Kind:** own idea / reading question.

**Own idea, high confidence as a proof obligation:** when passing from the constant-coefficient calculation to arbitrary ξ, specify exactly which equivalence class contains α and which coefficient restriction it controls, because membership in a constant-coefficient class does not itself state the stronger all-coefficient comparison. The cancelled “D-équiv. 2-complète” clause on 047 is evidence that the source itself considered a strengthened hypothesis, while the exponent on `W_Ψ^g` on 045 remains uncertain. This connects to BISITE A.19/A.20 and RESIDUE I.7 without declaring the displayed argument false or silently replacing its W notation.

### R34 — A closer parallel for the transfinite construction

**Location:** 105/034–040, all lifting squares and successive X_α(f). **Kind:** unpursued implication / source comparison.

The construction from “all diagrams” and the successive X_α(f) has a particularly close counterpart in `DER_XV-a.tex`, §1, ms. 1–12, including formula (1.23), the amalgamated sum over all lifting squares, and Theorem 1's functorial ordinal factorization. The later text itself adds “Il faudrait quand même expliciter la dépendance fonctorielle” at ms. 10, a useful parallel to the work still being organized in cote 105. This strengthens the comparison for PATHS D.22 and BISITE A.28/E.11 without asserting that the two texts have been dated relative to one another by their printer or edition dates.

### R35 — The total-category square and its genuine cover replacement

**Location:** 105/049, left leaf NB; 052, W7 bis/W8 bis. **Kind:** unpursued implication / source comparison.

The observation that the diagram “n'a rien de carré” in the total category, since the two side fibres are disjoint, closely anticipates XII ms. 125's replacement by genuine closed pieces and the resulting square in Hot_W (`DER_XIIb-b.tex`, Proposition 13 and dgrb555). That later primary-text proposition states the two biconditionals at ms. 126, and its corollary at ms. 126–127 states the cube's two-of-three conclusion under W(7). Thus the strongest direct textual match for cote 105's total-category forms is these later statements, with the variance and the strong-axiom hypothesis retained, rather than only the more elementary two-open formulation at XII ms. 75–78 (TOTASPH A.9/A.13; RESIDUE B.10/B.14).

### R36 — “Strict Quillen triple” and the later weak model formalism

**Location:** 105/025, 028, 030–032. **Kind:** unpursued implication / source comparison.

The source's pair/triple definitions and its extra base/cobase-change condition have close primary-text forms in `DER_XIII-a.tex`, §1, ms. 5–6, and §2, ms. 7–8. The later text distinguishes the weaker inclusions `TC⊂C∩W`, `TF⊂F∩W` from the equalities and identifies its intrinsic-condition M″ with “propriety,” whereas cote 105's chosen Quillen triples already seek those equalities. This supplies a precise comparison for BISITE A.22/A.27 and RESIDUE D.4 and guards against reading “Quillen pair” as a Quillen adjunction between two model categories.

### R37 — Which generating objects need accessibility?

**Location:** 105/034, last paragraph; 036, continuation. **Kind:** unpursued implication / source comparison.

Cote 105 explicitly requires the “source and target of g” to satisfy a common accessibility bound. The later Theorem 1 in `DER_XV-a.tex`, ms. 11, requires accessibility of the sources of the generating maps, and the supplied small-object explanation in `DER_XIX.tex`, dgrb1161, makes the fixed map from the target into Y part of the lifting-square data. This is a concrete refinement of the sufficient hypothesis, not evidence for changing the earlier wording or dropping the small generating family (PATHS D.22; BISITE A.28).

## Steps the manuscript itself leaves unverified

This register records explicit questions, conditional expectations, deferred work, and withdrawals, including cancelled passages. A question mark inside an editor's `\unsure{…}` is not counted as an authorial question; uncertain words quoted below remain identified as uncertain. The references connect each flag to the nearest relevant context entry without treating that entry's return status as proof of the step.

### S01 — Path projection as a W∞-fibration

**Location:** 105/003, middle and lower parts of the cancelled sheet. **Kind:** self-flagged / conjecture.

“Il semblerait que p soit une W∞-fibration” is immediately qualified by “C'est une chose à vérifier,” and the possible cohomological properties of the individual projections are introduced by “Peut-être.” Compare PATHS E.3/E.4/E.11 and BISITE B.14/B.21: those later distinctions cannot decide this question until the particular `Ch(C)` is identified.

### S02 — A Quillen structure on Cat

**Location:** 105/003, final question. **Kind:** self-flagged / conjecture.

The question whether W∞-fibrations and cofibrations defined by LLP yield a Quillen structure is posed, not answered, and belongs to a cancelled page. PATHS D.18 and BISITE A.22 concern related model-recognition issues, while RESIDUE D.4 warns against identifying every intrinsic fibration class with an RLP class.

### S03 — Product and internal-Hom hypotheses

**Location:** 105/007, transition to the product discussion. **Kind:** self-flagged / unproved claim.

“under suitable assumptions” qualifies the product/internal-Hom comparison before the lifting-adjunction calculation is developed on 010–012. This is a local recognition problem rather than the derived Kan-extension projection formula of BISITE F.4/F.7; the latter is the comparison target, not an unspoken hypothesis here.

### S04 — Which orthogonal class?

**Location:** 105/010, marginal “or in Φ_*?”. **Kind:** self-flagged / reading question.

The author queries the class entering the Hom/product argument, and several nearby TC/TF readings are separately uncertain in the transcription. BISITE A.23 and the orthogonality discussion in `DER_XIX.tex`, ms. 2–4, explain the formal adjunction to check, but do not decide these handwritten letters.

### S05 — Pushout-product closure still to check

**Location:** 105/010, lower argument. **Kind:** self-flagged.

“Thus we have to check” and the conditional “OK if ... monomorphisms” restrict the claimed closure to the assumptions being explored. Compare PATHS E.7 and TOTASPH F.23 only after keeping the ambient topos and its monomorphisms distinct from intrinsic cofibrations in Cat.

### S06 — Two “resp.” extensions queried

**Location:** 105/012, revised mixed closure discussion. **Kind:** self-flagged.

The two inserted “resp. ... ?” clauses are questions about extensions of the product/lifting statement, not completed parallel theorems. The nearest context is BISITE A.23 and the interval-generator finding `105-interval-anodyne-generators`; neither validates every revised cell of this table.

### S07 — Identity deferred for verification

**Location:** 105/014, margin beside `i′ ⊠ h(i₀,I,e)=h(i′ ⊠ i₀,I,e)`. **Kind:** self-flagged.

The margin reads “vérifier un [jour?]”, with the final word uncertain. This is a specific algebraic verification inside the interval construction, matching the method described by `105-interval-anodyne-generators`, not permission to suppress the flag because the formula is familiar.

### S08 — M1 and M5 not yet known

**Location:** 105/014, central English paragraph. **Kind:** self-flagged.

“We do not know yet M1 ... nor M5” explicitly withholds factorization and saturation of W̃. The later English leaves work on these gaps, while BISITE A.22/A.27 and `DER_XIX.tex`, Theorem 1.1, provide the nearest context; their later status cannot be transferred backwards to this point in the argument.

### S09 — Two factorizations admitted temporarily

**Location:** 105/014, same paragraph and margin. **Kind:** self-flagged.

“I'll assume the factorizability ... in the two ways” is accompanied by “to work out.” The construction on 034–040 is the eventual response within this package, retaining the smallness qualifications discussed under PATHS D.22 and GALOIS B.13.

### S10 — Taking all intervals may spoil smallness

**Location:** 105/014, last paragraph, continued on 016. **Kind:** self-flagged.

“But this may make a difficulty for factorization” concerns taking all W-aspheric intervals as generators. `DER_XIX.tex`, ms. 5–7, and PATHS D.18/D.22 show why a small generating subfamily is a separate issue, not a consequence of merely naming an interval class.

### S11 — First inclusion and its universal interval axiom

**Location:** 105/016, upper discussion and margins. **Kind:** self-flagged / unproved claim.

The query about `W̃⊂W` leads to taking `TF⊂W` as an axiom and to the universal-W criterion on the Lawvere interval. The compressed diagonal justification remains especially doubtful, so the readable criterion rather than an editorial reconstruction is compared with `105-interval-anodyne-generators` and BISITE A.3/A.27.

### S12 — Closure argument to be made explicit

**Location:** 105/018, margin beside the cobase-change condition. **Kind:** self-flagged.

“to write explicit” is a tentative reading of the note marking the closure argument, and conditions 2, 4, 3, 5 remain in their written order. The later factorization criterion on 030 helps organize the task, while BISITE A.27/A.28 is the relevant context; the proof cannot be made complete by renumbering the page.

### S13 — Does saturation imply retract stability?

**Location:** 105/018, condition 5. **Kind:** self-flagged.

The parenthesis “not a consequence of saturation?” asks about the relation between the current saturation convention and direct factors. Compare the renewed questions on 025/027/028 and context BISITE A.1/A.27 and RESIDUE B.9; different meanings of saturation must be kept separate.

### S14 — Reverse inclusion and adequacy of intervals

**Location:** 105/020, opening and left margin. **Kind:** self-flagged.

“We still have to see if W⊂W̃” is followed by the objection that a single separating interval “cannot possibly be enough” to recover every proposed W. This leaves a recognition problem for test categories and their product variants, matching PATHS D.18/D.22 and the qualification needed for `105-interval-anodyne-generators`.

### S15 — Four question marks at the lifting reduction

**Location:** 105/020, margin beside “all monomorphisms which are in W.” **Kind:** self-flagged.

The explicit “[????]” marks a doubtful reduction after the author inserts “[first!]” over his reference to the two displayed inclusions. The later direct retract argument on 030 is relevant, but it does not prove that the earlier interval-generated class already has the required equality (BISITE A.22/A.27).

### S16 — Desired test-category cases

**Location:** 105/020, final two cases. **Kind:** conjecture / stated goal.

“We would like this to hold” introduces both local W-test categories and the product `A₀×T` with componentwise weak equivalences. These are targets, not claimed finished constructions; compare BISITE A.31/C.1/C.2 and PATHS D.18, whose fine or diagramwise conclusions require additional hypotheses.

### S17 — Factorization c admitted for the time being

**Location:** 105/022, item c. **Kind:** self-flagged.

“this shouldn't be too hard” ends with “Thus I'll admit c for the time being.” The statement explicitly distinguishes a known factorization independent of W from the proposed one involving `TC=C∩W`; compare the later 034–040 construction and BISITE A.27/A.28.

### S18 — Properness remains a desired extra property

**Location:** 105/022, item d and final paragraph. **Kind:** self-flagged / stated goal.

“I'm interested in the following, quite important for me” introduces base-change stability of W along F, followed by “presumably I'll have to rely strongly upon factorization c).” The same requirement becomes condition 4 on 032; BISITE A.11/A.21 and RESIDUE C.1 compare the intrinsic-fibration consequences without making them automatic here.

### S19 — Retract condition on W may be redundant

**Location:** 105/025, margin beside Quillen triples. **Kind:** self-flagged.

“it should not be necessary here to impose the direct factor condition on W, if one assumes b)” is an expectation about redundancy. The explicit doubt on 028 shows the issue was still being examined; compare BISITE A.27 and RESIDUE B.9, not a generic claim that all uses of saturation are synonymous.

### S20 — Strong saturation qualified by limits

**Location:** 105/025, final assertion and margin. **Kind:** unproved claim / self-qualified.

The assertion “This implies W is strongly saturated” carries “true at any rate” when finite direct and inverse limits exist. The package later attributes the corresponding conclusion to Quillen on 028, but no independent literature proof is reproduced in these notes (BISITE A.1/A.27; `DER_XIX.tex`, Quillen-pair framework).

### S21 — Kan versus Serre in the cancelled sheet

**Location:** 105/027, top. **Kind:** self-flagged / conjecture.

“is it a Serre fibration” follows a claimed Kan-fibration statement for an internal Hom. The cancellation and undeveloped fibre notation leave the intended comparison unresolved, and PATHS E.1–E.4 supplies only a thematic path-fibration connection, not an answer to this particular question.

### S22 — Two-sided composites and three retract conditions

**Location:** 105/027, middle and lower cancelled argument. **Kind:** self-flagged.

“but does it imply saturation ... ??” and the several displayed question marks ask whether the composite and retraction conditions imply one another. The uncertainty is part of the discarded draft, and the diagrams should be compared with BISITE A.1/A.27 and RESIDUE B.9 without correcting the uncertain conclusions `fg|f,g` in the frozen text.

### S23 — Closedness and direct factors still questioned

**Location:** 105/028, paragraph after conditions (i)–(iii). **Kind:** self-flagged.

“I'm ... in doubt” concerns whether the equivalent closedness conditions imply stability of W under direct factors; the following appeal to Quillen includes the finite-limit/colimit qualification. This is the same developing distinction registered in BISITE A.27 and RESIDUE B.9, not a claim that the author has found a counterexample.

### S24 — Factorization is the remaining technical task

**Location:** 105/030, lower paragraph. **Kind:** self-flagged / stated goal.

“We have to develop mainly a criterion to get factorization” and “2) causes a little technical problem” identify the gap after the retract argument establishing `F∩W⊂TF`. The following transfinite construction addresses it under hypotheses, as in `DER_XIX.tex`, Theorem 1.1, and PATHS D.22.

### S25 — Why do horn-like generators recover C∩W?

**Location:** 105/032, NB and final sentence. **Kind:** self-flagged / stated goal.

“What remains to be understood” is why `TC=C∩W` is the saturation of `(TC)₀` for general test categories, followed by “Maybe I should have a look at Gabriel-Zisman.” The named book is an intended source in the manuscript, not evidence that this package already contains its proof; compare PATHS D.18/D.22 and the interval-generator register entry.

### S26 — First cellular attachment is only “hopefully” in Φ

**Location:** 105/034, after the first attachment diagram. **Kind:** self-flagged.

“(hopefully) i₁(f)∈Φ” precedes the listed closure and existence assumptions. The changing cardinal bound on the same page shows why both class closure and the size of the family of lifting squares matter (`DER_XIX.tex`, ms. 5–7; BISITE A.28).

### S27 — Promised relaxation of small generators

**Location:** 105/034, condition a; 040, final two sentences. **Kind:** self-flagged / deferred extension.

“we'll see later how to relax this condition” on 034 is not fulfilled by 040, which still says “We have to assume Φ₀ small” and ends “Next step is to try to get rid of this.” The continuation therefore remains open in this package and bears on PATHS D.22 and RESULTS_STATE GALOIS B.13.

### S28 — Ordinal bound to be fixed

**Location:** 105/034, transfinite induction paragraph; 036, continuation. **Kind:** self-flagged.

The ordinal α₀ is explicitly “to be fixed later,” and 036 develops the accessibility bound and the finite-presentability special case. This is subsequent progress on the same flagged step, not evidence that the earlier small-generator assumption has disappeared (`DER_XIX.tex`, Theorem 1.1; BISITE A.28).

### S29 — Stability under filtering limits

**Location:** 105/038, “What about d)?” and lower Zorn argument. **Kind:** self-flagged.

The question concerns the closure condition needed to identify the generated class, with a difficult marginal phrase tentatively read “for compact limits.” The precise lemma on 040 is about compatible continuous ordinal composition, so the stronger reading should remain a question when compared with `DER_XIX.tex`, ms. 2–5, and PATHS D.17/D.22.

### S30 — W equals W_D?

**Location:** 105/043, heading. **Kind:** self-flagged / stated goal.

The heading's “W=WD?” advertises another intended identification in addition to the W7 discussion; no general equality theorem is completed on the following pages. Compare RESULTS_STATE GALOIS B.4/B.13 and RESIDUE I.7, whose recognition and enhancement questions are not settled by the subsequent square construction.

### S31 — The isomorphism-edge criterion

**Location:** 105/046, lower right and margin. **Kind:** self-flagged.

The proposed `i′₀* iso ⇔ i′* iso` is marked “à vérifier” with the possible alternative of making it an axiom. The lemma on 051 returns to an isomorphism-edge case, but the flag remains essential to the source assessment of `105-derivator-crible-excision` and TOTASPH A.9.

### S32 — Cocartesianness needed for the inverse

**Location:** 105/047, central paragraph. **Kind:** self-flagged / conjecture.

“il faudrait savoir,” “Moralement,” and “on peut s'attendre (sous certaines conditions)” qualify the passage from the categorical square to a cocartesian coherent coefficient square. Compare BISITE A.33 and TOTASPH A.13: the missing conditions are substantive, as the later counterexample to unrestricted reverse excision illustrates.

### S33 — A general principle only suspected

**Location:** 105/048, final paragraph, continued on 049. **Kind:** self-flagged / conjecture.

The “fait général que je [subodore?]” is introduced as a “Principe” for the total category of a three-object diagram. Its use of a Grothendieck construction makes it relevant to POLES B.2 and BISITE F.1/F.2, but the following provisional axiom, rather than a completed argument, is the source's answer.

### S34 — The existing derivator axioms seem insufficient

**Location:** 105/049, right-hand leaf, opening paragraph. **Kind:** self-flagged / conjecture.

“J'ai l'impression que ça ne peut absolument pas découler” of Der 1–Der 5,5′ leads to Der 6 “(provisoire).” This marks the proposed cocartesian conclusion as extra structure, in direct relation to STRATA D.2, BISITE A.33, and RESIDUE I.7.

### S35 — The coefficient generalization is itself queried

**Location:** 105/049, right gutter and bottom margins. **Kind:** self-flagged / reading question.

The main text replaces “constant” by “quelconque,” while the difficult margin contains tentative readings about checking whether the statement is already false for non-locally-constant ξ. The full marginal sentences are low-confidence and are not used as a reliable retraction; the secure tension between the main replacement and the marginal check is compared with BISITE A.19/A.20 and RESIDUE I.7.

### S36 — The dual provisional axiom

**Location:** 105/050, Der 6′ and its NB. **Kind:** self-flagged / conjecture.

Der 6′ is again “provisoire,” and “Je ne vois pas comment l'un impliquerait l'autre” introduces a possible exceptional dualizing-functor case. Compare BISITE F.8 and G.2/G.6 and *Pursuing Stacks* VII §136, ms. 569–570; the source has not supplied that dualizing construction.

### S37 — The stronger geometric axiom may be absurd

**Location:** 105/050, final reformulation and insertion. **Kind:** self-flagged / conjecture.

“il semblerait que le bon axiome” proposes cartesian if and only if cocartesian, followed by the insertion “à moins que ça [ne soit absurde?].” The final words are uncertain, but the reservation is clear; the next scan's lemma and 052's withdrawal must be read alongside the proposal (STRATA D.2; BISITE G.1/G.13).

### S38 — Hot square claim withdrawn

**Location:** 105/052, top left and associated margin. **Kind:** withdrawn in the same text.

“Complètement faux” explicitly rejects the preceding universal Hot-square assertion and its proposed π₀ criterion on the same leaf. This is a local withdrawal with both statement and correction preserved, relevant to NEW_RESULTS 8, TOTASPH A.13, and BISITE G.13; it is not a licence to delete the original sentence.

### S39 — The extra five-lemma implication

**Location:** 105/052, Der 8, lower left and margin. **Kind:** self-flagged.

The additional `a+b⇒c` is followed by “?” and revised commentary, unlike the separately described cartesian and cocartesian implications. BISITE A.33 and RESIDUE B.14 are the exact context comparisons; a proof requires the extra conservativity or structural assumptions, not merely the phrase “lemme des cinq.”

### S40 — A presumption cancelled but not supplied with a full proof

**Location:** 105/052, W7 bis, parenthesis after the square. **Kind:** unproved claim / revised wording.

The words “je présume que” are struck out before the assertion that the two composites are homotopic by a path of length 2, each through the inclusion of X₀. The explicit length-1/length-2 explanation is evidence of the intended natural-transformation construction, but it is distinct from the stronger W-biconditional that follows (RESIDUE B.5; PATHS B.1/C.1).

### S41 — Last-page strengthened corollaries

**Location:** 105/053, both labelled assertions. **Kind:** unproved claim.

The proper/smooth versions are given as W7 ter/W8 ter, with the suffix itself uncertain, and no supporting proof is written on this final leaf. Compare `DER_XIIb-b.tex`, ms. 125–126 and 147–149, and BISITE F.2; the direction conventions and the extra reverse implications require a separate check.

## Other claims and post-freeze reading questions

### Q01 — The first leaf's lifting criteria

**Location:** 105/002, lemma and corollary. **Kind:** unproved claim / reading question.

The lemma claims W∞-asphericity and proper/smooth consequences from specified RLP tests, but no proof is given and the overwritten corollary is among the least secure readings in the package. Compare PATHS E.9, BISITE A.15/B.7, and RESIDUE D.4; in particular the lemma's literal “alors X est” is not replaced by the mathematically more expected assertion about the morphism.

### Q02 — Generated weak equivalences and closure

**Location:** 105/005–007 and 025. **Kind:** unproved claim.

The equalities `TC=C∩W̃` and `TF=F∩W̃` are asserted using the orthogonal pairs and finite amalgamated/fibred constructions, before agreement with the prescribed W is known. This is a precursor of the closedness distinctions in BISITE A.22/A.27, and the later claims about strong saturation must be read with their explicitly stated limit hypotheses.

### Q03 — The retract argument's literal intermediate target

**Location:** 105/018, paragraph beginning “Thus any map.” **Kind:** reading question.

The text says that to conclude `f∈W` it remains to prove `p∈W`, but the displayed retraction then makes f a retract of `i∈W`. The argument's apparent intended endpoint suggests a different wording, yet the frozen sentence and the unusual arrow directions remain unchanged; the clearer retract proof on 030 and BISITE A.27 are comparison evidence, not corrections to the ink.

### Q04 — Bar or tilde on TC

**Location:** 105/028, central displays. **Kind:** reading question.

The frozen alternatives `\overline{TC}|\widetilde{TC}` preserve the visually different mark rather than normalizing it to the tilde on TF. The mutual-orthogonality formulas and `DER_XIX.tex`, ms. 2–4, make a uniform generated-class notation mathematically tempting, but they cannot establish which mark is on this sheet.

### Q05 — The functorial factorization claim

**Location:** 105/036, final paragraph; 038, corollary. **Kind:** unproved claim / method.

The text states a functorial factorization after attaching all lifting squares and choosing accessibility bounds. `DER_XIX.tex`, Theorem 1.1 and its footnote, is a close later form of this claim, with the same smallness mechanism; the current pages do not independently justify every accessibility assumption for the intended topos or diagram categories (BISITE A.28; PATHS D.22).

### Q06 — General square lemma and shifted tests

**Location:** 105/051, lemma and margin. **Kind:** unproved claim / method.

The lemma reduces an isomorphism-edge case through the map ρ and a counit described as a form of Der 3, with an additional requirement on all D_I. It supplies a route to checking the earlier square assertion on 046, but is not a proof that arbitrary cartesian squares are cocartesian (BISITE F.1/F.2, A.33, and E.13).

### Q07 — Lawvere notation and the external register

**Location:** 105/016, main text and diagonal note. **Kind:** reading question.

The frozen reading is `L_A`, while the supplied Hua register describes Ω; these may name the same intended object, but the register is a paraphrase rather than a second image witness. The transcription remains untouched, and any future identification should distinguish notational equivalence from a corrected visual reading (`105-interval-anodyne-generators`).

### Q08 — W8 bis's first condition

**Location:** 105/052, lower-right list a–c. **Kind:** reading question.

The alternative `f|f_a` affects whether the three conditions are “total map / intersection / two pieces,” the pattern explicitly used in XII ms. 76–78. The contextual pattern favours f as a mathematical interpretation but cannot eliminate the frozen doubt, so comparisons with TOTASPH A.9/A.13 and BISITE A.33 are conditional at this one glyph.

### Q09 — Variance and the final Φ drawing

**Location:** 105/053, top and bottom diagrams. **Kind:** reading question.

The top drawing's arrow from 0 to b differs from the lower drawing's arrow from b to 0, and the suffixes of W7/W8 remain doubtful. The expected fork from XII is not substituted for the visible diagrams; comparisons with `DER_XIIb-b.tex` and BISITE F.2/F.8 must state the variance actually used.

### Q10 — Sigma and xi in the dual axiom

**Location:** 105/050, displayed exclamation direct image. **Kind:** reading question.

The frozen display reads `ψ_!(σ)` after a sentence introducing ξ, whereas the preceding right-direct-image version on 049 is written with ξ. That adjacent parallel and the duality convention in BISITE F.8 suggest checking whether the argument's input should be ξ, but no contextual correction is made to the frozen σ or to the exclamation sign.

### Q11 — The cancelled comparison before the W7 heading

**Location:** 105/043, top cancelled block. **Kind:** unproved claim / reading question.

Before the W7 heading, the source writes `q∈W ⇔ q_Ū∈W` and derives a comparison with q_U from a square whose horizontal maps lie in W, ending with an uncertain “q.e.d.”. The immediate two-of-three step is visible, but the retained block does not identify q and its barred restrictions sufficiently to equate this with the full reverse two-open inclusion axiom. It is an earlier biconditional that must be recorded in any chronology, while TOTASPH A.9 and `DER_XIIb-a.tex`, ms. 75–78, do not justify filling in its missing setting.

## Title sheets, internal headings, and page counts

### T01 — Catalogue title versus a title on the paper

**Location:** all scans, especially 105/004. **Kind:** source comparison.

The supplied catalogue label is “[Champs (stacks) 2] : notes manuscrites (s.d.),” but no retained sheet visibly supplies that phrase as its own title. Scan 004 carries a cancelled uncertain name and the number 3, not a title page or a statement of the total number of pages; this is a bounded correction to what may be inferred from the README/catalogue framing.

### T02 — Two substantive internal headings

**Location:** 105/034, upper margin; 043, top. **Kind:** source description.

“Factoriza-tion Problem” labels the construction begun on 034, while “Dém. de W7, W(7bis) et W=WD?” heads the later French sequence on 043. These are local working headings, not declarations that either sequence is complete; their subjects match `DER_XIX.tex`, §1, and `DER_XIIb-a.tex`, ms. 75–80, respectively.

### T03 — English internal pagination

**Location:** 105/005–040, tops of the mathematical leaves. **Kind:** source description.

The visible English sequence is numbered 1–16 with an additional “10 bis,” on scans 005, 007, 010, 012, 014, 016, 018, 020, 022, 025, 028, 030, 032, 034, 036, 038, 040. This is internal foliation, not an explicit “17 pages” title or a warrant to count the intervening printer faces as missing mathematics; it is independent of the bottom numbers and of the companion's later chapter pagination.

### T04 — French internal pagination and double leaves

**Location:** 105/043 and 045–053. **Kind:** source description / reading question.

The French sequence begins with an uncertain 6 on 043, then 7 on 045, 8–9 on the two halves of 046, 10 on 047, 11 on 048, 12–13 on 049, 14 on 050, 15 on 051, 16–17 on 052, and 18 on 053. Those paired numbers identify writing on the two halves of single scans, so neither “18” nor the number of scans is an authorial total for this sequence; no earlier pages 1–5 of this sequence are identified by conjecture.

### T05 — Bottom foliation

**Location:** retained scans 105/002–053. **Kind:** source description.

The separate visible foliation follows scan number minus one, from 1 on 002 to 52 on 053, with the gaps corresponding to omitted scans 009/024/029/042. This describes the supplied objects and does not establish who added the foliation or that all 52 numbered surfaces contain this mathematical text; the delivered package contains the specified 48 nonblank scan pages.

### T06 — Reused typescript page 90

**Location:** 105/044, printed page number and manuscript corrections. **Kind:** reading question / source description.

The French prose typescript is numbered 90 and carries corrections and the separate folio 43. No title on the retained sheet identifies the larger work, so it is not assigned to *Récoltes et semailles* or another text from subject matter alone; neither the context README nor the supplied mathematical excerpts resolves its identity.

### T07 — Printer pagination is not manuscript extent

**Location:** 105/006–041, especially 028 and 031. **Kind:** source description.

The job headers and listings include printer “PAGE” numbers, and the GUTS listing has PAGE 1 on 028 and PAGE 2 on 031. These belong to the recycled computer output, not to a count of mathematical manuscript pages, and they do not change the distinction between the English and French internal numberings.

### T08 — Counts beside code lists

**Location:** 105/037 and 039. **Kind:** source description.

The handwritten numbers 21, 51, 20, 11 on 037 and 146, 124 on 039 are positioned beside module/member or utility lists. They are not introduced by “pages” or a manuscript title and are therefore recorded as list-associated counts, not estimates of the extent of a mathematical work; no corresponding page-total claim is supplied by the context.

### T09 — Dates and manufacturer imprint

**Location:** 105/017, 021, 026, 028, 033, 041, and 048. **Kind:** source description / chronological limitation.

The recycled printing includes April–June 1982 dates, while 048 includes the maker's “MédiGraf Montpellier 21999” imprint. These are support-level records, not handwritten dates or a “21,999 pages” count, and they cannot independently answer the README's question about a specifically 1983 formulation.

### T10 — No explicit total-length declaration found

**Location:** all 48 retained scans. **Kind:** source comparison; negative finding.

No separate “N pages,” “Pages 1–N,” or equivalent title-sheet extent declaration for the mathematical contents was found. The reliable counts are the delivered scan count and the visibly recorded foliations just listed, with printer pagination and code counts distinguished rather than combined.

## Every numbered entry in NEW_RESULTS.md

The numbering below is the supplied register's numbering. Its provenance and review statements are reported, not independently expanded into literature claims; several proof files named by the register are not included in this context archive. The three “Known after all” addenda are covered after the twelve numbered entries.

### NEW_RESULTS 1 — Finite monoids, bounded homology, and finite type

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 1; *Les Dérivateurs* V ms. 51–52; CATHOT G.4; OWN_RESULTS §2. **Reported review:** the enlarged equivalence and corollaries are “not yet” checked; the earlier finite-dimensional case has separate review history.

No finite-monoid theorem, universal-group calculation, or equivalence between finite type and bounded homology appears in these scans. The accessibility discussion on 034–040 concerns domains of generating maps and transfinite factorization, so it supplies no form of the register's finite-classifying-space assertion. This package neither strengthens nor independently checks the new extension of CATHOT G.4.

### NEW_RESULTS 2 — Miller-type conclusion under a cohomological bound

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 2, OWN_RESULTS §1. **Reported review:** “not yet.”

No statement about maps from BG, finite or residually finite fundamental groups, or eventual vanishing of integral cohomology is present. The phrase “cohomological criteria” on 032 concerns the intended input class W and does not supply the bounded-cohomology theorem used by item 1. The register's claim is consequently unchanged and unverified by this transcription.

### NEW_RESULTS 3 — Kan–Thurston without small quotients and invariant ind-objects

**Location:** 105/003 and 034–040 are the nearest different topics; no form of the result found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 3; GALOIS B.10–B.12; V ms. 46, VII ms. 129–132, IX ms. 22–23; PATHS D.K3/D.K4. **Reported review:** the GALOIS route is reported reviewed; the independent OWN_RESULTS §3 route is not, and its cardinality bound was quoted from memory.

The cancelled `Ch(C)` question on 003 does not discuss W∞-invariant path ind-categories or reflection into groupoids, and the cardinal estimates on 034–040 are for a different small-object construction. No Kan–Thurston group, small-quotient bound, or E.17 reduction is stated. The package offers no additional proof step for either of the two separately credited routes.

### NEW_RESULTS 4 — Uncountably many maps to S²

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 4; CATHOT D.6; V ms. 43–46; OWN_RESULTS §4. **Reported review:** “not yet.”

The first leaf's spherical-looking RLP tests do not state the hypothesis of infinitely many sphere retracts or a cardinality conclusion for `[X,S²]`. Neither the H¹ condition nor the relevant homotopy-group criterion occurs here. There is therefore no manuscript form or new evidence for the supplied claim in this package.

### NEW_RESULTS 5 — Lower bound of 34 arrows for an RP² poset

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 5; CATHOT G.8; OWN_RESULTS §5. **Reported review:** “not yet.”

No RP² model, finite-poset census, or lower-bound argument appears. The numerical lists on 037/039 are recycled computing material and associated handwritten counts, not arrow enumerations for categories. Cote 105 neither confirms the new bound nor supplies a form of the earlier bound 28.

### NEW_RESULTS 6 — Minimal-arrow categories for spheres

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 6; CATHOT G.14–G.15; XII appendix ms. 8–11. **Reported review:** the entry says “not yet” for the enlarged result while recording earlier computational checks of smaller subclaims.

No minimal-arrow classification for S¹, S², or S³ is stated, and the three- and four-object indexing diagrams near the end serve an excision argument rather than a minimal homotopy-type census. The manuscript therefore contributes neither the asserted minima nor the uniqueness refinements. Its printed program listings are not programs verifying those claims.

### NEW_RESULTS 7 — A reversible localizer not detected by spectra

**Location:** 105/047, 050, 052, especially W7 bis/W8 bis. **Kind:** unproved claim / unpursued implication. **Context:** `NEW_RESULTS.md`, item 7; POLES F.14(1); XII §5; XVI §3; RESIDUE I.7. **Reported review:** “not yet.”

The manuscript supplies the problem-setting form of reversibility—“Forme renforcée de W7” and the two biconditionals—but gives no construction of the particular localizer W_S or its RP∞/RP² tests. The proposed relation between cartesian and cocartesian squares on 050 is a possible conceptual motive, not a classification by spectral homology. The unreviewed counterexample in this register is precisely why the notes avoid inferring “all reversible localizers are homology theories” from the failure of W∞.

### NEW_RESULTS 8 — Failure of the strong XII excision theorem for W∞

**Location:** 105/043, 046–047, 050, 052–053; first complete W7 bis at 052. **Kind:** source comparison / proposed axiom contradicted in its unrestricted application. **Context:** `NEW_RESULTS.md`, item 8; TOTASPH A.13; `DER_XIIb-a.tex`, ms. 75–80, dgrb516–517; `DER_XIIb-b.tex`, XIIbb-A045 and later corollaries. **Reported review:** TOTASPH A.13 is reported checked, including recomputation of its finite example, with agreement from another expert review.

Cote 105 explicitly reaches the strong biconditional on 052 after marking its reverse direction as a missing cocartesian step on 047, and it locally withdraws the universal Hot-square assertion with “Complètement faux” on 052. The supplied companion's double-cone counterexample addresses the unrestricted reverse implication and preserves the distinction from forward excision; cote 105 supplies no counterexample of its own and no complete repair. The register's phrase “homology localizers only” is stronger than the counterexample establishes and must be qualified in light of the separately unreviewed item 7.

### NEW_RESULTS 9 — Failure of Loc(7 F) for homology localizers

**Location:** 105/022 and 032, desired base-change property; no trefoil construction found. **Kind:** source comparison / stated goal. **Context:** `NEW_RESULTS.md`, item 9; XVI ms. 105; BISITE B.11/B.18; RESIDUE D.11. **Reported review:** “not yet.”

The manuscript's condition 4 asks that W be stable under base change along its chosen F, and it calls the resulting object a “strict Quillen triple.” It does not assert a universal Loc(7 F) factorization theorem for every homology localizer or construct the trefoil-complement example. The later negative claim is relevant as a limitation on overgeneralizing the program, but is not a contradiction of a theorem proved on these sheets.

### NEW_RESULTS 10 — Total path categories force totality under simple connectivity

**Location:** 105/003, cancelled `Ch(C)` discussion; no form of the stated implication found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 10; XII ms. 102–103 and 112; PATHS E.12. **Reported review:** “not yet.”

The path-space sheet asks about fibrations and cohomological smoothness/properness and never states that `Ch(Y;y₀,−)` is total or assumes Y simply connected. Its “C'est une chose à vérifier” concerns a different property of the endpoint projection. The common Ch notation therefore gives a comparison lead only, not a manuscript antecedent of this implication.

### NEW_RESULTS 11 — Total W∞-asphericity does not force filteredness

**Location:** all 105 scans; no form found. **Kind:** source comparison; negative finding. **Context:** `NEW_RESULTS.md`, item 11; `DER_II-a.tex`, ms. 36–36ter, II-C-003; TOTASPH C.5–C.10; PATHS A.6; RESIDUE F.3. **Reported review:** the register reports medium and max reviews and checks of the bridge and counterexample.

The implication “totalement asphérique ⇒ filtrant” does not appear in this package, including the English filtering-limit discussion. The earliest explicit occurrence located in the supplied comparison text is the question at II ms. 36, “cela implique-t-il que X soit filtrante ?”, followed by the ms. 36bis–36ter revisions; that is a context locator, not proof of an archive-wide chronological first occurrence. The Δ_inj counterexample and its relation to Isbell–Mitchell are cited as the supplied reviewed result, without re-deriving it or treating the filtering hypothesis in the small-object argument as its subject.

### NEW_RESULTS 12 — RP² is not the classifying space of a finite monoid

**Location:** 105/002–053, no form found. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, item 12; CATHOT G.4/G.6; the register's cited Conjecture 7.1. **Reported review:** multiple reviews, including reported primary-text checking, are recorded.

No RP² obstruction, universal-group argument, finite-monoid realization conjecture, or related counterexample is present. The package does not add to the cited result and cannot be used to date its mathematical content to these notes. Its absence also means that the later communication mentioned in the register is irrelevant to the manuscript's own claims.

### K01 — Isbell–Mitchell addendum

**Location:** no corresponding statement in 105/002–053. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, “Known after all,” and item 11.

The register explicitly identifies an older source for the category and exactness fact used in item 11 while distinguishing the total-asphericity bridge. These notes preserve that credit and make no independent claim about the contents of the 1973 paper, which was not separately opened in this task.

### K02 — Nielsen-realization uniqueness addendum

**Location:** no corresponding statement in 105/002–053. **Kind:** source comparison. **Context:** `NEW_RESULTS.md`, “Known after all,” Harvey 1971 attribution.

There is no Nielsen-realization or mapping-class-group uniqueness assertion on these pages. The register's attribution is retained as its attribution and contributes no comparison to the model-category or excision arguments here.

### K03 — “Localiseur spécial” and accessibility addendum

**Location:** 105/034–040, nearest related discussion. **Kind:** unpursued implication / source comparison. **Context:** `NEW_RESULTS.md`, “Known after all,” citing Cisinski, Astérisque 308, Corollary 4.2.22; `DER_XIX.tex`, ms. 5–7; PATHS D.18/D.22.

The small-generating-family requirement and the final “Next step is to try to get rid of this” are closely relevant to the accessibility issue. They do not state the cited modern equivalence for “localiseur spécial,” and the specialness terminology of the later companion must be matched before importing it into the English notes. The literature attribution is reported from the supplied context, not independently certified here.

## Individual comparison of every dossier statement

Each heading identifies exactly one row of the supplied `DOSSIER_STATEMENTS_WITH_STATUS.md`. The register status is quoted as a claim, including when its label says “Proved” or “Known”; no independent review is inferred from that label. Source-line numbers locate the supplied Markdown register, while manuscript references are reproduced from its locator cell.

## Dossier family: STRATA

### STRATA D.1 — Exceptional adjunctions for open and closed pieces

**Location:** 105/043–047, two-open construction. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.1, source line 15; I ms.1–9; Lead 4. **Register status:** claim (return: Known).

The two-open diagram is present, but no exceptional adjunction chain for a complementary open/closed pair is constructed. The phrase “carré abstrait σ” on 047 concerns coherent excision, so this is a partial thematic antecedent rather than a form of the six-operation assertion.

### STRATA D.2 — Pointed fibres, cofibres, and stable exactness

**Location:** 105/050, final Der 6; 052, upper left. **Kind:** conjecture / withdrawn in the same text. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.2, source line 16; I ms.2–9; Lead 4 exactness clauses. **Register status:** claim (return: Known).

“σ est cartésien ssi il est cocartésien” proposes the relevant exactness principle, but without the pointed stable hypotheses of the context row. The assertion about Hot is then marked “Complètement faux” on 052, so the package records a proposed principle and its unstable obstruction, not the full stable theorem or a triangulation construction.

### STRATA D.3 — Proper and smooth lifting criteria for posets

**Location:** 105/045 and 051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.3, source line 17; I ms.53–56; Lead 4 map classification. **Register status:** claim (return: Proved).

The use of “propre” for the cofibred replacement and of “lisse” for ρ gives a fibrewise base-change method. No poset lifting-category criterion or necessity-and-sufficiency proof appears, so the context classification is not restated here.

### STRATA D.4 — Proper/smooth base change

**Location:** 105/045, fibre calculation; 051, counit calculation. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.4, source line 18; I ms.49–59; VI ms.162–169; Lead 4. **Register status:** claim (return: Proved).

The manuscript uses properness and smoothness in concrete Kan-extension calculations, a close instance of the context's base-change mechanism. Its “φ̄ est propre” argument does not formulate the complete arbitrary-square theorem or its converse, and the excision conclusion on 046 retains a verification flag.

### STRATA D.5 — Failure of a naive geometric properness criterion

**Location:** 105/002–053, no corresponding example. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.5, source line 19; Ib-C003; I ms.53–59; GALOIS D.9; Lead 4. **Register status:** claim (return: Refuted).

No proposed topological characterization of proper poset maps, and no counterexample to one, occurs. The categorical “propre” of 045 is used for base change and cannot be equated with a geometric criterion merely by name.

### STRATA D.6 — A diamond map beyond strict (op)fibrations

**Location:** 105/046–053, square-shaped indexing diagrams. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.6, source line 20; VIc-C008 strictness comparison; Lead 4. **Register status:** claim (return: Proved).

The diamond drawings encode coherent squares and excision, not the specific finite-poset map distinguishing smooth/proper maps from strict fibrations and opfibrations. No such separating example or bundle claim is supplied.

### STRATA D.7 — Inclusions and product projections

**Location:** 105/043–045 and 051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.7, source line 21; I ms.54–56; Lead 4 examples and edge cases. **Register status:** claim (return: Proved).

The two-open sieve construction and a particular proper/smooth ρ are present, but there is no general classification of poset inclusions or product projections. These are examples used inside an argument, not a statement of all the context row's criteria.

### STRATA D.8 — Finite-poset geometric dictionary

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.8, source line 22; Lead 4 constructible base-change comparison. **Register status:** claim (return: Proved).

No realization-stratification dictionary or comparison of constructible base-change operations is developed. The four-vertex square shapes near the end do not supply that geometric interpretation.

### STRATA D.9 — Specialization and slice variance correction

**Location:** 105/043, open-sieve convention. **Kind:** reading question / source comparison. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA D.9, source line 23; I ms.54; XII ms.59. **Register status:** claim (return: Proved).

The source fixes a two-open categorical cover, but does not give the context's formula involving y\\X and closure of a point. Accordingly it neither states nor corrects the particular variance error in the later companion; the directions of its own diagrams remain frozen independently.

### STRATA G.2 — Totality and universal homotopy-colimit correctness

**Location:** 105/018 and 034–040, filtering limits. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, STRATA G.2, source line 24; XII ms.88–89; TOTASPHB.11. **Register status:** claim (return: Proved).

No equivalence between total asphericity and all simplicial homotopy-colimit comparisons is stated. “filtering direct limits” here belongs to closure and accessibility for factorization and is not the context's universal comparison property.

## Dossier family: PATHS

### PATHS A.P1 — Components of full path categories

**Location:** 105/003, cancelled Ch(C) sheet. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.P1, source line 32; VII ms.65–74. **Register status:** claim (return: Proved).

The notation “Ch(C)” appears, but the sheet discusses its projections rather than identifying π₀ of path categories with localized Hom sets. No full-path definition or component calculation is supplied, so the context proposition has no stated form here.

### PATHS A.P2 — Sequential and all-type path comparisons

**Location:** 105/003, cancelled Ch(C) sheet. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.P2, source line 33; VII ms.99–110. **Register status:** claim (return: Proved).

There is no sequence of path types or fibred-roof comparison. The W∞-fibration question does not establish equivalence between sequential and all-type constructions.

### PATHS A.1 — Grothendieck construction for span roofs

**Location:** 105/045 and 048–049, total categories. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.1, source line 34; VII ms.99-110; VIIb-C026. **Register status:** claim (return: Proved).

“la cat. cofibrée ... qu'il définit” on 048 gives a Grothendieck-construction method for a span used in excision. It does not identify the path-category roof construction or prove the comparison in the context row; the common method is the connection.

### PATHS A.2 — Filtered Cat-colimits and total categories

**Location:** 105/038–040, filtering-limit closure. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.2, source line 35; VII ms.108-109; VIIb-C026. **Register status:** claim (return: Proved).

The filtering-colimit discussion concerns lifting classes in M, not the map from a Grothendieck total category to an ordinary colimit of categories. No weak-equivalence theorem for that comparison is stated or proved.

### PATHS A.3 — Universal total-functor criterion

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.3, source line 36; VII ms.99-110; VIIb-C026. **Register status:** claim (return: Proved).

The package does not formulate the context's condition on every functor and every u/t. The comma fibres used on 045 serve a specific right-Kan calculation and do not provide the universal criterion.

### PATHS A.4 — Insufficiency of preorder cofinality and parallel homotopy

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.4, source line 37; VII ms.99-109; VIIb-C026. **Register status:** claim (return: Refuted).

No such sufficient-condition proposal or counterexample appears. The ordinal choices in the small-object argument do not concern cofinality in a path-type preorder.

### PATHS A.5 — Total shapes can give incorrect Cat-colimits

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.5, source line 38; After TOTASPH correction; VIIb-C026. **Register status:** claim (return: Refuted).

Neither Δ_inj nor the diagram of monoid categories BN^(n+1) occurs. The source's use of filtered limits supplies no example separating total asphericity from ordinary Cat-colimit correctness.

### PATHS A.6 — Δ_inj is total and exact but not filtered

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.6, source line 39; TOTASPH C.7-C.10 verification. **Register status:** claim (return: Proved).

No Δ_inj counterexample, exactness calculation, or total-asphericity assertion appears. This is the same absence recorded for NEW_RESULTS 11, not a reason to reinterpret “filtering” in the English argument.

### PATHS A.7 — Three classes of indexing shapes

**Location:** 105/018 and 034–040, nearest different use. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.7, source line 40; Part A; VIIb-C026. **Register status:** claim (return: Proved).

The hierarchy from filtered categories through universally correct Cat-colimit shapes to total shapes is not stated. The manuscript assumes filtering where needed for factorization and does not compare those three classes.

### PATHS A.8 — Classification of Cat-colimit shapes remains open

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.8, source line 41; Part A. **Register status:** claim (return: Open).

No intrinsic classification of universally correct Cat-colimit shapes is attempted. The unfinished removal of smallness on 040 is a different open problem and cannot settle this row.

### PATHS A.9 — Subdivision map without a Cat_hot inverse

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS A.9, source line 42; POLES D.6 verification; VIIc-A046; V-I066. **Register status:** claim (return: Proved).

There is no triangle-boundary face poset, subdivision map, or enumeration of reverse monotone maps. The natural homotopies on 052 concern a total-category inclusion and are not the context counterexample.

### PATHS B.1 — Full and weak-vertical path diagrams

**Location:** 105/003, Ch(C); 052, short homotopies. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.1, source line 43; VII ms.27–78. **Register status:** claim (return: Proved).

The path notation on the cancelled sheet does not define which vertical arrows are allowed or prove strict compatibility with concatenation. The length-2 homotopy described on 052 is a particular natural-transformation zigzag, not a construction of both path diagrams.

### PATHS B.2 — Weak-vertical paths and hammocks

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.2, source line 44; Lead1 weak-vertical identification. **Register status:** claim (return: Known).

No hammock mapping simplicial set or reduction to it is constructed. Lifting-class and factorization arguments do not by themselves furnish a mapping-space comparison.

### PATHS B.3 — Literal inclusion J need not be an isomorphism

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.3, source line 45; Lead1 forcing claim. **Register status:** claim (return: Refuted).

The manuscript does not introduce J or a marking on the vertical maps of paths. Its saturation questions therefore do not give the specific counterexample claimed by this row.

### PATHS B.4 — Isomorphism markings and all-arrow markings

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.4, source line 46; Lead2. **Register status:** claim (return: Proved).

Neither extremal marking case is analyzed for full path categories. The all-coefficient remark on 046 concerns ξ and is unrelated to marking all arrows of a path construction.

### PATHS B.5 — Homotopy fractions on the restricted side

**Location:** 105/025–030, localization and saturation. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.5, source line 47; Part B HCF/model/fibrant-object sufficient statements on restricted side. **Register status:** claim (return: Known).

“W is strongly saturated” is discussed, but no homotopy calculus of fractions or short-fraction comparison is stated. The uncertain isolated word “Relations|fractions” on 030 cannot carry such a theorem.

### PATHS B.6 — Coherent full-path map to localization mapping spaces

**Location:** 105/003 and 046–047, different coherence issues. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.6, source line 48; VII ms.68–70;PartB partial comparison. **Register status:** claim (return: Proved).

No coherent map from a full path space to a localization mapping space, or split-monic conclusion for J, appears. The coherent-square distinction on 047 is conceptually related but supplies none of the required construction.

### PATHS B.7 — Padding backward squares into hammocks

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.7, source line 49; PartB grid-sweep reduction. **Register status:** claim (return: Proved).

Identity padding and mixed-boundary hammock sweeps are absent. The lifting squares attached in 034 are cells in a factorization construction, not squares of path morphisms.

### PATHS B.8 — Whether J is always a weak equivalence

**Location:** 105/003, cancelled path question. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.8, source line 50; PartB central unrestricted-vertical comparison. **Register status:** claim (return: Open).

“C'est une chose à vérifier” concerns the endpoint projection's fibration property, not J. The package does not resolve or restate the unrestricted-vertical comparison problem.

### PATHS B.9 — Finite search of 132 comparisons

**Location:** 105/006–041, recycled computing sheets. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS B.9, source line 51; PartB requested finite search. **Register status:** claim (return: Proved).

No path-category search, F₂ homology table, or count of 132 comparisons is present. The reused job and program output is unrelated evidence and is not repurposed as a verification of this claim.

### PATHS C.P1 — Categories of endpoint-preserving type maps

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P1, source line 52; VII ms.86–94. **Register status:** claim (return: Proved).

The source does not define the increasing maps between path types or their enriched composition. Its interval I in the topos construction is a different object with a different role.

### PATHS C.P2 — Descent to a reachability preorder

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P2, source line 53; VII ms.99–123. **Register status:** claim (return: Proved).

There is no reachability preorder of path types or descent of a coherent path-space diagram. The transfinite ordinal indexing on 034–040 is not the sequential cofinality result in this row.

### PATHS C.P3 — The three CATHOT E.26 comparisons

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P3, source line 54; CATHOT E.26(1),(2),(3);VIIc-A046 in Hot;V-I066 in Hot. **Register status:** claim (return: Proved).

No wide-marking theorem or three-comparison statement is present. The use of Hot_W on 052 only locates an excision square and supplies no form of those path-space comparisons.

### PATHS C.P4 — Mixed-sign blocks and composition in Hot

**Location:** 105/052, length-2 homotopy, nearest limited connection. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P4, source line 55; CATHOT E.27;IX-037 raw path composition;VII ms.125–127. **Register status:** claim (return: Proved).

The manuscript describes two composites homotopic to an inclusion, but gives no block padding, mixed-sign condition, or associative unital composition theorem. This local homotopy does not state the context's block independence.

### PATHS C.P5 — q_L can fail to be invertible in Cat_hot

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.P5, source line 56; VIIc-A046 in Cat hot;V-I066 strong independence inference. **Register status:** claim (return: Refuted).

There is no q_L comparison or four-object crown example. The four-vertex square category used for derivator axioms is not that counterexample.

### PATHS C.1 — Strict enrichment by all-type paths

**Location:** 105/003, cancelled Ch(C) question. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.1, source line 57; IX-037. **Register status:** claim (return: Proved).

The Ch(C) notation points toward a path construction, but strict units, associativity, enrichment, nerves, and Kan replacement are not developed. The sheet's tentative W∞-fibration claim cannot be promoted to the enrichment theorem.

### PATHS C.2 — Hammock composition and simplicial localization

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.2, source line 58; IX-037. **Register status:** claim (return: Known).

No composition-compatible hammock model is stated. The factorization methods concern arrows of M and do not compare mapping simplicial sets.

### PATHS C.3 — Failure of pointed Cartesian units

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.3, source line 59; IX-044; IX-049. **Register status:** claim (return: Proved).

A pointed Cartesian path-composition law and the zero-object unit obstruction are absent. The candidate bicartesian axiom does not address this unit calculation.

### PATHS C.4 — Kan mapping spaces for pointed simplicial objects

**Location:** 105/027, cancelled Hom(I,Y) passage. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.4, source line 60; IX-044; IX-049; IX-052. **Register status:** claim (return: Proved).

The manuscript writes that an internal-Hom endpoint map is a Kan fibration and asks about Serre fibrations. It does not supply the context's cofibrant–fibrant pointed simplicial mapping-space statement, and the cancelled passage leaves the ambient assumptions undeveloped.

### PATHS C.5 — Quillen groupoid from derived mapping spaces

**Location:** 105/025–030, Quillen terminology. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.5, source line 61; IX-040; IX-041; IX-072. **Register status:** claim (return: Known).

“Quillen pair” and “Quillen triple” describe lifting and factorization, not the fundamental groupoid of a derived mapping space. No identification of that groupoid appears.

### PATHS C.6 — Loop and suspension formulas

**Location:** 105/050, proposed cartesian/cocartesian axiom. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.6, source line 62; IX-084; IX-087. **Register status:** claim (return: Proved).

The phrase “cartésien ssi ... cocartésien” suggests a setting in which loop/suspension comparisons would matter. No pointed loop or suspension formula is stated, so the context row is a possible consequence to investigate under additional hypotheses, not a manuscript theorem.

### PATHS C.7 — Representability of π₁ versus loop formulas

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.7, source line 63; IX-084; tests (a) and (c). **Register status:** claim (return: Refuted).

The source makes no representability claim for π₁ of a mapping space and does not distinguish it from a loop-object formula. The path-fibration question on 003 supplies neither assertion.

### PATHS C.8 — Derived Hom complexes

**Location:** 105/007–012, internal Hom in a topos. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.8, source line 64; IX-061; IX-065; IX-070. **Register status:** claim (return: Proved).

The underlined Hom is used in a tensor/Hom lifting adjunction, not a derived Hom complex of additive or chain-complex coefficients. Thus the shared notation does not provide the context result.

### PATHS C.9 — General additive path proposal

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.9, source line 65; IX-061; IX-065; IX-070. **Register status:** claim (return: Open).

No additive path-category theory is proposed. The dualizing-functor speculation on 050 does not assume additivity or solve the open additive comparison.

### PATHS C.10 — Pointed ind-path problem

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS C.10, source line 66; IX-044; IX-049; IX-052; IX-072. **Register status:** claim (return: Open).

Pointed ind-path objects and their comparison problem are absent. The smallness assumptions of 034–040 concern generating arrows, not ind-objects representing mapping invariants.

### PATHS D.1 — The three Chapter IX diagram tests

**Location:** 105/046–052, coherent square discussion. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.1, source line 67; IX ms.22-23; IX-080. **Register status:** claim (return: Proved).

The distinction between an abstract square and its “diagramme squelettique” is relevant to diagram testing. The three Chapter IX conditions themselves are not formulated or compared here.

### PATHS D.2 — Five-arrow pointed counterexample

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.2, source line 68; IX ms.23; IX-080; Lead 3; CATHOT E.14; Kaledin addendum (iii). **Register status:** claim (return: Refuted).

No five-arrow pointed category or counterexample to a diagram test is given. The finite square and fork shapes are indexing categories, not the claimed relative-category example.

### PATHS D.3 — Finite products force a finite category to be a preorder

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.3, source line 69; IX ms.23. **Register status:** claim (return: Proved).

No finite-category product classification is stated. Product closure in the topos lifting argument concerns classes of maps and is mathematically different.

### PATHS D.4 — Rectification implies constant-shape tests

**Location:** 105/046–047, coherent versus skeletal diagrams. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.4, source line 70; IX ms.22; IX-080; Lead 3. **Register status:** claim (return: Proved).

The manuscript insists on the coherent σ behind its skeletal square. It gives no general rectification hypothesis or derivation of the constant-shape tests, so only the need for coherent data is shared.

### PATHS D.5 — Six-object suspension restriction counterexample

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.5, source line 71; VII-c ms.134 companion; IX-080. **Register status:** claim (return: Refuted).

No six-object suspension or failure of restriction is constructed. The shape Q on 046 is used for Kan extension, not this counterexample.

### PATHS D.6 — Loop formulas imply representability

**Location:** 105/050–052, nearest possible structural link. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.6, source line 72; IX-081, IX-088; IX ms.22-25. **Register status:** claim (return: Proved).

The source does not state a loop formula or infer representability from one. Its provisional square axioms cannot replace the missing pointed representability argument.

### PATHS D.7 — Rectification for derivable categories

**Location:** 105/034–040, factorization method. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.7, source line 73; Lead 3; Part D(2). **Register status:** claim (return: Known).

Functorial factorization is explicitly asserted, but the package does not construct diagram categories of a derivable category or prove their rectification comparison. This is a method potentially usable in such a proof, not the theorem in the row.

### PATHS D.8 — Intrinsic cofibrations and finite rectification

**Location:** 105/030–032, recognition and properness conditions. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.8, source line 74; XII ms.228-234,272; POLES A.8-A.9/G.26 addendum (i)-(iv). **Register status:** claim (return: Proved).

The Quillen-triple criterion and additional “strict” base/cobase-change condition are close structural input. No finite-shape rectification conclusion or full intrinsic-cofibration axiom package is written, so the relationship is partial.

### PATHS D.9 — Finite counterexamples to cofibration axioms

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.9, source line 75; POLES addendum (i). **Register status:** claim (return: Refuted).

The diamond and finite-set counterexamples to CF5/CF6 are absent. Nothing about the square-shaped derivator diagrams supplies those relative-category examples.

### PATHS D.10 — Cubes do not test all finite posets

**Location:** 105/051–052, shifted square axioms. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.10, source line 76; Part D(3) cubical test. **Register status:** claim (return: Refuted).

The request to impose an axiom on all D_I acknowledges diagramwise structure, but the manuscript does not claim that cubes test every finite poset. It therefore supplies neither the false implication nor the context counterexample.

### PATHS D.11 — Finite semisimplicial tests versus BZ and BK

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.11, source line 77; Part D(3) finite posets versus BZ and BK question. **Register status:** claim (return: Proved).

No distinction between finite-poset tests and BZ/BK diagram shapes occurs. The finitely presented special case on 036 is about accessibility, not rectification at those shapes.

### PATHS D.12 — A contractible fence can fail BK rectification

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.12, source line 78; Part D(3) converse BK question. **Register status:** claim (return: Refuted).

There is no fence example or comparison with BK. The early path notation alone does not identify an eventual-fence construction.

### PATHS D.13 — Localization by a relative poset does not imply rectification

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.13, source line 79; STRATA B.8 addendum; Part D(3). **Register status:** claim (return: Refuted).

No replacement by a relative poset is constructed. The cofibred replacement on 045 is used for a specific cohomology square and is not a rectification theorem for all diagrams.

### PATHS D.14 — Shape audit of Kaledin's framework

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.14, source line 80; Recent results Kaledin; GALOIS F.5 addendum. **Register status:** claim (return: Known).

No Kaledin-type enhancement or audit of its allowed indexing shapes is present. The package's small and finite diagram shapes cannot be used to supply hypotheses absent from the later comparison.

### PATHS D.15 — Naive Pos-enhancement criterion

**Location:** 105/046–047 and 051, diagramwise distinctions. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.15, source line 81; Recent results Kaledin (i),(iv); Part D(3). **Register status:** claim (return: Known).

The source separates coherent objects of D(Q) from their skeletal diagrams and asks for shifted versions. It neither defines the naive Pos-enhancement nor proves its equivalence criterion, so this is a conceptual antecedent only.

### PATHS D.16 — Circle and infinite-additivity failure

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.16, source line 82; Recent results Kaledin (ii),(iii). **Register status:** claim (return: Proved).

No infinite-additivity counterexample indexed by a circle is given. The colimit hypotheses in the factorization section are assumptions, not a calculation of this failure.

### PATHS D.17 — Finite versus all-shape cofibration axioms

**Location:** 105/018, 034–040. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.17, source line 83; XIII ms.7-12,50-59; XVII ms.39-40; XIX ms.33-38,48; Part D(4). **Register status:** claim (return: Proved).

“filtering direct limits” and the continuous transfinite lemma make closure under larger constructions explicit. The source does not state the finite/all-shape rectification dichotomy, but records the sort of additional closure input that such a distinction needs.

### PATHS D.18 — Accessible localizers and Thomason model structures

**Location:** 105/020, 030–032, and 040. **Kind:** stated goal / unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.18, source line 84; POLES G.24/E.2 addendum; Part D(2),(3). **Register status:** claim (return: Known).

“What remains to be understood” on 032 asks how the generator description recovers `C∩W`, and 040 retains small generators. This is a close model-recognition program, not a proof of the full accessible-localizer Thomason theorem or a removal of its accessibility hypothesis.

### PATHS D.19 — Locally constant full faithfulness need not satisfy two-of-three

**Location:** 105/047, cancelled locally constant clause. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.19, source line 85; GALOIS A.5 addendum; Part D(1). **Register status:** claim (return: Refuted).

The cancelled clause concerns coefficient scope and a proposed complete equivalence. It does not define the class in this row or prove a failure of two-of-three, so cancellation cannot be cited as its counterexample.

### PATHS D.20 — Ho Fun and Fun Ho differ

**Location:** 105/046–047, abstract versus skeletal square. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.20, source line 86; Recent results references; STRATA C.7 addendum. **Register status:** claim (return: Known).

“plus précisément ... le carré abstrait σ” explicitly locates the property in D(Q), not merely in the visible commuting square. This is a direct precursor of the distinction in the row, although no general nonfaithfulness example or full comparison theorem is supplied.

### PATHS D.21 — All shape tests force an infinity-equivalence

**Location:** 105/051, margin on D_I. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.21, source line 87; GALOIS mapping-space upgrade suggestion. **Register status:** claim (return: Proved).

The manuscript asks for the axiom on shifted derivators, so arbitrary diagram parameters are relevant. It does not formulate the context's A×J testing condition or derive an infinity-categorical equivalence, and those stronger quantifiers must not be inferred.

### PATHS D.22 — Open recognition and nonaccessible localizers

**Location:** 105/032 and 040, final lines. **Kind:** self-flagged / method. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.22, source line 88; IX-080; Part D(3); recent/additional unresolved questions. **Register status:** claim (return: Open).

“Next step is to try to get rid of this” explicitly leaves the small-generator restriction in place. The construction contributes a conditional method to the open recognition problem but gives no nonaccessible recognition theorem or general accessibility result.

### PATHS D.23 — Homology localizers and intrinsic fibrations

**Location:** 105/022 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.23, source line 89; POLES C.4-C.5 addendum; Part D(2) cofibration-fibration asymmetry. **Register status:** claim (return: Proved).

Base-change stability along F is an added goal, not claimed for every cohomologically defined W. The later negative claims about intrinsic fibrations therefore limit a possible generalization of the program rather than contradicting a completed theorem on these pages.

### PATHS D.K1 — Acyclic maps are epimorphic in Hot

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.K1, source line 90; GALOIS B.9 verification; CATHOT E.17 reduction. **Register status:** claim (return: Proved).

No epimorphism assertion for acyclic maps in Hot is stated. The excision square is a different use of the homotopy category.

### PATHS D.K2 — Large acyclic simple groups

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.K2, source line 91; GALOIS B.10 verification; KT_mu. **Register status:** claim (return: Proved).

No group construction or small-quotient obstruction appears. The cardinal parameters in the small-object argument have no such group-theoretic interpretation.

### PATHS D.K3 — The cardinal Kan–Thurston statement

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.K3, source line 92; GALOIS B.11 verification; KT_mu; CATHOT E.17. **Register status:** claim (return: Proved).

The package contains no BG→W construction or bound on homomorphisms into small groups. This absence agrees with the comparison under NEW_RESULTS 3.

### PATHS D.K4 — Invariant ind-objects reflect to groupoids

**Location:** 105/003, nearest path notation. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.K4, source line 93; GALOIS B.12 verification; CATHOT E.17. **Register status:** claim (return: Proved).

No ind-groupoid reflection or W∞-invariance criterion is stated. The tentative fibration property of Ch(C) does not imply that reflection theorem.

### PATHS D.K5 — All-shape tests force a one-type

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS D.K5, source line 94; V ms.44-46; Lead 3 size correction; CATHOT E.17. **Register status:** claim (return: Proved).

There is no conclusion that an object must be a one-type from its shape tests. The small squares and interval tests in the manuscript are not the quantified test family of this row.

### PATHS E.1 — Endpoint fibres of all-arrow paths

**Location:** 105/003, cancelled endpoint projection. **Kind:** conjecture / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.1, source line 95; CATHOT E.20-E.25; VIIc-C004; VIIc-C005. **Register status:** claim (return: Known).

The source's “p:Ch(C)→C×C” is the closest local form, but its path construction and strict fibre identification are not developed. Its explicit verification flag prevents using the sheet as a proof of the later endpoint-fibre theorem.

### PATHS E.2 — Strict monoidal loop model

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.2, source line 96; Part E; IX-037. **Register status:** claim (return: Proved).

No strict monoidal loop category or unit/composition calculation is present. The internal Hom of an interval on 027 does not provide that structure.

### PATHS E.3 — All-type endpoints smooth but not proper

**Location:** 105/003, middle of cancelled sheet. **Kind:** reading question / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.3, source line 97; VII ms.161-166; Part E; STRATA path test. **Register status:** claim (return: Refuted).

The source says p is not cohomologically proper or smooth, whereas the context row distinguishes properties of a specified all-type construction. This is a potential difference to investigate, not a certified contradiction, because the exact Ch(C) and coefficient conventions on the sheet have not been identified with that later construction.

### PATHS E.4 — Eventual endpoints smooth and proper, not strict

**Location:** 105/003, cancelled path projection. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.4, source line 98; Part E; filtered-union lifting distinction. **Register status:** claim (return: Refuted).

The text separates categorical and cohomological fibration language but gives no eventual-fence definition or theorem with both properties. Its tentative statements cannot be transferred to the eventual model simply because both are called paths.

### PATHS E.5 — Functorial mapping-path replacement

**Location:** 105/003 and 034–038. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.5, source line 99; Part E; XII ms.188-207. **Register status:** claim (return: Proved).

There is an endpoint-fibration question and a separate functorial cellular factorization method. No mapping-path replacement is constructed from them, so the manuscript supplies two related ingredients in different settings rather than the context factorization.

### PATHS E.6 — Rectangular-band monoid counterexample

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.6, source line 100; STRATA E.11 test case. **Register status:** claim (return: Refuted).

No rectangular-band monoid or strictification counterexample is given. The cancelled path discussion has no such finite witness.

### PATHS E.7 — Interval pushout-products versus intrinsic Cat-cofibrations

**Location:** 105/012–018, topos construction. **Kind:** reading question / limited comparison. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.7, source line 101; POLES H.6; TOTASPH F.23; Part E. **Register status:** claim (return: Refuted).

The interval pushout-product is present in a topos with monomorphisms as C. The row's failure for intrinsic cofibrations in Cat has different ambient hypotheses, so it does not refute the same assertion as written here.

### PATHS E.8 — Finite interval cotensors can have wrong fibres

**Location:** 105/027, cancelled Hom(I,Y) discussion. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.8, source line 102; Part E; dual interval assertion. **Register status:** claim (return: Proved).

The Kan/Serre question makes interval endpoint maps relevant, but there is no proof of the needed fibre formula or the counterexample in this row. This is a warning against filling in that formula from the notation alone.

### PATHS E.9 — W∞-smooth/proper does not imply larger-W fibration

**Location:** 105/002–003 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.9, source line 103; GALOIS/STRATA localizer qualification; Part E. **Register status:** claim (return: Refuted).

The early lemmas explicitly use W∞, and the English section separately asks for properness relative to its selected W and F. The manuscript does not assert the invalid passage to every larger localizer, so the context row supplies a boundary on generalization.

### PATHS E.10 — Marking components is not a stratification

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.10, source line 104; STRATA proposed general stratified reading. **Register status:** claim (return: Refuted).

No component marking or stratification theorem appears. The two-open categorical cover is not a definition of a marked-component stratification.

### PATHS E.11 — Open strict bifibration replacement R

**Location:** 105/003, final cancelled question. **Kind:** conjecture / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.11, source line 105; STRATA E.11; VIc-C022. **Register status:** claim (return: Open).

The question about W∞-fibrations and a Quillen structure signals interest in replacement maps but does not construct R or prove strict bifibration. It therefore adds historical evidence of the issue without settling the open row.

### PATHS E.12 — Fixed-origin paths: contractible versus total/filtered

**Location:** 105/003, Ch(C) sheet. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.12, source line 106; TOTASPH G.1-G.6; XIIba-C005. **Register status:** claim (return: Known).

Fixed-origin path categories, total asphericity, and filteredness are not related on this sheet. In particular the fibration speculation is not a statement that path categories are total or filtered.

### PATHS E.13 — Finite Yoneda data need not be faithful

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, PATHS E.13, source line 107; VIIc-C004 faithfulness question; CATHOT F.2 verification. **Register status:** claim (return: Refuted).

There is no finite-Yoneda embedding or nonfaithfulness example. The skeletal/coherent distinction is relevant background but does not state this particular obstruction.

## Dossier family: BISITE

### BISITE A.1 — Saturation conventions and Theorem A variants

**Location:** 105/005, 025, 027–028. **Kind:** reading question / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.1, source line 115; XVI ms.1--3. **Register status:** claim (return: Proved).

The source explicitly distinguishes “mild saturation,” direct factors, and “strongly saturated,” while questioning relations among them. This supplies historical forms for the terminology discussion, but does not formulate the context's absolute/relative Theorem A distinction.

### BISITE A.2 — Intrinsic fibrations as universal pullback preservation

**Location:** 105/022, item d; 032, condition 4. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.2, source line 116; XII ms.207--209; GALOIS D.1. **Register status:** claim (return: Proved).

“W stable by base changes by any g∈F” is demanded as an extra property of a Quillen triple. F itself is defined by RLP here, so this is not a definition or proof identifying the entire intrinsic-fibration class with the universal pullback-preserving class.

### BISITE A.3 — Slice, universal, and local weak-equivalence classes

**Location:** 105/016–018, UW interval condition. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.3, source line 117; XII ms.210,220; GALOIS A.5. **Register status:** claim (return: Proved).

The boxed universal condition `(I−e)∈UW` is a genuine local form of a universal-W notion. The full family of slice and fine/local equivalence classes in the context row is not defined or compared.

### BISITE A.4 — Postcomposition and raw pullback

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.4, source line 118; XII ms.226--227,248. **Register status:** claim (return: Proved).

No general statement about postcomposition between localized slices and raw pullback is made. The pullback stability desired on 032 is restricted to the selected F, not an unrestricted raw-pullback theorem.

### BISITE A.5 — Maximal universal test class

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.5, source line 119; XII ms.222. **Register status:** claim (return: Proved).

The source does not construct the maximal class defined by all universal tests. Its chosen interval family and orthogonal classes solve a different generation problem.

### BISITE A.6 — Transporter Galois connection

**Location:** 105/025, lifting polarity. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.6, source line 120; II ms.83--89, (6.7). **Register status:** claim (return: Proved).

“order reversing bijections” describes the left/right lifting polarity on saturated classes. This is formally analogous to the context's transporter Galois connection but has a different defining relation, so the two constructions are not identified.

### BISITE A.7 — Transporter composition criterion

**Location:** 105/025 and 040, closure under composition. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.7, source line 121; II Proposition 6.1, ms.88--89. **Register status:** claim (return: Proved).

The closure results concern orthogonal lifting classes and continuous cellular composites. They do not state or prove the context's transporter-composition criterion.

### BISITE A.8 — Failure of transporter composition

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.8, source line 122; II first versions (6.2)--(6.5). **Register status:** claim (return: Refuted).

No chain example showing failure of transporter composition is supplied. The manuscript's composition assumptions are not a claim that arbitrary transporters compose.

### BISITE A.9 — Smooth/proper stabilizers versus intrinsic fibrations

**Location:** 105/002–003 and 045. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.9, source line 123; II ms.66,89; XII ms.225--226. **Register status:** claim (return: Proved).

The early French sheets distinguish W∞-properness, smoothness, and fibration language, and 045 uses categorical cofibredness to obtain properness. They do not define both stabilizer classes or give the full comparison with intrinsic fibrations, so the evidence is terminological and methodological.

### BISITE A.10 — Three fibre axioms and slice localization

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.10, source line 124; XII ms.215--218; XIIc B055--B065. **Register status:** claim (return: Proved).

No three-axiom package for intermediate fibre categories or equivalence of their localizations appears. The two lifting factorizations are different data.

### BISITE A.11 — Factorization implies Fib∩W equals universal W

**Location:** 105/030–032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.11, source line 125; XIII ms.10--11; XVI 4.4.1. **Register status:** claim (return: Proved).

The retract proof obtains `F∩W=TF` for the selected Quillen classes, and the next page separately adds properness. It does not state the general intrinsic identity `Fib_W∩W=W_u`, although the conditional model framework is a natural place to compare it.

### BISITE A.12 — Functorial replacement and intermediate localizations

**Location:** 105/036–038, functorial factorization. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.12, source line 126; XII ms.217--218; XIIc B060--B065. **Register status:** claim (return: Proved).

A functorial factorization is explicitly claimed after the small-object construction. The source does not use it to prove equivalence of every intermediate slice localization, so the relation is a possible method rather than a form of that theorem.

### BISITE A.13 — Six-object failure of the third fibre axiom

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.13, source line 127; XII ms.207,217--218; XIIc B062. **Register status:** claim (return: Refuted).

No six-object example separating fibre axioms a, b, and c is present. The author's distinct a–d list on 022 concerns model recognition and must not be confused with those axioms.

### BISITE A.14 — Fine axioms

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.14, source line 128; XII ms.225--227. **Register status:** claim (return: Proved).

The package does not state the fine-slice axiom system. Its topos and test-category discussion is a related ambient setting, not the fine formalism itself.

### BISITE A.15 — Four fibration classes and Loc(7)

**Location:** 105/002–003 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.15, source line 129; XVI ms.27--41; POLES A.5--A.6. **Register status:** claim (return: Proved).

W∞-proper, W∞-smooth, W∞-perfect, and fibration language occurs, with several conclusions unproved or uncertain. There is no complete four-class comparison or Loc(7) equivalence theorem, and the separate property 4 on 032 remains an additional requirement.

### BISITE A.16 — ABC transfer through replacements

**Location:** 105/034–038, cellular factorization. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.16, source line 130; XVI 4.4.1,4.4.9,4.4.10; POLES A.13--A.14. **Register status:** claim (return: Proved).

The explicit functorial factorization is a possible replacement method. The manuscript does not formulate an ABC transfer theorem or verify the required hypotheses for transferred diagram or slice structures.

### BISITE A.17 — Brown/ABC criterion with terminal hypotheses

**Location:** 105/030–032. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.17, source line 131; XVI 4.4.3; POLES A.13. **Register status:** claim (return: Proved).

The Quillen-triple criterion and its properness addition are present, but no Brown/ABC equivalence with the specified terminal-object assumptions is stated. Those terminal hypotheses cannot be inferred from the existence of the terminal symbol e in individual diagrams.

### BISITE A.18 — Weak constant-coefficient maps may fail composition

**Location:** 105/045–047, coefficient discussion. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.18, source line 132; I ms.117--118; GALOIS D.3. **Register status:** claim (return: Refuted).

The manuscript moves between constant and locally constant coefficients and cancels one attempted qualification. It gives no composition counterexample for the weak constant-coefficient class, so the deletion is evidence of uncertainty rather than that later refutation.

### BISITE A.19 — Asymmetric local-coefficient repair

**Location:** 105/046–047, “pas seulement ξ constant” and cancelled lc clause. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.19, source line 133; I ms.79--81,117--123; GALOIS D.2. **Register status:** claim (return: Proved).

The broadened coefficient scope and the attempted “coeff. loc. constants” condition show that the author notices a distinction central to the later repair. The precise universal right-direct-image hypothesis and its asymmetric conclusion are not formulated, and the cancelled 047 clause does not prove them.

### BISITE A.20 — Properness does not preserve local constancy

**Location:** 105/045–047. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.20, source line 134; I ms.102; Ib-C003; GALOIS D.9; STRATA D.5. **Register status:** claim (return: Refuted).

Properness is used to compute fibres of a right direct image, while preservation of locally constant coefficients is not separately proved. This is consistent with the context's warning, but the manuscript supplies no explicit counterexample and no general preservation claim to refute.

### BISITE A.21 — Derived products with one intrinsic fibration leg

**Location:** 105/022, item d; 032, condition 4. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.21, source line 135; XII ms.241--248. **Register status:** claim (return: Proved).

Pullback stability along F is explicitly desired and then included in a “strict Quillen triple.” The source does not identify arbitrary intrinsic fibrations with that F or state the fine-slice derived-product theorem, so the comparison is conditional on extra identifications.

### BISITE A.22 — Weak Quillen axioms versus trivial-class equalities

**Location:** 105/007, 028, 030. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.22, source line 136; XIII ms.7--12,27--28; PATHS D.17. **Register status:** claim (return: Proved).

The source repeatedly isolates `TC=C∩W` and `TF=F∩W`, and 030 proves the latter by a retract argument under its factorization assumptions. This is a close form of the distinction between merely having factorizations and having the desired closed classes, not a proof that weaker intrinsic axioms always identify them.

### BISITE A.23 — Lifting adjunctions and Kan variance

**Location:** 105/010–012, Hom/tensor calculation. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.23, source line 137; XIII ms.45--50. **Register status:** claim (return: Proved).

The displayed lifting-adjunction calculation gives a genuine formal antecedent: a product or pushout-product condition is translated into an internal-Hom lifting condition. The context row concerns Kan-extension adjunctions in particular variances, which are not themselves constructed by this calculation.

### BISITE A.24 — Ordinary Kan extensions need not be derived

**Location:** 105/045–046 and 049–051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.24, source line 138; XIII ms.45--50. **Register status:** claim (return: Refuted).

The notation is explicitly that of a derivator's direct-image functors and coherent squares. No claim is made that an arbitrary ordinary Kan extension computes the derived one, so the context warning is relevant to interpretation rather than a correction of such a claim here.

### BISITE A.25 — Noetherian sober Alexandrov finiteness

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.25, source line 139; XIII ms.60--67. **Register status:** claim (return: Proved).

No topological finiteness criterion of this kind is stated. The finite indexing categories in the square argument do not provide a theorem about Alexandrov spaces.

### BISITE A.26 — A finite floor does not give every small Kan extension

**Location:** 105/034–040, size assumptions. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.26, source line 140; XIII ms.50--59; PATHS D.9. **Register status:** claim (return: Refuted).

The factorization argument explicitly assumes small colimits and accessibility where needed. It does not derive all small Kan extensions from finite diagram data, and its unresolved small-generator issue is compatible with the context's limitation.

### BISITE A.27 — Closedness and retract stability

**Location:** 105/005–007, 025, 028, 030. **Kind:** unpursued implication / self-flagged. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.27, source line 141; XIII ms.27--29,57. **Register status:** claim (return: Proved).

Quillen pairs are defined by orthogonality, factorization, and direct factors, and 030 gives a concrete retract argument for the remaining trivial-fibration equality. This is one of the closest manuscript forms of the context row, but the author's earlier doubts about W's retract stability on 025/028 and the precise saturation convention must remain visible.

### BISITE A.28 — Uniform diagram structures and derived Kan extensions

**Location:** 105/034–040, functorial factorization. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.28, source line 142; XIII ms.57--72. **Register status:** claim (return: Proved).

The construction is carried out in M under explicit colimit and accessibility assumptions. It does not construct compatible model structures for every M(I) or prove all derived Kan adjunctions; the margin about D_I on 051 belongs to a later axiom proposal, not a supplied uniform model construction.

### BISITE A.29 — Double closure and joins in a polarity

**Location:** 105/025, left/right saturation. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.29, source line 143; II section 5, ms.69--80, especially (5.20). **Register status:** claim (return: Proved).

The equalities `Φ=(Φ_*)^*` and `Ψ=(Ψ^*)_*` and the order-reversing correspondence are explicitly written. This is a partial form of the polarity framework, but no full lattice-of-classes join formula is stated on the page.

### BISITE A.30 — Unions need not preserve composition closure

**Location:** 105/040, left Q-saturated closure lemma. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.30, source line 144; II ms.65--67. **Register status:** claim (return: Refuted).

The lemma concerns a specified left lifting class and continuous transfinite composition. It does not claim stability of arbitrary unions of compositional classes or supply the row's counterexample.

### BISITE A.31 — Fine structure is additional to the bisite remark

**Location:** 105/020, desired presheaf test-category cases. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.31, source line 145; VI ms.81--84; XII ms.222--225. **Register status:** claim (return: Proved).

The target cases involve presheaves and componentwise equivalences over A₀, but no fine bisite structure is built. The phrase “We would like this to hold” is an explicit goal, so the context's additional fine hypotheses are not already verified here.

### BISITE A.32 — Absolute versus relative Theorem A

**Location:** 105/045–046, special replacement; all other leaves. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.32, source line 146; XVI Loc (1,2,3)/(3 bis); POLES A.16. **Register status:** claim (return: Refuted).

The particular α-equivalence is used inside a fibre calculation, with no general relative Theorem A stated. It gives neither an identification of the absolute and relative versions nor an answer to the README's question about cotes 117–118.

### BISITE A.33 — Converse cube implication needs more than exactness

**Location:** 105/052, Der 8, “a+b⇒c”. **Kind:** self-flagged / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.33, source line 147; XII ms.273--275; POLES G.17--G.18. **Register status:** claim (return: Refuted).

This is a direct manuscript form of the issue: the two one-directional implications are separated, while `a+b⇒c` is followed by “?”. The source's proposed bicartesian hypothesis is not developed into a proof of the required conservativity, matching the reason the context row treats the extra converse separately.

### BISITE A.34 — Stabilizer assignments need not be antitone

**Location:** 105/025, lifting polarity. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE A.34, source line 148; II cancelled section 4, ms.65--68. **Register status:** claim (return: Refuted).

The genuine antitone lifting correspondence is present, but the different stabilizer assignment in the context row is not defined. The order-reversing statement on 025 therefore cannot serve as a proof of an invalid stabilizer monotonicity claim.

### BISITE B.1 — Over/under comma variance in fine slices

**Location:** 105/045, fibres of the replacement. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.1, source line 149; VI ms.81--84; XII ms.222. **Register status:** claim (return: Proved).

The replacement's fibres are described through slice/comma categories in the properness calculation. The source does not define the paired fine theories or derive their complete over/under variance dictionary, so only the fibrewise technique is shared.

### BISITE B.2 — Simplicial slice tests

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.2, source line 150; Lead 1; VI ms.81--84. **Register status:** claim (return: Known).

No simplicial fine-slice test or full comparison over a nerve is formulated. The interval lifting tests of 012–018 live in the topos model-construction problem instead.

### BISITE B.3 — Fine nerve comparison with infinity-presheaves

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.3, source line 151; Lead 1; VI ms.81--84. **Register status:** claim (return: Proved).

The package supplies no infinity-localization equivalence for fine slices. Presheaf notation on 020 is not such a recognition theorem.

### BISITE B.4 — Horn base-change counterexample

**Location:** 105/032, reference to horn lifting. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.4, source line 152; Lead 1. **Register status:** claim (return: Refuted).

The author mentions the “horn lifting property” as an a priori generator description. He gives no horn-based counterexample to preservation under a specified base change, so the context example is absent.

### BISITE B.5 — Naming dictionary for proper and smooth maps

**Location:** 105/045 and 051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.5, source line 153; I ms.54; XII ms.224--225. **Register status:** claim (return: Known).

A cofibred replacement is called proper, and a particular ρ is called smooth and proper, consistent with the manuscript's working variance. No modern nerve-theoretic dictionary or full recognition criterion is stated, so the comparison should retain the source's conventions explicitly.

### BISITE B.6 — Maximal raw-pullback-preserving classes

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.6, source line 154; XII ms.222; II ms.66 and 88--89. **Register status:** claim (return: Proved).

The source does not identify maximal fine pullback-preserving classes with Liss and Prop. Its properness condition is a desired restriction along F, not a maximality theorem.

### BISITE B.7 — Strict bifibrations, smooth/proper maps, intrinsic fibrations

**Location:** 105/002–003. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.7, source line 155; XII ms.225--226; STRATA D.5--D.6. **Register status:** claim (return: Proved).

The cancelled path sheet distinguishes categorical fibration/cofibration language from cohomological properness/smoothness and conjectural W∞-fibration. It provides no strict-inclusion hierarchy or separating examples for all three levels, but it is a clear sign that the notions are not being identified without argument.

### BISITE B.8 — Eventual integer-fence path resolution

**Location:** 105/003, Ch(C) sheet. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.8, source line 156; VII ms.161--169; PATHS E.9. **Register status:** claim (return: Proved).

There is no explicit integer-fence formula or eventual-path resolution. The undeveloped notation Ch(C) is insufficient to identify the intended construction with this row.

### BISITE B.9 — Complementarity only for W∞ or the total class

**Location:** 105/002–003, W∞-specific statements. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.9, source line 157; XII ms.225--226; POLES E.5; STRATA G.5. **Register status:** claim (return: Proved).

No classification of localizers satisfying complementarity is stated. The repeated W∞ qualification does not imply a conclusion about every larger localizer.

### BISITE B.10 — Finite truncation localizers fail complementarity

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.10, source line 158; XII ms.225--226; POLES C.8--C.9; STRATA G.3--G.4. **Register status:** claim (return: Refuted).

No W_n example or failure of complementarity is given. The spherical test notation on the first leaf does not constitute a truncated-localizer construction.

### BISITE B.11 — One cover obstructs all nonzero homology coefficients

**Location:** 105/022 and 032, properness sought. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.11, source line 159; XII ms.225--226; POLES C.10; PATHS E.9. **Register status:** claim (return: Refuted).

The source wants base-change stability for cohomologically specified W, but supplies no common cover obstruction for homology localizers. This later negative claim constrains a generalization of the goal, not a theorem already proved in the manuscript.

### BISITE B.12 — Finite bifibration fails W₁ or rational lc condition

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.12, source line 160; GALOIS D.4--D.5; XII ms.225--226. **Register status:** claim (return: Proved).

No such finite bifibration or rational locally constant coefficient calculation occurs. The proper/smooth labels on 051 refer to a different small shape and no W₁ claim.

### BISITE B.13 — Cover tests distinguish local from constant coefficients

**Location:** 105/046–047, coefficient changes. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.13, source line 161; GALOIS D.3; POLES C.10; PATHS E.9. **Register status:** claim (return: Proved).

The remark “pas seulement ξ constant” and the cancelled locally constant qualification are directly relevant to coefficient scope. They do not furnish the covering example or the proof distinguishing the two tests in this row.

### BISITE B.14 — Cohomological fibration is not properness

**Location:** 105/003, cancelled path discussion. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.14, source line 162; I ms.117--118; GALOIS D.2 and D.9. **Register status:** claim (return: Refuted).

The text separately discusses a W∞-fibration and failure of cohomological properness or smoothness. This is a close indication of the intended distinction, but the exact Ch(C) and its verification remain unresolved on the sheet.

### BISITE B.15 — Eight maps and 48 finite comparison entries

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.15, source line 163; GALOIS D.3--D.5; I ms.117--123. **Register status:** claim (return: Proved).

No eight-map test suite or 48-entry invariant table is present. The count 48 in this task counts scans and has no relation to that computation.

### BISITE B.16 — Accessible coefficient fine-class classification

**Location:** 105/034–040, small-object hypotheses. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.16, source line 164; VI ms.81--84; XII ms.222--226. **Register status:** claim (return: Proved).

Small generation and accessible objects are used to construct factorizations. They are not a classification of accessible coefficient fine classes or an infinity-presheaf recognition result.

### BISITE B.17 — Intrinsic fibrations for truncation localizers

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.17, source line 165; POLES C.8--C.9; STRATA G.4. **Register status:** claim (return: Known).

There is no necessary-and-sufficient criterion for intrinsic W_n-fibrations. The W∞ lifting claims do not state the truncation boundary-map condition.

### BISITE B.18 — Bounds for homology intrinsic fibrations

**Location:** 105/022 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.18, source line 166; POLES C.10; XII ms.225--226. **Register status:** claim (return: Proved).

The manuscript treats cohomological W as given and asks for a proper model structure. No lower/upper classification of its intrinsic fibrations is supplied, so the context row remains additional information rather than a restatement.

### BISITE B.19 — Functorial factorization by full-fence paths

**Location:** 105/003 and 034–038. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.19, source line 167; VII ms.161--169; PATHS E.4--E.5. **Register status:** claim (return: Proved).

The source has a path-projection question and separately a functorial cellular factorization. It never identifies the latter with a full-fence mapping-path factorization, and no endpoint-fibre proof bridges them.

### BISITE B.20 — Word reversal does not repair all-type paths

**Location:** 105/003, undeveloped Ch(C). **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.20, source line 168; VII ms.161--166; PATHS E.3. **Register status:** claim (return: Refuted).

No word-reversal operation or counterexample to its proposed repair occurs. The lack of a complete path definition prevents deciding this row from the cancelled sheet.

### BISITE B.21 — Strict bifibration R remains open

**Location:** 105/003, final question. **Kind:** conjecture / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.21, source line 169; STRATA E.11; PATHS E.6 and E.11. **Register status:** claim (return: Open).

The question about a Quillen structure concerns replacement-like fibration behavior but provides no strict bifibration R. It therefore records interest in the problem without resolving the open assertion.

### BISITE B.22 — Maximal simplicial classes under every base change

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE B.22, source line 170; Lead 1; XII ms.222--226. **Register status:** claim (return: Proved).

No universal simplicial pullback-preservation classification is given. The additional base-change property on 032 does not include a maximality or all-bases recognition argument.

### BISITE C.1 — Categories of elements and presheaf fine classes

**Location:** 105/020, A₀×T target case. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.1, source line 171; VI ms.83; XII ms.224--225. **Register status:** claim (return: Proved).

The source explicitly wants a componentwise theory on presheaves of `A₀×T`. It does not state the categories-of-elements fine-class criterion or its localization theorem, so this is a related target setting rather than the complete result.

### BISITE C.2 — Test categories do not give autodual fine theories

**Location:** 105/020, desired local test categories. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.2, source line 172; XII ms.224--225; Part C. **Register status:** claim (return: Refuted).

The test-category hypothesis is part of the model-recognition goal, with no assertion of autoduality for the fine presheaf theory. Thus the context's warning limits an inference that the manuscript itself has not made.

### BISITE C.3 — Elementwise smooth and proper criteria

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.3, source line 173; XII ms.224--225; Part C. **Register status:** claim (return: Refuted).

No elementwise presheaf smoothness/properness classification appears. Properness of the special replacement on 045 is not the general criterion for categories-of-elements maps.

### BISITE C.4 — Extra involutive duality for presheaf theories

**Location:** 105/050, D^o. **Kind:** reading question / limited comparison. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.4, source line 174; VI ms.84; XII ms.224--225. **Register status:** claim (return: Proved).

“Der 6′ pour D ... Der 6 pour D^o” invokes opposition of a derivator. It does not equip a presheaf fine theory with the additional involutive duality required in the context row.

### BISITE C.5 — Higher strict Theorem A

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.5, source line 175; Recent-results family 317; Part C. **Register status:** claim (return: Known).

No strict higher-category Theorem A is stated. Even the general ordinary relative theorem is absent, so it cannot be promoted to the higher result.

### BISITE C.6 — Two higher fine oppositions

**Location:** 105/050, ordinary opposition only. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.6, source line 176; Recent-results family 317; XII ms.224--225. **Register status:** claim (return: Proved).

The D/D^o comparison does not distinguish the two cell-level higher oppositions. No higher fine-slice variance table is present.

### BISITE C.7 — Cellwise opposites preserve higher equivalences

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.7, source line 177; Recent-results family 317; Part C. **Register status:** claim (return: Proved).

The package uses ordinary categories and their indexing opposites, with no cellwise duality theorem for strict higher categories. The context statement therefore has no manuscript form here.

### BISITE C.8 — Thomason structures on strict 2-categories

**Location:** 105/003 and 030–040, ordinary model questions. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.8, source line 178; Recent-results family 317. **Register status:** claim (return: Known).

The question on 003 is explicitly about Cat, and the later abstract construction supplies no strict 2-category application. No 2-Cat Thomason model structure or proof is stated.

### BISITE C.9 — Absolute higher model structures give only coarse information

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.9, source line 179; VI ms.83; Recent-results family 317. **Register status:** claim (return: Proved).

No higher model structure or distinction between its coarse and fine slice theories is developed. The general recognition argument in M does not identify such theories automatically.

### BISITE C.10 — Open higher fine recognition

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE C.10, source line 180; Recent-results family 317; Parts C and E. **Register status:** claim (return: Open).

There is no recognition theorem over a genuinely higher base or construction of lax-comma coherence. The open item remains untouched by the ordinary-category square argument.

### BISITE E.1 — Formal fine-slice operations

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.1, source line 181; XII ms.207–208, 216–218, 226. **Register status:** claim (return: Proved).

The source does not construct the formal fine-slice categories and their operation calculus. Its derivator direct images concern a particular excision diagram and cannot supply that entire formalism.

### BISITE E.2 — Arbitrary raw pullback fails

**Location:** 105/045–046 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.2, source line 182; XII ms.226; Lead 3. **Register status:** claim (return: Refuted).

The fibre calculation invokes properness, and property 4 restricts pullback to the selected F. This respects the need for hypotheses but neither states nor proves the later counterexample to arbitrary raw pullback.

### BISITE E.3 — Three Kan functors require recognition and enhancement

**Location:** 105/045–051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.3, source line 183; VI ms.108–113; XII ms.225–227. **Register status:** claim (return: Proved).

The source uses derivator Kan functors and their duals, but gives no recognition theorem for three Kan operations arising from a fine-slice enhancement. Its use of an existing coherent D(Q) is not a construction of such an enhancement.

### BISITE E.4 — Coefficient localization and exact squares

**Location:** 105/045–046 and 051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.4, source line 184; VI ms.138–169; XII ms.226. **Register status:** claim (return: Proved).

The calculation through fibres and the counit for ρ are concrete instances of coefficientwise exactness reasoning. No general coefficient-localization recognition theorem or classification of all exact squares is stated.

### BISITE E.5 — Cat fine theory and finite Alexandrov examples

**Location:** 105/043–045, categorical opens. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.5, source line 185; VI ms.81–84, 108–113. **Register status:** claim (return: Proved).

A cover by two categorical opens appears, but no equivalence among the specified Cat fine theory, finite Alexandrov theory, and coarse locally constant theory is developed. The open-cover notation alone does not establish those identifications.

### BISITE E.6 — Coarse theory need not equal locally constant fine theory

**Location:** 105/047, cancelled coefficient clause. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.6, source line 186; VI ms.108–113; arbitrary-W lead. **Register status:** claim (return: Refuted).

The manuscript notices locally constant coefficients but does not define or identify the two whole theories in this row. Its cancellation is not a counterexample to their equality and does not supply a classification for arbitrary W.

### BISITE E.7 — Enough intrinsic fibrations and Brown finite structure

**Location:** 105/030–032 and 034–040. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.7, source line 187; XII ms.240–261; XIII ms.7–12; PATHS D.8,D.17,D.18. **Register status:** claim (return: Proved).

Factorization and an extra properness condition are the closest structural input. The source does not prove the general intrinsic-fibration-to-Brown criterion or verify its finite-limit hypotheses in the intended intrinsic category.

### BISITE E.8 — Accessible factorization and nullification

**Location:** 105/034–040. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.8, source line 188; XVI Loc (7 F); POLES E.2–E.3. **Register status:** claim (return: Known).

The small-object theorem keeps a small family of generators and accessible objects, then asks to remove the restriction. It does not classify factorization by nullification localizers, nor establish that every accessible localizer has the additional intrinsic properness property.

### BISITE E.9 — Path objects require a universal source-equivalence

**Location:** 105/003; 016–018, different universal interval condition. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.9, source line 189; XVI Loc (7 F); PATHS E.5. **Register status:** claim (return: Proved).

The cancelled endpoint-fibration question does not verify a universally W-equivalent source evaluation. The universal interval condition in the topos construction is a related mechanism in a different setting, so it cannot fill that missing path-object proof without an explicit comparison.

### BISITE E.10 — Groupoid coarse/fine collapse

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.10, source line 190; VI ms.83–84; OpenAI family 312 lead. **Register status:** claim (return: Proved).

No groupoid specialization of the fine/coarse theories is given. The ordinary-category replacement argument does not establish the context's collapse theorem.

### BISITE E.11 — Functorial replacements and fibre axioms

**Location:** 105/036–038. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.11, source line 191; XII ms.217–218; XIIc B062. **Register status:** claim (return: Proved).

“functorial factorization” is an explicit claim and a potentially useful method. The manuscript does not derive the specified fibre axioms or compare all intermediate fibre-category localizations, which are additional conclusions in the row.

### BISITE E.12 — Six-object counterexample revisited

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.12, source line 192; XII ms.217–218; XIIc B062. **Register status:** claim (return: Refuted).

No finite example separating the fibre axioms is present. The author's a–d list on 022 is a different list about model recognition, so its unresolved item cannot be equated with this counterexample.

### BISITE E.13 — Coherent diagrams versus diagrams in a homotopy category

**Location:** 105/046–047, σ and its skeletal square. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.13, source line 193; PATHS D.20; STRATA C.7. **Register status:** claim (return: Refuted).

The words “plus précisément ... le carré abstrait σ” locate the desired property in the coherent diagram category. This closely anticipates the row's distinction, although no explicit example of nonfaithfulness or general comparison functor theorem is proved.

### BISITE E.14 — Nullification and local Cartesian closure

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE E.14, source line 194; POLES E.2–E.3 modality/LCC comparison. **Register status:** claim (return: Proved).

No nullification criterion for local Cartesian closure is stated. The cartesian/cocartesian square proposal concerns a different exactness property and is not such a criterion.

### BISITE F.1 — Derivator Kan triples and comma formulas

**Location:** 105/045–046, 049–051. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.1, source line 195; I; VI ms.138–169. **Register status:** claim (return: Known).

Fibrewise right direct images, the dual exclamation direct image, and the ρ counit are used explicitly. They supply concrete forms of part of the Kan-extension method, but the complete Der 1–4 triple and every comma formula are not restated or proved in these pages.

### BISITE F.2 — Proper and smooth strict base change

**Location:** 105/045 and 051; proposed extensions on 053. **Kind:** unpursued implication / unproved claim. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.2, source line 196; VI ms.138–169; STRATA D.4. **Register status:** claim (return: Proved).

Properness of φ̄ and smoothness/properness of ρ are used to support particular comparisons. The final strengthened versions are unproved, so the source does not supply a complete converse classification of all base-change squares.

### BISITE F.3 — Strict squares are not automatically exact

**Location:** 105/047 and 049–050. **Kind:** self-flagged / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.3, source line 197; Lead 3. **Register status:** claim (return: Refuted).

“sous certaines conditions” and “Der 6 (provisoire)” explicitly acknowledge that an extra square property is needed. The source does not assert the unrestricted strict-square exactness theorem refuted in the context, and it gives no specific counterexample beyond the separate Hot-square withdrawal on 052.

### BISITE F.4 — Monoidal projection formula

**Location:** 105/010–012, tensor/Hom lifting. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.4, source line 198; Lead 3; VI projection formulas. **Register status:** claim (return: Proved).

The tensor and pushout-product formulas translate lifting properties. They are not a derived Kan-extension projection formula, and no monoidal derivator hypotheses for that formula are stated.

### BISITE F.5 — Failure of an unqualified projection formula

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.5, source line 199; Lead 3. **Register status:** claim (return: Refuted).

No projection-formula counterexample is supplied. The doubts in the lifting-adjunction calculation concern a different assertion.

### BISITE F.6 — Right projection formulas and dualizability

**Location:** 105/050, dualizing-functor expectation. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.6, source line 200; Lead 3. **Register status:** claim (return: Proved).

A possible “foncteur dualisant” is mentioned as exceptional help in comparing the provisional axioms. No dualizability hypothesis, right projection formula, or limit-preservation proof appears.

### BISITE F.7 — Hom exchange and adjoint mates

**Location:** 105/010–012, Hom lifting adjunction. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.7, source line 201; VI exchange formulas. **Register status:** claim (return: Proved).

The source gives a formal tensor/Hom adjunction argument for lifting classes. It does not construct the specific exchange morphism between Kan functors or prove a mates-based Hom-exchange theorem, so the shared adjunction technique is the connection.

### BISITE F.8 — Opposition of the derivator and its base

**Location:** 105/050, NB. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.8, source line 202; VI ms.84. **Register status:** claim (return: Proved).

“Der 6′ pour D ... Der 6 pour D^o” explicitly links the two provisional axioms by opposition, and the diagrams display opposite indexing shapes. This is a close local form of the variance principle, though the full modern bookkeeping of base and coefficient opposition is not separately developed.

### BISITE F.9 — Exceptional sequences for complementary open/closed pieces

**Location:** 105/043–047, two-open cover. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.9, source line 203; I; VI open–closed formulas. **Register status:** claim (return: Known).

The source studies a cover by two opens, not a complementary open/closed recollement with exceptional functors. A square for their intersection does not provide the pointed exact sequences in this row.

### BISITE F.10 — Six-functor correspondence enhancement

**Location:** 105/050, duality expectation; 051, shifts. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.10, source line 204; Lead 3; Mann correspondence question. **Register status:** claim (return: Proved).

The manuscript's duality and shifted-derivator remarks indicate related ambitions. It does not build a correspondence category, coherent extension, or six-functor enhancement, and the README's separate question about cote 115 remains outside this package.

### BISITE F.11 — Étale equality and finite-bifibration ambidexterity

**Location:** 105/050–051. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.11, source line 205; Lead 3 terminology. **Register status:** claim (return: Proved).

No theorem `f!=f*` for an étale class or universal ambidexterity classification is stated. The exclamation on ψ denotes a left direct-image operation in a proposed axiom, not an exceptional-functor identification.

### BISITE F.12 — Smooth maps are not closed under diagonals

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.12, source line 206; Mann versus later geometric-setup conventions. **Register status:** claim (return: Refuted).

The source does not test diagonal closure of the smooth class or give the separating map. Its particular smooth ρ on 051 is not a maximal diagonal-stable classification.

### BISITE F.13 — Multiderivators and correspondence coherence

**Location:** 105/051, demand on all D_I. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.13, source line 207; Hörmann comparison. **Register status:** claim (return: Known).

The demand for shifted axioms is genuinely diagramwise. It does not construct a monoidal multiderivator or the coherence of a correspondence extension, which is additional structure in the context row.

### BISITE F.14 — Anel–Weinberger calibration

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.14, source line 208; Anel–Weinberger comparison. **Register status:** claim (return: Proved).

No abstract six-functor calibration or comparison with the cited framework appears. The duality speculation on 050 supplies no check of that framework's hypotheses.

### BISITE F.15 — Genus-zero mapping-class examples

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.15, source line 209; STRATA genus-zero comparison. **Register status:** claim (return: Known).

There are no moduli or mapping-class-group examples. The square and fork categories are unrelated to the stated genus-zero application.

### BISITE F.16 — Forgetting markings: proper but not smooth

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.16, source line 210; STRATA forgetting-mark question. **Register status:** claim (return: Proved).

No forgetful map of marked objects or proof of its proper/smooth behavior occurs. Categorical properness on 045 is a different construction.

### BISITE F.17 — Geometric boundary base change

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.17, source line 211; STRATA geometric direct image and boundary base change. **Register status:** claim (return: Proved).

No moduli-boundary diagram or geometric boundary-piece calculation is supplied. The categorical two-open square is not a form of that specific application without additional geometric identification.

### BISITE F.18 — Open strict n-category Kan formalism

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.18, source line 212; Strict nCat-indexing question. **Register status:** claim (return: Open).

The manuscript has no strict n-category base, lax comma construction, or higher Kan-extension recognition theorem. Its ordinary derivator square discussion does not settle the open higher item.

### BISITE F.19 — Stable proper class of finite bifibrations

**Location:** 105/050–053, duality and proper/smooth language. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE F.19, source line 213; Mann proper-class question. **Register status:** claim (return: Proved).

The source links duality expectations with proposed proper/smooth excision variants. It does not impose the stable coefficient and universal ambidexterity conditions or classify the finite bifibration class in the context row.

### BISITE G.1 — Stable finite limits commute with finite colimits

**Location:** 105/050, proposed Der 6; 052, withdrawal. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.1, source line 214; Lead 4 stable-derivator input. **Register status:** claim (return: Known).

The proposed equality of cartesian and cocartesian squares is close to the stable exactness mechanism. It is not supplied with stable hypotheses or a general commutation theorem, and its unrestricted Hot application is explicitly withdrawn.

### BISITE G.2 — Spectral dualizing weight

**Location:** 105/050, “foncteur dualisant”. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.2, source line 215; Lead 4 dualizing-object and limit-colimit clause. **Register status:** claim (return: Proved).

The author suggests a dualizing functor as a possible way to compare homology and cohomology. No spectral weight or explicit duality kernel is written, so the context formula is a later comparison rather than a transcription of this idea.

### BISITE G.3 — Failure of a pointwise dualizing twist

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.3, source line 216; Lead 4 exaggerated objectwise interpretation. **Register status:** claim (return: Refuted).

No pointwise twist formula is proposed or refuted. The broad duality expectation on 050 does not include the formula that the context row rejects.

### BISITE G.4 — Transitivity of duality kernels

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.4, source line 217; Part G compatibility and transitivity. **Register status:** claim (return: Proved).

No kernel composition or transitivity identity appears. The composition of Kan functors on 046 is not a construction of duality kernels.

### BISITE G.5 — Dualizing weight is not naive restriction

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.5, source line 218; Part G unrestricted dualizing-weight base change. **Register status:** claim (return: Refuted).

The source gives no dualizing-weight restriction formula and no example distinguishing it. The coefficient restriction maps in the square have a different purpose.

### BISITE G.6 — Finite-coefficient duality

**Location:** 105/050, exceptional dualizing-functor case. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.6, source line 219; Part G suitable finiteness subcategories. **Register status:** claim (return: Proved).

The phrase “cas exceptionnel” flags a possible coefficient duality that could relate the two axioms. No finiteness conditions or finite-category duality theorem are stated, so the row supplies a precise direction in which the manuscript's expectation might be tested.

### BISITE G.7 — Finite EI categories need not admit the proposed weights

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.7, source line 220; Part G finite EI scope. **Register status:** claim (return: Refuted).

No finite EI category or weighted-duality counterexample is present. The small indexing diagrams do not establish weighted duality for all finite categories.

### BISITE G.8 — Finite-group norm with invertible order

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.8, source line 221; Part G coefficient-sensitive finite EI class. **Register status:** claim (return: Proved).

There is no finite-group norm map or invertibility-of-order hypothesis. The dualizing-functor remark cannot be read as this ambidexterity theorem.

### BISITE G.9 — Gorenstein duality for finite posets

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.9, source line 222; Lead 4 corrected equivalence; Part G finite posets. **Register status:** claim (return: Known).

No Gorenstein condition or finite-poset duality calculation is given. The square-shaped posets are used as diagram shapes, not as instances of the context classification.

### BISITE G.10 — Minimal-vertex constructible dictionary

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.10, source line 223; STRATA A.4 A.5; Part G prerequisite dictionary. **Register status:** claim (return: Proved).

The source does not construct a minimal-vertex realization or identify constructible sheaves through it. The categorical open-cover argument supplies no such geometric dictionary.

### BISITE G.11 — Verdier duality need not preserve minimal constructibility

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.11, source line 224; Lead 4 unconditional geometric identification. **Register status:** claim (return: Refuted).

No Verdier-duality example or failure of a constructibility convention appears. The word “dualisant” on 050 is not a theorem about constructible sheaves.

### BISITE G.12 — Geometric Verdier kernel comparison

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.12, source line 225; Part G positive geometric identification. **Register status:** claim (return: Known).

No geometric kernel is defined or compared with a categorical one. The supplied context's verification adds information external to the manuscript package.

### BISITE G.13 — Unstable limits are not fixed colimit weights

**Location:** 105/052, “Complètement faux”. **Kind:** withdrawn in the same text / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.13, source line 226; Part G unstable clause. **Register status:** claim (return: Refuted).

The explicit rejection of the universal Hot-square claim is a close warning against extending stable exactness reasoning to unstable spaces. It is not the context's weighted-limit counterexample, but it records the same need to distinguish unstable and stable assertions.

### BISITE G.14 — Tree orientations and strong stable equivalence

**Location:** 105/050 and 053, fork oppositions. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, BISITE G.14, source line 227; Lead 4 Groth-Stovicek contribution. **Register status:** claim (return: Known).

Opposite fork shapes occur in the provisional duality discussion. No reflection functor, arbitrary-tree construction, or strong stable equivalence theorem is supplied, so the diagrams offer a suggestive special shape rather than the result.

## Dossier family: RESIDUE

### RESIDUE B.1 — Component-dependent absolute/relative distinction

**Location:** 105/045–046, special α-equivalence. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.1, source line 235; XVI ms.1–3. **Register status:** claim (return: Proved).

No general absolute or relative Theorem A is formulated, and there is no component-dependent localizer construction. The particular α used in excision does not identify the two versions of Theorem A.

### RESIDUE B.2 — Hot quotient through S¹

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.2, source line 236; No manuscript-page locator supplied in this row. **Register status:** claim (return: Proved).

No quotient of Hot through S¹ or associated localization example appears. The source's Hot_W square does not define the quotient in this row.

### RESIDUE B.3 — Saturation does not repair absolute Theorem A

**Location:** 105/025 and 028, saturation discussion. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.3, source line 237; XVI ms.1–3, Loc(1bis)/(1ter)+absolute Loc(3). **Register status:** claim (return: Refuted).

The manuscript discusses direct factors and strong saturation but does not use them to derive relative Theorem A from an absolute form. The context's obstruction therefore constrains an inference not actually made on these pages.

### RESIDUE B.4 — Finite 10-to-6 certificate over a three-object base

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.4, source line 238; No manuscript-page locator supplied in this row. **Register status:** claim (return: Proved).

No such finite functor or certificate is supplied. The three-object fork used for excision is not the counterexample merely because its object count agrees with the stated base.

### RESIDUE B.5 — Natural homotopies and adjoint functors

**Location:** 105/052, W7 bis parenthesis. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.5, source line 239; XVI Rappel1.2, ms.3. **Register status:** claim (return: Known).

The two composites are said to be homotopic “par un chemin de longueur 2,” through length-1 homotopies to the inclusion of X₀. This is a concrete form of the natural-homotopy mechanism, but no general theorem about every adjoint functor is stated or proved here.

### RESIDUE B.6 — Opposition invariance W=W^o

**Location:** 105/050, D/D^o comparison. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.6, source line 240; XVI Rappel1, ms.2. **Register status:** claim (return: Known).

The source identifies the dual provisional derivator axiom by passage to D^o. It does not state an opposition-invariance theorem for every fundamental localizer, so the derivator duality is only a related form.

### RESIDUE B.7 — XVI Proposition 1.3 and Theorem A scope

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.7, source line 241; XVI Proposition1.3, ms.3–8. **Register status:** claim (return: Proved).

The proposition's absolute-versus-relative scope is not discussed. No general Theorem A statement here can be used to determine that later proposition's interpretation.

### RESIDUE B.8 — Finite-product closure and literal hypotheses

**Location:** 105/007–012, product lifting conditions. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.8, source line 242; XVI Rappel2.3 and Proposition2.4, ms.9–10. **Register status:** claim (return: Refuted).

The manuscript explicitly works out additional product and internal-Hom closure conditions rather than treating every product assertion as part of the definition of W. It does not state the exact localizer theorem in this row, but it supports keeping hypotheses separate from derived closure properties.

### RESIDUE B.9 — Historical saturation terminology

**Location:** 105/005, 025, 027–028. **Kind:** reading question / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.9, source line 243; No manuscript-page locator supplied in this row. **Register status:** claim (return: Known).

“mild saturation,” direct-factor stability, and localization-theoretic “strongly saturated” are visibly distinguished and sometimes questioned. This is direct historical material for the terminology audit, with the caveat that later conventions must not silently replace the definitions or uncertain wording on these sheets.

### RESIDUE B.10 — Historical audit of strong Mayer–Vietoris excision

**Location:** 105/043, 047, 052–053. **Kind:** self-flagged / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.10, source line 244; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

“Pour avoir l'implication inverse” on 047 and “Forme renforcée de W7” on 052 provide explicit local stages in the stronger excision proposal. The package adds those formulations and qualifications, but gives no dated archive-wide priority or complete proof of the later strong Mayer–Vietoris claim.

### RESIDUE B.11 — Finite coproducts and filtered closure do not give decomposition

**Location:** 105/018 and 034–040. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.11, source line 245; XVI ms.9, Corollary2.2 parenthesis. **Register status:** claim (return: Refuted).

The source uses filtering-limit and cellular closure to build factorizations. It does not infer the context's decomposition axiom from those closures alone, so no counterexample to its stated construction follows from this row.

### RESIDUE B.12 — Formal decomposition and finite localization

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.12, source line 246; XVI2.1,2.2 principal clause,2.5 finite intended version,2.6; XV9.4 formal equivalences,9.5,9.6. **Register status:** claim (return: Proved).

No decomposition theorem for the specified finite localization is given. The factorization theorem concerns lifting classes and a small generating set, not that localization's components.

### RESIDUE B.13 — π₀ adjunctions with discrete categories

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.13, source line 247; XVI second2.8,second2.9,2.11–2.14. **Register status:** claim (return: Known).

There is no statement that π₀ has the specified two adjoint relations with discrete categories. The π₀ condition on 052 belongs to a withdrawn square criterion and does not supply this result.

### RESIDUE B.14 — Formal directions of cube implications

**Location:** 105/052, Der 8. **Kind:** self-flagged / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.14, source line 248; XVI3.1, ms.18′. **Register status:** claim (return: Proved).

The manuscript explicitly distinguishes `b+c⇒a` for cartesian squares and `a+c⇒b` for cocartesian squares, and marks the additional `a+b⇒c` with “?”. This is a close form of the context's direction audit, but the hypotheses of the derivator cube and of the localizer cube must be matched rather than treating every displayed two-of-three statement as formal.

### RESIDUE B.15 — Product closure needs a localizer hypothesis

**Location:** 105/005 and 007–012. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.15, source line 249; XVI2.5 arbitrary-W literal wording. **Register status:** claim (return: Refuted).

The construction starts with stated conditions on W, including isomorphisms and saturation, and then investigates products. It is not a theorem for an arbitrary class of arrows, so the context's warning against that broader formulation does not contradict the manuscript's setup.

### RESIDUE B.16 — Near-bijective component example

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.16, source line 250; XVI/XV literal absolute package. **Register status:** claim (return: Proved).

No near-bijective component localizer or separating example appears. The withdrawn π₀ coverage condition on 052 is a different statement about a square of spaces.

### RESIDUE B.17 — Failure of a literal nontriviality equivalence

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE B.17, source line 251; XVI2.7; XV9.9,9.10,9.12,9.13. **Register status:** claim (return: Refuted).

The specific equivalence involving nontriviality is neither stated nor tested. Nothing about the assumed W class or the isolated terminal object e supplies the row's counterexample.

### RESIDUE C.1 — Factorization gives Fib∩W=W_u

**Location:** 105/030–032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.1, source line 252; No manuscript-page locator supplied in this row. **Register status:** claim (return: Proved).

The source proves `F∩W=TF` for its orthogonal factorization pairs and adds properness as condition 4. It does not identify F with all intrinsic fibrations or TF with W_u in the full generality of the context row, so the comparison is a conditional model instance to investigate.

### RESIDUE C.2 — Intermediate localization without functoriality

**Location:** 105/036–038, functorial factorization. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.2, source line 253; XII ms.215–218,240; XIIc B062 with factorization. **Register status:** claim (return: Proved).

The author constructs and values functorial factorization. He does not assert that functoriality is necessary for intermediate-slice localization, so the later claim that ordinary factorization suffices is an additional strengthening rather than a contradiction of these pages.

### RESIDUE C.3 — Five-object failure of the third axiom

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.3, source line 254; XII ms.215–218; XIIc B062 without factorization. **Register status:** claim (return: Refuted).

No five-object fibre-axiom counterexample is present. The distinct model-recognition items on 022 cannot be substituted for its a, b, c conditions.

### RESIDUE C.4 — Unbounded arrow search at fixed object number

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.4, source line 255; No manuscript-page locator supplied in this row. **Register status:** claim (return: Proved).

No finite-category enumeration problem or observation about unbounded arrow counts is stated. The recycled computer listings document another use of the paper and provide no such search evidence.

### RESIDUE C.5 — Perfect path replacement

**Location:** 105/003, tentative W∞-fibration; 002, RLP corollary. **Kind:** conjecture / partial connection. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.5, source line 256; No manuscript-page locator supplied in this row. **Register status:** claim (return: Proved).

The first leaves use perfect/fibration terminology, but the path projection remains “une chose à vérifier.” There is no explicit perfect path-replacement construction or full proof of its properties, so this package does not establish the later result.

### RESIDUE C.6 — Every intermediate perfect category localizes correctly

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.6, source line 257; XII ms.217, F_0,S. **Register status:** claim (return: Proved).

No theorem for every intermediate perfect fibre category is stated. The appearance of “W∞-parfait” on the first leaf is a different unproved lifting criterion, not a localization equivalence.

### RESIDUE C.7 — Derivative-fibre identities

**Location:** 105/032, pullback stability. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.7, source line 258; XII ms.240–241, footnotes128–130. **Register status:** claim (return: Proved).

Stability under base change along F is a related mechanism for comparing fibres. The source does not formulate the derivative-fibre identities attributed to XII ms. 240, nor verify all their slice hypotheses.

### RESIDUE C.8 — Minimal-object counterexample remains open

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE C.8, source line 259; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

No minimal-object search for the relevant fibre-axiom obstruction is attempted. The small drawn indexing categories are not candidates accompanied by the required axiom checks.

### RESIDUE D.1 — Intrinsic fibrations for truncation localizers

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.1, source line 260; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Known).

No W_n intrinsic-fibration classification is stated. The initial W∞ RLP tests do not give the row's truncation criterion.

### RESIDUE D.2 — Boundary-map criterion

**Location:** 105/002, spherical-looking tests, nearest limited connection. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.2, source line 261; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Proved).

The first leaf gives lifting tests for W∞-asphericity and properness, with uncertain exponents and an unproved corollary. It does not state the homotopy-boundary-map criterion for truncated intrinsic fibrations in this row.

### RESIDUE D.3 — Component lifting and π₀

**Location:** 105/052, withdrawn π₀ square condition. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.3, source line 262; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Proved).

The only nearby π₀ criterion concerns a square in Hot and is explicitly rejected. It is not a component-lifting criterion for intrinsic fibrations and supplies no proof or counterexample for this row.

### RESIDUE D.4 — Intrinsic fibrations need not be a right lifting class

**Location:** 105/003 and 022–032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.4, source line 263; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Refuted).

The English F is defined by RLP, whereas the cancelled French sheet only asks about W∞-fibrations and a Quillen structure. Because the manuscript has not identified that F with the whole intrinsic class, the context's obstruction does not contradict an established equality here; it identifies a necessary extra check.

### RESIDUE D.5 — Locally constant integral coefficients and W∞

**Location:** 105/046–047. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.5, source line 264; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Known).

The source expands coefficient scope and briefly considers locally constant ξ. It does not compute the resulting integral-coefficient equivalence class or identify it with W∞, so the later classification is not present.

### RESIDUE D.6 — Rational boundary map of degree two

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.6, source line 265; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Proved).

No rational degree-two boundary calculation or example separating integral and rational behavior appears. The source's general cohomological W is not specialized in this way.

### RESIDUE D.7 — General coefficient classification remains open

**Location:** 105/032, cohomological input W. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.7, source line 266; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

“W is given beforehand ... by cohomological criteria” treats the class as input rather than classifying every coefficient theory. No solution of the later general coefficient-classification problem is provided.

### RESIDUE D.8 — Nontrivial intrinsic covers for mod-p coefficients

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.8, source line 267; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Refuted).

No mod-p covering example or calculation of intrinsic fibration behavior is present. The proper/smooth constructions do not specify these coefficients.

### RESIDUE D.9 — General homology classification remains open

**Location:** 105/022 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.9, source line 268; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

The source asks for proper model behavior of a given cohomological W. It does not classify all homology intrinsic fibrations, and the unresolved generator and properness steps prevent extracting such a classification.

### RESIDUE D.10 — The finite 48-entry comparison remains unchanged

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.10, source line 269; XII ms.208,225; XVI §4; I ms.99–100; BISITE B.15 (all 48 entries). **Register status:** claim (return: Proved).

No matching finite table or recomputation is supplied. The manuscript's 48 retained scans and the register's 48 comparison entries are unrelated counts.

### RESIDUE D.11 — Loc(7) table for different localizers

**Location:** 105/002–003 and 032. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.11, source line 270; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Proved).

The early discussion is W∞-specific, and later pullback stability is an additional desired property for a chosen W. No table across truncation and homology localizers, or uniform Loc(7) assertion, appears.

### RESIDUE D.12 — Integral/rational covering monodromy

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE D.12, source line 271; XII ms.208,225; XVI §4; I ms.99–100. **Register status:** claim (return: Proved).

No classification of covers by trivial monodromy for these coefficient theories is given. The locally constant coefficient remark is too general and unfinished to supply the result.

### RESIDUE F.1 — Totality via action categories

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.1, source line 272; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases). **Register status:** claim (return: Proved).

The source does not state an action-category criterion for total asphericity. Its Grothendieck constructions encode excision diagrams, with no universal totality conclusion.

### RESIDUE F.2 — Totality and common-successor conditions

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.2, source line 273; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases). **Register status:** claim (return: Proved).

No total-asphericity theorem about common successors or affine parallel-arrow conditions is written. The filtering assumptions of the small-object construction are not a derivation of those conditions.

### RESIDUE F.3 — Unbounded subcategories of Δ_inj

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.3, source line 274; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases). **Register status:** claim (return: Proved).

Neither Δ_inj nor its unbounded full subcategories appears. Exactness, totality, and failure of filteredness in this row are therefore additional context, not a form of the manuscript's filtering-limit argument.

### RESIDUE F.4 — Weakly terminal total categories are filtered

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.4, source line 275; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases). **Register status:** claim (return: Proved).

No weak-terminal hypothesis is combined with total asphericity. The occurrence of terminal objects in individual square shapes cannot supply that categorical implication.

### RESIDUE F.5 — Converse from totality to exactness remains open

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.5, source line 276; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

The source does not relate total asphericity to exact abelian colimits. Its use of colimit preservation and accessible objects addresses a different problem and leaves this open item untouched.

### RESIDUE F.6 — Total presheaves and composed Dwyer maps

**Location:** 105/012–018, pushout products in a topos. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.6, source line 277; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

The source's pushout-product construction has monomorphisms and intervals as input. It does not introduce total presheaves or the boundary-weight condition for composing Dwyer maps, so the open context assertion cannot be inferred from those closure calculations.

### RESIDUE F.7 — Universal Cat-colimit correctness and filteredness

**Location:** 105/038–040, nearest different colimit discussion. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE F.7, source line 278; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

No classification of universally correct ordinary Cat-colimit shapes is attempted. The continuous-ordinal closure lemma does not answer whether all connected shapes with the context's universal comparison property must be filtered.

### RESIDUE I.1 — Diagonal-stable smooth maps are discrete fibrations

**Location:** 105/051, a particular smooth ρ. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.1, source line 279; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

The source does not test the strict diagonal of an arbitrary smooth map or characterize discrete fibrations. A single proper/smooth ρ is not a form of the maximal diagonal-stable classification.

### RESIDUE I.2 — Space-valued ambidexterity forces isomorphism

**Location:** 105/050–052, duality expectation and unstable withdrawal. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.2, source line 280; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

The source's expectation of a dualizing functor and its rejection of a universal Hot-square assertion show why unstable and stable cases need separation. No universal left/right Kan ambidexterity test for discrete fibrations is stated, so the exact isomorphism classification is absent.

### RESIDUE I.3 — Enhanced correspondence functor with smooth legs

**Location:** 105/050–051, duality and shifted axioms. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.3, source line 281; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

The manuscript raises duality and diagramwise conditions but does not construct an infinity-categorical correspondence functor or prove its coherence. The presentable monoidal enhancement and its hypotheses in the context row are additional data, not implicit in D(e).

### RESIDUE I.4 — Cancellation obstruction in a proposed correspondence proof

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.4, source line 282; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

No suitable-decomposition cancellation axiom or [1] counterexample is discussed. The manuscript's own smooth/proper examples cannot verify the hypotheses of the later abstract correspondence theorem.

### RESIDUE I.5 — Opposite-base proper correspondence theory

**Location:** 105/050, D/D^o. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.5, source line 283; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

The explicit duality of Der 6 and Der 6′ is a local antecedent of opposition-based variance changes. It does not build the proper-leg correspondence formalism, classify its diagonal-stable maps, or prove exceptional functors have trivial twist.

### RESIDUE I.6 — Pointed-space ambidexterity and component inclusions

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.6, source line 284; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

No universal ambidexterity classification for pointed spaces occurs. The π₀ coverage test on 052 is withdrawn and is not a statement about inclusions of connected components.

### RESIDUE I.7 — Reversible-localizer and bare-derivator open problems

**Location:** 105/047, 050, 052. **Kind:** conjecture / partial antecedent. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.7, source line 285; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

The reverse-excision goal, the duality expectation, and the strengthened W7/W8 axioms are direct historical forms of the reversibility problem. The cancelled locally constant clause on 047 indicates interest in changing coefficient scope, but supplies neither a natural assignment D→D′ on all bare derivators nor a classification of reversible accessible localizers.

### RESIDUE I.8 — Stable ambidexterity and finite discrete bifibrations

**Location:** 105/050–053, proposed duality and proper/smooth variants. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.8, source line 286; BISITE F.10–F.12 and F.19. **Register status:** claim (return: Proved).

No spectrum or D(k) coefficient category, norm comparison, or finite-fibre classification is stated. The source suggests a duality program whose precise stable realization is additional content in the context row.

### RESIDUE I.9 — Enhanced locally constant towers and second stages

**Location:** 105/047, cancelled lc clause. **Kind:** unpursued implication. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE I.9, source line 287; Prompt I(3), concrete enhanced second stages for spectra and D(F_p); GALOIS E.8/E.10 independently checked; bare-derivator GALOIS E.11/G.6 remains Open. **Register status:** claim (return: Proved).

The phrase “coeff. loc. constants” is a narrow antecedent of the coefficient-scope question. There is no tower, localized-space realization, Ω-test, spectrum calculation, or mod-p second-stage formula, and the context's enhanced construction must remain distinct from the open bare-derivator assertion in I.7.

### RESIDUE J.1 — Strict 2-category slices over an ordinary base

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE J.1, source line 288; VI ms.83; BISITE C.10 and F.18. **Register status:** claim (return: Proved).

No Street nerve or 2-Cat slice recognition theorem is given. The ordinary-category cofibred replacement is not a higher strictification or straightening result.

### RESIDUE J.2 — Recognition over bases with nontrivial 2-cells

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE J.2, source line 289; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

The source does not consider a walking noninvertible or invertible 2-cell or retain its lax-triangle action. Its ordinary squares do not solve the open higher-base recognition problem.

### RESIDUE J.3 — Higher pullback classes and lax-comma base change

**Location:** 105/002–053, no form found. **Kind:** source comparison; no form found. **Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), `DOSSIER_STATEMENTS_WITH_STATUS.md`, RESIDUE J.3, source line 290; No manuscript-page locator supplied in this row. **Register status:** claim (return: Open).

No higher boundary-piece test or lax-comma Der 4 theorem is stated. The ordinary proper/smooth calculations and proposed excision axioms supply no proof of the open higher variance table.

## Source register and research limits

### Primary manuscript consulted

Grothendieck, A. (n.d.). *Mathematical working notes preserved in cote 105* [Manuscript, catalogue label “[Champs (stacks) 2] : notes manuscrites (s.d.)”]. Montpellier archive, cote 105, retained PDF scans 002–053. Supplied images: `MPL_105_105_scanNNN.jpg` and their `_a`/`_b` halves; the frozen diplomatic reading is in `MPL_105_transcription.tex` and `pages/`. The reused printed support is included in the transcription without attributing every printed item to the author of the handwritten notes.

### Supplied primary-text comparison witnesses

Grothendieck, A. (n.d.). *Les Dérivateurs*, Chapter II, manuscript pp. 32–36ter [Text reproduced with commentary in the supplied companion]. `companion/chunks/DER_II-a.tex`; claim index II-C-003 in `companion/LesDerivateurs_companion.tex`. The question about total asphericity is at ms. 36; the index explicitly associates the conjecture with ms. 36 and 36ter.

Grothendieck, A. (n.d.). *Les Dérivateurs*, Chapter XII, §5, manuscript pp. 75–80 and subsequent comparisons [Text reproduced with commentary in the supplied companion]. `companion/chunks/DER_XIIb-a.tex`; for the later total-category square/cube and proper/smooth comparisons, `companion/chunks/DER_XIIb-b.tex`, ms. 125–127 and 147–149. The primary-text W(7 bis) square and W(7) cube statements are kept distinct from the companion's editorial commentary blocks dgrb516–517 and dgrb555–556 and from the research-return review claims.

Grothendieck, A. (n.d.). *Les Dérivateurs*, Chapter XIII, §§1–2, manuscript pp. 5–8 [Text reproduced with commentary in the supplied companion]. `companion/chunks/DER_XIII-a.tex`. The directly compared primary-text passages define Quillen pairs, state a small-generator theorem, and distinguish weak model inclusions from trivial-class equalities and the additional properness requirement.

Grothendieck, A. (n.d.). *Les Dérivateurs*, Chapter XV, §1, manuscript pp. 1–12 [Text reproduced with commentary in the supplied companion]. `companion/chunks/DER_XV-a.tex`, especially formula (1.23), Theorem 1, and Corollaries 1–2. The all-squares attachment, functoriality note at ms. 10, and source-accessibility assumption at ms. 11 are the directly inspected comparison points.

Grothendieck, A. (n.d.). *Les Dérivateurs*, Chapter XIX, §1, manuscript pp. 2–7 [Text reproduced with commentary in the supplied companion]. `companion/chunks/DER_XIX.tex`, especially Theorem 1.1, its functoriality footnote, and Corollary 1.2; the commentary block dgrb1161 supplies the displayed small-object and retract arguments. The theorem's statement is a primary-text comparison; the explanatory proof and references embedded in the commentary are secondary claims of the supplied companion.

Grothendieck, A. (n.d.). *Pursuing Stacks*, Chapter VI, §125, manuscript pp. 530–532, dated “13.10.” in the supplied text [Typed transcription]. `ps_chapters_VI_VII/ps6.tex`. The comparison used here is the discussion of weak equivalences as basic data and the role of auxiliary cofibration/fibration structures, not an endorsement of every mathematical expectation in that historical passage.

Grothendieck, A. (n.d.). *Pursuing Stacks*, Chapter VII, §§136–137, manuscript pp. 568–577 [Typed transcription]. `ps_chapters_VI_VII/ps7.tex`. The directly checked passages concern the distinction between ordinary homology Kan extension and a possible exceptional formalism, the cohomological meanings of proper/smooth, and the additional finiteness or duality expectations. Dates are not inferred for cote 105 from these passages.

The companion and typed *Pursuing Stacks* files are the supplied witnesses, not a fresh collation against their manuscript images. “n.d.” in these entries reflects the absence of a separately verified bibliographic edition date for the supplied excerpt; it does not claim that the underlying works are undatable. The README identifies the *Pursuing Stacks* source as the typed text associated with arXiv:2111.01000, but no external edition or article was newly downloaded for this task.

### Supplied research registers

*Context for the research notes: Package 73 (cotes 105).* (2026, November 12; additional state-file note dated November 15). `README.md` in the supplied context archive. This is the source of the research questions, catalogue wording, and warnings about unreviewed prior runs.

*Results proved while writing the companion that we did not find in the literature.* (2026, November 12, with the supplied credit/review annotations). `NEW_RESULTS.md`. All twelve numbered entries and its three “Known after all” addenda are compared above; authorship and review claims are those reported by this register.

*DOSSIER_STATEMENTS_WITH_STATUS.* (n.d.). [Supplied research-return register]. `DOSSIER_STATEMENTS_WITH_STATUS.md`. The comparison contains all 10 STRATA, 76 PATHS, 113 BISITE, and 56 RESIDUE statements, each with its exact ID and the register's own status; an empty manuscript-reference cell is explicitly reported rather than replaced by an invented scan.

*RESULTS_STATE.* (2026, November 15, supplied snapshot). `notes/RESULTS_STATE.md`. Principal connected IDs are GALOIS B.1/B.3/B.4/B.13, D.2, E.11/G.6; POLES B.2/F.14; TOTASPH A.9/A.13/C.10; and the dossier IDs named throughout. A “Proved” or “Refuted” return label is not automatically a review record; the explicit review reports in `NEW_RESULTS.md` are distinguished wherever used.

Hua, M., project findings register. (n.d.). Entries `105-interval-anodyne-generators` and `105-derivator-crible-excision` [AI-produced findings quoted in the supplied research state]. Source consulted: `notes/RESULTS_STATE.md`, “Findings of another project on these pages, to check.” The original website was not independently retrieved; R14 and R15 assess the quoted findings against the present scans, and the register's page-to-scan offset is not generalized beyond its stated convention.

*Pursuing Stacks contents.* (n.d.). `PURSUING_STACKS_CONTENTS.md` [Supplied section index]. Used to locate sections and titles, not as evidence for proofs in chapters whose full text was not supplied or inspected.

### What these notes do and do not establish

The affirmative documentary findings are the interval/lifting construction and its remaining generation problem, the conditional transfinite factorization, the sequence of proposed excision axioms, the distinction between coherent and skeletal squares, and the author's explicit verification flags and withdrawal. The negative findings about total-asphericity/filteredness, relative Theorem A, finite-monoid results, higher fine recognition, and six-operation classifications are bounded by these 48 scans. No priority claim or archive-wide dating follows from them.

Mathematical literature named inside the context—among it Quillen, Gabriel–Zisman, Artin–Mazur, Isbell–Mitchell, Cisinski, and the later commentary's references—is used here as a set of attributed comparison leads. These notes do not represent those external works as newly read or independently checked, and do not re-prove the results the supplied review record already treats as reviewed. The two Hua findings are checked directly against the manuscript rather than accepted because they appeared in a register.

The hardest readings remain the overwritten first-leaf corollary, the cancelled saturation sheet 027, the diagonal note on 016, the lower/gutter annotations on 049, parts of the revised Der 8 and W8 bis notes on 052, and the final diagram/suffix differences on 053. Interpretive comparisons depending on those readings remain qualified; `MPL_105_doubts.md` is the authoritative list of in-place transcription doubts and alternatives.

### Technical status of the deliverable

The package's checks establish the presence and order of all 48 page fragments, exact bytewise agreement of their concatenation with the combined fragment, completion of all 1,180 inventory rows, coverage of all 267 requested comparison IDs, and preservation of the 49 frozen SHA-256 hashes. Lexical checks also cover braces, environments, math delimiters, allowed commands, and explicit TikZ matrix-arrow targets. They do not certify the manuscript readings or the mathematics, and a full TeX compilation was unavailable because the installed engine lacked `pdflatex.fmt`; no compiled PDF is claimed or included.
