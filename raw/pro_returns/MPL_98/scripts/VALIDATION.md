# Mechanical validation

`validate_transcription.py` performs file-level and lexical checks. It does not
read scans, decide manuscript readings, certify the inventory's completeness,
or check mathematics. In particular, running it does not satisfy a visual audit
and must not generate a manuscript `audited` event or a research check event.

During transcription:

```sh
python3 scripts/validate_transcription.py --partial --compile --output /tmp/mpl98-validation
```

For the complete deliverable, omit `--partial`. The complete mode requires scans
002–044 and the combined fragment. Paths are resolved relative to the script,
so the working directory does not affect its default input path.

Checks include page filenames and sequence, cote and scan markers, fragment
status, literal braces, environment nesting, inventory header and field values,
inventory coverage, unique per-page element identifiers, and agreement of the
combined fragment with the ordered page files. Only whitespace separating
complete page fragments is ignored in the combined comparison. A command
inventory is reported for review. The script rejects local definitions or file
inputs in page fragments; arbitrary standard-versus-nonstandard command status
requires successful compilation or manual review.

The generated `syntax_harness.tex` is separate from the transcription. It loads
standard packages and provides the required editorial macros. Its large paper
and simple colored state wrappers exist to expose TeX syntax errors, not to
certify manuscript geometry or produce a critical edition. The program does
not overwrite any page, inventory, progress log, research note, or hash record.

Compilation preflight reports engine executables and required TeX resources.
The presence of engine binaries alone does not establish that LaTeX formats or
packages are installed. A dependency failure is recorded as *not run*, never
as a successful compile. No shell escape is enabled when compilation runs.

## Local TeX resource setup

In this workspace the TeX resource files are installed, but the default search
configuration requires missing filename databases. There are also no generated
format or default font-map files. `setup_tex_validation.py` fixes this for an
individual validation process without downloads, package installations, or
changes to system files:

```sh
python3 scripts/setup_tex_validation.py --runtime /tmp/mpl98-tex-runtime
python3 scripts/validate_transcription.py --partial --compile --tex-environment /tmp/mpl98-tex-runtime/tex_environment.json --output /tmp/mpl98-validation
```

The setup uses ordinary recursive lookup in the installed trees, creates a
local pdfLaTeX format, assembles a local font map from installed Computer Modern,
AMS/Euler, and Latin Modern maps, then compiles an independent one-page smoke
test containing French accents, mathematical alphabets, a tikz-cd square, and
a TikZ curve. It reads no manuscript or context file. Keep the runtime directory
outside the deliverable tree: generated formats and copies of installed font
maps are disposable setup data.

`ulem.sty` is not available in this environment. If it remains unavailable, the
syntax harness defines `\uline` and `\uuline` using standard `\underline`; these
fallbacks do not wrap across lines. The installed `hyphen.tex` supplies the
format's default hyphenation because `language.dat` is absent. Neither choice
affects the transcription files, but the rendered harness is therefore only a
syntax aid, not a final typeset diplomatic edition.

If the combined compilation stops at an early error, `compile_pages.py` can
compile each page separately and report every page's first syntax blocker:

```sh
python3 scripts/compile_pages.py --tex-environment /tmp/mpl98-tex-runtime/tex_environment.json --output /tmp/mpl98-page-compilation
```

This auxiliary run does not edit or reinterpret any manuscript file. It is
useful for locating independent syntax errors; it is not an additional visual
reading and does not justify manuscript audit or research check events.
