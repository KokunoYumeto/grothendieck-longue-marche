#!/usr/bin/env python3
"""Assemble the research report; never reads or writes the frozen transcription."""
from pathlib import Path
import re
base=Path(__file__).resolve().parents[1]
research=base/'research'
read=lambda f:(research/f).read_text()
root=read('root_notes.md')
level=root.split('## L.',1)[1].split('## T.',1)[0]
analytic=root.split('## T.',1)[1].split('## U.',1)[0]
standing='## U.'+root.split('## U.',1)[1]
arithmetic=read('arithmetic_checks.md')
anotes=arithmetic.split('## A01',1)[1].split('## L90',1)[0]
lnotes=arithmetic.split('## L90',1)[1].split('## Primary-source',1)[0]
b=read('modular_context.md').split('## B01',1)[1].split('## References',1)[0]
sh=read('connections_hua.md')
snotes=sh.split('## S.',1)[1].split('### Q3',1)[0]
hnotes=sh.split('## H.',1)[1].split('## Reproducible',1)[0]
demote=lambda x:re.sub(r'^## ([ABHL]\d\d)',r'### \1',x,flags=re.M)
parts=[
 read('notes_preface.md'),
 '## L.'+level,
 demote('## L90'+lnotes),
 '## T.'+analytic,
 '## B. Modular cusp and congruence levels\n\n'+demote('## B01'+b),
 '## S.'+snotes,
 '## A. Quadratic normality and arithmetic covers\n\n'
 'For A01–A09, the supplied register has no directly matching numbered normality theorem; '
 'these calculations provide local arithmetic background without settling LM4_SUCCESSOR B.38 or EXIT_TOWER E.24.\n\n'
 +demote('## A01'+anotes),
 '## H.'+hnotes,
 standing,
 read('notes_status.md'),
 read('REFERENCES.md').replace('# References and primary-source verification','## References and primary-source verification',1)
]
text='\n\n'.join(p.strip() for p in parts)+'\n'
# Presentation-only spacing in research prose, never in source transcription.
text=re.sub(r'\b(scan|scans|cote|page|pages|Proposition|Propositions|Theorem|Corollary|Remark|Lemma|Definition|Exposé|Exposés|Tag|Version)(?=\d)',r'\1 ',text)
text=re.sub(r'\b(pp?\.)(?=\d)',r'\1 ',text)
text=text.replace('the39','the 39').replace('through157','through 157').replace('from116','from 116')
text=text.replace('excluding122,130,142','excluding 122, 130, 142').replace('with1728','with 1728')
(base/'MPL_64_116-157_notes.md').write_text(text)
ids=re.findall(r'^### ([A-Z]\d\d)\b',text,re.M)
if len(ids)!=len(set(ids)):
    raise ValueError('Duplicate note identifiers')
print(f'Assembled {len(ids)} short notes; {len(text.split())} whitespace-delimited words; {len(text.encode())} bytes.')
print('IDs: '+', '.join(ids))

