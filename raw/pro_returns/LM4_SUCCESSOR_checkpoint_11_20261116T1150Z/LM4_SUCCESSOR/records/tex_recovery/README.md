# Recovered private TeX runtime

The replacement environment contains LuaHBTeX1.18 and the LaTeX2024
system sources, but lacked a discoverable format, usable font map, and the
Lua font-loader dependencies. We repaired genuine installed/vendor inputs;
no stub loader or replacement font semantics were used in the final build.
The final build is certified separately by checkpoint07_recovery_metrics.json.

## Reproduction on this class of installed TeX environment

Create a private tex_runtime directory beside LM4_SUCCESSOR. Its env.json
must name the vendor and installed trees explicitly in TEXMF, without the
index-only !! prefixes. Point TEXINPUTS and LUAINPUTS recursively at vendor,
/usr/share/texlive/texmf-dist/tex and /usr/share/texmf/tex. Point TEXFORMATS at
the private formats directory. The retained env.json records the actual
paths used; relocate those paths if the workspace changes.

Obtain the official CTAN packages luaotfload, luatexbase, lualibs, and
lua-uni-algos. The ZIP names, lengths and SHA-256 values used here are in
official_ctan_archives.json. Extract them under vendor. The source-only
lualibs and luatexbase packages require their own docstrip steps:

    tex --ini --interaction=nonstopmode '\input plain \input lualibs.dtx'
    tex --ini --interaction=nonstopmode '\input plain \input luatexbase.ins'

Run these in the corresponding extracted package directories. Their actual
stdout is retained in this directory. Generate a private format with:

    luahbtex --ini --interaction=nonstopmode --jobname=lualatex \
      --progname=lualatex lualatex.ini

The actual format setup stdout is retained. Collect noncomment, nonempty
entries from the installed fonts/map/dvips/*.map files into private
pdftex.map and psfonts.map. The recovered setup used69 installed map files,
1569 distinct entries; it did not add arbitrary fonts. Point TEXFONTMAPS at
these private maps followed by the installed font-map roots.

The font cache must use the relative directory tex_cache within the paper
working directory. Set TEXMFCACHE=tex_cache and LUAOTFLOAD_CACHE=tex_cache.
An absolute sibling cache path was rejected by this installation's TeX
write policy; that failed attempt is not the final build.

From the parent workspace run:

    python3 LM4_SUCCESSOR/code/build_paper.py --env tex_runtime/env.json

The build script records every actual pass and adds a bounded number of
passes if cross-references have changed. The recovered final PDF has zero
warnings, undefined references, errors and overfull boxes. Full vendor
packages and caches are reproducible infrastructure and are not included
in the research archive; authored recipes, source, PDF and logs are.
