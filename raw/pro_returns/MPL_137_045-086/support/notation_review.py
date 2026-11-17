"""Root's pre-context notation decisions, after direct comparison of the ink.

This does not recognize text or images. It applies only the explicitly recorded
typographic uncertainty decisions made by the single manuscript reader.
"""
from pathlib import Path
import json, re
from record import ROOT, PREFIX, rebuild, log, now

if 'transcription frozen ' in (ROOT/'progress.log').read_text():
    raise RuntimeError('Transcription is frozen.')

changes=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
    scan=int(re.search(r'scan(\d+)',p.name).group(1))
    old=p.read_text()
    new=old
    if scan==45:
        needle=r'\unsure{K}(x)'
        assert new.count(needle)==2
        new=new.replace(needle,r'\unsure{K^\bullet|K}(x)',1)
        new=new.replace(needle,r'\unsure{K|K^\bullet}(x)',1)
    if scan>=49:
        # The same looped capital occurs in both the exact-category and
        # polynomial-category passages; the ink does not securely distinguish
        # ordinary from calligraphic P. Do not encode an unmarked distinction.
        new=re.sub(r'\\mathcal\s*\{P\}|\\mathcal\s+P', '\u2118',new)
        new=re.sub(r'(?<![A-Za-z\\])P(?![A-Za-z])', '\u2118',new)
        new=new.replace('\u2118',r'\unsure{\mathcal P|P}')
    if new!=old:
        p.write_text(new)
        changes.append({'scan':scan,'old':old,'new':new})

(ROOT/'support/notation_changes.json').write_text(json.dumps(
    {'time':now(),'basis':'Direct cross-page ink comparison before context; explicit font and degree-dot doubts, no mathematical restoration.',
     'changes':changes},ensure_ascii=False,indent=2)+'\n')
rebuild()
log('Cross-page notation comparison completed; looped category P marked consistently as calligraphic/plain alternative; scan045 K degree-dot doubts explicit; Phi/Psi, stars/dots, rho/sigma, delta/beta, e/gamma, primes and quotation strokes reviewed')
print('Notation decisions applied to',len(changes),'page fragments.')
