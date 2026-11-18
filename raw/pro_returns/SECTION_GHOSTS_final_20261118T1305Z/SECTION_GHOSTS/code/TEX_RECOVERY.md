# Reproducing the final LuaLaTeX build

Run from any directory:

```sh
python path/to/SECTION_GHOSTS/code/tex_recovery_bootstrap.py
```

The wrapper runs the existing `code/build.py` unchanged. The runtime must provide LuaHBTeX, BibTeX, and the standard LaTeX/font package trees at `/usr/share/texlive/texmf-dist` and `/usr/share/texmf` (the recovered Debian TeX Live2025/dev runtime does). A complete ordinary TeX Live installation can instead run `code/build.py` directly.

The recovery runtime lacked generated system file databases, format files, and the Lua font-loader packages. The wrapper uses non-database-only file lookup for the installed trees, generates `build/lualatex.fmt`, and retains caches/configuration/font maps in the sibling `tex_deps` directory. Its job-specific `TEXMFOUTPUT` points only to that local dependency directory; TeX's existing `openout_any=p` policy remains enabled. It makes no system installation changes.

Four exact official CTAN source archives are included under `code/tex_runtime_sources`: luaotfload, lualibs, luatexbase, and lua-uni-algos. `manifest.json` records their source URLs, byte lengths, and SHA-256 hashes. The wrapper checks those hashes before extraction and uses their documented docstrip extraction for lualibs/luatexbase. It requires no network download. Each original archive retains its upstream license and documentation.

The manuscript mathematics, bibliography and master metadata are not changed by the wrapper. The minimal normal PDF font map is assembled from the runtime's installed CM, AMS, Euler, RSFS, and Latin Modern maps.

Logs: `tex_deps/format_bootstrap.out`, `tex_deps/final_build_summary.out`, and `SECTION_GHOSTS/code/build.out`. The last path retains the full LaTeX/BibTeX transcript.
