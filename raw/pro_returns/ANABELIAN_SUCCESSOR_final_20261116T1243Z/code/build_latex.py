"""Build with LuaLaTeX, keeping missing system-format/cache data in scratch."""
import os,sys,subprocess,re
from pathlib import Path
W=Path(__file__).resolve().parents[1]
R=W.parent/'tex-runtime';R.mkdir(exist_ok=True)
E=os.environ.copy()
E.update({'TEXMF':f'{{{R},/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}}',
          'TEXMFVAR':str(R),'TEXMFCACHE':str(R),'TEXMFCONFIG':str(R),
          'TEXFORMATS':f'{R}//:'})
# The installed minimal TeX tree has no OpenType loader.  The document uses
# classic T1/Type1 Latin Modern, so build a LuaLaTeX format with that font
# mode selected explicitly, omitting only the unused OpenType startup block.
# The source copy and exact patch are retained in the scratch runtime; no
# installed TeX file is modified. A full TeX installation needs no patch.
kernel=Path('/usr/share/texlive/texmf-dist/tex/latex/base/latex.ltx').read_text()
start=kernel.index('\\everyjob\\expandafter{%\n  \\the\\everyjob\n  \\directlua{%\n  if xpcall')
end=kernel.index('\n\\fi\n%%% From File: ltexpl.dtx',start)
patched=kernel[:start]+r'''\everyjob\expandafter{%
  \the\everyjob
  \def\encodingdefault{OT1}% Explicit classic-font LuaLaTeX format.
  \let\f@encoding\encodingdefault
  }
'''+kernel[end:]
local=R/'latex.ltx'
if not local.exists() or local.read_text()!=patched:
    local.write_text(patched)
    if (R/'lualatex.fmt').exists():(R/'lualatex.fmt').unlink()
def run(args,cwd,name):
    with (W/'qa'/name).open('w') as f:
        p=subprocess.run(args,cwd=cwd,env=E,stdout=f,stderr=subprocess.STDOUT)
    print(name,p.returncode,flush=True)
    if p.returncode:print((W/'qa'/name).read_text()[-5000:]);sys.exit(p.returncode)
if not (R/'lualatex.fmt').exists():
    run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','--progname=lualatex','lualatex.ini'],R,'format_build.log')
run(['lualatex','-interaction=nonstopmode','-halt-on-error','ANABELIAN_SUCCESSOR_paper.tex'],W,'lualatex_pass1.stdout.txt')
run(['bibtex','ANABELIAN_SUCCESSOR_paper'],W,'bibtex.stdout.txt')
for n in [2,3]:run(['lualatex','-interaction=nonstopmode','-halt-on-error','ANABELIAN_SUCCESSOR_paper.tex'],W,f'lualatex_pass{n}.stdout.txt')
