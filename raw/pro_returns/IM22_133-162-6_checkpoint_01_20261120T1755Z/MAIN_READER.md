# Operational record for this transcription run

The user requests all 405 table rows on all 309 supplied pages, with no unrelated corrections. Three reader agents work concurrently, each on exactly one page at a time. `scripts/assign_next.py` is the main reader's locked, ordered dispatcher. It assigns the next page to the first free reader. Readers return only single-page results and crops; the main reader reviews and writes final pages.

## Source and outputs

The original ZIP was extracted once into `../source/`. It remains unmodified. Original pages use CRLF line endings. The commit script retains those exact bytes except for accepted row edits. The correction IDs are not globally unique: identify placement rows by `(id,cote,scan)`, preserving original table order.

`page_jobs/<stem>/input.json` gives one page's original paths and rows. `result.json` is that reader's proposed decision record, subject to main-reader amendments. `reviews/<stem>.json` records the main reader's committed decision and hashes. `edited_pages/`, `placements.tsv`, `notes.md`, `CHECK_EVENTS.tsv` and `progress.log` are written only by the main reader's commit script.

## Reviewing a returned page

1. `python work/scripts/review_and_commit.py status` reports completed and unreviewed returns.
2. `python work/scripts/review_batch.py <stem> ...` checks exact unique original spans, compares row requests and decisions, and creates labelled sheets from the saved crops. The main reader must read the returned account and inspect the image evidence, especially every proposed edit or uncertainty.
3. Resolve any remaining ambiguity with the manuscript and the supplied conventions. Do not insert a mathematical repair merely because it is correct. Do not correct incidental text not actually supplied by a table row. Main-reader amendments belong in the result's note/events.
4. `python work/scripts/review_and_commit.py commit <stem> '<specific review account>'` reconstructs from the original, writes the final page, rebuilds ordered tables and notes, then appends the prescribed UTC completion line. A page is not complete until this operation succeeds.

No OCR, PDF text layer, or text-recognition library has been used. Reader visual checks are optical comparisons, not mathematical proofs. Background mathematical claims must remain labelled as such. Refuted reading claims name a refined statement in the notes; event outcomes identify the page because some IDs recur.

## Timed preservation

The first line of `progress.log` is the actual start time in UTC. `python work/scripts/package_work.py checkpoint` creates a new numbered ZIP only when the next 45-minute boundary has arrived; otherwise it reports that the checkpoint is not due. It never overwrites an existing ZIP or includes earlier checkpoint ZIPs. After creation, save that exact ZIP durably with the current Library transfer helper and retain its receipt. Do not make extra checkpoint ZIPs at section or cote boundaries.

The current Library helper files were read from the cloud Library skill and written into `../.library_helpers_current/` for this environment. They are transfer infrastructure, not manuscript-processing scripts. Use the prescribed direct-create route for a single file below about 50 MiB, including xattr persistence in the same code-mode call; use the prepared-upload helper for larger files. Preserve checkpoint names and successful upload identities. If restoring in a new environment, re-extract the attached source ZIP once there and update packet source paths to that environment before resuming.

## Final gate

`python work/scripts/package_work.py verify --final` requires all 405 placements and all 309 reviewed pages, exact source-span reconstruction, matching hashes, original table order, and agreement of original pages with the immutable uploaded ZIP. `python work/scripts/package_work.py final` creates `../IM22_133-162-6.zip` with all current deliverables and documentation, excluding original attachments and checkpoint ZIPs. Save the final ZIP durably and offer it as the only download. No other file should be offered separately.

A focused TeX render attempt for the reversed inclusion arrow could not run because the installed pdflatex lacked its format file. The run does not claim compiled-page validation. The correction's direction, hook and label were checked against the crop and its TikZ-cd source.
