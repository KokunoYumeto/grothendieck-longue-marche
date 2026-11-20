# R3 final source audit — consolidated scans002–009

Saved: 2026-11-19 23:21:46 UTC

Reader: R3 — GPT-6 Astra Pro; effort setting not exposed.

## Scope and method

This records two completed, read-only audits of the consolidated page sources:

- `SP35_CW_156-7/pages/H156-01_156-7_scan002.tex` through `H156-01_156-7_scan008.tex`.
- `SP35_CW_156-7/pages/H156-01_156-7_scan009.tex` in a subsequent audit.

The reference was the supplied `source/SP35_CW_156-7_witnesses/codex/H156-01/PREAMBLE.tex`, including its LaTeX, AMS, mathrsfs, TikZ/tikz-cd, ulem and xcolor imports. R3 also read `SP35_CW_156-7/scripts/check_tex.py` to distinguish its existing structural checks from the requested additional source review.

The audits inspected source text and control-word inventories. They did not compile or render TeX, open manuscript images, perform OCR, or undertake external research. R3 did not edit the consolidated source files during either audit. No additional source inspection or checking was performed while saving this record.

The existing checker covers brace balance, environment nesting, delimiter counts and the presence of the tikz-cd ampersand-replacement option. The additional review considered defined/allowed control sequences, TikZ paths and node references, ulem grouping, and math-script constructions. Findings below are source-level results, not compilation results.

## Findings from scans002–008

No undefined or nonallowed control sequence was identified against the supplied preamble and its imported packages.

One concrete structural risk was reported in scan008, in the **cf Cor insertion** inside the outer `\deleted` block (lines39–41 in the source version inspected):

```tex
\tikz[baseline=(b.base),every node/.style={inner sep=0pt}]{...}
```

The supplied preamble implements text-mode `\deleted` through ulem's `\sout`. The raw inline TikZ optional argument contains an unprotected space in the key name `every node`. That exposes an incomplete optional argument to ulem's word-wise processing. The reported risk was splitting the TikZ command before its closing option bracket, which the existing balance checker does not detect.

The proposed protection was to box the complete inline picture as one unit, for example:

```tex
\mbox{\tikz[baseline=(b.base),every node/.style={inner sep=0pt}]{...}}
```

No further concrete macro or structural risk was reported in scans002–008.

## Findings from scan009

The inspected source still contained the known `\inM` token in the first cancelled At DC1 statement (line15 in that version). This is an undefined control sequence rather than the intended membership command followed by the letter M. The main reader had already identified it and announced its correction before requesting R3's scan009 audit.

No additional undefined or nonallowed control sequence was identified. In particular, `\fill` is supplied by TikZ and `\S` is standard LaTeX.

The raw inline TikZ at the start of the deleted upper NB was reviewed specifically against the scan008 risk. Its option list was only `[baseline=(nb.base)]`, with no unprotected internal space, and the drawing body was braced. R3 therefore did not report the same optional-argument splitting risk there.

No further concrete TikZ path, node-reference, ulem-grouping or math-script structural issue was reported in scan009.

## Fixes reported by the main reader

The main reader subsequently reported these changes:

| Source | Main-reported change | Relation to R3 findings |
|---|---|---|
| scan008, cf Cor insertion | Boxed the complete inline TikZ picture. | Addresses the ulem/TikZ grouping risk reported by R3. |
| scan009, first cancelled At DC1 statement | Replaced `\inM` with `\in M`. | Addresses the undefined token already identified by the main reader. |
| scan009, upper NB | Boxed its inline TikZ picture for consistency. | Additional protection reported by main; R3 had not identified the scan008 optional-space risk in this baseline-only option list. |

These are **main-reported fixes**. R3 did not reopen or independently recheck the changed files after receiving that report. No compilation or rendering was performed, and this record does not assert a successful TeX build.
