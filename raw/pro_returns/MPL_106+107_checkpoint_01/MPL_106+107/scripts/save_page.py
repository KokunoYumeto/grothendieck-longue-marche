from pathlib import Path
from datetime import datetime, timezone
import csv,re,json
ROOT=Path(__file__).resolve().parents[1]
BASE='MPL_106+107'

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def macro_values(text,name):
    pat='\\'+name+'{'; start=0
    while (i:=text.find(pat,start))>=0:
        j=i+len(pat); depth=1; k=j
        while k<len(text) and depth:
            if text[k]=='{' and (k==0 or text[k-1]!='\\'): depth+=1
            elif text[k]=='}' and (k==0 or text[k-1]!='\\'): depth-=1
            k+=1
        yield text.count('\n',0,i)+1,text[j:k-1]
        start=k

def save(cote,scan,tex,elements,kind='text',notes=''):
    page=ROOT/'pages'/f'{BASE}_{cote}_scan{scan:03}.tex'
    if page.exists(): raise RuntimeError('Page already saved; revise explicitly before freeze')
    prefix=(f'\\cotefile{{{cote}}}\n' if scan==2 else '')+f'\\scanpage{{{scan}}}\n'
    body=prefix+tex.strip()+'\n'
    page.write_text(body)
    inv=ROOT/f'{BASE}_inventory.csv'
    fresh=not inv.exists()
    with inv.open('a',newline='') as f:
        w=csv.writer(f)
        if fresh:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        count=0
        for el in elements:
            count+=1;w.writerow([cote,scan,kind,f'{count:03}',*el,'yes'])
        for macro,typ in [('deleted','deletion'),('inserted','insertion'),('margin','margin note')]:
            for line,value in macro_values(body,macro):
                count+=1;w.writerow([cote,scan,kind,f'{count:03}',typ,f'tex line {line}',value,'yes'])
    d=ROOT/'records/doubts.jsonl'; d.parent.mkdir(exist_ok=True)
    with d.open('a') as f:
        for macro in ['unsure','illegible']:
            for line,value in macro_values(body,macro):
                parts=value.split('|',1)
                f.write(json.dumps(dict(cote=cote,scan=scan,line=line,reading=parts[0],alternative=parts[1] if len(parts)>1 else '',confidence='low' if macro=='illegible' or len(value)>65 else 'medium',macro=macro),ensure_ascii=False)+'\n')
    if notes:
        with (ROOT/'records/manuscript_leads.md').open('a') as f:f.write(f'\n## {cote}, scan {scan:03}\n\n'+notes.strip()+'\n')
    with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03} done {now()}\n')
    (ROOT/f'{BASE}_transcription.tex').write_text('\n'.join(p.read_text() for p in sorted((ROOT/'pages').glob('*.tex'))))
    update_doubts()
    print(f'Saved {page.name}: {len(body)} characters, {count} inventory elements. {now()}')
    started=datetime.strptime((ROOT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    elapsed=(datetime.now(timezone.utc)-started).total_seconds()
    saved=len(list(ROOT.parent.glob('MPL_106+107_checkpoint_*.zip')))
    if elapsed//3600>saved:print('HOURLY CHECKPOINT DUE')

def update_doubts():
    notation=(ROOT/'records/notation.md').read_text()
    rows=[]
    p=ROOT/'records/doubts.jsonl'
    if p.exists():
        for l in p.read_text().splitlines():
            r=json.loads(l); esc=lambda s:s.replace('|','\\|').replace('\n',' ')
            rows.append(f"| {r['cote']} | {r['scan']:03} | TeX {r['line']} | `{esc(r['reading'])}` | {esc(r['alternative']) or 'Unresolved; no secure alternative'} | {r['confidence']} |")
    (ROOT/f'{BASE}_doubts.md').write_text(notation+'\n\n## Reading doubts\n\nLocations use the approximate line in the corresponding page fragment, not a reconstructed manuscript line.\n\n| File | Scan | Approximate line | Reading | Alternatives | Confidence |\n|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n\n## Legibility and limits\n\nProvisional during transcription. Rapid cursive, cancelled labels, overlapping arrows, and marginal additions require particular caution. Every doubt in the fragments is recorded above; a marked reading is a proposed reading of the ink, not a mathematical correction.\n')
