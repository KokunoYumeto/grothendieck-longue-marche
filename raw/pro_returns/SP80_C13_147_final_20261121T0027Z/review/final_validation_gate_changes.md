# Final validation gate changes

Only `scripts/validate.py` was changed, together with this change record. No page, report, assembled deliverable, progress entry or freeze record was modified.

## Changes

- Corrected recognition of `\begin{document}` and `\end{document}`, including whitespace around the environment name. The previous trailing word boundary failed after the closing brace.
- Required all eleven mandatory top-level deliverable files. Added exact, ordered headers and field-count checks for the collation, decisions, check events and inventory, and for all five kinds of second-reading TSV.
- Added check-event validation: every required field must be nonempty; dates must be valid ISO calendar dates; event types must match the six established types; provenance must contain at least three nonempty components with explicit effort and run information.
- Added optional `--final`. It requires exactly the 23 supplied page paths and the combined transcription in `review/frozen_hashes.json`, valid SHA-256 values matching the current bytes, a matching UTC freeze entry, every frozen hash in `progress.log`, and a subsequent dated unchanged-hash verification. Without `--final`, final freeze requirements are not imposed.

## Use

Run ordinary validation before freezing. After root creates and checks the final freeze, run `python edition/scripts/validate.py --final` before packaging, so the ZIP includes the logged unchanged-hash verification.

## Verification performed

The script parsed and compiled in memory. Twenty-two isolated checks passed using temporary fixture tables, synthetic page files and synthetic freeze records. These covered the corrected macro recognition, headers and field counts, invalid event dates/types/provenance, both argument modes, a valid 24-file freeze, missing or incomplete freeze records, missing or out-of-order verification entries, missing logged hashes and changed frozen bytes.

The edition's freeze script was not run. These fixture checks are not a claim that the final edition has passed validation; root's image adjudications and final validation remain separate.

The final gate additionally requires every canonical error_category to belong to the exact ten-category vocabulary. This closes the observed gap in which descriptive root shorthand could otherwise be omitted silently from the category totals. The original detail is retained as error_detail.
