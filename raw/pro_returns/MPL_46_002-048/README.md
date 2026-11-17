# MPL_46_002-048

## Contents

- **MPL_46_002-048_transcription.tex** — the frozen diplomatic LaTeX fragment, in archive scan order, without a document preamble.
- **pages/** — all 42 individual page fragments.
- **MPL_46_002-048_inventory.csv** — 625 element records, all marked transcribed.
- **MPL_46_002-048_doubts.md** — the notation table, localized uncertainties, abbreviation interpretations, and legibility assessment.
- **MPL_46_002-048_notes.md** — 71 research notes, the Fourier/Jacobian witness comparison, self-flagged-step register, title/pagination register, results-state connections, and APA-style references.
- **progress.log** — page completions, second readings, freeze hashes, context opening, checkpoints, and final verification.
- **records/** — page records, second-reading and notation records, frozen hash manifest, technical report, research searches, proof checks, and specialist review records.
- **scripts/** — the tools used to record, check, and package the work.

The supplied selection contains scans 002–048 except 024–026, 035, and 037. Those five faces were excluded by the prompt because another run transcribed them; no pages have been supplied for them in this archive. The attached scans, contextual source files, and input prompt are intentionally not duplicated here.

## Frozen text and research status

The transcription was frozen on 17 November 2026 at 11:42:33 UTC, before opening the contextual archive. Research comparisons are confined to the notes; all 42 page hashes and the combined-fragment hash are checked against records/transcription.sha256.

The main notes incorporate the corrections from the specialist reviews. Research-support files retain intermediate formulations and review recommendations as a record of the work; the main notes give the integrated conclusions and their qualifications. Contextual transcriptions, Hua's modernised reading, and unreviewed results-register claims are explicitly distinguished from the supplied leaves and published mathematical sources.

## Verification and limits

Every supplied whole image and both halves were visually read by the primary transcriber, followed by a second reading of each page. No manuscript OCR was used and no transcription or image audit was delegated. Doubt marks remain material, particularly on the difficult plans, cancelled headings, and late marginal notes.

The inventory verifies inclusion, not infallibility of reading. The source passed structural TeX checks, including the reviewed diagram-arrow syntax, but **no successful compile or rendered-layout verification is claimed**: XeLaTeX failed before manuscript input because its format and the required installation were unavailable. The disposable harness and exact failure output are in records/technical.

The combined file is a fragment using the requested diplomatic macros. An eventual compiling document must supply compatible definitions for those macros and load the needed LaTeX/TikZ packages; the retained harness is technical support, not a verified publication style.

To repeat the read-only structural and freeze checks from this extracted directory:

    python3 scripts/archive_tools.py validate --hashes records/transcription.sha256
    python3 scripts/archive_tools.py verify-hashes records/transcription.sha256
    python3 scripts/verify_notes.py

The final ZIP is the complete deliverable. The two hourly checkpoints are separate recovery snapshots and are not nested in it.
