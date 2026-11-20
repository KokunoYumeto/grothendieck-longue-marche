# SP44_CW_36 — consolidated diplomatic transcription and record

## Scope and status

The assigned source is cote 36, scans 010–027 (18 pages), corresponding to witness H's pages 9–26. The exact completed scope is recorded by the `scan NNN done` lines in `progress.log`; a checkpoint may contain an unfinished current page. Only the files in `pages/` and `SP44_CW_36_transcription.tex` are the main reader's consolidated text. Independent files under `readers/` are evidence, not alternate final editions.

The source images, witnesses C and H, and sweep S were supplied with the task. No OCR, PDF text layer, recognition library, external source, published edition, or web research is used. This is an AI collation, not a claim of human verification. Source identity and image hashes are recorded in `SOURCE_MANIFEST.tsv`; the source attachments themselves are not included.

## Main deliverables

| File | Contents |
|---|---|
| `pages/` | One consolidated LaTeX fragment per scan, with the original witness-C filename. |
| `SP44_CW_36_transcription.tex` | Ordered concatenation of those page fragments, without a preamble. |
| `SP44_CW_36_changes.md` | Per-page decisions, C/H readings, three independent alternatives, crop evidence, uncertainty and counts. |
| `SP44_CW_36_collation.tsv` | Each substantive H-to-final difference, in the requested columns. |
| `SP44_CW_36_doubts.md` | Notation observations, remaining doubts, abbreviation expansions and legibility assessment. |
| `SP44_CW_36_inventory.csv` | Text blocks, displays, figures and individual interventions, checked against the consolidated text. |
| `SP44_CW_36_notes.md` | Page-specific English notes, source reservations, mathematical diagnostics and their limits. |
| `CHECK_EVENTS.tsv` | Actual mathematical checks and uses, with their stated scope; reading an assertion is not labelled a proof. |
| `progress.log` | UTC start, ordered page completions, checkpoints and final hash freeze/verification. |
| `SP44_CW_36_workflow.md` | Independent-reader procedure, evolving brief and crop counts. |

## Supporting record

`PREAMBLE.tex` is the supplied macro definition file. The transcription uses those macros and standard LaTeX/TikZ facilities. Structural checks are recorded under `validation/`; no TeX compilation is claimed.

`readers/scanNNN/R1`, `R2`, and `R3` contain each fresh reader's full page, report and structured return. `RUNS.tsv` records the runs and the metadata actually exposed. The main reader's `decisions/scanNNN.json` records the consolidated decisions; matching main-view records identify the crops actually inspected. `crops/` contains those derived local views and coordinate/processing sidecars. A repeated visible glyph is not silently normalized: notation observations stay subordinate to the ink of each occurrence.

Counts in the change log are counts of separately recorded loci, not a statistical error rate per word. A locus can differ from both witnesses. C-doubt confirmations and reader disagreements that leave the text unchanged are retained but do not inflate change counts. Actual deletion/insertion state and literal source typography are distinguished from equivalent macros in the two witness systems.

The scripts reproduce packaging, comparison and record formatting; they do not perform text recognition or choose readings. Page-local packets are reproducible from the supplied attachment with `scripts/prepare_packets.py` and are excluded from the archive because they duplicate witness input. Checkpoint ZIPs never contain earlier checkpoint ZIPs. The final archive contains the complete current record rather than only the newest pages.
