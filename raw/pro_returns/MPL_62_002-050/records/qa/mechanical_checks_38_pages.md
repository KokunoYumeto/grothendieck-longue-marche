# Mechanical LaTeX checks of 38 saved page fragments

Checked at 2026-11-16 18:24:26 UTC. The snapshot contains scans 002, 004–017, 019–026 and 028–042. No manuscript images, crops, context contents, or earlier manuscript material were read during this check. Page files were not modified.

## Results

- All 38 snapshot page fragments compiled together successfully with LuaLaTeX: exit code 0.
- Scans 025, 032 and 036 were also compiled separately, including their custom TikZ paths and labels: all succeeded.
- Mechanical package validation found 38 page files, 688 inventory rows, and 38 done entries, with no errors or warnings. The separate visual audit had not begun at this snapshot; no audit claim is made here.
- No unbalanced braces or environments, prohibited editorial macro substitutions, or malformed editorial arguments were found.
- The successful compiler log contained no LaTeX/package warnings, overfull boxes, or underfull boxes. There was one missing-glyph message, detailed below.
- SHA-256 values taken for each compilation snapshot are retained in `compile_38_pages.json`. Every source file was byte-identical to its snapshot when compilation ended.

## Encoding issue for the primary transcriber to decide

Scan019, line51, has this math-mode source fragment:

```tex
\uline{\unsure{module\ p|unité\ pr}}
```

The raw `é` is unavailable in the legacy math italic font `cmmi12`; LuaLaTeX therefore reports `Missing character: There is no é (U+00E9) in font cmmi12!` and omits that glyph from this temporary rendering. A mechanical text-encoding form that preserves both alternatives is:

```tex
\uline{\unsure{\text{module}\ p|\text{unité}\ pr}}
```

This is an encoding suggestion, not a proposed manuscript reading. No source change was applied. The primary transcriber should decide the desired text/math treatment before freezing the transcription.

## Harness and limits

The reusable harness is `scripts/compile_fragments.py`. It compiles copies into a scratch build directory and records hashes; it never writes a page file. The editorial wrappers are identity groupings for syntax checks, and the diagram wrapper preserves TikZ ampersand catcodes by reading the body without capturing it as a pre-tokenized macro argument. It accepts diagram bodies that already contain `$...$` or `\[...\]` and supplies math mode to bare arrays. This prevents harness-generated errors from being mistaken for source defects.

This checks whether the LaTeX content parses and compiles. It does not validate manuscript readings, symbol choices, layout fidelity, deletion/insertion semantics, mathematical claims, or coverage against the ink. The source remains a fragment; the temporary document preamble is not added to the deliverable.

The first compilation attempts exposed environment/harness issues rather than page defects: default TeX package paths were unconfigured; Lua font caches needed local relative paths; ordinary argument-taking wrappers pre-tokenized TikZ ampersands; and a universal display wrapper conflicted with diagrams already carrying math delimiters. These were resolved entirely in the harness.

The supporting results JSON and successful console log are preserved in this directory. Temporary PDFs, font caches, copied fragments, and build products remain outside the work directory and are excluded from the deliverable ZIP.

## Reuse in this execution environment

```sh
python /workspace/scratch/a578466e229b/MPL_62_002-050_work/scripts/compile_fragments.py \
  --build /workspace/scratch/a578466e229b/mpl_mechanical_qa \
  --engine lualatex \
  --env-json /workspace/scratch/a50d05093ca1/tex_runtime/env.json \
  --combined
```

The external runtime location contains generic TeX support files, not manuscript material. On a normally configured TeX installation, omit `--env-json` and select an available engine. Run `package_tools.py validate --stage draft` for the non-compilation checks. Neither command appends audit or freeze entries.
