# Mechanical LaTeX verification

## Scope and final result

The complete run started at **2026-11-16 19:13:51 UTC**, after root's visual audits and encoding normalization. All **43 saved page fragments** compiled individually with exit code 0 using pdfTeX 1.40.26 (TeX Live 2025/dev/Debian), a temporary LaTeX format, and the wrapper in `verify_latex.py`.

Following the final alphabet-encoding changes, an incremental run started at **2026-11-16 19:16:22 UTC** and recompiled scans **272, 281, 285, 289, 291, and 292** only. All six passed without command or missing-glyph warnings. The unchanged 37 validated source hashes and results from the complete run are retained.

The final checked source state has **zero fatal errors, zero undefined-control-sequence errors, zero command warnings, and zero missing-glyph warnings**. No page file changed while its individual compilation was running. Routine overfull/underfull box diagnostics from the temporary page layout are outside this syntax check's scope.

This is mechanical verification, not an image audit or a finding about the accuracy, completeness, or interpretation of any reading. No scans or contextual sources were accessed. The verifying agent did not modify page files, transcription records, doubts, notes, audit entries, or frozen-state records.

## Earlier warnings: resolved in the final run

The earlier 18:51:38 UTC run warned about accented letters in math mode on scans 275, 276, 277, 279, 280, 281, and 309, and text-circle commands in math mode on scan 286. After root's encoding normalization, none of those warnings or dropped glyphs occurs in the final run. These were typesetting concerns, not proposed changes to manuscript readings. No warning remains pending from this mechanical check.

## Wrapper and package requirements

The checker loads `amsmath`, `amssymb`, `tikz-cd`, and `graphicx`, with UTF-8 input and T1 text encoding. It loads the TikZ libraries listed in its preamble, including **`shapes.geometric`**, needed for the ellipse decoration on scan 297.

Most marking macros are transparent during this syntax check. The underlining state macros preserve the grouping of mathematical expressions and exponents:

```latex
\newcommand{\uline}[1]{\ifmmode\underline{#1}\else#1\fi}
\newcommand{\uuline}[1]{\ifmmode\underline{\underline{#1}}\else#1\fi}
```

A completely transparent identity macro would erase grouping and could introduce a false double-superscript error. These math-aware definitions avoid that issue. The wrapper is still not a finished diplomatic rendering of textual underlining, deletions, insertions, doubt marks, or margins; this check does not validate their final visual style or page layout.

Raw `&` tokens in a `tikzcd` body require appropriate category codes, including when a diagram is nested inside another marking macro. The temporary wrapper uses:

```latex
\long\def\diagram#1{\begingroup\endlinechar=-1\relax\scantokens{#1}\endgroup}
```

An ordinary one-argument identity definition of `\diagram` can introduce wrapper errors for these fragments. Retokenization resolves those errors without changing the saved source. The standard `\figure` environment command is replaced in the temporary preamble to provide the task's requested one-argument drawing macro.

## Reproduction

From the deliverable directory:

```bash
python scripts/manage.py validate
python scripts/verify_latex.py
```

To recheck only particular pages after an edit:

```bash
python scripts/verify_latex.py 275 276 277 279 280 281 286 309
```

The script uses only installed TeX components. If the installed `ls-R` search database is unavailable, it enables direct package-tree searches for this subprocess environment. It builds a temporary LaTeX format locally when needed; it performs no installation or network operation. Shell escape is disabled and compilation uses draft mode.

Generated formats and wrappers were built outside the deliverable tree in `../tex_mechanical_qa/`. The final package retains JSON results and compiler logs/stdout in `records/latex_verification/`; historical warning records are labelled there and their resolution is explained above. No temporary compiler binary or source attachment is included here. The script never uploads, creates an archive, freezes a transcription, or writes an audit entry. The final run has no command or missing-glyph warnings; future edits should be rechecked.

## Record-saving behavior

`manage.py save` writes the submitted page, its complete `records/scanNNN.json`, the combined transcription, the inventory CSV, and a revision/completion log entry. It does **not** rebuild or overwrite `doubts.md` or `notes.md`. The combined transcription is derived from record `tex` fields, so an edit made only to a page `.tex` file will not be incorporated into the combined file.

For audit revisions, begin with the current `records/scanNNN.json`, preserve its existing inventory, doubts, observations, and other retained fields, change the intended fields, and submit it through `save --input`. The submitted record replaces that scan's record wholesale; omitted optional doubts and observations become empty lists. Old `inputNNN.json` files may be stale. Independently consolidating the Markdown doubts file is safe from `manage.py save`.

## Exact source state checked

These hashes identify the latest validated version of each page. The six changed pages were rechecked at 19:16:22 UTC; the unchanged 37 hashes are preserved from the 19:13:51 UTC complete run. This manifest does not itself constitute the transcription-freeze operation.

| Scan | Checked (UTC, 2026-11-16) | SHA-256 of page file |
|---|---|---|
| 271 | 19:13:51 | `6a47b5ba24999f87dc4859e814d68e091c201f441af50b9f325dafa35f097a46` |
| 272 | 19:16:22 | `cbefa6aabfa1f7f8d1adceca79371353ab02141049a3040c4c54f298cd0ab1be` |
| 273 | 19:13:51 | `f08b91b339248f52aee5cbd6700e26bdd9ee922d274592f2baf972daf948b6f3` |
| 274 | 19:13:51 | `7ce23ac26e880aebe6f885c14b7ea33e3d53fbb2db192eade44459c3ba630d0b` |
| 275 | 19:13:51 | `cf375b616e4aa611a2a5ec8be786ba697e546d4a6082e085713376f1cb089497` |
| 276 | 19:13:51 | `c9ff0ef42dd296b9c855fd5211736b3eddc7c468fc53e03a32633a0c8f75b7a7` |
| 277 | 19:13:51 | `4b588252709ad7117913e23b713961d5506ecbd5885dee90ed40c10d8c04903f` |
| 279 | 19:13:51 | `4d5002b477656700de5517dbc21fa731e4e3f8dd4d894852904e2403400fcae3` |
| 280 | 19:13:51 | `6a122d643baa7d96ccabbc3e341560e131299c6e9679abf57afac07391ae9d26` |
| 281 | 19:16:22 | `451744cea4bfb42b4310d84f3dcdd90c65cb305a3fe3bb3c2ad7bf4c095bb013` |
| 282 | 19:13:51 | `f732c7bebbcfc432d221704d3a2c18b24ec1fa571775c18594c3f17fa0487220` |
| 283 | 19:13:51 | `edda697966d501b3e8379f12094bd3de1f1cbf925172f58239974f07b1e4cec5` |
| 284 | 19:13:51 | `b58f7a485ce020aaef06d49b98779689c0806f03e0c4b29bec0ae9aa820d3705` |
| 285 | 19:16:22 | `5c969f94417bdd9d155e1ab5970e991868271f03e297b5d1b1f913f52a73a216` |
| 286 | 19:13:51 | `16e325dd26abd294009fee8f36f774b37ae51bf065c7f6a29b71eccf5d2e998e` |
| 287 | 19:13:51 | `8d36f4b50a5269763694d5a78ad24c717c3c280b3db3e448b6831dd5ae2b83f4` |
| 288 | 19:13:51 | `6f583913396696b18d21d9dc9d40429a19b60c273a503f3b79becf7a90c1f036` |
| 289 | 19:16:22 | `0f82abd8248722f726f2b0f96909f1b712b18c967b22fe27636a5e50b3f7deca` |
| 290 | 19:13:51 | `c4f14ae72be54fa2146d678f9a6ea00ea8506d5d320cfc60bbe6de53da4d41ca` |
| 291 | 19:16:22 | `ea89d8fd230a9c3cdc12263050e268d2ab7ec224ef6ce44f33e3ad5d9068da36` |
| 292 | 19:16:22 | `a028692cfc39112503852fed9029d7b4ccd99870ab1f73238ba3d1bbb8c9c935` |
| 294 | 19:13:51 | `6bafdb641fd9654415e8535e6a93185480f294a85480126269d263f0fcee3545` |
| 295 | 19:13:51 | `d2a7a56179d8c2744cc277d081c6a4de35d7282b3584c5af083a9163127fa4b4` |
| 296 | 19:13:51 | `f124f5c81f6e62ef86b5d906dd22e8762e581c47656b7424898879fc3b86f34b` |
| 297 | 19:13:51 | `b229d01f1280a544906c35a995b750fc267aa456a02b7b1bf736c31c9904a29a` |
| 298 | 19:13:51 | `86729bf3acde55e64c396bf46655b256d102938aaa38c256057b6d94c345dd06` |
| 299 | 19:13:51 | `8f26743d08b0cc693bc5974ef83a3982c0deb0fade24dc9728c7e21f481aa6a9` |
| 300 | 19:13:51 | `9777012e0fce0533f0e8c084beafc7a76844e128734cdd4a6cccc114a73bc8a5` |
| 301 | 19:13:51 | `ee8dedbedf1a300313dacb4843022904d8a21ad1d150b53027062182a1552e5d` |
| 302 | 19:13:51 | `2f567f743f0afabc7f1b9bd6adddd98676c4346fc62253e59a2633ddb3f451c2` |
| 303 | 19:13:51 | `5a751fa1eee6f5820b57323923b17b94fa46adbeeb13244416f9e28b3760d9cd` |
| 304 | 19:13:51 | `5552a0ae68c2d5e65e09b0bcc9573705ccb2bd2ce4f31cf3b8b85754559eb182` |
| 305 | 19:13:51 | `e83546b7b0be6561852f6c136b2b716f2202cdb7ef3eaf472a5571790faabae1` |
| 306 | 19:13:51 | `7754fdf8f49e8db78cf61d17af2d96b8dceec246e71cc587b52f071e10e2d616` |
| 307 | 19:13:51 | `fc17b2c5e439d3bbc7a45d10358b09982537c8d86402f744a8af24368b33f9e3` |
| 308 | 19:13:51 | `d5680756e992f2f5cc01f78502055f9ba9b10709952a453199402707ab18cad3` |
| 309 | 19:13:51 | `f6aaa1009394a232e6b6b5d37ec8feca167cd7b082c3265417122b19902719d0` |
| 310 | 19:13:51 | `66d903bdde4673c1055a7460145051389a2bc98f7b5edb3db6ef2b2032bc9467` |
| 311 | 19:13:51 | `b02f3ef9d12e38663d8d4006e736bc5a9f2ebfeb2a887313f1ce45d1175ffaaf` |
| 312 | 19:13:51 | `45a10d2563bce0efb67116c1043629f16c53cef7c9637f484d146f16380ad009` |
| 313 | 19:13:51 | `39aa2b9f038ceb679830615ead25cb408a097a3e25283f7d1040ab9858d89986` |
| 314 | 19:13:51 | `1833c0e99e4bc20cbde405faa0ce5671d1b99732cec25e9e1a0df60e104764a9` |
| 315 | 19:13:51 | `f227c0ac807f1e6966f16d664335fb1fbce3979f77c6b44dbd05eecba08c2e63` |
