"""Write the edition guide from the completed verification and frozen hashes."""
from pathlib import Path
import collections
import csv
import json

E = Path(__file__).resolve().parents[1]
v = json.loads((E/'verification.json').read_text())
frozen = json.loads((E/'transcription_sha256.json').read_text())
with (E/'CHECK_EVENTS.tsv').open() as stream:
    events = list(csv.DictReader(stream, delimiter='\t'))
types = collections.Counter(x['type'] for x in events)
event_lines = '\n'.join(f'- {label}: {count}.' for label, count in types.items())
text = f'''# SP75_C13_145 — consolidated diplomatic transcription

This edition covers all 24 supplied scans, in the order 003,005–027. It contains a consolidated reading of the manuscript and the evidence and records from the two passes. The source inscriptions, including cancellations, insertions, marginal notes, drawings, abbreviations, unmatched delimiters and apparent slips, govern the transcription. The supplied AI witnesses are comparison material, not independent evidence for a reading.

## Transcription

`SP75_C13_145_transcription.tex` is the combined LaTeX fragment, with no preamble. `pages/` contains the 24 corresponding page fragments named exactly as in witness C. Use the supplied `PREAMBLE.tex` from the original attachment when incorporating the fragment into a LaTeX document. No additional macro definitions or package requirements have been introduced.

The transcription was frozen at **{frozen['frozen']}**. `transcription_sha256.json` contains the SHA-256 values of all 24 page files and the combined fragment; those values and the final unchanged-hash verification are also in `progress.log`. Source validation was non-compiling: no TeX compilation was performed.

## Reading apparatus

| File | Contents |
| --- | --- |
| `SP75_C13_145_changes.md` | Per-page and total counts; consequential corrections; C, H and final readings; observed strokes, crop filenames, original pixel boxes and confidence; remaining doubts; independent-reading comparisons and decisions. |
| `SP75_C13_145_collation.tsv` | One row for every counted locus differing from H, with the requested 11 columns. H's page number is our scan number minus 1. |
| `decisions.tsv` | All {v['marks']} indexed C doubt marks in original MARKS.tsv order, including retained uncertainty and the crops supporting resolved readings. |
| `SP75_C13_145_doubts.md` | Consolidated notation table, page-specific notation observations, remaining doubts, abbreviation expansions and legibility assessment. |
| `SP75_C13_145_inventory.csv` | All {v['inventory_elements']} inventoried page elements, each marked transcribed, with sheet kind and hand attribution. |
| `SP75_C13_145_notes.md` | Page accounts, the mathematical reasons for looking again, retained authorial slips and the limits of actual checks. |
| `SP75_C13_145_sheet_feedback.md` | Counts under the ten supplied error categories and recurring subcases, with locus references. |
| `SP75_C13_145_hand_log.md` | Page-scoped handwriting and notation observations, their limits and the witness consequences. |

There are **{v['substantive_loci']} substantive loci**: **{v['against_C']} departures from C** and **{v['against_H']} from H**. A locus can differ from both. One additional uncertainty-only observation is fully published and explicitly excluded from these totals and the confidence/category totals. The doubts table contains **{v['remaining_doubts']} entries**; entries may concern several alternative glyph or revision states. Neither these figures nor the audit totals below estimate a token error rate.

## Independent second reading

All 24 first pages were completed before the independent audits began. Each second reader differed from that page's first reader and received only its image and structural box list. The first box readings were sealed before comparison. The audits cover **{v['second_boxes']} boxes**; **{v['second_differing_boxes']} boxes differed token by token**, and crop adjudication changed the consolidated page at **{v['second_changed_boxes']} boxes**. Overlapping boxes can concern the same substantive locus.

`second/` preserves each box list, first reading, independent reading, crop manifest, comparison, token-level differences, assignment, reading receipt and adjudication, together with `FIRST_READINGS_SHA256.tsv` and `AUDIT_METHOD.md`. `packet_boundary_incident.json` records the corrected TSV packet-boundary incident and the resulting second-reader exclusion. The final verifier enforces that exclusion. `crops/` includes the saved visual evidence for both passes; no OCR was used.

## Mathematical checks and their scope

`CHECK_EVENTS.tsv` has **{len(events)} recorded events**:

{event_lines}

These labels describe the work actually performed. Transcribing an assertion was not counted as proving it. Conditional computations state their assumed conventions or preferred readings; their outputs do not settle obscured ink. Source slips and incomplete expressions remain in the transcription even when a local calculation refutes a proposed interpretation. No sources beyond the supplied pages and witnesses were researched.

## Documentation and source maintenance

`reader_reports/` retains original first-reader reports, current reviewed reports, proof outputs, consistency reviews and application receipts. Original first-reader checks are historical records; scan027's original validation is explicitly retained as `initial_reader_validation`, with current counters separately identified. `assignment_metadata/first/` preserves the geometry, guidance and notation snapshots supplied with each first-reading assignment. `scripts/first_reading/` contains unchanged historical preparation scripts. These historical scripts and snapshots are documentation and should not be rerun against the finalized edition.

Final static maintenance addressed display payloads inside text-mode cancellation macros, an insertion around a display, a marginal command within an enclosing strike, TikZ boxing, a prime, and the grouping of an uncertain base before an exponent. The doubled Gamma on scan024 uses a small inline TikZ glyph because the supplied blackboard font's Greek-capital slot does not supply that glyph. Exact plans, narrow current-quotation updates and before/after receipts are included. The source readings and physical correction scopes are unchanged by these serialization edits. First/second readings, comparison token records, source-witness quotations and historical edit instructions were preserved.

`verification.json` records the final completeness checks, including all 24 audits, all 1,017 source difference-list rows, all 117 indexed marks, crop references, grouping, derived counts, the first-reading seals and exact equality of the combined fragment to its 24 page fragments. `FILE_LIST.txt` lists the archive members. `checkpoint_registry.json`, `run_state.json` and `progress.log` document the run and checkpoint history.

The original attachment, full scans, witness files, supplied preamble, reproducible page halves and earlier checkpoint archives are deliberately excluded. The saved crops and work documentation are included.

## Primary source

Grothendieck, A. (n.d.). *Printemps 81 (vieille rédaction)[149]: Notes manuscrites* [Manuscript, cote 145]. Montpellier archive. Archival identification and title are supplied by the task; scan numbers provide the source locators. C and H are the two supplied derivative transcriptions.
'''
(E/'README.md').write_text(text)
print('Wrote README.md from completed verification, check events and frozen transcription hashes.')
