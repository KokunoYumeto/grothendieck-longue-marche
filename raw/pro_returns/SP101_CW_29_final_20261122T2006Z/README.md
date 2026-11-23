# SP101_CW_29 — consolidated diplomatic transcription

## Scope and reading order

The edition covers archive scans 13–17, 19–26, 29, 31–33, 35 and 79–81 of cote 29: 21 pages in all. Assignments follow the supplied page-map order (79–81, then the earlier scans); the combined LaTeX fragment is assembled in ascending archive-scan order. Each page is first read by one of three readers, checked by the main reader, and later audited at selected difficult loci by a reader who did not read that page in the first pass.

The authority is the visible ink in the supplied JPEGs. C, H and S are aids to collation, not independent confirmations. No OCR, text-recognition service, outside transcription or external research is used. No TeX compilation is performed; the structural validation is limited to the specified syntax and documentary consistency checks.

## Completed edition

All 21 pages received the first reading, main adjudication and a blind second reading of the prescribed difficult places. The second reading covered 585 boxes. Exact token comparison, ignoring whitespace alone, found 321 differing boxes; this includes differences of notation and crop context. Main adjudication changed 97 physical places, including changes in certainty. A box may contain more than one physical place, and overlapping boxes may cover the same place; these three totals therefore measure different things. The blind reading was a second reading of those boxes, not a second transcription of every line on every page.

| Apparatus item | Count |
|---|---:|
| Finished page files | 21 |
| Recorded decisions | 631 |
| Substantive changes against C | 130 |
| Substantive changes against H / H collation rows | 593 |
| Inventory elements, all transcribed | 410 |
| Remaining doubtful loci | 149 |

The 21 page files and the combined fragment were frozen together at 19:54:24 UTC on 22 November 2026. Their 22 SHA-256 values are in `records/transcription_sha256.json` and `progress.log`; the latter records the final check that they remained unchanged. `STRUCTURAL_VALIDATION.txt` records the syntax and documentary checks, and `BUNDLE_MANIFEST.json` identifies every other file in the archive by size and SHA-256. Documentary corrections after the freeze do not alter the transcription.

## Contents

- `pages/` and `SP101_CW_29_transcription.tex`: adjudicated diplomatic LaTeX. The combined file is a fragment; use the PREAMBLE.tex already supplied with the witnesses. No unchanged source file is duplicated here.
- Changes, collation, inventory, doubts, notes, error-sheet feedback and hand log: the requested editorial apparatus.
- `crops/`: the actual contextual crops read during first adjudication and blind audit. Coordinates in the apparatus refer to the whole-page source image, not a resized half.
- `second/`: box coordinates, first readings, blind second readings, token comparisons and main resolutions.
- `records/`: page-reader returns and the main reader’s adjudications. These are documentary records, not additional authorities.
- `records/checkpoint_drafts/`: the exact three unfinished page drafts present in earlier checkpoints before their completed versions were moved to `pages/`. These historical files are retained to preserve the checkpoint record; use `pages/` for the finished transcription.
- `scripts/`: assembly, audit comparison and structural-validation programs; none recognizes text in images.
- `progress.log`, `CHECK_EVENTS.tsv`, `SOURCE_INDEX.tsv`: chronology, the exact scope of mathematical checking, and hashes identifying the supplied sources.

## Source and witness credits

Université de Montpellier. (n.d.). *Groupe fondamental [Autour de SGA 4 et SGA 7]: Lettres (1959, 1967, 1969), tapuscrits et copies de tapuscrit annotés (s.d.), notes manuscrites (s.d.)* [Fonds Alexander Grothendieck, cote 29, selected scans]. Supplied JPEG images from archive file 29.pdf; no external page was consulted.

Murre, J. P. (1969, April 30). *Letter to Alexander Grothendieck and Comments* [Typescript with handwritten interventions, cote 29, scans 79–81]. Université de Montpellier, fonds Grothendieck. The date is read from scan 79; the attribution is supported by its signature.

Commutator project (Michel Hua). (n.d.). *Grothendieck project: Transcriptions of cote 29* (commit aef7db2) [AI-generated LaTeX witness H, supplied files]. https://github.com/Commutator-IO/grothendieck-project

Witness C comprises the supplied GPT-6 Astra transcriptions A29-01 and C29-01 through C29-03, dated 13–15 November 2026 in the package provenance. Witness S comprises the supplied 18–19 November sweep’s decided readings. These provenance statements come from the supplied materials and have not been independently verified online.

The correction tables supplied for S have no explicit ID column. This edition cites them by filename plus a one-based data-row number (excluding the header), for example `c29a_CORRECTIONS.tsv:row1`. The two rows that touch the selected scans concern the section-heading overprint on scan 31 and the disjointness condition on scans 21–22.

## Interpretation of the apparatus

Counts refer to loci, not token error rates. A macro wrapper alone is not a textual correction. The apparatus retains explicit decisions on previous doubts without counting certainty alone as a substantive change. Hand/type attribution is documented separately where the letters agree. An unresolved reading remains marked in the text; neither witness agreement nor mathematical plausibility removes it. Mathematical comments never replace the visible text.
