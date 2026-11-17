# Mechanical validation and compilation tools

These tools check the package's machine-readable structure. They do not assess manuscript readings, mathematical correctness, completeness against scans, or the fidelity of drawings. Tool preparation used synthetic material; manuscript transcription and visual audit remained with the primary reader.

## Package validator

From the package directory:

```bash
python scripts/validate_package.py
```

Use `--partial` while pages or the combined transcription are still being written, or `--json` for a structured report. The validator checks the expected 43 scans, page markers, balanced braces and environments, forbidden embedded-image/preamble commands, inventory fields and coverage, and agreement between the combined transcription and ordered page fragments. Every approved editorial macro must have an explicitly braced argument; whitespace and comments before the opening brace are permitted.

The lightweight parser ignores comments and escaped characters but does not expand TeX macros. Literal/verbatim content is outside its scope. A successful check is not evidence that a reading is correct.

## Doubts register builder

```bash
python scripts/build_doubts.py
```

This rebuilds the doubts file from the notation and doubt arrays in the page records and every nested, balanced-brace occurrence of `\unsure` and `\illegible` in the page fragments. It groups only exactly matching notation pairs and uses page-file line numbers for the occurrence concordance. Alternatives split only at unescaped vertical bars outside nested braces; the occurrence-level confidence values are mechanical defaults, not fresh judgments.

The default build ends with pending legibility and abbreviation sections and overwrites the output file. To preserve a completed reader-written narrative during later rebuilding, save that narrative separately and pass its path with `--review-note PATH`.

## Compilation wrapper

From the package directory:

```bash
python scripts/compile_fragment.py MPL_83_178-222_transcription.tex --output ../MPL_83_178-222_render
```

The wrapper inputs the fragment unchanged and writes its wrapper, PDF, and logs to the selected output directory. The runtime used for preparation had XeLaTeX and the packages `amsmath`, `amssymb`, `mathtools`, `geometry`, `xcolor`, TikZ, and `tikz-cd`; its TeX database lookup and compiled formats were absent. The helper therefore searches the installed `/usr/share/texmf` and `/usr/share/texlive/texmf-dist` trees directly and builds a local XeLaTeX format alongside the helper, without changing the system installation. Other installations may need those tree paths adapted. TeX shell escape is disabled.

The wrapper is for compilation validation, not a finished diplomatic edition. Editorial states are shown in colors; margins are kept in the text flow. Because `ulem` was unavailable, underlines use ordinary unbreakable LaTeX underlines. The definitions of `\diagram`, `\figure`, and the colored editorial macros preserve streaming input so nested `tikz-cd` content can set its ampersand category codes correctly.

The runtime also lacks generated font maps. In a full-fragment test, XeLaTeX reached the end of the document, but `xdvipdfmx` aborted in `pdf_new_string` after reporting a null glyph name in `LMMathSymbols10-Regular`. Verbose driver diagnostics showed that `lmsy10` was using its built-in encoding instead of the installed `lm-mathsy.enc` mapping. Loading `lm-math.map` resolved the failure; the wrapper now emits `\special{pdf:mapfile +lm-math.map}`. The ordinary one-command build then completed with exit status 0 and produced 44 PDF pages from the 43 scan fragments. That is wrapper pagination, not a manuscript page count. The fix changes only compilation support, not the transcription.

A two-page synthetic fragment exercised every editorial macro, accented text, aligned mathematics, matrices, a commutative diagram, and a TikZ drawing. It compiled to a two-page PDF without missing-character, font, error, overfull-box, or warning messages. Synthetic verification concerns the wrapper setup only; actual-fragment validation and any resulting source fixes are tracked separately.
