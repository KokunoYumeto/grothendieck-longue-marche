# Static deliverable and coverage audit

**Audit scope:** operative `upload/PROMPT(20261121-115654).md`, validation/aggregation/blind-reading/adjudication/freezing/packaging scripts, canonical reviewed reports, page and generated-deliverable text, progress records, saved first/second records, and checkpoint ZIP directory/manifests/receipts. No source or crop image was viewed in this audit. No mathematical check, OCR, TeX compilation, comparison regeneration, canonical edit, TSV edit, freeze, packaging, or upload was performed. The only file written by this audit is this report.

**Snapshot:** 2026-11-21 15:23:45 UTC. Work is still in progress. At assignment, root audits 098, 100, 101 and 102 were unfinished. During this audit, root completed 100 at **2026-11-21 15:17:02 UTC**. The status below therefore distinguishes that update; 098, 101 and 102 remain release gates for the main reader. Figures in this report are snapshot counts, not a claim that the run has been frozen.

## Result

The core structure and original coverage pass: **23 page files and canonical reports; 85 original MIDs in exact source order; all 590 original C/H differences represented exactly once; all 23 frozen first-reading hashes unchanged.** The saved audited-page decisions inspected here preserve both original readings and explicitly adjudicate every token-different box. Checkpoint contents and exclusions pass.

The concrete metadata issues below should be reconciled before the final rebuild and freeze. None requires changing a frozen first/second reading, viewing an image again, or changing the transcription merely to satisfy this static audit.

## Concrete findings

### F01 — Two difference-coverage links still refer to removed substantive rows

After interpreting semicolon-separated `change_place` values as multiple references, exactly two links fail to resolve within their report's `changes` list:

| Report | Difference | Current metadata | Canonical state |
|---|---|---|---|
| `review/149_scan079_reviewed.json` | D0027 | `disposition: substantive`, `change_place: live_index` | `live_index` was deliberately moved to `certainty_resolutions`; M1218 records the resolved first reading. Its entry has both `against_c` and `against_h` false. `progress.log` explicitly records its exclusion from lexical counts. |
| `review/149_scan089_reviewed.json` | D0282 | `change_place: final_underlined_letter` | That substantive row was removed as an underline/font convention difference. M1247 retains the literal O/U uncertainty; no `final_underlined_letter` change remains. |

**Suggested metadata-only correction for D0027:** retain the row and its ID; set `change_place` to null, classify it as `certainty-only resolution`, and state that the index is resolved to 1 in M1218 and `certainty_resolutions/live_index`, agreeing with H and with C's preferred branch. For example:

```json
{
  "diff_id": "D0027",
  "disposition": "certainty-only resolution",
  "change_place": null,
  "reason": "The index is resolved to 1 in M1218 and certainty_resolutions/live_index. H and C's preferred branch agree; no substantive collation row is counted."
}
```

**Suggested metadata-only correction for D0282:** retain the row and its ID; set `change_place` to null and classify the remaining representation difference as conventional, with the unresolved source reading explicitly linked to M1247. For example:

```json
{
  "diff_id": "D0282",
  "disposition": "macro/editorial convention and retained mark",
  "change_place": null,
  "reason": "The source underline and O/U uncertainty remain in M1247. The removed final_underlined_letter row represented the underline/mathcal-O convention rather than a substantive lexical difference; no collation row is counted."
}
```

These are traceability corrections. Do not delete either of the 590 coverage rows and do not reintroduce a convention-only collation row.

### F02 — Scan093's notation table still reports the superseded eta/K doubt

`review/149_scan093_reviewed.json`, `notation_additions[1]`, still contains:

```tex
\mathcal E_{U_{\unsure{\eta|K}}}
```

Its evidence says the nested form differs from the outer K. That entry is propagated to `notation.md` and to the opening notation table in `SP87_C13_149_doubts.md` (the scan093 “small rounded nested index after U” row).

By contrast, the canonical page's composite already reads:

```tex
\mathcal E_K\mathrel{\text{---}}\mathcal E_{U_K}\mathrel{\text{---}}\mathcal E_U
```

The same reviewed report's final blind-adjudication paragraph expressly says the nested index is K and withdraws the earlier eta preference. **Update that current notation entry and its evidence to the recorded final K decision, then regenerate the two derived tables.** Keep the frozen first TSV and its historical reading unchanged. This finding is a comparison of saved textual records, not a new letter-reading decision.

### F03 — Some scan090 doubt-table readings are editorial summaries rather than the canonical source reading

The report and generated doubts file retain these `reading` values:

| Place | Current value | Literal value available in the canonical page |
|---|---|---|
| `090.kappa` | `\kappa_i\text{ preferred, at both occurrences}` | `\unsure{\kappa|k}_i` |
| `090.f_deleted_words` | `désigne ... aussi` | `\deleted{\unsure{désigne|désignons} \unsure{aussi}}` |
| `090.f_deleted_formula` | `lower exists i tel que; upper i in I(k), simeq, colon` | The full cancelled array reproduced below. |

The operative prompt requires the doubts file's readings to be as on the page. Move explanatory wording to `alternatives` or an evidence/note field, and use the literal current TeX as the `reading`. In particular, the dots between désigne and aussi in the current summary are editorial, not present in that canonical phrase.

The exact current cancelled array is:

```tex
\deleted{$\begin{array}[b]{@{}c@{\ }l@{}}
&\inserted{\unsure{i\in I(k)}\,\unsure{\simeq|\sim}:}\\
\exists&i\ \text{\unsure{tel que}}
\end{array}$}
```

Related nonlexical entries such as scan096's `formula_attachment` and scan097's `pale_traces_before_definissant` are clearly explanations of placement/nontextual uncertainty rather than omitted lexical readings. Their presence accounts for the mismatch between the number of inline doubt wrappers and the number of unresolved rows on those pages; that mismatch is **not** a missing-text finding.

### F04 — README's opening cote label conflicts with the operative prompt and canonical identifiers

`README.txt` begins:

> SP87 / cote 13, file 149 — diplomatic transcription and audit

The operative prompt repeatedly identifies **cote 149**; the combined transcription has `\cotefile{149}`, the collation has `folder=149`, and the decisions have `cote=149`. The filename prefix `SP87_C13_149` should remain as requested, but the README title should identify the work consistently, for example:

> SP87 / cote 149 — diplomatic transcription and audit

No interpretation of the filename component C13 is needed to correct this contradictory prose label.

### F05 — Provisional prose still promises work that must be completed before release

The following were still present when inspected:

- `review/feedback.md` and the derived sheet-feedback file: “The final second-reading comparison will be added after the full first reading.”
- `review/legibility.md` and the derived doubts file: “reviewed so far” and “This note will be completed after the remaining leaves and the independent second reading.”
- `review/notation_comparison.md`, under “Final dispositions”: “To be completed after the blind comparisons,” plus pre-audit descriptions of unresolved cross-leaf decisions.

Root advised that reader C is already preparing feedback/legibility/notes cleanup. This report makes **no duplicate edits**. The final rebuild should consume those completed sources, and the notation-comparison register should record the actual final dispositions rather than leave the future-work placeholder.

## Checks passed

### Deliverables, scan and source coverage

- `pages/` and `review/*_reviewed.json` each contain precisely scans **079–098 and 100–102**, 23 in total. Scan099 is absent from the supplied set and is not reconstructed; the generated notes state this explicitly.
- The combined transcription has no preamble or document wrapper and matches the canonical page files under the aggregation convention. The required one-per-page scan markers and TeX brace checks pass.
- Changes and notes have one scan section for each of the 23 supplied leaves.
- The consolidated transcription, changes log, collation, decisions, doubts/notation/abbreviations, inventory, notes, `CHECK_EVENTS.tsv`, hand log, sheet feedback, progress log, and per-page first/box/second records exist where expected, except the still-running scan101 second reading at the initial audit snapshot.
- Source `MARKS.tsv` contains **85 unique IDs, M1216–M1300**. Canonical mark lists total 85; `decisions.tsv` has exactly the same IDs in exactly the original order. At the inspected snapshot: 38 `first`, 8 `other`, 39 `undecided`. Every resolved mark has an existing crop; no resolved reading still contains an unresolved wrapper.
- The source differences file has **590 rows**. Canonical `diff_coverage` contains exactly **D0001–D0590**, each once. Every per-page packet row agrees with the corresponding original source row. The two stale link/classification issues are F01, not missing differences.
- All required TSV/CSV column names match the operative prompt. Collation page mapping is consistently `their_page = our_scan - 1`, with `folder=149`.
- Every inventory record is nonempty, has `transcribed=yes`, and uses an allowed element/sheet kind. All 23 scans are represented. The current count after the 100 rebuild was **316** elements, all `sheet_kind=text`; hand values describe author/main and separate foliation hands.
- All crop paths referenced by changes, original mark decisions, completed adjudications, and generated textual crop references exist. Reported crop boxes are within the associated source dimensions; the validator also checks anonymous box bounds.

### Immutable readings and explicit adjudications

- All **23** `_first.tsv` hashes still equal `review/blind_stage_start_hashes.json`.
- All available comparison-hash records match the current first and second TSV bytes. The comparison script refuses to replace a saved comparison and verifies the first-stage baseline before comparing.
- All 23 blind assignments name a reader different from that leaf's first reader. The assignment log starts only after all 23 first-stage pages were committed.
- The anonymous box lists contain **466 boxes** across the 23 leaves. Available second readings preserve their box IDs and order.
- At the first audit snapshot, scans079–097 comprised **19 completed root audits**, with **264 differing boxes** and **96 changed boxes**. Each differing box had an explicit JSON decision and an adjudication TSV row, in comparison order, with the frozen first and second strings unchanged, a nonempty final reading, evidence and an existing crop.
- Scan100 then completed with **15 boxes, 10 differences, 5 changed**, bringing completed root audits to **20**, differing boxes to **274**, and changed boxes to **101**. Counts recorded in audited progress lines agree with their saved records. No `changed=yes` row falsely repeats its unchanged frozen first string.
- Pending at the end of this static inspection: **098** (32 boxes; second/comparison saved, 25 differences), **101** (18 boxes; blind return/root audit still pending at the checked snapshot), **102** (24 boxes; second/comparison saved, 15 differences). These are expected work in progress, not claimed release passes.

### Generated counts and structural validation

- A read-only run of `python scripts/validate_work.py` returned `pages: 23`, `marks: 85`, `errors: []` in partial mode. Final mode was not represented as passing while root audits remained unfinished.
- After the scan100 rebuild, canonical reports and the generated changes total agreed: **511 rows; 133 against C; 466 against H; 352 high, 108 medium, 51 low**. The changes log explicitly defines these as places, not changed tokens. Earlier 509-row totals seen during the live audit predated the scan100 update and were not treated as a stale-output defect.
- `CHECK_EVENTS.tsv` has **31 events** with nonempty required fields and only permitted event types: 18 targeted proof checks, 3 used-and-rechecked events, 10 carried-as-background events. This audit checks their schema and preservation only; it does not check or endorse their mathematics. The two entries in `root_pending_check_events.json` are already present in the event TSV, so that filename does not indicate omitted check events.
- Grouped unresolved rows account for multiple inline doubts; a mechanical one-wrapper/one-row equality is not required. The concrete literal-reading issue found is F03.

### Checkpoints and packaging exclusions

| Checkpoint | Files | Page files | Crops | Archive bytes |
|---|---:|---:|---:|---:|
| 01 | 347 | 11 | 246 | 73,390,032 |
| 02 | 580 | 19 | 411 | 126,968,018 |
| 03 | 843 | 23 | 597 | 191,732,962 |
| 04 | 1,207 | 23 | 859 | 279,370,214 |

- Each archive has all core deliverables written by that time, including `CHECK_EVENTS.tsv`, work scripts and crop evidence.
- No checkpoint contains source attachments, original scan/witness directories, generated witness packets (`input.json`), halves, bytecode, or an earlier ZIP.
- The archived manifest path set exactly matches each archive's entries apart from the manifest itself. Each ZIP's current SHA-256 matches its saved packaging receipt.
- Each later checkpoint is a superset of the earlier checkpoints' file paths. Every path archived in any checkpoint still exists in the current work tree, so final packaging can remain cumulative.
- Durable-save receipts exist for all four checkpoints. Their logged packaging times are respectively 20, 24, 2 and 28 seconds after the corresponding 45-minute boundary from the initial UTC timestamp; no extra checkpoint is recorded.
- `package_work.py` refuses overwrite, uses exclusive ZIP creation, snapshots bytes before writing its manifest, and excludes the forbidden path categories. It packages crops and documentation. No packaging command was run by this audit.

### No compilation/OCR evidence and release gates

- Saved work scripts contain no invocation/import of Tesseract, EasyOCR, PaddleOCR, OCR libraries, PDF text extraction, `pdflatex`, `xelatex`, `lualatex`, or `latexmk`; no subprocess/system wrapper was found in the inspected script set. The README and reading notes expressly record no compilation/OCR. This is a static check of saved evidence, not a reconstruction of every tool invocation in the session.
- `freeze_transcription.py` requires all 23 audited progress records, writes hashes for the 23 page files and combined transcription, refuses a second freeze, and has an explicit verification mode that logs unchanged hashes.
- The freeze record and final ZIP were absent at the checked snapshot, as expected during the remaining root audits. The packaging helper checks for a freeze log entry; it does not itself invoke final validation or hash verification. The main reader must therefore complete the final rebuild/validation, freeze and unchanged-hash verification before final packaging.
- Once the remaining audits and metadata cleanup are complete, run the required final structural gate and freeze verification, then make the final cumulative ZIP. Do not replace any frozen first/second TSV, prior checkpoint or comparison record in order to reconcile metadata.


## Independent review of the proposed documentation cleanup

**Reviewed 2026-11-21 15:32:39 UTC by reader B.** This is an appended review of `scripts/propose_documentation_cleanup.py` and `review/documentation_consistency_findings.md`, as requested by root. No cleanup script was executed or imported. Its literal `PATCHES` data were extracted by Python AST and its preconditions were independently evaluated on in-memory copies. Only this audit report was appended.

**Conclusion: the guarded metadata-only proposal is sound; no blocking discrepancy was found.** Every non-hand replacement was compared with its cited completed adjudication's final reading/evidence and current canonical metadata. All 72 hand-label changes were checked as a group against their existing attributions and the deliberately untouched numeral-hand entries. The separate root-only scan090 literal Reading replacements in the findings document agree with the current canonical page and preserve the two-level cancelled array.

The reviewed versions are bound by these SHA-256 values:

- `scripts/propose_documentation_cleanup.py`: `c4d666fa2e1e2ee9dbb86250eda01e39ec762ef9533f251c60552ec63da283ed`
- `review/documentation_consistency_findings.md`: `842cc6f332dac783b2554b1cfa88ef07b74e4e870cf8aac8095b365754d30eba`

### Scope and exact guards verified

The proposal contains **178 patches across scans079–095**:

| Permitted field | Patches | Actual leaf fields |
|---|---:|---|
| `notes` | 48 | Exact, unique substring replacements |
| `inventory` | 110 | 34 `first_words_or_objects`, 4 `position`, 72 `hand` |
| `hand_observations` | 17 | 3 `habit`, 8 `evidence`, 6 `witness_errors` |
| `notation_additions` | 3 | Scan093 `written`, `transcription`, `evidence` |

- All **48 `replace_once`** preconditions occur exactly once at the proposed target, after prior patches to the same in-memory record. There are no regex replacements or unbounded global replacements.
- All **130 `set`** preconditions match their complete existing values exactly.
- Every target falls within scans079–095 and the four allowed fields. The independent in-memory simulation found **no changed protected field** and no schema-key change. In particular, `changes`, `marks`, `unresolved`, `check_events`, `diff_coverage`, `second_boxes`, scan IDs and line counts remain unchanged.
- The script defaults to validation/printing without writing. `--apply` is explicit. It validates the full patch list and protected-field invariants before the first write, then replaces each JSON atomically.
- No target touches page text, witnesses, first/second TSVs, box coordinates, comparisons, adjudications, generated global files, progress records, hashes or archives. The proposal does not run aggregation.

### Final-reading agreement verified

The reviewed replacements correctly follow the saved final decisions, including the 080 arrow/shaft distinctions and live stop after cancelled car; the 082 cancelled-label and G_m doubts; the 086 K/equals/colon distinctions; the 087 separate marginal cancellation states and old/replacement-symbol doubts; the 088 four headless diagram links while retaining the separately headed prose map; the 089 overwritten-digit order and verb-ending doubts; the 090 resolved K forms and cancelled alors alternatives; the 091 literal short forms and recovered cancelled letters; the 092 tentative Gal/replacement-E layers; the 093 K, inverse, Ainsi/Aussi alternatives and broken-word accent uncertainty; and the 094–095 final word, punctuation, index and cancellation alternatives. These are agreements between saved textual records, not new image judgments.

The proposal also fixes the stale scan093 notation entry identified as F02 above. It leaves the root-only F01 coverage metadata, F03 `unresolved` Reading values, README label, and global feedback/legibility/notation promotion outside the script, as documented. It does not imply those separate release tasks are already complete.

The hand-label normalizations use existing main-manuscript attributions; they do not recast an unresolved numeral hand as authorial. The specifically flagged 079 upper number, 087 upper/lower numbers, 090 lower folio and 093 upper/lower numbers remain outside the automated attribution changes. This matches the findings document's stated limitation.

### Application sequencing and current status

The script's exact-precondition checks are performed when it loads each record; it then writes full JSON records with protected values preserved from that snapshot. **Apply it serially while no other process is changing reports079–095.** This is the ordinary sequencing condition for its read/modify/write design, not a blocking defect or a request for another approval. If canonical text drifts before application, its preconditions should stop the batch; review the changed precondition rather than weakening it. Per-file writes are atomic; the multi-file batch is not a transaction.

Root reports that **098 and100 are now audited** (098 was recorded at **2026-11-21 15:23:12 UTC**, 100 at **15:17:02 UTC**). Root is auditing102 and waiting for101. This status supersedes the earlier snapshot's pending-098 line. No final freeze, final packaging, image reading or mathematical check was undertaken by this review.


## Final evidence-integrity gate — 2026-11-21 15:37:47 UTC

**Status: PASS.** All **23** root audits are now complete, including 102 at 2026-11-21 15:29:29 UTC and 101 at 2026-11-21 15:33:11 UTC. This final evidence check supersedes all earlier pending-audit statuses in this historical report. The machine-readable record is `review/final_evidence_integrity.json`.

- **23/23 first readings** still match the blind-stage baseline and their comparison records; **23/23 second readings** match their comparison records.
- Every saved comparison was independently reconstructed in memory from the immutable readings using the recorded token rule and deterministic edit algorithm. **23/23 comparison files match both their reconstructed rows and SHA-256 of the deterministic TSV bytes.** No comparison file was rewritten.
- All **466 boxes** have ordered first/second readings. All **328 token-different boxes** have explicit decisions and adjudication rows preserving both frozen readings, final text, evidence, crop path and changed flag. **122 boxes changed** a reading or doubt state; **206 differing boxes** retained the final first reading/state. All progress counts agree.
- All **590 original difference rows** and **85 original MIDs** retain their established page mapping and source order. All substantive `change_place` references resolve after the F01 corrections; D0027 and D0282 are retained with their correct non-substantive/mark handling. Of the 590 rows, 467 name a total of 513 valid change-place references, while 123 have an explicit non-substantive or mark-only disposition without such a link.
- All **23 blind readers differ from their leaf's first reader**; assignment, comparison and audit timestamps have the required order after the full first stage.
- F01, F02, F03 and F04 are now resolved in the canonical metadata/README: obsolete links repaired, scan093 notation aligned to K, scan090 Reading summaries replaced with literal TeX, and cote 149 correctly identified. C's reviewed metadata cleanup has been applied. Root/A own the remaining final prose reconciliation and generated-deliverable rebuild.

No source/image reading, mathematical check, broad optional test, aggregation, freeze, packaging or upload occurred in this gate. Only the integrity JSON and this appended status were written. Error count: **0**.
