# Research method and restart guidance

The primary agent completed the single-stream transcription and both visual passes. No OCR was used for the manuscript images, and no parallel agent transcribed or amended a page. The page and combined TeX files are frozen; verify them against frozen_sha256.json, but never regenerate or edit them after the context opening.

The context was extracted only after the recorded freeze. Its README, RESULTS_STATE, and Hua project README were read before research drafting. The supplied Hua modernised reading was read in full by the research team, with focused sections compared against the frozen transcription by the responsible reader. Earlier context notes remain claims/leads, and no source-driven correction has entered the transcription.

Research division after freeze:

- Deuring gerbes, local signs, crystalline comparison, and descent: records/research_deuring.md.
- Brandt, Morita, Picard constraints, exact sequences, and order arithmetic: records/research_brandt.md.
- Planning questions, requested linear/nonlinear table, neighboring period evidence, and modern motive comparisons: records/research_motivic_bridges.md.
- Compact tori and norm calculations, reused typescripts, and markup disclosure: records/research_root.md.
- Explicit manuscript questions and title/page-number register: records/research_standing.md.

The primary agent reviews drafts and opens primary web references before assembling the main notes. A working main notes file may omit sections not yet reviewed, while the checkpoint still includes every draft already saved. The final report is generated only from reviewed sections; the individual research drafts remain work records.

Run assemble_notes.py only for the Markdown report. Do not run finalize_pre_context.py again: it belongs to the pre-freeze record and writes frozen material.

make_archive.py verifies all 32 frozen hashes, packages every deliverable and record, and excludes source/rendered-source image formats and supplied ZIP/PDF sources. Checkpoints are due once per hour from 2026-11-17 20:04:21 UTC, starting at 21:04:21, and must not be created at intermediate milestones. Final packaging is separate from the hourly checkpoint rule.

The original attachments and extracted context are intentionally absent from the archive; a new session can re-extract the supplied attachments. Source-page crops and Oda renders belong outside the deliverable directory. External references are identified by URLs and theorem/section locators, not copied into the ZIP.

## Known validation limitation

Structural checks before freeze passed, but a complete LaTeX compile could not run because the installed TeX executable lacks the LaTeX format and required package tree. During research inspection, the frozen scan069 file was found to encode the initial v of the prose word vérifient with a math-font command outside math mode; this markup defect is disclosed in note X08, with no post-freeze edit. This specific issue and the absent compilation must not be reported as a successful render test.
