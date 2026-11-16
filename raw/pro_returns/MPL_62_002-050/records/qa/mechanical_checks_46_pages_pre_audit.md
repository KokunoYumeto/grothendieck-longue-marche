# Mechanical compilation of all 46 saved fragments before completion of the visual audit

All 46 expected page files were present and compiled together successfully with LuaLaTeX at 2026-11-16 18:33:44 UTC. The successful run used snapshot copies and left every page file unchanged. The primary reader's visual audit was in progress; this run is not a final frozen-transcription check and does not constitute any delegated reading or audit of the images.

The source hashes and compilation result are recorded in `compile_46_pages_pre_audit.json`; the corresponding console log is `compile_46_pages_pre_audit.log`. The harness loads TikZ `shapes.geometric` for ellipse nodes. No LaTeX syntax error was found. The previously reported raw math-mode `é` in scan019 remains a missing-glyph warning in this snapshot; see `mechanical_checks_38_pages.md` for the exact source fragment and the proposed encoding-only adjustment.

The structural validator at this stage found 46 page files, 819 inventory rows and 46 done entries, with no brace, environment, editorial-macro, or inventory errors or warnings. Audit entries were still being added by the primary reader. Those counts do not establish completeness against the manuscript.

## Consolidated records

`scripts/consolidate_doubts.py` generates the main doubts Markdown from `records/doubts.jsonl` and places the content of `records/notation.md` at the top as a mechanical table. It preserves the recorded readings, alternatives and confidence values, without interpreting them. The legibility section is explicitly provisional and must be replaced or finalized by the primary reader after the visual audit. The abbreviation section is also a review placeholder.

`abbreviation_candidates.md` and `abbreviation_candidates.json` contain automatically extracted lexical candidates and exact source locations. They assign no expansions. Sentence-final full words, initials, mathematical symbols and TikZ dimension tokens are possible false positives; only the primary reader's reviewed items belong in the final abbreviations list.

If additional doubt or notation records are added during the audit, rerun `consolidate_doubts.py` **before** manually finalizing the legibility and abbreviation sections: regeneration overwrites the generated doubts Markdown. It does not modify the JSONL, notation source, transcription, inventory, or log.

No ZIP was created or uploaded in this mechanical-support step. In particular, the first hourly checkpoint remains due at 18:40:09 UTC under the primary agent's control.
