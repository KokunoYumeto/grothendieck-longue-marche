# Mechanical LaTeX review before freeze

The mechanical reviewer opened the LaTeX page files and page-record JSON solely
to inspect syntax and inventory consistency. No source image or context text
was opened, and no page file was edited by the reviewer.

## Findings

- All 44 expected page fragments were present in the required cote/scan order.
- Braces and environments were balanced; dollar counts were even, and display
  opening/closing counts agreed.
- In the initial pass, the 996 inventory rows matched their corresponding page-record elements,
  positions, first words/objects, and sheet kinds. Every row said `yes`.
- The command review found only the permitted state macros and standard LaTeX,
  AMS, or TikZ commands. The validation recognition list was extended for these
  standard commands: `\textsuperscript`,
  `\textsubscript`, `\hrule`, `\not`, `\xrightarrow`, and `\xleftarrow`.

Three syntax changes were demonstrated in temporary copies and authorized by
the principal transcriber for the repair script:

1. Within every `tikzcd`, add `ampersand replacement=\&` and change matrix
   separator `&` tokens to `\&`. The matrix is inside the argument of
   `\diagram`, so the explicit replacement preserves its cell boundaries under
   macro argument tokenization. Existing diagram options are retained.
2. In cote 23 scan 004, remove the inner dollar pair from
   `\deleted{$\unsure{\Omega^r}$}` within an existing display. The result is
   `\deleted{\unsure{\Omega^r}}`.
3. In cote 23 scan 006, enclose the opening array in display math:
   `\diagram{\[\begin{array}{cc}...\end{array}\]}`. The array's contents are
   unchanged.

The `\diagram{\[...\]}` array wrapper in cote 23 scan 014 compiles with the
transparent test definition of `\diagram`. Dollar pairs inside `\text{...}`
in cote 23 scan 016 also compile.

## Compilation

Every page was compiled individually in a temporary directory. With the three
repairs above applied only to those temporary copies, all 44 pages compiled
successfully using XeLaTeX. Forty passed on the first repaired pass. The four
remaining probes passed after adding the scan 006 math delimiters and loading
the TikZ `shapes.geometric` library for the ellipse nodes in cote 22 scan 010
and cote 23 scans 010–011.

`syntax_test_preamble.tex` preserves the working test preamble. Each probe
consisted of that preamble, `\begin{document}`, one page fragment, and
`\end{document}`. Its state macros pass their arguments through, so these
checks establish syntax under those definitions; they do not test the visual
appearance of a full diplomatic macro implementation or the correctness of
any reading. `syntax_compile_results.json` records the per-page exit results.

The TeX binaries were installed but the normal filename lookup lacked usable
indexes/formats. For the isolated probe process, `TEXMF` was set to
`{/usr/share/texlive/texmf-dist,/usr/share/texmf}`. A local XeLaTeX format was
built in the temporary directory using
`xetex -ini -etex -jobname=xelatex -progname=xelatex -interaction=nonstopmode xelatex.ini`,
then selected with XeLaTeX's `-fmt` option. No system TeX configuration was edited.

## Applying the authorized repairs

The principal transcriber applies the script before freezing:

```sh
python3 records/repair_tex_syntax.py --apply
```

Without `--apply` it reports proposed changes. It refuses application after a
freeze marker, preserves existing content outside the three transformations,
and writes before/after hashes and transformation counts to
`records/syntax_repair_log.json`. The mechanical reviewer has not invoked this
script against the page files.

## Audited and frozen page verification

After all 44 visual audits, the syntax probes were repeated on the audited
page contents. All 44 compiled successfully with the same three mechanical
repairs. The principal transcriber applied those repairs to the page files at
23:06:31 UTC on 2026-11-16 and subsequently froze the transcription.

At 23:08:56 UTC, the mechanical reviewer compared each frozen page file with
the corresponding successfully compiled temporary fragment. All 44 matched
byte for byte. The inventory then contained 999 rows, all matching their
page-record JSON fields, with every `transcribed` value equal to `yes`.
`syntax_compile_results_audited.json` retains the frozen-page hashes, individual
compile exit codes, and equality-check results. No source images or context
contents were accessed by the mechanical reviewer.

The metadata reconciliation removed 19 abbreviation forms that had no literal
occurrence in the page fragments, deleted six resulting empty abbreviation
rows, and added three verified literal variants under already supplied
expansions. Seven duplicate doubt groups were consolidated while retaining
their observations and the lower confidence where the records disagreed.
The 22/029 nonmembership/noninclusion candidates were reordered in the doubt
record to match the frozen transcription. The rebuilt report contains 207
doubt entries: 20 high, 85 medium, and 102 low confidence. These operations
changed metadata and scripts only; the frozen page and combined-transcription
files were not changed.
