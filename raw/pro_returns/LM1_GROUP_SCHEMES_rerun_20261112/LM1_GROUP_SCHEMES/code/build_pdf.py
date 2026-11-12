"""Build the paper with LuaLaTeX and BibTeX, including a minimal-host repair.

On a normal TeX Live installation this uses its stock lualatex format.
The supplied execution host has the TeX Live files and LuaHBTeX binary,
but lacks the generated format/font maps and luaotfload. For that case
we build a local Type-1-only LuaLaTeX format, replacing solely the optional
OpenType-loader startup hook. The document uses T1 Latin Modern fonts.
No system file is changed, no file is downloaded, and all fonts are the
installed upstream fonts. The source also compiles with stock LuaLaTeX.
"""
from pathlib import Path
import argparse, os, re, shutil, subprocess, hashlib

BASE=Path(__file__).resolve().parents[1]
CODE=BASE/'code'
RUNTIME=BASE.parent/'.tex_runtime'
PAPER='LM1_GROUP_SCHEMES_paper'
parser=argparse.ArgumentParser()
parser.add_argument('--latex-only',action='store_true')
parser.add_argument('--prepare-only',action='store_true')
args=parser.parse_args()
env=os.environ.copy()

def output(cmd,**kw):
    p=subprocess.run(cmd,cwd=BASE,env=env,text=True,capture_output=True,**kw)
    if p.returncode: raise RuntimeError(f'{cmd}: {p.stdout}\n{p.stderr}')
    return p.stdout.strip()

def logged(cmd,name):
    with (CODE/name).open('w') as f:
        p=subprocess.run(cmd,cwd=BASE,env=env,text=True,stdout=f,stderr=subprocess.STDOUT)
    print(name,'exit',p.returncode,flush=True)
    if p.returncode:
        print('\n'.join((CODE/name).read_text(errors='replace').splitlines()[-35:]))
        raise SystemExit(p.returncode)

stock_fmt=output(['kpsewhich','-var-value=TEXMFVAR'])
probe=subprocess.run(['kpsewhich','lualatex.fmt'],cwd=BASE,env=env,text=True,capture_output=True)
latex=['lualatex','--interaction=nonstopmode','--halt-on-error']
if probe.returncode or not probe.stdout.strip():
    RUNTIME.mkdir(exist_ok=True)
    dist=Path(output(['kpsewhich','-var-value=TEXMFDIST']))
    extra=Path('/usr/share/texmf')
    env.update(TEXMF='{.,'+str(RUNTIME)+','+str(extra)+','+str(dist)+'}',
               TEXMFVAR=str(RUNTIME),TEXMFCONFIG=str(RUNTIME),
               TEXFORMATS=str(RUNTIME),
               TEXINPUTS=str(RUNTIME)+'//:',
               TEXFONTMAPS=str(RUNTIME)+':')
    for dst,src in [('language.dat','language.us'),('language.def','language.us.def'),
                    ('language.dat.lua','language.us.lua')]:
        shutil.copyfile(dist/'tex/generic/config'/src,RUNTIME/dst)
    maps=[extra/'fonts/map/dvips/lm/lm.map',dist/'fonts/map/dvips/rsfs/rsfs.map']
    maps+=sorted((dist/'fonts/map/dvips/amsfonts').glob('*.map'))
    (RUNTIME/'pdftex.map').write_text('\n'.join(p.read_text() for p in maps))
    kernel=(dist/'tex/latex/base/latex.ltx').read_text()
    start=kernel.index("\\everyjob\\expandafter{%\n  \\the\\everyjob\n  \\directlua{%\n  if xpcall")
    end=kernel.index('\\expandafter\\let\\csname ver@luaotfload.sty\\endcsname\\fmtversion',start)
    end=kernel.index('\n  }',end)+len('\n  }')
    replacement='\\everyjob\\expandafter{%\n  \\the\\everyjob\n  \\def\\encodingdefault{OT1}%\n  \\let\\f@encoding\\encodingdefault\n  }'
    patched=kernel[:start]+replacement+kernel[end:]
    # A distinct filename identifies the locally modified format source.
    local_kernel=RUNTIME/'lm_type1_kernel.ltx'
    local_kernel.write_text(patched)
    ini=(dist/'tex/latex/tex-ini-files/lualatex.ini').read_text()
    ini=ini.replace('\\input latex.ltx',f'\\input "{local_kernel}"')
    (RUNTIME/'lm_type1.ini').write_text(ini)
    fmt=RUNTIME/'lualatex_type1.fmt'
    signature=hashlib.sha256(patched.encode()).hexdigest()
    stamp=RUNTIME/'type1_format.sha256'
    if not fmt.exists() or not stamp.exists() or stamp.read_text().strip()!=signature:
        logged(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
                '--jobname=lualatex_type1',f'--output-directory={RUNTIME}',
                str(RUNTIME/'lm_type1.ini')],'latex_format.out')
        stamp.write_text(signature+'\n')
    latex+=['--fmt=lualatex_type1']
    print('Local LuaLaTeX Type-1 format:',signature,flush=True)
    print('Font maps:',', '.join(p.name for p in maps),flush=True)
else:
    print('Using stock LuaLaTeX format:',probe.stdout.strip(),flush=True)
if args.prepare_only: raise SystemExit(0)
logged(latex+[PAPER+'.tex'],'latex_pass1.out')
if not args.latex_only:
    logged(['bibtex',PAPER],'bibtex.out')
    logged(latex+[PAPER+'.tex'],'latex_pass2.out')
    logged(latex+[PAPER+'.tex'],'latex_pass3.out')
    log=(BASE/(PAPER+'.log')).read_text(errors='replace')
    bad=re.findall(r'^.*(?:Undefined control sequence|undefined citations|undefined references|Citation .* undefined|Reference .* undefined|Overfull \\[hv]box|Missing character:).*$',log,re.M)
    if bad:
        raise RuntimeError('Final log requires inspection: '+repr(bad))
print('PDF bytes:',(BASE/(PAPER+'.pdf')).stat().st_size)
