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

