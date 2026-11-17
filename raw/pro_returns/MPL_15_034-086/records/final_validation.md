# Final validation — MPL_15_034-086

Checked 2026-11-17 21:14:40 UTC.

## Integrity and coverage

- All 31 page fragments and the combined transcription match all 32 SHA-256 values recorded before the context opened.
- The combined file is the exact ordered concatenation of the page fragments, apart from its documented blank-line separators; it starts with the required cote and scan commands and has no preamble.
- The actual supplied scan list contains 31 pages; the later reference to 49 pages in the prompt does not match the attachment manifest.
- Inventory: 644 rows, all transcribed=yes, with the required eight column names and all seven permitted element kinds represented.
- Sheet classifications: 23 handwritten subject sheets and 8 reused typed/printed sheets.
- Doubts: 415 occurrences of the doubt macros in the transcription and 415 corresponding register rows.
- Progress log: 31 page-completion entries and 31 second-reading audit entries; freeze precedes context opening.

## Research report

The final report has 15,843 whitespace-separated words and 77 individually identified research notes: MB01–MB16, D01–D18, B01–B21, R01–R14 and X01–X08. It also has the 22-entry unverified-step register U01–U22 and the 18-entry title/page-number register P01–P18. The planning answers, linear/nonlinear comparison, cautious A–D concordance, arithmetic Nori sequence, and S15 scope table are included. Markdown table column counts were checked; the report has one top-level title and contains no working-status banner or raw retrieval IDs.

The primary agent reviewed the research sections, checked the cited primary-source passages, and independently checked the main explicit examples and calculations. A second mathematical review checked the special-ideal tensor inverse, the generator-change argument, the monoidal counterexample and adjusted tensorator, the Dedekind localization converse, and the norm/character/cocharacter qualifications. These checks do not confer archival review status on the supplied first-pass contextual notes or solve the open ledger items.

## Limits of validation

The primary agent visually read every supplied whole image and both halves, then audited each page against its image before freezing. No OCR was used on those images and no parallel worker transcribed or changed a page.

Structural LaTeX checks passed before the freeze, but a full LaTeX compile and rendered output were unavailable because the installed executable lacks its format and required package tree. After the context opened, scan 069 was found to encode the initial v of the prose word vérifient as a math-font command outside math mode. This known markup defect is preserved under the user's strict freeze rule and described in X08; successful compilation is not claimed. Hash equality proves preservation, not that every difficult reading is correct.

The archive builder separately checks ZIP integrity and excludes the supplied attachments, extracted source files, source images and image renders. Work records, scripts, notes and logs are retained.
