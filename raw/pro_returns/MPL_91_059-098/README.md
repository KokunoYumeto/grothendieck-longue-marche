# MPL_91_059-098

This package contains the diplomatic transcription of the 38 supplied scans of cote 91, scans 059–098, excluding the two omitted blank scans 060 and 086.

## Deliverables

- `MPL_91_059-098_transcription.tex`: the combined LaTeX fragment, without a preamble.
- `pages/`: the 38 individual page fragments, in archive scan order.
- `MPL_91_059-098_doubts.md`: the shared notation table, all 299 uncertainty entries, abbreviation list, and limits of legibility.
- `MPL_91_059-098_inventory.csv`: 499 individually located elements, all marked transcribed.
- `MPL_91_059-098_notes.md`: 68 research notes, context and literature comparisons, the standing unverified-step and title/count registers, and the results-register disposition.
- `progress.log`: completion and audit times, the pre-context freeze, hashes, checkpoint history, and final verification.

## Reading and provenance

The transcription was read visually in one sequential stream, without OCR or delegated page transcription. Each supplied whole image and its two halves were inspected, followed by a second audit of every retained page. Uncertain readings remain marked; the least secure passages are identified in the doubt register.

The page fragments and combined fragment were frozen at **2026-11-17 21:07:18 UTC**, before context contents were opened at **21:07:29 UTC**. Their 39 SHA-256 values are in `records/frozen_sha256.json` and `progress.log`. Final verification checks those exact bytes. Context-led alternative readings appear only in the research notes.

The notes distinguish the source's statements, first-pass context leads, published comparisons, and editorial mathematical examples. The examples are not originality claims. Post-freeze mathematical checking did not delegate manuscript reading or alter the frozen transcription.

## Work records

The `records/` directory preserves the visual audit, notation work, pre-context observations, context-query index and short search excerpts, mathematical checks, validation records, checkpoint receipts, and scripts. `records/doubts.jsonl` and `records/inventory_before_final_reconciliation.csv` preserve earlier working states; the final doubt register, final inventory, and `records/final_doubts.json` supersede them where readings changed. The attached scans, input ZIPs, and complete context files are not included.

## LaTeX syntax check

`records/compile_harness.tex` provides a neutral syntax-check wrapper using standard LaTeX, AMS packages, TikZ and tikz-cd. Run it with `records/` as the working directory. It deliberately renders the state-of-page macros neutrally and is not a facsimile or an editorial display style. The recorded successful run produced 39 DVI pages: one cote heading plus 38 scan pages. The requested deliverable remains the LaTeX fragment, with no added preamble.

`records/final_validate.py` can repeat the read-only checks of the frozen files, scan list, inventory, note-query coverage, and audit log. It writes its result only when explicitly given `--write-report`. The other scripts are historical work records and may contain paths from the original workspace.
