# Raw research outputs on *La Longue Marche* and the manuscripts around it

This folder holds raw research outputs, not edited for publication:

- the answers of GPT-6 Astra (ChatGPT Pro mode) to four research prompts on *La Longue Marche*: the group schemes
  and schematic envelopes of §§48–50 (LM1), the equation of loops of §§36–47 (LM2) and the Teichmüller tower (LM3,
  LM3b), with the reviews of LM3 and LM2 by Claude Fable 5.2;
- first-pass transcriptions by GPT-6 Astra (ChatGPT Pro mode) of seven packages of Grothendieck's manuscript notes from
  the Montpellier archive, cotes 146, 147 and 149, which the archive groups with *La Longue Marche*, with sample checks
  of two of them by Claude Opus 5.5;
- the prompts with the full list of what was attached to each, the working notes, and the scripts that built the
  prompts and the archive packages;
- second passes of the transcription of *La Longue Marche* itself, against the archive's scans, that are not yet in
  the edition's `transcription/` and `notes/` folders, with their prompts and scripts (`second_pass/`, described at
  the end of this file).

How this was done, return by return, is in the section "Raw research outputs (11 November 2026)" of
[../methodology/METHODOLOGY.md](../methodology/METHODOLOGY.md).

- Each paper and transcription in `pro_returns/` is AI-produced by GPT-6 Astra (ChatGPT Pro mode). The date of each
  return is given below.
- The reviews of `LM3_TEICHMULLER_TOWER` and `LM2_LOOP_EQUATIONS` are by Claude Fable 5.2; the two sample checks of
  the archive transcriptions are by Claude Opus 5.5.
- The second passes in `second_pass/` are by Claude Opus 5.5, one subagent per package, over the first pass by
  GPT-6 Astra (ChatGPT Pro mode).
- The labels Proved, Refuted, Known and Open are the model's own. The reviews give the verdicts checked so far;
  statements the reviews do not cover are unchecked.
- No priority or novelty is claimed.
- The programs in the returns (the `code/` folders and the other program files) are published as returned, with
  their data and outputs; we have not run them. The reviewer's own programs are in
  `reviews/LM3_TEICHMULLER_TOWER/checks_author/` and `reviews/LM2_LOOP_EQUATIONS/checks_author/`, with their outputs.
- In these copies the first name of the user who ran the project is replaced by "user", local paths included, and
  e-mail addresses are replaced by "[e-mail address removed]". Nothing else in the files is changed. LaTeX auxiliary
  files, Python caches and compiled binaries are not included. The background zips are not uploaded as zips: their
  contents are listed file by file in `prompts/<name>/ATTACHMENTS.md`, with a link to each of our own files and the
  citation and address of each paper by other authors, and of each archive scan, which are not re-published here.

To the extent that we hold any rights in these AI-produced texts, they are dedicated to the public domain under CC0 1.0.

## Folders

Dates are those of the return (UTC).

| Folder | What it is | Date | Reviewed |
|---|---|---|---|
| `pro_returns/LM1_GROUP_SCHEMES/` | Answer to the prompt on the group schemes `M_{ρ,σ}` over `Z` and the schematic envelopes of discrete groups (§§48–50). The model's workspace disconnected during the final assembly and it wrote every file into the chat as text: these files are split by script from the text copy of the chat of 21:03 UTC (`chat_text_copy_2026-11-11T2103Z.md`, beside them; the script and the log of the split are in `tools/lm1_text_copy/`). The model kept working after this copy (on A.10 and a citation of Stix); that part is not included | 11 Nov 2026 | not yet |
| `pro_returns/LM2_LOOP_EQUATIONS/` | Answer to the prompt on the equation of loops in types (0,3) and (1,1): Grothendieck's conditions on the image of Galois, against the Grothendieck–Teichmüller relations (§§36–47) | 11 Nov 2026 | yes (`reviews/LM2_LOOP_EQUATIONS/`) |
| `pro_returns/LM3_TEICHMULLER_TOWER/` | Answer to the prompt on the Teichmüller tower, its profinite forms and the "conjecture fondamentale" (§§19, 21, 26–30, 32–36) | 11 Nov 2026 | yes (`reviews/LM3_TEICHMULLER_TOWER/`) |
| `pro_returns/LM3b_TEICHMULLER_PUSH/` | Answer to the second prompt on the tower: the rows the first answer left open, and his statements derived from theorems that were only cited | 11 Nov 2026 | not yet |
| `pro_returns/MPL_147_003-047/` | First-pass transcription, cote 147, scans 3–47 | 11 Nov 2026 | sample check of eight pages (`reviews/MPL_147_003-047/`) |
| `pro_returns/MPL_147_048-137/` | First-pass transcription, cote 147, scans 48–137 | 11 Nov 2026 | sample check of eight pages (`reviews/MPL_147_048-137/`) |
| `pro_returns/MPL_147_138-190/` | First-pass transcription, cote 147, scans 138–190 | 11 Nov 2026 | not yet |
| `pro_returns/MPL_149_091-136/` | First-pass transcription, cote 149, scans 91–136 | 11 Nov 2026 | not yet |
| `pro_returns/MPL_146_001-099/` | First-pass transcription, cote 146, scans 1–99 | 11 Nov 2026 | not yet |
| `pro_returns/MPL_146_100-134/` | First-pass transcription, cote 146, scans 100–134 | 11 Nov 2026 | not yet |
| `pro_returns/MPL_149_001-090/` | First-pass transcription, cote 149, scans 1–90 | 12 Nov 2026 | not yet |
| `reviews/` | The reviews of `LM3_TEICHMULLER_TOWER` and `LM2_LOOP_EQUATIONS` with the reviewer's programs; the two sample checks with the checked pages corrected (`pages_checked/`) and the list of page images they used (`IMAGES.md`) | 11–12 Nov 2026 | — |
| `prompts/` | Each prompt (`<name>/PROMPT.md`) with `ATTACHMENTS.md`, `attached/` (our own attached files not published elsewhere in this repository) and `work/` (background notes, manifests, earlier versions); the index and overview of the Longue Marche prompts (`README.md`, `OVERVIEW.md`), their shared second half (`_COMMON_BLOCK.md`) and the record of their rewrite (`work/`) | 10–11 Nov 2026 | — |
| `tools/archive/` | The scripts that download the archive's scans, enhance the pages and build the transcription packages, and the transcription prompt template | 10–11 Nov 2026 | — |
| `tools/prompts/` | The scripts that rewrote and packaged the Longue Marche prompts | 11 Nov 2026 | — |
| `tools/lm1_text_copy/` | The scripts that recovered the text copy of the LM1 chat and split it into the files of the answer, with the log of the split (every line left out, with its text) | 11 Nov 2026 | — |
| `second_pass/` | Second passes of the transcription that are not yet in the edition, with their prompts and scripts, and the fixes merged by hand on 12 Nov (section "Second passes" below) | 12 Nov 2026 | — |

## Second passes (`second_pass/`)

The method is section 3 of [../methodology/METHODOLOGY.md](../methodology/METHODOLOGY.md). For each package one
subagent (Claude Opus 5.5) reads the first pass line by line against the archive's scans, enlarged where the hand is
hard, and against the earlier transcriptions used as witnesses. It writes `LM_<KEY>_checked.tex` (the corrected
transcription), `LM_<KEY>_changes.md` (each change with its evidence and confidence, the places still unresolved, the
witnesses' own errors) and `LM_<KEY>_notes_checked.md` (the first pass's research notes checked against the corrected
text, and its own notes). Its prompt is `PROMPT_LM_<KEY>.md`. The edition's `transcription/` and `notes/` hold these
files for the packages up to `LM_P070-071` (cote 140-3, scan 130). The files here are in no release yet.

### 12 November 2026

The pilot packages of cote 140-2 (first pass of prompt version 1). Claude Opus 5.5, subagent, 12 Nov 2026:

| Package | Scans | Changes (high, medium, low) | Places unresolved | First-pass notes | Own notes |
|---|---|---|---|---|---|
| `LM_P06` | 51–60 | 68 (14, 42, 12) | 67 | 14 kept with corrections, 1 sharpened, 7 kept as they were, none dropped | 10 |
| `LM_P07` | 61–70 | 69 (18, 35, 16) | 57, 26 of them in struck-through text | 12 kept, 15 corrected, none dropped | 6 |
| `LM_P08` | 71–80 | 63 (13, 32, 18) | 35 | 19 kept, 4 corrected, none dropped | 3 |
| `LM_P09` | 81–90 | 70 (18, 34, 18) | 51 | 27 kept, 10 corrected, none dropped | 5 |
| `LM_P10` | 91–100 | 57 (2, 37, 18) | 60 | 17 kept, 6 corrected, none dropped | 3 |

`work_LM_P08/` and `work_LM_P10/` hold the scripts these two passes wrote (crops, a check of the TeX) and the wrapper in
which each compiled its text; `work_LM_P10/PROGRESS.md` is that pass's own record. The other three wrote crops only.

The fixes merged by hand. Claude Opus 5.5, subagent, 12 Nov 2026: `merge_fixes_open.md` lists the 33 fixes from the
fix packages (METHODOLOGY.md, "Fix packages and the strict prompt"; cote 140-2, scans 110–400) that the scripted merge
of 8 Nov had not placed in the second-pass texts. Each
was checked against its scan, and the outcome is written after it: 12 applied, 3 rejected (the ink does not show the
fix's reading), 18 already in. The twelve texts that changed are `LM_<KEY>_checked_fixed.tex` of P011, P013, P017,
P019, P022, P024, P025, P026, P032, P033, P034 and P035 (scans 101–350); before the merge they were
`transcription/140-2/LM_<KEY>_checked.tex` of this repository. `work_merge_20261112/` holds the scripts, the dump of
each fix with the text around it (`open_dump.md`), the record of the work (`PROGRESS.md`), and
`fix_tikzcd_in_macros.py` (written 8 Nov), which repaired the LaTeX of seven diagrams of P013 without changing what
they say.

Not included: the crops of the scans (the scans are the archive's own), LaTeX logs and auxiliary files, the
compile-check PDFs and the merge's `build/` folder (wrappers written by `compile_changed.py`), and the merge's dated
copies of files already in this repository.
