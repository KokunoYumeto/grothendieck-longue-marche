# Context-only mapping for MPL_136_095–141

## Scope and citation convention

This mapping was prepared after the principal reader reported that the transcription had been frozen and the context opened. It uses only the supplied context files; it does not inspect the scans or the frozen transcription, establish new readings, or decide whether a particular scan confirms a contextual claim. Those comparisons remain with the principal reader.

Paths below are relative to `context/`. Line numbers are source-file line numbers. A **PS page** is the number explicitly encoded by the nearest applicable `\pspage{...}` marker in the supplied LaTeX; no printed-PDF pagination or archive scan number is inferred. When a marker occurs within a line, the number changes at that marker, rather than at the beginning of the line. The contents file supplies section titles but no corresponding page markers.

## What was supplied, and what is missing

The context contains `README.md`, `notes/RESULTS_STATE.md`, `PURSUING_STACKS_CONTENTS.md`, `ps_chapters_VI_VII/ps6.tex`, `ps_chapters_VI_VII/ps7.tex`, and the accompanying CC0 notice. README lines 29–33 describe the PS materials as the typed-up text and warn that material originating in earlier research runs must be treated as claims.

The most directly relevant retrospective is **PS §94**, whose title is given in `PURSUING_STACKS_CONTENTS.md`, line 120: “retrospective on the ``De Rham complex with divided powers''”. This belongs to Chapter V, identified at line 112. **Chapter V is not supplied.** Its retrospective cannot be reconstructed from its title or treated as read merely because Chapters VI–VII refer back to it.

The README states at lines 16 and 27 that the return for the first 45 scans of cote 136, sent as package 49, was not yet available. `notes/RESULTS_STATE.md`, lines 117–119, says: “None of ours meets these folders yet.” Accordingly, this context does not contain an earlier transcription or research-note return for cote 136 against which the present page readings can be compared. Nor does it supply cote 137, the cited scans of cotes 16 and 47, the full planning documents, the full underlying research-return CSV files, or the literature named in README lines 22–23. References to those absent files remain leads.

## Status caveats and relevant RESULTS_STATE IDs

`notes/RESULTS_STATE.md`, lines 5–8, distinguishes a return's claimed status from subsequent intake and referee checks. The broad warning is explicit: “a claim of a GPT-6 Astra ... run unless an intake verdict follows it” (line 7). The enumerated referee checks at line 8 concern specified LM4/LM7 entries; they do not certify the separate de Rham planning questions. Some return excerpts are themselves visibly truncated in the register. Their source paths at lines 134–149 identify absent full documents, rather than supplying the arguments.

| ID | Exact register location | Stated status | Legitimate use in these notes |
|---|---|---|---|
| **WG2 §2.4 #5** | `notes/RESULTS_STATE.md`, line 124 | Question/plan item, round 2, unchecked | Direct link for the proposed relation between divided powers on cochains and the two earlier integrality questions: the integral Lefschetz ring of cote 16 scan 14 and divisibility of δ′ powers in cote 47 scan 9. The row itself says “A thread, not a statement”; it cannot certify that the present manuscript establishes this bridge. |
| **WG H6** | `notes/RESULTS_STATE.md`, line 125 | Hunch, “Believe”, unchecked | Direct link for the conjectured relationship between finite-dimensional local systems, a fundamental localizer, and schematization in characteristic zero. A de Rham or schematization comparison bears on this target only to the extent supported by the new manuscript evidence; the register supplies no proof of the hunch. |
| **WG2 §Week #3** | `notes/RESULTS_STATE.md`, line 126 | Question/plan item, unchecked | Organizational pointer to the R-SCHEM dossier and cotes 137, 133, 153 plus PS extracts. It is not a mathematical result or an independent source for a specific comparison theorem. |

No directly settled result on this particular divided-power de Rham complex is supplied in the selected register. The many other rows concern different localizer, derivator, exactness, and total-asphericity problems. A shared word such as “abelian” or “semisimplicial” is not sufficient reason to map a manuscript claim to one of those IDs.

## Precise PS correspondences

### C1. The missing retrospective and the scope of the question

**Source:** `PURSUING_STACKS_CONTENTS.md`, line 120, §94; no PS page marker supplied. The title continues with “linearization of homotopy types and arbitrary ground-ring extension in homotopy types”. Chapter VI expressly refers back to §94 in `ps_chapters_VI_VII/ps6.tex`, lines 3945–3947, PS p. 521 (`\pspage{521}` at line 3938).

**Use:** The contents establish the existence and advertised subject of a retrospective, not its detailed statements. This is the strongest missing-source lead for the 1976 lecture and bears on **WG2 §2.4 #5**, with **WG H6** relevant only to the broader schematization issue.

### C2. A topos of sheaves on affine schemes appears, but is not identified as the de Rham topos

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 34–47, §110, PS p. 443 (`\pspage{443}` at line 6). Brief quotation: “a semi-simplicial object in the topos ... of all functors from ... algebras to sets” (lines 40–42); the “flat” topology is suggested at lines 42–44.

**Use:** This is a concrete contextual example of a topos serving as an ambient category for schematic models. It does **not** define a “topos de De Rham,” nor does it identify any particular faisceautisation in cote 136. It offers a possible comparison relevant to **WG H6**, not an equation between the constructions.

### C3. Universal polynomial maps and the completion issue

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 370–404, §111, PS pp. 450–451. Page 450 is marked at line 338; page 451 begins within line 389. The map into the divided-power algebra is described as the “universal polynomial map” at lines 379–384. Lines 385–388 explicitly notice that the infinite exponential “doesn't take its values in ... actually, but in a suitable completion”. The completed object is displayed at lines 390–394 as a product of the homogeneous divided-power pieces.

**Use:** This is a precise contextual instance of a universal construction involving divided powers. Its completion proviso should be retained in any comparison. It is not evidence that the lecture's phrase “constructions universelles” refers to this particular PS construction. The algebraic theme bears on **WG2 §2.4 #5**; no additional result ID is justified by the context alone.

### C4. Polynomial cochains are a distinct comparison question

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 927–933, §112, PS p. 461 (`\pspage{461}` at line 890). Brief quotation: “using ... polynomial cochains rather than arbitrary ones” (line 930). The surrounding question concerns the discrete cohomology of the discrete monoid of integral points.

**Use:** This gives a precise cochain-level comparison in the supplied context, but it does not use the phrase “generalized cochains” and does not by itself state the requested integral multiplicative theorem for the lecture's complex. It must be read with the later withdrawal in C5.

### C5. The retracted Γ-linearization expectation is not automatically a retraction of the lecture's de Rham theorem

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 2899–2915, §119, PS pp. 500–501. Page 500 is marked at line 2863; page 501 begins within line 2913. The assumption is specified at lines 2900–2903: the homology of Eilenberg–Mac Lane objects should be computable using derived functors of the divided-power-algebra functor. The text reports that Illusie found it “definitely false” (lines 2904–2905), and that Grothendieck independently convinced himself of failure for the degree-one case (lines 2911–2913).

**Source for the worked example:** the same file, lines 2917–2949, PS p. 501. The discrete second cohomology is compared with central extensions of the additive group scheme; a truncated-power-series group and its polynomial splitting equation are displayed. Lines 2951–2962, PS pp. 501–502 (`\pspage{502}` within line 2955), distinguish polynomials with integral coefficients from rational-coefficient polynomials taking integral values.

**Use:** This is a genuine withdrawal recorded in the supplied PS text. Its target is the specified schematic-versus-discrete Γ-linearization comparison. It must not be silently promoted into a counterexample to a different divided-power de Rham construction in the 1976 pages. It is directly relevant to the interpretation of **WG H6** and, more broadly, **WG2 §2.4 #5**, but neither hunch is settled by a name match.

### C6. PS explicitly separates divided-power de Rham algebra from the proposed binomial approach

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 2975–2998, §119, PS p. 502 (`\pspage{502}` at line 2955). Brief quotation: “linearization of homotopy types via De~Rham complexes with divided powers relies on a ... commutative algebra with divided powers” (lines 2981–2984). The alternative through unipotent bundles is said to “might well rely” on binomial commutative algebra (lines 2985–2989).

**Use:** This passage positively recognizes the de Rham divided-power approach while differentiating it from the new binomial proposal. The conditional language belongs to the source. It supplies a particularly useful qualification to C5 and bears on **WG2 §2.4 #5** and **WG H6** without proving either planning claim.

### C7. Universal operations are discussed through analyzers

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 3131–3197, §120, PS pp. 506–507. The page markers occur at line 3129 and within line 3179. Lines 3138–3154 compare divided-power operations on a suitable ideal, λ-operations, binomial operations, and Adams-type operations. Brief quotation: “the unifying notion here is the notion of an ... analyzer” (lines 3147–3148). The source says that the composition structure satisfies “a bunch of simple axioms I don't feel like writing down here” (lines 3163–3165).

**Use:** This is an explicit contextual lead for a research note on universal algebraic operations, and it marks an unwritten axiomatization. The exact phrase “constructions universelles” is not present in the supplied PS chapters. A comparison to the lecture would be the researcher's comparison, not a link made on these pages. **WG2 §2.4 #5** is the relevant broad planning entry.

### C8. Several approaches to schematization remain in play

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 3227–3239, §121, PS p. 508 (`\pspage{508}` within line 3227). Brief quotation: “many different approaches (for instance via De~Rham complexes with divided powers, or additive small categories with diagonal maps)” (lines 3230–3232).

**Use:** This is a direct contextual link, but the passage asks for the wished-for formal features and a possible axiomatic uniqueness statement. It is not a completed equivalence theorem among the approaches. It bears on **WG H6** and the programmatic part of **WG2 §2.4 #5**.

### C9. A specific base-ring problem for the de Rham approach

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 3945–3980, §124, PS p. 521 (`\pspage{521}` at line 3938). Lines 3965–3974 consider turning a chain complex of modules into a semisimplicial module, forgetting to a semisimplicial set, and applying the divided-power de Rham construction. The objection is explicit: “the result doesn't depend on the ... module structure of the chain complex we start with” (lines 3970–3972). The existence of the corresponding right adjoint is then called doubtful.

**Use:** This is a precise limit on a proposed extension or reconstruction procedure. It does not deny that a complex assigned to an underlying semisimplicial set computes cohomology. It bears on arbitrary ground-ring extension in the missing §94 and on **WG H6**; a manuscript note should identify which construction is actually under comparison.

### C10. Sheaf-level weak equivalences versus taking sections

**Source:** `ps_chapters_VI_VII/ps6.tex`, lines 4730–4783, §127, PS pp. 536–537. Page 536 begins within line 4730; page 537 begins within line 4782. The ambient objects are sheaves on schemes or affine schemes for a suitable topology “such as the fpqc topology” (lines 4731–4733). Lines 4755–4765 warn that a weak equivalence of semisimplicial sheaves need not become a weak equivalence after taking ordinary sections. Brief quotation: “no more-or-less tautological ... sections ... functor” (lines 4763–4764).

**Further source:** lines 4831–4844, PS pp. 537–538 (`\pspage{538}` within line 4834), propose a vanishing condition on higher cohomology of homotopy sheaves, with “Maybe” and “as a consequence, maybe, of some spectral sequence”.

**Use:** These passages give useful contextual distinctions between a sheaf construction, its weak equivalences, and its global sections. They do not supply a definition of the lecture's faisceautisation. They are at most a related method or warning for a topos comparison; no direct settled RESULTS_STATE result is supplied for this de Rham question.

### C11. “Integration” in PS has an explicitly different contextual use from a Stokes pairing

**Source:** `ps_chapters_VI_VII/ps7.tex`, lines 116–144, §134, PS pp. 557–558 (`\pspage{557}` at line 92; page 558 begins within line 144). Lines 133–135 describe a left-derived direct-image operation computable with an integrator. Lines 187–209, PS pp. 558–559 (`\pspage{559}` within line 202), distinguish the standard simplicial integrator from the Kan–Dold–Puppe equivalence before normalization.

**Source:** the same file, lines 588–610, §135, PS pp. 566–567 (`\pspage{566}` at line 561; page 567 begins within line 607). Brief quotation: “homotopy colimits (or ... integration, as I call it)” (lines 593–594). The passage discusses the total category of a fibered category and an adjoint characterization.

**Use:** These are real integration references, but a lexical hit on “integration” does not establish a Stokes theorem or a comparison with integration of differential forms. No “Stokes” occurrence was found in the supplied chapters or contents. No direct RESULTS_STATE ID should be attached merely because both constructions use that word.

## Searched terms with no direct supplied-source answer

Searches covered both complete supplied PS chapter files and the contents, case-insensitively, with line breaks and TeX nonbreaking spaces normalized for phrase checks. Negative findings below are bounded to those supplied files; they are not claims about all of PS, all of cote 136, or the wider archive.

| Requested topic | Result in the supplied PS material | Source limits or nearest related passage |
|---|---|---|
| “topos de De Rham” | No direct occurrence or definition located. | General ambient sheaf topoi appear in §110, p. 443, and §127, pp. 536–538; see C2 and C10. The question itself is in README lines 19–21. |
| “faisceautisation” / “sheafification” | Neither terminology was located. | The sheaf-versus-sections discussion is related but does not identify the 1976 operation. |
| “constructions universelles” / “universal constructions” | Exact phrase absent. | Universal polynomial map in §111, pp. 450–451; analyzer operations in §120, pp. 506–507. |
| “generalized/generalised cochains” | Exact phrase absent. | Polynomial and Hochschild cochains occur in §112, p. 461, and §119, pp. 501–502. |
| Sullivan / minimal models | No occurrence of Sullivan or the phrase “minimal model(s)”. | A generic “minimal stratum” in Chapter VII is not a minimal-model reference. |
| Cartan cochain comparison | No supplied treatment identified. | Cartan hits in `ps6.tex` are Cartan–Serre truncation/tower references (lines 55, 4602, 4655) and “Cartan-type isomorphisms” (line 97). README lines 22–23 list Cartan's *Théories cohomologiques* as a literature lead, not as supplied or verified text. |
| Stokes / differential-form integration | No Stokes occurrence. | “Integration” in §135 explicitly means homotopy colimits; see C11. |
| Abelian varieties | No such named example located. | The only “variety” hits in `ps7.tex` are a compact aspherical variety (line 830) and a topological variety (line 948), not abelian varieties. “Complex of generalised jacobians” is only a Chapter I contents heading at line 23; Chapter I is absent. |
| Fourier transform / Chern classes | No Fourier or Chern occurrence in either supplied chapter or the contents. | The question occurs only in README line 21. This absence cannot decide whether the 1976 scans name such examples. |
| The lecture plan | No independent 1976 plan supplied in the context. | README lines 15–25 state the planners' questions and explicitly call them guesses made before reading the pages. The contents of PS are the plan of a different text. |

## How to use this map in the final research notes

The strongest direct contextual citations are C3, C5–C9. They support comparison of divided-power linearization, universal operations, base-ring changes, and competing schematization approaches. C2, C10, and C11 are useful chiefly to keep distinct constructions from being conflated. The missing §94 and missing earlier cote-136 return must be stated wherever the notes would otherwise imply a completed cross-package check. Any claim that the new scans add to, restate, differ from, or contradict these passages must be supplied by the principal reader's frozen-text analysis; this context-only map intentionally does not manufacture that comparison.
