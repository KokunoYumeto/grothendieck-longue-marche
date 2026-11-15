# Final validation report

Validation time: 2026-11-15 11:47:56 UTC

## Coverage and state

| Check | Result |
|---|---|
| Expected retained scan set | 42 pages; exact match |
| Page-completion log records | 42 |
| Second image-audit log records | 42 |
| Combined transcription | Exact ordered byte concatenation |
| Inventory | 693 rows; all transcribed=yes |
| Sheet classifications | 24 reused_typed; 9 typed; 7 text; 2 cover |
| Doubt register | 124 entries |
| Research notes | 82 unique labelled items |
| Research-note context searches | Refreshed by the per-note builder |
| Frozen SHA-256 values | All 43 unchanged |
| Context timing | Opened only after the recorded freeze |

Research-notes SHA-256: 456a268f724f1072ecd3ad32de893bb6a31172f7061b5b551813a4ae3e1a9ac2

## Mechanical validator

PASS: 42 page files; 1 SHA-256 manifest(s); partial=False; mechanical checks only, no claim of transcription completeness or accuracy

## Per-note context validator

PASS: 82 notes, 453 queries, 143 matched queries, 310 empty queries

## Limits and independent review

The mechanical validator does not verify paleography or mathematical truth.
All images were read by the primary transcriber before the freeze; no additional
reading is claimed by these tests. The research-note integrity and targeted
mathematical reviews are documented in research/final_notes_review.md and the
source-verification registers. Full TeX compilation was unavailable because
format/package data were missing; no rendered typesetting proof is claimed.

The archive builder additionally verifies ZIP integrity, every packaged file
against package_contents_sha256.txt, and all frozen page/combined hashes inside
the archive before reporting success.
