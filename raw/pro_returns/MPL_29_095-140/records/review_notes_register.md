# Independent review of notes and check register

Reviewed 2026-11-18, approximately 06:30–06:36 UTC, by the local research-support agent. Read the assembled notes and the 56 JSON entries, including witness, body, context, relation, register connection, and check references; inspected all 41 CHECK_EVENTS rows and the note-ID mapping. No image or transcription was opened, and no existing file was edited. This file is the only write made for this review.

## Concrete fixes

### 1. Already communicated; root is correcting these

1. **N039: “different”, not “stronger”.** Its last body sentence still says “under its stronger hypothesis” in the reviewed Markdown/JSON snapshot. Use “under its differently formulated hypothesis”. Keep the exact tested condition **extensions between algebraically closed fields**. The same stale comparative occurs in `notes_local_candidates.json` and twice in `notes_local_support.md` (candidate L04 and the last sentence of P5); synchronize those support records if they are included in the final package. CHECK_EVENTS already states the correct limited conclusion and expressly disclaims an implication between the general conditions.

2. **N038: provisional reference.** “The characteristic-polynomial proof supplied in L02” must point to **N037 / proof P3 in `records/notes_local_support.md`**. L02 is an authoring label, not a final note ID. Similarly, N036/N037/N041's “below” should identify the accompanying support proof P1/P3/P4; N040's “this support record” should become “the accompanying support records”.

3. **CHECK_EVENTS, N004 outcome.** Replace “has prime-to-p order |d|” by **“has order equal to the prime-to-p part of |d|”** for nonzero d. The note body itself already has the correct formulation, and the event correctly keeps the calculation conditional on the exact sequence and degree map.

4. **Refinement-ID mapping.** The reviewed files have `N002.R1`, `N025.R1`, `N027.R1`, `N032.R1`, `N033.R1`, `N036.R1`, `N037.R1`, `N041.R1`, and `N056.R1` in CHECK_EVENTS, but none is defined or aliased in the notes or `note_id_mapping.json`. Some have event rows and some occur only in outcomes. Add the precise refinement map being prepared by root, linking each identifier to its parent note, exact qualified statement, and supporting proof. This is an ID-definition issue, not a discovered mathematical defect in those proofs.

### 2. Remaining source/context and scope adjustments

5. **N041: locality and the geometric-model qualification.** Replace “maps to all the other local objects” by **“maps to X(t) for every t∈U”**, matching the inserted source hypothesis. P4's counterexample to specialization-only gluing is sound within its stated scope; its additional explanation that the inserted condition excludes that example uses **quasi-finite étale neighborhood models in the intended geometric category**. Say this explicitly if explaining that exclusion, and continue to state that sufficiency of the full source insertion was not proved. A fourth body sentence can carry that scope limit without exceeding the sentence allowance.

6. **N019: exactness versus rigidity.** No overclaim is presently required to be removed: the body attributes exactness to the page and retains exactness of F/category closure, while its event rechecks only the qualified rigidity statement N027.R1. To make the limit visible without opening the register, an optional fourth sentence is: **“Only this qualified rigidity ingredient is independently rechecked here.”** Do not relabel proof C as a proof of the full exactness or pro-representability assertion.

7. **N051: exact subsection title.** The modern file's heading at line2781 is **“Le π₁ local le long de deux branches”**, not “Le groupe fondamental local à deux branches”. Its Hua p.106 → scan107 mapping is correct. The other cited headings “La traduction simpliciale” and “Le van Kampen” do exist.

8. **N024 and N042: remove page/agent ambiguity.** In N024, “the contextual dating page125” should read **“archive scan125 (Hua p.124)”**, since Hua p.125 is the supplied scan126. In N042, replace “outside this agent's assigned source-reading subset” by the package-level statement **“scans125 and127 are outside the supplied evidence; scan126 is supplied”**. Explicitly repeat that distinction in N055/N056's related pp.124–126 → scans125–127 references if strict outside-page flags are required. The “parent separately verified” wording in N024 should also become a statement about this run's limited publication-metadata verification.

9. **N053: avoid a necessity claim broader than the checked derivative argument.** The current wording “its usual étale surjectivity requires n invertible” can sound like an if-and-only-if claim about every individual base/site. The recorded root-algebra/derivative argument proves the usual sufficient hypothesis. Safer wording: **“The Kummer sequence is exact on the fppf site for every positive n, and the usual étale Kummer statement applies when n is invertible.”** No new assertion of necessity needs to be added.

## Checks that passed

- **56 notes**, with sequential unique IDs N001–N056; all 56 headings occur in the same order in Markdown, and every JSON body is present verbatim in the Markdown snapshot. No broken local Markdown file link was found.
- **Allowed kinds:** 13 unproved claims, 14 own ideas, 5 self-flagged items, 15 reading questions, 6 unpursued implications, and 3 conjectures. All 14 own ideas have nonempty confidence and reason; both fields are null for the other 42 items.
- **Body length:** all bodies have 1–4 substantive sentences. A naive punctuation count flags N013 because its quoted subsection titles begin “1.” and “2.”; these are not sentence breaks. Section/formula numbers and “alg.” likewise should not trigger a false failure.
- **Counts:** 31 page files and 521 inventory rows. Unique page classifications agree with the notes: 17 text, 4 typed, 7 reused typed, 1 cancelled draft, and 2 covers. The declared scan list has exactly 31 distinct scans and agrees with the inventory.
- **CHECK_EVENTS:** 41 well-formed TSV data rows and 24 distinct statement IDs in the reviewed snapshot; counts include the refinement IDs. Proof labels C1–C6, A/B/C/D1/D2, P1–P5, and R1/R2/R3/R7 resolve to headings in their respective support records. N048's reference to P4 is a cross-reference to the check registered under N041; no new mathematical check of its wording discrepancy is implied or needed.
- **Scope discipline:** the centrality and CRT/gluing counterexamples are explicitly aimed at contextual formulations; the cusp check declares its repaired minimality convention and distinguishes variable S-group maps from the letter's field-group category. The full criterion, full source gluing lemma, source-image continuation, external Lean check, and Nori proofs are not claimed as completed. The outside continuation scans141–143 and the excluded determinant witness scan121 are clearly flagged.

No additional proof or novelty claim is made by this register review. The task was consistency and claim-scope review, not another proof of every supporting argument or an independent re-verification of external publication records.

## Reviewed snapshot identifiers

These hashes identify the snapshot before the root's announced fixes; this review should not be read as reporting those fixes absent from a later version.

| File | SHA-256 |
|---|---|
| `MPL_29_095-140_notes.md` | `3e9f8bb22e88dc1d2983ec88ebd2dadcb1ab7ba3a7c236d56b18ab1fa215b899` |
| `records/research_notes.json` | `2dd173696ac7aec00e558258524a6961b34b932d1d4a2610a74878313a53d30f` |
| `CHECK_EVENTS.tsv` | `7b2748297767791f4c8a01837e9b8f010d3e84c347e3f63ada793a3588f5aac0` |
