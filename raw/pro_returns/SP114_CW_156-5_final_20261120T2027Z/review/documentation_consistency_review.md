# Documentation consistency review

Reviewed 2026-11-20 at approximately 19:49 UTC, while the main reader was still auditing scans 026–031. This is a read-only review of documentation and recorded decisions, not another reading of the manuscript images. No transcription, sealed reading, adjudicated record, or script was modified. The only file written by this reviewer is this report. Findings below describe the files at that time and are recommendations to the main reader; later corrections may supersede them.

## 1. Hand-log assembly loses fields present in the records

**Action needed before final assembly.** `scripts/metadata.py`, lines 25–28, accepts only a subset of the field names actually present in `hand_habits`. Consequently the generated hand log drops available evidence or witness effects, and scan030 has blank habit descriptions.

| Record | Actual populated keys not consumed | Result in generated hand log | Recommended mapping |
| --- | --- | --- | --- |
| `scan027_adjudicated.json` | `places`, `holds_at_every_occurrence`, `misreadings`, `evidence_crop` | Anchor and witness-effect cells are empty; scope becomes “Not asserted”. | Include `places` and `evidence_crop` in anchors; recognize `holds_at_every_occurrence` as coverage and `misreadings` as witness effects. |
| `scan028_adjudicated.json` | `occurrences`, `consistency`, `affected_witnesses` | Scope becomes “Not asserted”; witness effects are empty. | Include `occurrences` with existing evidence; recognize `consistency` as coverage and `affected_witnesses` as witness effects. |
| `scan030_adjudicated.json` | `observation` | All eight habit-description cells are blank. | Accept `observation` after `habit`/`form`. Do not invent universal scope or witness effects absent from this record. |
| `scan032_adjudicated.json` | `observed`, `misread` | Anchor and witness-effect cells are empty. | Accept `observed` as anchor evidence and `misread` as witness effects. |

The existing schemas for026,029,031 and033 are already handled. A robust adapter should preserve all supplied anchor information rather than choose only one of `evidence`, `occurrences`, `places`, and `evidence_crop`. Paths beginning `deliverable/` in reader metadata may be normalized to package-relative paths for the generated hand log. This is a serialization correction, requiring no new image decision.

## 2. Inventories need the recorded blind corrections

The inventory is generated directly from each record's `inventory` array by `assemble.py`. Therefore editing only the generated CSV would be lost on the next assembly. Array indices below are zero-based.

### Scan032

- `inventory[3]`, “raised glyph after strate”: current `\\unsure{$G$|$\\in$}` omits the new `e` alternative in the page. Update to the final local reading from the audited page.
- `inventory[4]`, “old On”: current `On` should carry the audited `On|les|le` uncertainty if the inventory quotes the reading.
- `inventory[8]`, “Corollary heading”: its short first-words field is not formally false, but the restored `\\unsure{pr.|pro.}` before *propriétés* should be visible in that text-element description or a separate local text row. It is a baseline short start, so do not automatically label it an insertion.
- **Missing element:** the separate raised `\\inserted{\\unsure{a)}}` above the end of *application*, restored by032-BL03, has no inventory row. Add an insertion row with the recorded position and uncertainty. This is a distinct element from the original a) beginning the preceding cancelled item.
- `inventory[26]`, “new c formulation”: current text says `... est une strate ouverte`; replace its quote with `... est une \\unsure{str.te|strate|str.} ouverte` in accord with032-BL04.
- `inventory[16]` and `[18]`, long oblique note and curve: both elements are present. Their descriptions should explicitly retain “preferred live; whole-note cancellation alternative” if the state is summarized. No new inventory element is required merely to duplicate the alternative state.

### Scan033

- **Missing element:** the restored live implication arrow before1°),033-BL01, is absent from the inventory. Add a local text/display element or explicitly incorporate `$\\Rightarrow$` into the opening text element; do not leave it represented only by the changes log.
- `inventory[7]`, “cancelled first On a”: update the quote to the new doubtful state `\\unsure{On a}`.
- `inventory[8]`, “bracketed underlined formulas”: the quote still has the earlier two-option relation, definite cancellation of both raised marks, and a supplied closing parenthesis at the clipped edge. Copy the audited formula excerpt, including the live-phi/q state alternatives and the clipped right end.
- `inventory[9]` and `[10]`, “first/second cancelled elevated mark”: their names assert cancellation although the new transcription explicitly allows live phi/q. Prefer neutral names such as “first/second overwritten elevated mark”; keep the recorded preferred cancellation and explicit alternative in the quote. The inventory kind can remain the preferred state if its uncertainty is explicit.
- `inventory[24]`, “underlined strate phrase”: the quoted `strate ouverte \\deleted{dans \\unsure{la}} de ...` is obsolete. Replace by `\\unsure{str.$^{t}$-ouvert|str.t-ouvert|strate ouverte} pour \\deleted{$\\unsure{F|A|la}$} $F'$` and use a neutral element name such as “underlined abbreviated phrase”.
- `inventory[25]`, “inner dans la cancellation”: obsolete name and quote. Use “hatched residue after pour” and `\\unsure{F|A|la}`, preserving the cancellation state.
- `inventory[29]`, “cancelled Posons”: use the audited uncertainty, `\\unsure{Posons}`.

Also consider changing the type of `inventory[17]`, “bien state”, from an unqualified deletion description to a label that reflects the preferred underlining and its deletion alternative. The current `first_words_or_objects` already preserves both states, so this is descriptive clarity rather than a missing element.

## 3. Stale scan033 metadata

These fields are current descriptive metadata, unlike the sealed first-reading fields, and should agree with the audited page.

| Location | Current wording | Proposed factual replacement |
| --- | --- | --- |
| `scan033_adjudicated.json`, `notation[5]`, approximately lines1867–1871 | `I^{\\unsure{\\ast|k|+}}`; “preferred ast used unmarked on I′”; “mark at first occurrence only” | The same `\\unsure{\\ast|k|+|\\leftarrow}` is marked on both I and I′. Character remains unresolved; star is preferred. |
| `hand_habits[3]`, approximately line1825 | “C ambiguity retained, marked only at first occurrence.” | “The repeated glyph is marked doubtful at both occurrences; blind comparison adds an arrow-like alternative without changing the preferred star.” |
| `hand_habits[2].evidence`, approximately line1817 | “long strate underline” | “the underline beneath the abbreviated str.t-ouvert-like phrase”. |
| `notes[5]`, approximately line1926 | “both retain star/k/plus doubt” | “both retain star/k/plus/left-arrow doubt.” |
| `changes` row033-38 evidence, approximately line1332 | “same star/k/plus ambiguity” | Include the added left-arrow alternative, or say “same explicitly recorded alternatives”. |

`unresolved[10]` (“bottom, repeated I superscript”) and `unresolved[15]` (“bottom, repeated superscript on I and I′”) describe the same two occurrences with the same preferred reading, alternatives and reason. Merge these into one doubt-table row, retaining the crop pointer from the latter. This duplication affects the doubt list, not the substantive-change totals.

The old evidence texts in033-25 and033-26 remain first-pass descriptions contradicted by the final phrase. They are safely excluded from the current substantive rows by `review_only`, false witness flags, and `merged_into: 033-27`; their `second_evidence` explicitly records supersession. They can remain as historical records. Similarly, `C_state_audit`, `difference_coverage` history, `second_boxes`, and all sealed `_first.tsv` content must not be rewritten to hide the earlier reading. In particular, the old formula wording in a sealed first-reading record is expected and is not a documentation error.

## 4. Cross-page documents need a short blind-audit supplement

### `notation_working.md`

- Line20 still says the exact scan026 adverb endings “are still being adjudicated”. Once026 is complete, replace this with the final recorded uncertainty and baseline/raised-ending distinction; do not decide it from this review.
- Line34 calls the upper033 raised marks “cancelled” without their now-explicit live-phi/q alternative. Prefer “overwritten raised marks with unresolved character and deletion state”.
- Line35 lists only k/plus alternatives for repeated I superscripts. Add `\\leftarrow`.
- Line36 can be extended with032 `pr./pro.` and `str.te/strate/str.`, and033 `str.$^{t}$-ouvert/str.t-ouvert/strate ouverte`. Keep the distinction between a doubtful short start and a confirmed abbreviation; do not expand either in the transcription.
- Line37 should explicitly state that032's oblique note has a whole-note cancellation alternative in the transcription. Its present statement of functional doubt is true but incomplete.
- Line39 describes only first-pass reconciliation. Replace after all audits with wording that the table incorporates main-reader adjudication of the independent blind differences, while retaining each local exception.

### `review/hand_synthesis.md`

- Line5's scope paragraph can be brought up to date: the final synthesis covers026–033 and incorporates the recorded blind adjudications, without being an additional image pass.
- Line20 still says the026 marginal order sign is doubtful. Reconcile with the final026 audit once applied. The reviewer has made no image decision about it.
- Line31's abbreviation examples should include the new032/033 forms, with explicit uncertainty.
- Line32 should say the032 whole-note cancellation alternative is now encoded, not merely “without silently cancelling the note”.
- Line58 needs the added left-arrow alternative for the two I superscripts and neutral state wording for the upper overwritten marks.
- The033 supplement lacks the restored initial arrow and changed abbreviated phrase. Suggested addition: “The blind audit restored a live implication arrow before1°). In the cancelled lower argument, the preferred structure is *est un* followed by a doubtful str.t-ouvert-like short form and *pour*; the earlier expanded *strate ouverte … de* reading was withdrawn. The exact short form and the hatched residue remain unresolved.”

### `review/legibility.md`

- Line3 currently describes033 as a later first-adjudication addendum. Update the scope once all blind audits are complete.
- Line14 should include the abbreviated lower phrase and hatched residue among033's remaining limits, and mention that the upper formula is clipped at the source edge. The paragraph otherwise remains compatible with the current record.
- The relative-witness paragraph gives local examples and expressly avoids an accuracy ranking. That framing is appropriate. If desired, replace “H is nevertheless useful independent evidence” with “H remains a useful comparison witness” to make the distinction from image authority explicit.

Generated `SP114_CW_156-5_doubts.md`, `_notes.md`, and `_hand_log.md` should be rebuilt after their input records and synthesis documents are reconciled; editing only generated output is insufficient.

## 5. Counts and script semantics checked

At this review snapshot, the record-derived totals are295 substantive loci,54 against C,281 against H,202 high-confidence,39 medium-confidence,54 low-confidence, and46 certainty decisions. The changes summary and error-sheet summary match these values, and the collation has281 data rows. These are interim counts and will change as026–031 are audited.

- All eight adjudicated records have unique change IDs.
- No `review_only` row currently retains a true witness-difference flag or `certainty_only` flag. Thus the current filtering correctly excludes them even though it does not explicitly test `review_only`.
- Merged033-25 and033-26 are correctly counted only through033-27. Their historical presence is not double-counting.
- `assemble.py` and `sheet_feedback.py` use the same substantive filter: not certainty-only and differing from at least one witness. Macro-only agreements are therefore excluded if their record flags are correct.
- `assemble.py` includes every recorded blind adjudication in the second-reading section, while keeping substantive totals based on primary change loci. This is consistent with the distinction between differing boxes and changed physical places.
- The README accurately distinguishes current deliverables from historical reader drafts, explains the source-path convention, and makes `progress.log` authoritative for completion and freezing. No immediate README blocker was found.
- Do not use this review as evidence that the remaining blind image audits are complete. It did not run a TeX engine, inspect manuscript pixels, or alter any reading.

## Suggested order of completion

Finish the image decisions; synchronize inventory and descriptive record fields; fix the hand-log schema adapter; reconcile the three cross-page documents; rebuild assembly, metadata and feedback; run the established structural validator; then freeze and verify transcription hashes. All historical and sealed reading evidence should remain unchanged.

## Follow-up implementation

At the main reader’s request, the current metadata was reconciled after this review. The hand-log schema adapter now preserves the actual reader-return fields. Scan032 has38 inventory elements; scan033 has33, including the newly restored raised label and implication arrow. The033 repeated-superscript duplicate was merged, leaving21 unresolved entries. Current033 notation and note wording now give the same four alternatives at both occurrences. The notation, hand-synthesis and legibility documents incorporate the completed032–033 blind decisions. Metadata output was regenerated; the transcription assembler was deliberately not run while the main reader continued other audits.

A before/after SHA-256 assertion confirmed that this metadata edit left all eight page files and every sealed first-reading and box TSV unchanged. Historical findings, comparisons and audit decisions were not edited. The current record edits were confined to inventory, unresolved, hand_habits, and the explicitly authorized current033 notation/notes fields.

The independent lossless PNG recompression operation is documented separately by `lossless_png_recompression_01.json`. It changes PNG encoding only after raw-pixel, mode and size verification, retains all non-IDAT chunks byte for byte, and does not touch source scans or checkpoint archives.

## Further reconciliation after026–028 audits

At the main reader’s request, current026–028 inventories, notation and hand observations were synchronized with their completed blind decisions. The026 inventory’s nonstandard kinds were mapped to the required categories; the more detailed element names and historical reader records remain. The028 inventory’s original kinds were retained in reader_kind while its primary kind was normalized. The028 coproduct inventory quote now preserves the audited doubtful bar/intersection structure instead of giving an unqualified normalized intersection. No page text, sealed TSV, primary change row or audit decision was altered. Current027 notes were reconciled with preferred C1/C5/C4 and C2_0/8_0/phi_0, preserving the distinct unchanged prose reference to C5.

The compression run completed with561 PNGs verified,487 smaller encodings adopted, and33,532,926 bytes saved (6.238%). Crops occupy503,997,380 bytes (480.649MiB). The complete deliverable tree measured485.334MiB immediately after verification, before subsequent text-only metadata additions. No crop filename was removed; all non-IDAT chunks and decoded pixels were preserved.

##029 synchronization and assembler schema inspection

The029 current metadata was reconciled with its completed audit: doubtful cancelled Alors, preferred l’apparente, cancelled quand/inter./intersection, the low L comma/subscript1/no-mark alternatives, and exclusion of the probable surface patch before l’appelle. The inter. abbreviation entry now identifies an alternative only. The removed surface mark was not restored to the inventory. Inventory kinds on029 and030 were normalized with original descriptors preserved in reader_kind;031 already used the required kinds. No primary page or blind/adjudication decision was altered.

A schema inspection found six032 H omission entries stored as JSON null (032-01,032-27,032-43,032-52,032-56,032-57). The current assembler prints None in the Markdown witness column and an empty field in the TSV. Rendering those values as (omitted) would communicate their already-recorded omission meaning consistently without changing any reading. This was reported to the main reader; the assembler was not edited or executed.

The independent-reading table serializes box, first, second and the composite decision string. That string preserves final reading, evidence, crop, source coordinates and inspection UTC, but does not explicitly export the separate confidence field. An explicit confidence column or appended confidence label would preserve that field in the human-readable table. The field remains available in the saved adjudication JSON.

Other requested output fields use consistent schemas across the inspected records: C/final/evidence/place/kind/confidence are strings; witness flags and H_marked are booleans; notes and abbreviation dictionaries are preserved by generic serialization; the check-event fields have consistent names. Smaller locus boxes and rotation data remain in review records rather than the main evidence table, whose required source box is preserved. Current notation is intentionally assembled from the shared maintained table. Historical C-state/doubt audits and first-reader hypotheses remain in review records and should not be dumped into current notes without distinguishing their historical status.

The remaining blank scope/witness-effect cells in the eight030 hand-habit rows reflect missing source fields, not an adapter failure: each row originally contained only observation and evidence. Those fields can be supplemented from the completed030 adjudication when available. The adapter now correctly exports every available observation.


## Final resolved status —2026-11-20, after all eight blind audits

This section supersedes the interim status statements above; the earlier review findings remain as history. All eight blind audits026–033 are complete. The current records contain300 substantive comparison loci,224 precommitted boxes,196 boxes with raw token differences, and71 changed physical loci. These measures have different purposes and are not interchangeable. No substantive flag or primary audit decision was changed by this metadata reconciliation.

The two reported assembler defects have been fixed in `scripts/assemble.py`: explicit JSON null witness values render as `(omitted)` in Markdown and TSV, and the independent-audit table includes its confidence column. The hand-log schema adapter in `scripts/metadata.py` exports all recorded observation, evidence, scope and witness-effect variants. All eight030 habit records now contain explicit local scope and witness effects. The former statement that the assembler had not been edited describes the earlier inspection only. The assembler has not been executed by this metadata reviewer; the main reader owns final assembly and validation.

Current030 inventory, notes, notation and abbreviation descriptions now follow the completed audit: cancelled bien/i.e., the headless gloss leader, the doubtful rotated relation, preferred C-subscript3/Cor./C6. label, the underlined Cor. stop, absent separate stop after C7₀, and the hatched old construction with F-minus-G/F-dot-G/F-times-G and2/question-mark alternatives. The le/les doubt is explicit, and local phi observations are not promoted to a universal rule. Abbreviation expansions are metadata only.

Current031 notation and hand summaries preserve standalone equals/superset-with-bar doubt, preferred cancelled superset/equals, the clear b-heading equality, all four élément-form alternatives, resolved lui, the absent opening parenthesis, the placement of the lower additions, and the script-R/Q/O adjective alternatives. The duplicate inventory descriptions031-S16/031-BL-I02 were consolidated into one physical margin-note element with both original IDs and explicit inserted/cancelled states. Historical findings and all primary decisions remain intact.

The shared notation table, hand synthesis and legibility note now describe all eight completed audits. README provenance distinguishes blind-difference counts from physical and substantive loci, records preservation of the earlier and fresh030/031 crops, and explains lossless recompression and seal verification. The24 pre-audit seal entries were verified:16 immutable first/box TSVs directly and8 original page hashes from historical bytes or exact reversible recorded edits in memory. All617 checkpoint02 paths and274 checkpoint01 paths remain in the deliverable. The compression report verifies all561 crop filenames and unchanged pixels; saved crops total503,997,380 bytes. No historical checkpoint archive was altered.

No metadata blocker remains for the main reader's final assembly, structural validation, freeze and packaging. This review did not reopen manuscript images, perform OCR, consult external research or run a TeX engine. The source pages, sealed first/box files and final blind TSVs were hash-checked as unchanged during the030/031 metadata edits.

Final main-reader reporting cleanup: the consequential-correction summary now quotes each row’s specific ink evidence when no separate consequence field exists, instead of repeating a procedural adjudication label. The generic manuscript-number exception was removed from unrelated scan026 decision labels; the actual manuscript-number row already cites its inspected saved crop. No reading, flag, count, page, or sealed TSV changed.
