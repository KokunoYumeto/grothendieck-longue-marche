"""Structural checks only; no OCR, external research or TeX compilation."""
from pathlib import Path
import csv
import json
import re
import sys

ROOT = Path('/workspace/scratch/b8c6ff258063')
WORK = ROOT/'SP87_C13_149_work'
SOURCE = ROOT/'source'
EXPECTED = list(range(79,99))+[100,101,102]
KINDS = {'misread word','misread symbol or index','omission','text not on the page',
         'deletion state','insertion or placement','abbreviation expanded or spelling modernised',
         r'readable ink left as \ill{}','drawing or diagram','other'}
EVENTS = {'targeted proof check','independent re-proof','computation or formal certificate',
          'used and rechecked in this run','carried as background without fault found','refuted'}
SHEETS = {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
INKINDS = {'text','display','diagram','drawing','margin note','insertion','deletion'}

def rows(path, delimiter='\t'):
    return list(csv.DictReader(path.open(), delimiter=delimiter))

def main():
    final = '--final' in sys.argv
    errs=[]
    reports=[json.loads(p.read_text()) for p in sorted((WORK/'review').glob('149_scan*_reviewed.json'))]
    seen=[r['scan'] for r in reports]
    if final and seen != EXPECTED:errs.append(f'Page coverage: {seen}')
    source_marks=rows(SOURCE/'SP87_C13_149_texts/MARKS.tsv')
    all_mark_ids=[]
    for r in reports:
        s=r['scan']; page=f'149_scan{s:03d}'
        tex=(WORK/'pages'/f'{page}.tex').read_text()
        # Deliberately do not require balanced manuscript punctuation.
        lexical=re.sub(r'(?<!\\)%[^\n]*','',tex)
        depth=0
        for token in re.findall(r'\\[{}]|[{}]',lexical):
            if token=='{':depth+=1
            elif token=='}':depth-=1
            if depth<0:errs.append(f'{s}: closing TeX brace without opening');break
        if depth:errs.append(f'{s}: TeX brace balance {depth}')
        if re.search(r'\\\[\s*\\diagram',tex):errs.append(f'{s}: paragraph diagram macro inside display math')
        if tex.count(f'\\scanpage{{{s}}}')!=1:errs.append(f'{s}: scan marker missing or duplicated')
        for c in r['changes']:
            if c['kind'] not in KINDS:errs.append(f'{s}/{c["place"]}: kind {c["kind"]}')
            if c['confidence'] not in {'high','medium','low'}:errs.append(f'{s}: confidence')
            if c.get('crop') and not (WORK/c['crop']).is_file():errs.append(f'{s}: missing {c["crop"]}')
            if not(c.get('against_c') or c.get('against_h')):errs.append(f'{s}/{c["place"]}: non-difference row')
        actual=[m['id'] for m in r['marks']]
        expected=[m['id'] for m in source_marks if int(m['scan'])==s]
        if actual!=expected:errs.append(f'{s}: marks {actual} != {expected}')
        all_mark_ids.extend(actual)
        for m in r['marks']:
            if m['decision'] not in {'first','alternative','other','undecided'}:errs.append(f'{s}: decision')
            if m['decision']!='undecided' and not m.get('crop'):errs.append(f'{s}/{m["id"]}: resolved without crop')
        for x in r['inventory']:
            if x['sheet_kind'] not in SHEETS or x['kind'] not in INKINDS or x['transcribed']!='yes':
                errs.append(f'{s}: inventory vocabulary or coverage')
        for e in r.get('check_events',[]):
            if e['type'] not in EVENTS:errs.append(f'{s}: check-event type {e["type"]}')
        packet=json.loads((WORK/'readers'/page/'input.json').read_text())
        expected_d=[d['diff_id'] for d in packet['differences']]
        actual_d=[d['diff_id'] for d in r.get('diff_coverage',[])]
        if sorted(actual_d)!=sorted(expected_d) or len(set(actual_d))!=len(actual_d):errs.append(f'{s}: diff coverage')
        boxes=rows(WORK/'second'/f'{page}_boxes.tsv')
        first=rows(WORK/'second'/f'{page}_first.tsv')
        if [b['box'] for b in boxes]!=[b['box'] for b in first]:errs.append(f'{s}: first-box coverage')
        width,height=packet['size']
        for b in boxes:
            x0,y0,x1,y1=[int(b[k]) for k in ('x0','y0','x1','y1')]
            if not(0<=x0<x1<=width and 0<=y0<y1<=height):errs.append(f'{s}/{b["box"]}: out-of-bounds box')
        if final:
            secondpath=WORK/'second'/f'{page}_second.tsv'
            if not secondpath.exists():errs.append(f'{s}: missing second reading')
            elif [b['box'] for b in boxes]!=[b['box'] for b in rows(secondpath)]:errs.append(f'{s}: second-box coverage')
            if not (WORK/'second'/f'{page}_adjudications.tsv').exists():errs.append(f'{s}: missing adjudications')
    decisions=rows(WORK/'decisions.tsv')
    expected_order=[m['id'] for m in source_marks if int(m['scan']) in seen]
    if [m['id'] for m in decisions]!=expected_order:errs.append('Global decisions order/coverage')
    combined='\\cotefile{149}\n\n'+'\n\n'.join((WORK/'pages'/f'149_scan{s:03d}.tex').read_text().rstrip() for s in seen)+'\n'
    if combined!=(WORK/'SP87_C13_149_transcription.tex').read_text():errs.append('Combined text does not match pages')
    print(json.dumps({'mode':'final' if final else 'partial','pages':len(seen),
                      'marks':len(decisions),'errors':errs},ensure_ascii=False))
    raise SystemExit(bool(errs))

if __name__=='__main__':main()
