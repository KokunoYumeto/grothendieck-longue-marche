# IM02_6-9 transcription corrections

## Contents and authority

- `placements.tsv` is the decision ledger, in the exact order of the supplied corrections table. The composite key is **id, cote, scan**; an id can occur on more than one page.
- `edited_pages/` contains the final diplomatic TeX pages. Each page is reconstructed from the original bytes using only its recorded category (a) replacements.
- `notes.md` records category (b) refinements, category (d) locations, and retained reading uncertainties. Catalogue descriptions and mathematical refinements remain editorial notes.
- `crops/` contains the enlarged visual evidence, with page and row identifiers in the filenames.
- `CHECK_EVENTS.tsv` records the actual scope of the readers' checks and the main review. Visual transcription checks do not constitute independent mathematical proofs.
- `progress.log` begins with the run's actual UTC start time and records each completed page after its files and placements were written.
- `reviews/` contains the accepted reports, including the main-reader decision and events. These reports govern the final pages and ledger.
- `reader_reports/` contains the working reader reports and proposed TeX files, including any explicit pre-acceptance main-reader adjudication. Later cross-location notes can appear only in the accepted report.
- `scripts/` contains the crop-generation, exact-span review, byte-restoration and packaging scripts, together with the assigned-page reader protocol.
- `PAGE_STATUS.tsv`, `VALIDATION.json` and `FILE_LIST.tsv` document page coverage, package validation and member hashes.

## Reading and preservation

Three readers worked concurrently, one assigned page at a time, with the next page assigned to the first free reader in the supplied page order. The main reader reviewed each returned decision and its scan evidence before accepting the page. Image readings were made by direct visual inspection; crop enlargement and contrast adjustment use Pillow.

For category (a), the `find` string is an exact, unique span of the original page, and `replace` contains only its correction. For (b), (c) and (d), both fields are empty. Some exact spans contain CRLF line endings and are quoted TSV fields: use a TSV reader that supports quoted multiline fields. Do not split the file into records by physical lines alone.

The original pages use CRLF line endings. The final byte comparison replays each accepted replacement over the original bytes and compares the complete resulting page. Existing spelling, punctuation, diagrams, cancellations, insertions and other unrelated bytes are preserved. An early newline-normalization error on the first thirteen accepted pages was corrected by replay over the original bytes; that correction is recorded in the log and check events.

An explicit `\unsure{reading|alternative}` is a completed diplomatic decision where the ink remains ambiguous. It does not mean the row was skipped. Mathematical or historical refinements supplied by the corrections table are identified as supplied unless the check event states a stronger, actually performed check.

External catalogue descriptions, scan ranges, and attribution labels absent from the page TeX receive category (d), even when the corrected local subject agrees with the manuscript. That positive local identification and any visually verified cross-location are recorded separately in the notes. Category (c) is reserved for a transcription locus that already represents the requested reading, including an explicitly retained doubt where the supplied correction itself is tentative.

Michel Hua readings supplied in the table are treated with the human-check authority specified by the prompt. They are applied unless the visible ink plainly contradicts them; references to earlier model passes are not silently assigned that authority. No external publications or independent mathematical proofs were used in this run.

## Original inputs and reproducibility

The attached prompt, original corrections table, original pages, scans and preamble are deliberately excluded from the archive, as requested. The scripts used the once-extracted originals under `IM02_work/source/`, the current-page bundles under `IM02_work/assignments/`, working reports under `IM02_work/reviews/`, and accepted deliverables under `IM02_work/deliverables/`.

To replay validation, arrange the original input and these deliverables in that layout. `scripts/review.py` reconstructs pages from the accepted reports; `scripts/package_work.py validate` checks exact original spans, row order, coverage of accepted pages, crops, notes, check events and the final TeX bytes. Crop scripts retain the actual crop boxes and image transformations used in this run. Their original workspace paths may need relocation when rerun elsewhere.

Checkpoint archives, if the run reaches a 45-minute interval, are separate immutable full snapshots and are not embedded in this archive. The final package contains the current deliverables and documentation.

## Completed review

All 92 supplied rows across 58 pages have a final decision: 16 category (a), 22 category (b), 2 category (c), and 52 category (d). The 16 recorded replacements affect 11 pages; the other 47 pages remain byte-identical. Seven targeted rows retain explicit reading uncertainty, described in the notes. All page-level questions are closed.
