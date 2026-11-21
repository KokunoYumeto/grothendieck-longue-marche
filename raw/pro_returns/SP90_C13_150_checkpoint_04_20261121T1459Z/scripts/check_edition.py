"""Structural and audit-record checks only; never a substitute for visual reading."""
from pathlib import Path
import csv, json, re, hashlib, argparse

ROOT=Path(__file__).resolve().parents[1]
EXPECTED=list(range(25,34))+list(range(36,52))

def escaped(s,i):
    n=0;i-=1
    while i>=0 and s[i]=='\\': n+=1;i-=1
    return n%2==1

def check_tex(text):
    stack=[]; errors=[]
    # Comments are removed without touching escaped percent signs.
    cleaned='\n'.join(re.split(r'(?<!\\)%',line)[0] for line in text.splitlines())
    for i,ch in enumerate(cleaned):
        if ch=='{' and not escaped(cleaned,i): stack.append(i)
        if ch=='}' and not escaped(cleaned,i):
            if stack: stack.pop()
            else: errors.append('unmatched closing brace')
    if stack: errors.append(f'{len(stack)} unmatched opening braces')
    env=[]
    for verb,name in re.findall(r'\\(begin|end)\{([^}]+)\}',cleaned):
        if verb=='begin':env.append(name)
        elif not env or env.pop()!=name:errors.append('environment mismatch: '+name)
    if env:errors.append('unclosed environments: '+str(env))
    return errors

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');a=parser.parse_args()
    issues=[]; statistics={}; pages=sorted((ROOT/'pages').glob('150_scan*.tex'))
    scans=[int(p.stem[-3:]) for p in pages]
    if a.final and scans!=EXPECTED:issues.append('Expected all 25 scans; found '+str(scans))
    for p in pages:
        for e in check_tex(p.read_text()):issues.append(p.name+': '+e)
        if f'\\scanpage{{{int(p.stem[-3:])}}}' not in p.read_text():issues.append(p.name+': missing correct scanpage')
    for p in sorted((ROOT/'editor').glob('150_scan*.json')):
        d=json.loads(p.read_text());s=d['scan']
        for c in d.get('changes',[]):
            if c.get('crop') and c['crop']!='page' and not (ROOT/'crops'/c['crop']).exists():issues.append(f'{s}: missing crop {c["crop"]}')
            if c.get('confidence') not in ['high','medium','low']:issues.append(f'{s}: invalid confidence')
            if c.get('crop') and c.get('box'):
                sidecar=(ROOT/'crops'/c['crop']).with_suffix('.json')
                if sidecar.exists():
                    crop_meta=json.loads(sidecar.read_text())
                    original_box=crop_meta.get('box',crop_meta.get('original_box'))
                    if original_box is not None and list(c['box'])!=list(original_box):
                        issues.append(f'{s}: change coordinates disagree with crop metadata: '+c['crop'])
        for x in d.get('inventory',[]):
            if x.get('transcribed')!='yes':issues.append(f'{s}: inventory element not transcribed: '+x.get('element','?'))
            if x.get('kind') not in ['text','display','diagram','drawing','margin note','insertion','deletion']:
                issues.append(f'{s}: invalid inventory kind: '+str(x.get('kind')))
        ids=[b['box'] for b in d.get('second_boxes',[])]
        if len(ids)!=len(set(ids)):issues.append(f'{s}: duplicate audit box ids')
        for b in d.get('second_boxes',[]):
            if len(b['coords'])!=4 or b['coords'][2]<=b['coords'][0] or b['coords'][3]<=b['coords'][1]:issues.append(f'{s}: invalid box '+b['box'])
        if a.final:
            files={k:ROOT/'second'/f'150_scan{s:03}_{k}.tsv' for k in ['boxes','first','second','comparison']}
            for k,f in files.items():
                if not f.exists():issues.append(f'{s}: missing second-pass {k}')
            if all(files[k].exists() for k in ['boxes','first','second']):
                box_ids=[]
                for k in ['boxes','first','second']:
                    with files[k].open() as h:box_ids.append([x['box'] for x in csv.DictReader(h,delimiter='\t')])
                if box_ids[0]!=box_ids[1] or set(box_ids[0])!=set(box_ids[2]):issues.append(f'{s}: second reading box correspondence mismatch')
            if files['comparison'].exists():
                with files['comparison'].open() as h:
                    compared=list(csv.DictReader(h,delimiter='\t'))
                if [x['box'] for x in compared]!=ids:issues.append(f'{s}: comparison box correspondence mismatch')
                for x in compared:
                    if x['different']=='yes':
                        for field in ['adjudicated_reading','decision','evidence','crop']:
                            if not x.get(field):issues.append(f'{s}: unadjudicated difference {x["box"]}: '+field)
                        if x.get('crop') and not (ROOT/'crops'/x['crop']).exists():
                            issues.append(f'{s}: missing audit evidence crop: '+x['crop'])
    with (ROOT/'decisions.tsv').open() as h: decisions=list(csv.DictReader(h,delimiter='\t'))
    with (ROOT.parent/'source/SP90_C13_150_texts/MARKS.tsv').open() as h: originals=list(csv.DictReader(h,delimiter='\t'))
    wanted=[x['id'] for x in originals if int(x['scan']) in scans]
    if [x['id'] for x in decisions]!=wanted:issues.append('Decision rows do not exactly follow the source MARKS order')
    for d in decisions:
        if d['decision']!='undecided' and (d['crop']=='page' or not d['crop']):issues.append(d['id']+': resolved doubt lacks crop')
    if a.final and len(decisions)!=195:issues.append('Final mark count is not 195')
    combined=(ROOT/'SP90_C13_150_transcription.tex').read_text()
    intended='\\cotefile{150}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n'
    if combined!=intended:issues.append('Combined transcription differs from page concatenation')
    statistics={'pages':len(pages),'decisions':len(decisions),'crops':len(list((ROOT/'crops').glob('*.jpg'))),'issues':issues}
    print(json.dumps(statistics,ensure_ascii=False,indent=2))
    if issues:raise SystemExit(1)

if __name__=='__main__':main()
