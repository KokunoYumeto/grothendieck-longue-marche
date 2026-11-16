# Mechanical structural QA

2026-11-16 17:54:02 UTC

Mechanical syntax and inventory checks only; no visual or reading audit. Source images and context not accessed.

## Summary

- 49 page files; expected 49.
- Combined transcription equals the expected ordered concatenation of all page files.
- Inventory: 1020 elements across 49 pages.
- Inventory exactly matches the structured element records.
- 49 audit log entries; complete page coverage: True; expected order: True.

## Findings

| Severity | File | Line | Finding |
|---|---|---:|---|
| review | `pages/MPL_36_053-085+39_36_scan065.tex` | 19 | illegible occurs within a mathematical region inside a text argument; verify it represents words, not symbols |
| review | `MPL_36_053-085+39_inventory.csv` | 1012 | Position-order candidate for 39/020: element 7 (upper half) follows element 6 (middle, CSV line 1011); coarse metadata-only ranking, inspect before reordering |

## Compilation availability

TeX executables are present where listed below, but a real compilation requires the format, class, and packages. No compilation was attempted when these dependencies were missing.

- `pdflatex`: /usr/bin/pdflatex
- `xelatex`: /usr/bin/xelatex
- `lualatex`: /usr/bin/lualatex
- `latexmk`: /usr/bin/latexmk
- `tectonic`: not found
- `pdflatex.fmt`: not found
- `xelatex.fmt`: not found
- `lualatex.fmt`: not found
- `article.cls`: not found
- `amsmath.sty`: not found
- `amssymb.sty`: not found
- `tikz-cd.sty`: not found
- `tikz.sty`: not found
- `mathrsfs.sty`: not found
- `ulem.sty`: not found

## Limits

These checks do not establish completeness against the manuscript, accuracy of readings, attachment of insertions, arrow directions, or visual fidelity of drawings. The custom macros have no supplied definitions in a fragment, so their final rendering cannot be assessed here. The report hashes identify the checked byte snapshot; later root audit changes may make the report stale.
