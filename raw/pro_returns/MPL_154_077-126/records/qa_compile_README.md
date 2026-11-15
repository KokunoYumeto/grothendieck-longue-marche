# LaTeX compilation QA harness

This is an infrastructure aid, separate from the diplomatic transcription.
Its preparation did not involve opening manuscript images, reading page
transcriptions, opening the context archive, compiling any page, or changing
any deliverable or `progress.log`.

## Run

From any directory:

```bash
python /workspace/scratch/e14c29a5357f/MPL_154_077-126/records/run_compile_qa.py
```

For one scan:

```bash
python /workspace/scratch/e14c29a5357f/MPL_154_077-126/records/run_compile_qa.py --first 77 --last 77
```

The launcher compiles `records/qa_compile.tex`, which inputs each selected page
file in numerical order and skips scan 99. It writes only under `records/`.
Expected output for the complete range is
`records/qa-build/qa-scans-077-126.pdf`, with its corresponding log. It halts at
the first TeX error unless `--keep-going` is specified. `--rebuild-format`
recreates the private XeLaTeX format.

## Installed environment, checked without compiling

- XeLaTeX: XeTeX 3.141592653-2.6-0.999996 (TeX Live 2025/dev/Debian).
- LuaLaTeX: LuaHBTeX 1.18.0 (TeX Live 2025/dev/Debian).
- pdfLaTeX is also installed; Tectonic is absent.
- The system filename-database links and several generated configuration links
  point into an absent `/var/lib/texmf`. Ordinary `kpsewhich` therefore reports
  installed files as missing. A `TEXMF` path without database-only `!!` prefixes
  finds the packages on disk.
- Found with that search configuration: article, fontspec, amsmath, amssymb,
  mathtools, unicode-math, TikZ, tikz-cd, adjustbox, xparse, fvextra, fancyvrb,
  geometry, xcolor, iftex, and Latin Modern OpenType text and math fonts.
- No ready-made XeLaTeX, LuaLaTeX, or pdfLaTeX format was found. The launcher
  initializes a private XeLaTeX format on its first run.
- `ulem.sty`, Babel's `french.ldf`, generated `language.dat`, generated font maps,
  and the generated dvipdfmx config were unavailable through the corrected
  search path. The launcher supplies private English hyphenation setup, a
  minimal driver config, and available basic font-map contents. XeLaTeX and
  OpenType fonts handle Unicode French directly; the harness does not apply
  French automatic punctuation or hyphenation rules.

## Editorial display conventions

All prescribed editorial macros have definitions. Deletions render red,
insertions blue, doubts amber, and margin notes purple. These color wrappers
allow paragraphs, nested macros, and drawings; deletions are not struck through
in this diagnostic rendering. Their source macros remain unchanged.

The figure macro accepts TikZ and scales it down only when wider than the text
area. The diagram macro additionally ensures math mode, allowing an array or a
tikz-cd diagram. Verbatim support uses fvextra and permits automatic line wraps.
The harness preserves Unicode letters using explicit Latin Modern OpenType
font files. Each manuscript scan starts on a fresh diagnostic page.

When ulem is unavailable, single and double underlines use a basic fallback.
That fallback cannot wrap a single underlined phrase across lines; overfull
boxes are visibly marked. A compilation error or overfull warning is a QA
finding, not authority to change a manuscript reading.

This harness was syntax-authored and its Python launcher was parsed, but no
format initialization or manuscript compilation was run during preparation.
