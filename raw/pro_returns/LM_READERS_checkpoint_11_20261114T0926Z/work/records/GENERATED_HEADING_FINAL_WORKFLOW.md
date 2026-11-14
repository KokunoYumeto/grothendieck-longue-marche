# Final generated-heading closure gate

This gate covers every physical page of all seven publication PDFs. It is separate from the ten source/note-heading witnesses in `work/data/heading_closure_final.json` and from source equation-tag pagination. It covers generated apparatus headings, retained-doubt headings, range headings, and a separator rule detached from its heading. Apparatus rules use .26 of the text width; retained-doubt rules use .2.

## Final report contract

The mandatory report is `work/data/generated_heading_audit_final.json`, with schema `generated-heading-audit-v1`. Its status is `PENDING_FINAL_BUILD`, `PENDING_ACTUAL_REVIEW`, `FAIL`, or `PASS`. Only `PASS` is releasable. A missing observation is never converted automatically into clearance.

Top-level fields are:

| Field | Required content |
|---|---|
| `schema` | `generated-heading-audit-v1` |
| `status` | `PASS` only after all gates below succeed |
| `files` | Exactly seven unique rows, each with `reader`, project-relative `path`, `sha256`, `pages`, `stable_during_audit`, `generated_heading_count`, `candidate_count` |
| `scanner` | `{path, sha256}` for `work/scripts/audit_generated_heading_endings.py` |
| `source_inputs` | Array of `{path, sha256}` for current generator/preamble inputs, all seven generated TeX drivers containing their complete inline source bodies, audit helper scripts, and available generation metadata |
| `candidate_inventory` | `{path, sha256}` for the current all-page scanner output |
| `witness_inventory` | `{path, sha256, count}` for the frozen collection of actually observed before-repair heading/rule/range detachments |
| `review_inputs` | Array of `{path, sha256}` for the actual observation files consumed |
| `primary_candidates` | Every unique current primary candidate with its actual observation and evidence; status `CLEARED_ON_FINAL_PDF` |
| `master_candidates` | Every unique current master candidate with status `CLEARED_BY_IDENTICAL_RENDER`, its source primary candidate and current all-page pixel-comparison reference |
| `witnesses` | Exactly one row for each frozen known witness, with status `RESOLVED_ON_FINAL_PDF`, actual observation, current PDF hash, source identifiers, and final images |
| `comparisons` | Array of `{path, sha256}` for the current FR/EN apparatus-to-master pixel reports used for transferred clearance |
| `counts` | `files`, `primary_candidates`, `primary_cleared`, `master_candidates`, `master_cleared`, `expected_witnesses`, `witnesses_resolved`, `unresolved` |
| `unresolved` | An empty array is required for `PASS` |

An actual primary-candidate observation has `id`, `reader`, `pdf_sha256`, `status`, `reviewer`, nonempty `observation`, `heading_page`, `first_content_page`, and a nonempty `images` array of `{path, sha256}`. A rule-only case also has `rule_page`. For a false-positive candidate these pages identify the intact unit; the observation must explain what the scanner could not infer (for example, graphic-only opening content).

A known-witness observation uses the same evidence fields plus `heading_kind`, `cote`, `scan`, and, where available, `package`. The required final unit has its separator, heading and first entry/content together. The first content page must equal the heading page, and the rule page, if supplied, must also equal it. A source range heading can have manuscript markers between it and the first actual source content; those markers alone do not close a witness.

Master candidates may inherit only a current, actually cleared primary candidate when both boundary pages have identical rendered RGB pixels and the full-page comparison covers the actual page counts and current hashes of both books. No review is inferred from a PDF title, source similarity or an old build.

## Publication validation

The finalizer checks every input, PDF and evidence image hash; exact candidate-ID coverage and uniqueness; exact known-witness-ID coverage and uniqueness; actual observation text and reviewer attribution; same-page closure; current all-page master comparisons; and the absence of unresolved findings. For a known apparatus or retained-doubt witness, the claimed title page must contain a prepared title hit and the claimed first-content page must contain its exact source-entry anchor. A range witness must match a prepared range-title hit and supply the actual source-content observation. Candidate title pages must match the prepared title side of the boundary. Reviewer-supplied fields cannot replace the source identity or prepared localization. The finalizer reopens all seven PDFs and freezes their hashes before and after validation. A failed or stale finalization writes a non-PASS result rather than leaving an earlier PASS in place.

The baseline inventory is historical evidence. It does not claim that every scanner candidate was defective. Only actually observed detachments enter the known-witness closure inventory. Every candidate of the final scanner run is nevertheless accounted for by an actual final observation or a rigorous current pixel-identity transfer.

## Frozen witnesses and execution

`work/data/generated_heading_known_witnesses.json` has schema `generated-heading-known-witnesses-v1` and status `FROZEN_ACTUAL_BEFORE_WITNESSES`. The expected count is derived from its complete unique witness array. The immutable original inventory is retained byte-for-byte as `work/data/generated_heading_known_witnesses_revision512.json`; every original row must remain unchanged in every extension. Its original 48 rows comprised 11 French apparatus, 9 English apparatus, 14 French reading, and 14 English reading witnesses. Three actually confirmed revision578 detachments at the C4:134 range opening were added, one each in French diplomatic, French apparatus and English apparatus, giving a current total of 51. Exact source identifiers, attributed observations, original PDF hashes and content-addressed historical PNG bytes are retained for every witness. The finalizer has no fixed numerical witness-count assumption.

After all seven complete PDFs are stable, prepare the final all-page scanner inventory and evidence queues:

```sh
python work/scripts/verify_generated_heading_final.py prepare --final
```

The command writes `work/data/generated_heading_final_candidates.json`, `work/data/generated_heading_verification_queue.json`, and one primary-reader queue under `work/data/generated_heading_final_queues/`. Images reside under a seven-PDF-hash namespace within `work/visual_repair_proofs/generated_heading_final/`. Historical files are not overwritten. Known entries are located by their exact printed source-entry anchor; range headings use the exact scan range and archive-link context. Localization supplies candidate pages only. Every observation still requires an actual image review.

Each reviewer writes an observations array containing the exact prepared item `id`, `reader`, `pdf_sha256`, required `status`, `reviewer`, `observation`, `heading_page`, `first_content_page`, optional or required `rule_page`, and the prepared `images` actually viewed. These fields are top-level fields of each observation, not nested inside another object. A rule-only item requires `rule_page`; all stated unit pages must coincide for clearance.

Once actual primary reviews and both current all-page master pixel reports are complete, finalize with one `--observations` argument per independent reviewer file:

```sh
python work/scripts/verify_generated_heading_final.py finalize \
  --observations work/data/generated_heading_final_FR_diplomatique_observations.json \
  --observations work/data/generated_heading_final_FR_apparatus_observations.json \
  --observations work/data/generated_heading_final_EN_apparatus_observations.json \
  --observations work/data/generated_heading_final_FR_reading_observations.json \
  --observations work/data/generated_heading_final_EN_reading_observations.json
```

Every book with known witnesses or final candidates requires its observations file. Every final primary candidate needs an actual clearance, including a candidate in a book with no historical known witness. A missing, duplicate, foreign, stale, or unresolved observation prevents `PASS`. The finalizer checks the actual current PDF page counts against the complete comparison records, rather than trusting a self-reported comparison length.
