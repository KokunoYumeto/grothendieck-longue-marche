# Reader B: final static QA

Snapshot: 2026-11-21T02:34:17.251158+00:00

Final read-only static output/metadata audit. No image rereading, OCR, outside research, or TeX compilation.

## Counts

| Measure | Count |
|---|---:|
| pages | 23 |
| finalized_audits | 23 |
| material_places | 715 |
| against_C | 276 |
| against_H | 640 |
| marks | 261 |
| inventory_elements | 520 |
| doubt_entries | 275 |
| in_place_unsure_occurrences | 304 |
| check_events | 63 |

## Output consistency

11 aggregate files were independently regenerated in a temporary directory and compared byte-for-byte with the deliverables.
Production static validator: 0 errors, 0 warnings.
Confirmed static errors: 0. Diagnostic candidates awaiting manual disposition: 0.

## Confirmed errors

None.

## Diagnostic review

- **doubt_mapping_review:dc7b7b90799120** (148_scan049): The leading somme and alternative sommes are stored in separate reading/alternatives fields.
- **doubt_mapping_review:3c4ff413a23286** (148_scan049): The sigma leading reading and star alternative are stored separately; this is the same exponent.
- **doubt_mapping_review:0606fb193ef35a** (148_scan049): The inserted-then-deleted caractérisé is the leading reading, and live inserted caractérisé is the explicit alternative.
- **doubt_mapping_review:d812ee526c5cb3** (148_scan050): The full uncertainty/deletion/diagram unit is present in the record; literal comparison differs only because the record has no source linebreak whitespace between commands.
- **doubt_mapping_review:06f23c37ee395e** (148_scan051): The record gives inserted de as its reading and continuous baseline de as the alternative, matching the in-place state alternatives.
- **doubt_mapping_review:79afcdd12a52c4** (148_scan051): The phrase dans un contour and alternative les uns un contour are stored separately.
- **doubt_mapping_review:61878980c5d9bf** (148_scan063): The repères leading reading and repéré alternative are separate fields at the same raised replacement.
- **doubt_mapping_review:04b0d79225ec0d** (148_scan063): The catégories reading and analogues alternative are separate fields for the same cancelled first word.
- **doubt_mapping_review:4113d8a5a1fc69** (148_scan063): The record identifies visible (**) with uncertain deletion state and gives deleted (**) explicitly as the alternative.
- **doubt_mapping_review:f534c0b26ae7de** (148_scan063): The whole target is recorded with plus/minus as primary and complete minus/plus target alternatives; it covers this local operator.
- **doubt_mapping_review:7ada37ad78ad8c** (148_scan065): The la reading and le alternative are stored separately at the named article.
- **doubt_mapping_review:87b5d8b181c82e** (148_scan067): The shared cancellation-state entry covers the complete definition and torsor block. Its alternatives explicitly distinguish complete cancellation from framing/earlier-drawing strokes; internal letter doubts have their own entries.
- **doubt_mapping_review:75d88558f5a2a9** (148_scan067): The same shared cancellation-state entry covers the intervening edge-condition equality within the large definition/torsor block. Its inner alpha/gamma and elevated-mark uncertainties are also separately recorded.
- **doubt_mapping_review:c28be05ceea567** (148_scan067): The shared entry explicitly names cancellation of the complete torsor block, covering this outer state wrapper; the inner isom/auto and gamma/index doubts are separately recorded.

## Limits and preservation

2 large figure uncertainty wrappers have separately reviewed links to their existing connectivity/state doubt entries. Literal checks and these dispositions found no confirmed missing mapping; they are metadata checks, not a new proof of visual transcription completeness.
All accepted page/record and aggregate input hashes were checked again after the audit. They were unchanged.
No accepted data were edited. The separate reader_a method/provenance report covers independent-reading chronology, frozen TSV continuity, crop provenance and checkpoint preservation. The reader_c report covers final notation-summary consistency. The main reader owns the final transcription freeze and package.
Earlier QA reports are retained as historical snapshots; their former pending-audit counts are not current totals.
