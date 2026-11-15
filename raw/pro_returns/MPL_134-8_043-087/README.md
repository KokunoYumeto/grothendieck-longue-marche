# MPL_134-8_043-087

## Authoritative deliverables

- `MPL_134-8_043-087_transcription.tex`: the diplomatic LaTeX fragment, with all 44 supplied scans in order and no document preamble.
- `pages/`: one frozen fragment per scan, numbered 043–087 with 060 absent from the supplied images.
- `MPL_134-8_043-087_doubts.md`: the notation table, abbreviation list, legibility statement, and all 457 recorded doubt occurrences, with page-file locations.
- `MPL_134-8_043-087_inventory.csv`: 1,240 inventory rows, using the seven requested element kinds and `transcribed=yes` throughout.
- `MPL_134-8_043-087_notes.md`: the integrated English research notes, including the source's unverified steps, revisions, support-sheet titles and pagination, comparisons with *Pursuing Stacks*, and item-by-item context-register mappings.
- `progress.log`: page completion and audit times, all frozen hashes, context-opening time, checkpoint events, and final verification.

The `records/` and `scripts/` directories document the work. Files containing `draft`, `proposed`, or `suggested` in their names are historical working records; they are not alternate authoritative transcriptions. The notes file above is the integrated research deliverable. Supplied scan images, input archives, context source files, generated image crops, and TeX caches are not included.

## Freeze and research boundary

The transcription was made by the primary reader in one ordered stream, using the whole-page image and supplied halves, followed by a second audit of every page. No OCR or other image-to-text software was used on the scans, and no transcription was delegated. Auxiliary work on LaTeX syntax and inventories used the written text; research comparisons were delegated only after the transcription freeze.

All 44 page files and their exact concatenation were frozen at **2026-11-15 11:49:57 UTC**. The combined SHA-256 is:

```
3f85b51570feeb779ae2fd3d9e338ea8f90078fbce6e6e406722a402d6bc8c79
```

The context contents were opened at **2026-11-15 11:50:22 UTC**. Earlier intake had listed the context archive's member names and sizes without reading their contents; `records/context_access.json` and the log preserve the boundary. The later context prompted reading questions only in the notes; no frozen transcription file was revised afterward.

## Validation and its limits

`scripts/freeze_and_verify.py` verifies all 45 frozen hashes. `scripts/assemble_and_validate.py --verify-existing` verifies the exact concatenation and page sequence. The doubts extractor and its independent integrity checker verify each recorded occurrence against its exact character and byte location in the frozen page files. These are structural checks, not replacements for the visual readings or independent certification of uncertain words.

The actual page fragments and the exact combined fragment were compiled using the separate QA harness in `scripts/latex_qa_preamble.tex`. The final installed harness corrects paragraph handling around diagrams without changing the source; its final record reports a successful compile, no missing-character diagnostic, and one 0.19052 pt rounding overrun on scan 050. The raw engine's default `pdftex.map` notice is documented, together with the explicitly loaded installed font maps, in `records/latex_qa_readme.md` and `records/latex_qa_combined_final.json`.

The QA preamble is supplied as an aid for inspection; it is not part of the requested LaTeX fragment. Its rendered pages are a transcription layout, not facsimiles of the original sheets. For doubtful ink, use the original supplied images together with the occurrence-by-occurrence doubts table; contextual conjectures and mathematical corrections have not been substituted into the frozen text.

## Research citations

Research notes cite the supplied context by filename, section, statement ID, manuscript page and printed page where available. Statuses in the result registers remain attributed claims unless their entries explicitly record review. The supplementary coverage manifests preserve source IDs, search scope, and mappings; absence findings concern this supplied 44-scan range and make no assertion that the mathematical subjects have no relationship.

The archive contains complete work records so that a later reader can distinguish the diplomatic source, its doubts, pre-freeze revisions, post-freeze research questions, and the provenance of every technical check.
