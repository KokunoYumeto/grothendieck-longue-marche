"""Pre-freeze encoding repairs; no source readings supplied by this script."""
from pathlib import Path
import json, re
from record_page import ROOT, REC, utc, refresh

assert 'transcription frozen ' not in (ROOT/'progress.log').read_text()
changed=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
    old=p.read_text(); s=old
    s=re.sub(r'\\diagram\{(\\begin\{array\}[\s\S]*?\\end\{array\})\}',lambda m:'\\diagram{$'+m[1]+'$}',s)
    s=s.replace(r'\operatorname{Dér}',r'\operatorname{D\acute{e}r}')
    if 'scan037' in p.name:
        s=s.replace('\\begin{aligned}\n[','\\begin{aligned}\n\\relax[')
    if 'scan040' in p.name:
        s=s.replace('\\\\\n[D\\longrightarrow L]','\\\\\n\\relax[D\\longrightarrow L]')
    if 'scan042' in p.name:
        assert r'&&1\arrow[dr]&&&1' in s
        s=s.replace(r'&&1\arrow[dr]&&&1',r'&&1\arrow[dr]&&&&1')
    if 'scan046' in p.name:
        s=s.replace(r'\textcircled{$\beta$}',r'\text{\textcircled{$\beta$}}')
    def diagram(m):
        t=m[0]
        if t.startswith(r'\begin{tikzcd}['):
            t=t.replace(r'\begin{tikzcd}[',r'\begin{tikzcd}[ampersand replacement=\&,',1)
        else:
            t=t.replace(r'\begin{tikzcd}',r'\begin{tikzcd}[ampersand replacement=\&]',1)
        return re.sub(r'(?<!\\)&',r'\\&',t)
    s=re.sub(r'\\begin\{tikzcd\}[\s\S]*?\\end\{tikzcd\}',diagram,s)
    if s!=old:
        p.write_text(s)
        n=int(re.search(r'scan(\d+)',p.name)[1])
        r=REC/f'scan{n:03}.json'; d=json.loads(r.read_text()); d['tex']=s
        d.setdefault('amendments',[]).append({'utc':utc(),'kind':'LaTeX encoding','details':'Math guards, accent-safe operator encoding, optional-bracket disambiguation, and/or explicit tikz-cd ampersand replacement. Scan042 terminal cell repositioned after root image check.'})
        r.write_text(json.dumps(d,ensure_ascii=False,indent=2)); changed.append(n)
with (ROOT/'progress.log').open('a') as f:
    f.write('pre-freeze syntax repairs '+utc()+' scans '+','.join(f'{n:03}' for n in changed)+'\n')
with (REC/'audit.md').open('a') as f:
    f.write('\n## Pre-freeze encoding repairs — '+utc()+'\n\nReal TeX compilation identified four array environments lacking math guards, accented operator names, two optional-bracket ambiguities, and captured TikZ alignment tokens. Repaired these without changing readings. Used explicit ampersand replacement uniformly in tikz-cd diagrams. Root re-viewed scan042 and confirmed its upper-right terminal 1 is northeast of M; inserted the missing empty matrix cell. Circled beta in scan046 now has an explicit text context.\n')
refresh()
print('Updated scans:',','.join(f'{n:03}' for n in changed))
