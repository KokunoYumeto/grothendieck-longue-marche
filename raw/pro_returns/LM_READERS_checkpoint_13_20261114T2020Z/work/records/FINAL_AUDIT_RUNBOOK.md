# Final rebuild audit runbook

This is an execution plan, not a claim that the pending rebuild has passed. Commands run from the project root. Historical revision 512 observations remain evidence for that revision only; final clearance must name the current PDF and TeX hashes or an explicit exact-pixel transfer record.

## 1. Shared changes installed

The apparatus rule, heading and first entry receive a four-footnote-baseline reservation, no-break boundaries, and a group-local starting-list penalty. The generated range heading receives an eleven-baseline reservation only in the forms that print that heading. The scan 494 reservation deferral recognizes both the historical six-baseline reservation and its accepted eighteen-baseline replacement for section 49. The independent source replay mirrors the latter two framing changes exactly.

Exact before/after definitions, file hashes, inverse checks and accepted candidate/validation hashes are recorded in `work/data/shared_heading_guard_integration.json`. The root's retained-doubt guard and `LMcancelledtag` definition are preserved. Typeset owns integration of the paired source-local section495 records and the other accepted layout records.

## 2. When each step can run

| Step | Required state | Owner |
|---|---|---|
| Ten-heading source inventory | Fresh final TeX and both source-mark inventories assembled | Editorial |
| Native finding source inventory | Immutable sources and current finding definitions available | Editorial; already prepared for 36 findings |
| Full source replay and seven-PDF margin audit | All seven final compilations complete; aggregate change logs refreshed | Editorial |
| Ten-heading PDF queue | All seven PDFs stable and source inventory matches that assembly | Editorial |
| Per-book native finding queue | Complete build stable; current source map and TeX beside each PDF | Per-book reviewer |
| Actual native observations | The exact queued images have been viewed | Per-book reviewer |
| Generated heading and pagination closure | Final stable PDF set and current candidate queues | Glossary and assigned reviewers |
| Master finding confirmation | Actual master image review, or explicit current all-page pixel comparison to reviewed apparatus pages | Glossary with root merge |
| Central release report | All current hash-bound reports and observations complete | Root |

No optional revision 512 audit rerun is needed. If a build, source-mark file, scan map, or finding definition changes after a queue is created, regenerate that queue. The native helper rejects stale queue inputs.

## 3. Source integrity

After assembly, compilation and aggregate record refresh:

```sh
python work/scripts/verify_sources.py --stage build
```

Use the full recipe. `--skip-current-recipe` and `--ledgers-only` do not constitute final source replay.

Outputs are `work/data/master_integrity_build.json` and `work/records/MASTER_INTEGRITY.md`. The JSON has top-level `stage`, `source_units`, `readers`, `languages`, `errors`, `warnings`, `paired_authorial_variant_ids_match`, and `status` fields. Release requires `status: PASS`, no errors, seven current TeX hashes and matching actual/declared common-body hashes.

The fixed source inventory is 116 packages and 245 translation units, reassembled in both languages, with 1588 manuscript scans per language. Each raw language has 17117 literal doubtful marks and 1261 illegible marks. There are 10888 paired authorial variants: 6702 deletions and 4186 insertions. French has 10888 total variants; English has 10889 because of the single documented glossary correction. These raw semantic counts are distinct from the number of literal marks in duplicated branches and from executed PDF annotations.

The audit checks raw source hashes, unit reassembly, the mechanical and layout stages, exact source projection of editorial annotation, corrected uncertainty preservation, reversible instrumentation, raw source readings in the change logs, one common body across each language's forms, source-ID execution ledgers, privacy, and single-file TeX portability. It rebuilds the framing independently and compares that result with the actual common body in all seven TeX files. PDF page layout remains a separate audit.

## 4. Seven-PDF margin collision audit

This can run concurrently with source integrity once all seven PDFs are stable:

```sh
python work/scripts/audit_margin_collisions.py
```

The candidate list remains `work/data/margin_collision_candidates.json`. The completed execution manifest is `work/data/margin_collision_audit.json`:

```json
{
  "schema": "margin-collision-audit-v1",
  "status": "COMPLETE",
  "readers": [
    {"file": "BOOK.pdf", "sha256": "CURRENT_PDF_SHA256", "pages": 0, "candidate_count": 0}
  ],
  "total_candidates": 0,
  "candidate_file": "work/data/margin_collision_candidates.json"
}
```

The actual manifest must contain all seven readers with their exact current hashes and page counts. `COMPLETE` means the audit ran to completion. It does not clear a nonempty candidate list.

The scanner identifies distinct right-margin text lines with substantial horizontal overlap and unusually close baselines. It excludes landscape pages and isolated single-character components to reduce mathematical false positives. Any candidate receives a native crop and requires actual visual resolution. This audit complements full-page and native diagram inspection; it does not prove that every mathematical component is collision-free.

## 5. Ten shared-heading witnesses

Regenerate the source inventory after final assembly, even when the immutable source wording is unchanged:

```sh
python work/scripts/check_heading_closure.py prepare
```

This reads source and assembled mark metadata only. Output: `work/data/heading_witness_inventory.json`. It refreshes exact current source IDs and master-argument hashes; in particular the section V preliminary note can have a newly inserted layout wrapper.

After the complete PDF set is stable:

```sh
python work/scripts/check_heading_closure.py queue --final
```

The queue writes `work/data/heading_closure_final.json` with ten `PENDING_VISUAL` witnesses and renders a full 900px page plus native 3× heading/body crop for each. Evidence is placed under a PDF-hash directory in `work/visual_repair_proofs/heading_final/`, so a new revision cannot overwrite historical images. The preceding report is preserved under `work/data/heading_closure_history/`.

The five diplomatic note witnesses are the source margins formerly numbered m582 at C2:492, m599 at C2:508, m725 at C3:73, m1108 at C3:416, and m1576 at C4:132. Their current printed m-numbers and physical pages are derived again from source IDs. The remaining five witnesses are section V and its preliminary-data opening at C3:548 in the five primary readers.

View all twenty generated images. Save an observations object keyed by `reader|witness-id`, for example:

```json
{
  "LM_FR_diplomatique|note-m582": {
    "status": "PASS",
    "observation": "Write the actual current full-page and enlarged heading/body observation here."
  }
}
```

Then record the actual observations:

```sh
python work/scripts/check_heading_closure.py record --observations work/data/heading_closure_final_observations.json
```

Release requires `heading_closure_final.json` to show `PASS`, `pass_count: 10`, `expected_witnesses: 10`, and the exact five current primary PDF/TeX hashes. Each witness must carry its current source ID, raw source hash, source scan, actual observation, reviewer and current evidence hashes. A same-page graphic candidate is only a lookup aid; it is never substituted for the actual image review.

## 6. The 36-finding native confirmation queue

The central ledger is `work/data/final_visual_issue_closure.json`, owned by root. Its current 36 finding definitions require 237 book confirmations:

| Book | Findings | Confirmation method |
|---|---:|---|
| `LM_FR_diplomatique` |31 | Actual current native images |
| `LM_FR_corrige_apparat` |35 | Actual current native images; editorial owns this queue |
| `LM_FR_texte_de_lecture` |33 | Actual current native images |
| `LM_EN_corrected_apparatus` |35 | Actual current native images |
| `LM_EN_reading` |33 | Actual current native images |
| `LM_FR_master_annotated` |35 | Actual images or exact current apparatus/master pixel transfer |
| `LM_EN_master_annotated` |35 | Actual images or exact current apparatus/master pixel transfer |

The source-only inventory is prepared with:

```sh
python work/scripts/prepare_native_closure.py prepare
```

Output: `work/data/final_native_closure_inventory.json`. This resolves every finding to a package, raw source path, source-file hash, scan-start line and raw scan-text hash in both languages. It records the required inspection, historical finding, affected forms and a stable hash of the finding definitions. It grants no clearance and reads no PDF.

After the complete rebuild is stable, each primary reviewer runs the queue command for their book. For the editorial allocation:

```sh
python work/scripts/prepare_native_closure.py queue --final --reader LM_FR_corrige_apparat
```

The corresponding output is `work/data/final_native_closure_queues/LM_FR_corrige_apparat.json`. Substitute any exact book basename from the table for another reader. The helper checks the actual common-body hash, resolves the current scan source ID, reads the compiled scan-to-page map, and renders 900px candidate pages in a PDF-hash namespace. It includes source scan pages and neighboring pages for headings, apparatus and introduced blocks. Candidate page selection is not a visual claim.

Every queue contains the current `pdf_sha256`, `tex_sha256`, `actual_body_sha256`, `scan_map_sha256`, `source_marks_sha256`, and `finding_definition_sha256`. Each finding includes `id`, `cote`, `scan`, `package`, source hashes, current `source_id`, `source_scan_pages`, `candidate_pages`, `required_inspection`, and `minimum_native_scale`.

Inspect the candidate full page to locate the exact source site. Render a native crop using the actual page number and PDF-point coordinates chosen from that page. The following is a command template; replace its capitalized values:

```sh
python work/scripts/prepare_native_closure.py crop \
  --queue work/data/final_native_closure_queues/BOOK.json \
  --finding FINDING_ID --page CURRENT_PHYSICAL_PAGE \
  --clip X0 Y0 X1 Y1 --scale 8
```

Omit `--clip` to produce a native full page. Geometry sites require at least 8× enlargement of the repaired labels/routes; heading, tag and option-syntax sites require at least 3×. The crop command appends its exact page, scale, clip, PDF hash and PNG hash to the queue's evidence catalog. It never records an observation. Source neighbors outside the default page neighborhood should be investigated and explicitly added by a reviewed helper change, not silently accepted by the validator.

For each finding, check the particular failure described in the historical observation and verify its current source context. A geometry check includes adjacent labels and endpoints. A heading check includes the first substantive opening rather than only a scan marker. Cancelled-tag checks distinguish generated parentheses from retained uncertainty anchors. The shared generated-heading findings also require glossary's separate all-page final candidate and known-witness closure; one representative crop cannot stand for that entire sweep.

Each reviewer writes an independent observations array, without mutating the central ledger:

```json
[
  {
    "id": "EXACT_FINDING_ID",
    "reader": "EXACT_BOOK_BASENAME",
    "pdf_sha256": "CURRENT_PDF_SHA256",
    "status": "RESOLVED",
    "reviewer": "ACTUAL_REVIEWER",
    "observation": "Specific description of the source site and visible result actually inspected.",
    "images": [
      {"path": "RELATIVE_VIEWED_IMAGE_PATH", "sha256": "CURRENT_IMAGE_SHA256"}
    ]
  }
]
```

Use `ISSUE` if a residual defect is actually visible. Do not copy an expected outcome into an observation before viewing its image.

Validate a complete per-book observation file:

```sh
python work/scripts/prepare_native_closure.py validate \
  --queue work/data/final_native_closure_queues/LM_FR_corrige_apparat.json \
  --observations work/data/final_native_fr_apparatus_observations.json
```

Output: `work/data/final_native_closure_validated/LM_FR_corrige_apparat.json`. The validator checks exact finding coverage, current build/source hashes, reviewer-supplied status and observation, image hashes, source-page neighborhood and required native enlargement. Its `VALIDATED_OBSERVATIONS` status authenticates the submitted evidence; the supplied observations remain the reviewer's responsibility. `--partial` can validate an unfinished subset, but a partial file is not a release gate.

Root merges these observations into each finding's `publication_confirmations`, adds the accepted repair record IDs, and changes a finding to `RESOLVED` only when its affected-book set is completely satisfied. The central report requires the exact current PDF hash and viewed images or explicit comparison records for every confirmation.

## 7. Annotated-master transfer

Glossary supplies current all-page apparatus/master pixel comparison reports. Transfer a reviewed site only if every final source page used by its apparatus observation is pixel-identical to the corresponding master page. The confirmation names the master reader and current master PDF hash, cites the actual apparatus observation and includes the comparison record path and hash. Different title pages do not prevent source-page transfer; an unverified source-page difference does.

A master comparison cannot transfer an unreviewed primary observation, a different PDF revision, or merely similar-looking pages. If the comparison fails at a required site, inspect the current master page and native crop directly.

## 8. Separate final gates retained

The above workflow does not replace final seven-book PDF/link/bounds checks, the selected-page visual ledgers, the equation-pagination closure, glossary's generated-heading/rule/range all-page audit, font and minimum-size checks, source-local repair semantic audit, privacy audit, or root's final release report. All of those reports must agree on the same current files before packaging.
