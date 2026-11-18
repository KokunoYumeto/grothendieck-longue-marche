# Mechanical pre-audit check

Checked at 2026-11-18 00:42:34 UTC.

Scope: saved page-file syntax, delimiters, markers, and inventory structure only. No source images, context ZIP, manuscript interpretation, or mathematical claims were checked. No page files were edited. The root was conducting its separate visual audit concurrently; line references below identify the file versions read during this pass.

## Results

- All 42 expected page files are present, scans 092–134 excluding 125.
- Every page has its expected scan marker; the first file starts with `\cotefile{93}` and `\scanpage{92}`, and no additional cote marker occurs.
- No unbalanced unescaped braces were detected after excluding TeX comments.
- Explicit `\[...\]`, `\(...\)`, and dollar delimiters are balanced. A group-aware lexical scan, accounting for text wrappers and implicit TikZ-CD cells, detected no nested explicit math or math delimiters crossing group boundaries.
- Environment beginnings and endings are balanced and properly nested in the lexical check.
- Inventory: 1,190 rows, all 42 expected scans covered, exact required header, all `transcribed=yes`. Category values, required fields, per-page sheet kind consistency, and per-page element-identifier uniqueness were checked.
- No image inclusion, external inclusion, preamble command, literal `[...]`/`[…]`, TODO, or PLACEHOLDER marker was detected.
- The page-state commands found are drawn from the requested macro list. Other commands are standard LaTeX/AMS math/TikZ commands except the concrete command listed below.

## Concrete findings

| File | Line | Finding |
| --- | ---: | --- |
| `MPL_93_092-134_93_scan101.tex` | 9 | `\longdash` is not a standard LaTeX/AMS/TikZ command and is not an allowed custom macro. Replace it with a standard math dash construction preserving the selected reading. |

## Wrapper-dependent issue

- `MPL_93_092-134_93_scan105.tex`, line 47: `\margin{\diagram{\begin{array}{r|l|l|l}` begins an `array` without explicit math delimiters. This is valid only if the surrounding `\diagram` definition enters math mode (for example with `\ensuremath`) or otherwise supplies it. A transparent text-mode wrapper would fail. This is a macro-definition dependency, not a claim about the reading.

## Limits and pending work

- The combined transcription has not yet been assembled and was deliberately not required or checked.
- No frozen hash comparison was attempted before the root finishes its visual audit and freezes the files.
- This was a lexical/static check, not an actual TeX compilation; custom macro definitions and layout were not supplied.
- Balanced syntax and inventory coverage do not establish that all visible content is transcribed, that inventory rows describe the source correctly, or that readings and doubt markers are accurate.
- Mathematical ellipsis commands such as `\ldots` and `\cdots` were retained as valid syntax; this check cannot distinguish an authored ellipsis from a substantive omission.
- Files changed while the final snapshot check was running: none detected. Later root edits can supersede these findings.
