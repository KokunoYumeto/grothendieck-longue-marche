from pathlib import Path
from datetime import datetime, timezone
import csv, re, json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_098-146'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def extract_doubts(text):
    result=[]
    for m in re.finditer(r'\\unsure\{',text):
        start=m.end(); depth=1; i=start
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'): depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'): depth-=1
            i+=1
        raw=text[start:i-1]
        first,sep,other=raw.partition('|')
        result.append({'line':text[:m.start()].count('\n')+1,'reading':first,'alternative':other if sep else 'No secure alternative','confidence':'medium'})
    for m in re.finditer(r'\\illegible\{([^}]+)\}',text):
        result.append({'line':text[:m.start()].count('\n')+1,'reading':'illegible{'+m.group(1)+'}','alternative':'Physically obscured or unresolved strokes after enlargement','confidence':'low'})
    return result

def save(scan, text, elements, notes='', sheet_kind='text'):
    path=ROOT/'pages'/f'{PREFIX}_33_scan{scan:03d}.tex'
    if path.exists(): raise RuntimeError('Use an explicit edit for an existing page; save() never overwrites.')
    assert f'\\scanpage{{{scan}}}' in text
    path.write_text(text.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    existed=inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        if not existed: writer.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,position,words) in enumerate(elements,1):
            writer.writerow(['33',scan,sheet_kind,f'{scan:03d}.{i:02d}',kind,position,words,'yes'])
    (ROOT/'records'/f'doubts_{scan:03d}.json').write_text(json.dumps(extract_doubts(text),ensure_ascii=False,indent=2)+'\n')
    if notes:
        with (ROOT/'records'/'manuscript_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan}\n\n{notes}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'33 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(elements)} inventory elements; {len(extract_doubts(text))} doubt marks.')

