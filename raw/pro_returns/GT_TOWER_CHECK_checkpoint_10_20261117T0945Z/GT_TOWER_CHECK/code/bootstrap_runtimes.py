#!/usr/bin/env python3
"""Restore the small missing TeX/GAP runtime components used by this audit.

All packages are extracted locally, with their SHA-256 checked.  No system
installation or privileged command is performed.  A normal TeX Live/GAP
installation can instead run the sources directly.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,urllib.request

ROOT=Path(__file__).resolve().parents[1]
WORKSPACE=ROOT.parent

def package(url,sha256,target,unpack):
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists():
        with urllib.request.urlopen(url,timeout=60) as response:
            target.write_bytes(response.read())
    digest=hashlib.sha256(target.read_bytes()).hexdigest()
    if digest!=sha256:raise ValueError(f'Hash mismatch: {target.name}')
    unpack.mkdir(parents=True,exist_ok=True)
    subprocess.run(['dpkg-deb','-x',str(target),str(unpack)],check=True)
    print(target.name,'SHA256',digest,'extracted',flush=True)

def tex():
    runtime=WORKSPACE/'.texruntime'
    if (runtime/'luatex/usr/share/texlive/texmf-dist/tex/luatex/luaotfload/luaotfload.sty').exists():
        print('Local LuaTeX component already present.',flush=True)
        return
    package('https://deb.debian.org/debian/pool/main/t/texlive-base/texlive-luatex_2024.20250309-1_all.deb',
            'c6601d6856af0b9cd25c64fcdab4a219a6ce7fd7a37724f532305add28fc72ff',
            runtime/'texlive-luatex.deb',runtime/'luatex')

def gap():
    runtime=WORKSPACE/'.gapruntime'
    if (runtime/'root/usr/lib/x86_64-linux-gnu/gap/gap').exists():
        print('Local GAP binary already present.',flush=True)
        return
    for p in json.loads((ROOT/'notes/gap_runtime_downloads.json').read_text()):
        package(p['url'],p['sha256'],runtime/p['name'],runtime/'root')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('runtime',choices=['tex','gap','all'],default='all',nargs='?')
    args=parser.parse_args()
    if args.runtime in ('tex','all'):tex()
    if args.runtime in ('gap','all'):gap()
