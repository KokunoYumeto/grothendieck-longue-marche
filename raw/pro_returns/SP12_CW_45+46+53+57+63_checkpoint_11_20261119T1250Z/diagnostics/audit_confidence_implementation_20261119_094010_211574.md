# Explicit audit confidence — implementation and validation

Installed and verified **2026-11-19 09:40:10 UTC**. Supplementary mechanical capture: **2026-11-19 09:43:33 UTC**. The current committed subset contains **43 pages and 43 decision records**, through 53/31.

## Outcome

Implemented the additive `audit_confidence.json` mechanism. The installed file contains exactly version 1 and an empty pages object: **zero actual occurrence entries and zero inferred assignments**. The required five-column doubts table is retained. The full existing doubts document is byte-identical after rebuilding with the empty file.

A valid explicit value is keyed by the mapped page filename, one-based source line and Unicode-code-point column, and exact full macro text. A raw-page SHA-256 binds the entry to the current page version. Confidence is supplied explicitly by the primary reader and is not inferred from its same-page decision reference.

## Helper changes

| File / function | Change |
|---|---|
| review.py: _audit_source_text | Shares UTF-8/universal-newline reading for exact source coordinates |
| review.py: _audit_json_loads | Rejects duplicate keys and non-finite JSON constants |
| review.py: _validate_audit_confidence | Validates schema, page hash, exact active occurrence, unique location, confidence enum and same-page decision reference |
| review.py: _unsure_confidence_detail / wrapper | Optional validated index takes precedence only at its exact occurrence; returns primary_occurrence provenance; missing entries retain first-pass behavior |
| review.py: rebuild_doubts | Validates all entries before its sole output write; rejects stale inputs without heuristic fallback; preserves existing output when validation fails |
| diagnose_committed.py: capture/load_helpers/audit/write_reports | Captures optional audit data and raw page bytes, uses the same validator/resolver, and reports explicit-audit coverage/provenance |

New support files are the empty root `audit_confidence.json`, root `AUDIT_CONFIDENCE.md`, and `scripts/test_audit_confidence.py`. No actual occurrence templates were populated. The complete code change is preserved in the adjacent unified diff.

Validation rejects unknown or missing fields, duplicate JSON keys/locations, stale hashes, changed coordinates or macro strings, inactive/commented examples, malformed unsure markup on an audited page, invalid reference paths or indices, booleans masquerading as integers, and confidence values outside high/medium/low. There is no whitespace normalization, closest-position search, semantic matching or automatic relocation on the explicit path. Referenced decision ordinals must remain stable; the schema validates their existence and same-page location, not their semantic suitability.

## Tests and preservation

**All 27 synthetic unittest methods passed, with zero errors or failures.** Tests cover the required invalid-input cases, Unicode columns/tabs/CRLF, repeated literals isolated by occurrence and page, explicit-value precedence, five-column rendering, absent/empty compatibility, unchanged last-good output after invalid data, duplicate keys in referenced synthetic decision records, and both rebuild and diagnostic adapters. Test authoring and fixtures did not use actual page or decision prose.

**All 95 protected data files retained their before/after SHA-256 hashes**, including all 43 pages, all 43 decisions, combined transcription, every derived table/document, notation, preamble and event log. The full existing doubts document stayed byte-identical. No c/h/final reading, decision confidence, page text, or combined text changed.

Actual committed-output checks were mechanical only, performed separately after the synthetic tests passed. Source scans, witness files and context stayed closed; no OCR, compilation or semantic review occurred.

## Mechanical QA through 53/31

| Check | Result |
|---|---|
| Inventory | 1,579 rows; exact decision-derived values and order |
| Collation | 1,200 rows; exact decision-derived values and order |
| Structural / enum / brace findings | None |
| TeX environments / explicit groups | 108 environment pairs; no imbalance findings |
| Python scripts | 33 parse, including the new test suite; zero warnings |
| Combined transcription | Raw-byte match to the existing page-map-order builder |
| Doubts | 490 literal entries; all generated confidence cells match the existing helper |
| Pending / explicit primary entries | 260 pending; 0 explicit entries |

53/31 has **92 decision entries, 71 inventory elements, and 28 unsure occurrences**. Seventeen occurrences copy existing recorded confidence and eleven remain explicitly not assessed:

| TeX line:column | Existing bookkeeping reason | Candidate decisions, one-based |
|---|---|---|
| 6:837 | Multiple retained-C records | 10, 25 |
| 17:48 | Multiple retained-C records | 10, 25 |
| 17:318 | Multiple final records | 30, 43 |
| 24:519 | Multiple final records | 33, 40, 57 |
| 30:53 | No qualifying record | — |
| 30:83 | Multiple retained-C records | 69, 78, 82 |
| 33:43 | Multiple retained-C records | 69, 78, 82 |
| 37:10 | Repeated retained-C occurrence | 80 |
| 37:25 | No qualifying record | — |
| 37:55 | Multiple retained-C records | 69, 78, 82 |
| 37:611 | Repeated retained-C occurrence | 80 |

53/30 has 82 decisions, 62 inventory elements and 21 unsure occurrences; five remain pending at 3:1146, 9:41, 11:44, 11:170 and 19:398. Their exact candidate associations are preserved in the supplementary JSON. The earlier copied-confidence associations on 53/17, 53/24 and 53/29 remain unchanged; no additional association was found in this capture.

## Evidence

- `audit_confidence_implementation_20261119_094010_211574.diff`: complete helper diff.
- `audit_confidence_implementation_20261119_094010_211574_tests.txt`: installed synthetic-suite result.
- `audit_confidence_implementation_20261119_094010_211574_hashes.json`: all preservation hashes and implementation metadata.
- `mechanical_support_43_20261119_094333_941377.json`: environment, syntax and exact pending-position checks.
- `committed_diagnostics_20261119_094010_838699.*`: the current standard structural reports and saved filename metadata.

Checkpoint 007 remains scheduled for **2026-11-19 09:50:45 UTC**, with a short mutation hold before packaging. No extra checkpoint was created during implementation.
