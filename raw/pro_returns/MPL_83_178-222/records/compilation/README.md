# Recorded compilation validation

This directory contains logs and status for the current scan fragments, compiled mechanically without changing their content. No PDF is included in the deliverable.

- Started: 2026-11-17 17:09:25 UTC
- Finished: 2026-11-17 17:09:28 UTC
- Scan fragments: 43
- Compiler exit status: 0
- Rendered PDF pages: 44
- TeX/driver error diagnostics: 0
- Overfull-box diagnostics: 0
- Source files unchanged during compilation: True

The PDF page count reflects wrapper pagination, not a manuscript page count. `compile-status.json` records the SHA-256 of each exact source page and of the scratch concatenation, along with any diagnostics and their source locations.

To reproduce from the package directory:

```bash
python scripts/compile_fragment.py MPL_83_178-222_transcription.tex --output ../MPL_83_178-222_render
```

The helper prepares its own local XeLaTeX format and uses the installed TeX package trees. The wrapper explicitly loads `lm-math.map` to provide `lm-mathsy.enc`; this avoids the runtime's `xdvipdfmx` null-glyph assertion caused by absent generated font maps. Editorial colors and simple underlines are validation styling, not a finished diplomatic layout. See `../compilation_tooling.md` for the complete setup and limits.
