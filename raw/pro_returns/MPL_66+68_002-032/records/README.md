# Work records

The authoritative deliverables are the four named files at the ZIP root, the frozen `pages/` files, and `progress.log`. The combined transcription is the byte-for-byte concatenation of the page files in scan order. The input scans, attached ZIPs, and supplied contextual source files are deliberately excluded from the deliverable ZIP.

## Reading and revision records

- `precontext_observations.md`: page-by-page research seeds recorded before context access.
- `audit_observations.md`: the complete second-reading changes, final cross-page notation comparison, and subsequent metadata clarifications. Later contextual reading questions never changed frozen TeX.
- `writeNNN.py` and `record_page.py`: historical first-pass save commands. They are records of work, not replacements for the audited page files; do not rerun them over the final edition.
- `audit_page.py`: the second-reading helper. It logged edits and audit times when the pages were not yet frozen.
- `write_doubts.py`: historical doubt-table generator with the root reader's confidence judgments. The final Markdown includes additional abbreviation-list QA; it is authoritative.
- `extract_doubts.py` and `doubt_occurrences.json`: balanced mechanical extraction of all 277 doubt macros, including exact page-file locations and source hashes. It does not assess handwriting.

## Research review and computations

- `game_research_review.md` and `convolution_research_review.md`: advisory post-freeze reviews of the frozen text and supplied context; the main notes incorporate the selected and checked findings. Their local item numbering is separate from the main notes and from RESULTS_STATE IDs.
- `convolution_examples.py` and `convolution_examples.json`: exact finite arithmetic for the examples discussed in the main research notes. General theorems and palaeographic readings are not established by those checks.
- `final_mechanical_review.md`: final structural and bookkeeping review, including any later qualification noted before final packaging.
- `validate_package.py`: reproducible mechanical checks; run `python3 records/validate_package.py . --mode final --hashes` from the extracted ZIP root.
- `library_file_transfer.py`: transfer helper retained as a record of the requested durable checkpoint/final-file save. It has no role in reading or mathematical analysis.

The frozen page hashes in `progress.log` are the integrity reference. A historical script, contextual modernization, or advisory note must never be used to silently overwrite the transcription.
