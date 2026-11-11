# Workspace-local LuaLaTeX runtime repair

This file records the environment used to produce the delivered PDF. The paths below are historical workspace paths; the repaired TeX tree, environment file and wrappers are not included in the archive. Portable recompilation uses the normal TeX Live commands in `README.md`.

The existing LuaHBTeX 1.18.0 binary is used. No system files were changed.

The installed TeX trees exist, but their `ls-R` links point to absent `/var/lib/texmf` databases. Their default `!!` lookup prevents finding existing sources. Local indexed views (`texmf-system`, `texmf-fonts`) consist of directory symlinks to the installed trees plus local filename databases. The LuaLaTeX format was built in `texmf-var/web2c/luahbtex` from the installed `lualatex.ini`.

The matching missing Debian package was downloaded and extracted locally:

- URL: https://deb.debian.org/debian/pool/main/t/texlive-base/texlive-luatex_2024.20250309-1_all.deb
- SHA-256: `c6601d6856af0b9cd25c64fcdab4a219a6ce7fd7a37724f532305add28fc72ff`
- Extracted with `dpkg-deb --extract` into `debs/`; no package manager installation or root permissions.

`updmap --user` with the local configuration generated maps for Computer Modern, AMS, RSFS, and Latin Modern. Font caches are confined to `cache/`. `TEXMFOUTPUT` names that cache directory so LuaTeX's normal `openout_any=p` policy permits the absolute cache paths; that policy remains unchanged.

## Commands used in the original workspace

From the paper directory:

```sh
. ../tmp/tex-local/env.sh
lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=../tmp/tex-local/build LM3_TEICHMULLER_TOWER_paper.tex
```

The original workspace also contained a `tmp/tex-local/bin/lualatex` wrapper sourcing the same environment and a matching `bibtex` wrapper. Compilation output was placed under `build/`; the paper sources remained in their original directory. These temporary wrappers are not archive dependencies.
