# Remaining workflow preflight — 73-page baseline

Generated: 2026-11-20 02:15:47 UTC

## Outcome

Static review found five concrete code-path defects and two final-stage responsibilities with no automatic completion gate. No inevitable normal-path blocker was found in the ordered 106-page audit or 107-file freeze. No scripts were changed and no workflow actions or tests were run.

The review began with 73 finalized pages through scan126. Root finalized scan127 during the review; there are now 74 page files and 74 records. All 146 page/record hashes in the saved 73-page preparation still match. All 150 current page/record/log inputs checked while writing this report remained unchanged.

## Concrete code findings

### AUDIT-UNKNOWN-FIELDS — Unknown audit payload keys are silently ignored

Category: code defect; priority: high.

Locations: scripts/record_audit.py lines 307–356; scripts/record_audit.py lines 456.

build_revision processes named fields without a top-level allowlist. A root payload using notation_updates instead of notation_updates_add/notation_updates_replace, or inventory_overrides instead of inventory_patches, can be preserved in root_payload while its requested change is not applied. Finalization can still succeed.

Suggested narrow fix: Reject unknown top-level audit fields in the shared preview/final validation path. Retain observations as the documented extensible text/JSON field. If optional identity fields are accepted, require exact agreement with the selected session.

Focused regression after an approved fix: A misspelled or first-pass-only field must be rejected before any publication in both preview and finalize.

### AUDIT-INVENTORY-IDS — Audit inventory operations can create ambiguous element IDs

Category: code defect; priority: medium.

Locations: scripts/record_audit.py lines 361–380; scripts/record_page.py lines 149–162.

element is an allowed inventory patch field, and extra rows are appended. The final validator does not enforce unique nonempty string-normalized element IDs. A rename/addition collision can be committed, after which the next patch/removal fails its exact-one-element lookup.

Suggested narrow fix: Validate nonempty, unique str(row['element']) values in the final resolved inventory, after all operations. Preserve explicit noncolliding renames.

Focused regression after an approved fix: Reject duplicate additions and rename-to-existing-ID cases identically in preview and finalize.

### AUDIT-CROP-REFERENCES — Crop-reference strings and recipe IDs are validated independently

Category: code defect with compatibility requirement; priority: medium.

Locations: scripts/record_page.py lines 106–107, 141–148; scripts/record_audit.py lines 294–304, 382–393, 470; scripts/inspect_page_sources.py lines 117–120.

A change.crop value must be nonempty, and recipes have unique IDs, but no shared validator resolves each reference to a recipe or supported whole-image view. A typo can therefore pass audit preview/finalization and leave an unusable evidence reference.

Suggested narrow fix: Add one shared reference resolver for first-pass and audit metadata. Accept an exact whole-string recipe ID before splitting multiple references because '+' is legal in IDs. Explicitly support or map the existing whole and both halves references; do not reject those legacy values or change readings merely because they are not crop IDs.

Focused regression after an approved fix: Cover an absent reference, an exact ID containing '+', multiple IDs, whole and both halves compatibility, and preview/final parity.

### VERIFY-WRITE-STATUS — Verification logging can report written=false after changing the log

Category: conditional interruption defect; priority: medium.

Locations: scripts/freeze_transcription.py lines 301–326, 509–517, 535–536.

verify(write=True) appends directly. If append_log raises after writing bytes or during flush/fsync, the generic CLI handler reports written=false although the log may already contain some or all of the verification event. The freeze commit path already has before/after observation; verification does not use it.

Suggested narrow fix: Apply the same observed-write reporting to verification logging and preserve its structured failure result. Keep the completed hash-check outcome separate from a later logging failure.

Focused regression after an approved fix: Inject an append-after-write or flush failure in a temporary fixture and require honest written/unknown status without touching live state.

### PACKAGE-PARTIAL-NAME — An interrupted ZIP write can occupy the immutable final name

Category: conditional interruption defect; priority: high.

Locations: scripts/package_output.py lines 69–77, 96.

The archive is opened in exclusive mode directly at its final/checkpoint filename before source reads and ZIP writes finish. An interruption can leave a partial final-named archive. The next normal retry refuses that occupied name, and CRC validation is reached only after writing.

Suggested narrow fix: Build and CRC-check an exclusive temporary archive in the destination directory, then publish to the immutable name with an exclusive operation such as a same-directory hard link. Never replace an existing archive; retain failed temporary output separately for diagnosis.

Focused regression after an approved fix: A simulated mid-write failure must leave the immutable destination absent; retry succeeds, while an already existing final archive remains untouched.

## Current metadata compatibility notes

The focused check of the original 73 records covers 3560 inventory rows and 2812 crop recipes. It found no duplicate or empty inventory element IDs. Five change rows use references that are not recipe IDs:

| Page | Change row | Reference(s) |
| --- | ---: | --- |
| B10-01_10_scan034 | 1 | whole |
| B10-01_10_scan035 | 1 | whole |
| B10-01_10_scan036 | 1 | whole |
| B10-01_10_scan037 | 2 | whole |
| B10-03_10_scan058 | 9 | whole, both halves |

The existing source-path helper exposes whole/a/b views (inspect_page_sources.py lines117–120). These values require explicit alias handling in a future cross-reference validator; they are not evidence of a transcription problem. Do not modify the records or reject them wholesale while adding a stricter guard.

## Manual final-stage handoffs

### NOTATION-COMPLETION — Notation reconciliation has no completion receipt required by freeze

Locations: scripts/assemble_and_index.py lines 73–100, 140–151; scripts/record_page.py lines 165–184; scripts/freeze_transcription.py lines 188–286; scripts/README_tools.md lines 135–137.

The occurrence/group files are explicitly lexical navigation aids; editorial tables preserve supplied forms and attestations. Freeze validates readings/audits/hashes but has no explicit root declaration that cross-page notation reconciliation is complete or tied to the final audited snapshot.

Suggested handling: Retain this as an explicit root-only stage before freeze. For machine-enforced handoff, add a root-authored completion receipt bound to the final page/record hashes and require it at freeze readiness. The helper must never decide whether notation is mathematically consistent.

### FINAL-DELIVERABLE-GATE — Final packaging does not validate notes, CHECK_EVENTS or final readiness

Locations: scripts/package_output.py lines 59–81, 89–97; scripts/record_page.py lines 327–333, 382–391; scripts/README_tools.md lines 186–193, 229; scripts/freeze_transcription.py lines 453–471.

--final only chooses the filename; it does not require a committed freeze, passing 107-file verification or final notes/CHECK_EVENTS schema. No workflow script creates or validates the research-notes/CHECK_EVENTS relationship. The doubts renderer retains its Work in progress fallback unless root supplies editorial_metadata.legibility. Context opening is manual; the verifier checks its line position, not its timestamp grammar.

Suggested handling: Keep checkpoint packaging permissive. Add or use a separate final-readiness check for the prescribed deliverable names, fresh passing frozen-file verification, required notes, CHECK_EVENTS header/row structure/statement IDs and the agreed date conventions, completed root notation handoff, and final editorial metadata without the fallback. Root supplies all substantive notes/check outcomes and logs actual context opening only after freeze.

## Schema observed without reading note content

Inventory columns: scan, sheet_kind, hand, element, kind, position, first_words_or_objects, transcribed.
Collation columns: folder, their_page, our_scan, line, their_reading, codex_reading, final_reading, scan_shows, kind, marked_in_H, confidence.
CHECK_EVENTS columns: statement_id, date, who, type, outcome.

At report time no top-level notes file is present, CHECK_EVENTS is 35 bytes, and editorial_metadata.json is absent. These are expected pending human stages while context remains sealed. The packaging code does not currently distinguish their pending state from a final-ready state.

The final transcription hash contract remains exactly 106 page files plus the combined file. Reports, notes, PREAMBLE, check events and supporting documentation need their separate final-deliverable completeness check; this does not change the 107-file freeze contract.

## Existing gates retained

- All106 mapped page/record identities and the84/22 cote split are required before audit/freeze completion.
- First-pass done events and first audits are checked in map order, with matched sessions and immutable history; incomplete sessions block freeze.
- Current pages and records must match the latest audited snapshots, and combined bytes must equal exact ordered page concatenation.
- New freeze preparation pins page/record/session/history/combined hashes and completion-event evidence; the freeze marker is the commit point.
- End-stage verification checks all107 frozen files. Context opening is a separate actual root action after the freeze marker.

## Scope and evidence

Only helper code, tooling documentation, headers, filenames, hashes and the specified ID/reference metadata were inspected. No image or witness-prose interpretation, mathematical work, source-edit replay, context opening/extraction, audit, freeze, package or upload occurred. This is a static preflight, not a live readiness assertion that the unfinished 106-page workflow is complete. Exact source hashes and protection evidence are in the companion JSON.
