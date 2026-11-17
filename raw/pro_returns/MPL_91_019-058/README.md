# MPL_91_019-058

Diplomatic transcription and separate research notes for Alexander Grothendieck's cote 91, retained scans 019–058. Scans 030 and 033 were omitted as blank in the supplied task; the package contains all 38 retained faces.

## Main files

| File | Contents |
|---|---|
| MPL_91_019-058_transcription.tex | One LaTeX fragment, in scan order, with no preamble or document class; an exact byte concatenation of the 38 page fragments. |
| pages/ | One fragment for each retained scan, beginning with its scan marker. |
| MPL_91_019-058_doubts.md | The single notation table, all 487 uncertainty marks and 13 illegible spans, proposed abbreviation expansions, and the legibility/reliability statement. |
| MPL_91_019-058_inventory.csv | 779 element rows with the requested columns, every row marked yes; 35 text faces, one cancelled draft and two programme/title faces. |
| MPL_91_019-058_notes.md | 97 scan-level research items, three synthesis tables, the separate indexes of authorial reservations and titles/counts, and checked primary comparisons. |
| progress.log | Initial UTC timestamp, sequential page completions, all 38 second audits, checkpoint records, freeze hashes, context-opening time and the final unchanged-hash verification. |

## Reading and uncertainty

The same reader inspected every whole-page image and both supplied halves, in order, without OCR or delegated transcription. Every retained page then received a separately logged visual audit before context was opened. The transcription was frozen at 2026-11-17 23:04:59 UTC; context was opened at 23:05:09 UTC. Subsequent interpretations and suggested repairs occur only in the research notes.

The uncertainty count is a count of marked occurrences, including nested or repeated marks, rather than a word-error estimate. The most difficult material includes the small margins, overwritten outlines, cancelled arguments and the clipped transition at scan 055. An unmarked reading is not guaranteed correct. Deletion, insertion and marginal states remain explicit, and graphic content is represented by 27 tikz-cd environments, one array/table diagram and 12 TikZ drawings.

The TeX fragment requires the supplied state macros to be defined by the reader's surrounding document and requires the usual mathematical and TikZ packages. Structural checks passed; a full typeset render could not be completed because the available environment lacked the LaTeX class/format and TikZ packages. Consequently the visual placement of typeset diagrams and callouts has not been render-verified.

## Research scope

The main notes keep the frozen source, Michel Hua's project's modernised interpretation, unreviewed neighbouring-package notes, and explicitly labelled editorial calculations separate. Every catalogue item was searched against all six supplied context files. RESULTS_STATE identifiers retain their stated run or intake status unless a narrowly specified calculation is checked in the notes; no novelty claim or global status upgrade is made.

The main findings include the two obstruction-compatibility obligations on scans 020–021; the mixed relation missing from the abstract linear formulation on 024; scheme-versus-algebraic-space and separation qualifications; the distinction between ordinary sheaf intersection and a quasi-coherent infimum on 039; counterexamples testing the scope of preservation and numerical claims; and a complete modern proof of the four-condition finite étale criterion under finite locally free hypotheses. The precise statements, hypotheses, attribution and limits are in the numbered notes and proof appendices.

## Supporting records

The research/ directory contains the three finalized source blocks, per-item context queries and match logs, primary-reference records, the detailed finite étale argument, and the independent linear-compatibility review. These files support the assembled main notes.

The review/ directory preserves the inventory reconciliation and its prior state. The current inventory is the top-level CSV. The precontext_observations.md file records provisional thoughts made during visual work; it is explicitly superseded by the final research notes. The notation, abbreviation and reliability source files also appear in the combined doubts file. audit_changes.md records the pre-freeze corrections.

The scripts/ directory documents page recording, auditing, notation/graphic inventory checks, freezing, hourly checkpoints, research assembly and mechanical validation. The supplied images, original archives and extracted source files are excluded.

To repeat the read-only package checks from the extracted package directory:

    python3 scripts/validate_package.py --strict-commands

These checks verify file structure, marker order, exact concatenation, inventory metadata, basic TeX syntax and the recorded hashes. They do not certify handwriting accuracy or replace the visual audits.
