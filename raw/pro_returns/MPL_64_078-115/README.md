# MPL 64, scans 078–115

Diplomatic transcription and post-transcription research notes for the 38 supplied scans of Alexander Grothendieck's manuscript, Montpellier archive, cote 64.

## Main files

| File | Contents |
|---|---|
| `MPL_64_078-115_transcription.tex` | All 38 scans in order, as a LaTeX fragment without a preamble |
| `pages/` | One independently saved fragment per scan, numbered 078–115 |
| `MPL_64_078-115_doubts.md` | Notation table, 408 uncertainty entries, abbreviations and a legibility assessment |
| `MPL_64_078-115_inventory.csv` | 697 inventoried elements, all marked `yes` in the `transcribed` column |
| `MPL_64_078-115_notes.md` | 62 individual research notes, the requested thematic answers, authorial reservations, title sheets and page numbering, context comparisons and references |
| `CHECK_EVENTS.tsv` | 90 events distinguishing proof checks, independent proofs, computations, rechecked uses, background uses and refutations |
| `progress.log` | Page completion and audit times, the freeze, hashes, context opening, research and packaging records |
| `records/` | Detailed mathematical arguments, computation scripts and outputs, context-search records, note/event concordance, editorial working records and technical QA logs |

The supplied scans and context sources are not included. References to `context/` in the notes identify files in the original context ZIP. The archive contains no earlier checkpoint ZIP.

## Reading the transcription

The source preserves deletions, insertions, marginalia and doubtful readings through the editorial macros requested in the task. There are 405 `\unsure` occurrences and three `\illegible` occurrences; these uncertainty marks remain part of the final text. Six diagrams and six drawings are rendered in TikZ or `tikz-cd`. The uncertainty count is not an estimate of the total number of possible reading errors.

Authorial page numbers and archive foliation are kept distinct. The title sheet is scan 101. The manuscript restarts its page numbering at scan 102; no authorial page number has been supplied where none was visible. The doubts file describes the least secure readings, including small insertions, cancellations and several recurring mathematical glyphs.

All image reading and both transcription passes were performed by the main transcriber in one stream. Research contributions were delegated only after the transcription had been frozen. Research findings, corrections and suggested alternative readings therefore appear in the notes, not as changes to the manuscript text.

## Freeze and verification

The 38 page files and combined fragment were frozen at **2026-11-17 23:01:38 UTC**, before opening the context. Their 39 SHA-256 values are recorded in `progress.log` and `records/SHA256SUMS.frozen`. Final verification found every frozen hash unchanged.

The combined fragment is exactly the concatenation of each page file followed by one additional LF newline. The additional newlines are page separators; every page payload is byte-for-byte preserved. A diagnostic comparison against concatenation *without* those separators reported a difference, retained in `records/literal_concatenation_diagnostic.txt`. The assembly comparison is recorded in `records/final_delivery_qa.json`, and the final structural check is in `records/final_structural_qa.txt`.

The separate QA wrapper compiled successfully with XeLaTeX, with no missing-glyph errors. Its preamble is not part of the transcription. The wrapper uses colors to display editorial states and is intended for syntax inspection; it does not reproduce the physical manuscript layout. One long underline produced an overfull line in the fallback used when `ulem` was unavailable. Compilation and structural checks do not establish paleographic correctness or mathematical truth.

## Research and reproducibility

The main notes answer the cusp, congruence-level and Gauss–Manin/Cartier questions first. They distinguish manuscript assertions, authorial withdrawals, our deductions, supplied-context claims and unresolved comparisons. Full supporting arguments are in `records/research_root.md`, `research_algebra.md`, `research_b5.md` and `research_connections.md`.

The principal computation records are `moduli_check_results.json`, `verify_algebra_output.json` and `legendre_s20_certificate.json`, accompanied by their Python scripts. Finite examples are distinguished from general proofs. The Picard–Fuchs interpretation is explicitly restricted to characteristic zero; the characteristic-p polynomial and Cartier computations are separate.

`records/note_event_concordance.tsv` links every individual research note to its check events. `records/final_note_context_searches.json` and its text companion document an actual context search for every note. Earlier context results retain their supplied review status.

For technical rendering, run XeLaTeX on `records/qa_wrapper.tex` from the package root with the dependencies named in that file. For a hash-only verification from the package root, use `sha256sum -c records/SHA256SUMS.frozen`. The archival source fragments should remain unchanged.
