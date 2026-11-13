"""Restore missing LuaLaTeX runtime files without changing the installation.

A complete standard TeX Live does not need this helper. Package archives are
fetched from CTAN and extracted into work/runtime/texmf only. Existing downloads
are reused unless --refresh is supplied. --packages restricts dependency repair;
--no-format leaves the existing LuaLaTeX format untouched.
"""
from pathlib import Path
import argparse, concurrent.futures, hashlib, io, json, os, subprocess, tarfile, urllib.request
ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/'runtime'; TEXMF=RUNTIME/'texmf'
PACKAGES=['luaotfload','lualibs','luatexbase','luacode','stix2-otf','hyphen-french','babel-french','lua-uni-algos','unicode-data','lualatex-math','ctablestack','ulem','newunicodechar','amsfonts']
CTAN='https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/'

def fetch(pkg,refresh=False):
    RUNTIME.mkdir(parents=True,exist_ok=True);TEXMF.mkdir(parents=True,exist_ok=True)
    url=CTAN+pkg+'.tar.xz';archive=RUNTIME/(pkg+'.tar.xz')
    if archive.exists() and not refresh:data=archive.read_bytes()
    else:
        with urllib.request.urlopen(url,timeout=60) as response:data=response.read()
        archive.write_bytes(data)
    count=0
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:xz') as tf:
        for m in tf.getmembers():
            name=m.name.removeprefix('texmf-dist/')
            if name.startswith(('tex/','fonts/','scripts/')) and m.isfile():
                if '..' in Path(name).parts:raise ValueError('Unsafe archive member')
                dest=TEXMF/name;dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(tf.extractfile(m).read());count+=1
    print(pkg,len(data),count,flush=True)
    return {'package':pkg,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'files':count}

def build_font_map():
    """Supply the missing default map from installed standard font maps."""
    from texenv import environment
    names=['cm.map','cmextra.map','symbols.map','euler.map','latxfont.map','cyrillic.map','lm.map']
    lines=['% Standard TeX Live font map assembled from installed package maps.'];seen=set()
    for name in names:
        result=subprocess.run(['kpsewhich',name],env=environment(force=True),capture_output=True,text=True)
        path=result.stdout.strip()
        if not path:continue
        lines.append('% '+name)
        for line in Path(path).read_text().splitlines():
            line=line.strip()
            if not line or line.startswith('%'):continue
            key=line.split()[0]
            if key not in seen:lines.append(line);seen.add(key)
    target=TEXMF/'fonts/map/pdftex/updmap/pdftex.map';target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('\n'.join(lines)+'\n')
    print('font map entries',len(seen),flush=True)

def build_format():
    from texenv import environment
    env=environment(force=True)
    for name in ['var','config','cache']:(RUNTIME/name).mkdir(exist_ok=True)
    lang=TEXMF/'tex/generic/config';lang.mkdir(parents=True,exist_ok=True)
    (lang/'language.dat').write_text('english hyphen.tex\n=usenglish\nfrench loadhyph-fr.tex\n')
    (lang/'language.def').write_text('\\addlanguage{english}{hyphen.tex}{}{2}{3}\n\\addlanguage{french}{loadhyph-fr.tex}{}{2}{3}\n')
    fmt=RUNTIME/'formats';fmt.mkdir(exist_ok=True)
    r=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','lualatex.ini'],cwd=fmt,env=env,capture_output=True,text=True)
    (RUNTIME/'bootstrap.log').write_text(r.stdout+r.stderr)
    print('format return',r.returncode,flush=True)
    if r.returncode:
        print((r.stdout+r.stderr)[-3500:],flush=True);raise SystemExit(r.returncode)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--packages',nargs='+',default=PACKAGES);ap.add_argument('--refresh',action='store_true');ap.add_argument('--no-format',action='store_true');args=ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        results=list(ex.map(lambda p:fetch(p,args.refresh),args.packages))
    record=ROOT/'records/RUNTIME_RESTORE.json';record.parent.mkdir(parents=True,exist_ok=True)
    old=json.loads(record.read_text()) if record.exists() else []
    byname={r['package']:r for r in old};byname.update({r['package']:r for r in results})
    record.write_text(json.dumps(list(byname.values()),indent=2)+'\n')
    build_font_map()
    if not args.no_format:build_format()

if __name__=='__main__':main()
