# api_typescripts_20261112: what is where

- `API_TYPESCRIPTS_REPORT.md`: the report (pilot, pages done, cost, what is left).
- `PS_ARXIV_DIFF.tsv`: every difference between the arXiv source of Pursuing Stacks and the page transcriptions,
  keyed to arXiv file, line, section and paragraph, with typescript page and scan (scripts/ps_arxiv_diff.py).
- `PAGES.json`: every page in scope (text, cote, site page, PDF page, typescript page, draft passage).
- `alignment/ALIGNMENT.tsv`: the alignment table (how each page was matched to its draft passage);
  `alignment/ALIGNMENT_raw.tsv`: the OCR aligner's votes for every page; `alignment/drafts/`: the passage sent with
  each page; `alignment/drafts_by_ocr/`: the aligner's own passages.
- `pursuing_stacks/`, `esquisse/`, `ega_v_cote25/`, `ega_v_cote24_blass/`: per text, `pages/<key>.tex` (one file per
  page), `<dir>_combined.tex` (all pages in archive order, with the macro definitions), `DIFFERENCES.tsv` (where the
  draft differs from the page; Pursuing Stacks and Esquisse only), `NOTES.tsv` (the model's notes per page: places
  to check by eye, long handwriting, counts of doubt marks and handwriting macros).
- `batches/<name>/requests.jsonl` (requests, images replaced by file name, size and SHA-256) and `results.jsonl`
  (raw answers); `RUNS.jsonl`: one line per batch submitted and collected.
- `pilot/`: `pilot_auto.tsv` and `pilot_review.tsv` (the check's items and whether the API caught them),
  `pilot_new_findings.tsv` (what the API found that the check did not, with the verdicts on the crops),
  `crops/` (the crops looked at).
- `scripts/`: align.py, reocr.py, inventory.py, prep_images.py, prompt_system.txt, batch.py, parse.py, preamble.tex,
  pilot_eval.py, pilot_show.py, pilot_new.py, pilot_review.py, pilot_new_verdicts.py, crop.py, findcrop.py,
  montage.py, ps_arxiv_diff.py, summary.py.
- `work/`: the OCR used for the alignment (`ocr/`), the page images sent (`img/`), the Circle text layer
  (`EsquisseFr.txt`, `EsquisseFr_recomposed.txt`), compile tests (`compile/`).
- 13 Nov 2026, the next texts (prepared, not yet submitted): `NEXT_TEXTS_20261113.md` (report), `TYPED_INVENTORY_20261113.tsv`
  (typed / handwritten class of every scan of 134-2 sites 115-144, 129, 162-5, 119, 10, 12, 15, 37),
  `PILOT_NEXT_20261113.json`, `scripts/next_texts_20261113.py` (inventory, PAGES.json entries for brown, mtl129, t162,
  esq119, r119, drafts), `alignment/ALIGNMENT_next_texts_20261113.tsv`; backups `work/*_before_next_texts_20261113.*`.
