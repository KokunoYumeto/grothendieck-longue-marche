from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_15_170-194r'

def args(text, command):
    token='\\'+command+'{'
    start=0
    while (idx:=text.find(token,start))>=0:
        a=idx+len(token); end=a; depth=1
        while end<len(text) and depth:
            if text[end]=='{': depth+=1
            elif text[end]=='}': depth-=1
            end+=1
        yield idx,text[a:end-1]
        start=a

out=['# Notation concordance and doubts\n\n', (ROOT/'records/notation.md').read_text(),
     '\n## Reading doubts\n\nEvery explicit uncertainty in the page fragments is indexed below. “TeX line” identifies its exact line in the individual page file; the accompanying third of the text is an approximate location, not a claim about original manuscript line numbering. Alternatives are competing readings, not corrections. Confidence concerns the first reading.\n\n',
     '| File | Scan | Approximate position / fragment line | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n']
for p in sorted((ROOT/'pages').glob('*.tex')):
    text=p.read_text(); scan=re.search(r'scan(\d+)',p.name).group(1)
    for idx,a in args(text,'unsure'):
        alts=a.split('|',1); reading=alts[0]; alt=alts[1] if len(alts)>1 else '—'
        line=text[:idx].count('\n')+1
        pos=['upper','middle','lower'][min(2,int(3*idx/max(1,len(text))))]
        confidence='low' if len(alts)>1 or len(reading.split())>3 or reading in {'présentiques','groupes','définis','finitude','a priori','quelconque','tore','ch','En une descente','élégante.','tordu','magnifiées','le problème','galoisien','fonctoriello-catégoriques'} else 'medium'
        reading=reading.replace('\n',' ').replace('|','\\|')
        alt=alt.replace('\n',' ').replace('|','\\|')
        out.append(f'| 15 | {scan} | {pos}; TeX line {line} | `{reading}` | `{alt}` | {confidence} |\n')
out.append((ROOT/'records/abbreviations_and_legibility.md').read_text())
(ROOT/f'{PREFIX}_doubts.md').write_text(''.join(out))
print('Doubts index refreshed from',len(list((ROOT/'pages').glob('*.tex'))),'pages.')
