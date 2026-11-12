# Close of the second pass of *La Longue Marche* (12 Nov 2026)

Claude Opus 5.5, one agent, no sub-agents. Work folder: `second_pass/work_close_20261112/` (scripts, tables, logs;
`build/` holds the compile wrappers and logs and is not published).

## 1. Coverage

Every package of `PACKAGES.md` that is not superseded has a second-pass text: **116 packages, 1,588 scans** (cote
140-1: 2 packages, 37 scans; 140-2: 58 packages, 575 scans; 140-3: 41 packages, 696 scans; 140-4: 15 packages, 280
scans). Superseded and left out: LM_P068–LM_P071 (by the combined LM_P068-069 and LM_P070-071) and LM_P072–LM_P160 (by
the C3, C4 and C1 packages of 19 images).

- Each current text has a `\scanpage` line for every scan of its range (`build_index.py` checks this): no scan missing.
- LM_P057: the current text is `LM_P057api_checked.tex`, the second pass made over the API first pass of that package
  (no other second pass of P057 exists).
- Compilation, each current text in the check wrapper `answers/fixed/build/wrap.tex` (LuaLaTeX): **95 compile as they
  are; 21 compile after the reader build's mechanical LaTeX repairs** (`fix_tikzcd_in_macros.py`,
  `unwrap_gathered_diagrams.py`, `normalize_reader_text.py`, applied to a copy; the reading is unchanged): P02, P03,
  P04, P014, P016, P057, C3-359-377, C3-492-510, C3-511-529, C3-549-567, C3-568-586, C3-606-624, C3-682-696,
  C4-001-019, C4-020-038, C4-039-057, C4-058-076, C4-115-133, C4-172-190, C4-248-266, C4-267-280. Almost all are a
  tikz-cd inside a `\diagram{...}` argument without `ampersand replacement`, which the reader build repairs. The texts
  themselves were not changed for this (`retry_failed.py`, `retry_failed_run1.tsv`, `retry_failed_run2.tsv`).
- Two texts failed even after those repairs, on LaTeX errors of the second pass, and were repaired in a
  `_checked_fixed.tex` (LaTeX only, `latex_repairs.py`): LM_P065 (line 289: `\mathfrak S` in text mode
  inside `\deleted{\unsure{...}}`, now in `$...$`) and LM_C3-302-320 (`T_\alpha\capB'_0` read as one control
  sequence, now `\cap B'_0`). Both now compile as they are.
- Gaps: **none**.

## 2. Merge of the fix lists

The fix packages (`fixes/`, LM_FIX_01–16: 444 items with Pro's replacements in `answers/LM_FIX_*_fixes.csv`) were
traced item by item into the current texts (`fix_status.py` before the merge, `fix_outcomes.py` after;
`work_close_20261112/fix_outcomes_20261112.tsv` has every item and its outcome):

| Outcome | Items |
|---|---|
| In the second pass's input (applied to the fixed first pass, then checked by the second pass) | 300 |
| Already in, merged 8 Nov (`merge_fixes_into_checked.py`, `fuzzy_merge.py`) | 77 |
| The 33 of `merge_fixes_open.md`: outcomes of 12 Nov 11:05 UTC (12 applied, 3 rejected, 18 already in) | 33 |
| Nothing to merge: Pro keeps the `\illegible` mark, as the text does | 15 |
| Settled by the second pass (the description or mark the fix was for is resolved in the second-pass text) | 11 |
| Settled 8 Nov by hand (P038 circles, `manual_LM_FIX_03_P038_checked.py`) | 3 |
| **Applied now**, checked on the scan | 3 |
| **Rejected now**, the ink does not show the fix's reading | 2 |
| Open | **0** |

Applied now (each in a new `_checked_fixed.tex`, `apply_close_merge.py`):
- LM_FIX_11-022, LM_P046, scan 451 (140-2): the struck mark after `-z` is raised; now `\unsure{-z}^{\deleted{\illegible{1}}}`.
- LM_FIX_14-027, LM_P068-069, scan 107 (140-3): a `c` is legible after the hatched block; now `\deleted{\illegible{1}c}=\delta+c(\dots)`.
- LM_FIX_16-025, LM_C3-321-339, scan 329 (140-3): after the struck «v+w²=» only the strike line continues; the
  `\illegible{1}` operand is removed, as Pro gives it.

Rejected now (the second pass's reading stays):
- LM_FIX_03-020, LM_P042, scan 417 (140-2): the annotation in diagram (26) reads «comm.?» (c-o-m-m), not Pro's «canon.?».
- LM_FIX_14-026, LM_P068-069, scan 107 (140-3): the struck cluster after «S=» is longer than «ad»; the `\illegible{1}` stays.

No second-pass reading was undone. The twelve passes of 12 Nov afternoon needed no merge: no fix item touches cote
140-1, cote 140-4 from scan 134, or LM_P04; the ten items of LM_P05 were in its input (its first pass was the fixed
one), and the one not applied there (LM_FIX_04-002, the prism of scan 42) was drawn by the second pass itself (P05
change 10). In LM_P08 one fix in the input was reverted by the second pass; that is its reading and stays.

Current texts that are `_checked_fixed.tex`: 32 (P011–P014, P016–P019, P022–P040 from 8 and 12 Nov; P046, P068-069,
C3-321-339 by this merge; P065, C3-302-320 by the LaTeX repairs).

## 3. The current text

`second_pass/CURRENT_TEXT_INDEX.tsv`, one row per package in manuscript order (cote 140-1, 140-2, 140-3, 140-4): cote,
scans, images, the current text (`_checked_fixed` if it exists, else `_checked`), whether it is a fixed file, the
number of changes and of unresolved places from its `_changes.md`, how the unresolved number was obtained, the
numbers of `\unsure` and `\illegible` marks in the text, the changes and notes files, and the compile result.

Counting (`build_index.py`): changes = the data rows of the tables before the unresolved section (these agree with
every total the second passes reported); unresolved = the number the file states where it states one (15 packages),
else its per-scan counts, else its numbered items or rows, else its bullet items split at «;». The second passes wrote
this section in different forms, so the unresolved totals of 101 packages are counts by that rule, not the passes' own.

## Totals

| | Packages | Scans | Changes | Unresolved places |
|---|---|---|---|---|
| cote 140-1 | 2 | 37 | 42 | 33 |
| cote 140-2 | 58 | 575 | 3,028 | 1,758 |
| cote 140-3 | 41 | 696 | 1,443 | 1,363 |
| cote 140-4 | 15 | 280 | 377 | 482 |
| **All** | **116** | **1,588** | **4,890** | **3,636** |

The twelve passes of 12 Nov afternoon: 345 changes, 411 unresolved places. In the current texts: 17,117 `\unsure`
and 1,261 `\illegible` marks.

## 4. Publication

KokunoYumeto/grothendieck-longue-marche, `raw/second_pass/` (clone `raw_publish_20261111/grothendieck-longue-marche`,
pulled first: up to date at 4f06a92). Staged with `tools_local/stage.py` (spec `spec_LMSP_CLOSE.json`, written by
`make_spec.py`); the first name becomes «user» in every text file; privacy scan `tools_local/scan.py` before the commit.
Published: the checked text, changes, checked notes and prompt of the twelve passes of 12 Nov afternoon; the five new
`_checked_fixed.tex` (P046, P065, P068-069, C3-302-320, C3-321-339); `CURRENT_TEXT_INDEX.tsv`; this report; the close's
scripts and tables (`work_close_20261112/`). Crops, page images and the compile build files are left out.

Commits: see the end of this file.

## Not done

- The texts listed in §1 that compile only after the reader's mechanical repairs were not rewritten; the edition
  build applies those repairs.
- The unresolved counts of 101 packages are counts by rule (§3), not exact.
- The edition (`transcription/`, `notes/`, the readers and a release) is not updated: the second-pass texts after
  LM_P070-071 are in `raw/second_pass/` and in the prompts' attachments only.
