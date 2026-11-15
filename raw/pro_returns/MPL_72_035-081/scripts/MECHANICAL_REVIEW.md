# Mechanical review of the 035–069 snapshot

## Scope and result

This review covered 35 saved page fragments (scans 035–069), their combined transcription, and 734 inventory rows. It read no manuscript image and no supplied context. It made no manuscript reading and changed no transcription, inventory, or progress record. Subsequent changes by the primary transcriber are outside this snapshot.

The structural validator reported no errors. Braces and environment pairs balance; page markers and completion records match the saved files; the combined transcription is the direct byte concatenation of the page files. Inventory IDs have matching scan prefixes and consecutive suffixes, with no duplicate or missing identifiers. All inspected rows carry `transcribed=yes`.

The unclassified command list consists of standard `\mathbin`, `\mathrel`, AMS `\diagdown`, and the TikZ loop variables `\x` and `\s` declared by `\foreach` on scan 051. This whitelist classification supplies no evidence about the accuracy of the underlying readings.

## Compilation limitation

`pdflatex`, `lualatex`, `xelatex`, and `latex` executables exist. The configured TeX trees do not resolve `pdflatex.fmt`, `article.cls`, `amsmath.sty`, `amssymb.sty`, `mathtools.sty`, `tikz.sty`, `tikz-cd.sty`, `ulem.sty`, or `mathrsfs.sty` through `kpsewhich`.

A temporary wrapper and copies of the existing fragments were placed outside the deliverable work directory, under `/tmp/mpl_compile__xw80fvj`. The wrapper supplied neutral definitions of the diplomatic macros. The attempted command was:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape validation.tex
```

It exited with status 1 before document processing:

```text
I can't find the format file `pdflatex.fmt'!
```

The format-generation diagnostic reported no configured formats. No TeX distribution was installed. Consequently, this review establishes no successful compilation or visual rendering of a fragment. The following findings come from static source inspection and the software's primary documentation.

## Static findings and proposed fixes for the primary transcriber

### TikZ-CD inside a macro argument

The snapshot has 16 `tikzcd` environments, all enclosed by `\diagram{...}`. Their cells use literal `&`. With an ordinary argument-taking definition of `\diagram`, those ampersands have already been tokenized before TikZ can change their category code. The TikZ-CD manual, section 3.4, documents this error and its supported remedy.

Add `ampersand replacement=\&` to each `tikzcd` option list and use `\&` for its cell separators. Keep ordinary `array` and `tabular` separators as `&`. This is a source-encoding change and adds no drawn object or manuscript symbol.

Affected snapshot scans: 036, 038, 039 (three diagrams), 041, 046, 054, 057 (three), 058, and 059 (four).

Primary source: [TikZ-CD manual, section 3.4](https://tug.ctan.org/graphics/pgf/contrib/tikz-cd/tikz-cd-doc.pdf). The same section is [available as HTML](https://tikz.dev/tikz-cd/advanced-usage).

### Scan 036: arrow target outside its matrix

At snapshot lines 34–36, the source occupies row 1, column 1, and its arrow has direction `ur`; the matrix contains one row. TikZ-CD's direction parser decrements the row for `u` and increments the column for `r`, producing row 0, column 2. That target does not exist in this matrix.

Preserving the encoded up-right direction requires placing the destination at row 1, column 2, and the source at row 2, column 1. The primary transcriber must check those positions against the image before applying that layout adjustment. This review supplies no alternative reading of the arrow.

Primary implementation: [TikZ-CD source, direction parser and arrow-target construction](https://github.com/astoff/tikz-cd/blob/master/tikzlibrarycd.code.tex).

### Scan 059: braces refer to empty cells

The first matrix's paths refer to `inc-1-5` and `inc-2-5`, both blank cells in the current matrix. Enable `nodes in empty cells` to create the required anchor nodes without adding visible contents.

Make the intended matrix names explicit in the matrix style:

```latex
every matrix/.append style={name=inc,nodes in empty cells}
```

Use the corresponding `every matrix/.append style={name=bs}` for the second matrix. These replace the top-level `name=inc` and `name=bs` options, respectively. TikZ-CD's implementation applies the environment's ordinary options to the enclosing picture and applies `every matrix` to the matrix itself; this explicit placement directs the names to the objects referenced by the paths.

Primary sources: [PGF/TikZ matrix library, section 59.1](https://tikz.dev/library-matrix), which describes generated cell names and `nodes in empty cells`; [TikZ-CD implementation](https://github.com/astoff/tikz-cd/blob/master/tikzlibrarycd.code.tex), at the `tikzcd` environment's matrix construction.

### Scan 059: array math mode in a consumer wrapper

Snapshot lines 56–59 contain `\diagram{\begin{array}...\end{array}}` outside explicit math delimiters. A consumer wrapper can support this fragment with:

```latex
\newcommand{\diagram}[1]{\ensuremath{#1}}
```

That definition also permits diagrams already inside math mode. Alternatively, explicit math delimiters can enclose the array. This is a wrapper requirement, not a demonstrated manuscript-content error. The attempted neutral wrapper could not reach this code because the TeX format was missing.

### Scan 065: subscript within deletion and uncertainty macros

Snapshot line 46 reads `\deleted{\unsure{_{n-j}}}` immediately after a `\gamma` token in a formula. With the neutral definitions `\def\deleted#1{#1}` and `\def\unsure#1{#1}`, the expanded local expression is `\gamma_{n-j}`. Thus a syntax failure is not established by that subscript alone.

A wrapper that boxes the contents of either macro must support a leading subscript. A self-contained empty base can be encoded as `\deleted{\unsure{{}_{n-j}}}`; adoption requires the primary transcriber's check that the added grouping preserves the intended attachment and marking. No edit was applied during this review.

### Nesting

None of the 16 inspected `tikzcd` environments occurs inside another `tikzcd` environment or a `tikzpicture` environment. Wrapping a diagram in `\margin` or `\deleted` does not itself introduce a second TikZ-CD environment. The source explicitly rejects nesting of TikZ-CD environments; the inspected environment structure does not contain that pattern.

## Record of non-actions

No checkpoint or final ZIP was created. No persistent upload was performed. No input archive was opened, and no image was viewed. Only this mechanical documentation was added to the deliverable work directory during this review.

## Follow-up: all 47 saved fragments, before freeze

The subsequent snapshot contains scans 035–081 and 1,001 inventory rows. Structural validation again reported no errors: page files and markers are complete, inventory kind and sheet-kind values are valid, element identifiers are consecutive within every scan, and the combined file equals the direct page-byte concatenation. The new commands `\sharp`, `\textcircled`, and `\xrightarrow` are standard math/LaTeX commands and were added to the validator's advisory whitelist. The remaining unclassified names `\x` and `\s` are the previously identified loop variables.

`static_tex_review.py` now performs conservative, read-only checks on explicit math delimiters, `\left`/`\right` pairing, TikZ-CD nesting, matrix cell separators, simple relative arrow targets, empty-cell anchor references, and marked arguments beginning with a script. Synthetic checks cover the distinction between the control token `\(` and a row break followed by a literal parenthesis, plus valid and invalid relative arrow targets. In the inspected all-page snapshot, it reports no delimiter-pair, environment-nesting, or out-of-range arrow errors. A separate parity check found no odd count of unescaped single-dollar or double-dollar delimiters.

The primary transcriber repaired scan 036's arrow matrix before this follow-up. At the follow-up snapshot, literal cell separators still occurred in 16 TikZ-CD blocks across scans 038, 039, 041, 046, 054, 057, 058, 059, and 071. The previously recorded scan 059 empty-cell anchors and scan 065 leading-subscript advisory also remained. These are observations of that snapshot; run the scripts again to assess subsequent corrections.

The companion `macro_inventory_coverage.md` and `macro_inventory_coverage.csv` supply the requested compact reconciliation report for all 47 scans. Every `figure`, `diagram`, `margin`, `inserted`, and `deleted` call has its scan, source line, argument prefix, marked-parent identifier, and matching inventory-kind count. This exposed count differences requiring inspection, particularly figure/drawing classification on scans 047, 058, 066, 071, 073, and 078, and multiple nested deletion calls represented by larger inventory blocks. No inference about an unread manuscript element is made from those counts.

The follow-up added supporting scripts and reports only. It did not edit transcription, inventory, progress, or audit records; it did not install TeX, open images or context, or create or upload a ZIP.
