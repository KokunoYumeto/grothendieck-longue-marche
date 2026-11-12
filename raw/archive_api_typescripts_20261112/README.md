# Three archive typescripts transcribed over the API by collation (12 November 2026)

Page-by-page diplomatic LaTeX transcriptions of typescripts in Grothendieck's Montpellier archive, made with Claude
Opus 5.5 (`claude-opus-5-5`, adaptive thinking, effort high) through the Anthropic Message Batches API, one request per
page, one batch at a time. Each page went as two colour images (upper and lower part) with, where there is one, the
matching passage of an existing edition as a draft. The model transcribes the page first, then compares it with the
draft and lists every difference. The full account is `API_TYPESCRIPTS_REPORT.md`; the folder guide is
`README_FOLDER.md`.

## What was done

- **The pilot passed.** On the 28 pages of an earlier check against the scans (11 of *Pursuing Stacks*, 11 of the
  *Esquisse d'un programme*, 6 of EGA V), the run caught 178 of the check's 184 differences (96.7 %). All 29 of its
  new findings that were looked at on crops were real, and no error introduced by the API was found on the crops.
- ***Pursuing Stacks*** (cote 134): all 680 pages in scope, typescript pp. 1–593 and the 134-2 front matter, letters
  and notes (`pursuing_stacks/`). The draft was the arXiv 2111.01000 v2 LaTeX. 12,140 differences
  (`pursuing_stacks/DIFFERENCES.tsv`), also keyed to the arXiv source by file, line, section and paragraph in
  `PS_ARXIV_DIFF.tsv`.
- ***Esquisse d'un programme*** (cote 119): all 58 pages of copy 1 (`esquisse/`). The draft was the text layer of the
  Grothendieck Circle's `EsquisseFr.pdf`. 327 differences (`esquisse/DIFFERENCES.tsv`).
- **"Nouveau EGA V"** (cote 25) and **EGA V, Blass's copy** (cote 24): the 3 pilot pages of each (`ega_v_cote25/`,
  `ega_v_cote24_blass/`); no draft. The other 181 and 73 pages were not done: the API refused the next batch because
  the account's credit ran out.

## Model and cost

Claude Opus 5.5 over the Message Batches API; $63.55 billed at batch price over 6 batches (744 pages; list price about
$127): $0.089 a page for *Pursuing Stacks*, $0.053 for the *Esquisse*. Every request finished with `end_turn`.

## What is unchecked

- Every page is AI-transcribed. Outside the 28 pilot pages, nothing has been checked by eye: the `DIFFERENCES.tsv` and
  `PS_ARXIV_DIFF.tsv` rows outside the pilot are the model's.
- The pilot shows the residual risk: a struck word left live, or a misspelling normalized, where the draft does the
  same.
- 53 pages of *Pursuing Stacks* carry many doubt marks and 18 pages long handwritten passages (`*/NOTES.tsv`); they
  need reading on the scan.
- `pursuing_stacks_combined.tex` does not yet typeset past scan 134-2/53; the per-page files are complete.
- Not sent: the handwritten documents in cote 134 (the letter "Cher Deligne", the notes on listing paper, the letter
  copies), R. Brown's translation in 134-2, duplicates and versos, and the annotations of the *Esquisse*'s copy 2.

## Editions quoted

The drafts, the differences tables and the raw requests and answers quote the text of two editions:

- *Pursuing Stacks*: A. Grothendieck, *Pursuing Stacks*, extended version by Mateo Carmona with the collaboration of
  Ulrik Buchholtz, of the 2015 edition by "the scrivener"; arXiv:2111.01000, version 2 (21 November 2021), LaTeX source
  (https://arxiv.org/abs/2111.01000v2), dedicated to the public domain under CC0 1.0. It is quoted in
  `pursuing_stacks/DIFFERENCES.tsv`, `PS_ARXIV_DIFF.tsv`, `alignment/drafts/ps_*.txt` and the requests and answers of
  the batches.
- *Esquisse d'un programme*: the French text published by the Grothendieck Circle,
  https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf (typeset PDF of 2008, which reproduces
  the French text of *Geometric Galois Actions* 1, LMS Lecture Note Series 242, 1997), linked from the Circle's page
  https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/unpubtexts.php. Its text layer is quoted in
  `esquisse/DIFFERENCES.tsv`, `pilot/pilot_new_findings.tsv`, `alignment/drafts/esq_*.txt`,
  `alignment/drafts_by_ocr/esq_*.txt`, `work/EsquisseFr*.txt` and the requests and answers of the batches.

## What is here and what is not

Published: the per-page transcriptions and combined files, the differences and notes tables, `PS_ARXIV_DIFF.tsv`,
`PAGES.json`, the alignment tables and the draft passages sent with each page (`alignment/`), the pilot's items, review
and new findings (`pilot/`), the requests (each image replaced by its file name, size and SHA-256) and the raw answers
of every batch (`batches/`), the run log (`RUNS.jsonl`, `batches_*.log`), the scripts and the system prompt
(`scripts/`), and the work files: the OCR used for the alignment (`work/ocr/`, `work/tsv/`), the Circle text layer
(`work/EsquisseFr*.txt`) and the compile tests (`work/compile/`).

Not published: the page images sent to the API (`work/img/`, 659 MB) and the pilot's crops (`pilot/crops/`); they are
images of the archive's scans, which the archive publishes at https://grothendieck.umontpellier.fr/. LaTeX auxiliary
files and Python caches are left out. No request or answer file contains a key or a header; the API key was read from
the environment and never written.

In these copies the first name of the user is replaced by "user", local paths included. In `scripts/batch.py` the path
of the local note that holds the API key and the label of the API account are replaced by descriptions. Nothing else in
the files is changed.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in
the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under
CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you
hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.
