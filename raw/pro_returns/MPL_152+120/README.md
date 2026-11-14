# MPL_152+120

Complete diplomatic transcription and English research notes for the 38 supplied scans, in the requested order: **152/001–013**, then **120/001–025**.

## Main files

| File or directory | Contents |
|---|---|
| `MPL_152+120_transcription.tex` | Combined LaTeX fragment, without a preamble or document class; all 38 pages in order. |
| `pages/` | One audited LaTeX file for each scan. |
| `MPL_152+120_doubts.md` | Notation table first, complete doubt register, abbreviation glossary and legibility assessment. |
| `MPL_152+120_inventory.csv` | The exact eight requested columns; 734 elements, all marked `yes`. |
| `MPL_152+120_notes.md` | Authoritative research synthesis: 96 numbered items, four requested questions, detailed verification blocks, two worked appendices, and the two standing sections. |
| `progress.log` | Sequential completion and audit timestamps, checkpoints, freeze hashes, and final verification. |

The transcription was frozen at **2026-11-14 16:52:13 UTC**, before the contextual archive was opened at **16:52:25 UTC**. Its 38 page-file hashes and combined-file hash are in both the log and `qa_infrastructure/transcription.sha256`. Final verification confirms that all 39 remain unchanged.

## Uncertainty and coverage

The fragment contains **376 explicit `\unsure` occurrences** and **9 `\illegible` word-count marks**, estimating **16 unreadable words**. These counts describe the explicitly marked passages. The doubts file identifies the least secure passages and preserves alternatives in cancelled text, formulas, diagrams, drawings and marginalia.

The same primary reader inspected every supplied whole-page image and its halves, transcribed the pages in sequence without OCR, and performed the second image-to-text audit. Drawings are TikZ reconstructions. The inventory includes covers, reused machine printouts, page numbers, additions and deletions as well as the mathematical text.

## Research evidence

The main research file preserves the source and scope of each conclusion. The exact identification sought for the terms on 149/133 and the specific month of the sphere continuation remain unresolved in the bounded search. The positive findings include earlier explicit tubular constructions, Grothendieck's own gerbe calculation, exact compact-definable and Boolean-family comparisons, and the stated Shiota comparisons.

`research/` preserves the component drafts, per-item context searches, primary-source retrieval ledgers and mathematical review records. The main research file incorporates later locator and wording corrections. An earlier component draft or search record is evidence of the work at that stage; the main file is the final synthesis.

The supplied scans, source archives and contextual files are intentionally absent. Newly consulted public PDFs and images are also excluded; their URLs, page locations and selected source hashes are recorded. References to `context/` and `research_sources/` describe the working source locations and the evidence supplied or retrieved during research.

## LaTeX verification

The combined fragment compiled successfully under the auxiliary XeLaTeX wrapper. The rendering used for compilation diagnostics has 40 output pages for 38 source scans. The final compiler record contains one 0.76105 pt overfull-box warning on 152/010 and no missing-character or underfull-box warnings.

`qa_infrastructure/README.md` documents the wrapper and its dependencies. In that wrapper, colours mark page states, and the available underline fallback does not reproduce word wrapping; those rendering choices do not change the fragment. Compiler logs and structural reports are retained in the same directory.

The two read-only checks can be run from this extracted directory:

```bash
python3 qa_infrastructure/preflight.py check --require-combined
python3 qa_infrastructure/preflight.py verify
```

## Historical scripts and observations

`scripts/page_*.py`, `reading_observations.md` and some earlier QA records predate the final audit. **Do not regenerate the frozen transcription from those first-pass scripts.** The audited files in `pages/` and the combined fragment are authoritative. `audit_observations.md` records the subsequent image checks.

`scripts/assemble_research_notes.py` assembles only the research synthesis and does not write any transcription file. `scripts/pack_checkpoint.py` packages the deliverable tree while excluding ZIP files, symlinks and Python cache directories. The remaining scripts and logs are retained as work records.

