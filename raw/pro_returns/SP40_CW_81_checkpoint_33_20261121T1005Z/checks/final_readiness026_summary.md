# Finalization readiness after scan025

Source-only readiness and unapplied proposals. This work read source files and performed in-memory exact comparisons. It did not view or read image bytes, recalculate stored mathematical or coordinate results, execute any existing/proposed builder or validator, compile, render, edit a page or committed record, change events/history/progress, freeze, archive or upload.

## Current result

The complete source audit at **2026-11-21 08:36:50 UTC** found all **23 expected records through025**, all **23 exact completion-log entries**, all **69 complete reader attestations**, and all required reader report/TeX files. Every page and the combined transcription passed the inspected structural checks. The combined bytes equal the builder's exact ordered page concatenation, with one cote marker and the correct 23 scan markers.

Current totals from those records are **1,156 decisions, C548/H620, 508 remaining local doubts, 1,028 inventory entries and 29 page check events**. The inventory CSV and 620-row H collation TSV exactly equal their current record projections. CHECK_EVENTS.tsv exactly equals its 29 page events plus 24 global events, for 53 rows. Every source input remained byte-identical throughout that audit.

The present final-validation rule rejects **30 documented C_doubt_status strings**. Their full values, original source rows and compound/component bindings are preserved in the status proposal described below. The current structural_validation.json is a historical nine-scan result, ending at011; its only recorded issue is `Only 9 of 24 scans complete`. A new full validation is required during finalization.

The scan026 record and selected-draft prerequisites were absent at the audit snapshot. A later source-only existence check found an **in-progress** scan026_root_crop_audit.json: three distinct positive-success paths, `planned_crops_completed: false`, and last decision time `2026-11-21T08:42:34.643670+00:00`. That file's observed SHA-256 was `15535dd7c3eb0cec4b08e7e38e12614ffc8c7c35f842e7ec519705f5ab82a8cb`. It supplies no final026 count. Root is still completing026.

Full source hashes, exact checks and current-input projections are in `out/checks/final_readiness026_audit.json` (SHA-256 `474aabe0bafd8d8e4060a71daf216adf1d6a2fdfd5c57bbe577695f151c62a90`).

## Exact proposal read order

1. Existing NREV proposal: `out/checks/notation_NREV01_NREV02_public_report_proposal_v01.md`, then its `.json` and `out/checks/notation_NREV01_NREV02_map_dependency_v01.json`.
2. Existing workflow proposal: `out/checks/wf_root_crop_counts_through025_proposal/proposal.md`, `preview.md`, `forward.diff`, `forward.patch.json`, and `source_replay.json`. Its `evidence.json` contains all exact path/source mappings.
3. New additive event proposal: `out/checks/final_readiness026_scan017_event_proposal.json`. The complete single-event public TSV preview is `out/checks/final_readiness026_scan017_event.proposed.tsv`.
4. New selector correction: `out/checks/final_readiness026_workflow_selector_proposal.json`.
5. New validator proposal: `out/checks/final_readiness026_status_review_index.json`, all six `final_readiness026_status_review_01.jsonl` through `_06.jsonl` files in order, `out/checks/final_readiness026_validate.diff`, and `out/checks/final_readiness026_validator_status_proposal.json`. Every review chunk is at most 11,000 bytes. The complete catalog and validator rule-data input are `final_readiness026_status_catalog.json` and `final_readiness026_status_rule_data.json`.

All proposals remain unapplied. Original copies and exact forward/inverse replays are retained under `final_readiness026_*` for the three newly prepared corrections.

## NREV-01 / NREV-02: verified existing proposal

The proposal JSON SHA-256 remains `499af7497dbe39609400f3ea6d2cb62a6d3ff090e1cff906868065c387c446ce`. Its 40 current before-values match exactly. Its 11 root-authority sections and 16 selected-source spans match their file hashes, character spans, UTF-8 byte spans and literal/span hashes. Forward replay changes exactly 20 decision-final values and 20 matching current doubt-reading values. Inverse replay recovers both original record byte strings with original key order and formatting.

| Target | Exact before SHA-256 | Exact proposed after SHA-256 | Changed fields |
| --- | --- | --- | ---: |
| out/records/scan018.json | 42a52aebd1f3157cf16540f01407289091564676f9e7b792c33e93a06dd118c4 | 9f999bd1ed0a4fe152124d79297134090bf6e0ae0fd286c197d09babb949c5c7 | 2 |
| out/records/scan021.json | 9f98d5d0cdbfe80b530915fdd818b659d8616855c2216538bd68abe035440429 | a4c1dee1b4583c9beac4d7bd5f331b2318be8892c00dc643b44c7ad097dfdad2 | 38 |

The page invariants are scan018 `b194c003d55fa088e4a8db1f64875c59919c253715c510298f7785daa9291e62` and scan021 `96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce`. Historical scan018 map SHA-256 `efb7882a461c319cc893b2649625b58bdea1376f32c1682cb2fb2894999fee0c` and all 263 equal-digest record leaves are preserved. The complete 40 exact target-pointer/old-value/new-value mappings are also in the readiness audit's `/nrev/exact_allowed_field_mapping`.

## Workflow crop-count proposal: verified existing proposal

The exact bounded source replacement targets only the workflow-generation block of `out/scripts/build_records.py`:

- Expected before SHA-256: `6724ab2ccd715f263f917e5b6af1c789058e13d118b009e5302cf4e032fb856a`.
- Proposed after SHA-256: `fefa9810da89eaab4ff70a1729e83140d6bb1826ddd66b423102d0f6dc33c618`.

The current builder equals the proposal's before snapshot byte for byte. The forward replacement yields its proposed full source exactly; the inverse recovers the original bytes. Prefix and suffix outside the replacement remain exact. The proposed source was kept inert.

All 13 formal audits for 013–025 and their exact successful-path rows still match the stored evidence: **293 distinct paths = 52 root-created + 241 reused reader paths**. All formal and historical source hashes match except `/existing_workflow_source`, which explicitly records the earlier 22-record cumulative workflow snapshot. That historical output hash is `f6e143cec371fdcee8c7084e5d961bb894f58df863f37c54b839f6d285f3a7f8`; the current 23-record output hash is `12bcaaa417ff39a47493ef65d7485410ef7267684ac064437d8a5cd0a30a8372`. The builder patch's before-hash guard remains satisfied.

The proposal preserves scan003's incompletely recorded total/reused counts. Root still needs the completed 026 audit and its exact source evidence before final workflow approval. The existing proposed helper reads that formal audit through its positive-success path array; no 026 count is supplied by the through025 proposal.

## Additive scan017 public-event projection

`out/records/scan017.json#/check_events/0` currently contains exact `id` and `actor` fields and its observation/input/map/result/scope data. The builder's five-column projection uses `statement_id,date,who,type,outcome`. The current zero-based TSV data row 28 is exactly:

| statement_id | date | who | type | outcome |
| --- | --- | --- | --- | --- |
| empty | 2026-11-20 | empty | computation or formal certificate | empty |

The new proposal adds exactly three keys at the end of that existing event: `statement_id` copies `/check_events/0/id`; `who` copies `/check_events/0/actor`; `outcome` is compact JSON text of the nine exact existing keys `statement_or_location`, `inputs`, `mapping`, `result`, `scope`, `event_clock`, `event_clock_note`, `rerun_by_clerk`, and `mathematical_theorem_check`, in that order. Each key/value has an explicit source pointer. Decoding that outcome recovers those exact typed values. No new event, coordinate calculation, result or claim is supplied.

- Record before SHA-256: `4653b2d90ba7d86e3306b4bf357c43ba9b74634e2fc97de2474d7503ef613435`.
- Proposed record after SHA-256: `acb8ba688eb4d9b38381a437213e7c4b91ce885a264ccb1b961111d60b2c7697`.
- Proposal SHA-256: `0f57754e91e3349994329109f98bc2a6c3badb64404b845eb89a0e91260ff6e8`.

All original fields and order remain; inverse removal of the three additions restores the exact original record bytes. Global events and prior logs remain untouched.

## One workflow-evidence selector correction

The exact current value at `evidence.json#/earlier_pages/2/enumeration_selector`, in the scan004 row, says `root-only manifest; scan003 successful use separately attested by journal line31`. Its own hashed journal source and exact excerpt identify scan004 line 3. The proposed single replacement is `root-only manifest; scan004 successful use separately attested by journal line3`.

- Evidence before SHA-256: `1a1bdd82104ce0981bc6efbc3ec372ef417f676d9081245922f9f7fbc2315dab`.
- Proposed after SHA-256: `9babfd57508488eb20a45aa50b6d55590628429c8b87faa6dea23fa7319db78c`.
- Proposal SHA-256: `3a5a82ea6977415b54552464e5464c32aa5d3e9f754fbb47bc69d3b502077806`.

Its inverse recovers the original evidence bytes. Counts, paths, journal content and the builder patch stay unchanged.

## Exact validator compatibility proposal

The original rule accepts only null, `resolved` and `retained`. The 30 additional recorded strings occur in 015 (3), 016 (6), 017 (1), and 024 (20). Their stored documents include primary-order/capitalization qualifications, compound glyph/state components, and original C row identifiers. The 25 original C rows and all 30 exact status pointers are retained in the bounded review. In particular, the 016 rows separately retain resolved glyph and qualified state components; 017-D06a retains its explicit original-et/new-state component list; 024-R09 retains its mixed accent/punctuation outcomes.

The proposed predicate retains the original three accepted values. For each of the 30 additional entries it requires the exact scan/decision identity, full original status string, exact source-row/part and qualification fields, and the exact documented row/component outcomes. Guard comparisons use ordered compact JSON, preserving scalar types and object key order. The rule-data file is guarded by its own SHA-256. There is no status conversion, prefix acceptance or change to a committed status.

- Validator before SHA-256: `36dd396ed69e6aa37f45766f6e71ee53e168fd1179825d0ee679f5f7557de358`.
- Proposed validator after SHA-256: `e0805651314a843f009c4fa563e240224bb3cd187ed431dd329d03c1488c2e66`.
- Required rule-data SHA-256: `4bf28c7a90b1399a7843d29557884e36c13fa1ceb9738fbbe09de7b29cdff9f8`.
- Proposal SHA-256: `4f031740b651503158cbee4424f19c2722765a248475bea59c42244588307f94`.

The finite equality evaluation on current records retains all 1,126 original acceptances and recognizes exactly the 30 documented additional entries, totaling 1,156. Proposed code was neither executed nor compiled. The two source replacements and their inverse recover the original validator bytes exactly. Its rule-data dependency must remain at `out/checks/final_readiness026_status_rule_data.json` with the stated hash. The future 026 record's actual statuses remain subject to the final gate.

## Root-owned execution sequence and dependencies

All commands below are for root's later authorized finalization; none was run by this helper.

1. Complete 026's selected source, decisions, inventory, doubts, original C outcomes, source audit and final crop audit. The approval script requires these exact paths: `out/checks/scan026_record_draft.json`, `scan026_reader_fingerprints.json`, `scan026_root_crop_audit.json`, `scan026_source_audit.md`, `scan026_final_draft.tex`, and `scan026_final_source_map.json`. It verifies every fingerprint pair, the three reader attestations, no whole/half root view, distinct once-successful crop records and their hashes, empty pending decisions, all reviewed counts, the draft SHA-256 and source-map draft binding. Root must supply the independently reviewed values for the following CLI arguments; they were unavailable at this readiness snapshot:

   `python out/scripts/approve_page.py 26 --sha256 REVIEWED_DRAFT_SHA256 --C REVIEWED_C --H REVIEWED_H --decisions REVIEWED_DECISIONS --inventory REVIEWED_INVENTORY --doubts REVIEWED_DOUBTS --crops REVIEWED_CROPS --events REVIEWED_EVENTS`

2. `python out/scripts/commit_page.py 26` checks all previous completion lines, the reader files, selected-page structure and root-text equality, decision IDs, source-reader keys, doubt/abbreviation fields and inventory flags. It rebuilds cumulative reports and appends 026's completion line. Its source invokes the structural TeX function; the full record-status gate is reached later through validate.py.

3. Finish root's all-page review and authorized bounded source changes: NREV 40-field repair, scan017's three additive event keys, the one evidence selector, workflow builder block, and the exact validator compatibility rule. Preserve every original/inverse artifact. Add completed 026 source evidence to the final workflow review. Review `out/notation.md`, `out/legibility_note.md`, and `out/workflow_assessment.md` as the builder's final report inputs; their existing historical wording remains source material.

4. `python out/scripts/build_records.py` regenerates changes, H collation, inventory, CHECK_EVENTS, notes, doubts, the combined transcription and workflow from the approved records and current report inputs. Read the complete generated public reports and their exact changed fields.

5. `python out/scripts/validate.py` writes `out/checks/structural_validation.json`. Root must inspect all 24 `complete_scans`, `tex_ok: true`, and an empty `record_issues` list. The script itself prints issues and normally exits 0, so exit status alone does not establish this gate.

6. `python out/scripts/finalize.py freeze` requires all 24 expected records, every main_adjudicated flag and completion entry, then reruns the builder and validator and asserts a clean result. It creates `out/freeze_manifest.json` with 25 exact SHA-256 bindings: 24 page files plus the combined transcription; it appends those hashes and the freeze time to progress.log. The manifest was absent at the readiness snapshot.

7. `python out/scripts/finalize.py archive` rechecks every frozen transcription hash, requires the nine public files listed below and a nonexistent final destination, appends recheck/archive log entries, and creates `SP40_CW_81.zip` in the workspace root. It recursively includes files under out/ except `.zip` files and `__pycache__` paths. Root controls final file quiescence, checkpoints, archive verification and uploads.

The archive existence list is: `SP40_CW_81_transcription.tex`, `SP40_CW_81_changes.md`, `SP40_CW_81_collation.tsv`, `SP40_CW_81_doubts.md`, `SP40_CW_81_inventory.csv`, `SP40_CW_81_notes.md`, `progress.log`, `SP40_CW_81_workflow.md`, and `CHECK_EVENTS.tsv`, all beneath out/. All nine exist now; the final 24-page contents remain dependent on 026 and the approved final rebuild. `SP40_CW_81.zip` did not exist at the readiness snapshot.

## Inspected current script hashes

| Script | SHA-256 |
| --- | --- |
| out/scripts/finalize.py | f5ce866685ad67b4995795078c92396688293bb703593c76445fcb3800271567 |
| out/scripts/validate.py | 36dd396ed69e6aa37f45766f6e71ee53e168fd1179825d0ee679f5f7557de358 |
| out/scripts/build_records.py | 6724ab2ccd715f263f917e5b6af1c789058e13d118b009e5302cf4e032fb856a |
| out/scripts/approve_page.py | be12ac120a5b5a8bcad35af475210468dd8c232d843d1a14122e0fd8f739f978 |
| out/scripts/commit_page.py | 9b1845887a6a11c4ee9fbd46959ebf2bd6b7ea9bf8d60f6560c66b5caa3ebce2 |
