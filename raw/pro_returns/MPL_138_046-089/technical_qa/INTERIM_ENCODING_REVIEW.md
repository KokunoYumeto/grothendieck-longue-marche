# Interim encoding review after the primary auditor's updates

> Historical interim review. The completed final result is in
> `FINAL_TECHNICAL_REPORT.md` and `final_validation.json`.

This is a targeted technical review of the saved source, not the final full
structural validation. The sources remain under active revision. The primary
auditor requested that the final validation wait for an explicit notice.

No scan images, context, archives, or manuscript readings were used. No page
source was edited. The scope remains syntax, mode nesting, and matrix-coordinate
existence only.

## Current targeted findings

No new concrete syntax error was found in the targeted checks below.

### scan064: named matrix and background construction paths

File: `../pages/MPL_138_046-089_138_scan064.tex`, lines 3–24 in the reviewed save.

- Lines 3–5 put the layer declaration and layer ordering before the picture,
  within a group that remains open until the picture ends. This is the required
  lifetime for the layer ordering.
- Line 6 uses `ampersand replacement=\&` consistently with its matrix cells.
  The braced `row sep` and `column sep` values safely contain the comma in the
  `between origins` specification.
- Line 7 names the actual matrix through
  `every matrix/.append style={/tikz/name=scan064matrix}`.
- Lines 8–18 protect the complete end-picture hook with braces. The
  `pgfonlayer` environment closes before the option's closing brace.
- The single `\draw` on lines 10–16 contains several disconnected subpaths.
  New coordinate groups begin those subpaths legally; a separate `\draw` for
  each is unnecessary. The final semicolon is present on line 16.
- All referenced cells exist and are nonempty in the saved matrix:
  `1-3`, `2-3`, `3-4`, `4-1`, `4-3`, `4-5`, and `5-3`.
- The original arrow directions on lines 19–23 also reach existing cells.

No syntax-only change is proposed for this block. This does not certify its
visual placement or establish the intended connections.

### scan081: nested delimiters inside ensuremath

File: `../pages/MPL_138_046-089_138_scan081.tex`, lines 18–22.

The current saved block begins:

```latex
\diagram{\ensuremath{\left\{\begin{array}{l}
```

and ends:

```latex
\end{array}\right.}}
```

The previously observed `\ensuremath{$...$}` is already absent. The saved form
keeps the entire delimiter/array construction in one math scope and needs no
further delimiter adjustment. In general, the conservative repair for an
unprotected `\ensuremath{$...$}` is to remove the inner dollar pair, preserving
the exact content and the `\ensuremath` wrapper. Dollar math inside a genuine
text-producing subargument, such as `\text{...$x$...}`, is a separate valid case.

### Previously reported mode hazards

The following saved changes now address the earlier concrete hazards:

| File and line | Current encoding | Technical status |
| --- | --- | --- |
| `MPL_138_046-089_138_scan051.tex:5` | `\text{\uline{$\cos^2u$}}` | The inner dollars occur within explicit text mode. |
| `MPL_138_046-089_138_scan060.tex:31` | `\deleted{\unsure{\ensuremath{G_x}}}` | The subscript has explicit math mode. |
| `MPL_138_046-089_138_scan068.tex:8` | `\deleted{\unsure{\ensuremath{\frac1p+\frac13+\frac12}}}` | The fraction tokens have explicit math mode. |

The previously conditional array bodies on scan047 lines 23/30, scan060 line 14,
scan062 line 16, and scan066 lines 65–70 now use `\ensuremath` as well. Their
math mode no longer depends on a blanket math definition of `\diagram`.

Annotation macros still need their previously stated contract: preserve the
caller's text/math mode and support the paragraphs or displays their saved
arguments contain. Their definitions are not supplied in the page fragments,
so this review cannot certify a particular unseen implementation. The inspected
annotations in scans 080–089 are used within explicit math or text scopes; no
additional concrete raw-math-in-text encoding was identified there.

### Ampersand conversion

A targeted check found 21 current `tikzcd` blocks. Every block specifies
`ampersand replacement=\&`; none retains a raw `&` separator. No converted
`\&` was found outside those blocks, so the conversion did not leak into the
ordinary `array`, `aligned`, or `tabular` separators.

### Previously noted arrow endpoints

- On scan078 line 7, the directions are now `dddll`/`dddrr`, reaching existing
  row 4 outer cells.
- On scan078 line 11, the directions are now `uul`/`uur` and `uuu`, reaching
  the existing row 3 side cells and row 2 central cell respectively.
- Scan053 line 27 still reaches the explicit empty `{}` at row 5, column 5.
  That is a defined empty endpoint rather than an uncreated cell; no
  unconditional syntax repair is proposed. Its intended geometry belongs to
  the primary visual audit.

## Validation status

The earlier full static snapshot remains in `static_results.json`. It has not
been overwritten or represented as validation of the actively edited sources.
The final whole-set brace/environment/mode/endpoint check is waiting for the
primary auditor's final notice. No compilation is claimed.

The generic background-layer example is saved separately as
`tikzcd_background_example.tex`; it is not part of the transcription.
