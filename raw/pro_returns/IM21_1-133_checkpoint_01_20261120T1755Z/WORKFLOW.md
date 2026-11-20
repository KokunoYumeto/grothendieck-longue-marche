# Scope and audit trail

The supplied correction table determines the page order and the scope of every edit. Three readers receive one page at a time, in first-appearance order, with the next page sent to the first reader free. `dispatch.tsv` records these assignments. Each reader inspects the scan visually and supplies `proposals/<page>.json`. The main reader reviews the return, adjudicates uncertainties, and alone commits the page and ledgers. No OCR or text-recognition system is used.

`review_records/` records the accepted decisions, source and edited SHA-256 hashes, review time and check events. The placement ledger is always rebuilt in the original correction-table order, even when pages finish in another order. The input has 405 rows but 372 distinct statement IDs: IDs recur on different pages. Row identity is the combination of ID, cote and scan; every occurrence is retained. An `a` row records a unique span from the original page; its replacement changes only that target. Identical corrections to the same span are applied once. Other decisions have empty find/replace fields. Existing CRLF line endings and unrelated bytes are preserved.

Visual agreement with ink does not establish the truth of a mathematical assertion. Check events state their scope. Proposed mathematical repairs remain background unless a separate check is expressly recorded. The notes retain authorial slips/refinements, missing targets and unsettled readings. For b decisions, the proposed correction is also quoted verbatim from the supplied row as unproved background, so its full intended mathematical refinement remains available. Where a requested omission remains uncertain, an empty alternative after the separator in \unsure{reading|} explicitly means no transcribed mark; existing visible-reading alternatives are retained. A doubtful reading can be fully adjudicated as a diplomatic decision by keeping alternatives in an in-place uncertainty macro; it does not become a certain reading.

The main reader resolved early newline normalization before the first checkpoint. The associated review records include the byte-preservation audit events. The original attached source files were never changed.

## Resume from a checkpoint

Restore the latest checkpoint into a working directory such as `IM21_work`. Restore the original attached inputs into the sibling `source` directory. Attached inputs and earlier checkpoint ZIPs are deliberately not embedded. Regenerate working page packets with `python scripts/prepare_packets.py`; these duplicate the attached content and are deliberately excluded from the archive. The paths in regenerated packets reflect the current location. Use `python scripts/workflow.py status` and `dispatch.tsv` to identify completed, proposed and outstanding pages. Preserve existing completed decisions and review records; reassign only work not completed or recoverable.

Continue using the original prompt and `READER_INSTRUCTIONS.md`. When the environment path changes, substitute the new working path in reader assignments. `python scripts/audit.py` checks current accounting and exact byte preservation against the restored original inputs. Use `--final --save` only after all 405 rows and 310 pages are complete.

## Checkpoint timing and packaging

Work began at the UTC time on the first line of `progress.log`. Checkpoints are due every 45 minutes from that time, under fresh numbered names, and at no other times. The package script refuses an existing ZIP path. Each checkpoint includes every current deliverable, crop, proposal, review record, script and workflow document. It excludes attached inputs, generated per-page packets, Python caches and all ZIPs. Checkpoints are saved durably; earlier ones are never overwritten or included in later ones. The final archive contains the complete current work.

`python scripts/workflow.py package <new-absolute-zip-path>` packages and checks ZIP CRCs. This command alone does not perform durable upload; the current Library upload helper performs that step. Upload receipts, when present, identify saved checkpoints without embedding them.
