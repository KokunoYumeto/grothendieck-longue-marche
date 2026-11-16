# Structural validation

`validate_deliverables.py` is a read-only checker. It does not open image pixels,
run OCR, consult the context ZIP, compare readings, or establish completeness of
the transcription. Its embedded scan list was copied from the supplied scan
archive's filenames. With the original archive present, it checks the member
names directly without reading their contents.

Run from the deliverable directory:

```sh
python scripts/validate_deliverables.py --stage draft
python scripts/validate_deliverables.py --stage frozen
python scripts/validate_deliverables.py --stage final
```

Draft mode checks the existing initial sequence of page files. Frozen mode
requires all 45 pages, all second-reading audit entries, the freeze event, and
checksums. Final mode additionally requires research notes, the context-opened
event, and a final statement that the frozen checksums remain unchanged.

The expected combined file is an exact concatenation of page bytes in scan
order, with **one additional newline** between page files. Use `--separator none`
for direct byte concatenation, or `--separator blankline` for two additional
newlines. The checker does not trim, rewrite, or normalize any text. The first
page file carries `\cotefile{15}` before `\scanpage{139}`; later page files start
with their own `\scanpage` marker.

Recommended checksum entries in `progress.log` are:

```text
sha256 <64 hexadecimal characters> pages/MPL_15_139-194_15_scan139.tex
sha256 <64 hexadecimal characters> MPL_15_139-194_transcription.tex
```

Ordinary `sha256sum` output, `sha256 PATH HASH`, and `SHA256(PATH) = HASH` are also
recognized. Frozen checksums must appear before the `context opened` event. Each
page and the combined fragment must have a matching checksum.

The lightweight TeX checks cover braces, begin/end environments, math
delimiters, required markers, forbidden image inclusion, fragment-only commands,
and use of `\illegible` in detected math. These checks are intentionally
syntactic and cannot replace compilation or visual reading. TeX constructs
that change category codes or deliberately place math shifts inside nested text
may need manual evaluation of a reported problem.

`validation_harness.tex` is an optional wrapper, separate from the diplomatic
fragment. LuaLaTeX, XeLaTeX, pdfLaTeX, and latexmk executables were present in the
execution environment when this script was prepared. However, all three LaTeX
format files were unavailable, and a synthetic LuaLaTeX run failed with
`I can't find the format file lualatex.fmt`. The `ulem` package was also
unavailable. Compilation therefore remains unverified in this environment;
the wrapper requires a working TeX installation with its listed packages.
The harness uses LuaLaTeX or XeLaTeX for Unicode text. Its macro appearance is
only for syntax checking and must not be treated as an editorial rendering
standard.

```sh
mkdir -p /tmp/mpl-tex-check
lualatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/mpl-tex-check scripts/validation_harness.tex
```

Exit status 0 means that the requested structural checks passed; exit status 1
means that one or more structural errors were found. `--json` prints a machine
readable report to stdout. No command in this workflow modifies a transcription
file.

## Verification of the checker

A synthetic fixture with 45 page files, 45 inventory rows, 45 completion events,
45 audit events, 46 SHA-256 entries, and the final context/freeze events passed
final-stage validation. Deliberately appending an unmatched brace to one fixture
page produced separate findings for the brace, combined-file byte mismatch, and
changed frozen checksum. Additional synthetic strings checked escaped braces,
escaped percent signs, ignored comments, and forbidden `\illegible` use within
detected mathematics. These tests used no manuscript content.
