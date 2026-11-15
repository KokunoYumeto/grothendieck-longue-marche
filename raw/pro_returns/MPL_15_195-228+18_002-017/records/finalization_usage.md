# Mechanical finalization helper

`records/finalize_mechanical.py` prepares derived files after the primary reader has finished all 49 page fragments and corrections. It performs no manuscript interpretation, image reading, OCR, contextual research, visual audit, or freezing.

## Input format inspected

The existing `records/record_page.py` writes each `records/C_NNN_inventory.json` as a JSON list of eight-field lists, in the same order as the CSV columns:

```text
cote, scan, sheet_kind, element, kind, position, first_words_or_objects, transcribed
```

The helper retains every field of manual `text`, `display`, `diagram`, and `drawing` rows. It discards prior generated `deletion`, `insertion`, and `margin note` rows and rebuilds these from final page macros. The original per-page JSON records are not changed.

## Commands

From the deliverable directory, first perform a dry run:

```bash
python records/finalize_mechanical.py
```

The dry run requires all 49 expected page files and per-page inventory JSON records. It reports counts and planned output paths but writes nothing.

Before freezing the transcription or opening context, write the derived files:

```bash
python records/finalize_mechanical.py --write
```

The write mode refuses to proceed if `progress.log` already contains an event beginning `transcription frozen` or `context opened`. It does not add either event and does not write audit or completion log entries.

## Outputs

1. `MPL_15_195-228+18_002-017_transcription.tex`: exact byte concatenation of the 49 page fragments in the required order, without editing any page or adding a preamble. The current page-writing helper supplies the two cote boundary markers.
2. `MPL_15_195-228+18_002-017_inventory.csv`: preserved manual rows plus regenerated alteration/marginal rows for every page.
3. `records/final_doubt_rows.jsonl`: every final `unsure` and `illegible` macro, with page filename, cote, scan, TeX line and column, character offset, raw argument, parsed reading and alternatives, and mechanically assigned confidence.
4. `records/final_doubt_table.md`: the same doubts as a Markdown table suitable for incorporation into the main doubts deliverable.
5. `records/finalization_report.json`: counts, per-page row counts, input page hashes, and the combined hash. This is a mechanical report, not a frozen-transcription declaration.

The main doubts document, its notation table and abbreviation prose, the historical `records/doubt_rows.jsonl`, the page fragments, original per-page inventory JSON, and `progress.log` remain untouched. To deliver a complete main doubts document, the primary reader should incorporate the regenerated table there while preserving the prose and notation material.

## Parser and confidence rules

The parser tracks balanced braces, masks comments and verbatim bodies, distinguishes escaped control symbols from grouping braces, and records nested target macros. Alternatives are split only at literal, unescaped `|` characters at brace depth zero. A `|` inside a braced formula or a nested macro is retained within that reading; `\|` is not an alternative separator. The exact original macro argument is retained in JSON even where presentation fields suppress comments or collapse whitespace.

Every `unsure` row receives `medium`; every `illegible` row receives `low`. These are the requested mechanical assignments, not renewed judgments of handwriting. For an illegible entry the reading column retains the full `\illegible{n}` marker. TeX line numbers refer to the individual page file, not to the combined transcription.

For inventory rows, original manual identifiers and row order are preserved. Regenerated auto rows follow each page's manual rows, in TeX occurrence order, with fresh numeric identifiers above the largest retained manual identifier. This avoids assigning visual positions from prose labels mechanically; the primary reader remains responsible for the page inventory's substantive completeness and visual ordering. The `first_words_or_objects` field uses the macro argument with whitespace collapsed and a maximum of 350 characters, matching the existing helper's excerpt convention.

## Verification and limits

The helper checks the exact 49-file set, page/cote marker sequence, brace balance, inventory schema and page identity, consistent sheet kinds, `yes` status, and unchanged page-file hashes during output preparation. Output files are staged and replaced individually only after all derivations succeed. The helper does not certify that any word, symbol, diagram, deletion, or insertion has been read correctly or that every visual element has been inventoried.

Preparation included a syntax check and synthetic checks for nested macro arguments, comments, escaped vertical bars, escaped braces, and escaped backslashes. No real page content was read or finalization output generated during this support task.
