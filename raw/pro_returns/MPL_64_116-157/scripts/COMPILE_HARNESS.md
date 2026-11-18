# Temporary compilation harness

`compile_harness.py` is a separate editorial renderer for structural TeX validation. It inputs the supplied fragment without modifying it. Its default action prepares a temporary wrapper; `--compile` explicitly runs the compiler. Build files must remain outside the deliverable directory.

## Prepared environment

The current environment has a working local `pdflatex.fmt` and font map under `/workspace/scratch/22f602b123f8/MPL_64_116-157_qa/tex-assets`. The format was built from the installed LaTeX sources, and the font map combines the installed AMS and Latin Modern maps. Global TeX configuration was not changed.

The harness sets process-local `TEXMFDBS`, `TEXINPUTS`, format, map, encoding, and font paths to compensate for the missing system filename database. The `MPL_TEX_ASSETS` environment variable can select another local asset directory. These fallback paths assume the installed Debian TeX directory layout.

To reproduce the local setup elsewhere with that layout:

```bash
python scripts/prepare_tex_assets.py --assets-dir /absolute/path/to/temporary/tex-assets
```

Then invoke the harness with `MPL_TEX_ASSETS` set to that path and `--root` set to the unpacked deliverable directory. The script does not install packages or initialize formats automatically.

## Rendering assumptions and limitations

- Text uses UTF-8 input, T1 encoding, and Latin Modern fonts. French Babel is unavailable; French-specific line-breaking and spacing conventions are therefore not configured.
- Doubt and insertion macros retain their content and add colored question/plus markers.
- Text deletions use red editorial brackets so that entire paragraphs and displayed formulas remain compilable and can reflow. Mathematical deletions use `cancel`. The wrapper does not reproduce manuscript strike geometry.
- If `ulem` is unavailable, text underlines use boxed text inside a mathematical underline. These fallback underlines do not wrap; long underlined passages may overflow. Double underlining uses two nested rules.
- Marginal notes appear in reading order with an editorial margin label. Manuscript page identifiers are also explicitly labeled.
- Each scan starts a new rendered page. Long scans can occupy more than one output page.
- The required `figure` macro is repurposed to hold TikZ drawings; ordinary LaTeX floating figure environments are not supported by this wrapper.
- The `diagram` wrapper reads active ampersands so that ordinary `tikz-cd` cell separators and ordinary array tables work. An entire diagram should not be captured inside another macro before this wrapper reads it; place deletion/doubt marks on individual diagram components.
- The supplied fragment is checked by SHA-256 before and after a compilation. Compilation success verifies TeX syntax under this wrapper; it does not verify readings, completeness, diagram fidelity, or mathematical claims.

## Infrastructure validation performed

A synthetic fixture outside the deliverables exercised accented French text, single and double underlining in text and math, doubt and insertion marks in text and math, mathematical deletion, a deletion spanning three paragraphs and a displayed equation, a marginal note, an illegibility mark, a labeled commuting square, an array table, and a TikZ drawing. It compiled successfully with `pdflatex`, exit status 0, with the fixture hash unchanged. No manuscript images, manuscript text, or context materials were read for this infrastructure work.
