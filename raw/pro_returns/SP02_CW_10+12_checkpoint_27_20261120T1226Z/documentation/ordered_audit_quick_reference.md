# Ordered audit and final delivery: root command guide

This guide describes existing mechanical interfaces. Root supplies every image observation, reading, correction, inventory decision, notation judgment, and research conclusion. Examples contain placeholders, not completed observations.

Run commands from `/workspace/scratch/57a811ad3c84/SP02_CW_10+12` with `PYTHONDONTWRITEBYTECODE=1`. The existing witness-root defaults are used for page-map metadata. No command in this guide opens sealed context automatically.

## One ordered second reading

1. Begin the next page in page-map order:

   ```bash
   python scripts/record_audit.py --begin EXACT_PAGE_KEY
   ```

   Save the returned `audit_id` and `baseline_page_sha256`. The returned `existing_loci` entries contain stable locus IDs and **zero-based** indices. All 106 first-pass pages must already exist. Earlier pages must have completed audits; only one audit can be active. Repeated audits of earlier pages are supported.

2. Root personally views the whole scan and the actual two halves, records unusual words, accents, and other image-first observations **before reopening the finalized page text**, and writes an observation JSON:

   ```json
   {
     "page_key": "EXACT_PAGE_KEY",
     "audit_id": "EXACT_RETURNED_AUDIT_ID",
     "baseline_page_sha256": "EXACT_RETURNED_SHA256",
     "viewed": {"whole": true, "half_a": true, "half_b": true},
     "observations": {
       "unusual_words": [],
       "accents": [],
       "other": "Root-authored observations, or an explicit statement that none were noted."
     }
   }
   ```

   Declare each view only after actually making it. The observations field may be a nonempty string, list, or object. Commit it:

   ```bash
   python scripts/record_audit_image_first.py --record ../work/IMAGE_FIRST.json
   ```

   This writes an immutable `documentation/audit_image_first/AUDIT_ID/image_first.json` using actual UTC. Do not supply timestamps. A retry with identical declarations preserves the original timestamp; changed declarations cannot overwrite it.

3. Immediately before reopening the finalized/consolidated page text:

   ```bash
   python scripts/record_audit_image_first.py --mark-text-open EXACT_PAGE_KEY
   ```

   This publishes `receipt.json` with actual text-opening UTC and the exact first-observation hash. It neither opens text nor completes the audit. The required order is audit start ≤ image observation < text opening < audit completion. Audit completion is stored to whole-second precision; a same-second completion that cannot prove this strict order will be rejected by receipt validation. Preserve actual times.

4. Root compares text against the images and supplies an audit JSON. Its required fields are:

   ```json
   {
     "audit_id": "EXACT_RETURNED_AUDIT_ID",
     "baseline_page_sha256": "EXACT_RETURNED_SHA256",
     "audit_reading_complete": true,
     "audit_inventory_confirmed": true
   }
   ```

   Optional identity fields are `key`, `folder`, `cote`, and `scan` and cannot change identity. **Do not add `page_key` or `schema_version` to this correction payload.** Those belong to a different interface. Omitted correction fields preserve existing data.

5. Preview, then explicitly commit root's completed audit:

   ```bash
   python scripts/record_audit.py --record ../work/AUDIT.json
   python scripts/record_audit.py --record ../work/AUDIT.json --finalize
   ```

   Preview validates the same revision and report projections as finalization, but returns metadata only: it leaves no candidate page file and no completion event. Finalization saves immutable before/after page and record snapshots plus `decision.json`, updates the current page/record and reports, records actual completion UTC, and closes the session. The helper does not run lexical validation or refresh the combined transcription/index.

For an interrupted prepared commit, inspect `--status AUDIT_ID` and use `--resume AUDIT_ID` only to finish the saved immutable decision. Resume does not accept replacement decisions. No audit mutation is allowed after freeze or context opening.

## Correction payload fields and projection effects

| Field | Input and effect |
|---|---|
| `edits` | Sequential exact replacements `{"old":"…","new":"…","count":1}` on the **current consolidated page**. The total old-string occurrence count must equal the asserted count. Default count is 1; empty new text is allowed. No normalization or interpretation. |
| `upsert_changes` | Complete locus rows with stable `id`; matching ID replaces in place, a new page-key-prefixed ID appends. These are complete rows, not partial field patches. |
| `remove_changes` | `[{"id":"EXACT_LOCUS_ID","reason":"Root's explicit reason"}]` removes one current row. The earlier row remains in immutable history. Removals precede upserts. |
| `inventory_patches` | Map exact existing element IDs to edited row fields. Each patch must resolve uniquely; scan identity must remain unchanged. |
| `inventory_extra` / `inventory_remove` | Append complete rows, or remove an exact element with a nonempty root-authored reason. Order is remove → patch → append → validation. |
| `remaining_doubts` | Replace the whole current list; omission preserves it and `[]` explicitly clears it. |
| `notation_updates_add` / `notation_updates_replace` | Choose addition or replacement, never both. Each entry has nonempty `sign` and `form`; optional `status` and `attestations`. |
| `abbreviations_add` / `abbreviations_replace` | Choose addition or replacement; each entry has `abbreviation` and `expansion`, with optional attestations. |
| `crops_upsert` | Complete recipes; matching ID replaces its recipe, otherwise it appends. IDs and references are mechanically checked. |
| `observations` | Root-authored text or finite JSON, preserved in the immutable decision and audit report. |

Change rows require `id,place,C,H,final,shows,crop,confidence,against_C,against_H`. Confidence is `high`, `medium`, or `low`; both against flags must be booleans. H differences require mapped H text, an allowed `kind`, and `marked_in_H`. The latter can be a boolean or an explicit nonempty string. Crop references must resolve to current recipes. Allowed kinds are:

- `misread word`
- `misread symbol or index`
- `omission`
- `text not on the page`
- `deletion state`
- `deletion state (struck given live or live given struck)`
- `insertion or placement`
- `abbreviation expanded or spelling modernised`
- `readable ink left as \ill{}`
- `drawing or diagram`
- `other`

Inventory rows use the eight columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed`. Accepted kinds are `text,display,diagram,drawing,margin note,insertion,deletion`. Accepted sheet kinds are `text,reused_typed,typescript,letter,list,cancelled_draft,cover`. The transcribed state must be `yes`. Audit revision uses the already resolved inventory; it does not re-import C.

Text edits and metadata rows are independent root instructions. Editing TeX does not infer changes to flags, collation, inventory, or doubts. Finalization regenerates changes, collation, inventory, doubts, and audit reports from the accumulated current records. H collation contains only rows whose explicit `against_H` is true.

### Root-identified archival numbering

After root's visual classification, an exact own-line `\mspage` may be replaced by a comment, for example:

```json
{"old":"\\mspage{EXACT_ARGUMENT}\n","new":"% archive sheet number: EXACT_ARGUMENT\n","count":1}
```

This is a syntax example only. It does not classify any actual number. For inline material, root must choose the exact span and a newline-terminated comment so percent-comment syntax does not hide following text. Root must separately upsert or remove any now-inaccurate change row, correct inventory as needed, and preserve appropriate unresolved doubts. An obsolete first-pass decision remains available in before-record history even if removed from current projections.

## After all 106 audits

Reconcile every pending entry in `evidence/audit_metadata_followups.json` through explicit root audit history before freezing. This includes the recorded043-30 hand correction. Only after the correction is actually committed may root mark its entry `status:"resolved"` (or `"applied"`) and `applied:true`; retain its source/reason and record the resolving audit ID/time as provenance. The gate never applies a correction. Pending, malformed, or unresolved dispositions block both freeze readiness and final readiness. A present followup file becomes part of the freeze evidence fingerprint.

Validate receipts without changing state:

```bash
python scripts/record_audit_image_first.py --validate --require-no-active --require-completed-pages 106
python scripts/assemble_and_index.py --write --require-complete
python scripts/validate_tex.py pages/*.tex
```

Root reviews the notation indices and reconciles notation across all pages. If that review requires a page change, record an explicit further audit before freezing, then reassemble and refresh the indices. Record the real completed notation review in `documentation/final_readiness/notation_reconciliation.json` using the incomplete template and schema guide. It must identify all 106 ordered keys and the final combined/index hashes. Unresolved notation may remain explicitly recorded.

The existing freeze helper checks all 106 first-pass and audit events, exact map order, complete immutable audit history, no open audit, and exact ordered combined bytes. It freezes 106 pages plus the combined file:

```bash
python scripts/freeze_transcription.py --freeze
python scripts/freeze_transcription.py --freeze --write
python scripts/freeze_transcription.py --verify
```

Only the second command explicitly commits and logs a freeze. Inspect its `committed` result. The freeze helper never opens context. Root may open context only after a valid committed freeze and logs the actual event separately, with the exact form `context opened YYYY-MM-DD HH:MM:SS UTC`. The final validator checks both log position and time against the committed 107-file freeze.

## Notes and final packaging

Use `final_readiness_schema.md` and the incomplete templates under `documentation/templates/final_readiness/`. The root-approved contract names notes files and actual standing-question IDs. Root supplies every review declaration, note section, event, and evidence marker. Classify each question explicitly as `mathematical`, `bibliographic`, or `transcription`. Bibliographic/transcription questions require concrete reviewed notes references, but no CHECK_EVENTS row. They must not be relabelled as mathematical checks.

CHECK_EVENTS retains exactly `statement_id,date,who,type,outcome`. Use only the user's types: `targeted proof check`; `independent re-proof`; `computation or formal certificate`; `used and rechecked in this run`; `carried as background without fault found`; and `refuted`. A refuted event records its refined statement ID in the outcome, or uses the supported `refuted: ID` type form. No transcription, notation, source-review, or generic invented check-event labels are accepted.

After notes, C-notes review, and standing-question work are complete:

```bash
python scripts/freeze_transcription.py --verify --write
python scripts/validate_final_readiness.py
```

The verification command recomputes the 107 frozen hashes and logs the actual result. The final validator independently recomputes them again, validates all ordered audits and image-first receipts, checks declared coverage and evidence hashes, and requires a successful logged verification after the final notes/checks. It is always read-only and never compiles mathematical text.

Only an `ok:true` final-readiness result is sufficient for this mechanical gate. `package_output.py --final` now invokes current final readiness automatically. It requires every validated input to be included, then verifies the closed temporary ZIP's input hashes, protected tree memberships, and required absences before exclusive publication. Root should preserve the validator result and pause output writes while packaging. Checkpoint behavior remains unchanged.

## Checkpoint during an active audit

An active audit is permitted in a checkpoint snapshot. The packager includes its sessions, immutable history, and image-first files. The checkpoint helper now protects those three audit trees as well as current pages/records/reports/logs. Root must pause output/audit writes through staging and packaging so the snapshot is coherent. Scratch image work can continue without changing staged inputs.
