#!/usr/bin/env python3
"""Pre-freeze TeX syntax repair: protect tikz-cd separators in macro arguments.

All affected matrices were inspected for nested alignment environments first.
No object, label, arrow, formula, or manuscript reading is changed.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
assert "transcription frozen " not in (ROOT/"progress.log").read_text(), "Transcription is frozen."
count=0
for p in sorted((ROOT/'pages').glob('*.tex')):
    old=p.read_text()
    def repair(m):
        global count
        s=m.group()
        if 'ampersand replacement' in s: return s
        assert len(re.findall(r'\\begin\{',s))==1
        s=re.sub(r'(?<!\\)&',r'\\&',s)
        if s.startswith(r'\begin{tikzcd}['):
            s=s.replace(r'\begin{tikzcd}[',r'\begin{tikzcd}[ampersand replacement=\&,',1)
        else:
            s=s.replace(r'\begin{tikzcd}',r'\begin{tikzcd}[ampersand replacement=\&]',1)
        count+=1
        return s
    new=re.sub(r'\\begin\{tikzcd\}(?:\[[^\]]*\])?[\s\S]*?\\end\{tikzcd\}',repair,old)
    if new!=old: p.write_text(new)
(ROOT/'MPL_138_001-045_transcription.tex').write_text('\n'.join(p.read_text().rstrip()+'\n' for p in sorted((ROOT/'pages').glob('*.tex'))))
print('Encoded',count,'tikz-cd matrices for macro-argument use.')
