# Local TeX compilation feasibility

Checked: 2026-11-20 07:15:36 UTC.

**Scratch format built; complete synthetic preamble test blocked.** No manuscript was compiled.

## Results

- LuaHBTeX initialization returned **0** and created `work/texcheck/formats/lualatex.fmt`: **5,708,635 bytes**, SHA256 `97296174f2e5b633fcbed81895ff1f627b7c19e9b09e222a1cffced71fc5d665`. The subsequent synthetic run successfully loaded this format.
- The synthetic test returned **1** and produced no PDF. It reported missing `luaotfload-main`, then failed to load the font requested by `fontspec` at `fontenc.sty:116`.
- `ulem.sty` is also absent from the inspected TeX/runtime/tool-cache roots. It remains a separate blocker; the failed test stopped before reaching that package.
- A process-local `TEXMF` override resolves the installed package files despite missing filename databases.
- Format initialization used installed `hyphen.tex` because `language.dat` was absent. No hyphenation or manuscript-layout correctness is claimed.
- The existing `PREAMBLE.tex` is unchanged: SHA256 `aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf`.
- All recorded writes were inside `work/texcheck`; no source/page/context/record paths occurred among recorded inputs. Recorder checks are not a kernel-level access trace.

## Commands and isolation

These are the actual environment values used for the subprocesses; no global environment or TeX configuration was modified. The directories already exist in scratch.

```bash
export TEXMF='{/workspace/scratch/57a811ad3c84/work/texcheck/texmf,/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
export TEXMFHOME=/workspace/scratch/57a811ad3c84/work/texcheck/texmf
export TEXMFVAR=/workspace/scratch/57a811ad3c84/work/texcheck/var
export TEXMFCONFIG=/workspace/scratch/57a811ad3c84/work/texcheck/config
export TEXMFCACHE=/workspace/scratch/57a811ad3c84/work/texcheck/cache
export TEXMFOUTPUT=/workspace/scratch/57a811ad3c84/work/texcheck/build
export TEXFORMATS=/workspace/scratch/57a811ad3c84/work/texcheck/formats//
export VARTEXFONTS=/workspace/scratch/57a811ad3c84/work/texcheck/fonts
export MKTEXFMT=0
export MKTEXTFM=0
export MKTEXPK=0
export MKTEXMF=0
cd /workspace/scratch/57a811ad3c84/work/texcheck
lualatex --ini --jobname=lualatex --progname=lualatex --no-shell-escape --interaction=nonstopmode --halt-on-error --file-line-error --recorder --output-directory=/workspace/scratch/57a811ad3c84/work/texcheck/formats lualatex.ini
lualatex --fmt=lualatex --no-shell-escape --interaction=nonstopmode --halt-on-error --file-line-error --recorder --output-directory=/workspace/scratch/57a811ad3c84/work/texcheck/build /workspace/scratch/57a811ad3c84/work/texcheck/synthetic_preamble.tex
```

Format logs: `work/texcheck/format_build.stdout.log`, `work/texcheck/formats/lualatex.log`, and `work/texcheck/formats/lualatex.fls`. Synthetic logs: `work/texcheck/synthetic_compile.stdout.log`, `work/texcheck/build/synthetic_preamble.log`, and `work/texcheck/build/synthetic_preamble.fls`. Detailed hashes and parameters are in the companion JSON.

## Invented test document

```tex
\input{/workspace/scratch/57a811ad3c84/SP02_CW_10+12/PREAMBLE.tex}
\begin{document}
Synthetic test only. \uline{sample} and \sout{sample}.
\[x^2+y^2=1,\quad \mathbb{R},\quad \mathscr{F}.\]
\begin{tikzpicture}\draw (0,0) -- (1,0);\end{tikzpicture}
\begin{tikzcd} A \arrow[r] & B \end{tikzcd}
\end{document}
```

## Local search and limits

Filename-only searches covered `/usr/share/texlive, /usr/share/texmf, /usr/local/share/texmf, /opt/codex, /home/agent/.codex/plugins/cache, /home/agent/.codex/skills`. Neither `ulem.sty` nor the required luaotfload assets was found. The `/root/.codex` tool roots and `/var/cache/apt/archives` were absent. No user-file or manuscript searches, archive extraction, installation, fetching, package replacement, or removal occurred.

With the currently located assets and the no-install/no-fetch restriction, the existing LuaLaTeX preamble cannot complete. A syntax compilation gate remains blocked by runtime dependencies. The successful format build makes no claim about manuscript syntax, mathematical content, fonts, line breaking, or visual rendering.
