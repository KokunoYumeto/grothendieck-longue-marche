from pathlib import Path
from datetime import datetime, timezone
import csv, re

ROOT = Path(__file__).resolve().parents[1]

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def macro_args(text, name):
    for m in re.finditer(r'\\'+name+r'\{', text):
        start=m.end(); depth=1; i=start
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'): depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'): depth-=1
            i+=1
        yield text.count('\n',0,m.start())+1, text[start:i-1]

def commit(scan, tex, elements, sheet_kind='text', observations=''):
    path=ROOT/'pages'/f'MPL_159_159_scan{scan:03}.tex'
    if path.exists():
        raise RuntimeError(f'Page already recorded: {scan}; edit explicitly for audit corrections')
    text=tex.strip()+'\n'
    if f'\\scanpage{{{scan}}}' not in text:
        raise ValueError('Missing scanpage marker')
    path.write_text(text)
    with (ROOT/'MPL_159_inventory.csv').open('a',newline='') as f:
        w=csv.writer(f)
        for i,(kind,pos,words) in enumerate(elements,1):
            w.writerow(['159',scan,sheet_kind,f'{scan:03}.{i:02}',kind,pos,words,'yes'])
    with (ROOT/'MPL_159_doubts.md').open('a') as f:
        for name in ['unsure','illegible']:
            for line,arg in macro_args(text,name):
                reading,sep,alt=arg.partition('|')
                if name=='illegible': reading=f'Unreadable: {arg} word(s)'; alt='No recoverable reading'; conf='low'
                else: conf='medium' if not sep else 'low'
                safe=lambda s:s.replace('|','\\|').replace('\n',' ')
                f.write(f'| 159 | {scan} | TeX line {line} | `{safe(reading)}` | {safe(alt) if alt else "Unresolved; no secure alternative"} | {conf} |\n')
    if observations:
        with (ROOT/'reading_observations.md').open('a') as f:
            f.write(f'\n## Scan {scan:03}\n\n{observations.strip()}\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'159 scan {scan:03} done {utc()}\n')
    print(f'159 scan {scan:03} saved; {len(elements)} inventoried elements')
