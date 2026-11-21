# SP89_C13_149+150 — Diplomatic transcription and evidence

All 25 manuscript pages have a consolidated reading, an independently fixed second reading and completed root crop adjudication. The accepted text preserves source spelling, abbreviations, punctuation, notation, revision states and local uncertainty. Mathematical diagnostics and proposed repairs belong to the notes; they do not replace written ink.

## Completion record

| Measure | Final count |
| --- | ---: |
| Pages / independently audited pages | 25 / 25 |
| Fixed comparison boxes | 560 |
| Nonidentical boxes / token-edit spans | 472 / 2,546 |
| Boxes revised after adjudication | 194 |
| Local witness-collation entries | 953 |
| Entries differing from C / from H | 502 / 826 |
| High / medium / low confidence entries | 522 / 276 / 155 |
| Original mark decisions | 195 |
| Original marks: first / alternative / other / undecided | 82 / 6 / 20 / 87 |
| Inventoried page elements | 679 |
| Preserved crop PNGs | 1,110 |

These are different units. A box may contain several differences; a collation entry may differ from both witnesses. A resolved original doubt is counted as a recorded certainty decision even where its preferred letters survive. Added uncertainty alone is not counted as a new correction against C. These counts are not witness error rates or a guarantee that every unmarked reading is certain.

The corpus is cote 149 scans 130–136 and cote 150 scans 002, 003, 004, 005, 007, 008, 010, 012, 013, 014, 015, 016, 017, 018, 019, 020, 023 and 024. Scan numbers, author foliation, later thin foliation and H’s page numbering remain distinct.

## Reading the files

| Material | Role |
| --- | --- |
| `pages/<page>.tex` and `SP89_C13_149+150_transcription.tex` | Accepted LaTeX fragments, without a preamble, in the specified page order. |
| `_changes.md` and `_collation.tsv` | C/H readings, accepted readings, crop evidence, coordinates and confidence. `codex_reading` in the TSV means witness C. |
| `decisions.tsv` | All 195 original mark IDs in source order. Here `first` means the mark’s first candidate, not the later fixed first-reader file. |
| `_doubts.md`, `notation.md`, `_inventory.csv` | Notation, unresolved alternatives, abbreviation explanations, comparative legibility and the complete element inventory. |
| `_notes.md`, `CHECK_EVENTS.tsv` | Source accounts and mathematical checks, with their actual hypotheses and limitations. Visual audits and source-comparison events are recorded separately in page metadata. |
| `_hand_log.md`, `_sheet_feedback.md` | Local handwriting habits, recurring errors and category counts. |
| `second/` | Fixed box lists, first/second readings, comparisons, root decisions, adjudications and application records. |
| `reports/`, `scripts/`, `progress.log` | Current reports, historical drafts/reviews, protocols, verification receipts and dated progress. |
| `crops/` | Every saved evidence frame, including overlapping and superseded crops. |
| `packaging/`, `MANIFEST.tsv`, `checkpoints.tsv` | Pixel/encoding receipts, archive methods, final entry hashes and checkpoint history. |

Filenames beginning `_` above share the `SP89_C13_149+150` prefix. Paths are relative to the extracted archive. Some historical records retain `work/` or the original workspace prefix.

## Fixed readings and later changes

The first and second TSVs were fixed before their comparison. Their disagreement with the accepted source is intentional and preserves independent provenance. Comparison metadata binds the input files by SHA256. Every one of the 472 nonidentical boxes has a root decision. The accepted source includes those decisions plus narrowly documented encoding and integration repairs.

Historical drafts, first-reading reports and builders remain provenance. **Do not rerun old builders to reconstruct the final edition, or rewrite fixed readings to match the final source.** Source-formatting repairs and metadata synchronizations have separate receipts. The final source freeze records all 25 page files plus the combined fragment in `reports/frozen_transcription.json` and `progress.log`; the subsequent unchanged-hash entry verifies those 26 files. Structural and final audit checks are documented in `reports/structural_verification.json` and `reports/final_verification.json`.

## Crops and extraction

All 1,110 crop paths are preserved. The attached original scans/witness files, prepared half-page images and previous checkpoint ZIPs are excluded as requested. Reading-time rotation, enlargement or contrast adjustment is distinct from later storage encoding.

The final ZIP uses Deflate and **ZIP BZIP2, method 12**. Use an extractor that supports method 12. The decoded images are ordinary PNGs. Some PNGs use uncompressed internal scanlines so that outer BZIP2 compresses them more effectively. The extracted crop PNGs therefore occupy **3,471,374,346 bytes (about 3.47 GB)**.

Every staged crop was compared against its saved reading-time original for dimensions and exact decoded RGBA bytes. The archive verifier binds those staged hashes to the delivered entries. Pixel equality does not mean PNG byte identity, or identity with the source JPEG before reading-time transformations. `packaging/encoding_receipts.jsonl`, `packaging/pixel_verification.jsonl`, `packaging/pixel_verification_summary.json` and `packaging/ZIP_METHODS.tsv` state the original/delivered byte hashes, dimensions, decoded-pixel bindings and per-entry compression method. `MANIFEST.tsv` hashes the delivered bytes. The manifest does not hash itself.

## LaTeX integration and checking limits

Use the original attachment’s `SP89_C13_149+150_texts/PREAMBLE.tex`. A separate driver can contain:

```tex
\input{../SP89_C13_149+150_texts/PREAMBLE.tex}
\begin{document}
\input{SP89_C13_149+150_transcription.tex}
\end{document}
```

Adjust the path to the supplied preamble. No TeX compilation or rendered-layout verification was performed, as instructed. Static integration repairs group two uncertain mathematical atoms before following superscripts and use explicit ampersand replacement in diagram matrices. Five diagram-environment conversions preserve the accepted objects, literal cells, coordinate strokes and cancellation layers; they introduce no new reading. The detailed source before/after receipts document these repairs. An unreadable mathematical alternative on scan005 is encoded with a mathematical doubt and explained in prose, without using the unreadable-prose macro inside the formula.

The work used direct visual reading, without OCR or external textual research to fill gaps. The mathematical event record certifies only the checks it actually describes; it is not a proof of every manuscript claim.

## Explicit workflow limitations

Several fixed boxes clipped adjacent context or crossed another writing direction. `reports/audit_box_scope_check.md` records how wider saved or native frames resolved those scope issues without altering the fixed comparisons. In particular, **150_scan024 P23** inadvertently duplicates most of P16 and supplied no new reading. It is retained as documentation and is not independent confirmation. P22’s ascender completion is separate.

The final user-facing deliverable is the single archive **`SP89_C13_149+150.zip`**. Its complete-archive hash, extraction/CRC verification and persistence receipt are recorded externally after creation; a ZIP cannot contain a receipt hashing its own final bytes.
