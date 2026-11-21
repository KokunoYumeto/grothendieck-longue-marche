"""Structural and accounting checks. This does not validate ink readings."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re
from PIL import Image

ROOT = Path('/workspace/scratch/d12e26a9cd50')
OUT = ROOT/'SP93_C13_151_work'
SRC = ROOT/'source'
CHANGE_KINDS = {'misread word','misread symbol or index','omission','text not on the page','deletion state',
    'insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
CHECK_TYPES = {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run',
    'carried as background without fault found',"refuted, with the refined statement's id"}
SHEET_KINDS = {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}

def read_tsv(path, quoting=csv.QUOTE_MINIMAL):
    with path.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t', quoting=quoting))

def main(complete=False, audited=False):
    errors, warnings = [], []
    source_pages = sorted(p.stem for p in (SRC/'SP93_C13_151_texts/pages').glob('*.tex'))
    final_pages = sorted(p.stem for p in (OUT/'pages').glob('*.tex'))
    if complete and final_pages != source_pages:
        errors.append(f'Page set differs: missing {sorted(set(source_pages)-set(final_pages))}')
    marks = read_tsv(SRC/'SP93_C13_151_texts/MARKS.tsv')
    all_diffs = read_tsv(SRC/'SP93_C13_151_C_H_differences.tsv',csv.QUOTE_NONE)
    actual_decisions=[]
    for name in final_pages:
        scan = int(name[-3:])
        p = OUT/'reviews'/f'{name}.json'
        if not p.exists(): errors.append(f'{name}: no reviewed report'); continue
        r = json.loads(p.read_text())
        if not r.get('root_reviewed'): errors.append(f'{name}: lacks main-reader review')
        if r.get('sheet_kind') not in SHEET_KINDS: errors.append(f'{name}: invalid sheet kind')
        for c in r.get('changes',[]):
            if c.get('kind') not in CHANGE_KINDS: errors.append(f"{name}/{c.get('id')}: invalid change kind {c.get('kind')}")
            if not c.get('differs_C') and not c.get('differs_H'): errors.append(f"{name}/{c.get('id')}: counted row has no witness departure")
        ids=[c.get('id') for c in r.get('changes',[])]
        if len(ids)!=len(set(ids)): errors.append(f'{name}: duplicate change IDs')
        for c in r.get('check_events',[]):
            if c.get('type') not in CHECK_TYPES: errors.append(f"{name}: invalid check-event type {c.get('type')}")
        expected_marks = [m['id'] for m in marks if int(m['scan'])==scan]
        got_marks = [d['id'] for d in r['decisions']]
        if got_marks != expected_marks: errors.append(f'{name}: mark order/set {got_marks} != {expected_marks}')
        actual_decisions += got_marks
        expected_diffs = [f'D{i:04d}' for i,d in enumerate(all_diffs,1) if d['page']==name]
        got_diffs = [d.get('id') for d in r.get('difference_coverage',[])]
        if any(not isinstance(x,str) for x in got_diffs) or sorted(got_diffs)!=sorted(expected_diffs): errors.append(f'{name}: supplied difference coverage mismatch')
        size = Image.open(SRC/'SP93_C13_151_scans'/f'{name}.jpg').size
        for collection in ['changes','decisions']:
            for row in r[collection]:
                loc=f"{name}/{collection}/{row.get('id','?')}"
                if row.get('confidence') not in ['high','medium','low']: errors.append(loc+': bad confidence')
                crop=row.get('crop')
                if crop and crop!='page' and not (OUT/crop).is_file(): errors.append(loc+': missing crop '+str(crop))
                box=row.get('box')
                if isinstance(box,list) and not (len(box)==4 and 0<=box[0]<box[2]<=size[0] and 0<=box[1]<box[3]<=size[1]): errors.append(loc+': invalid box')
                if collection=='decisions':
                    if row.get('decision') not in ['first','alternative','other','undecided']: errors.append(loc+': bad decision')
                    if row.get('decision')!='undecided' and (not crop or crop=='page' or not isinstance(box,list)): errors.append(loc+': resolved mark without crop and box')
        for row in r['inventory']:
            if row.get('transcribed')!='yes': errors.append(f'{name}: inventory not transcribed: {row}')
            if row.get('kind') not in {'text','display','diagram','drawing','margin note','insertion','deletion'}: errors.append(f'{name}: invalid inventory kind')
        bpath=OUT/'second'/f'{name}_boxes.tsv'
        fpath=OUT/'second'/f'{name}_first.tsv'
        if not bpath.exists() or not fpath.exists(): errors.append(f'{name}: missing prepared second-reading files'); continue
        boxes=read_tsv(bpath); first=read_tsv(fpath)
        if [x['box'] for x in boxes]!=[x['box'] for x in first]: errors.append(f'{name}: first-reading box IDs mismatch')
        for b in boxes:
            x0,y0,x1,y1=[int(b[k]) for k in ['x0','y0','x1','y1']]
            if not(0<=x0<x1<=size[0] and 0<=y0<y1<=size[1]): errors.append(f"{name}: invalid second box {b['box']}")
        if audited:
            spath=OUT/'second'/f'{name}_second.tsv'
            if not spath.exists(): errors.append(f'{name}: no blind second reading')
            elif [x['box'] for x in read_tsv(spath)]!=[x['box'] for x in boxes]: errors.append(f'{name}: second-reading box IDs mismatch')
            if not r.get('second_audit_complete'): errors.append(f'{name}: second audit not adjudicated')
        text=(OUT/'pages'/f'{name}.tex').read_text()
        if f'\\scanpage{{{scan}}}' not in text: errors.append(f'{name}: scan marker absent')
        clean=re.sub(r'(?<!\\)%[^\n]*','',text)
        stack=[]
        for m in re.finditer(r'(?<!\\)[{}]',clean):
            if m[0]=='{': stack.append(m.start())
            elif stack: stack.pop()
            else: errors.append(f'{name}: unmatched closing brace at {m.start()}')
        if stack: errors.append(f'{name}: unmatched opening braces: {stack}')
        environments=[]
        for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
            action,environment=m.groups()
            if action=='begin': environments.append(environment)
            elif not environments or environments.pop()!=environment: errors.append(f'{name}: mismatched environment end {environment}')
        if environments: errors.append(f'{name}: unclosed environments {environments}')
        dollars=0
        for m in re.finditer(r'\$',clean):
            preceding=0; i=m.start()-1
            while i>=0 and clean[i]=='\\': preceding+=1; i-=1
            if preceding%2==0: dollars+=1
        if dollars%2: errors.append(f'{name}: odd number of unescaped dollar delimiters')
        if re.search(r'\\begin\{document\}|\\documentclass',clean): errors.append(f'{name}: not a LaTeX fragment')
    if complete and actual_decisions != [m['id'] for m in marks]: errors.append('Consolidated MARKS order/count mismatch')
    manifest=OUT/'second/first_reading_manifest.json'
    if audited:
        if not manifest.exists(): errors.append('Missing pre-blind first-reading manifest')
        else:
            for name,expected in json.loads(manifest.read_text())['sha256'].items():
                p=OUT/'second'/name
                if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected: errors.append('First reading or blind box list changed: '+name)
    result={'pages_checked':len(final_pages),'marks_checked':len(actual_decisions),'errors':errors,'warnings':warnings}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--complete',action='store_true'); p.add_argument('--audited',action='store_true')
    a=p.parse_args(); raise SystemExit(main(a.complete,a.audited))
