#!/usr/bin/env python3
"""Apply the reader's pre-freeze placement corrections to existing figure macros."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
if 'transcription frozen ' in (root/'progress.log').read_text():
    raise SystemExit('Frozen: no transcription edits permitted.')

def extract(n, count):
    path = root/f'pages/MPL_57_089-132_57_scan{n:03d}.tex'
    lines = path.read_text().splitlines()
    figures = [line for line in lines if line.startswith(r'\margin{\figure{')]
    assert len(figures)==count, (n,len(figures))
    return path, '\n'.join(line for line in lines if not line.startswith(r'\margin{\figure{'))+'\n', figures

def put(s, anchor, item, before=False):
    assert s.count(anchor)==1, (anchor,s.count(anchor))
    return s.replace(anchor, item+' '+anchor if before else anchor+' '+item)

path,s,f=extract(117,7)
s=put(s,r"\uline{par la donnée de descente sur} $X'$.",f[0])
s=put(s,'(i.e. injectif,',f[1])
s=put(s,'WEIL).',f[2])
s=put(s,r"$S'=\operatorname{Spec}(\bar A)$",f[3],True)
s=put(s,r"$X'=X\times_S S'$",f[4])
s=put(s,r'morphismes}.-',f[5])
s=put(s,"$P$''.",f[6])
path.write_text(s)

path,s,f=extract(119,12)
s=put(s,r"relativement à $\alpha:S'\longrightarrow S$.",f[0])
s=put(s,r'\inserted{des} préschémas',f[1])
s=put(s,r"\uline{Théorème} 2.-Soit $\alpha:S'\longrightarrow S$",f[2])
s=put(s,r'$X,Y$ deux préschémas',f[3])
s=put(s,r"$X',Y'$ leurs images inverses",f[4],True)
s=put(s,r'est \uline{exact}, i.e.',f[5])
s=put(s,r"sur $X',Y'$ (i.e.",f[6])
s=put(s,r'\uline{Lemme} 1.2.-',f[7],True)
s=put(s,r"\uline{Lemme} 1.2.- Soit $\alpha:S'\longrightarrow S$",f[8])
s=put(s,r"un $S'$-préschéma",f[9])
s=put(s,r"\uline{relativement à} $\alpha:S'\longrightarrow S$",f[10])
circle=r'\margin{\textcircled{$k$}}'
assert s.count(circle)==1
s=s.replace(circle+'\n','')
s=put(s,r"d'un corps \inserted{$k$}",circle+' '+f[11])
path.write_text(s)

path=root/'pages/MPL_57_089-132_57_scan111.tex'
s=path.read_text()
old=r'\draw (0,0)--(2.6,.08);'
assert s.count(old)==1
s=s.replace(old,old+r'\draw (2.7,1.8)--(2.72,-2.1);')
path.write_text(s)

stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for n in (111,117,119):
    p=root/f'records/scan{n:03d}.json'
    r=json.loads(p.read_text())
    r['audit']['notes'].append('Pre-freeze placement review '+stamp+(': added the visible vertical divider to the existing marginal separator figure.' if n==111 else ': moved existing proofreader-mark figure macros beside their visually recorded textual anchors; no words or mathematical readings changed.'))
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as stream:
    stream.write('pre-freeze drawing placement review '+stamp+'; scans111,117,119; existing marks moved to recorded anchors and vertical divider111 added\n')
print('Root placement corrections applied to111,117,119.')
